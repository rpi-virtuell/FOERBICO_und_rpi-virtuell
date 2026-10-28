// Push-Wrapper (Spec 4.6): pr/* nur mit Signer poutnik, main nur mit joerg; Patch-Rückfall abbrechen.

export type Signer = 'poutnik' | 'joerg';

export type PushDecision = { ok: true; signer: Signer; args: string[] } | { ok: false; reason: string };

export type RunResult = { code: number; stdout: string; stderr: string; timedOut?: boolean };
export type Runner = (cmd: string[], cwd?: string, timeoutMs?: number) => Promise<RunResult>;
export type PushIo = { log: (s: string) => void };
const DEFAULT_TIMEOUT_S = 180;

export function checkPush(branch: string, signer: string): PushDecision {
  if (signer !== 'poutnik' && signer !== 'joerg') return { ok: false, reason: `Unbekannter Signer „${signer}“ (erlaubt: poutnik, joerg)` };
  if (branch.startsWith('pr/')) {
    if (signer !== 'poutnik') return { ok: false, reason: `Branch ${branch}: pr/-Branches werden nur als poutnik gepusht, nicht als ${signer}` };
    return { ok: true, signer, args: ['git', '-c', 'nostr.signer=poutnik', 'push', '-u', 'origin', branch] };
  }
  if (branch === 'main') {
    if (signer !== 'joerg') return { ok: false, reason: `Branch main wird nur als joerg gepusht, nicht als ${signer}` };
    return { ok: true, signer, args: ['git', '-c', 'nostr.signer=joerg', 'push', 'origin', 'main'] };
  }
  return { ok: false, reason: `Branch ${branch}: nur pr/* (als poutnik) und main (als joerg) sind erlaubt` };
}

/** Erkennt, dass ngit Patches (kind 1617) statt eines Pull Requests gesendet hat. Eng gefasst (Review I1):
 *  nur „kind 1617“/„kind: 1617“ oder „as patches“, damit Hex-IDs, Branch-Namen wie pr/patch-… und
 *  ngits Erfolgsmeldung („… for the old patch“) nicht anschlagen. */
export function detectPatchFallback(output: string): boolean {
  const t = output.toLowerCase();
  return /kind:?\s*1617\b/.test(t) || /\bas patch(es)?\b/.test(t);
}

/** Positivmarker: ngit hat ein PR-Event veröffentlicht. */
export function detectPrSuccess(output: string): boolean {
  const t = output.toLowerCase();
  return t.includes('proposal as pr event') || /published \d+ pr\b/.test(t) || t.includes('pr event');
}

export const defaultRunner: Runner = async (cmd, cwd, timeoutMs) => {
  const child = new Deno.Command(cmd[0], { args: cmd.slice(1), cwd, stdout: 'piped', stderr: 'piped' }).spawn();
  let timer: ReturnType<typeof setTimeout> | undefined;
  let timedOut = false;
  if (timeoutMs) {
    timer = setTimeout(() => {
      timedOut = true;
      try {
        child.kill('SIGTERM');
      } catch { /* schon beendet */ }
    }, timeoutMs);
  }
  const out = await child.output();
  clearTimeout(timer);
  const dec = new TextDecoder();
  return { code: timedOut ? -1 : out.code, stdout: dec.decode(out.stdout), stderr: dec.decode(out.stderr), timedOut };
};

function withTimeout(p: Promise<RunResult>, ms: number): Promise<RunResult> {
  let t: ReturnType<typeof setTimeout> | undefined;
  const timer = new Promise<RunResult>((res) => {
    t = setTimeout(() => res({ code: -1, stdout: '', stderr: '', timedOut: true }), ms);
  });
  return Promise.race([p, timer]).finally(() => clearTimeout(t));
}

function parseArgs(argv: string[]): { branch?: string; as?: string; cwd?: string; timeoutS: number } {
  const o: { branch?: string; as?: string; cwd?: string; timeoutS: number } = { timeoutS: DEFAULT_TIMEOUT_S };
  for (let i = 0; i < argv.length; i++) {
    if (argv[i] === '--as') o.as = argv[++i];
    else if (argv[i] === '--cwd') o.cwd = argv[++i];
    else if (argv[i] === '--timeout') o.timeoutS = Number(argv[++i]);
    else if (!o.branch) o.branch = argv[i];
  }
  if (!Number.isFinite(o.timeoutS) || o.timeoutS <= 0) o.timeoutS = DEFAULT_TIMEOUT_S;
  return o;
}

export async function cmdPush(argv: string[], run: Runner = defaultRunner, io: PushIo = { log: (s) => console.error(s) }): Promise<number> {
  const { branch, as, cwd, timeoutS } = parseArgs(argv);
  if (!branch || !as) {
    io.log('Aufruf: push <branch> --as poutnik|joerg [--cwd <klon>] [--timeout <s>]');
    return 2;
  }
  const d = checkPush(branch, as);
  if (!d.ok) {
    io.log(`Abgelehnt: ${d.reason}`);
    return 1;
  }
  const head = await run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], cwd);
  const current = head.stdout.trim();
  if (head.code !== 0 || current !== branch) {
    io.log(`Abgelehnt: ausgecheckt ist „${current || '?'}“, gepusht werden soll „${branch}“`);
    return 1;
  }
  if (d.signer === 'joerg') io.log('Hinweis: Amber fragt am Handy nach der Freigabe für den Repo-Stand (kind 30618).');
  const timeoutMs = timeoutS * 1000;
  const res = await withTimeout(run(d.args, cwd, timeoutMs), timeoutMs);
  const output = res.stdout + '\n' + res.stderr;
  if (output.trim()) io.log(output.trim());
  if (res.timedOut) {
    io.log(`Abgebrochen: keine Antwort vom Signer in ${timeoutS} s. Ist Amber am Handy geöffnet und online? Stand des Pushes auf gitworkshop prüfen.`);
    return 1;
  }
  if (detectPatchFallback(output)) {
    io.log('Achtung: Die Ausgabe deutet auf Patches (kind 1617) statt eines Pull Requests hin. Status auf gitworkshop prüfen, nicht wiederholen.');
    return 1;
  }
  if (res.code !== 0) return 1;
  if (branch.startsWith('pr/') && !detectPrSuccess(output)) {
    io.log('Ergebnis unklar: git hat gepusht, aber ngit meldet kein PR-Event. Bitte auf gitworkshop prüfen, bevor etwas wiederholt wird.');
    return 1;
  }
  return 0;
}
