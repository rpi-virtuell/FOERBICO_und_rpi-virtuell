// Tests für forgejo.ts: offene Issues beider Repos mit letztem Kommentar, nur lesend, ohne Netz.
import { assertEquals, assertRejects } from 'jsr:@std/assert@^1.0.0';
import { fetchForgejoThreads, ForgejoAuthError } from './forgejo.ts';

const BASE = 'https://git.example';
const REPO = 'Comenius-Institut/FOERBICO_und_rpi-virtuell';
const SINCE = new Date('2026-10-01T00:00:00Z');

type Route = (url: URL, init?: RequestInit) => Response;

function fakeFetch(routes: Record<string, Route>, calls: string[] = []): typeof fetch {
  return ((input: string | URL | Request, init?: RequestInit) => {
    const url = new URL(typeof input === 'string' ? input : input instanceof URL ? input : input.url);
    calls.push(url.pathname + url.search);
    const key = Object.keys(routes).find((k) => url.pathname === k);
    if (!key) return Promise.resolve(new Response('not found', { status: 404 }));
    return Promise.resolve(routes[key](url, init));
  }) as typeof fetch;
}

const json = (body: unknown, headers: Record<string, string> = {}) =>
  new Response(JSON.stringify(body), { status: 200, headers: { 'content-type': 'application/json', ...headers } });

const issue = (n: number, updated: string, login = 'joerglohrer') => ({
  number: n,
  title: `Issue ${n}`,
  state: 'open',
  html_url: `${BASE}/${REPO}/issues/${n}`,
  created_at: '2026-09-01T10:00:00Z',
  updated_at: updated,
  user: { login },
  comments: n === 1 ? 1 : 0,
});

Deno.test('fetchForgejoThreads: Issues vor since fallen weg, letzter Kommentar liefert lastActor', async () => {
  const calls: string[] = [];
  const f = fakeFetch({
    [`/api/v1/repos/${REPO}/issues`]: () => json([issue(1, '2026-10-20T12:00:00Z'), issue(2, '2026-09-15T12:00:00Z')]),
    [`/api/v1/repos/${REPO}/issues/1/comments`]: () =>
      json([
        { user: { login: 'joerglohrer' }, created_at: '2026-10-10T08:00:00Z', body: 'a' },
        { user: { login: 'sicking' }, created_at: '2026-10-20T12:00:00Z', body: 'b' },
      ]),
  }, calls);
  const threads = await fetchForgejoThreads({ base: BASE, repos: [REPO], token: 't', since: SINCE, fetchFn: f });
  assertEquals(threads.length, 1);
  const t = threads[0];
  assertEquals(t.source, 'forgejo');
  assertEquals(t.kind, 'issue');
  assertEquals(t.id, `${REPO}#1`);
  assertEquals(t.title, 'Issue 1');
  assertEquals(t.status, 'open');
  assertEquals(t.createdBy, 'joerglohrer');
  assertEquals(t.lastActor, 'sicking');
  assertEquals(t.lastAction, 'Kommentar');
  assertEquals(t.lastActivityAt, Math.floor(Date.parse('2026-10-20T12:00:00Z') / 1000));
  assertEquals(t.url, `${BASE}/${REPO}/issues/1`);
  // Issue 2 liegt vor since: keine Kommentar-Abfrage dafür
  assertEquals(calls.filter((c) => c.includes('/issues/2/')).length, 0);
  // Liste wird mit state=open, sort=updated, type=issues und since angefragt
  assertEquals(calls[0].includes('state=open') && calls[0].includes('type=issues') && calls[0].includes('since='), true);
});

Deno.test('fetchForgejoThreads: Issue ohne Kommentare hat den Autor als lastActor und lastAction "angelegt"', async () => {
  const f = fakeFetch({
    [`/api/v1/repos/${REPO}/issues`]: () => json([issue(3, '2026-10-05T12:00:00Z', 'sicking')]),
    [`/api/v1/repos/${REPO}/issues/3/comments`]: () => json([]),
  });
  const [t] = await fetchForgejoThreads({ base: BASE, repos: [REPO], token: 't', since: SINCE, fetchFn: f });
  assertEquals(t.lastActor, 'sicking');
  assertEquals(t.lastAction, 'angelegt');
});

Deno.test('fetchForgejoThreads: 401 wirft ForgejoAuthError', async () => {
  const f = fakeFetch({ [`/api/v1/repos/${REPO}/issues`]: () => new Response('unauthorized', { status: 401 }) });
  await assertRejects(() => fetchForgejoThreads({ base: BASE, repos: [REPO], token: 'alt', since: SINCE, fetchFn: f }), ForgejoAuthError);
});

Deno.test('fetchForgejoThreads: holt die zweite Seite, wenn X-Total-Count größer als die Seite ist', async () => {
  const calls: string[] = [];
  const f = fakeFetch({
    [`/api/v1/repos/${REPO}/issues`]: (url) => {
      const page = url.searchParams.get('page') ?? '1';
      const list = page === '1' ? [issue(10, '2026-10-21T00:00:00Z')] : [issue(11, '2026-10-22T00:00:00Z')];
      return json(list, { 'X-Total-Count': '2' });
    },
    [`/api/v1/repos/${REPO}/issues/10/comments`]: () => json([]),
    [`/api/v1/repos/${REPO}/issues/11/comments`]: () => json([]),
  }, calls);
  const threads = await fetchForgejoThreads({ base: BASE, repos: [REPO], token: 't', since: SINCE, fetchFn: f, pageSize: 1 });
  assertEquals(threads.map((t) => t.id).sort(), [`${REPO}#10`, `${REPO}#11`]);
  assertEquals(calls.filter((c) => c.startsWith(`/api/v1/repos/${REPO}/issues?`)).length, 2);
});
