// NIP-19: npub und nevent (bech32 mit TLV), ohne externe Abhängigkeit.
const CHARSET = 'qpzry9x8gf2tvdw0s3jn54khce6mua7l';
const GEN = [0x3b6a57b2, 0x26508e6d, 0x1ea119fa, 0x3d4233dd, 0x2a1462b3];

function polymod(values: number[]): number {
  let chk = 1;
  for (const v of values) {
    const b = chk >>> 25;
    chk = ((chk & 0x1ffffff) << 5) ^ v;
    for (let i = 0; i < 5; i++) if ((b >> i) & 1) chk ^= GEN[i];
  }
  return chk >>> 0;
}

const hrpExpand = (hrp: string) => [...hrp].map((c) => c.charCodeAt(0) >> 5).concat([0], [...hrp].map((c) => c.charCodeAt(0) & 31));

function convertBits(data: number[], from: number, to: number, pad: boolean): number[] {
  let acc = 0, bits = 0;
  const out: number[] = [];
  const max = (1 << to) - 1;
  for (const v of data) {
    acc = (acc << from) | v;
    bits += from;
    while (bits >= to) {
      bits -= to;
      out.push((acc >> bits) & max);
    }
  }
  if (pad && bits > 0) out.push((acc << (to - bits)) & max);
  return out;
}

function bech32Encode(hrp: string, bytes: Uint8Array): string {
  const data = convertBits([...bytes], 8, 5, true);
  const pm = polymod([...hrpExpand(hrp), ...data, 0, 0, 0, 0, 0, 0]) ^ 1;
  const chk = Array.from({ length: 6 }, (_, i) => (pm >> (5 * (5 - i))) & 31);
  return hrp + '1' + [...data, ...chk].map((d) => CHARSET[d]).join('');
}

function bech32Decode(s: string): { hrp: string; bytes: Uint8Array } {
  const low = s.toLowerCase();
  const pos = low.lastIndexOf('1');
  if (pos < 1) throw new Error('kein bech32: ' + s);
  const hrp = low.slice(0, pos);
  const data = [...low.slice(pos + 1)].map((c) => {
    const i = CHARSET.indexOf(c);
    if (i < 0) throw new Error('ungültiges Zeichen in ' + s);
    return i;
  });
  if (polymod([...hrpExpand(hrp), ...data]) !== 1) throw new Error('Prüfsumme falsch: ' + s);
  return { hrp, bytes: new Uint8Array(convertBits(data.slice(0, -6), 5, 8, false)) };
}

const hexToBytes = (h: string) => new Uint8Array(h.match(/.{2}/g)!.map((b) => parseInt(b, 16)));
const bytesToHex = (b: Uint8Array) => [...b].map((x) => x.toString(16).padStart(2, '0')).join('');

export function npubEncode(hex: string): string {
  return bech32Encode('npub', hexToBytes(hex));
}

export function npubDecode(npub: string): string {
  const { hrp, bytes } = bech32Decode(npub);
  if (hrp !== 'npub') throw new Error('kein npub: ' + npub);
  return bytesToHex(bytes);
}

export type NeventParts = { id: string; relays?: string[]; author?: string; kind?: number };

/** TLV: 0 = id (32 Byte), 1 = relay (utf8), 2 = author (32 Byte), 3 = kind (uint32). */
export function neventEncode(p: NeventParts): string {
  const enc = new TextEncoder();
  const parts: number[] = [];
  const push = (t: number, v: Uint8Array) => parts.push(t, v.length, ...v);
  push(0, hexToBytes(p.id));
  for (const r of p.relays ?? []) push(1, enc.encode(r));
  if (p.author) push(2, hexToBytes(p.author));
  if (p.kind !== undefined) push(3, new Uint8Array([(p.kind >>> 24) & 255, (p.kind >>> 16) & 255, (p.kind >>> 8) & 255, p.kind & 255]));
  return bech32Encode('nevent', new Uint8Array(parts));
}

export type Decoded = { type: string; id: string; relays: string[]; author?: string; kind?: number };

export function decodeNip19(s: string): Decoded {
  const { hrp, bytes } = bech32Decode(s);
  if (hrp === 'npub') return { type: 'npub', id: bytesToHex(bytes), relays: [] };
  const out: Decoded = { type: hrp, id: '', relays: [] };
  const dec = new TextDecoder();
  for (let i = 0; i < bytes.length;) {
    const t = bytes[i], l = bytes[i + 1];
    const v = bytes.slice(i + 2, i + 2 + l);
    i += 2 + l;
    if (t === 0) out.id = bytesToHex(v);
    else if (t === 1) out.relays.push(dec.decode(v));
    else if (t === 2) out.author = bytesToHex(v);
    else if (t === 3) out.kind = (v[0] << 24) | (v[1] << 16) | (v[2] << 8) | v[3];
  }
  return out;
}
