// Tests für config.ts: Konfiguration der Repos und Identitäten, Umgebungsdatei.
import { assert, assertEquals, assertMatch } from 'jsr:@std/assert@^1.0.0';
import { loadConfig, loadEnv } from './config.ts';

const EDUFEED = '30617:1c5ff3caacd842c01dca8f378231b16617516d214da75c7aeabbe9e1efe9c0f6:edufeed-app';
const JOERG = '4fa5d1c413e2b45e10d40bf3562ab701a5331206e359c90baae0e99bfd6c6e41';

Deno.test('loadConfig: edufeed-app hat die Repo-Koordinate aus der Spec', () => {
  const cfg = loadConfig();
  assertEquals(cfg.repos['edufeed-app'].coordinate, EDUFEED);
});

Deno.test('loadConfig: reli-hub nennt Jörg als Maintainer', () => {
  const cfg = loadConfig();
  assert(cfg.repos['reli-hub'].maintainers.includes(JOERG));
});

Deno.test('loadConfig: readRelays lassen groups.edufeed.org aus', () => {
  const cfg = loadConfig();
  for (const repo of Object.values(cfg.repos)) {
    assert(repo.relays.length >= 2);
    assert(!repo.readRelays.some((r) => r.includes('groups.edufeed.org')), repo.id);
    assert(repo.readRelays.length <= 3);
  }
});

Deno.test('loadConfig: genau die Identitäten joerg und poutnik mit hex-Pubkeys', () => {
  const cfg = loadConfig();
  assertEquals(cfg.identities.map((i) => i.alias).sort(), ['joerg', 'poutnik']);
  for (const i of cfg.identities) assertMatch(i.pubkey, /^[0-9a-f]{64}$/);
});

Deno.test('loadEnv: liest KEY=WERT, ignoriert Kommentare, entfernt Anführungszeichen', () => {
  const f = Deno.makeTempFileSync();
  Deno.writeTextFileSync(f, 'A=1\n#k\nB="x y"\n\n');
  assertEquals(loadEnv(f), { A: '1', B: 'x y' });
});
