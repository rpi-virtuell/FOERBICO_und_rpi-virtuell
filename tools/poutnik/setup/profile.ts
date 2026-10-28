// Einmaliges Setup: Poutníks Profil (kind 0) ergänzen und Relay-Liste (kind 10002) um die Repo-Relays erweitern.
// Signiert über Amber (NIP-46) mit POUTNIK_BUNKER_URL + POUTNIK_CLIENT_SECRET_HEX aus ~/.config/poutnik/env.
// Muster: Website/scripts/blossom-bunker.ts. Aufruf: deno run -A setup/profile.ts [--yes]
import { loadConfig, loadEnv } from '../src/config.ts';
import { queryRelays, type NostrEvent } from '../src/relays.ts';

export const ABOUT =
  "Der Pilger aus Comenius' „Labyrinth der Welt und Paradies des Herzens“, unterwegs zwischen Forgejo und gitworkshop. " +
  'Agent von Jörg Lohrer (Comenius-Institut); jeder Beitrag ist von Jörg gelesen und freigegeben.';

const EDUFEED_RELAYS = ['wss://relay.edufeed.org', 'wss://relay-rpi.edufeed.org', 'wss://amb-relay.edufeed.org'];

/** Ergänzt das vorhandene Profil; unbekannte Felder und das Bild bleiben erhalten. */
export function buildProfile(current: Record<string, unknown>): Record<string, unknown> {
  return { ...current, name: 'Poutník', display_name: 'Poutník', about: ABOUT, bot: true };
}

const norm = (u: string) => u.replace(/\/+$/, '');

/** Vereinigt die bestehenden r-Tags mit den Repo-Relays, bestehende zuerst, ohne Duplikate (Schrägstrich egal). */
export function buildRelayList(current: string[][], repoRelays: string[]): string[][] {
  const out: string[][] = [];
  const seen = new Set<string>();
  for (const t of current) {
    if (t[0] !== 'r' || seen.has(norm(t[1]))) continue;
    seen.add(norm(t[1]));
    out.push(t);
  }
  for (const u of repoRelays) {
    if (seen.has(norm(u))) continue;
    seen.add(norm(u));
    out.push(['r', u]);
  }
  return out;
}

type Unsigned = { kind: number; content: string; tags: string[][]; created_at: number };

/** Baut beide neuen Events aus den gelesenen; bricht ab, wenn kind 0 fehlt/ohne Bild ist oder kind 10002 fehlt
 *  (Schutz gegen leeres Überschreiben bzw. Verkürzen der Relay-Liste, Review I4). */
export function planUpdates(kind0: NostrEvent | undefined, kind10002: NostrEvent | undefined, repoRelays: string[], now = Math.floor(Date.now() / 1000)): { neu0: Unsigned; neu10002: Unsigned } {
  if (!kind0) throw new Error('Kein kind 0 für Poutník gefunden, Abbruch (Schutz gegen leeres Überschreiben).');
  let current: Record<string, unknown>;
  try {
    current = JSON.parse(kind0.content || '{}') as Record<string, unknown>;
  } catch {
    throw new Error('kind 0 ist kein gültiges JSON, Abbruch.');
  }
  if (!current.picture) throw new Error('Gelesenes Profil hat kein Bild, Abbruch (Schutz gegen leeres Überschreiben).');
  if (!kind10002) throw new Error('Keine Relay-Liste (kind 10002) gelesen, Abbruch (sonst würde die Liste verkürzt).');
  return {
    neu0: { kind: 0, content: JSON.stringify(buildProfile(current)), tags: [], created_at: now },
    neu10002: { kind: 10002, content: '', tags: buildRelayList(kind10002.tags, repoRelays), created_at: now },
  };
}

