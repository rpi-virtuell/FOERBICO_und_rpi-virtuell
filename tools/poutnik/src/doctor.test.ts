// Tests für doctor.ts: Einrichtung prüfen, ohne Netz, mit Fakes für Prozesse und Relays.
import { assert, assertEquals } from 'jsr:@std/assert@^1.0.0';
import { loadConfig } from './config.ts';
import { runDoctor, type DoctorDeps } from './doctor.ts';
import type { Runner } from './push.ts';
import type { NostrEvent } from './relays.ts';

const cfg = loadConfig();
const S = '1c5ff3caacd842c01dca8f378231b16617516d214da75c7aeabbe9e1efe9c0f6';

// Form wie `ngit account whoami --json` (3.0.4) sie wirklich ausgibt: aliases als Liste, active-Flag.
const whoamiOk = JSON.stringify({
  accounts: [
    { active: false, aliases: ['poutnik'], name: 'Poutník', npub: 'npub1d2g2mkna55ufjnhyxhgwuqldmczsmqrwee954z4pldzlqn04gamstvkeev', scopes: [] },
    { active: false, aliases: ['joerg'], name: 'joerglohrer', npub: 'npub1f7jar3qnu269uyx5p0e4v24hqxjnxysxudvujza2ur5ehltvdeqsly2fx9', scopes: [] },
  ],
});

function runner(overrides: Record<string, { code?: number; stdout?: string; hang?: boolean }> = {}): Runner {
  const defaults: Record<string, { code?: number; stdout?: string; hang?: boolean }> = {
    '--version': { stdout: 'ngit 3.0.4\n' },
    'account whoami': { stdout: whoamiOk },
  };
  const base = { ...defaults, ...overrides };
  // Überschreibungen zuerst prüfen, damit spezifischere Schlüssel („--signer poutnik“) vor allgemeinen greifen.
  const order = [...Object.keys(overrides), ...Object.keys(defaults)];
  return (cmd) => {
    const key = order.find((k) => cmd.join(' ').includes(k));
    const hit = key ? base[key] : {};
    if (hit.hang) return new Promise(() => {});
    return Promise.resolve({ code: hit.code ?? 0, stdout: hit.stdout ?? '', stderr: '' });
  };
}

function announcement(repoId: string, relays: string[], maintainers: string[], pubkey = S): NostrEvent {
  return {
    id: 'a'.repeat(64),
    kind: 30617,
    pubkey,
    created_at: 1,
    tags: [['d', repoId], ['relays', ...relays], ['maintainers', ...maintainers]],
    content: '',
    sig: 's',
  };
}

function deps(over: Partial<DoctorDeps> = {}): DoctorDeps {
  return {
    run: runner(),
    query: (_relays, filter) => {
      const d = (filter as { '#d'?: string[] })['#d']?.[0] ?? '';
      const repo = cfg.repos[d];
      return Promise.resolve({ events: repo ? [announcement(d, repo.relays, repo.maintainers, repo.owner)] : [], warnings: [] });
    },
    env: { POUTNIK_PUBKEY_HEX: 'x', JOERG_PUBKEY_HEX: 'y', FORGEJO_TOKEN_FILE: '/tmp/token' },
    config: cfg,
    timeoutMs: 1000,
    ...over,
  };
}

const byName = (checks: { name: string; ok: boolean; detail: string }[], name: string) => checks.find((c) => c.name.startsWith(name))!;

Deno.test('doctor: alles in Ordnung, wenn ngit 3.0.4, beide Aliase, Ankündigungen stimmen und env vollständig', async () => {
  const checks = await runDoctor(deps());
  assert(checks.every((c) => c.ok), JSON.stringify(checks.filter((c) => !c.ok)));
});

Deno.test('doctor: falsche ngit-Version schlägt fehl', async () => {
  const checks = await runDoctor(deps({ run: runner({ '--version': { stdout: 'ngit 2.5.0\n' } }) }));
  const c = byName(checks, 'ngit');
  assertEquals(c.ok, false);
  assert(c.detail.includes('2.5.0'));
});

Deno.test('doctor: fehlender Alias joerg wird benannt', async () => {
  const only = JSON.stringify({ accounts: [{ active: false, aliases: ['poutnik'], npub: 'npub1d2g2…' }] });
  const checks = await runDoctor(deps({ run: runner({ 'account whoami': { stdout: only } }) }));
  const c = byName(checks, 'Konten');
  assertEquals(c.ok, false);
  assert(c.detail.includes('joerg'));
});

Deno.test('doctor: Abweichung der Relays oder Maintainer in der Ankündigung wird gemeldet', async () => {
  const checks = await runDoctor(deps({
    query: (_r, filter) => {
      const d = (filter as { '#d'?: string[] })['#d']?.[0] ?? '';
      const repo = cfg.repos[d];
      // Ankündiger (maintainers[0]) zählt implizit; weggelassen wird der letzte, damit eine echte Abweichung entsteht.
      return Promise.resolve({ events: [announcement(d, ['wss://anders.example'], repo.maintainers.slice(0, -1))], warnings: [] });
    },
  }));
  const c = byName(checks, 'Ankündigung edufeed-app');
  assertEquals(c.ok, false);
  assert(c.detail.includes('wss://anders.example'));
  assert(c.detail.toLowerCase().includes('maintainer'));
});

Deno.test('doctor: fehlende Umgebungsvariable wird gemeldet', async () => {
  const checks = await runDoctor(deps({ env: { POUTNIK_PUBKEY_HEX: 'x' } }));
  const c = byName(checks, 'Umgebung');
  assertEquals(c.ok, false);
  assert(c.detail.includes('FORGEJO_TOKEN_FILE'));
});

Deno.test('doctor: hängender Bunker-Aufruf läuft in den Timeout statt zu blockieren', async () => {
  const checks = await runDoctor(deps({ run: runner({ '--signer poutnik': { hang: true } }), timeoutMs: 100 }));
  const c = byName(checks, 'Signer poutnik');
  assertEquals(c.ok, false);
  assert(c.detail.includes('0,1 s'));
});

Deno.test('doctor: Signer-Check nennt ehrlich, dass Amber nicht angesprochen wird', async () => {
  const checks = await runDoctor(deps());
  const c = byName(checks, 'Signer poutnik');
  assertEquals(c.ok, true);
  assert(c.detail.toLowerCase().includes('nicht geprüft'));
});

Deno.test('doctor: Ankündiger zählt als Maintainer, auch ohne maintainers-Tag (poutnik-test unter Jörg)', async () => {
  const JOERG = '4fa5d1c413e2b45e10d40bf3562ab701a5331206e359c90baae0e99bfd6c6e41';
  const checks = await runDoctor(deps({
    query: (_r, filter) => {
      const d = (filter as { '#d'?: string[] })['#d']?.[0] ?? '';
      const repo = cfg.repos[d];
      if (d === 'poutnik-test') {
        return Promise.resolve({ events: [{ ...announcement(d, repo.relays, []), pubkey: JOERG, tags: [['d', d], ['relays', ...repo.relays]] }], warnings: [] });
      }
      return Promise.resolve({ events: [announcement(d, repo.relays, repo.maintainers, repo.owner)], warnings: [] });
    },
  }));
  const c = byName(checks, 'Ankündigung poutnik-test');
  assertEquals(c.ok, true, c.detail);
});
