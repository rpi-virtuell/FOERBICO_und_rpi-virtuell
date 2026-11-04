# Hub als Nachweis, Etappe 3: Spielregeln, Material-Detail, Schaufenster live. Umsetzungsplan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bis 24.11.2026 zeigt der reli_hub-Prototyp echte Inhalte: das FOERBICO-Schaufenster liest Seiten, Beiträge und Termine live vom Schaufenster-Schlüssel (Issue 10), darin liegt der Bereich „Spielregeln“ mit vier Seiten (Issue 03), der Materialpool listet Materialien live als `kind:30142` mit Zähler, und jedes Material hat eine Detailansicht mit Vokabular-Links, Lizenzpille, Rohdaten und einem Lizenzstand, der bestimmt, was geht (Issues 04 und 15). Die vier Spielregeln-Seiten entstehen parallel als Markdown im FOERBICO-Repo (Inhaltsstrang, Spec 5a, Frist 30.11.). Abnahme mit dem UX-Gast am 25.11.2026.

**Architecture:** Eine HTML-Datei ohne Build (`index.html`), drei Inline-Skripte; alles Neue kommt ins Anwendungsskript (letzter `<script>`-Block) und nutzt die Datenschicht aus Etappe 2 (`hubFetch`, `datenstand`, `npubToHex`, `naddr`, `sichereUrl`, ADR-0006). Inhalte werden nicht in den Code geschrieben: Seiten sind `kind:30023` mit Seiten-Label vom FOERBICO-Schlüssel (ADR-0027 im oer-community-Repo), Beiträge `kind:30023` ohne Seiten-Label, Menü und Fußzeile `kind:30004`, Materialien `kind:30142` (AMB-Tags `feld:id`, `feld:prefLabel:de`). Ein kleiner, sicherer Markdown-Renderer `mdSeite` macht aus Event-Inhalten HTML. Jedes Issue wird ein PR-Branch `pr/<name>`, gestapelt in dieser Reihenfolge, weil alle `index.html` ändern. Prüfungen bleiben textbasiert (`deno task test`), Verhaltenstests extrahieren Funktionen aus dem Skript wie `tests/datenschicht.test.ts`.

**Tech Stack:** HTML/CSS/JavaScript ohne Framework, WebSocket zu Nostr-Relays (NIP-01, Kinds 30023, 30004, 31923, 30142, NIP-32-Labels), Deno 2 für Tests und Schnappschuss, ngit 3.0.4 (Konten `poutnik` und `joerg`, Amber), Wrapper `tools/poutnik`, Prüfwerkzeug `tools/nachweis/check.py`. Inhaltsstrang: Markdown mit Frontmatter in `Website/content/de/`, Sync-Pipeline (mdparser) signiert mit dem FOERBICO-Schlüssel.

**Spec:** `docs/superpowers/specs/2026-11-02-hub-nachweis-gesamtkonzeption-design.md` (Abschnitte 3, 4.2, 4.3, 4.12, 4.13, 4.15, 5a Inhaltsstrang, 7 Issues 3/4/10/15, 8 Fahrplan dritte Zeile, 9, 10). Vorbild für Form und Ablauf: `docs/superpowers/plans/2026-11-05-hub-etappe-2-navigation.md`; Übergabe der Etappe 2: `Hub-Entwicklung/2026-11-05-etappe-2-uebergabe.md`. Issue-Texte: `~/.config/poutnik/protokolle/issue-kommentare-2026-11-04/` (`03-spielregeln.md`, `04-material-detail.md`, `10-schaufenster-live.md`, `15-lizenzstand.md`; nevent-Links in den `.fertig.json`). ADR-0027 (Seiten, Menü, Fußzeile aus Nostr): `~/repositories/oer-community/docs/entscheidungen/0027-seitenstruktur-aus-nostr.md`; Lizenzkürzel: `~/repositories/oer-community/src/lib/lizenzlabel.js` (Werte kopieren, nie verlinken). Schlüsselliste: `Hub-Entwicklung/communities-schluessel.md`.

**Issue-Kurz-IDs** (erste acht Hex-Zeichen der Event-ID): 03 Spielregeln `371d9cbf`, 04 Material-Detail `9770e756`, 10 Schaufenster live `4a3d1b54`, 15 Lizenzstand `516faa60`; Querschnitt 13 Live-Abfrage `bc8d97d8` (erledigt in Etappe 2). Stand 04.11.2026: alle vier offen, ohne Antwort des Teams.

**Befund vom 04.11.2026 (Sondierung der Relays, Grundlage der Entscheidungen unten):** Der FOERBICO-Schlüssel (`npub1tgftg8kptdrxxg0g3sm3hckuglv3j0uu3way4vylc5qyt0f44m0s3gun6e`, Hex `5a12b41ec15b466321e88c371be2dc47d9193f9c8bba4ab09fc50045bd35aedf`) hat auf `relay.edufeed.org` elf Seiten (`kind:30023`, Tags `["L","foerbico/typ"]` und `["l","seite","foerbico/typ"]`, `d` = `startseite`, `tagungen`, `qualitaet`, `oer-und-oep`, `unser-team`, `impressum`, `datenschutz` und englische Fassungen `en/…`), 92 Beiträge (`kind:30023` ohne Seiten-Label, `d` = Slug, `published_at`, `summary`, `image` oft relativ, `t`-Tags), zwei Listen (`kind:30004`, `d` = `navigation` mit vier `a`-Tags, `d` = `fusszeile` mit zwei) und keine Termine (`kind:31923`). Die vier Spielregeln-Seiten gibt es noch nicht. Materialien (`kind:30142`): 269 auf `relay.edufeed.org`, 45 auf `relay-rpi.edufeed.org`, 60 auf `amb-relay.edufeed.org`, von vielen Absendern (Hochschul-Importe, Kanban-Boards, Einzelne); keines trägt den `h`-Tag der Community rpi-virtuell; Lizenz-URLs von Creative Commons (teils `legalcode.de`, `deed.de`), Wikipedia-Urheberrecht oder fehlend (etwa ein Zehntel); Vokabular-IDs zeigen auf w3id.org/kim und purl.org/dcx (noch keine nocabs-Adressen). Der Materialpool-Nachbau im Hub zeigt sechs eingebettete Karten („Spiegel vom 22.10.2026“).

**Folgepläne (nicht Teil dieses Plans):** Etappe 4 bis 07.12. (Sammlung, Kataloge, Kalender über alle Quellen, Personen; die Lizenzstand-Regel aus Task 5 gilt dort weiter), Etappe 5 bis 23.12. (Rest, Erschließungs-Layer), Etappe 6 Januar.

## Global Constraints