async function main(argv: string[]): Promise<number> {
  const yes = argv.includes('--yes');
  const cfg = loadConfig();
  const env = loadEnv();
  const pubkey = env.POUTNIK_PUBKEY_HEX;
  const bunkerUrl = env.POUTNIK_BUNKER_URL;
  const clientSecretHex = env.POUTNIK_CLIENT_SECRET_HEX;
  if (!pubkey || !bunkerUrl || !clientSecretHex) {
    console.error('Fehlt in ~/.config/poutnik/env: POUTNIK_PUBKEY_HEX, POUTNIK_BUNKER_URL, POUTNIK_CLIENT_SECRET_HEX');
    return 2;
  }
  const readRelays = [...EDUFEED_RELAYS, 'wss://relay.ngit.dev'];
  const { events, warnings } = await queryRelays(readRelays, { kinds: [0, 10002], authors: [pubkey] });
  for (const w of warnings) console.error('Warnung:', w);
  const latest = (kind: number): NostrEvent | undefined =>
    events.filter((e) => e.kind === kind).sort((a, b) => b.created_at - a.created_at)[0];
  const repoRelays = [...new Set(Object.values(cfg.repos).flatMap((r) => r.relays))];
  let neu0: Unsigned, neu10002: Unsigned;
  try {
    ({ neu0, neu10002 } = planUpdates(latest(0), latest(10002), repoRelays));
  } catch (e) {
    console.error(e instanceof Error ? e.message : String(e));
    return 1;
  }
  console.log('Neues kind 0:', neu0.content);
  console.log('Neues kind 10002:', JSON.stringify(neu10002.tags));
  if (!yes) {
    const antwort = prompt('Veröffentlichen? (ja/nein)');
    if (antwort?.trim().toLowerCase() !== 'ja') return 1;
  }

  const { NostrConnectSigner, SimpleSigner } = await import('npm:applesauce-signers@^2.0.0');
  const { RelayPool } = await import('npm:applesauce-relay@^2.0.0');
  const pool = new RelayPool();
  NostrConnectSigner.subscriptionMethod = (relays, filters) => pool.req(relays, filters);
  NostrConnectSigner.publishMethod = (relays, event) => pool.event(relays, event);
  const benign = (msg: string) => /already connected|no permission/i.test(msg);
  globalThis.addEventListener('unhandledrejection', (e) => {
    const msg = e.reason instanceof Error ? e.reason.message : String(e.reason);
    if (benign(msg)) e.preventDefault();
  });
  const mitTimeout = <T>(p: Promise<T>, ms: number, was: string): Promise<T> => {
    let t: ReturnType<typeof setTimeout> | undefined;
    const timeout = new Promise<never>((_, rej) => {
      t = setTimeout(() => rej(new Error(`${was}: Timeout nach ${ms / 1000}s`)), ms);
    });
    return Promise.race([p, timeout]).finally(() => clearTimeout(t));
  };
  const { remote, relays, secret } = NostrConnectSigner.parseBunkerURI(bunkerUrl);
  console.error(`Bunker: ${remote.slice(0, 8)}… über ${relays.join(', ')} – verbinde …`);
  const signer = new NostrConnectSigner({ relays, remote, signer: SimpleSigner.fromKey(clientSecretHex) });
  // „already connected“ kommt von Amber bei einem erneuten Lauf mit derselben Client-Identität (CLIENT_SECRET_HEX);
  // dann genügt open(). Ein fremder Client auf demselben Bunker-Link bekommt dagegen keine Antworten (Task-3-Ruling).
  try {
    await mitTimeout(signer.connect(secret), 60_000, 'Bunker connect');
    console.error('Bunker: verbunden');
  } catch (err) {
    const msg = err instanceof Error ? err.message : String(err);
    if (!benign(msg)) throw err;
    console.error(`Bunker: „${msg}“ – öffne bestehende Verbindung`);
    await mitTimeout(signer.open(), 30_000, 'Bunker open');
    (signer as unknown as { isConnected: boolean }).isConnected = true;
  }
  const got = await mitTimeout(signer.getPublicKey(), 30_000, 'Bunker getPublicKey');
  console.error(`Bunker: Pubkey ${got.slice(0, 8)}…`);
  if (got !== pubkey) {
    console.error(`Bunker-Pubkey ${got.slice(0, 8)}… ist nicht Poutník (${pubkey.slice(0, 8)}…), Abbruch.`);
    return 1;
  }
  const ziele = [...EDUFEED_RELAYS, ...repoRelays.filter((r) => !r.includes('groups.edufeed.org'))];
  for (const ev of [neu0, neu10002]) {
    console.error(`Signiere kind ${ev.kind} (Amber: Dauerfreigabe für Poutník) …`);
    const signed = (await mitTimeout(signer.signEvent(ev), 60_000, `Signatur kind:${ev.kind}`)) as NostrEvent;
    console.error(`kind ${ev.kind} signiert, veröffentliche an ${ziele.length} Relays …`);
    const oks = await Promise.all(ziele.map((u) => anRelay(u, signed)));
    const n = oks.filter((o) => o.ok).length;
    console.log(`kind ${ev.kind}: ${n}/${ziele.length} Relays OK`, oks.filter((o) => !o.ok).map((o) => `${o.url} ${o.msg}`).join('; '));
    if (n < 2) {
      console.error('Zu wenige Relays haben angenommen, Abbruch.');
      Deno.exit(1);
    }
  }
  Deno.exit(0);
}

function anRelay(url: string, ev: NostrEvent, ms = 10_000): Promise<{ url: string; ok: boolean; msg: string }> {
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

if (import.meta.main) Deno.exit(await main(Deno.args));
