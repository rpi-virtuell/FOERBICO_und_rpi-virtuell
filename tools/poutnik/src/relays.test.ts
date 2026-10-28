// Tests für relays.ts: Relay-Abfrage ohne Netz über einen WebSocket-Fake.
import { assertEquals, assert } from 'jsr:@std/assert@^1.0.0';
import { queryRelays, type SocketFactory } from './relays.ts';

type Handler = ((ev: { data: string }) => void) | null;

/** Baut einen WebSocket-Fake, der auf REQ die gegebenen Relay-Nachrichten schickt. */
function fakeFactory(script: (subId: string) => unknown[][]): SocketFactory {
  return (_url: string) => {
    const sock = {
      onopen: null as (() => void) | null,
      onmessage: null as Handler,
      onerror: null as ((e: unknown) => void) | null,
      onclose: null as (() => void) | null,
      send(raw: string) {
        const [, subId] = JSON.parse(raw) as [string, string];
        for (const msg of script(subId)) sock.onmessage?.({ data: JSON.stringify(msg) });
      },
      close() {
        sock.onclose?.();
      },
    };
    queueMicrotask(() => sock.onopen?.());
    return sock;
  };
}

const ev = (id: string) => ({ id, kind: 1, pubkey: 'p', created_at: 1, tags: [], content: '', sig: 's' });

Deno.test('queryRelays: dedupliziert Events nach id und endet bei EOSE', async () => {
  const factory = fakeFactory((sub) => [['EVENT', sub, ev('a')], ['EVENT', sub, ev('a')], ['EVENT', sub, ev('b')], ['EOSE', sub]]);
  const { events, warnings } = await queryRelays(['wss://x', 'wss://y'], { kinds: [1] }, { socketFactory: factory });
  assertEquals(events.map((e) => e.id).sort(), ['a', 'b']);
  assertEquals(warnings, []);
});

Deno.test('queryRelays: CLOSED vom Relay wird zur Warnung mit Relay-Name', async () => {
  const factory = fakeFactory((sub) => [['CLOSED', sub, 'blocked: too many subscriptions']]);
  const { events, warnings } = await queryRelays(['wss://gesperrt'], { kinds: [1] }, { socketFactory: factory });
  assertEquals(events, []);
  assertEquals(warnings.length, 1);
  assert(warnings[0].includes('wss://gesperrt') && warnings[0].includes('blocked'));
});

Deno.test('queryRelays: Timeout ohne EOSE wird zur Warnung, Events bleiben erhalten', async () => {
  const factory = fakeFactory((sub) => [['EVENT', sub, ev('c')]]);
  const { events, warnings } = await queryRelays(['wss://lahm'], { kinds: [1] }, { socketFactory: factory, timeoutMs: 20 });
  assertEquals(events.map((e) => e.id), ['c']);
  assert(warnings[0].includes('wss://lahm') && warnings[0].toLowerCase().includes('timeout'));
});
