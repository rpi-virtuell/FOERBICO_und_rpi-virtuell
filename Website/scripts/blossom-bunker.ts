#!/usr/bin/env -S deno run -A
/**
 * blossom-bunker — Gegenstück zu md2blossom mit dem FOERBICO-Key
 *
 * md2blossom hasht, schreibt index.md um und legt unsignierte kind:1063-Vorlagen
 * ab, hat aber keinen Key. Dieses Skript übernimmt die beiden Schritte, die den
 * Key brauchen, über den NIP-46-Bunker (derselbe wie in der CI, mdparser/.env):
 *
 *   upload  <post-dir>     Bilddateien per BUD-01 (kind:24242) nach Blossom,
 *                          Hash der Antwort wird gegen die Datei geprüft;
 *                          vorhandene Blobs werden übersprungen.
 *   publish <_nostr-dir>   <slug>.1063.<hash8>.json signieren, auf die
 *                          Lizenz-Relays publizieren, .signed.json daneben ablegen.
 *
 * Aufruf (aus Website/scripts/, Tasks in deno.json, .env liegt in ../../../mdparser/):
 *   deno task upload  ../content/de/posts/<post>
 *   node md2blossom.mjs ../content/de/posts/<post> --write
 *   deno task publish ../_nostr/<post>
 *
 * Reihenfolge je Beitrag: upload → md2blossom --write → publish → Commit von
 * index.md. Den 30023 publiziert die CI (mdparser/sync) nach dem Merge auf main.
 *
 * Braucht in der .env: BUNKER_URL, CLIENT_SECRET_HEX (feste Client-Identität,
 * sonst fragt Amber jeden Lauf neu), optional AUTHOR_PUBKEY_HEX als Soll-Wert.
 * Kein Key im Skript, keine Ausgabe von Secrets. deno.json setzt
 * nodeModulesDir: none, damit Deno die npm-Pakete nicht im node_modules von
 * md2blossom sucht.
 */
import { NostrConnectSigner, SimpleSigner } from 'npm:applesauce-signers@^2.0.0'
import { RelayPool } from 'npm:applesauce-relay@^2.0.0'
import { encodeHex } from 'jsr:@std/encoding@^1.0.5/hex'
import { extname, join } from 'jsr:@std/path@^1.0.8'

const BLOSSOM = 'https://blossom.edufeed.org'
// Wie foerbico-editor (nostr.js) und der Hub: hier liegen die Nachweise.
const LICENSE_RELAYS = ['wss://relay-rpi.edufeed.org/', 'wss://relay.edufeed.org/']
const MIME: Record<string, string> = {
  '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png', '.gif': 'image/gif',
  '.webp': 'image/webp', '.svg': 'image/svg+xml', '.avif': 'image/avif',
}

type Unsigned = { kind: number; pubkey: string; created_at: number; tags: string[][]; content: string }
type Signed = Unsigned & { id: string; sig: string }

const [cmd, dir] = Deno.args
if (!['upload', 'publish'].includes(cmd) || !dir) {
  console.error('Aufruf: blossom-bunker.ts upload <post-dir> | publish <_nostr-dir>')
  Deno.exit(2)
}

// ---------- Bunker (wie mdparser/sync/core/signer.ts) ----------
const bunkerUrl = Deno.env.get('BUNKER_URL')
const clientSecretHex = Deno.env.get('CLIENT_SECRET_HEX')
const soll = Deno.env.get('AUTHOR_PUBKEY_HEX')
if (!bunkerUrl) { console.error('BUNKER_URL fehlt (--env-file=<mdparser>/.env)'); Deno.exit(1) }

const pool = new RelayPool()
NostrConnectSigner.subscriptionMethod = (relays, filters) => pool.req(relays, filters)
NostrConnectSigner.publishMethod = (relays, event) => pool.event(relays, event)

// Amber antwortet bei erneutem connect oft mit „already connected" — unschädlich.
const benign = (msg: string) => /already connected|no permission/i.test(msg)
globalThis.addEventListener('unhandledrejection', (e) => {
  const msg = e.reason instanceof Error ? e.reason.message : String(e.reason)
  if (benign(msg)) e.preventDefault()
})
function mitTimeout<T>(p: Promise<T>, ms: number, was: string): Promise<T> {
  let t: number | undefined
  const timeout = new Promise<never>((_, rej) => { t = setTimeout(() => rej(new Error(`${was}: Timeout nach ${ms / 1000}s`)), ms) })
  return Promise.race([p, timeout]).finally(() => clearTimeout(t))
}

const { remote, relays, secret } = NostrConnectSigner.parseBunkerURI(bunkerUrl)
const signer = new NostrConnectSigner({
  relays, remote, signer: clientSecretHex ? SimpleSigner.fromKey(clientSecretHex) : undefined,
})
console.log(`Bunker: ${remote.slice(0, 8)}… über ${relays.length} Relay(s)`)
try {
  await mitTimeout(signer.connect(secret), 60_000, 'Bunker connect')
} catch (err) {
  const msg = err instanceof Error ? err.message : String(err)
  if (!benign(msg)) throw err
  await signer.open()
  ;(signer as unknown as { isConnected: boolean }).isConnected = true
}
const pubkey = await mitTimeout(signer.getPublicKey(), 30_000, 'Bunker getPublicKey')
if (soll && pubkey !== soll) { console.error(`Bunker-Pubkey ${pubkey.slice(0, 8)}… ≠ AUTHOR_PUBKEY_HEX`); Deno.exit(1) }
console.log(`Key:    ${pubkey.slice(0, 8)}… (Amber muss ggf. freigeben)`)