- Launch-Stack ist der HTML-Prototyp: eine Datei `index.html`, kein Build, kein Framework, keine externen Abhängigkeiten außer Google Fonts (Spec 3). Kein Svelte, kein Stack-Wechsel.
- Relays, von denen der Hub liest: `wss://relay.edufeed.org`, `wss://relay-rpi.edufeed.org`, `wss://amb-relay.edufeed.org`. Nie `wss://groups.edufeed.org`. Je Ansicht ein `REQ` pro Relay mit allen Filtern der Ansicht, `MAX_CONN = 3`, `TIMEOUT_MS = 8000`, `RETRY_MS = 60000`, Cache in `sessionStorage` über `hubFetch(name, filters, opts)` (ADR-0006, `docs/daten.md`). Keine Subscription je Eintrag; eine Detailansicht liest zuerst aus dem Ergebnis der Listenabfrage und fragt nur bei Fehlen gezielt nach.
- Jede Ansicht zeigt sichtbar „live · …“, „Stand vom <Datum>“ oder „Nachbau · …“ über `datenstand(viewId, zustand, info)`; nichts wird als echt ausgegeben, was es nicht ist. Fehlende Inhalte (eine Seite, die noch nicht auf dem Relay liegt) erscheinen als „in Vorbereitung“ mit Verweis, nie als toter Link.
- Inhalte vom Relay sind fremder Text: Alles wird mit `esc()` maskiert, bevor Markdown-Auszeichnung zu HTML wird; `href` und `src` nur über `sichereUrl()` (nur `http(s)://`, sonst leer); kein `innerHTML` mit unmaskiertem Event-Inhalt; `<` in eingebetteten Schnappschüssen als `<`.
- Farbsystem nach ADR-0001: Bereichsfarben nur in `:root`; neue Farben als Fläche plus Textfarbe mit mindestens 4,5:1 auf `--paper`, `--card` und dem eigenen Hellton; keine Hex-Bereichsfarbe im Anwendungsskript; Fokus sichtbar. Das Schaufenster bleibt in seinen Farben (`--fo-*`), der Materialpool in `--mp`/`--mp-dark`.
- Die vier Hub-Ergänzungen je Instanz bleiben (ADR-0002 Punkte 2 bis 4); Porträts unter © werden nicht übernommen, dort stehen Initialen (ADR-0002 Punkt 3): die Teamseite bleibt deshalb Schnappschuss.
- Keine Arbeitspakete, Meilensteine, AP-/M-Nummern, Förderkennzeichen, kein Projektträger, kein Zwischenbericht in Code, Docs, ADRs, Commits, PR-Texten, Issue-Kommentaren und in den Spielregeln-Seiten (die auf dem Relay und auf oer.community erscheinen). Prüfung: `deno task test` und `python3 -I tools/nachweis/check.py gitworkshop <ordner>` über jeden Entwurfsordner vor der Veröffentlichung.
- Keine Vornamen von Partnern in Dateien, Commits oder Kommentaren; Rollen („der UX-Gast“, „die Redaktion“, „der Leit-Maintainer“), Handles (`laoc42`), Pubkey-Präfixe. Erlaubt: „Jörg Lohrer“, „Jens Dechow“. Namen, die ein Event selbst trägt (`creator:name`, Teamseite auf oer.community), werden angezeigt, nicht in den Code geschrieben.
- Keine privaten Schlüssel, `nsec`, Bunker-Links oder Tokens in Dateien oder im Gespräch; nur `npub` und Hex-Pubkeys.
- Hub-Texte auf Deutsch in Du-Ansprache; neue Texte nennen den Hub nicht beim Namen (Faden „Selbstverständnis“ offen). Die Spielregeln-Seiten sprechen Nutzende an, nicht einen Förderer.
- Commits auf PR-Branches mit Author `Poutník <poutnik@users.noreply.edufeed.org>`; Branch `pr/<name>` ab dem Kopf des vorigen Branches (gestapelt), der erste ab `main` (`21ae08b`); Push nur über `cd ~/repositories/FOERBICO_und_rpi-virtuell/tools/poutnik && deno task push pr/<name> --as poutnik --cwd ~/repositories/reli-hub`, nie `git push origin`. Patch-Rückfall: nicht wiederholen, Jörg melden. `deno.lock` im Klon nie committen; Dateiserver für Browserprüfungen außerhalb des Repos starten (zum Beispiel `cd /tmp && deno run --allow-net --allow-read jsr:@std/http/file-server ~/repositories/reli-hub`).
- Merge und Push von `main` nur durch Jörg (`ngit --signer joerg pr merge --offline` auf dem PR-Branch, ohne Amber-Tipp; `deno task push main --as joerg`, ein Amber-Tipp; `git push forgejo main`); der Container unter hub.rpi-virtuell.net liefert `main` aus. Ablauf wie in der Übergabe der Etappe 2.
- Tests der Etappe liegen in `tests/inhalte.test.ts` (neu, Task 1); `tests/index.test.ts`, `tests/navigation.test.ts`, `tests/datenschicht.test.ts` bleiben grün (37); Helfer in `tests/helfer.ts`. Testzahl steigt je Task; der Prüfbefehl ist in jedem Task `cd ~/repositories/reli-hub && deno task test`.
- Schnittregel der Tests: Funktionen des Anwendungsskripts beginnen mit zwei Leerzeichen (`  function name(…) {`) und enden mit `\n  }`; innere Zeilen sind tiefer eingerückt, auch in Template-Literalen, damit die Tests eine Funktion per Regex schneiden können. Funktionen, die ein Test mit `new Function` baut (`mdSeite`, `lizenzLabel`, `lizenzStand`, `lizenzAktionen`, `tagWert`, `tagWerte`, `ambWerte`, `ambJsonLd`), rufen außer `esc`, `sichereUrl` und den im jeweiligen Test mitgeschnittenen Funktionen nichts aus dem Skript auf.
- Rückfallreihenfolge dieser Etappe (Spec 8, auf Inhalte übertragen): Gerät der 24.11. in Gefahr, fällt zuerst in Task 5 der Rohdaten-Knopf weg (Link auf das Event bei edufeed bleibt), dann in Task 2 das Termine-Archiv (Abschnitt mit ehrlichem Hinweis bleibt), dann in Task 4 die Suche im Materialpool. Nicht verhandelbar: Tasks 1, 2 (Seiten und Beiträge live), 3 (Spielregeln-Bereich), 4 (Liste live mit Zähler), 5 (Detail mit Lizenzstand) und Task 7 (die vier Seitentexte), weil sie das Ergebnis der Etappe sind.

## Review Focus

1. Relay-Inhalt mit HTML oder `</script>` im Markdown einer Seite oder eines Beitrags: `mdSeite` maskiert alles vor der Auszeichnung; nichts wird als HTML ausgeführt (Task 1, Test `mdSeite: maskiert und filtert`).
2. Links `javascript:`, `data:` oder relative Pfade in Markdown, `image`-Tag oder `r`-Tag: `href`/`src` werden nur bei `http(s)://` gesetzt, sonst Text ohne Link beziehungsweise Platzhalter (Task 1 derselbe Test; Task 4 Test `Materialpool live: Karten ohne unsichere Adressen`).
3. Seiten fehlen auf dem Relay (die Spielregeln-Seiten kommen erst im Inhaltsstrang): der Bereich zeigt vier Kacheln mit „in Vorbereitung“ und Verweis, Stand-Zeile „live · 0 von 4 Seiten“, keine Ausnahme in der Konsole (Task 3, Test `Spielregeln: vier Seiten mit Vorbereitungs-Rückfall`).
4. Material ohne Lizenz, ohne `prefLabel`, ohne Bild oder mit unbekanntem `d` in der Adresse: Pille „Lizenz nicht angegeben“ als eigener Stand, Chip mit dem letzten Pfadteil der ID, Platzhalter statt Bild, „Material nicht gefunden“ mit Rückweg (Task 1 Test `lizenzLabel und lizenzStand`; Task 5 Tests `ambJsonLd und ambWerte` und `Material-Detail: Felder, Lizenzstand, Rohdaten, …`).
5. Relay-Last auf der Tagung: Schaufenster und Materialpool fragen je Relay genau einen `REQ` mit `limit`; die Detailansicht nutzt das Ergebnis der Liste aus dem Cache und fragt nur bei Fehlen mit `#d` nach; Menü und Seiten kommen aus derselben Abfrage wie die Beiträge (Task 1 Test `ocLaden: ein REQ je Relay`, Task 5 Test `Material-Detail: kein zweiter REQ bei Treffer im Cache`).

---

## Merge-Ablauf (gilt für jeden Task, wird dort nur referenziert)

Vorbereitung vor dem ersten Push: `cd ~/repositories/reli-hub && git checkout main && git -c nostr.signer=joerg fetch origin main && git log --oneline main..origin/main` (leer heißt: `main` unverändert, sonst `git merge --ff-only origin/main` und den Stapel rebasen).

PR öffnen (nach Jörgs Ja zum Diff): `cd ~/repositories/FOERBICO_und_rpi-virtuell/tools/poutnik && deno task push pr/<name> --as poutnik --cwd ~/repositories/reli-hub` (ausgecheckt muss der Branch sein). Erwartet: `posting proposal as PR event`, kein Patch-Rückfall. PR-Beschreibung: Issue mit Kurz-ID und gitworkshop-Link, Entscheidung in zwei Sätzen, Prüfbefehl.

Mergen (Jörg): `cd ~/repositories/reli-hub && git checkout pr/<name> && ngit --signer joerg pr merge --offline`, nach allen Merges einmal `cd ~/repositories/FOERBICO_und_rpi-virtuell/tools/poutnik && deno task push main --as joerg --cwd ~/repositories/reli-hub` (Amber) und `cd ~/repositories/reli-hub && git push forgejo main`. Erwartet: gitworkshop zeigt die PRs als erledigt, `curl -s https://hub.rpi-virtuell.net/ | grep -c mdSeite` ist größer als 0.

---

### Task 1: Inhalte aus Events: Seitenrenderer, Schaufenster-Daten, Lizenzkürzel (Querschnitt für Issues 10, 03, 04, 15)

**Files:** Modify `index.html` (Anwendungsskript, direkt nach dem Block „Datenschicht (ADR-0006)“: neuer Block „Inhalte aus Events“), Create `tests/inhalte.test.ts`, Modify `docs/daten.md` (Abschnitt „Inhalte aus Events“). Branch `pr/inhalte-aus-events` ab `main`.

