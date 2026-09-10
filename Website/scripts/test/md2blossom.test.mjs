// Tests für md2blossom.mjs — Spec Teil 3 (mdparser/docs/superpowers/specs/2026-09-07-…)
// Aufruf: cd Website/scripts && npm test
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync, writeFileSync, readFileSync, mkdirSync, readdirSync } from 'node:fs';
import { spawnSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { join } from 'node:path';
import { tmpdir } from 'node:os';

const SKRIPT = new URL('../md2blossom.mjs', import.meta.url).pathname;
const sha = (buf) => createHash('sha256').update(buf).digest('hex');

function post(name, indexMd, dateien) {
  const root = mkdtempSync(join(tmpdir(), 'md2blossom-'));
  const dir = join(root, 'content', 'de', 'posts', name);
  mkdirSync(dir, { recursive: true });
  writeFileSync(join(dir, 'index.md'), indexMd);
  for (const [f, inhalt] of Object.entries(dateien)) writeFileSync(join(dir, f), inhalt);
  return { dir, out: join(root, 'out') };
}

function lauf(dir, out, ...extra) {
  const r = spawnSync('node', [SKRIPT, dir, '--out', out, ...extra], { encoding: 'utf8' });
  const dateien = Object.fromEntries(readdirSync(out).map((f) => [f, readFileSync(join(out, f), 'utf8')]));
  return { code: r.status, stdout: r.stdout, stderr: r.stderr, dateien };
}

const FM_MIGRATION = `---
# commonMetadata
'@context': https://schema.org/
name: Test
license: https://creativecommons.org/licenses/by/4.0/
id: https://oer.community/test
image: https://oer.community/test/Titel.jpeg
datePublished: '2026-09-01'

# staticSiteGenerator
title: Test
cover:
  relative: true
  image: Titel.jpeg
  hiddenInSingle: false
url: test
# bilder  (Konvention: bildattribution.md)
bilder:
  Titel.jpeg:
    alt: Ein Titelbild
    title: Titel
    author: Jörg Lohrer
    authorUrl: https://example.org/joerg
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
    sourceUrl: https://example.org/quelle
    modification: beschnitten
    ai: modified
  Ohne.png:
    # licenceUrl:
---

Text.

![](Titel.jpeg)

![Alt aus dem Markdown](Ohne.png)

Ende.
`;

test('Migration: Frontmatter, Endung, Caption, bilder-Block, TODO', () => {
  const titel = Buffer.from('titelbild-bytes');
  const ohne = Buffer.from('png-bytes');
  const { dir, out } = post('2026-09-01-test', FM_MIGRATION, { 'Titel.jpeg': titel, 'Ohne.png': ohne });
  const r = lauf(dir, out);
  const md = r.dateien['test.md'];
  const urlTitel = `https://blossom.edufeed.org/${sha(titel)}.jpeg`;
  const urlOhne = `https://blossom.edufeed.org/${sha(ohne)}.png`;

  // Punkt 3: Endung bleibt .jpeg
  assert.ok(md.includes(urlTitel), 'Blossom-URL mit Originalendung');
  assert.ok(!md.includes(`${sha(titel)}.jpg`), 'kein .jpg aus .jpeg');

  // Punkt 1: Frontmatter mitgeschrieben
  assert.match(md, new RegExp(`^image: ${urlTitel}$`, 'm'));
  assert.match(md, /^cover:\n {2}relative: false\n {2}image: https:\/\/blossom\.edufeed\.org\/[a-f0-9]{64}\.jpeg\n {2}hiddenInSingle: false$/m);
  assert.ok(md.includes("datePublished: '2026-09-01'"), 'übriges Frontmatter unangetastet');

  // Punkt 4: Caption nach bildattribution.md, direkt unter dem Bild, ohne Leerzeile
  assert.ok(md.includes(
    `![Ein Titelbild](${urlTitel})\n[Titel](https://example.org/quelle), [Jörg Lohrer](https://example.org/joerg), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), KI-verändert, beschnitten\n`
  ), 'Caption-Zeile:\n' + md);

  // Punkt 5: Block bleibt erhalten, kein bilder.yaml nötig; Bild ohne Eintrag → TODO
  assert.ok(md.includes('# bilder  (Konvention: bildattribution.md)\nbilder:\n  Titel.jpeg:'), 'Block erhalten');
  assert.ok(md.includes(`![Alt aus dem Markdown](${urlOhne})\n\n<!-- TODO:LICENSE Ohne.png -->`));
  assert.equal(r.code, 2);
  assert.match(r.stdout, /TODO:LICENSE Ohne\.png/);
  assert.match(r.stdout, /bilder:\n {2}Ohne\.png:/, 'Vorlage für den Block im Bericht');

  // 1063 mit Konventions-Abbildung
  const ev = JSON.parse(r.dateien[`test.1063.${sha(titel).slice(0, 8)}.json`]);
  const tag = (n) => ev.tags.find((t) => t[0] === n)?.[1];
  assert.equal(tag('url'), urlTitel);
  assert.equal(tag('x'), sha(titel));
  assert.equal(tag('m'), 'image/jpeg');
  assert.equal(tag('size'), String(titel.length));
  assert.equal(tag('credit'), 'Jörg Lohrer');
  assert.equal(tag('license'), 'https://creativecommons.org/licenses/by/4.0/');
  assert.equal(tag('source'), 'https://example.org/quelle');
  assert.equal(tag('authorUrl'), 'https://example.org/joerg');
  assert.equal(tag('modification'), 'beschnitten');
  assert.equal(tag('alt'), 'Ein Titelbild');
  // KI-Kennzeichnung (edufeed-Wiki license-events-nope): ai als letzter Tag
  assert.deepEqual(ev.tags.at(-1), ['ai', 'modified']);
  assert.equal(Object.keys(r.dateien).filter((f) => f.includes('.1063.')).length, 1, 'kein 1063 ohne Lizenz');

  // 30023: image + x (Cover zuerst), weitere x je Fließtextbild
  const art = JSON.parse(r.dateien['test.30023.json']);
  assert.deepEqual(art.tags.filter((t) => t[0] === 'x').map((t) => t[1]), [sha(titel), sha(ohne)]);
  assert.equal(art.tags.find((t) => t[0] === 'image')[1], urlTitel);
});

const HASH = 'a2a54ea54f386ba0abceb4d28498c4c5c0b66da153bdec04c36bf40a6c32bf5b';
const URL_ATTESTIERT = `https://blossom.edufeed.org/${HASH}.jpeg`;
const FM_BESTAND = `---
# commonMetadata
name: Bestand
id: https://oer.community/bestand
image: ${URL_ATTESTIERT}

# staticSiteGenerator
cover:
  relative: false
  image: ${URL_ATTESTIERT}
  hiddenInSingle: true
url: bestand
# bilder
bilder:
  "${URL_ATTESTIERT}":
    alt: Schrein
    title: nosTr-schrein
    author: Comenius-Institut
    licenceUrl: https://creativecommons.org/publicdomain/zero/1.0/
    pubkey: ${'5a12b41ec15b466321e88c371be2dc47d9193f9c8bba4ab09fc50045bd35aedf'}
---

![Schrein](${URL_ATTESTIERT})
nosTr-schrein, Comenius-Institut, [CC0](https://creativecommons.org/publicdomain/zero/1.0/)
`;

test('Bestand: Hash-URL wird respektiert, nicht neu gehasht, Markdown unverändert', () => {
  // lokale Datei ist ein anderes Encoding als der attestierte Blob
  const { dir, out } = post('2025-07-02-bestand', FM_BESTAND, { 'nosTr-schrein.jpg': Buffer.from('anderes-encoding') });
  const r = lauf(dir, out);
  assert.equal(r.code, 0, r.stdout + r.stderr);
  assert.equal(r.dateien['bestand.md'], FM_BESTAND, 'index.md byteidentisch');

  const art = JSON.parse(r.dateien['bestand.30023.json']);
  assert.equal(art.tags.find((t) => t[0] === 'image')[1], URL_ATTESTIERT);
  assert.deepEqual(art.tags.filter((t) => t[0] === 'x').map((t) => t[1]), [HASH]);

  const ev = JSON.parse(r.dateien[`bestand.1063.${HASH.slice(0, 8)}.json`]);
  const tag = (n) => ev.tags.find((t) => t[0] === n)?.[1];
  assert.equal(tag('url'), URL_ATTESTIERT);
  assert.equal(tag('x'), HASH);
  assert.equal(tag('m'), 'image/jpeg');
  assert.equal(tag('size'), undefined, 'Größe unbekannt → kein size-Tag statt falscher Zahl');
  assert.equal(tag('credit'), 'Comenius-Institut');
  assert.equal(tag('p'), '5a12b41ec15b466321e88c371be2dc47d9193f9c8bba4ab09fc50045bd35aedf');
  assert.match(r.stdout, /unbenutzt: nosTr-schrein\.jpg/);
});

test('Cover ohne cover-Block und ohne image-Zeile wird ergänzt', () => {
  const fm = `---
# commonMetadata
name: Kurz
id: https://oer.community/kurz

# staticSiteGenerator
url: kurz
# bilder
bilder:
  c.png:
    licenceUrl: https://creativecommons.org/publicdomain/zero/1.0/
---

![](c.png)
`;
  const c = Buffer.from('cover');
  const { dir, out } = post('2026-01-01-kurz', fm, { 'c.png': c });
  const r = lauf(dir, out);
  const md = r.dateien['kurz.md'];
  const url = `https://blossom.edufeed.org/${sha(c)}.png`;
  // erstes Bild im Text wird nicht automatisch Cover — ohne image/cover bleibt das Frontmatter ohne Cover
  assert.ok(!/^image:/m.test(md), 'kein Cover erfunden');
  assert.ok(md.includes(`![](${url})\n[CC0](https://creativecommons.org/publicdomain/zero/1.0/)`), 'Mindestform der Caption');
  assert.equal(r.code, 0);
});
