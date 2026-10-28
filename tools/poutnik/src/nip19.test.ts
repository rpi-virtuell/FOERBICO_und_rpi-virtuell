// Tests für nip19.ts: npub/nevent (bech32 + TLV) so, wie ngit und gitworkshop sie verwenden.
import { assertEquals } from 'jsr:@std/assert@^1.0.0';
import { decodeNip19, neventEncode, npubEncode, npubDecode } from './nip19.ts';

const POUTNIK_HEX = '6a90adda7da538994ee435d0ee03edde050d806ece4b4a8aa1fb45f04df54777';
const POUTNIK_NPUB = 'npub1d2g2mkna55ufjnhyxhgwuqldmczsmqrwee954z4pldzlqn04gamstvkeev';
// nevent aus `ngit issue list --json` für „Kommentare auf verknüpften Events zusammenführen“ (Issue-ID 4e5417f8a6…)
const NGIT_NEVENT = 'nevent1qqsyu4qhlzn92ppuyh3lcy9ccdmrnstfemrqgm3wypwk6nqac9gqzmgpz3mhxue69uhhyetvv9ujumn8d96zuer9wcdmqc6w';

Deno.test('npubEncode/npubDecode: Poutníks Schlüssel hin und zurück', () => {
  assertEquals(npubEncode(POUTNIK_HEX), POUTNIK_NPUB);
  assertEquals(npubDecode(POUTNIK_NPUB), POUTNIK_HEX);
});

Deno.test('decodeNip19: nevent von ngit enthält die Issue-ID und den Relay-Hint', () => {
  const d = decodeNip19(NGIT_NEVENT);
  assertEquals(d.type, 'nevent');
  assertEquals(d.id.startsWith('4e5417f8a6'), true);
  assertEquals(d.relays, ['wss://relay.ngit.dev']);
});

Deno.test('neventEncode: erzeugt aus ID und Relay dieselbe Kennung wie ngit', () => {
  const d = decodeNip19(NGIT_NEVENT);
  assertEquals(neventEncode({ id: d.id, relays: d.relays, author: d.author }), NGIT_NEVENT);
});