**Interfaces:**
- Consumes: `hubFetch(name, filters, opts)`, `datenstand`, `npubToHex`, `naddr(d, pubHex, kind)`, `esc` (Anwendungsskript, Zeile um 2127), `sichereUrl(u)` (nur `http(s)://`, sonst `''`).
- Produces:
  - `const FO_NPUB = 'npub1tgftg8kptdrxxg0g3sm3hckuglv3j0uu3way4vylc5qyt0f44m0s3gun6e'`, `const FO_HEX = npubToHex(FO_NPUB)`; Kommentar: Schaufenster-Schlüssel oer.community (ADR-0027 dort).
  - `function tagWert(ev, name)` → erster Wert des Tags `name` oder `''`; `function tagWerte(ev, name)` → alle Werte als Array.
  - `function mdSeite(src)` → HTML-String. Regeln: zuerst `esc()` auf jede Zeile; Überschriften `#` bis `####` werden `<h2>` bis `<h5>` (eine Stufe tiefer, die Ansicht hat die `<h1>`); Absätze; ungeordnete (`- `, `* `) und geordnete Listen (`1. `); Blockquote (`> `); Fett `**`, Kursiv `*`, Code `` ` ``; Links `[text](url)` nur mit `sichereUrl(url)`, sonst nur der Text; Bilder `![alt](url)` mit `sichereUrl` als `<img loading="lazy" alt="…">` in `<figure>`, bei relativer Adresse ein `<span class="img-fehlt">Bild: alt</span>`; Zeilen `---` als `<hr>`; Tabellen werden nicht erkannt (Zeilen bleiben Absätze). Leerer Eingang → `''`. Die bestehende Funktion `md(src)` (Blog-Editor-Vorschau) bleibt unverändert.
  - `function lizenzLabel(url)` → Kürzel nach `lizenzlabel.js` aus dem oer-community-Repo (Werte kopiert: CC0, Public Domain, Unsplash, Pixabay, Canva, Wikipedia-Urheberrecht → „Urheberrechtlich geschützt“, MIT, `CC <KÜRZEL> <Version>[ <LAND>]`; unbekannt → die URL; leer → `''`). `legalcode.de` und `deed.de` am Ende werden vorher abgeschnitten (Befund: so liegen die URLs auf dem Relay).
  - `function lizenzStand(url)` → `'offen'` (CC0, Public Domain Mark, CC BY, CC BY-SA), `'geschuetzt'` (CC mit NC oder ND, Wikipedia-Urheberrecht, Unsplash, Pixabay, Canva, jede andere bekannte Nicht-OER-Adresse), `'unbekannt'` (leer oder nicht erkannt). Kommentar nennt die Quelle der Regel (Issue 15, Spec 4.3: offen = holen, weiterbearbeiten, sammeln; geschützt = ansehen und verlinken).
  - `function ocLaden()` → `Promise<{ seiten: Map<d, ev>, beitraege: ev[], listen: { navigation: ev|null, fusszeile: ev|null }, termine: ev[] }>`, einmal je Sitzung (`ocDaten` gehalten): `hubFetch('oercommunity', [{ kinds: [30023], authors: [FO_HEX], '#l': ['seite'], limit: 40 }, { kinds: [30023], authors: [FO_HEX], limit: 40 }, { kinds: [30004], authors: [FO_HEX], limit: 5 }, { kinds: [31923], authors: [FO_HEX], limit: 200 }], { relays: ['wss://relay-rpi.edufeed.org', 'wss://relay.edufeed.org'] })`; je Adresse (`kind:pubkey:d`) gilt das neueste `created_at`; Seite = `kind:30023` mit Tag `['l','seite',…]`; Beiträge = die übrigen `kind:30023`, sortiert nach `published_at` (sonst `created_at`) absteigend; Termine nach `start` aufsteigend.
  - `function beitragUrl(ev)` → `'https://oer.community/' + encodeURIComponent(d) + '/'`; `function beitragBild(ev)` → `sichereUrl(tagWert(ev, 'image'))` (relative Bildnamen ergeben `''`, Platzhalter mit Titel, ADR-0002 Punkt 3).

- [ ] **Step 1: Tests schreiben** (`tests/inhalte.test.ts`; Technik aus `tests/datenschicht.test.ts`: Funktionsquelltext per Regex aus `appScript()` schneiden und mit `new Function` bauen, `esc` und `sichereUrl` mitgeben)

```ts
import { assert, assertEquals } from 'jsr:@std/assert@1';
import { appScript, html } from './helfer.ts';
const s = appScript();
const block = (re: RegExp) => (s.match(re) || [''])[0];
const esc = (t: string) => String(t).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]!));
const sichereUrl = (u: string) => /^https?:\/\//.test(u || '') ? u : '';
const bau = (name: string) => new Function('esc', 'sichereUrl', block(new RegExp(`  function ${name}\\([^)]*\\) \\{[\\s\\S]*?\\n  \\}`)) + `; return ${name};`)(esc, sichereUrl);

Deno.test('Inhalte aus Events: Schlüssel, Signaturen, Doku', async () => {
  assert(/const FO_NPUB = 'npub1tgftg8kptdrxxg0g3sm3hckuglv3j0uu3way4vylc5qyt0f44m0s3gun6e'/.test(s) && /const FO_HEX = npubToHex\(FO_NPUB\)/.test(s), 'Schaufenster-Schlüssel');
  for (const f of ['tagWert(ev, name)', 'tagWerte(ev, name)', 'mdSeite(src)', 'lizenzLabel(url)', 'lizenzStand(url)', 'ocLaden()', 'beitragUrl(ev)', 'beitragBild(ev)']) assert(s.includes('function ' + f), f);
  assert(/function md\(src\)/.test(s), 'md() für den Editor bleibt');
  const d = await Deno.readTextFile(new URL('../docs/daten.md', import.meta.url));
  assert(/ocLaden/.test(d) && /mdSeite/.test(d) && /lizenzStand/.test(d), 'docs/daten.md');
});

