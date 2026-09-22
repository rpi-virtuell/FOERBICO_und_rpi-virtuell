#!/usr/bin/env node
/**
 * md2blossom — Hugo-Post → Blossom-URLs + Nostr-Vorlagen
 *
 * Aufruf:
 *   node md2blossom.mjs <post-dir> [--write] [--blossom https://blossom.edufeed.org]
 *                                  [--pubkey <hex>] [--out DIR]
 *
 * Macht:
 *   1. SHA-256 aller Bilddateien im Post-Verzeichnis (Originalendung bleibt)
 *   2. Markdown: relative Bildpfade → Blossom-URL, Caption nach bildattribution.md
 *      direkt darunter; Frontmatter: image, cover.relative: false, cover.image
 *      Bilder, die schon als Hash-URL stehen, werden nicht neu gehasht — der
 *      Blob dahinter ist attestiert, die lokale Datei womöglich ein anderes Encoding.
 *   3. Schreibt nach <site>/_nostr/<post-dir-name>/ (oder --out DIR):
 *        <slug>.30023.json            unsignierter Artikel (image + x je Bild, Cover zuerst)
 *        <slug>.1063.<hash8>.json     unsignierter Lizenznachweis je Bild mit Eintrag
 *        <slug>.amb.json              AMB-JSON für `amb-convert amb:nostr`
 *        <slug>.md                    umgeschriebener Markdown (bei --write: index.md ersetzt)
 *   4. Meldet Bilder ohne Eintrag im `# bilder`-Block als TODO:LICENSE (Exit 2)
 *      und druckt eine Vorlage für den Block.
 *
 * Macht NICHT: hochladen, signieren, publizieren. Kein Key im Skript.
 *
 * Bildmetadaten stehen im Frontmatter von index.md als dritter markierter Block,
 * Feldnamen nach der Konvention (Orga/…/wissensgrundlagen/bildattribution.md):
 *
 *   # bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
 *   bilder:
 *     Datei.jpeg:
 *       alt: …                 # empfohlen (Barrierefreiheit)
 *       title: …
 *       author: …              # Pflicht außer bei CC0
 *       authorUrl: https://…
 *       licence: CC BY 4.0     # optional, sonst aus licenceUrl abgeleitet
 *       licenceUrl: https://…  # Pflicht
 *       sourceUrl: https://…   # Pflicht außer bei CC0
 *       modification: …        # Pflicht bei Bearbeitung von CC-BY-Werken
 *       pubkey: <hex>          # optional, Nostr-Urheber:in → p-Tag
 *       ai: generated          # optional: generated (KI-generiert) | modified (mit KI bearbeitet)
 *
 * Der Block ist Eingabe zum Prägen; das kind:1063 auf dem Relay ist Wahrheit
 * (Spec 2026-09-07, Teil 3). Abbildung auf das 1063:
 *   title→title · author→credit · authorUrl→authorUrl · licenceUrl→license ·
 *   sourceUrl→source · modification→modification · alt→alt · pubkey→p · ai→ai
 *   url, x, m, size rechnet das Skript aus der Datei. Ein ai-Wert außer
 *   generated/modified ergibt keinen Tag (edufeed-Wiki: Leser ignorieren ihn).
 *
 * Einmalig: cd scripts && npm i     Tests: npm test
 */

