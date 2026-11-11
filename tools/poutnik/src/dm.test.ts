// Tests für dm.ts: NIP-17-Verpackung mit lokalen Schlüsseln, ohne Netz und ohne Amber.
import { assertEquals, assertRejects } from 'jsr:@std/assert@^1.0.0';
import { generateSecretKey, getPublicKey, verifyEvent } from 'npm:nostr-tools@2.10.4';
import { buildRumor, cmdDm, dmRelaysFrom, localSigner, toHex, unwrap, wrapFor, type DmDeps } from './dm.ts';
import type { NostrEvent } from './relays.ts';

const POUTNIK_HEX = '6a90adda7da538994ee435d0ee03edde050d806ece4b4a8aa1fb45f04df54777';
const POUTNIK_NPUB = 'npub1d2g2mkna55ufjnhyxhgwuqldmczsmqrwee954z4pldzlqn04gamstvkeev';
const NOW = 1_800_000_000;

Deno.test('wrapFor/unwrap: Empfänger liest Text und Absender, Hülle trägt nur den p-Tag', async () => {
  const skA = generateSecretKey(), skB = generateSecretKey();
  const a = localSigner(skA), b = localSigner(skB);
  const pkA = getPublicKey(skA), pkB = getPublicKey(skB);
  const rumor = buildRumor(pkA, pkB, 'Hallo, ein Pad-Account?', NOW);
  const wrap = await wrapFor(pkB, rumor, a, NOW, () => 0.5);
  assertEquals(wrap.kind, 1059);
  assertEquals(wrap.tags, [['p', pkB]]);
  assertEquals(wrap.pubkey === pkA, false); // Einmalschlüssel, nicht der Absender
  assertEquals(verifyEvent(wrap as never), true);
  assertEquals(wrap.created_at, NOW - 86400); // halbe Spanne von zwei Tagen
  const { from, rumor: r } = await unwrap(wrap, b);
  assertEquals(from, pkA);
  assertEquals(r.content, 'Hallo, ein Pad-Account?');
  assertEquals(r.id, rumor.id);
});

Deno.test('unwrap: ein Dritter kann die Hülle nicht öffnen', async () => {
  const skA = generateSecretKey(), skB = generateSecretKey();
  const pkB = getPublicKey(skB);
  const wrap = await wrapFor(pkB, buildRumor(getPublicKey(skA), pkB, 'geheim', NOW), localSigner(skA), NOW);
  await assertRejects(() => unwrap(wrap, localSigner(generateSecretKey())));
});

Deno.test('dmRelaysFrom: neuestes kind 10050, ohne Schrägstrich, ohne Duplikate', () => {
  const ev = (created_at: number, relays: string[]): NostrEvent =>
    ({ id: String(created_at), kind: 10050, pubkey: POUTNIK_HEX, created_at, tags: relays.map((r) => ['relay', r]), content: '', sig: '' });
  assertEquals(dmRelaysFrom([ev(1, ['wss://alt.example']), ev(2, ['wss://dm.edufeed.org/', 'wss://dm.edufeed.org'])], POUTNIK_HEX), [
    'wss://dm.edufeed.org',
  ]);
  assertEquals(dmRelaysFrom([], POUTNIK_HEX), []);
});

Deno.test('toHex: npub und hex', () => {
  assertEquals(toHex(POUTNIK_NPUB), POUTNIK_HEX);
  assertEquals(toHex(POUTNIK_HEX), POUTNIK_HEX);
});

function fakeDeps(sk: Uint8Array, recipient: string, logs: string[], published: NostrEvent[]): DmDeps {
  const me = getPublicKey(sk);
  const liste = (pubkey: string): NostrEvent =>
    ({ id: pubkey, kind: 10050, pubkey, created_at: 1, tags: [['relay', 'wss://dm.example/']], content: '', sig: '' });
  return {
    env: { POUTNIK_PUBKEY_HEX: me },
    query: () => Promise.resolve({ events: [liste(recipient), liste(me)], warnings: [] }),
    connect: () => Promise.resolve(localSigner(sk)),
    publish: (url, ev) => {
      published.push(ev);
      return Promise.resolve({ url, ok: true, msg: '' });
    },
    now: () => NOW,
    out: (s) => logs.push(s),
    err: (s) => logs.push(s),
  };
}

Deno.test('cmdDm send: ohne --send wird nichts veröffentlicht', async () => {
  const sk = generateSecretKey(), empf = getPublicKey(generateSecretKey());
  const logs: string[] = [], pub: NostrEvent[] = [];
  assertEquals(await cmdDm(['send', empf, '--text', 'Probe'], fakeDeps(sk, empf, logs, pub)), 0);
  assertEquals(pub.length, 0);
  assertEquals(logs.some((l) => l.includes('Probelauf')), true);
});

Deno.test('cmdDm send --send: Hülle an Empfänger und Kopie an Poutník', async () => {
  const sk = generateSecretKey(), skE = generateSecretKey(), empf = getPublicKey(skE);
  const logs: string[] = [], pub: NostrEvent[] = [];
  assertEquals(await cmdDm(['send', empf, '--text', 'Hallo', '--send'], fakeDeps(sk, empf, logs, pub)), 0);
  assertEquals(pub.length, 2);
  assertEquals(pub[0].tags, [['p', empf]]);
  assertEquals((await unwrap(pub[0], localSigner(skE))).rumor.content, 'Hallo');
  assertEquals(pub[1].tags, [['p', getPublicKey(sk)]]);
});