const jetzt = () => Math.floor(Date.now() / 1000)
const signieren = (ev: Unsigned) => mitTimeout(signer.signEvent(ev), 60_000, `Signatur kind:${ev.kind}`) as Promise<Signed>

// ---------- Relay-Publish (rohes WebSocket, wie foerbico-editor) ----------
function anRelay(url: string, ev: Signed, ms = 10_000): Promise<{ url: string; ok: boolean; msg: string }> {
  return new Promise((resolve) => {
    const ws = new WebSocket(url)
    const fertig = (ok: boolean, msg: string) => { clearTimeout(t); try { ws.close() } catch { /* egal */ } resolve({ url, ok, msg }) }
    const t = setTimeout(() => fertig(false, 'Timeout'), ms)
    ws.onopen = () => ws.send(JSON.stringify(['EVENT', ev]))
    ws.onmessage = (m) => {
      const d = JSON.parse(String(m.data))
      if (d[0] === 'OK' && d[1] === ev.id) fertig(Boolean(d[2]), d[3] ?? '')
      if (d[0] === 'NOTICE') fertig(false, String(d[1]))
    }
    ws.onerror = () => fertig(false, 'Verbindungsfehler')
  })
}

// ---------- upload ----------
if (cmd === 'upload') {
  let n = 0
  for await (const e of Deno.readDir(dir)) {
    const ext = extname(e.name).toLowerCase()
    if (!e.isFile || !MIME[ext]) continue
    const buf = await Deno.readFile(join(dir, e.name))
    const hash = encodeHex(await crypto.subtle.digest('SHA-256', buf))
    if ((await fetch(`${BLOSSOM}/${hash}`, { method: 'HEAD' })).ok) {
      console.log(`vorhanden    ${hash.slice(0, 8)}…  ${e.name}`)
      continue
    }
    const auth = await signieren({
      kind: 24242, pubkey, created_at: jetzt(), content: `Upload ${e.name}`,
      tags: [['t', 'upload'], ['x', hash], ['expiration', String(jetzt() + 600)]],
    })
    const r = await fetch(`${BLOSSOM}/upload`, {
      method: 'PUT',
      headers: { Authorization: 'Nostr ' + btoa(JSON.stringify(auth)), 'Content-Type': MIME[ext] },
      body: buf,
    })
    const text = await r.text()
    if (!r.ok) { console.error(`FEHLER HTTP ${r.status} bei ${e.name}: ${r.headers.get('x-reason') ?? text}`); Deno.exit(1) }
    const desc = JSON.parse(text)
    if (desc.sha256 !== hash) { console.error(`HASH-ABWEICHUNG bei ${e.name}: Server ${desc.sha256}`); Deno.exit(1) }
    console.log(`hochgeladen  ${hash.slice(0, 8)}…  ${e.name}  ${desc.size} B`)
    n++
  }
  console.log(`${n} Blob(s) neu. Weiter: node md2blossom.mjs <post-dir> --write`)
}

// ---------- publish ----------
if (cmd === 'publish') {
  let n = 0
  for await (const e of Deno.readDir(dir)) {
    if (!/\.1063\.[a-f0-9]{8}\.json$/.test(e.name)) continue
    const vorlage = JSON.parse(await Deno.readTextFile(join(dir, e.name))) as Unsigned
    const url = vorlage.tags.find((t) => t[0] === 'url')?.[1] ?? ''
    if (url.startsWith(BLOSSOM) && !(await fetch(url, { method: 'HEAD' })).ok) {
      console.error(`FEHLER ${e.name}: Blob ${url} liegt nicht auf Blossom — erst upload`); Deno.exit(1)
    }
    const signed = await signieren({ ...vorlage, pubkey, created_at: jetzt() })
    const acks = await Promise.all(LICENSE_RELAYS.map((r) => anRelay(r, signed)))
    await Deno.writeTextFile(join(dir, e.name.replace(/\.json$/, '.signed.json')), JSON.stringify(signed, null, 2))
    const x = signed.tags.find((t) => t[0] === 'x')?.[1] ?? ''
    console.log(`1063 ${x.slice(0, 8)}…  id ${signed.id.slice(0, 8)}…  ` +
      acks.map((a) => `${new URL(a.url).host}: ${a.ok ? 'ok' : 'FEHLER ' + a.msg}`).join('  '))
    if (!acks.some((a) => a.ok)) Deno.exit(1)
    n++
  }
  console.log(`${n} Nachweis(e) publiziert. Der 30023 folgt über die CI nach dem Merge auf main.`)
}
Deno.exit(0)
