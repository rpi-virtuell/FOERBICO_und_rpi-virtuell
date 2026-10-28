// Tests für nostr.ts: Fäden (Issues, PRs) aus Relay-Events, ohne Netz über einen Query-Fake.
import { assert, assertEquals } from 'jsr:@std/assert@^1.0.0';
import { fetchNostrThreads, type QueryFn } from './nostr.ts';
import type { NostrEvent } from './relays.ts';
import { loadConfig } from './config.ts';

const J = '4fa5d1c413e2b45e10d40bf3562ab701a5331206e359c90baae0e99bfd6c6e41'; // Jörg
const P = '6a90adda7da538994ee435d0ee03edde050d806ece4b4a8aa1fb45f04df54777'; // Poutník
const S = '1c5ff3caacd842c01dca8f378231b16617516d214da75c7aeabbe9e1efe9c0f6'; // laoc42
const A = '28d7ca9cba0e40f59843cd1cd507c1a912919769f4495a0f38df2b0ab0238bc4'; // Antiope
const REPO = `30617:${S}:edufeed-app`;
const T0 = 1_761_000_000; // ~ 20.10.2026

let n = 0;
const ev = (p: Partial<NostrEvent> & { kind: number; pubkey: string }): NostrEvent => ({
  id: (p.id ?? `id${++n}`).padEnd(64, '0').slice(0, 64),
  created_at: T0,
  tags: [],
  content: '',
  sig: 's',
  ...p,
});

const issueJ = ev({ id: 'aa', kind: 1621, pubkey: J, created_at: T0, tags: [['a', REPO], ['subject', 'Lizenzpille fehlt (`/calendar/event/<naddr>`)']] });
const issueS = ev({ id: 'bb', kind: 1621, pubkey: S, created_at: T0 + 10, tags: [['a', REPO], ['subject', 'Issue des edufeed-Leads mit Poutník-Kommentar']] });
const issueX = ev({ id: 'cc', kind: 1621, pubkey: S, created_at: T0 + 20, tags: [['a', REPO], ['subject', 'Fremdes Issue ohne uns']] });
const commentA = ev({ id: 'c1', kind: 1111, pubkey: A, created_at: T0 + 100, tags: [['E', issueJ.id], ['K', '1621']], content: 'Fix in nostr:nevent…' });
const commentP = ev({ id: 'c2', kind: 1111, pubkey: P, created_at: T0 + 50, tags: [['E', issueS.id], ['K', '1621']], content: 'Hinweis von Poutník' });
const statusA = ev({ id: 's1', kind: 1631, pubkey: A, created_at: T0 + 200, tags: [['e', issueJ.id, '', 'root']], content: 'Merged into main' });
const prP = ev({ id: 'dd', kind: 1618, pubkey: P, created_at: T0 + 300, tags: [['a', REPO], ['subject', 'Prototyp 5']] });

/** Routet Filter grob wie ein Relay: kinds, authors, #a, #E, #e. */
function fakeQuery(all: NostrEvent[], calls: object[] = []): QueryFn {
  return (_relays, filter) => {
    calls.push(filter);
    const f = filter as Record<string, string[] | number[]>;
    const hit = all.filter((e) => {
      if (f.kinds && !(f.kinds as number[]).includes(e.kind)) return false;
      if (f.authors && !(f.authors as string[]).includes(e.pubkey)) return false;
      if (f['#a'] && !e.tags.some((t) => t[0] === 'a' && (f['#a'] as string[]).includes(t[1]))) return false;
      if (f['#E'] && !e.tags.some((t) => t[0] === 'E' && (f['#E'] as string[]).includes(t[1]))) return false;
      if (f['#e'] && !e.tags.some((t) => t[0] === 'e' && (f['#e'] as string[]).includes(t[1]))) return false;
      if (f.ids && !(f.ids as string[]).includes(e.id)) return false;
      if (typeof f.since === 'number' && e.created_at < (f.since as unknown as number)) return false;
      return true;
    });
    return Promise.resolve({ events: hit, warnings: [] });
  };
}

const cfg = loadConfig();
const repo = cfg.repos['edufeed-app'];

Deno.test('fetchNostrThreads: eigene Issues und Issues mit eigenem Kommentar, fremde nicht', async () => {
  const calls: object[] = [];
  const { threads } = await fetchNostrThreads({ repos: [repo], me: [J, P], since: T0 - 1, query: fakeQuery([issueJ, issueS, issueX, commentA, commentP, statusA, prP], calls) });
  const ids = threads.map((t) => t.id).sort();
  assertEquals(ids, [issueJ.id, issueS.id, prP.id].sort());
  // kein Filter benutzt groups.edufeed.org und keiner fragt kind 1617 (Patches)
  assert(!calls.some((c) => JSON.stringify(c).includes('1617')));
});