Deno.test('mdSeite: maskiert und filtert', () => {
  const md = bau('mdSeite');
  const out = md('# Titel\n\n<script>alert(1)</script> **fett**\n\n- a\n- b\n\n1. eins\n\n> Zitat\n\n[ok](https://oer.community/x) [böse](javascript:alert(1)) ![Bild](bild.jpg) ![Foto](https://blossom.edufeed.org/a.jpg)');
  assert(out.startsWith('<h2>Titel</h2>'), 'Überschrift eine Stufe tiefer');
  assert(!/<script/.test(out) && /&lt;script&gt;/.test(out), 'HTML maskiert');
  assert(/<b>fett<\/b>/.test(out) && /<ul><li>a<\/li><li>b<\/li><\/ul>/.test(out) && /<ol><li>eins<\/li><\/ol>/.test(out) && /<blockquote>Zitat<\/blockquote>/.test(out), 'Auszeichnung');
  assert(/<a href="https:\/\/oer\.community\/x"[^>]*rel="noopener"/.test(out), 'sicherer Link');
  assert(!/javascript:/.test(out) && /böse/.test(out), 'unsicherer Link wird Text');
  assert(/img-fehlt">Bild: Bild</.test(out) && /<img[^>]*src="https:\/\/blossom\.edufeed\.org\/a\.jpg"/.test(out), 'Bilder');
  assertEquals(md(''), '');
});

Deno.test('lizenzLabel und lizenzStand', () => {
  const label = bau('lizenzLabel'), stand = bau('lizenzStand');
  assertEquals(label('http://creativecommons.org/licenses/by-sa/4.0/legalcode.de'), 'CC BY-SA 4.0');
  assertEquals(label('https://creativecommons.org/licenses/by/4.0/deed.de'), 'CC BY 4.0');
  assertEquals(label('https://creativecommons.org/publicdomain/zero/1.0/'), 'CC0 (Public Domain)');
  assertEquals(label('https://de.wikipedia.org/wiki/Urheberrecht_(Deutschland)'), 'Urheberrechtlich geschützt');
  assertEquals(label('https://example.org/eigene'), 'https://example.org/eigene');
  assertEquals(label(''), '');
  assertEquals(stand('https://creativecommons.org/licenses/by/4.0/'), 'offen');
  assertEquals(stand('https://creativecommons.org/publicdomain/zero/1.0/'), 'offen');
  assertEquals(stand('https://creativecommons.org/licenses/by-nc-sa/4.0/'), 'geschuetzt');
  assertEquals(stand('https://creativecommons.org/licenses/by-nd/4.0/'), 'geschuetzt');
  assertEquals(stand('https://de.wikipedia.org/wiki/Urheberrecht_(Deutschland)'), 'geschuetzt');
  assertEquals(stand(''), 'unbekannt');
  assertEquals(stand('https://example.org/eigene'), 'unbekannt');
});

Deno.test('ocLaden: ein REQ je Relay, Seiten und Beiträge getrennt', () => {
  const oc = block(/function ocLaden\(\)[\s\S]*?\n  \}/);
  assert(/hubFetch\('oercommunity', \[/.test(oc) && (oc.match(/kinds: \[30023\]/g) || []).length === 2 && /kinds: \[30004\]/.test(oc) && /kinds: \[31923\]/.test(oc), 'vier Filter in einem Aufruf');
  assert(/'#l': \['seite'\]/.test(oc) && /authors: \[FO_HEX\]/.test(oc), 'Seiten-Label und Absender');
  assert(/relay-rpi\.edufeed\.org/.test(oc) && /relay\.edufeed\.org/.test(oc) && !/amb-relay/.test(oc), 'Relays des Schaufensters');
  assert(/published_at/.test(oc), 'Beiträge nach published_at');
  assert(!/groups\.edufeed\.org/.test(html));
});
```

- [ ] **Step 2: Fehlschlag sehen** · Run: `deno task test` · Expected: vier FAIL in `inhalte.test.ts` (Funktionen fehlen), 37 PASS.

- [ ] **Step 3: Block „Inhalte aus Events“ schreiben** (Konstanten, acht Funktionen, `ocDaten`-Halter), `docs/daten.md` um den Abschnitt „Inhalte aus Events“ ergänzen (Filter, Sortierung, Sicherheitsregel, Lizenzregel mit den Stand-Werten).

- [ ] **Step 4: Tests laufen lassen** · Expected: grün (41).

- [ ] **Step 5: Committen, PR** (`pr/inhalte-aus-events`)

```bash
git add index.html tests/inhalte.test.ts docs/daten.md && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "Inhalte aus Events: Seitenrenderer, Schaufenster-Daten vom FOERBICO-Schlüssel, Lizenzkürzel und Lizenzstand"
```

### Task 2: Schaufenster live vom Relay: Start, Menü, Beiträge, Seiten, Termine-Archiv (Issue 10 `4a3d1b54`)

**Files:** Modify `index.html` (Ansicht `#v-oercommunity`: `data-stand="stand:28.10.2026"` bleibt Startwert; `ocRender()` wird `ocRender(daten)`; neue Seitenansicht; `route()`; CSS-Block „oer.community“), Modify `tools/schnappschuss.ts` (zweiter Block), Modify `tests/inhalte.test.ts`, `tests/navigation.test.ts` (Zählung der Stand-Zeilen bleibt gültig). Branch `pr/schaufenster-live` ab `pr/inhalte-aus-events`.

**Interfaces:**
- Consumes: `ocLaden`, `mdSeite`, `beitragUrl`, `beitragBild`, `tagWert`, `datenstand`, `OC_POSTS`, `OC_TAGUNGEN`, `OC_TEAM`, `evToTermin`.
- Produces:
  - Routen: `#oercommunity` (Schaufenster), `#oercommunity/<d>` (eine Seite des Schaufensters, zum Beispiel `#oercommunity/qualitaet`). `route()` trennt zuerst an `?`, dann `view` an `/`: `const [viewRaw, qs] = raw.split('?'); const [view, sub] = viewRaw.split('/');`; `sub` wird an `ocOpen(sub)` gegeben; unbekannter `sub` zeigt die Startseite des Schaufensters mit Toast „Diese Seite gibt es im Schaufenster nicht.“ Die Liste gültiger Ansichten bleibt.
  - `function ocOpen(sub)`: zeigt sofort den Schnappschuss (`ocRender(null)` = heutiger Stand aus `OC_POSTS`/`OC_TAGUNGEN`/`OC_TEAM`), ruft `ocLaden()` und rendert mit Daten. Stand-Zeile: vor der Antwort „Stand vom 28.10.2026“; mit Antwort `live · <n> Beiträge · <m> Seiten`; ohne Antwort bleibt „Stand vom 28.10.2026“.
  - `function ocRender(daten)`: **Menü** aus der Liste `navigation` (`a`-Tags in Reihenfolge, Beschriftung = `title` der referenzierten Seite, Ziel `#oercommunity/<d>`), plus feste Einträge „Spielregeln“ (`#oercommunity/spielregeln`, Task 3), „Blog“ (`#oc-blog`), „Team“ (`#oc-team`); ohne Liste die bisherigen Knöpfe. **Start**: Inhalt der Seite `startseite` über `mdSeite` (Bild `/images/FOERBICO.png` ist relativ und wird Platzhalter; davor bleibt das feste `<img src="https://oer.community/images/FOERBICO.png">`), ohne Daten der bisherige Starttext. **Blog**: die zwölf neuesten Beiträge als `oc-card` (Bild über `beitragBild`, sonst Platzhalter mit Titel; Titel verlinkt auf `beitragUrl`; Datum aus `published_at` im Format `TT.MM.JJJJ`; `t`-Tags als Chips, höchstens sechs; `summary` als Text; Lizenzpille nur, wenn ein Tag `image:license` oder `license` vorhanden ist, sonst keine), Link „Alle Beiträge auf oer.community ›“. **Tagungen**: Inhalt der Seite `tagungen` über `mdSeite`, ohne Daten `OC_TAGUNGEN`. **Was ist OER? · Qualität**: zwei Karten mit Link auf `#oercommunity/oer-und-oep` und `#oercommunity/qualitaet` und dem `summary` der jeweiligen Seite. **Team**: bleibt `OC_TEAM` mit Initialen (Porträts ©), darunter Link „Teamseite auf oer.community ›“. **Termine-Archiv** (neuer Abschnitt `#oc-termine`): alle `kind:31923` des Schaufenster-Schlüssels chronologisch, vergangene grau mit „vergangen“, anstehende mit Link `u`; sind es null, der Satz „Unter dem Schaufenster-Schlüssel liegen noch keine Termine; Tagungen stehen auf der Tagungsseite.“ mit Link `#oercommunity/tagungen`. **Projektlogbuch**: Satz „Der offene Issue-Tracker ist das Logbuch des Projekts.“ mit Link `https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues` (`target="_blank" rel="noopener"`). Fußzeile: Links aus der Liste `fusszeile` (Impressum, Datenschutz als `#oercommunity/<d>`), ohne Liste die bisherigen externen Links.
  - Seitenansicht (`sub` gesetzt): `<article class="oc-seite">` mit `<h1>` = `title`, Datum `published_at`, Inhalt `mdSeite(content)`, Lizenzzeile „CC BY 4.0 FOERBICO“ nur wenn `tagWert(ev,'license')` oder die Fußzeile es sagt (sonst „Lizenz: siehe oer.community“), Link „Auf oer.community ansehen ›“ (`https://oer.community/<d>/`), Rückweg „‹ Schaufenster“. Fehlt die Seite im Ergebnis: Hinweis „Diese Seite ist in Vorbereitung.“ mit Link auf oer.community; Stand-Zeile unverändert.
  - Schnappschuss: `tools/schnappschuss.ts` holt zusätzlich die sechs neuesten Beiträge des Schaufenster-Schlüssels (`{ kinds: [30023], authors: [FO], limit: 12 }`, Seiten-Label ausgeschlossen, gekürzt auf `id, pubkey, created_at, kind, tags, content: ''`) und schreibt sie zwischen `/* schnappschuss:beitraege */` und `/* /schnappschuss:beitraege */` als `let OC_RAW = […]; let OC_STAND = 'TT.MM.JJJJ';` `OC_POSTS` entsteht daraus (`OC_RAW.map(…)`) in der bisherigen Form `{ t, date, ago, tags, x, img, lic: '', url }` (`date` aus `published_at` als `TT.MM.JJJJ`, `ago` berechnet als „vor n Tagen“ oder „vor n Wochen“, `tags` aus `t`, `x` aus `summary`, `img` über `beitragBild`, `url` über `beitragUrl`), weil `CR.oercommunity` diese Felder weiter liest; `data-stand` der Ansicht wird `stand:<OC_STAND>` beim Laden gesetzt. Beim ersten Lauf des Skripts ersetzt der Implementierer die bisherige handgeschriebene Liste; Ausgabe des Skripts: `<n> Termine, <k> Beiträge, Stand <Datum>`. Liefert das Relay für einen Block nichts, bleibt dieser Block unverändert.

- [ ] **Step 1: Tests ergänzen**

```ts
Deno.test('Schaufenster live: Routen, Menü, Abschnitte, Schnappschuss', async () => {
  const route = block(/function route\(\)[\s\S]*?window\.scrollTo/);
  assert(/split\('\/'\)/.test(route) && /ocOpen\(/.test(route), 'Unterroute #oercommunity/<d>');
  const oc = block(/function ocRender\(daten\)[\s\S]*?\n  \}/);
  assert(/navigation/.test(oc) && /#oercommunity\/spielregeln/.test(oc) && /id="oc-termine"/.test(oc) && /FOERBICO_und_rpi-virtuell\/issues/.test(oc), 'Menü, Spielregeln-Eintrag, Termine-Archiv, Logbuch');
  assert(/mdSeite\(/.test(oc) && /beitragBild\(/.test(oc) && /beitragUrl\(/.test(oc), 'Seiten und Beiträge aus Events');
  assert(/OC_TEAM/.test(oc) && /ocInit\(/.test(oc), 'Team bleibt Schnappschuss mit Initialen');
  assert(/noch keine Termine/.test(oc), 'ehrlicher Satz bei leerem Archiv');
  assert(/in Vorbereitung/.test(block(/function ocOpen\(sub\)[\s\S]*?\n  \}/) + oc), 'fehlende Seite');
  assert(/schnappschuss:beitraege \*\/[\s\S]*let OC_RAW = \[[\s\S]*let OC_STAND = '\d\d\.\d\d\.\d{4}'[\s\S]*\/schnappschuss:beitraege/.test(s), 'Schnappschuss-Block Beiträge');
  assert(/const OC_POSTS = OC_RAW\.map\(/.test(s), 'OC_POSTS aus OC_RAW');
  assert(!/<\//.test(s.match(/let OC_RAW = .*/)![0]), 'OC_RAW enthält </');
  const t = await Deno.readTextFile(new URL('../tools/schnappschuss.ts', import.meta.url));
  assert(/schnappschuss:beitraege/.test(t) && /30023/.test(t) && /'seite'/.test(t), 'Skript kennt den zweiten Block');
  assert((html.match(/<div class="view"/g) || []).length - 1 === (html.match(/class="stand"/g) || []).length, 'Stand-Zeilen vollständig');
});
```

- [ ] **Step 2: Fehlschlag sehen** · Expected: ein FAIL („Unterroute …“), 41 PASS.

- [ ] **Step 3: Ansicht, `ocOpen`, `ocRender`, Seitenansicht, CSS (`.oc-seite`, `.oc-termin`, `.img-fehlt`), Routing und Schnappschuss-Skript schreiben**; einmal `deno task schnappschuss` laufen lassen (nicht wiederholen); `docs/daten.md` Tabelle „Zustände je Ansicht“ für `v-oercommunity` auf „Stand vom `OC_STAND` → live“ ändern.

- [ ] **Step 4: Tests laufen lassen** · Expected: grün (42).

- [ ] **Step 5: Im Browser prüfen** (Dateiserver außerhalb des Repos): `#oercommunity` zeigt Stand-Zeile „live · …“, Menü aus der Liste (Tagungen, OER und OEP, Qualität, Team, Spielregeln, Blog), zwölf Beiträge mit Bildern oder Platzhaltern; `#oercommunity/qualitaet` rendert die Seite mit Überschriften und Links; `#oercommunity/gibtsnicht` zeigt Start und Toast; Netzwerk: zwei WebSockets; Konsole ohne Ausnahme; `?` im Markdown der Seiten ergibt kein HTML.

- [ ] **Step 6: Committen, PR** (`pr/schaufenster-live`)

```bash
git add index.html tools/schnappschuss.ts tests/inhalte.test.ts docs/daten.md && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "Schaufenster live vom Relay: Menü und Seiten aus Listen und Events, Beiträge, Termine-Archiv, Logbuch; Schnappschuss der Beiträge"
```

### Task 3: Spielregeln als Bereich im Schaufenster (Issue 03 `371d9cbf`)

**Files:** Modify `index.html` (Bereich `#oercommunity/spielregeln`, Konstante `SPIELREGELN`, Erklärkarte `EX['veroeffentlichen']`-Hinweis, Kontext `oer-community`), Modify `tests/inhalte.test.ts`, Modify `docs/navigation.md` (Zeile Spielregeln). Branch `pr/spielregeln` ab `pr/schaufenster-live`.

**Interfaces:**
- Consumes: `ocLaden`, `ocOpen(sub)`, `mdSeite`, `datenstand`.
- Produces:
  - `const SPIELREGELN = [ { d: 'spielregeln-qualitaetskriterien', t: 'Qualitätskriterien', x: 'Vier Dimensionen, Checklisten, die Handreichung.', heute: 'https://oer.community/qualitaet/' }, { d: 'spielregeln-metadatenprofil', t: 'Metadatenprofil', x: 'Welche Felder, welche Vokabulare, mit Links auf die Begriffe.', heute: 'https://oer.community/metadaten-die-unsichtbare-infrastruktur-offener-bildung/' }, { d: 'spielregeln-redaktion', t: 'Redaktion', x: 'Wie ein Entwurf zur Veröffentlichung wird, wer freigibt, wie Bildnachweise aussehen.', heute: 'https://oer.community/blog/' }, { d: 'spielregeln-ablaeufe', t: 'Abläufe', x: 'Vom Beitrag im Git zum Relay, von der Webseite zum Termin.', heute: 'https://oer.community/blog/' } ]`. Die `d`-Namen sind die Konvention für den Inhaltsstrang (Task 7); `heute` ist der Verweis, solange die Seite fehlt.
  - `#oercommunity/spielregeln`: Kopf „Spielregeln“ mit Satz „Die gemeinsame Grammatik des Ökosystems: nach diesen Regeln entstehen Material, Beiträge und Termine.“; vier Kacheln (`oc-card`) mit Titel, Satz und Knopf: liegt die Seite vor (in `ocDaten.seiten`), „Lesen ›“ nach `#oercommunity/<d>`, sonst Vermerk „in Vorbereitung“ (Klasse `oc-vorbereitung`) und Link „Heute: auf oer.community ›“ (`heute`, `_blank`). Fünfte Kachel „Veröffentlichen: so geht es“ mit Link `#veroeffentlichen` → Hinweis: Das Tutorial ist Stufe B (Spec 4.4); die Kachel führt zur Konsole „veröffentlichen“ im Tutorial-Modus (`setModus('tutorial'); go('start'); ` und Toast „Die Konsole erklärt die drei Wege zum Relay.“). Stand-Zeile des Schaufensters bei geöffnetem Bereich: `live · <k> von 4 Seiten` (k aus `ocDaten.seiten`), ohne Daten „Stand vom <OC_STAND> · 0 von 4 Seiten“.
  - Lizenzpille und Prüf-Marker (Task 5) verlinken auf `#oercommunity/spielregeln-qualitaetskriterien`, wenn die Seite vorliegt, sonst auf `#oercommunity/spielregeln`: dafür `function spielregelLink(d)` → Route.
  - Kontext `oer-community`: `veroeffentlichen.*` bleibt in der Standardkette; `kooperieren.communities` unverändert. `docs/navigation.md`: neue Zeile „Spielregeln | Schaufenster-Menü | — | — | #oercommunity/spielregeln“ in der Begriffstabelle.

- [ ] **Step 1: Tests ergänzen**

```ts
Deno.test('Spielregeln: vier Seiten mit Vorbereitungs-Rückfall', async () => {
  const sr = block(/const SPIELREGELN = \[[\s\S]*?\n  \];/);
  for (const d of ['spielregeln-qualitaetskriterien', 'spielregeln-metadatenprofil', 'spielregeln-redaktion', 'spielregeln-ablaeufe']) assert(sr.includes(`d: '${d}'`), d);
  assert((sr.match(/heute: 'https:\/\//g) || []).length === 4, 'jede Kachel hat einen Verweis für heute');
  assert(/in Vorbereitung/.test(s) && /oc-vorbereitung/.test(s) && /von 4 Seiten/.test(s), 'Rückfall sichtbar');
  assert(/function spielregelLink\(d\)/.test(s), 'spielregelLink');
  assert(/'spielregeln'/.test(block(/function ocOpen\(sub\)[\s\S]*?\n  \}/)), 'ocOpen kennt den Bereich');
  const n = await Deno.readTextFile(new URL('../docs/navigation.md', import.meta.url));
  assert(/Spielregeln/.test(n), 'docs/navigation.md');
});
```

- [ ] **Step 2: Fehlschlag sehen** · Expected: ein FAIL, 42 PASS.

- [ ] **Step 3: Bereich, Konstante, Kacheln, `spielregelLink`, Stand-Zeile, CSS (`.oc-vorbereitung` in `--fo-text` auf `--fo-hell`, Kontrast prüfen) und Doku-Zeile schreiben.**

- [ ] **Step 4: Tests laufen lassen** · Expected: grün (43).

- [ ] **Step 5: Im Browser prüfen**: `#oercommunity/spielregeln` zeigt vier Kacheln „in Vorbereitung“ mit Links, Stand-Zeile „live · 0 von 4 Seiten“; die Kachel „Veröffentlichen“ schaltet die Konsole in den Tutorial-Modus; bei 375 px eine Spalte.

- [ ] **Step 6: Committen, PR** (`pr/spielregeln`)

```bash
git add index.html tests/inhalte.test.ts docs/navigation.md && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "Spielregeln als Bereich im Schaufenster: vier Seiten vom Relay mit Vorbereitungs-Rückfall, Weg zum Veröffentlichen"
```

### Task 4: Materialpool live als kind:30142 mit Suche, Vorauswahl und Zähler (Issue 04 `9770e756`, Spec 4.12)

**Files:** Modify `index.html` (Ansicht `#v-materialpool`: Liste `#mpList`, Suchformular, Fußzeile; Anwendungsskript: `mpLaden()`, `mpRender()`, `mpOpen(qs)`, `MP`-Rückfall bleibt), Modify `tests/inhalte.test.ts`, `docs/daten.md`. Branch `pr/materialpool-live` ab `pr/spielregeln`.

**Interfaces:**
- Consumes: `hubFetch`, `datenstand`, `tagWert`, `tagWerte`, `lizenzLabel`, `lizenzStand`, `sichereUrl`, `PRE_NAMES`, `route()`-Zweig `materialpool` (Vorauswahl `thema`/`stufe`).
- Produces:
  - `function mpLaden()` → `Promise<ev[]>`, einmal je Sitzung: `hubFetch('materialpool', [{ kinds: [30142], limit: 200 }])` auf allen drei Relays; je Adresse (`pubkey:d`) das neueste `created_at`; Ergebnis in `mpDaten` gehalten (Task 5 liest daraus).
  - `function mpMaterial(ev)` → `{ d, pk, t: name, x: description, art: learningResourceType:prefLabel:de (sonst letzter Pfadteil von learningResourceType:id), stufe: educationalLevel:prefLabel:de, fach: about:prefLabel:de (erste), lic: license:id, licLabel: lizenzLabel(lic), stand: lizenzStand(lic), bild: sichereUrl(image), quelle: publisher:name oder creator:name (erste), url: sichereUrl(r) oder sichereUrl(d), datum: datePublished oder dateCreated oder created_at, vollstaendig: boolean }`; `vollstaendig` = `name`, `description`, `license:id`, `learningResourceType:id` und (`about:id` oder `educationalLevel:id`) vorhanden (Zähler nach Spec 4.12).
  - `function mpRender()`: Karten `mp-card` aus `mpDaten` (neueste 24 nach `datum`), je Karte Titel als Link `#materialpool?d=<encodeURIComponent(d)>`, Zeile `art · quelle · stufe`, Lizenzpille `<span class="lic lic-<stand>">licLabel oder „Lizenz nicht angegeben“</span>`; Suche (`input[type=search]`, Eingabe filtert clientseitig auf `t`, `x`, `keywords`, `t`-Tags, `about:prefLabel:de`; Rotation `#mpRot` bleibt); Vorauswahl aus `route()` (`thema`, `stufe`) filtert mit derselben Regel; leer: „Nichts gefunden; Vorauswahl entfernen oder anders suchen.“ Fußzeile: `<n> von <m> Materialien mit vollständigen Metadaten · live von <k> Relays` ersetzt den Satz vom Spiegel; Stand-Zeile `live · <m> Materialien`. Ohne Antwort: Karten aus `MP` (sechs), Stand „Stand vom 22.10.2026“, Fußzeile wie bisher. Rotation `#mpRot` und Sektion „Aktuelle Empfehlung“ bleiben.
  - `function mpOpen(qs)`: aus `route()` aufgerufen (ersetzt den bisherigen Inline-Zweig); `?d=` wird in Task 5 ausgewertet (hier: ignorieren).

- [ ] **Step 1: Tests ergänzen**

```ts
Deno.test('Materialpool live: Karten ohne unsichere Adressen, Zähler, Rückfall', () => {
  const mp = block(/function mpLaden\(\)[\s\S]*?\n  \}/);
  assert(/hubFetch\('materialpool', \[\{ kinds: \[30142\], limit: 200 \}\]/.test(mp), 'ein Filter, alle Relays');
  const m = block(/function mpMaterial\(ev\)[\s\S]*?\n  \}/);
  assert(/sichereUrl\(/.test(m) && /lizenzStand\(/.test(m) && /lizenzLabel\(/.test(m) && /vollstaendig/.test(m), 'Felder');
  const r = block(/function mpRender\(\)[\s\S]*?\n  \}/);
  assert(/#materialpool\?d=/.test(r) && /encodeURIComponent/.test(r) && /Lizenz nicht angegeben/.test(r) && /vollständigen Metadaten/.test(r), 'Karten, Pille, Zähler');
  assert(/MP\.map\(/.test(r) || /MP\.map\(/.test(s), 'Rückfall auf den Schnappschuss');
  assert(/function mpOpen\(qs\)/.test(s) && /mpOpen\(qs\)/.test(block(/function route\(\)[\s\S]*?window\.scrollTo/)), 'route ruft mpOpen');
  assert(/lic-offen/.test(html) && /lic-geschuetzt/.test(html) && /lic-unbekannt/.test(html), 'drei Pillen im CSS');
});
```

- [ ] **Step 2: Fehlschlag sehen** · Expected: ein FAIL, 43 PASS.

- [ ] **Step 3: `mpLaden`, `mpMaterial`, `mpRender`, `mpOpen`, Suche, Fußzeile, CSS der Pillen (`.lic-offen` grün-, `.lic-geschuetzt` grau-, `.lic-unbekannt` gelbtonig; Textfarben 4,5:1 auf dem jeweiligen Hellton, Farben in `:root` als `--lic-*`) schreiben; `docs/daten.md`: Verbraucher „Materialpool“ mit Filter, Dedupe, Zählerregel.**

- [ ] **Step 4: Tests laufen lassen** · Expected: grün (44).

- [ ] **Step 5: Im Browser prüfen**: `#materialpool` zeigt Stand-Zeile „live · … Materialien“, 24 Karten mit Pillen, Fußzeile mit Zähler; Suche „Feste“ filtert; `#materialpool?thema=Schöpfung` filtert über die Vorauswahl; Netzwerk: drei WebSockets, je ein REQ; offline (DevTools) bleiben die sechs Karten mit „Stand vom 22.10.2026“.

- [ ] **Step 6: Committen, PR** (`pr/materialpool-live`)

```bash
git add index.html tests/inhalte.test.ts docs/daten.md && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "Materialpool live: Materialien als kind:30142 von drei Relays, Suche und Vorauswahl, Lizenzpille, Zähler vollständiger Metadaten"
```

### Task 5: Material-Detail mit Vokabular-Links, Rohdaten und Lizenzstand (Issue 04 `9770e756`, Issue 15 `516faa60`, Spec 4.3, 4.13)

**Files:** Modify `index.html` (Ansicht `#v-materialpool`: neuer Block `<section class="mp-detail" id="mpDetail" hidden>`; Anwendungsskript: `mpDetail(d)`, `ambJsonLd(ev)`, `lizenzAktionen(stand)`; CSS), Modify `tests/inhalte.test.ts`, `docs/daten.md`. Branch `pr/material-detail` ab `pr/materialpool-live`.

**Interfaces:**
- Consumes: `mpDaten`, `mpMaterial`, `mpOpen(qs)`, `hubFetch`, `tagWerte`, `lizenzStand`, `lizenzLabel`, `spielregelLink`, `naddr`, `go`, `openChooser`, `toast`, `sichereUrl`.
- Produces:
  - `mpOpen(qs)`: bei `?d=<d>` ruft `mpDetail(decodeURIComponent(d))`, blendet Hero und Listen aus (`#v-materialpool.detail`), sonst Liste.
  - `function mpDetail(d)`: Material aus `mpDaten` (Treffer: kein Netz); fehlt es, ein gezielter Aufruf `hubFetch('material:' + d, [{ kinds: [30142], '#d': [d], limit: 2 }])`; fehlt es weiter: „Material nicht gefunden.“ mit Link „‹ Zum Materialpool“. Darstellung: Rückweg „‹ Materialpool“; `<h1>` Titel; Bild (`sichereUrl(image)`, sonst Platzhalter mit Art-Symbol); Beschreibung; **Felder** als Definitionsliste: Fach (alle `about`), Bildungsstufe (`educationalLevel`), Art (`learningResourceType`), Zielgruppe (`audience`): je Wert ein Chip mit Text `prefLabel:de` (sonst letzter Pfadteil der ID) und `href` = `sichereUrl(id)` (`target="_blank" rel="noopener"`, Titel „Begriff im Vokabular“); dafür `function ambWerte(ev, feld)` → `[{ id, label }]` aus den Tags `feld:id` und dem jeweils folgenden `feld:prefLabel:de` (Reihenfolge der Tags). Quelle (`publisher:name`, `creator:name`), Datum, Link „Zur Ressource ›“ (`r` oder `d` als URL) und „Bei edufeed ansehen ›“ (`https://edufeed.org/` + `naddr(d, pubkey, 30142)`). **Lizenzpille** groß mit `lizenzLabel` und Link auf `license:id`; **Bildnachweis**: nur wenn ein Tag `image:license:id` oder `image:creator:name` existiert, sonst keine Zeile. **Rohdaten-Knopf** „Rohdaten (JSON-LD)“: öffnet `<details>` mit `<pre>` = `JSON.stringify(ambJsonLd(ev), null, 2)` und Knopf „Kopieren“ (`rtCopy`), Vermerk „aus dem Event gebildet (AMB-Kontext)“. **Lizenzstand**: Zeile mit einem Satz je Stand: offen „Offen lizenziert: Du kannst es auf den Schreibtisch holen, in der Community weiterbearbeiten und in Sammlungen aufnehmen.“; geschützt „Geschützt: Du kannst es ansehen, verlinken und empfehlen; Weiterbearbeiten und Sammeln gehen nur mit offener Lizenz.“; unbekannt „Lizenz nicht angegeben: Bis das geklärt ist, gilt es als geschützt.“ Darunter die Aktionen aus `lizenzAktionen(stand, m)`.
  - `function lizenzAktionen(stand, m)` (`m` = Material aus `mpMaterial`, nur in den `tu`-Funktionen gelesen, nie beim Aufbau) → Array `{ label, geht, tu }`: „Auf den Schreibtisch holen“ (`go('relidesk?tab=schreibtisch')`), „In der Community weiterbearbeiten“ (`openChooser('materialpool')`), „In Sammlung aufnehmen“ (Toast mit `data-todo`-Hinweis „Sammlungen kommen in der nächsten Etappe“), „Ansehen“ (Link zur Ressource), „Link kopieren“ (`rtCopy(location.href, …)`), „Empfehlen“ (Toast „Teilen in Communities folgt“). `geht` = true für alle bei `offen`; bei `geschuetzt` und `unbekannt` sind die ersten drei `false`. Nicht gehende Aktionen werden als `<button disabled aria-disabled="true" title="…">` mit Hinweis „nur mit offener Lizenz“ gerendert, nicht ausgeblendet (Issue 15). Prüf-Marker „nach Kriterien geprüft“: nur wenn das Event ein Tag `['l', 'geprueft', …]` trägt, sonst der Satz „Noch nicht nach den Qualitätskriterien geprüft.“ mit Link `spielregelLink('spielregeln-qualitaetskriterien')` (Stufe B bleibt sichtbar als Lücke).
  - `function ambJsonLd(ev)` → Objekt: `@context: ['https://w3id.org/kim/amb/context.jsonld']`, `id` = `d`, `type` = alle `type`-Tags, `name`, `description`, `inLanguage`, `image`, `license: { id }`, `isAccessibleForFree` (als Boolean), `dateCreated`, `datePublished`, `dateModified`, `keywords` (alle `keywords`), und je Feld `about`, `learningResourceType`, `educationalLevel`, `audience`, `creator`, `publisher`, `conditionsOfAccess`, `interactivityType`: Array von Objekten aus `feld:id`, `feld:type`, `feld:name`, `feld:prefLabel:<lang>` → `prefLabel: { de: … }` (Gruppierung: ein neues Objekt beginnt bei `feld:id`, `feld:name` oder `feld:type` ohne vorheriges `id`). Keine Erfindung von Werten: fehlende Felder fehlen.
  - Materialpool-Karten (Task 4) tragen `data-stand`-Klasse der Pille; Konsole im Materialpool unverändert.

- [ ] **Step 1: Tests ergänzen**

```ts
Deno.test('lizenzAktionen: offen alles, geschützt nur ansehen', () => {
  const la = new Function('go', 'openChooser', 'toast', 'rtCopy', block(/  function lizenzAktionen\(stand, m\) \{[\s\S]*?\n  \}/) + '; return lizenzAktionen;')(() => {}, () => {}, () => {}, () => {});
  assertEquals(la('offen', {}).map((a: any) => a.geht), [true, true, true, true, true, true]);
  assertEquals(la('geschuetzt', {}).map((a: any) => a.geht).slice(0, 3), [false, false, false]);
  assertEquals(la('unbekannt', {}).map((a: any) => a.geht).slice(0, 3), [false, false, false]);
  assertEquals(la('geschuetzt', {}).length, 6, 'nichts verschwindet');
});

Deno.test('ambJsonLd und ambWerte: aus Tags gebildet, nichts erfunden', () => {
  const ev = { kind: 30142, pubkey: 'ab'.repeat(32), created_at: 1, content: '', tags: [['d', 'https://x.org/r'], ['type', 'LearningResource'], ['name', 'N'], ['license:id', 'https://creativecommons.org/licenses/by/4.0/'], ['about:id', 'https://w3id.org/kim/hochschulfaechersystematik/n0'], ['about:prefLabel:de', 'Fachübergreifend'], ['about:id', 'https://w3id.org/kim/x/n1'], ['audience:id', 'http://purl.org/dcx/lrmi-vocabs/educationalAudienceRole/teacher'], ['audience:prefLabel:de', 'Lehrperson'], ['isAccessibleForFree', 'true']] };
  const src = block(/  function tagWert\(ev, name\)[\s\S]*?\n  \}/) + block(/  function tagWerte\(ev, name\)[\s\S]*?\n  \}/) + block(/  function ambWerte\(ev, feld\)[\s\S]*?\n  \}/) + block(/  function ambJsonLd\(ev\)[\s\S]*?\n  \}/);
  const { ambWerte, ambJsonLd } = new Function(src + '; return { ambWerte, ambJsonLd };')();
  assertEquals(ambWerte(ev, 'about'), [{ id: 'https://w3id.org/kim/hochschulfaechersystematik/n0', label: 'Fachübergreifend' }, { id: 'https://w3id.org/kim/x/n1', label: 'n1' }]);
  const j = ambJsonLd(ev);
  assertEquals(j['@context'], ['https://w3id.org/kim/amb/context.jsonld']);
  assertEquals(j.id, 'https://x.org/r'); assertEquals(j.license, { id: 'https://creativecommons.org/licenses/by/4.0/' }); assertEquals(j.isAccessibleForFree, true);
  assertEquals(j.about[0], { id: 'https://w3id.org/kim/hochschulfaechersystematik/n0', prefLabel: { de: 'Fachübergreifend' } });
  assertEquals(j.audience[0].prefLabel, { de: 'Lehrperson' }); assert(!('description' in j) && !('educationalLevel' in j), 'fehlende Felder fehlen');
});

Deno.test('Material-Detail: Felder, Lizenzstand, Rohdaten, kein zweiter REQ bei Treffer im Cache', () => {
  const det = block(/function mpDetail\(d\)[\s\S]*?\n  \}/);
  assert(/mpDaten/.test(det) && /hubFetch\('material:' \+ d, \[\{ kinds: \[30142\], '#d': \[d\]/.test(det) && det.indexOf('mpDaten') < det.indexOf('hubFetch'), 'Cache vor Netz');
  assert(/Material nicht gefunden/.test(det) && /ambJsonLd\(/.test(det) && /lizenzAktionen\(/.test(det) && /spielregelLink\(/.test(det) && /naddr\(/.test(det), 'Bausteine');
  assert(/Begriff im Vokabular/.test(det) && /target="_blank" rel="noopener"/.test(det), 'Vokabular-Links');
  assert(/Offen lizenziert/.test(det) && /nur mit offener Lizenz/.test(det) && /disabled aria-disabled="true"/.test(det), 'Lizenzstand mit ausgegrauten Aktionen');
  assert(/image:license:id|image:creator:name/.test(det), 'Bildnachweis nur mit Tag');
  assert(/mpDetail\(decodeURIComponent/.test(block(/function mpOpen\(qs\)[\s\S]*?\n  \}/)), 'mpOpen wertet ?d= aus');
  assert(/id="mpDetail"/.test(html), 'Detail-Block in der Ansicht');
});
```

- [ ] **Step 2: Fehlschlag sehen** · Expected: drei FAIL, 44 PASS.

- [ ] **Step 3: Detail-Block, `mpDetail`, `ambWerte`, `ambJsonLd`, `lizenzAktionen`, CSS (`.mp-detail`, Definitionsliste, Chips in `--mp-dark` auf `--card`, deaktivierte Knöpfe mit sichtbarem Kontrast ≥ 3:1 für den Rahmen) schreiben; `docs/daten.md`: Verbraucher „Material-Detail“ (Cache-vor-Netz, Lizenzstand-Regel, JSON-LD aus Tags, Prüf-Marker als Stufe B).**

- [ ] **Step 4: Tests laufen lassen** · Expected: grün (47).

- [ ] **Step 5: Im Browser prüfen**: Karte anklicken → `#materialpool?d=…` zeigt Felder mit Links auf w3id/purl, Pille, Lizenzsatz, sechs Aktionen (drei ausgegraut bei NC- oder fehlender Lizenz), Rohdaten aufklappbar und kopierbar; Rückweg zur Liste; unbekanntes `d` zeigt „nicht gefunden“; Netzwerk: kein zusätzlicher WebSocket beim Öffnen aus der Liste; 375 px: Felder untereinander.

- [ ] **Step 6: Committen, PR** (`pr/material-detail`)

```bash
git add index.html tests/inhalte.test.ts docs/daten.md && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "Material-Detail: AMB-Felder mit Vokabular-Links, Lizenzpille, Rohdaten als JSON-LD, Lizenzstand bestimmt die Aktionen"
```

### Task 6: ADR-0007 und Doku der Etappe

**Files:** Create `docs/adr/0007-inhalte-aus-events.md`, Modify `README.md` (ADR-Tabelle, Ansichten-Liste: Schaufenster live, Spielregeln, Material-Detail), `docs/konstruktion.md` (Abschnitt Inhalte: Seiten, Beiträge, Materialien aus Events; Lizenzstand), `tests/inhalte.test.ts`. Branch `pr/doku-etappe-3` ab `pr/material-detail`.

**Interfaces:**
- Consumes: Entscheidungen der Tasks 1 bis 5.
- Produces: ADR-0007 nach der Vorlage in `docs/adr/README.md` (Status: angenommen · <Datum> · Entscheidung der Maintainer · Bezug: Issues `4a3d1b54…`, `371d9cbf…`, `9770e756…`, `516faa60…`), Entscheidung in fünf Punkten: (1) Inhalte des Schaufensters kommen als Events vom Schaufenster-Schlüssel (Seiten mit Seiten-Label, Beiträge, Listen `navigation`/`fusszeile`, Termine), Konvention der `d`-Namen für die Spielregeln; (2) der Hub rendert Markdown mit einem eigenen, maskierenden Renderer ohne Tabellen und ohne HTML-Durchreichung; (3) Teamseite bleibt Schnappschuss mit Initialen (Porträts ©); (4) Materialien kommen als `kind:30142` von allen drei Relays, Detailansicht aus dem Listen-Cache, JSON-LD aus den Tags gebildet; (5) Lizenzstand aus dem Lizenzfeld: offen / geschützt / unbekannt, nicht gehende Aktionen bleiben sichtbar; Prüf-Marker über NIP-32-Label ist Stufe B. Verworfen: Texte im Hub-Code; Markdown-Bibliothek von außen; Ausblenden gesperrter Aktionen. Folgen: Inhaltsstrang liefert die vier Seiten; Etappe 4 wendet die Lizenzregel auf Sammlung und Katalog an.

- [ ] **Step 1: Test ergänzen**

```ts
Deno.test('ADR-0007 und README nennen die Etappe', async () => {
  const adr = await Deno.readTextFile(new URL('../docs/adr/0007-inhalte-aus-events.md', import.meta.url));
  assert(/^# ADR-0007/.test(adr) && /## Status/.test(adr) && /## Entscheidung/.test(adr) && /4a3d1b54/.test(adr) && /516faa60/.test(adr));
  assert(!/Arbeitspaket|Meilenstein|Förderkennzeichen|Projektträger|Zwischenbericht/.test(adr), 'Projektsprache');
  const r = await Deno.readTextFile(new URL('../README.md', import.meta.url));
  assert(/0007-inhalte-aus-events/.test(r) && /Spielregeln/.test(r), 'README');
});
```

- [ ] **Step 2: Fehlschlag sehen** · Expected: ein FAIL, 47 PASS.
- [ ] **Step 3: ADR, README, Konstruktionsbeschreibung schreiben** (prüfen: `python3 -I ~/repositories/FOERBICO_und_rpi-virtuell/tools/nachweis/check.py gitworkshop docs`).
- [ ] **Step 4: Tests laufen lassen** · Expected: grün (48).
- [ ] **Step 5: Committen, PR** (`pr/doku-etappe-3`)

```bash
git add docs/adr/0007-inhalte-aus-events.md README.md docs/konstruktion.md tests/inhalte.test.ts && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "ADR-0007: Inhalte aus Events (Seiten, Beiträge, Materialien, Lizenzstand); README und Konstruktion nachgeführt"
```

### Task 7: Inhaltsstrang: die vier Spielregeln-Seiten als Markdown im FOERBICO-Repo (Spec 5a, Frist 30.11.)

**Files (FOERBICO-Repo, Branch `spielregeln-seiten` ab `main`):** Create `Website/content/de/spielregeln-qualitaetskriterien/index.md`, `Website/content/de/spielregeln-metadatenprofil/index.md`, `Website/content/de/spielregeln-redaktion/index.md`, `Website/content/de/spielregeln-ablaeufe/index.md`. Form wie `Website/content/de/qualitaet/index.md` (Frontmatter `commonMetadata` mit `name`, `description`, `datePublished`, `creator` FOERBICO, `license` CC BY 4.0, `id` `https://oer.community/<url>`, `inLanguage`, `learningResourceType` text/web_page, `educationalLevel` level_A; `staticSiteGenerator` mit `title` und `url` = der `d`-Name aus Task 3). Kein Code, keine Pipeline-Änderung: die Sync-Pipeline (`nostr-sync-pipeline`: Forgejo → GitHub-Spiegel → Action → mdparser → Amber) signiert Seiten mit dem FOERBICO-Schlüssel und setzt das Seiten-Label (ADR-0027); die Seiten erscheinen auf oer.community, aber nicht im Menü (Spec 5).

**Quellen (lesen, nicht kopieren, Nutzersicht):** Qualitätskriterien: `Website/content/de/qualitaet/index.md`, `Website/content/de/qualitaet/Handreichung_Qualitätskriterien.pdf`, Beiträge `2025-10-10-OER-Qualitätskriterien-Checkliste` und `2025-09-10-OER-und-visuelle-Qualität`. Metadatenprofil: Beitrag `2026-09-10-metadaten`, Vokabulare in `~/repositories/amb-religionsbezogen` und `~/repositories/grundschul-vokab` (Begriffe, Adressen; nocabs.edufeed.org als Ziel nennen, wo die Adressen dort liegen, sonst w3id/purl), `~/repositories/amb-nostr-converter/README.md` (Tag-Form). Redaktion: oer-community ADR-0021 (Redaktion in Nostr, Übernahme durch den FOERBICO-Schlüssel), ADR-0022/0032 (Lizenzpille, Lizenzstand), ADR-0013/0015/0023/0038 (Bilder, Bildnachweis-Konvention), `docs/bildattribution.md` im oer-community-Repo, falls vorhanden. Abläufe: Memory-Notizen `nostr-sync-pipeline` und `edufeed-kalender-konvention-prozess` (Kalender-Konvention, Guide-PR), oer-community ADR-0034 (Kalender aus der Community), `~/repositories/nostr-kalender*` (README).

**Produces:** vier Seiten mit je 400 bis 900 Wörtern, Gliederung je Seite: ein Satz, worum es geht; die Regel in Abschnitten; eine Checkliste („Bevor du veröffentlichst“); „Wo die Regel herkommt“ mit Links auf die Quellen (oer.community, Repos, Guides). Keine Arbeitspakete, M-Nummern, Förderer, Zwischenbericht, keine Vornamen (Rollen: Redaktion, Community-Management, Maintainer). Lizenzzeile CC BY 4.0 FOERBICO.

- [ ] **Step 1: Vier Seiten schreiben** (Entwurf, auf dem Branch; `datePublished` = Tag des Entwurfs, `creativeWorkStatus: Draft` bis zur Freigabe).
- [ ] **Step 2: Prüfen** · Run: `cd ~/repositories/FOERBICO_und_rpi-virtuell && mkdir -p /tmp/claude-501/sr && for d in Website/content/de/spielregeln-*; do cp "$d/index.md" "/tmp/claude-501/sr/$(basename "$d").md"; done && python3 -I tools/nachweis/check.py gitworkshop /tmp/claude-501/sr; python3 -I tools/nachweis/check.py erschliessung /tmp/claude-501/sr` · Expected: Namensprüfung „ohne Befund“; die gitworkshop-Prüfung meldet nur „kopf: TITEL/ZIEL fehlt“ (sie erwartet Issue-Entwürfe), keine Projektsprache-Befunde.
- [ ] **Step 3: Gate**: Jörg und die Redaktion lesen gegen (Frist 30.11.); erst dann `creativeWorkStatus: Published`, Commit auf `spielregeln-seiten`, Merge nach `main` durch Jörg; die Pipeline veröffentlicht. Danach zeigt `#oercommunity/spielregeln` „live · 4 von 4 Seiten“ ohne Codeänderung (Prüfung: `curl -s https://hub.rpi-virtuell.net/` ist unverändert, die Seite lädt die Events).

```bash
cd ~/repositories/FOERBICO_und_rpi-virtuell && git checkout -b spielregeln-seiten main && git add Website/content/de/spielregeln-*/index.md && git commit -m "Spielregeln-Seiten: Qualitätskriterien, Metadatenprofil, Redaktion, Abläufe (Entwurf für die Redaktion)"
```

### Task 8: Abschluss der Etappe (vorbereitet, Veröffentlichung nur durch Jörg)

**Files:** `~/.config/poutnik/protokolle/issue-kommentare-2026-11-24/`: `00-uebersicht.md` und vier Kommentar-Entwürfe `03-kommentar-spielregeln.md`, `04-kommentar-material-detail.md`, `10-kommentar-schaufenster-live.md`, `15-kommentar-lizenzstand.md` (Form wie Runde 5: `ZIEL:`/`ID:` in voller Länge aus den `.fertig.json`, Leerzeile, Text „Umsetzt in PR {{pr:<branch>}} (main {{main}}): <Entscheidung in einem Satz>. Ausprobieren: https://hub.rpi-virtuell.net/#<route>. Offen bleibt: <ein Satz>.“). FOERBICO-Repo: `Hub-Entwicklung/2026-11-24-etappe-3-uebergabe.md` (Branch-Stapel mit SHAs, Merge-Ablauf, Gates, Hashes nach dem Merge), Ergänzung der Abnahme-Checkliste in `Hub-Entwicklung/2026-11-16-stand-fuer-ux-gast.md` um drei Aufgaben (ein Material finden und seine Lizenz deuten; die Spielregeln finden; einen Beitrag im Schaufenster öffnen), Spec-Fahrplan dritte Zeile „Erledigt am <Datum>: …“, Kommentar auf den Nachweis-Issues (Nummern in `Orga/nachweis-hub/ergebnis.json`: Schlüssel `01-ap-3-2-3-3` für die Zeilen 4.2 und 4.15, der Schlüssel der Metadaten-Zeile für 4.3 und 4.12; Zuordnung in `docs/superpowers/plans/2026-11-03-hub-nachweis-etappe-1-buchfuehrung-backlog.md`) über `forgejo-api comment` (eigener Aufruf, nicht mit Commit kombiniert), Commit der Dateien.

- [ ] **Step 1: Entwürfe schreiben und prüfen** · Run: `python3 -I tools/nachweis/check.py gitworkshop ~/.config/poutnik/protokolle/issue-kommentare-2026-11-24` · Expected: Exit 0.
- [ ] **Step 2: Gate**: Jörg pusht die PRs (`deno task push … --as poutnik`), mergt, pusht `main`, setzt `{{pr:…}}` und `{{main}}` (Skript aus der Etappe-2-Übergabe wiederverwenden), liest die Kommentare, gibt frei.
- [ ] **Step 3: Veröffentlichen** (nach Freigabe) · Run: je Datei `zsh tools/poutnik/skripte/pub-comment.sh <datei>`; `cd tools/poutnik && deno task threads --repo reli-hub --since 1` · Expected: vier Kommentare von Poutník mit heutigem Datum.
- [ ] **Step 4: Buchführung** · Spec-Fahrplan, Forgejo-Kommentar(e), Commit und Push im FOERBICO-Repo wie am 04.11.; Prüfung `python3 -I tools/nachweis/check.py erschliessung <ordner mit den neuen Dateien>` · Expected: ohne Befund.
- [ ] **Step 5: Abnahme am 25.11.2026**: Checkliste aus Etappe 2 plus die drei neuen Aufgaben; Ergebnis in `Hub-Entwicklung/2026-11-25-abnahme-navigation.md` (Befunde ohne Personennamen); Einwände werden Issue-Kommentar oder neues Issue (Runde 6).
