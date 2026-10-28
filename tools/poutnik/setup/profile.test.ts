// Tests für setup/profile.ts: Profil ergänzen ohne das Bild zu verlieren, Relay-Liste erweitern.
import { assert, assertEquals } from 'jsr:@std/assert@^1.0.0';
import { buildProfile, buildRelayList, planUpdates } from './profile.ts';

const PIC = 'https://blossom.edufeed.org/32e4e89270e49ffd60a144b2efb90437bc02f45182f5fd562848cb14bd3401c1.png';
const REPO_RELAYS = ['wss://relay.ngit.dev', 'wss://gitnostr.com', 'wss://ngit.danconwaydev.com', 'wss://groups.edufeed.org'];

Deno.test('buildProfile: behält das Bild, setzt bot, display_name und about', () => {
  const p = buildProfile({ name: 'Poutník', picture: PIC, about: '' });
  assertEquals(p.picture, PIC);
  assertEquals(p.name, 'Poutník');
  assertEquals(p.display_name, 'Poutník');
  assertEquals(p.bot, true);
  assert(String(p.about).startsWith("Der Pilger aus Comenius'"));
});

Deno.test('buildProfile: unbekannte Felder bleiben erhalten', () => {
  const p = buildProfile({ name: 'Poutník', picture: PIC, website: 'https://x', lud16: 'a@b' });
  assertEquals(p.website, 'https://x');
  assertEquals(p.lud16, 'a@b');
});

Deno.test('buildRelayList: alte Einträge zuerst, Repo-Relays angehängt, keine Duplikate', () => {
  const alt = [['r', 'wss://relay.damus.io/'], ['r', 'wss://nos.lol/'], ['r', 'wss://relay.edufeed.org/']];
  const neu = buildRelayList(alt, REPO_RELAYS);
  assertEquals(neu.length, 7);
  assertEquals(neu.slice(0, 3), alt);
  assertEquals(neu[3], ['r', 'wss://relay.ngit.dev']);
  assertEquals(buildRelayList(neu, REPO_RELAYS), neu);
});

Deno.test('buildRelayList: erkennt Duplikate auch mit abschließendem Schrägstrich', () => {
  const alt = [['r', 'wss://relay.ngit.dev/']];
  assertEquals(buildRelayList(alt, ['wss://relay.ngit.dev']).length, 1);
});

const ev0 = { id: 'a'.repeat(64), kind: 0, pubkey: 'p', created_at: 1, tags: [], content: JSON.stringify({ name: 'Poutník', picture: PIC }), sig: 's' };
const ev10002 = { id: 'b'.repeat(64), kind: 10002, pubkey: 'p', created_at: 1, tags: [['r', 'wss://nos.lol/']], content: '', sig: 's' };

Deno.test('planUpdates: ohne gelesene Relay-Liste wird abgebrochen (keine Verkürzung)', () => {
  let err = '';
  try {
    planUpdates(ev0, undefined, REPO_RELAYS);
  } catch (e) {
    err = String(e);
  }
  assert(err.includes('10002'));
});

Deno.test('planUpdates: ohne Bild im Profil wird abgebrochen', () => {
  const ohneBild = { ...ev0, content: JSON.stringify({ name: 'Poutník' }) };
  let err = '';
  try {
    planUpdates(ohneBild, ev10002, REPO_RELAYS);
  } catch (e) {
    err = String(e);
  }
  assert(err.includes('Bild'));
});

Deno.test('planUpdates: liefert neues kind 0 und erweiterte Relay-Liste', () => {
  const { neu0, neu10002 } = planUpdates(ev0, ev10002, REPO_RELAYS);
  assertEquals(JSON.parse(neu0.content).bot, true);
  assertEquals(neu10002.tags.length, 5);
  assertEquals(neu10002.tags[0], ['r', 'wss://nos.lol/']);
});
