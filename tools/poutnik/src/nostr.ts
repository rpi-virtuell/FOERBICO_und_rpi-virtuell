// Fäden auf Nostr (gitworkshop): Issues (1621) und PRs (1618) von uns oder mit unserem Kommentar,
// Stand aus Status-Events (1630–1633) und Kommentaren (1111). Nur lesend, über queryRelays.
import type { RepoConfig } from './config.ts';
import { neventEncode } from './nip19.ts';
import { queryRelays, type NostrEvent } from './relays.ts';
import type { Thread, ThreadStatus } from './threads.ts';

export type QueryFn = (relays: string[], filter: object) => Promise<{ events: NostrEvent[]; warnings: string[] }>;

export type NostrOptions = {
  repos: RepoConfig[];
  me: string[]; // Pubkeys (hex) von Jörg und Poutník
  since: number; // Unix-Sekunden
  query?: QueryFn;
  chunk?: number; // IDs je Filter
};

const STATUS_BY_KIND: Record<number, ThreadStatus> = { 1630: 'open', 1631: 'resolved', 1632: 'closed', 1633: 'draft' };
const ACTION_BY_KIND: Record<number, string> = { 1630: 'wieder geöffnet', 1631: 'erledigt', 1632: 'geschlossen', 1633: 'Entwurf' };

const tag = (e: NostrEvent, name: string) => e.tags.find((t) => t[0] === name)?.[1];
const chunks = <T>(arr: T[], n: number): T[][] => Array.from({ length: Math.ceil(arr.length / n) }, (_, i) => arr.slice(i * n, (i + 1) * n));

export async function fetchNostrThreads(o: NostrOptions): Promise<{ threads: Thread[]; warnings: string[] }> {
  const query = o.query ?? ((relays, filter) => queryRelays(relays, filter));
  const chunk = o.chunk ?? 50;
  const threads: Thread[] = [];
  const warnings: string[] = [];
  const collect = async (relays: string[], filter: object): Promise<NostrEvent[]> => {
    const r = await query(relays, filter);
    warnings.push(...r.warnings);
    return r.events;
  };

  // Unsere eigenen Kommentare seit `since` (repo-unabhängig, einmal holen) → Wurzel-IDs, an denen wir beteiligt sind.
  const firstRelays = o.repos[0]?.readRelays ?? [];
  const myComments = o.repos.length ? await collect(firstRelays, { kinds: [1111], authors: o.me, since: o.since }) : [];
  const commentedRootIds = [...new Set(myComments.map((c) => tag(c, 'E')).filter((x): x is string => !!x))];

  for (const repo of o.repos) {
    const relays = repo.readRelays;
    // Wurzeln (Issues, PRs) OHNE Zeitfilter: eigene im Repo, plus die, die wir kürzlich kommentiert haben.
    // Das Zeitfenster gilt für die letzte Aktivität (Spec 4.4), nicht für das Anlegedatum (Review C1).
    const own = await collect(relays, { kinds: [1621, 1618], '#a': [repo.coordinate], authors: o.me });
    const commented = commentedRootIds.length ? await collect(relays, { kinds: [1621, 1618], ids: commentedRootIds }) : [];
    const byId = new Map<string, NostrEvent>();
    for (const r of [...own, ...commented]) {
      if (r.tags.some((t) => t[0] === 'a' && t[1] === repo.coordinate)) byId.set(r.id, r);
    }
    const mine = [...byId.values()];
    if (mine.length === 0) continue;
    const ids = mine.map((r) => r.id);
    const comments: NostrEvent[] = [];
    const statuses: NostrEvent[] = [];
    for (const part of chunks(ids, chunk)) {
      comments.push(...(await collect(relays, { kinds: [1111], '#E': part })));
      statuses.push(...(await collect(relays, { kinds: [1630, 1631, 1632, 1633], '#e': part })));
    }
    for (const root of mine) {
      const rootComments = comments.filter((c) => tag(c, 'E') === root.id);
      const rootStatus = statuses
        .filter((s) => s.tags.some((t) => t[0] === 'e' && t[1] === root.id) && (s.pubkey === root.pubkey || repo.maintainers.includes(s.pubkey)))
        .sort((a, b) => b.created_at - a.created_at);
      const latestStatus = rootStatus[0];
      const latestComment = rootComments.sort((a, b) => b.created_at - a.created_at)[0];
      let last: { at: number; actor: string; action: string } = { at: root.created_at, actor: root.pubkey, action: 'angelegt' };
      if (latestStatus && latestStatus.created_at > last.at) last = { at: latestStatus.created_at, actor: latestStatus.pubkey, action: ACTION_BY_KIND[latestStatus.kind] };
      if (latestComment && latestComment.created_at > last.at) last = { at: latestComment.created_at, actor: latestComment.pubkey, action: 'Kommentar' };
      if (last.at < o.since) continue; // keine Aktivität im Zeitfenster
      threads.push({
        source: 'nostr',
        repo: repo.id,
        kind: root.kind === 1618 ? 'pr' : 'issue',
        id: root.id,
        title: tag(root, 'subject') ?? root.content.split('\n')[0].slice(0, 80),
        status: latestStatus ? STATUS_BY_KIND[latestStatus.kind] : 'open',
        createdBy: root.pubkey,
        lastActivityAt: last.at,
        lastActor: last.actor,
        lastAction: last.action,
        url: `https://gitworkshop.dev/${neventEncode({ id: root.id, relays: [repo.relays[0]], author: root.pubkey })}`,
      });
    }
  }
  return { threads, warnings };
}
