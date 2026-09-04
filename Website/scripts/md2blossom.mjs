#!/usr/bin/env node
/**
 * md2blossom — Hugo-Post → Blossom-URLs + Nostr-Vorlagen
 *
 * Aufruf:
 *   node md2blossom.mjs <post-dir> [--write] [--blossom https://blossom.edufeed.org]
 *                                  [--pubkey <hex>] [--out DIR]
 *
 * Macht:
 *   1. SHA-256 aller Bilddateien im Post-Verzeichnis
 *   2. Markdown: relative Bildpfade → Blossom-URL, TULLU-Zeile darunter
 *      Cover (frontmatter.cover.image / image) → Blossom-URL
 *   3. Schreibt nach <site>/_nostr/<post-dir-name>/ (oder --out DIR):
 *        <slug>.30023.json            unsignierter Artikel
 *        <slug>.1063.<hash8>.json     unsignierter Lizenznachweis je Bild
 *        <slug>.amb.json              AMB-JSON für `amb-convert amb:nostr`
 *        <slug>.md                    umgeschriebener Markdown (bei --write: index.md ersetzt)
 *   4. Meldet Bilder ohne Eintrag in bilder.yaml als TODO:LICENSE (Exit 2)
 *
 * Macht NICHT: hochladen, signieren, publizieren. Kein Key im Skript.
 *
 * bilder.yaml (im Post-Verzeichnis):
 *   Datei.jpeg:
 *     title: …          # Pflicht
 *     credit: …         # Pflicht
 *     license: https:// # Pflicht (CC-URL)
 *     source: https://  # optional
 *     alt: …            # optional, sonst title
 *     pubkey: <hex>     # optional, Nostr-Urheber → p-Tag
 *
 * Einmalig: cd scripts && npm i
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
const LICENSE_LABEL = [
  [/publicdomain\/zero/, 'CC0 1.0'],
  [/licenses\/by-nc-sa/, 'CC BY-NC-SA 4.0'],
  [/licenses\/by-nc-nd/, 'CC BY-NC-ND 4.0'],
  [/licenses\/by-nc/, 'CC BY-NC 4.0'],
  [/licenses\/by-nd/, 'CC BY-ND 4.0'],
  [/licenses\/by-sa/, 'CC BY-SA 4.0'],
  [/licenses\/by/, 'CC BY 4.0'],
];
const licenseLabel = (url) => (LICENSE_LABEL.find(([re]) => re.test(url)) ?? [null, url])[1];

// ---------- Eingaben ----------
const indexPath = join(postDir, 'index.md');
if (!existsSync(indexPath)) { console.error(`Kein index.md in ${postDir}`); process.exit(1); }
const raw = readFileSync(indexPath, 'utf8');
const fm = /^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/.exec(raw);
if (!fm) { console.error('Kein Frontmatter gefunden'); process.exit(1); }
const meta = YAML.parse(fm[1]);
let body = fm[2];

const bilderPath = join(postDir, 'bilder.yaml');
const bilder = existsSync(bilderPath) ? (YAML.parse(readFileSync(bilderPath, 'utf8')) ?? {}) : {};

const slug = meta.url || basename(postDir).replace(/^\d{4}-\d{2}-\d{2}-?/, '');

// ---------- Bilder hashen ----------
/** @type {Record<string, {file:string, hash:string, url:string, mime:string, size:number, lic:any|null}>} */
const images = {};
for (const f of readdirSync(postDir)) {
  const ext = extname(f).toLowerCase();
  if (!IMG_EXT.has(ext)) continue;
  const p = join(postDir, f);
  if (!statSync(p).isFile()) continue;
  const buf = readFileSync(p);
  const hash = createHash('sha256').update(buf).digest('hex');
  const ext2 = ext === '.jpeg' ? '.jpg' : ext;
  images[f] = {
    file: f, hash, mime: MIME[ext], size: buf.length,
    url: `${BLOSSOM}/${hash}${ext2}`,
    lic: bilder[f] ?? null,
  };
}

// ---------- TULLU ----------
function tullu(img) {
  const l = img.lic;
  if (!l?.license) return '';
  const parts = [`"${l.title || img.file}"`];
  if (l.credit) parts.push(`von ${l.credit}`);
  parts.push(`[${licenseLabel(l.license)}](${l.license})`);
  if (l.source) parts.push(`Quelle: ${l.source}`);
  return `*${parts.join(', ')}*`;
}

