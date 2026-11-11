// dm: private Nachrichten nach NIP-17 als Poutník senden und lesen.
// ngit kann keine DMs; darum signiert hier ein eigener Amber-Bunker (POUTNIK_DM_BUNKER_URL +
// POUTNIK_DM_CLIENT_SECRET_HEX in ~/.config/poutnik/env), getrennt von ngit und dem Profil-Setup.
// Aufbau: rumor (kind 14, unsigniert) → seal (kind 13, von Poutník signiert, nip44 an Empfänger)
// → gift wrap (kind 1059, Einmalschlüssel, nip44 an Empfänger). Zustellung an dessen kind 10050.
import { finalizeEvent, generateSecretKey, getEventHash, getPublicKey, nip44 } from 'npm:nostr-tools@2.10.4';
import { loadEnv } from './config.ts';
import { npubDecode } from './nip19.ts';
import { queryRelays, type NostrEvent } from './relays.ts';

/** Was der Bunker für DMs können muss (Amber-Freigaben: Pubkey lesen, nip44 ver-/entschlüsseln, sign kind 13). */
export type DmSigner = {
  getPublicKey(): Promise<string>;
  signEvent(t: { kind: number; created_at: number; tags: string[][]; content: string }): Promise<NostrEvent>;
  nip44Encrypt(pubkey: string, plaintext: string): Promise<string>;
  nip44Decrypt(pubkey: string, ciphertext: string): Promise<string>;
};

export type Rumor = { id: string; kind: 14; pubkey: string; created_at: number; tags: string[][]; content: string };

const ZWEI_TAGE = 2 * 24 * 3600;
const LESE_RELAYS = ['wss://relay.edufeed.org', 'wss://nos.lol'];
const norm = (u: string) => u.replace(/\/+$/, '');

export function buildRumor(sender: string, recipient: string, text: string, now: number): Rumor {
  const r = { kind: 14 as const, pubkey: sender, created_at: now, tags: [['p', recipient]], content: text };
  return { ...r, id: getEventHash(r as never) };
}

/** Verpackt ein Rumor für einen Empfänger. Zeitstempel von Seal und Wrap werden bis zu zwei Tage zurückverlegt (NIP-59). */
export async function wrapFor(
  recipient: string,
  rumor: Rumor,
  signer: DmSigner,
  now: number,
  random: () => number = Math.random,
): Promise<NostrEvent> {
  const zeit = () => now - Math.floor(random() * ZWEI_TAGE);
  const seal = await signer.signEvent({
    kind: 13,
    created_at: zeit(),
    tags: [],
    content: await signer.nip44Encrypt(recipient, JSON.stringify(rumor)),
  });
  const eph = generateSecretKey();
  const ck = nip44.v2.utils.getConversationKey(eph, recipient);
  return finalizeEvent(
    { kind: 1059, created_at: zeit(), tags: [['p', recipient]], content: nip44.v2.encrypt(JSON.stringify(seal), ck) },
    eph,
  ) as unknown as NostrEvent;
}

/** Packt einen Gift Wrap an den Signer aus. Prüft, dass Seal und Rumor vom selben Absender stammen. */
export async function unwrap(wrap: NostrEvent, signer: DmSigner): Promise<{ from: string; rumor: Rumor }> {
  const seal = JSON.parse(await signer.nip44Decrypt(wrap.pubkey, wrap.content)) as NostrEvent;
  if (seal.kind !== 13) throw new Error(`kein Seal (kind ${seal.kind})`);
  const rumor = JSON.parse(await signer.nip44Decrypt(seal.pubkey, seal.content)) as Rumor;
  if (rumor.pubkey !== seal.pubkey) throw new Error('Absender von Seal und Nachricht weichen ab');
  return { from: seal.pubkey, rumor };
}

/** DM-Relays aus dem neuesten kind 10050 eines Schlüssels. */
export function dmRelaysFrom(events: NostrEvent[], pubkey: string): string[] {
  const neu = events.filter((e) => e.kind === 10050 && e.pubkey === pubkey).sort((a, b) => b.created_at - a.created_at)[0];
  return neu ? [...new Set(neu.tags.filter((t) => t[0] === 'relay' && t[1]).map((t) => norm(t[1])))] : [];
}

export function toHex(key: string): string {
  if (/^[0-9a-f]{64}$/.test(key)) return key;
  if (key.startsWith('npub1')) return npubDecode(key);
  throw new Error(`Unbekannter Schlüssel: ${key.slice(0, 12)}… (npub oder hex erwartet)`);
}

export function publishTo(url: string, ev: NostrEvent, ms = 10_000): Promise<{ url: string; ok: boolean; msg: string }> {
  return new Promise((resolve) => {
    const ws = new WebSocket(url);
    const fertig = (ok: boolean, msg: string) => {
      clearTimeout(t);
      try {
        ws.close();
      } catch { /* egal */ }
      resolve({ url, ok, msg });
    };
    const t = setTimeout(() => fertig(false, 'Timeout'), ms);
    ws.onopen = () => ws.send(JSON.stringify(['EVENT', ev]));
    ws.onmessage = (m) => {
      let d: unknown[];
      try {
        d = JSON.parse(String(m.data));
      } catch {
        return;
      }
      if (d[0] === 'OK' && d[1] === ev.id) fertig(Boolean(d[2]), String(d[3] ?? ''));
      if (d[0] === 'NOTICE') fertig(false, String(d[1]));
    };
    ws.onerror = () => fertig(false, 'Verbindungsfehler');
  });
}

