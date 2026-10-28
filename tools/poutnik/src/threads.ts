// „Wo stehen meine Fäden?“ (Spec 4.4): Fäden aus gitworkshop (Nostr) und Forgejo zusammenführen,
// nach letzter Aktivität sortieren, „wartet auf dich“ markieren. Nur lesend.
import { loadConfig, loadEnv } from './config.ts';
import { fetchForgejoThreads, ForgejoAuthError } from './forgejo.ts';
import { fetchNostrThreads } from './nostr.ts';

export type ThreadStatus = 'open' | 'resolved' | 'closed' | 'draft';

export type Thread = {
  source: 'nostr' | 'forgejo';
  repo: string;
  kind: 'issue' | 'pr';
  id: string;
  title: string;
  status: ThreadStatus;
  createdBy: string;
  lastActivityAt: number; // Unix-Sekunden
  lastActor: string;
  lastAction: string;
  url: string;
};

export type RankedThread = Thread & { waitingOnMe: boolean };

export type Part = { threads: Thread[]; warnings: string[] };

/** Führt Teile zusammen, sortiert absteigend nach Aktivität; wartet auf mich = letzter Akteur ist keiner von `me`. */
export function mergeThreads(parts: Part[], me: string[]): { threads: RankedThread[]; warnings: string[] } {
  const mine = new Set(me);
  const threads = parts
    .flatMap((p) => p.threads)
    .map((t) => ({ ...t, waitingOnMe: !mine.has(t.lastActor) }))
    .sort((a, b) => b.lastActivityAt - a.lastActivityAt);
  return { threads, warnings: parts.flatMap((p) => p.warnings) };
}

const TITLE_MAX = 60;
const datum = (secs: number) => new Date(secs * 1000).toISOString().slice(0, 10);
const kurz = (s: string, n: number) => (s.length > n ? s.slice(0, n) + '…' : s);
const wer = (actor: string) => (/^[0-9a-f]{64}$/.test(actor) ? actor.slice(0, 8) + '…' : actor);

export function formatThreadLine(t: RankedThread): string {
  const mark = t.waitingOnMe ? '→' : ' ';
  const quelle = t.source === 'nostr' ? 'gitworkshop' : 'forgejo';
  return `${mark} ${datum(t.lastActivityAt)} | ${quelle} | ${t.repo} | ${kurz(t.title, TITLE_MAX)} | ${t.status} | ${wer(t.lastActor)}: ${t.lastAction} | ${t.url}`;
}

export type ThreadsDeps = {
  nostr: (since: number, repoFilter?: string) => Promise<Part>;
  forgejo: (since: Date) => Promise<Thread[]>;
  print: (s: string) => void;
  me: string[];
};

function parseArgs(argv: string[]): { sinceDays: number; json: boolean; repo?: string } {
  const o = { sinceDays: 30, json: false } as { sinceDays: number; json: boolean; repo?: string };
  for (let i = 0; i < argv.length; i++) {
    if (argv[i] === '--since') o.sinceDays = Number(argv[++i]);
    else if (argv[i] === '--json') o.json = true;
    else if (argv[i] === '--repo') o.repo = argv[++i];
  }
  if (!Number.isFinite(o.sinceDays) || o.sinceDays <= 0) o.sinceDays = 30;
  return o;
}

function defaultDeps(): ThreadsDeps {
  const cfg = loadConfig();
  const env = loadEnv();
  const me = [...cfg.identities.map((i) => i.pubkey), cfg.forgejo.login];
  return {
    me,
    print: (s) => console.log(s),
    nostr: (since, repoFilter) =>
      fetchNostrThreads({
        repos: Object.values(cfg.repos).filter((r) => !repoFilter || r.id === repoFilter),
        me: cfg.identities.map((i) => i.pubkey),
        since,
      }),
    forgejo: async (since) => {
      const file = env.FORGEJO_TOKEN_FILE ?? `${Deno.env.get('HOME')}/.config/forgejo/token.txt`;
      let token: string;
      try {
        token = (await Deno.readTextFile(file)).trim();
      } catch {
        throw new ForgejoAuthError(`Forgejo: Token-Datei ${file} nicht lesbar`);
      }
      return fetchForgejoThreads({ base: cfg.forgejo.base, repos: cfg.forgejo.repos, token, since });
    },
  };
}

export async function cmdThreads(argv: string[], deps: ThreadsDeps = defaultDeps()): Promise<number> {
  const { sinceDays, json, repo } = parseArgs(argv);
  const sinceSecs = Math.floor(Date.now() / 1000) - sinceDays * 86_400;
  const parts: Part[] = [];
  parts.push(await deps.nostr(sinceSecs, repo));
  if (!repo) {
    try {
      parts.push({ threads: await deps.forgejo(new Date(sinceSecs * 1000)), warnings: [] });
    } catch (e) {
      parts.push({ threads: [], warnings: [e instanceof Error ? e.message : String(e)] });
    }
  }
  const { threads, warnings } = mergeThreads(parts, deps.me);
  if (json) {
    deps.print(JSON.stringify({ threads, warnings }, null, 2));
    return 0;
  }
  deps.print(`Fäden der letzten ${sinceDays} Tage (→ = wartet auf dich):`);
  if (threads.length === 0) deps.print('  keine');
  for (const t of threads) deps.print(formatThreadLine(t));
  for (const w of warnings) deps.print(`Warnung: ${w}`);
  return 0;
}