// ---------- Markdown umschreiben ----------
const used = new Set();
const missing = [];
body = body.replace(/!\[([^\]]*)\]\(([^)\s]+)(\s+"[^"]*")?\)/g, (m, alt, src, title) => {
  const file = decodeURIComponent(src.replace(/^\.\//, ''));
  const img = images[file];
  if (!img) return m; // externe URL oder unbekannte Datei: unverändert
  used.add(file);
  const a = alt || img.lic?.alt || img.lic?.title || '';
  const line = `![${a}](${img.url}${title ?? ''})`;
  const cap = tullu(img);
  if (!cap) { missing.push(file); return `${line}\n\n<!-- TODO:LICENSE ${file} -->`; }
  return `${line}\n\n${cap}`;
});

// Cover
let coverFile = meta.cover?.relative ? meta.cover?.image : null;
if (!coverFile && typeof meta.image === 'string' && images[basename(meta.image)]) coverFile = basename(meta.image);
const cover = coverFile ? images[coverFile] : null;
if (cover) { used.add(coverFile); if (!cover.lic?.license) missing.push(coverFile); }

// ---------- Ausgaben ----------
mkdirSync(OUT, { recursive: true });
const now = Math.floor(Date.now() / 1000);
const publishedAt = meta.datePublished ? Math.floor(new Date(String(meta.datePublished).replace(/'/g, '')).getTime() / 1000) : now;
const keywords = meta.keywords ?? meta.tags ?? [];

// 30023
const tags30023 = [
  ['d', slug],
  ['title', meta.title || meta.name],
  ['published_at', String(publishedAt)],
];
if (meta.summary) tags30023.push(['summary', String(meta.summary).trim()]);
if (cover) tags30023.push(['image', cover.url], ['x', cover.hash]);
for (const k of keywords) tags30023.push(['t', String(k).toLowerCase()]);
if (meta.id) tags30023.push(['r', meta.id]);
if (meta.license) tags30023.push(['license', meta.license]);
const ev30023 = { kind: 30023, pubkey: PUBKEY, created_at: now, content: body.trim() + '\n', tags: tags30023 };
writeFileSync(join(OUT, `${slug}.30023.json`), JSON.stringify(ev30023, null, 2));

// 1063 je genutztem Bild mit Lizenz
let n1063 = 0;
for (const file of used) {
  const img = images[file];
  const l = img.lic;
  if (!l?.license || !l?.credit) continue;
  const tags = [
    ['url', img.url], ['x', img.hash], ['m', img.mime], ['size', String(img.size)],
    ['title', l.title || file], ['license', l.license], ['credit', l.credit],
    ['alt', l.alt || l.title || file],
  ];
  if (l.source) tags.push(['source', l.source]);
  if (l.pubkey) tags.push(['p', l.pubkey]);
  writeFileSync(join(OUT, `${slug}.1063.${img.hash.slice(0, 8)}.json`),
    JSON.stringify({ kind: 1063, pubkey: PUBKEY, created_at: now, content: l.description ?? '', tags }, null, 2));
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
const newRaw = `---\n${fm[1]}\n---\n${body}`;
if (WRITE) writeFileSync(indexPath, newRaw);
else writeFileSync(join(OUT, `${slug}.md`), newRaw);

// ---------- Bericht ----------
console.log(`Post:      ${slug}`);
console.log(`Bilder:    ${Object.keys(images).length} gefunden, ${used.size} verwendet, ${n1063} Nachweise`);
if (cover) console.log(`Cover:     ${coverFile} → ${cover.url}`);
for (const f of Object.keys(images)) if (!used.has(f)) console.log(`unbenutzt: ${f}`);
for (const f of [...new Set(missing)]) console.log(`TODO:LICENSE ${f}  → Eintrag in bilder.yaml fehlt (title, credit, license)`);
console.log(`Ausgabe:   ${OUT}${WRITE ? '  (index.md überschrieben)' : ''}`);
console.log(`Weiter:    npx amb-convert amb:nostr ${join(OUT, slug + '.amb.json')} -p`);
process.exitCode = missing.length ? 2 : 0;
