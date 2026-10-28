// Forgejo nur lesend: offene Issues beider Repos mit Aktivität seit `since`, letzter Kommentar als Stand.
import type { Thread } from './threads.ts';

export class ForgejoAuthError extends Error {
  constructor(msg = 'Forgejo: Token abgelehnt (401/403)') {
    super(msg);
    this.name = 'ForgejoAuthError';
  }
}

export type ForgejoOptions = {
  base: string;
  repos: string[];
  token: string;
  since: Date;
  fetchFn?: typeof fetch;
  pageSize?: number;
};

type ForgejoIssue = {
  number: number;
  title: string;
  state: 'open' | 'closed';
  html_url: string;
  created_at: string;
  updated_at: string;
  user: { login: string };
};

type ForgejoComment = { user: { login: string }; created_at: string };

const secs = (iso: string) => Math.floor(Date.parse(iso) / 1000);

async function getJson<T>(fetchFn: typeof fetch, url: URL, token: string): Promise<{ body: T; headers: Headers }> {
  const res = await fetchFn(url, { headers: { Authorization: `token ${token}`, Accept: 'application/json' } });
  if (res.status === 401 || res.status === 403) throw new ForgejoAuthError();
  if (!res.ok) throw new Error(`Forgejo ${res.status} bei ${url.pathname}`);
  return { body: (await res.json()) as T, headers: res.headers };
}

async function listOpenIssues(o: Required<Pick<ForgejoOptions, 'base' | 'token' | 'since' | 'fetchFn' | 'pageSize'>>, repo: string): Promise<ForgejoIssue[]> {
  const out: ForgejoIssue[] = [];
  for (let page = 1; ; page++) {
    const url = new URL(`${o.base}/api/v1/repos/${repo}/issues`);
    url.searchParams.set('state', 'open');
    url.searchParams.set('sort', 'updated');
    url.searchParams.set('type', 'issues');
    url.searchParams.set('since', o.since.toISOString());
    url.searchParams.set('limit', String(o.pageSize));
    url.searchParams.set('page', String(page));
    const { body, headers } = await getJson<ForgejoIssue[]>(o.fetchFn, url, o.token);
    out.push(...body);
    const total = Number(headers.get('X-Total-Count') ?? out.length);
    if (body.length < o.pageSize || out.length >= total) break;
  }
  return out;
}

export async function fetchForgejoThreads(opts: ForgejoOptions): Promise<Thread[]> {
  const o = { ...opts, fetchFn: opts.fetchFn ?? fetch, pageSize: opts.pageSize ?? 50 };
  const sinceSecs = Math.floor(o.since.getTime() / 1000);
  const threads: Thread[] = [];
  for (const repo of o.repos) {
    const issues = (await listOpenIssues(o, repo)).filter((i) => secs(i.updated_at) >= sinceSecs);
    for (const i of issues) {
      const url = new URL(`${o.base}/api/v1/repos/${repo}/issues/${i.number}/comments`);
      const { body: comments } = await getJson<ForgejoComment[]>(o.fetchFn, url, o.token);
      const last = comments.at(-1);
      threads.push({
        source: 'forgejo',
        repo,
        kind: 'issue',
        id: `${repo}#${i.number}`,
        title: i.title,
        status: i.state === 'open' ? 'open' : 'closed',
        createdBy: i.user.login,
        lastActivityAt: last ? secs(last.created_at) : secs(i.updated_at),
        lastActor: last ? last.user.login : i.user.login,
        lastAction: last ? 'Kommentar' : 'angelegt',
        url: i.html_url,
      });
    }
  }
  return threads;
}
