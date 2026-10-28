// Tests für push.ts: pr/* nur als poutnik, main nur als joerg, Patch-Rückfall abbrechen.
import { assert, assertEquals } from 'jsr:@std/assert@^1.0.0';
import { checkPush, cmdPush, detectPatchFallback, detectPrSuccess, type Runner } from './push.ts';

Deno.test('checkPush: pr/-Branch als poutnik ergibt git push mit nostr.signer=poutnik', () => {
  const d = checkPush('pr/prototyp-5', 'poutnik');
  assert(d.ok);
  assertEquals(d.signer, 'poutnik');
  assertEquals(d.args, ['git', '-c', 'nostr.signer=poutnik', 'push', '-u', 'origin', 'pr/prototyp-5']);
});

Deno.test('checkPush: main als joerg ergibt git push origin main', () => {
  const d = checkPush('main', 'joerg');
  assert(d.ok);
  assertEquals(d.args, ['git', '-c', 'nostr.signer=joerg', 'push', 'origin', 'main']);
});

Deno.test('checkPush: pr/-Branch als joerg wird abgelehnt und nennt poutnik', () => {
  const d = checkPush('pr/x', 'joerg');
  assert(!d.ok);
  assert(d.reason.includes('pr/') && d.reason.includes('poutnik'));
});

Deno.test('checkPush: main als poutnik wird abgelehnt', () => {
  const d = checkPush('main', 'poutnik');
  assert(!d.ok);
});

Deno.test('checkPush: andere Branches werden abgelehnt', () => {
  assert(!checkPush('feature/x', 'joerg').ok);
  assert(!checkPush('feature/x', 'poutnik').ok);
});

Deno.test('checkPush: unbekannter Signer wird abgelehnt', () => {
  assert(!checkPush('main', 'alice').ok);
});

Deno.test('detectPatchFallback: erkennt „kind 1617“ und „as patches“, nicht aber Hex-IDs, pr/patch-Branches oder „old patch“', () => {
  assertEquals(detectPatchFallback('no grasp server available, sending as patches (kind 1617)'), true);
  assertEquals(detectPatchFallback('published 2 patch events (kind: 1617)'), true);
  assertEquals(detectPatchFallback('refs/nostr/ede6c25b827998b4ae22ff51dbb5954cbd7e3556868f4dc5c0081350cf8ce093 -> pr/patch-lizenzpille'), false);
  assertEquals(detectPatchFallback('proposal revision as new PR event, and a close status for the old patch'), false);
  assertEquals(detectPatchFallback('posting proposal as PR event\nPublished 1 PR to 4/5 relays'), false);
});

Deno.test('detectPrSuccess: pr/-Push gilt nur mit PR-Marker in der Ausgabe als Erfolg', () => {
  assertEquals(detectPrSuccess('signing event (Pull Request) with remote signer...\nposting proposal as PR event\nPublished 1 PR to 4/5 relays'), true);
  assertEquals(detectPrSuccess('Everything up-to-date'), false);
});

Deno.test('cmdPush: pr/-Push ohne PR-Marker endet mit Exit 1 und Hinweis auf gitworkshop, nicht „kein PR gesendet“', async () => {
  const calls: string[][] = [];
  const run = runner([
    { cmd: 'rev-parse --abbrev-ref HEAD', stdout: 'pr/x\n' },
    { cmd: 'push', stdout: 'To nostr://x\n * [new branch] pr/x -> pr/x' },
  ], calls);
  const out: string[] = [];
  const code = await cmdPush(['pr/x', '--as', 'poutnik'], run, { log: (s) => out.push(s) });
  assertEquals(code, 1);
  assert(out.join('\n').includes('gitworkshop'));
  assert(!out.join('\n').includes('kein PR gesendet'));
});

Deno.test('cmdPush: Timeout beim Push bricht mit Amber-Hinweis ab (Exit 1)', async () => {
  const run: Runner = (cmd) => {
    if (cmd.join(' ').includes('rev-parse')) return Promise.resolve({ code: 0, stdout: 'main\n', stderr: '' });
    return new Promise(() => {});
  };
  const out: string[] = [];
  const code = await cmdPush(['main', '--as', 'joerg', '--timeout', '0.1'], run, { log: (s) => out.push(s) });
  assertEquals(code, 1);
  assert(out.join('\n').includes('Amber'));
});

function runner(script: { cmd: string; code?: number; stdout?: string; stderr?: string }[], calls: string[][]): Runner {
  return (cmd) => {
    calls.push(cmd);
    const key = cmd.join(' ');
    const hit = script.find((s) => key.includes(s.cmd));
    return Promise.resolve({ code: hit?.code ?? 0, stdout: hit?.stdout ?? '', stderr: hit?.stderr ?? '' });
  };
}

Deno.test('cmdPush: bricht bei Patch-Rückfall mit Exit 1 ab und ruft nicht noch einmal', async () => {
  const calls: string[][] = [];
  const run = runner([
    { cmd: 'rev-parse --abbrev-ref HEAD', stdout: 'pr/x\n' },
    { cmd: 'push', stdout: 'falling back to patches (kind 1617)' },
  ], calls);
  const code = await cmdPush(['pr/x', '--as', 'poutnik'], run);
  assertEquals(code, 1);
  assertEquals(calls.filter((c) => c.includes('push')).length, 1);
});

Deno.test('cmdPush: lehnt ab, wenn der ausgecheckte Branch nicht der genannte ist', async () => {
  const calls: string[][] = [];
  const run = runner([{ cmd: 'rev-parse --abbrev-ref HEAD', stdout: 'main\n' }], calls);
  const code = await cmdPush(['pr/x', '--as', 'poutnik'], run);
  assertEquals(code, 1);
  assertEquals(calls.filter((c) => c.includes('push')).length, 0);
});

Deno.test('cmdPush: erfolgreicher Push gibt 0 zurück und nutzt --cwd', async () => {
  const calls: string[][] = [];
  const seenCwd: (string | undefined)[] = [];
  const run: Runner = (cmd, cwd) => {
    seenCwd.push(cwd);
    return runner([{ cmd: 'rev-parse --abbrev-ref HEAD', stdout: 'main\n' }], calls)(cmd, cwd);
  };
  const code = await cmdPush(['main', '--as', 'joerg', '--cwd', '/tmp/klon'], run);
  assertEquals(code, 0);
  assert(seenCwd.every((c) => c === '/tmp/klon'));
});