const mitTimeout = <T>(p: Promise<T>, ms: number, was: string): Promise<T> => {
  let t: ReturnType<typeof setTimeout> | undefined;
  const timeout = new Promise<never>((_, rej) => {
    t = setTimeout(() => rej(new Error(`${was}: Timeout nach ${ms / 1000}s (Amber am Handy offen?)`)), ms);
  });
  return Promise.race([p, timeout]).finally(() => clearTimeout(t));
};

/** Verbindet den DM-Bunker. „already connected“ von Amber ist harmlos und wird abgefangen (sonst Absturz ohne Meldung). */
export async function connectDmSigner(env: Record<string, string>): Promise<DmSigner> {
  const url = env.POUTNIK_DM_BUNKER_URL;
  const secretHex = env.POUTNIK_DM_CLIENT_SECRET_HEX;
  if (!url || !secretHex) throw new Error('Fehlt in ~/.config/poutnik/env: POUTNIK_DM_BUNKER_URL, POUTNIK_DM_CLIENT_SECRET_HEX');
  const { NostrConnectSigner, SimpleSigner } = await import('npm:applesauce-signers@^2.0.0');
  const { RelayPool } = await import('npm:applesauce-relay@^2.0.0');
  const pool = new RelayPool();
  NostrConnectSigner.subscriptionMethod = (relays, filters) => pool.req(relays, filters);
  NostrConnectSigner.publishMethod = (relays, event) => pool.event(relays, event);
  globalThis.addEventListener('unhandledrejection', (e) => {
    const msg = e.reason instanceof Error ? e.reason.message : String(e.reason);
    if (/already connected/i.test(msg)) e.preventDefault();
  });
  const { remote, relays, secret } = NostrConnectSigner.parseBunkerURI(url);
  const s = new NostrConnectSigner({ relays, remote, signer: SimpleSigner.fromKey(secretHex) });
  try {
    await mitTimeout(s.connect(secret), 60_000, 'Bunker connect');
  } catch (err) {
    const msg = err instanceof Error ? err.message : String(err);
    if (!/already connected/i.test(msg)) throw err;
    await mitTimeout(s.open(), 30_000, 'Bunker open');
    (s as unknown as { isConnected: boolean }).isConnected = true;
  }
  return {
    getPublicKey: () => mitTimeout(s.getPublicKey(), 30_000, 'Amber get_public_key'),
    signEvent: (t) => mitTimeout(s.signEvent(t) as Promise<NostrEvent>, 90_000, `Amber Signatur kind ${t.kind}`),
    nip44Encrypt: (pk, txt) => mitTimeout(Promise.resolve(s.nip44!.encrypt(pk, txt)), 90_000, 'Amber nip44_encrypt'),
    nip44Decrypt: (pk, txt) => mitTimeout(Promise.resolve(s.nip44!.decrypt(pk, txt)), 90_000, 'Amber nip44_decrypt'),
  };
}

/** Für Tests und Probeläufe: Signer mit lokalem Schlüssel. */
export function localSigner(sk: Uint8Array): DmSigner {
  const pk = getPublicKey(sk);
  const ck = (other: string) => nip44.v2.utils.getConversationKey(sk, other);
  return {
    getPublicKey: () => Promise.resolve(pk),
    signEvent: (t) => Promise.resolve(finalizeEvent(t, sk) as unknown as NostrEvent),
    nip44Encrypt: (other, txt) => Promise.resolve(nip44.v2.encrypt(txt, ck(other))),
    nip44Decrypt: (other, txt) => Promise.resolve(nip44.v2.decrypt(txt, ck(other))),
  };
}

export type DmDeps = {
  env: Record<string, string>;
  query: typeof queryRelays;
  connect: (env: Record<string, string>) => Promise<DmSigner>;
  publish: typeof publishTo;
  now: () => number;
  out: (s: string) => void;
  err: (s: string) => void;
};

const defaultDeps = (): DmDeps => ({
  env: loadEnv(),
  query: queryRelays,
  connect: connectDmSigner,
  publish: publishTo,
  now: () => Math.floor(Date.now() / 1000),
  out: (s) => console.log(s),
  err: (s) => console.error(s),
});

const HILFE = `deno task dm send <npub|hex> (--text "…" | --file <pfad>) [--send]
  Ohne --send nur Probelauf: zeigt Empfänger, DM-Relays und Text, verbindet Amber, signiert nichts.
deno task dm inbox [--since <Tage>]
  Liest an Poutník gerichtete DMs (entschlüsselt über Amber).`;

function opt(argv: string[], name: string): string | undefined {
  const i = argv.indexOf(name);
  return i >= 0 ? argv[i + 1] : undefined;
}

