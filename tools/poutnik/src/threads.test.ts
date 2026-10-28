// Tests für threads.ts: Zusammenführen, Sortierung, „wartet auf dich“, Zeilenformat, Befehl mit Warnungen.
import { assert, assertEquals } from 'jsr:@std/assert@^1.0.0';
import { cmdThreads, formatThreadLine, mergeThreads, type Thread } from './threads.ts';

const J = '4fa5d1c413e2b45e10d40bf3562ab701a5331206e359c90baae0e99bfd6c6e41';
const P = '6a90adda7da538994ee435d0ee03edde050d806ece4b4a8aa1fb45f04df54777';
const A = '28d7ca9cba0e40f59843cd1cd507c1a912919769f4495a0f38df2b0ab0238bc4';
const ME = [J, P, 'joerglohrer'];

const t = (p: Partial<Thread>): Thread => ({
  source: 'nostr',
  repo: 'edufeed-app',
  kind: 'issue',
  id: 'x',
  title: 'T',
  status: 'open',
  createdBy: J,
  lastActivityAt: 0,
  lastActor: J,
  lastAction: 'angelegt',
  url: 'https://gitworkshop.dev/nevent1x',
  ...p,
});

Deno.test('mergeThreads: sortiert nach letzter Aktivität absteigend und verkettet Warnungen', () => {
  const r = mergeThreads(
    [
      { threads: [t({ id: 'a', lastActivityAt: 100 }), t({ id: 'b', lastActivityAt: 300 })], warnings: ['w1'] },
      { threads: [t({ id: 'c', lastActivityAt: 200, source: 'forgejo', lastActor: 'sicking' })], warnings: ['w2'] },
    ],
    ME,
  );
  assertEquals(r.threads.map((x) => x.id), ['b', 'c', 'a']);
  assertEquals(r.warnings, ['w1', 'w2']);
});

Deno.test('mergeThreads: waitingOnMe nur, wenn zuletzt jemand anderes aktiv war; Poutník zählt zu mir', () => {
  const r = mergeThreads([{ threads: [t({ id: 'a', lastActor: A }), t({ id: 'b', lastActor: P }), t({ id: 'c', lastActor: 'joerglohrer', source: 'forgejo' })], warnings: [] }], ME);
  assertEquals(r.threads.map((x) => [x.id, x.waitingOnMe]), [['a', true], ['b', false], ['c', false]]);
});

Deno.test('mergeThreads: leere Teile mit Warnung ergeben leere Liste, aber die Warnung bleibt', () => {
  const r = mergeThreads([{ threads: [], warnings: ['wss://relay.ngit.dev: timeout'] }], ME);
  assertEquals(r.threads, []);
  assertEquals(r.warnings, ['wss://relay.ngit.dev: timeout']);
});

Deno.test('formatThreadLine: Titel mit Umlauten und Backticks bleibt, über 60 Zeichen wird gekürzt', () => {
  const lang = 'Lizenzpille fehlt auf der Kalender-Event-Seite (`/calendar/event/<naddr>`)';
  const line = formatThreadLine({ ...t({ title: lang, lastActivityAt: 1_792_497_600, lastActor: A, lastAction: 'erledigt', status: 'resolved' }), waitingOnMe: true });
  assert(line.startsWith('→'));
  assert(line.includes(lang.slice(0, 60) + '…'));
  assert(line.includes('erledigt'));
  assert(line.includes('2026-10-'));
  const kurz = formatThreadLine({ ...t({ title: 'Gästelink in Anrufen' }), waitingOnMe: false });
  assert(kurz.includes('Gästelink in Anrufen'));
  assert(!kurz.startsWith('→'));
});

Deno.test('cmdThreads: zeigt Warnungen und Fäden, Forgejo-Auth-Fehler wird zur Warnung', async () => {
  const out: string[] = [];
  const code = await cmdThreads(['--since', '30'], {
    nostr: () => Promise.resolve({ threads: [t({ id: 'a', lastActivityAt: 5, lastActor: A })], warnings: ['wss://x: timeout'] }),
    forgejo: () => Promise.reject(new (class ForgejoAuthError extends Error {})('Forgejo: Token abgelehnt')),
    print: (s) => out.push(s),
    me: ME,
  });
  assertEquals(code, 0);
  const text = out.join('\n');
  assert(text.includes('→'));
  assert(text.includes('wss://x: timeout'));
  assert(text.includes('Forgejo: Token abgelehnt'));
});

Deno.test('cmdThreads --json: gibt threads und warnings als JSON aus', async () => {
  const out: string[] = [];
  await cmdThreads(['--json'], {
    nostr: () => Promise.resolve({ threads: [t({ id: 'a' })], warnings: [] }),
    forgejo: () => Promise.resolve([]),
    print: (s) => out.push(s),
    me: ME,
  });
  const parsed = JSON.parse(out.join('\n'));
  assertEquals(parsed.threads.length, 1);
  assertEquals(parsed.warnings, []);
});
