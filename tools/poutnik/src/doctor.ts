// doctor (Spec 4.8): prüft ngit-Version, Konto-Aliase, Bunker-Erreichbarkeit, Umgebungsdatei
// und ob Relays/Maintainer der Repo-Ankündigungen (kind 30617) zur config.json passen.
import { loadConfig, loadEnv, type Config } from './config.ts';
import { npubDecode } from './nip19.ts';
import type { QueryFn } from './nostr.ts';
import { defaultRunner, type Runner } from './push.ts';
import { queryRelays } from './relays.ts';

export type Check = { name: string; ok: boolean; detail: string };

export type DoctorDeps = {
  run: Runner;
  query: QueryFn;
  env: Record<string, string>;
  config: Config;
  timeoutMs?: number;
};

const NGIT_VERSION = '3.0.4';
const ENV_REQUIRED = ['POUTNIK_PUBKEY_HEX', 'JOERG_PUBKEY_HEX', 'FORGEJO_TOKEN_FILE'];

function withTimeout<T>(p: Promise<T>, ms: number): Promise<T | 'timeout'> {
  let t: ReturnType<typeof setTimeout> | undefined;
  const timer = new Promise<'timeout'>((res) => {
    t = setTimeout(() => res('timeout'), ms);
  });
  return Promise.race([p, timer]).finally(() => clearTimeout(t));
}

const sekunden = (ms: number) => (ms / 1000).toLocaleString('de-DE', { maximumFractionDigits: 1 }) + ' s';

export async function runDoctor(d: DoctorDeps): Promise<Check[]> {
  const timeoutMs = d.timeoutMs ?? 20_000;
  const checks: Check[] = [];

  // ngit-Version
  const ver = await withTimeout(d.run(['ngit', '--version']), timeoutMs);
  const verText = ver === 'timeout' ? '' : ver.stdout.trim();
  checks.push({
    name: 'ngit',
    ok: verText.includes(NGIT_VERSION),
    detail: ver === 'timeout' ? `keine Antwort in ${sekunden(timeoutMs)}` : verText || 'nicht gefunden',
  });

  // Konto-Aliase
  const who = await withTimeout(d.run(['ngit', 'account', 'whoami', '--json']), timeoutMs);
  const aliases = new Map<string, string>();
  if (who !== 'timeout' && who.code === 0) {
    try {
      // ngit 3.0.4: accounts[].aliases ist eine Liste; `alias` als Einzelfeld nur zur Sicherheit.
      const parsed = JSON.parse(who.stdout) as { accounts?: { alias?: string; aliases?: string[]; npub?: string }[] };
      for (const a of parsed.accounts ?? []) {
        for (const alias of [...(a.aliases ?? []), ...(a.alias ? [a.alias] : [])]) aliases.set(alias, a.npub ?? '');
      }
    } catch { /* kein JSON */ }
  }
  const fehlend = ['poutnik', 'joerg'].filter((a) => !aliases.has(a));
  checks.push({
    name: 'Konten (ngit-Aliase)',
    ok: fehlend.length === 0,
    detail: fehlend.length ? `fehlt: ${fehlend.join(', ')}` : [...aliases.entries()].map(([a, n]) => `${a} → ${n.slice(0, 12)}…`).join(', '),
  });
  for (const [alias, npub] of aliases) {
    const soll = d.config.identities.find((i) => i.alias === alias)?.pubkey;
    if (!soll || !npub.startsWith('npub1') || npub.length !== 63) continue;
    let hex = '';
    try {
      hex = npubDecode(npub);
    } catch { /* unbrauchbar */ }
    if (hex && hex !== soll) checks.push({ name: `Konto ${alias}`, ok: false, detail: `npub ${npub.slice(0, 12)}… ist nicht der konfigurierte Schlüssel` });
  }

  // Signer je Alias: prüft, dass ngit das Konto auflösen kann. Ob Amber wirklich antwortet, zeigt erst eine
  // Signatur (Review I3); darum steht das ehrlich im Detail, und der Timeout fängt einen hängenden Aufruf ab.
  for (const alias of ['poutnik', 'joerg']) {
    if (!aliases.has(alias)) continue;
    const r = await withTimeout(d.run(['ngit', '--signer', alias, 'account', 'whoami']), timeoutMs);
    checks.push({
      name: `Signer ${alias} (ngit)`,
      ok: r !== 'timeout' && r.code === 0,
      detail: r === 'timeout'
        ? `keine Antwort in ${sekunden(timeoutMs)} (Amber geöffnet? Handy online?)`
        : r.code === 0
        ? 'Konto auflösbar; Amber selbst wird hier nicht geprüft, erst beim Signieren'
        : (r.stderr || r.stdout).trim().slice(0, 160),
    });
  }

  // Umgebungsdatei
  const envFehlt = ENV_REQUIRED.filter((k) => !d.env[k]);
  checks.push({ name: 'Umgebung (~/.config/poutnik/env)', ok: envFehlt.length === 0, detail: envFehlt.length ? `fehlt: ${envFehlt.join(', ')}` : 'vollständig' });

  // Repo-Ankündigungen
  for (const repo of Object.values(d.config.repos)) {
    const r = await withTimeout(d.query(repo.readRelays, { kinds: [30617], authors: [repo.owner], '#d': [repo.id] }), timeoutMs);
    if (r === 'timeout' || r.events.length === 0) {
      checks.push({ name: `Ankündigung ${repo.id}`, ok: false, detail: r === 'timeout' ? `keine Antwort in ${sekunden(timeoutMs)}` : 'nicht gefunden' + (r.warnings.length ? ` (${r.warnings.join('; ')})` : '') });
      continue;
    }
    const ev = r.events.sort((a, b) => b.created_at - a.created_at)[0];
    const relays = (ev.tags.find((t) => t[0] === 'relays') ?? []).slice(1).map((u) => u.replace(/\/+$/, ''));
    // NIP-34: Der Ankündiger ist selbst Maintainer, auch wenn er nicht im maintainers-Tag steht.
    const maint = [...new Set([ev.pubkey, ...(ev.tags.find((t) => t[0] === 'maintainers') ?? []).slice(1)])];
    const relaysSoll = repo.relays.map((u) => u.replace(/\/+$/, ''));
    const diffs: string[] = [];
    const relayDiff = [...relays.filter((x) => !relaysSoll.includes(x)), ...relaysSoll.filter((x) => !relays.includes(x))];
    if (relayDiff.length) diffs.push(`Relays weichen ab: ${relayDiff.join(', ')}`);
    const maintDiff = [...maint.filter((x) => !repo.maintainers.includes(x)), ...repo.maintainers.filter((x) => !maint.includes(x))];
    if (maintDiff.length) diffs.push(`Maintainer weichen ab: ${maintDiff.map((m) => m.slice(0, 8) + '…').join(', ')}`);
    checks.push({ name: `Ankündigung ${repo.id}`, ok: diffs.length === 0, detail: diffs.length ? diffs.join('; ') : `${relays.length} Relays, ${maint.length} Maintainer wie konfiguriert` });
  }
  return checks;
}

export async function cmdDoctor(_argv: string[]): Promise<number> {
  const checks = await runDoctor({ run: defaultRunner, query: (relays, filter) => queryRelays(relays, filter), env: loadEnv(), config: loadConfig() });
  for (const c of checks) console.log(`${c.ok ? '✓' : '✗'} ${c.name} — ${c.detail}`);
  return checks.every((c) => c.ok) ? 0 : 1;
}