export async function cmdDm(argv: string[], deps: DmDeps = defaultDeps()): Promise<number> {
  const [sub, ...rest] = argv;
  const me = deps.env.POUTNIK_PUBKEY_HEX;
  if (!me) {
    deps.err('Fehlt in ~/.config/poutnik/env: POUTNIK_PUBKEY_HEX');
    return 2;
  }
  if (sub === 'send') return await send(rest, me, deps);
  if (sub === 'inbox') return await inbox(rest, me, deps);
  deps.err(HILFE);
  return 2;
}

async function send(argv: string[], me: string, deps: DmDeps): Promise<number> {
  const ziel = argv.find((a) => !a.startsWith('--') && a !== opt(argv, '--text') && a !== opt(argv, '--file'));
  const datei = opt(argv, '--file');
  const text = (opt(argv, '--text') ?? (datei ? await Deno.readTextFile(datei) : '')).trim();
  if (!ziel || !text) {
    deps.err(HILFE);
    return 2;
  }
  const empf = toHex(ziel);
  const { events, warnings } = await deps.query(LESE_RELAYS, { kinds: [10050], authors: [empf, me] });
  for (const w of warnings) deps.err(`Warnung: ${w}`);
  const zielRelays = dmRelaysFrom(events, empf);
  const eigene = dmRelaysFrom(events, me);
  deps.err(`Empfänger ${empf.slice(0, 8)}… · DM-Relays: ${zielRelays.join(', ') || '–'} · eigene: ${eigene.join(', ') || '–'}`);
  deps.err(`Text (${text.length} Zeichen):\n${text}`);
  if (zielRelays.length === 0) {
    deps.err('Empfänger hat keine DM-Relays (kind 10050) veröffentlicht, Abbruch.');
    return 1;
  }
  const signer = await deps.connect(deps.env);
  const got = await signer.getPublicKey();
  if (got !== me) {
    deps.err(`Bunker-Pubkey ${got.slice(0, 8)}… ist nicht Poutník, Abbruch.`);
    return 1;
  }
  if (!argv.includes('--send')) {
    deps.err('Probelauf: Amber verbunden, nichts signiert, nichts gesendet. Zum Senden --send anhängen.');
    return 0;
  }
  const rumor = buildRumor(me, empf, text, deps.now());
  const wrap = await wrapFor(empf, rumor, signer, deps.now());
  const r1 = await Promise.all(zielRelays.map((u) => deps.publish(u, wrap)));
  deps.out(`An Empfänger: ${r1.map((r) => `${r.url} ${r.ok ? 'OK' : `FEHLER ${r.msg}`}`).join('; ')}`);
  if (eigene.length) {
    const kopie = await wrapFor(me, rumor, signer, deps.now());
    const r2 = await Promise.all(eigene.map((u) => deps.publish(u, kopie)));
    deps.out(`Kopie an Poutník: ${r2.map((r) => `${r.url} ${r.ok ? 'OK' : `FEHLER ${r.msg}`}`).join('; ')}`);
  }
  deps.out(`Nachricht ${rumor.id} · Gift Wrap ${wrap.id}`);
  return r1.some((r) => r.ok) ? 0 : 1;
}

async function inbox(argv: string[], me: string, deps: DmDeps): Promise<number> {
  const tage = Number(opt(argv, '--since') ?? '7');
  const { events: listen } = await deps.query(LESE_RELAYS, { kinds: [10050], authors: [me] });
  const relays = dmRelaysFrom(listen, me);
  if (relays.length === 0) {
    deps.err('Poutník hat keine DM-Relays (kind 10050).');
    return 1;
  }
  // Wrap-Zeitstempel liegen bis zu zwei Tage zurück, darum großzügiger abfragen.
  const since = deps.now() - tage * 86400 - ZWEI_TAGE;
  const { events, warnings } = await deps.query(relays, { kinds: [1059], '#p': [me], since });
  for (const w of warnings) deps.err(`Warnung: ${w}`);
  const signer = await deps.connect(deps.env);
  const grenze = deps.now() - tage * 86400;
  const nachrichten: { from: string; rumor: Rumor }[] = [];
  for (const w of events) {
    try {
      const n = await unwrap(w, signer);
      if (n.rumor.created_at >= grenze) nachrichten.push(n);
    } catch (e) {
      deps.err(`Nicht lesbar (${w.id.slice(0, 8)}…): ${e instanceof Error ? e.message : String(e)}`);
    }
  }
  nachrichten.sort((a, b) => a.rumor.created_at - b.rumor.created_at);
  for (const n of nachrichten) {
    const wann = new Date(n.rumor.created_at * 1000).toISOString().slice(0, 16).replace('T', ' ');
    const richtung = n.from === me ? `an ${n.rumor.tags.find((t) => t[0] === 'p')?.[1]?.slice(0, 8)}…` : `von ${n.from.slice(0, 8)}…`;
    deps.out(`${wann} ${richtung}\n${n.rumor.content}\n`);
  }
  if (nachrichten.length === 0) deps.out(`Keine DMs in den letzten ${tage} Tagen.`);
  return 0;
}