import { readFileSync, writeFileSync, readdirSync, mkdirSync, existsSync, statSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { join, extname, basename, resolve } from 'node:path';
import YAML from 'yaml';

// ---------- CLI ----------
const args = process.argv.slice(2);
if (!args[0] || args[0].startsWith('--')) {
  console.error('Aufruf: node md2blossom.mjs <post-dir> [--write] [--blossom URL] [--pubkey HEX] [--out DIR]');
  process.exit(1);
}
const postDir = resolve(args[0]);
const flag = (n, d) => { const i = args.indexOf(n); return i > -1 && args[i + 1] ? args[i + 1] : d; };
const WRITE = args.includes('--write');
const BLOSSOM = flag('--blossom', 'https://blossom.edufeed.org').replace(/\/$/, '');
const PUBKEY = flag('--pubkey', '0'.repeat(64));
// Standard-Ausgabe: <site>/_nostr/<post> — außerhalb von content/, sonst
// veröffentlicht Hugo die JSON-Dateien als Page Resources.
function defaultOut() {
  let d = postDir;
  while (d !== '/' && basename(d) !== 'content') d = resolve(d, '..');
  return d === '/' ? join(postDir, '_nostr') : join(d, '..', '_nostr', basename(postDir));
}
const OUT = args.includes('--out') ? resolve(flag('--out')) : defaultOut();

const IMG_EXT = new Set(['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg', '.avif']);
const MIME = { '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png', '.gif': 'image/gif', '.webp': 'image/webp', '.svg': 'image/svg+xml', '.avif': 'image/avif' };
// Kürzel wie im foerbico-editor (bilder.js, LIZENZEN), damit beide Wege dieselbe Caption schreiben
const LICENSE_LABEL = [
  [/publicdomain\/zero/, 'CC0'],
  [/licenses\/by-nc-sa/, 'CC BY-NC-SA 4.0'],
  [/licenses\/by-nc-nd/, 'CC BY-NC-ND 4.0'],
  [/licenses\/by-nc/, 'CC BY-NC 4.0'],
  [/licenses\/by-nd/, 'CC BY-ND 4.0'],
  [/licenses\/by-sa/, 'CC BY-SA 4.0'],
  [/licenses\/by/, 'CC BY 4.0'],
];
const licenseLabel = (url) => (LICENSE_LABEL.find(([re]) => re.test(url)) ?? [null, url])[1];
// KI-Kennzeichnung nach edufeed-Wiki (EU-AI-Office-Icons): nur diese zwei Werte sind bedeutungsvoll.
const KI_WERTE = { generated: 'KI-generiert', modified: 'KI-verändert' };
const kiWert = (l) => (typeof l?.ai === 'string' && Object.hasOwn(KI_WERTE, l.ai) ? l.ai : null);
const HASH_URL = /^https?:\/\/[^/\s]+\/([a-f0-9]{64})(\.[a-z0-9]+)?$/i;
const hashAusUrl = (u) => (typeof u === 'string' ? HASH_URL.exec(u)?.[1]?.toLowerCase() ?? null : null);

// ---------- Eingaben ----------
const indexPath = join(postDir, 'index.md');
if (!existsSync(indexPath)) { console.error(`Kein index.md in ${postDir}`); process.exit(1); }
const raw = readFileSync(indexPath, 'utf8');
const fm = /^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/.exec(raw);
if (!fm) { console.error('Kein Frontmatter gefunden'); process.exit(1); }
const meta = YAML.parse(fm[1]);
let body = fm[2];

// `# bilder`-Block: die Markerzeile ist YAML-Kommentar, der Schlüssel `bilder`
// steht damit im selben Dokument wie commonMetadata und staticSiteGenerator.
const bilder = meta.bilder && typeof meta.bilder === 'object' ? meta.bilder : {};
if (existsSync(join(postDir, 'bilder.yaml'))) {
  console.error('Hinweis: bilder.yaml wird nicht mehr gelesen — Einträge gehören in den `# bilder`-Block von index.md (seit 2026-09-07).');
}

const slug = meta.url || basename(postDir).replace(/^\d{4}-\d{2}-\d{2}-?/, '');

// ---------- Bilder ----------
/**
 * Schlüssel: Dateiname (lokal gehasht) oder Hash-URL (übernommen, nicht gehasht).
 * @type {Record<string, {key:string, file:string|null, hash:string, url:string, mime:string|null, size:number|null, lic:any|null}>}
 */
const images = {};

/** Eintrag im Block: unter dem Dateinamen, der URL oder einer URL mit gleichem Hash */
function lizenz(file, url) {
  const direkt = (file && bilder[file]) || bilder[url];
  if (direkt) return direkt;
  const hash = hashAusUrl(url);
  const treffer = Object.entries(bilder).find(([k]) => hashAusUrl(k) === hash);
  return treffer?.[1] ?? null;
}

for (const f of readdirSync(postDir)) {
  const ext = extname(f).toLowerCase();
  if (!IMG_EXT.has(ext)) continue;
  const p = join(postDir, f);
  if (!statSync(p).isFile()) continue;
  const buf = readFileSync(p);
  const hash = createHash('sha256').update(buf).digest('hex');
  const url = `${BLOSSOM}/${hash}${ext}`; // Originalendung: url im 1063 und image am Artikel byteidentisch
  images[f] = { key: f, file: f, hash, mime: MIME[ext], size: buf.length, url, lic: lizenz(f, url) };
}

/** Bild, das bereits als Hash-URL vorliegt: vorhandenen Blob nehmen, nie neu hashen */
function bestand(url) {
  const hash = hashAusUrl(url);
  if (!hash) return null;
  if (images[url]) return images[url];
  const lokal = Object.values(images).find((i) => i.hash === hash);
  if (lokal) return lokal;
  const ext = extname(new URL(url).pathname).toLowerCase();
  images[url] = { key: url, file: null, hash, mime: MIME[ext] ?? null, size: null, url, lic: lizenz(null, url) };
  return images[url];
}

// ---------- Caption nach bildattribution.md ----------
// [title](sourceUrl), [author](authorUrl), [licence](licenceUrl), KI-Kennzeichnung, modification
// Nur `, ` als Trenner, direkt unter dem Bild. Mindestform: [licence](licenceUrl).
// Die KI-Kennzeichnung (ai-Tag) steht direkt hinter der Lizenz — wie im Hub.
function caption(img) {
  const l = img.lic;
  if (!l?.licenceUrl) return '';
  const t = [];
  if (l.title) t.push(l.sourceUrl ? `[${l.title}](${l.sourceUrl})` : l.title);
  if (l.author) t.push(l.authorUrl ? `[${l.author}](${l.authorUrl})` : l.author);
  t.push(`[${l.licence || licenseLabel(l.licenceUrl)}](${l.licenceUrl})`);
  if (kiWert(l)) t.push(KI_WERTE[l.ai]);
  if (l.modification) t.push(l.modification);
  return t.join(', ');
}

// ---------- Markdown umschreiben ----------
const used = new Set();
const missing = [];
body = body.replace(/!\[([^\]]*)\]\(([^)\s]+)(\s+"[^"]*")?\)/g, (m, alt, src, title) => {
  if (hashAusUrl(src)) { used.add(bestand(src).key); return m; } // schon Blossom: unverändert
  const file = decodeURIComponent(src.replace(/^\.\//, ''));
  const img = images[file];
  if (!img) return m; // externe URL oder unbekannte Datei: unverändert
  used.add(file);
  const a = alt || img.lic?.alt || img.lic?.title || '';
  const line = `![${a}](${img.url}${title ?? ''})`;
  const cap = caption(img);
  if (!cap) { missing.push(file); return `${line}\n\n<!-- TODO:LICENSE ${file} -->`; }
  return `${line}\n${cap}`;
});

// Cover: bestehende Hash-URL hat Vorrang (nicht neu hashen), sonst Datei im Bundle
function coverBild() {
  const kandidaten = [meta.image, meta.cover?.image].filter((s) => typeof s === 'string');
  for (const s of kandidaten) if (hashAusUrl(s)) return bestand(s);
  for (const s of kandidaten) { const f = basename(s); if (images[f]) return images[f]; }
  return null;
}
const cover = coverBild();
if (cover) {
  used.add(cover.key);
  if (cover.file && !cover.lic?.licenceUrl) missing.push(cover.file);
}

// ---------- Frontmatter mitschreiben ----------
// Textuell, nicht über YAML.stringify: Blockmarker, Quoting und Reihenfolge bleiben.
function frontmatterSchreiben(yaml) {
  if (!cover) return yaml;
  let y = yaml;
  const imageZeile = `image: ${cover.url}`;
  if (/^image:.*$/m.test(y)) y = y.replace(/^image:.*$/m, imageZeile);
  else {
    const i = y.indexOf('\n# staticSiteGenerator');
    y = i >= 0 ? `${y.slice(0, i)}\n${imageZeile}${y.slice(i)}` : `${y}\n${imageZeile}`;
  }
  const coverBlock = /^cover:\n((?:[ \t]+\S.*(?:\n|$))+)/m;
  if (coverBlock.test(y)) {
    y = y.replace(coverBlock, (_, inner) => {
      const einzug = /^([ \t]+)/.exec(inner)?.[1] ?? '  ';
      let z = inner;
      z = /^[ \t]+relative:.*$/m.test(z) ? z.replace(/^([ \t]+)relative:.*$/m, '$1relative: false') : `${einzug}relative: false\n${z}`;
      z = /^[ \t]+image:.*$/m.test(z) ? z.replace(/^([ \t]+)image:.*$/m, `$1image: ${cover.url}`) : `${einzug}image: ${cover.url}\n${z}`;
      return `cover:\n${z}`;
    });
  } else {
    const block = `cover:\n  relative: false\n  image: ${cover.url}`;
    const i = y.indexOf('\n# bilder');
    y = i >= 0 ? `${y.slice(0, i)}\n${block}${y.slice(i)}` : `${y}\n${block}`;
  }
  return y;
}
const fmNeu = frontmatterSchreiben(fm[1]);

// ---------- Ausgaben ----------
mkdirSync(OUT, { recursive: true });
const now = Math.floor(Date.now() / 1000);
const publishedAt = meta.datePublished ? Math.floor(new Date(String(meta.datePublished).replace(/'/g, '')).getTime() / 1000) : now;
const keywords = meta.keywords ?? meta.tags ?? [];

// 30023 — x je Bild, Cover zuerst (Konvention wie mdparser/sync)
const tags30023 = [
  ['d', slug],
  ['title', meta.title || meta.name],
  ['published_at', String(publishedAt)],
];
if (meta.summary) tags30023.push(['summary', String(meta.summary).trim()]);
if (cover) tags30023.push(['image', cover.url], ['x', cover.hash]);
for (const key of used) if (images[key] !== cover) tags30023.push(['x', images[key].hash]);
for (const k of keywords) tags30023.push(['t', String(k).toLowerCase()]);
if (meta.id) tags30023.push(['r', meta.id]);
if (meta.license) tags30023.push(['license', meta.license]);
const ev30023 = { kind: 30023, pubkey: PUBKEY, created_at: now, content: body.trim() + '\n', tags: tags30023 };
writeFileSync(join(OUT, `${slug}.30023.json`), JSON.stringify(ev30023, null, 2));

// 1063 je genutztem Bild mit Eintrag — Tag-Form wie foerbico-editor (bilder.js, nachweisEvent)
let n1063 = 0;
for (const key of used) {
  const img = images[key];
  const l = img.lic;
  if (!l?.licenceUrl) continue;
  const tags = [['url', img.url], ['x', img.hash]];
  if (img.mime) tags.push(['m', img.mime]);
  if (img.size != null) tags.push(['size', String(img.size)]);
  tags.push(
    ['title', l.title || ''], ['license', l.licenceUrl], ['credit', l.author || ''],
    ['alt', l.alt || l.title || ''],
  );
  if (l.sourceUrl) tags.push(['source', l.sourceUrl]);
  if (l.authorUrl) tags.push(['authorUrl', l.authorUrl]);
  if (l.modification) tags.push(['modification', l.modification]);
  if (l.pubkey) tags.push(['p', l.pubkey]);
  if (kiWert(l)) tags.push(['ai', l.ai]);
  else if (l.ai) console.warn(`Warnung: ai-Wert „${l.ai}" bei ${key} unbekannt (erlaubt: generated, modified) — kein ai-Tag`);
  writeFileSync(join(OUT, `${slug}.1063.${img.hash.slice(0, 8)}.json`),
    JSON.stringify({ kind: 1063, pubkey: PUBKEY, created_at: now, content: '', tags }, null, 2));
  n1063++;
}

// AMB
const asConcept = (uri) => ({ id: uri });
const amb = {
  '@context': ['https://w3id.org/kim/amb/context.jsonld'],
  id: meta.id || `https://oer.community/${slug}`,
  type: ['LearningResource', ...(meta.type && meta.type !== 'LearningResource' ? [meta.type] : [])],
  name: meta.name || meta.title,
  description: meta.description,
  inLanguage: meta.inLanguage ?? ['de'],
  license: { id: meta.license },
  keywords,
  datePublished: String(meta.datePublished ?? '').replace(/'/g, '') || undefined,
  creator: (meta.creator ?? []).map((c) => {
    const o = { type: c.type || 'Person', name: [c.givenName, c.familyName].filter(Boolean).join(' '), givenName: c.givenName, familyName: c.familyName };
    if (c.id) o.id = c.id;
    if (c.affiliation) o.affiliation = { type: 'Organization', name: c.affiliation.name, ...(c.affiliation.id ? { id: c.affiliation.id } : {}) };
    return o;
  }),
  about: (meta.about ?? []).map(asConcept),
  learningResourceType: (meta.learningResourceType ?? []).map(asConcept),
  educationalLevel: (meta.educationalLevel ?? []).map(asConcept),
  image: cover?.url ?? (typeof meta.image === 'string' && /^https?:/.test(meta.image) ? meta.image : undefined),
};
for (const k of Object.keys(amb)) if (amb[k] === undefined || (Array.isArray(amb[k]) && amb[k].length === 0)) delete amb[k];
writeFileSync(join(OUT, `${slug}.amb.json`), JSON.stringify(amb, null, 2));

// Markdown
const newRaw = `---\n${fmNeu}\n---\n${body}`;
if (WRITE) writeFileSync(indexPath, newRaw);
else writeFileSync(join(OUT, `${slug}.md`), newRaw);

// ---------- Bericht ----------
console.log(`Post:      ${slug}`);
console.log(`Bilder:    ${Object.keys(images).length} gefunden, ${used.size} verwendet, ${n1063} Nachweise`);
if (cover) console.log(`Cover:     ${cover.file ?? '(Hash-URL, übernommen)'} → ${cover.url}`);
for (const i of Object.values(images)) if (i.file && !used.has(i.key)) console.log(`unbenutzt: ${i.file}`);
for (const i of Object.values(images)) if (!i.file && !i.lic) console.log(`Bestand:   ${i.url} ohne Eintrag im Block — Nachweis liegt ggf. nur auf dem Relay`);
const fehlend = [...new Set(missing)];
if (fehlend.length) {
  for (const f of fehlend) console.log(`TODO:LICENSE ${f}  → Eintrag im \`# bilder\`-Block fehlt (licenceUrl; author, alt empfohlen)`);
  console.log('Vorlage für das Frontmatter von index.md (Konvention: bildattribution.md):');
  console.log('# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)');
  console.log('bilder:');
  for (const f of fehlend) console.log(`  ${f}:\n    alt: \n    author: \n    licenceUrl: \n    # ai: generated | modified   (nur bei KI-Beteiligung)`);
}
console.log(`Ausgabe:   ${OUT}${WRITE ? '  (index.md überschrieben)' : ''}`);
console.log(`Weiter:    deno task publish ${OUT}   (blossom-bunker.ts signiert und publiziert die 1063; Blobs vorher mit "deno task upload")`);
process.exitCode = fehlend.length ? 2 : 0;