Deno.test('fetchNostrThreads: letzter Status und letzter Kommentar bestimmen Stand, Akteur und Aktion', async () => {
  const { threads } = await fetchNostrThreads({ repos: [repo], me: [J, P], since: T0 - 1, query: fakeQuery([issueJ, commentA, statusA]) });
  const t = threads.find((t) => t.id === issueJ.id)!;
  assertEquals(t.source, 'nostr');
  assertEquals(t.kind, 'issue');
  assertEquals(t.repo, 'edufeed-app');
  assertEquals(t.title, 'Lizenzpille fehlt (`/calendar/event/<naddr>`)');
  assertEquals(t.status, 'resolved');
  assertEquals(t.createdBy, J);
  assertEquals(t.lastActivityAt, T0 + 200);
  assertEquals(t.lastActor, A);
  assertEquals(t.lastAction, 'erledigt');
  assert(t.url.startsWith('https://gitworkshop.dev/nevent1'));
});

Deno.test('fetchNostrThreads: Kommentar nach Status zählt als letzte Aktivität', async () => {
  const late = ev({ id: 'c9', kind: 1111, pubkey: S, created_at: T0 + 500, tags: [['E', issueJ.id]] });
  const { threads } = await fetchNostrThreads({ repos: [repo], me: [J], since: T0 - 1, query: fakeQuery([issueJ, statusA, late]) });
  const t = threads[0];
  assertEquals(t.lastActivityAt, T0 + 500);
  assertEquals(t.lastActor, S);
  assertEquals(t.lastAction, 'Kommentar');
});

Deno.test('fetchNostrThreads: PR von Poutník erscheint als kind pr mit Status open', async () => {
  const { threads } = await fetchNostrThreads({ repos: [repo], me: [P], since: T0 - 1, query: fakeQuery([prP]) });
  assertEquals(threads.length, 1);
  assertEquals(threads[0].kind, 'pr');
  assertEquals(threads[0].status, 'open');
  assertEquals(threads[0].lastAction, 'angelegt');
});

Deno.test('fetchNostrThreads: Warnungen der Relays werden durchgereicht, Ergebnis bleibt', async () => {
  const q: QueryFn = async (relays, filter) => {
    const r = await fakeQuery([issueJ])(relays, filter);
    return { events: r.events, warnings: ['wss://relay.ngit.dev: timeout'] };
  };
  const { threads, warnings } = await fetchNostrThreads({ repos: [repo], me: [J], since: T0 - 1, query: q });
  assertEquals(threads.length, 1);
  assert(warnings.some((w) => w.includes('timeout')));
});

Deno.test('fetchNostrThreads (C1): altes eigenes Issue mit neuem Kommentar erscheint, Aktivität zählt, nicht das Anlegedatum', async () => {
  const alt = ev({ id: 'ee', kind: 1621, pubkey: J, created_at: T0 - 60 * 86_400, tags: [['a', REPO], ['subject', 'Altes Issue vom September']] });
  const neu = ev({ id: 'c7', kind: 1111, pubkey: A, created_at: T0 + 10, tags: [['E', alt.id], ['K', '1621']], content: 'Antwort heute' });
  const { threads } = await fetchNostrThreads({ repos: [repo], me: [J, P], since: T0 - 30 * 86_400, query: fakeQuery([alt, neu]) });
  assertEquals(threads.map((t) => t.id), [alt.id]);
  assertEquals(threads[0].lastActor, A);
});

Deno.test('fetchNostrThreads (C1): altes fremdes Issue, das Poutník kürzlich kommentiert hat, erscheint', async () => {
  const fremd = ev({ id: 'ff', kind: 1621, pubkey: S, created_at: T0 - 40 * 86_400, tags: [['a', REPO], ['subject', 'Fremdes altes Issue']] });
  const mein = ev({ id: 'c8', kind: 1111, pubkey: P, created_at: T0 + 5, tags: [['E', fremd.id], ['K', '1621']] });
  const { threads } = await fetchNostrThreads({ repos: [repo], me: [J, P], since: T0 - 30 * 86_400, query: fakeQuery([fremd, mein]) });
  assertEquals(threads.map((t) => t.id), [fremd.id]);
});

Deno.test('fetchNostrThreads (C1): eigenes altes Issue ohne neue Aktivität bleibt draußen', async () => {
  const alt = ev({ id: 'gg', kind: 1621, pubkey: J, created_at: T0 - 60 * 86_400, tags: [['a', REPO], ['subject', 'Ruhendes Issue']] });
  const { threads } = await fetchNostrThreads({ repos: [repo], me: [J], since: T0 - 30 * 86_400, query: fakeQuery([alt]) });
  assertEquals(threads, []);
});
