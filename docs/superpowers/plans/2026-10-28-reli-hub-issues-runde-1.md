# reli-hub-Prototyp: erste Issue-Runde — Umsetzungsplan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fünf Issues der Co-Maintainerin im reli-hub-Prototyp beantworten (Farbsystem, OER-Community-Schaufenster, Teilen in Communities, Artikel im Finden, Newsletter) und die Grundentscheidungen als ADRs im reli-hub-Repo festhalten, als ein PR von Poutník.

**Architecture:** Alles passiert in `~/repositories/reli-hub` auf Branch `pr/issues-runde-1` ab `main` (`d130782`). Die einzige Produktdatei ist `index.html` (ein Dokument, zwei Inline-Skripte: Konsole als Web Component, dann die Prototyp-Anwendung). Tests sind textbasierte Deno-Tests über `index.html` (Farbkontraste rechnerisch, Struktur per Regex) plus Sichtprüfung im Browser über einen statischen Server. Ein Commit je Issue, Author Poutník.

**Tech Stack:** HTML/CSS/Vanilla-JS ohne Build; Deno 2 (`deno test`) nur für `tests/`; Browser-Sichtprüfung über `python3 -m http.server`.

**Spec:** `docs/superpowers/specs/2026-10-28-reli-hub-issues-runde-1-design.md` (im FOERBICO-Repo). Konstruktionsbeschreibung des Prototyps: `~/repositories/reli-hub/docs/konstruktion.md`.

## Global Constraints

- `index.html` bleibt allein lauffähig: keine Dateien neben ihr nötig, keine Build-Schritte, externe Ressourcen nur Google Fonts und per URL verlinkte Bilder mit `onerror`-Fallback.
- Fünf-Funktionen-Ontologie der Konsole bleibt (fünf Kreise); neue Knospen sind erlaubt.
- Jeder Text, auch kleiner, hat ≥ 4,5:1 Kontrast zu seinem Grund; Fokus ist überall sichtbar.
- Bereichsfarben der Prototyp-Anwendung (zweites Skript) kommen ausschließlich aus `:root` über `cssVar()`; die Konsole (erstes Skript) behält Fallback-Werte und liest `--relihub-c-<id>` / `--relihub-text-<id>`.
- Prototyp-Konventionen bleiben: `data-todo`, `later()`, Persona Luca Beispiel, Fuß „Teil des reli_hub“, Touch-Regel der Flip-Kacheln, `prefers-reduced-motion`.
- Commits: Author `Poutník <poutnik@users.noreply.edufeed.org>` (`git -c user.name=Poutník -c user.email=poutnik@users.noreply.edufeed.org commit`), Text nennt die Issue-Kurz-ID, Trailer `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`. Keine Arbeitspakete, Meilensteine, Förderkennzeichen oder Personenbewertungen in Commits, ADRs, README.
- Namen: Teamnamen nur im Schaufenster-View (Nachbau der öffentlichen Teamseite); sonst Rollen/Handles.
- Push nur über `cd <FOERBICO>/tools/poutnik && deno task push pr/issues-runde-1 --as poutnik --cwd ~/repositories/reli-hub`, nie `git push`. Vorher Freigabe durch Jörg.

## Review Focus

1. Bild-URLs von oer.community/Blossom nicht erreichbar (offline, 404, Blockade): das Schaufenster muss ohne Lücken rendern (Platzhalter mit Initialen/Titel), nichts darf das Layout springen lassen. Test in Task 2.
2. Beitrags-Editor ohne gewählte Community: Veröffentlichen muss weiter funktionieren (Toast ohne Teilen-Satz, nichts in `CR`). Test in Task 3.
3. Zweimal denselben Beitrag veröffentlichen: kein doppelter Eintrag im Raum-Tab „Artikel“ über denselben Titel hinaus unvermeidbar, aber keine Exception, Liste bleibt sortierbar. Test in Task 3.
4. Profil-Panel „Artikel aus deinen Communities“, wenn die Persona keiner Community folgt (leerer `cyFollow`): Leerzustandstext statt leerem Block. Test in Task 4.
5. Konsole auf einer Seite ohne `--relihub-c-*` (eigenständige Nutzung): Fallback-Farben greifen, `mix()` erhält gültige Hex-Werte. Test in Task 1.

---

## Dateistruktur

- Modify: `~/repositories/reli-hub/index.html` (alle Tasks)
- Create: `~/repositories/reli-hub/tests/index.test.ts` (Task 1, von allen folgenden erweitert), `~/repositories/reli-hub/deno.json` (Task `test`)
- Create: `~/repositories/reli-hub/docs/adr/README.md`, `docs/adr/0001-farbsystem.md` … `0005-artikel-im-finden.md` (Task 6)
- Modify: `~/repositories/reli-hub/README.md` (Task 6)
- Create (FOERBICO-Repo): `.claude/launch.json`-Eintrag `reli-hub` für die Browser-Vorschau (Task 1, nicht Teil des PR)

Testhilfen (Task 1, in `tests/index.test.ts`, von späteren Tasks konsumiert):

```ts
export const html: string;                       // Inhalt von ../index.html
export function rootVars(): Record<string,string>; // --name → #RRGGBB aus dem ersten :root-Block
export function contrast(a: string, b: string): number; // WCAG-Verhältnis zweier Hex-Farben
export function appScript(): string;              // Text des letzten <script>-Blocks (Prototyp-Anwendung)
export function consoleScript(): string;          // Text des ersten <script>-Blocks (Web Component)
```

Alle Tests laufen mit `cd ~/repositories/reli-hub && deno task test` (= `deno test --allow-read tests/`).

---

### Task 1: Farbsystem (Issue `fd31ec90…`)

**Files:**
- Create: `tests/index.test.ts`, `deno.json`
- Modify: `index.html` — `:root` Z. 10–15; Konsole `FUNCS` Z. 1103–1113 und Farbinitialisierung (`mix()` Z. 1141, SVG-`fill` Z. ~1281/1299/1384); App `C`/`T` Z. 1490–1491, `TINT`/`TINK` 1568–1569, Petals ~1496, `SHIELD` 1914, `CY` CampusCom Z. ~1920, `rtPre` ~2162, `crItem`-Fallback; CSS-Regeln `.src` 102, `.mat .th` 96, `.ev .date` 116, `.cr-date` 589, `.cr-ev small` 597, `.cy-back small` 471, `.cy-follow.on`/`.cr-fol.off` 469/566, `.cr-badge` 576, `.eyebrow i` 44, Fokus Z. 38, Nachbau-Stellen `.rd-ey`, Platzhalter `#8A8378`/`#7A808A`, `.reco .img` 165, `.rd-toggle` 247, `.rd-hero`.

**Interfaces:**
- Produces: Testhilfen (siehe Dateistruktur); `cssVar(name: string): string` im App-Skript (liest `getComputedStyle(document.documentElement).getPropertyValue(name).trim()`); `:root`-Variablen `--c-hub #203A8F`, `--c-finden #007A75`, `--c-erstellen #FFA500`, `--c-koop #D6336C`, `--c-ver #7B4FB8`, `--x-hub`, `--x-finden`, `--x-erstellen`, `--x-koop`, `--x-ver`, `--fo-blau #203A8F`, `--fo-orange #FFA500`, `--fo-titel #002366`, `--fo-text #333333`, `--fo-hell #F0F8FF`, `--fo-kopf #E6F2FF`, `--fo-rahmen #D3D3D3`, `--relihub-c-hub|finden|erstellen|kooperieren|veroeffentlichen` und `--relihub-text-…` (gesetzt aus `--c-*`/Textfarben).

- [ ] **Step 1: Testgerüst und Kontrasttest schreiben**

`deno.json`: `{ "tasks": { "test": "deno test --allow-read tests/" } }`. In `tests/index.test.ts` die Hilfen aus der Dateistruktur und:

```ts
Deno.test('Textfarben je Bereich erreichen 4,5:1 auf paper, card und Tint', () => {
  const v = rootVars();
  for (const b of ['hub','finden','erstellen','koop','ver'])
    for (const bg of [v['paper'], v['card'], v['t-' + b]])
      assert(contrast(v['x-' + b], bg) >= 4.5, `${b} auf ${bg}`);
});
Deno.test('Weiß bzw. Dunkel auf Bereichsflächen', () => {
  const v = rootVars();
  for (const b of ['hub','finden','koop','ver']) assert(contrast('#FFFFFF', v['c-' + b]) >= 4.5, b);
  assert(contrast('#2B1A00', v['c-erstellen']) >= 4.5);
  assert(contrast(v['muted'], v['paper']) >= 4.5);
});
Deno.test('Bereichsfarben nur in :root', () => {
  assert(!/#(203A8F|007A75|FFA500|D6336C|7B4FB8|233E99|008C86|F39200)\b/i.test(appScript()));
  assert(/cssVar\(/.test(appScript()));
});
Deno.test('Konsole liest Custom Properties und behält Fallback', () => {
  assert(consoleScript().includes('--relihub-c-'));
  assert(/#203A8F/i.test(consoleScript()) || /#233E99/i.test(consoleScript()));
});
Deno.test('Generische Fokusregel vorhanden', () => {
  assert(/button:focus-visible[^{]*\[tabindex\]:focus-visible[^{]*\{[^}]*outline:\s*3px/.test(html));
});
```

- [ ] **Step 2: Tests laufen lassen, Fehlschlag sehen**

Run: `cd ~/repositories/reli-hub && deno task test`
Expected: FAIL — `x-hub` undefined (Kontrasttest), `cssVar(` fehlt, `--relihub-c-` fehlt, Fokusregel fehlt.

- [ ] **Step 3: `:root` umbauen**

Neue Werte und Variablen laut Interfaces eintragen; `--x-*` so wählen, dass Step 1 grün wird (Startwerte: `--x-hub #203A8F`, `--x-finden #00605C`, `--x-erstellen #8A4C00`, `--x-koop #7A1A3E`, `--x-ver #5A3590`; `--t-erstellen` bei Bedarf auf `#FFF1D6`). `--relihub-c-*`/`--relihub-text-*` aus denselben Werten setzen (Labeltext: erstellen `#2B1A00`, sonst `#FFFFFF`).

- [ ] **Step 4: Konsole: Custom Properties lesen**

In der Web Component beim `connectedCallback` (vor `mix()`-Aufrufen und SVG-Aufbau): für jede Funktion in `FUNCS` `const cs = getComputedStyle(this); const c = cs.getPropertyValue('--relihub-c-' + f.id).trim();` — wenn gesetzt, `f.color = c`, analog `f.text`. `FUNCS`-Hex-Werte bleiben als Fallback; Reihenfolge so, dass abgeleitete Werte (`light`, Petals) nach dem Überschreiben berechnet werden.

- [ ] **Step 5: App-Skript auf `cssVar()` umstellen**

`cssVar(name)` definieren; `C`, `T`, `TINT`, `TINK`, Petals, `SHIELD`-Füllung, CampusCom-`col` in `CY`, `rtPre`, `crItem`-Fallback daraus speisen (`TINT`/`TINK` aus `--t-*`/`--x-*`). Keine der acht Hex-Werte aus Step 1 mehr im App-Skript.

- [ ] **Step 6: CSS-Textstellen und Fokus**

Die in **Files** genannten Regeln auf `var(--x-<bereich>)` umstellen; Nachbau-Stellen abdunkeln (`.rd-ey`, Platzhalter, `.reco .img`, `.rd-toggle`, relidesk-Hero-Text), ohne die Instanzpalette zu wechseln. Fokusregel neben Z. 38 einfügen: `button:focus-visible, [tabindex]:focus-visible, a:focus-visible, .btn:focus-visible { outline: 3px solid var(--ink); outline-offset: 2px }`.

- [ ] **Step 7: Tests grün**

Run: `deno task test`
Expected: PASS, 5 Tests.

- [ ] **Step 8: Sichtprüfung**

`.claude/launch.json` im FOERBICO-Repo um `{ "name": "reli-hub", "runtimeExecutable": "python3", "runtimeArgs": ["-m", "http.server", "8765", "--directory", "/Users/joerglohrer/repositories/reli-hub"], "port": 8765 }` ergänzen; Vorschau starten, Start, Profil, Communities, Materialpool, relidesk ansehen: Konsole zeigt neue Farben, Labels lesbar, Fokusringe per Tab sichtbar. Screenshot für Jörg.

- [ ] **Step 9: Commit**

```bash
cd ~/repositories/reli-hub && git add deno.json tests/index.test.ts index.html
git -c user.name=Poutník -c user.email=poutnik@users.noreply.edufeed.org commit -m "Farben: FOERBICO-Blau und -Orange, Textfarben je Bereich, alles in :root (Issue fd31ec90)" -m "<Kontrastwerte-Tabelle aus Step 1>" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 2: OER-Community als Schaufenster (Issue `74b30cd5…`)

**Files:**
- Modify: `index.html` — Font-Link Z. 8 (Roboto Condensed 400 ergänzen), neuer `<div class="view" id="v-oercommunity">` nach `#v-relidesk` (vor Z. ~1028), `nav.proto` Z. 1030, `PARTNERS` Z. 1554–1567, `CY` Z. 1915–1934, `cyFollow` Z. 1936, `EVENTS` Z. 1603, `registerContext` Z. 2200–2280, `route()` Z. 2305–2321 (View-Liste, `document.title`), CSS-Block `.oc-*`.
- Test: `tests/index.test.ts`

**Interfaces:**
- Consumes: `cssVar`, `--fo-*` (Task 1); `later()`, `go()`, `toast()`, `openBlog(ctx)`, `cyRel(c)`, `T_`.
- Produces: View-ID `oercommunity` (Hash `#oercommunity`), Kontextname `oer-community`, `CY`-Eintrag `{ id:'oercommunity', n:'OER-Community', ty:'netz', inst:['OER-Community','oercommunity'], … }`, `CR.oercommunity.act` mit fünf `T_('Artikel', …)`-Einträgen (`who:'OER-Community'`, `ago`, `x` = erster Satz, `tags`, `url`), zwei `EVENTS`-Einträge mit Quelle „OER-Community“, Konstante `OC_POSTS` (Array der fünf Beiträge: `{t, date, tags, x, img, url, lic}`), `OC_TEAM` (drei Gruppen × Personen `{n, f, img}`).

- [ ] **Step 1: Strukturtest schreiben**

```ts
Deno.test('Schaufenster OER-Community ist verdrahtet', () => {
  assert(html.includes('id="v-oercommunity"'));
  assert(/<nav class="proto"[\s\S]*?href="#oercommunity"[^>]*>FOERBICO<\/a>/.test(html));
  assert(/'OER-Community',\s*'Schaufenster des Projekts FOERBICO'/.test(appScript()));
  assert(/id:\s*'oercommunity'[\s\S]*?inst:\s*\['OER-Community',\s*'oercommunity'\]/.test(appScript()));
  assert(/registerContext\('oer-community'/.test(appScript()));
  assert(/'oercommunity'/.test(appScript().match(/function route\(\)[\s\S]*?includes\(view\)/)![0]));
  assert(/Roboto\+Condensed:wght@400/.test(html));
  assert((appScript().match(/OC_TEAM[\s\S]*?\];/)![0].match(/\bn:/g) || []).length === 10);
  assert((appScript().match(/OC_POSTS[\s\S]*?\];/)![0].match(/\bt:/g) || []).length === 5);
  assert(/onerror=/.test(html.match(/id="v-oercommunity"[\s\S]*?<\/footer>/)![0]) || /onerror=/.test(appScript()));
});
```

- [ ] **Step 2: Test fehlschlagen sehen** — Run: `deno task test` · Expected: FAIL (View fehlt).

- [ ] **Step 3: Daten anlegen** — `OC_POSTS` (fünf Beiträge vom 29.09., 28.09., 22.09., 11.09., 02.09.2026 aus `Website/content/de/posts/*/index.md` des FOERBICO-Repos: Titel, Datum, Tags, erster Satz, `cover.image`-URL, Lizenz aus `bilder`), `OC_TEAM` (zehn Personen aus `Website/content/de/unser-team/index.md`: Name, Funktion, Bilddatei → `https://oer.community/unser-team/<Datei>`), zwei Tagungen als Objekte; `CY`-Eintrag (Bio: erster Einladungsabsatz der Startseite, gekürzt); `cyFollow.add('oercommunity')` (Folgen, nicht `mine`); `CR.oercommunity = { act: OC_POSTS.map(p => T_('Artikel', p.t, { who:'OER-Community', ago:<aus Datum>, x:p.x, tags:p.tags, url:p.url })) }`; zwei `EVENTS`-Zeilen `['02','FEB','Offen. Vernetzt. Zukunft – Abschlusstagung','OER-Community · Frankfurt · 2./3. Feb. 2027']` und Zwischenfazit-Tagung (Datum aus `Website/content/de/tagungen/index.md`).

- [ ] **Step 4: View bauen** — Markup nach Spec 4.2: Kopfzeile (Wortmarke, Menü mit Ankern `#oc-tagungen`, `#oc-oer`, `#oc-qualitaet`, `#oc-team`, `#oc-blog`), Abschnitte Start, Blog (Karten mit Bild + Lizenzpille), Tagungen, OER/Qualität, Team (drei Gruppen, Porträt mit `onerror` → Initialen-Kreis in `--fo-hell`), Fuß (CC-BY-Zeile, Impressum/Datenschutz extern, Hub-Zeile „Teil des reli_hub · Datenstand 29.09.2026“), `<relihub-steuerkonsole floating context="oer-community">`. CSS-Präfix `.oc-`, Schrift Roboto Condensed, Farben nur über `--fo-*`.

- [ ] **Step 5: Verdrahten** — `nav.proto`: `<a href="#oercommunity" data-v="oercommunity">FOERBICO</a>`; `PARTNERS`-Zeile mit `href '#oercommunity'`, Bereich `hub`; `registerContext('oer-community', …)` mit `hub.home → go('start')`, `finden.material → go('materialpool?thema=OER')`, `veroeffentlichen.beitrag → openBlog('OER-Community')`, `kooperieren.communities → go('community?c=oercommunity')`, Rest `later`; `route()`: `'oercommunity'` in der View-Liste, Titel „OER-Community · FOERBICO“.

- [ ] **Step 6: Tests grün** — Run: `deno task test` · Expected: PASS.

- [ ] **Step 7: Sichtprüfung** — Vorschau `#oercommunity`: alle Abschnitte, Menü-Anker, Bilder laden (oder Platzhalter), Konsole schwebt, Partner-Kachel flippt und führt hin, Community-Kachel zeigt „↔ Instanz: OER-Community“. Netz abschalten (DevTools offline oder Bild-URL manipulieren) und prüfen, dass Platzhalter erscheinen (Review Focus 1). Screenshot.

- [ ] **Step 8: Commit** — `… commit -m "OER-Community als Schaufenster: eigener View, Eintrag in Prototyp-Leiste, Partner-Kachel, Community (Issue 74b30cd5)"` mit Trailer.

---

### Task 3: In Communities teilen (Issue `ef87ccaa…`)

**Files:**
- Modify: `index.html` — `openBlog` Z. 1866–1910 (Markup nach Hashtags, Veröffentlichen-Handler ~1904), `openEvent` Z. 1688–1759 (gleicher Abschnitt), neue Funktion `communityPicker`, `CY`/`COMM`-Semantik Z. 1600/1915–1948, `crRender` Z. 2046.
- Test: `tests/index.test.ts`

**Interfaces:**
- Consumes: `CY`, `COMM`, `cyFollow`, `CR`, `crData`, `crRender`, `T_`, `toast`, `CTX_NAME`.
- Produces: `isMember(c): boolean` (Persona ist Mitglied: Status „Mitglied“ in `COMM` bzw. entsprechendes `CY`-Feld), `communityPicker(ctx: string): { html: string, selected: () => string[] }` (rendert Abschnitt „Mit Communities teilen (optional)“ / „Communities auswählen“ mit Checkboxen aller Communities aus `cyFollow`; gesperrte Zeilen für Nicht-Mitglieder mit 🔒 „Nur Mitglieder“; Buttons „Alle auswählen“/„Alle abwählen“; Vorbelegung: Community mit `n === ctx` oder mit `inst[0] === CTX_NAME[ctx]`, nur wenn wählbar), `shareTo(ids: string[], item): void` (fügt `item` vorn in `crData(CY.find(id)).act` ein, rendert offenen Raum neu).

- [ ] **Step 1: Test schreiben**

```ts
Deno.test('Teilen in Communities im Beitrags- und Termin-Editor', () => {
  const s = appScript();
  assert(s.includes('Mit Communities teilen (optional)') && s.includes('Communities auswählen'));
  assert(s.includes('Alle auswählen') && s.includes('Alle abwählen') && s.includes('Nur Mitglieder'));
  assert((s.match(/communityPicker\(/g) || []).length >= 3);   // Definition + openBlog + openEvent
  assert(/function shareTo\(/.test(s) && /kind 16/.test(s) && /h-Tag/.test(s));
  assert(/function isMember\(/.test(s));
});
```

- [ ] **Step 2: Test fehlschlagen sehen** — Run: `deno task test` · Expected: FAIL.

- [ ] **Step 3: `isMember`, `communityPicker`, `shareTo` implementieren** — Markup im Stil der `ef-*`-Editorklassen (Liste max. 160 px hoch, Avatar-Kreis mit `c.col`, Name, Checkbox, Status „(wird geteilt)“). Mitgliedschaft aus `COMM` ableiten (Status „Mitglied“), Nicht-Mitglieder in `cyFollow` gesperrt.

- [ ] **Step 4: In `openBlog` und `openEvent` einbauen** — Abschnitt unter den Hashtags; im Veröffentlichen-Handler: `const ids = picker.selected()`; bei Beitrag `shareTo(ids, T_('Artikel', titel, { who:'Luca Beispiel', ago:'jetzt', x: zusammenfassung, tags }))`, bei Termin `shareTo(ids, T_('Termin', titel, { who:'Luca Beispiel', ago:'jetzt', d:[…], tags }))`. Toast: bisheriger Satz + „und mit einem Repost (kind 16) mit h-Tags an N Communities geteilt: A, B“ (nur wenn `ids.length`); bei Öffnung aus einem Raum zusätzlich „der Artikel selbst trägt das h-Tag von <Raum>“. Ohne Auswahl: bisheriger Toast unverändert (Review Focus 2).

- [ ] **Step 5: Tests grün** — Run: `deno task test` · Expected: PASS.

- [ ] **Step 6: Sichtprüfung** — Vorschau: Start → Konsole → veröffentlichen.beitrag: Abschnitt sichtbar, relimentar/OER-Community gesperrt, relilab/narrt wählbar; aus `#community?c=relilab` öffnen: relilab vorausgewählt; aus `#relilab`: relilab vorausgewählt; veröffentlichen mit relilab + narrt → Raum relilab, Tab Artikel zeigt den Beitrag oben; zweimal veröffentlichen → zwei Einträge, keine Konsolenfehler (Review Focus 3). Termin-Editor ebenso.

- [ ] **Step 7: Commit** — `… commit -m "Beitrag und Termin: mit Communities teilen wie in der edufeed-App (Issue ef87ccaa)"` mit Trailer.

---

### Task 4: Artikel im Finden (Issue `390d2fa0…`)

**Files:**
- Modify: `index.html` — `FUNCS` Z. 1103–1113 (finden.subs), `ROUTES` Z. 1122–1134, `EX` Z. ~1506–1512, `SUBL` Z. 1541, `#v-profil` Z. 709–770 (neues Panel nach „Neue Materialien für dich“, vor `#news`), Kontextprofile Z. 2200–2280 (`finden.beitraege` je Kontext), ggf. Erklärtext `EX.finden`.
- Test: `tests/index.test.ts`

**Interfaces:**
- Consumes: `CR`, `crData`, `crItem`, `cyFollow`, `CY`, `go`, `later`.
- Produces: Aktion `finden.beitraege` (Label „Beiträge“, Route `/finden/beitraege`), Panel `#artikel` im Profil mit Überschrift „Artikel aus deinen Communities“, Funktion `renderArtikel(): void` (sammelt `type === 'Artikel'` aus `crData(c)` für `c` in `cyFollow`, sortiert nach `ago`, rendert `crItem` mit Quelle = Community-Name; Leerzustand „Folge Communities, um hier Artikel zu sehen.“).

- [ ] **Step 1: Test schreiben**

```ts
Deno.test('finden hat die Knospe Beiträge und das Profil ein Artikel-Panel', () => {
  const c = consoleScript(), s = appScript();
  assert(/finden\.beitraege/.test(c) && /'\/finden\/beitraege'/.test(c + s));
  assert(/'finden\.beitraege':\s*'Beiträge'/.test(s));
  assert(html.includes('id="artikel"') && html.includes('Artikel aus deinen Communities'));
  assert(/function renderArtikel\(/.test(s) && s.includes('Folge Communities, um hier Artikel zu sehen.'));
});
```

- [ ] **Step 2: Test fehlschlagen sehen** — Run: `deno task test` · Expected: FAIL.

- [ ] **Step 3: Knospe anlegen** — `FUNCS[finden].subs` um `{ id:'finden.beitraege', label:'Beiträge' }` erweitern (Form wie die vorhandenen Subs), `ROUTES['finden.beitraege'] = '/finden/beitraege'`, `EX['finden.beitraege']` mit Pfad „finden › Beiträge“, Titel „Artikel und Nachrichten“, Absatz „Artikel und Nachrichten aus deinen Communities und Instanzen. Lehr- und Lerninhalte findest du im Materialpool.“, `go: 'profil'`; `SUBL['finden.beitraege'] = 'Beiträge'`; Erklärtext von `finden` ergänzen (drei Knospen nennen). Kontextprofile: `hub-*` → `go('profil')` + `scrollIntoView` auf `#artikel`; Instanz-Kontexte → `later`.

- [ ] **Step 4: Panel bauen** — Markup im Stil der Profil-Panels (`data-c="finden"`), Untertitel „aus Communities, denen du folgst; Nachrichten aus dem Netz stehen unter News“; `renderArtikel()` beim Betreten des Profils aufrufen (in `route()` bei `v === 'profil'`) und nach `shareTo` (Task 3).

- [ ] **Step 5: Tests grün** — Run: `deno task test` · Expected: PASS.

- [ ] **Step 6: Sichtprüfung** — Konsole auf Start: finden zeigt drei Knospen (Popover-Form wechselt auf Knospen, gewollt); Klick „Beiträge“ → Profil scrollt zum Panel; Panel listet Artikel aus relilab, narrt, OER-Community; in der Konsole `cyFollow.clear(); renderArtikel()` → Leerzustand (Review Focus 4). Screenshot.

- [ ] **Step 7: Commit** — `… commit -m "finden: dritte Knospe Beiträge und Profil-Panel Artikel aus deinen Communities (Issue 390d2fa0)"` mit Trailer.

---

### Task 5: Newsletter (Issue `da392383…`)

**Files:**
- Modify: `index.html` — `CY` Z. 1915–1934 (Feld `nl`), `cyCards` Z. 1941–1948, `crRender` Z. 2046–2060, relilab-Terminbereich Seitenleiste `rt-side` Z. ~937–946, CSS `.cy-nl`, `.rt-nl`.
- Test: `tests/index.test.ts`

**Interfaces:**
- Consumes: `CY`, `cyCards`, `crRender`.
- Produces: `CY[i].nl?: [name: string, rhythmus: string, url: string][]`; Funktion `nlBox(): string` (HTML-Liste aller `CY.filter(c => c.nl)` mit Fußnote „Nostr: NIP-B0-Lesezeichen (kind 39701) des Community-Schlüssels, Tag newsletter“).

- [ ] **Step 1: Test schreiben**

```ts
Deno.test('Newsletter je Community', () => {
  const s = appScript();
  assert((s.match(/\bnl:\s*\[\[/g) || []).length >= 2);          // relilab, Münchner Reli Room
  assert(/function nlBox\(/.test(s) && s.includes('Newsletter der Communities') && s.includes('39701'));
  assert(/cy-nl/.test(s) && /Newsletter:/.test(s));                 // Kachel-Pille und Raum-Kopf
});
```

- [ ] **Step 2: Test fehlschlagen sehen** — Run: `deno task test` · Expected: FAIL.

- [ ] **Step 3: Daten und Darstellung** — `nl` bei relilab (`['relilab-Newsletter','monatlich','https://relilab.org/newsletter']`) und beim Münchner Reli Room (`['Münchner Reli Room-Newsletter','4–6 Mal im Jahr', <URL aus `series`-Kontext oder relilab.org>]`); `cyCards`: Pille `<span class="cy-nl">Newsletter</span>` neben `.cy-ser`; `crRender`: Zeile „Newsletter: Name · Rhythmus · <a target=_blank>anmelden</a>“ unter `cyRel`; `nlBox()` in die relilab-Terminseitenleiste (unter den Quellen) einhängen. Verworfene Alternativen stehen nur im ADR (Task 6).

- [ ] **Step 4: Tests grün** — Run: `deno task test` · Expected: PASS.

- [ ] **Step 5: Sichtprüfung** — Communities-Übersicht: Pillen bei relilab und Münchner Reli Room; Raum relilab: Newsletter-Zeile; `#relilab?tab=termine`: Box mit zwei Einträgen und Fußnote. Screenshot.

- [ ] **Step 6: Commit** — `… commit -m "Newsletter je Community als NIP-B0-Lesezeichen: Kachel-Pille, Raum-Kopf, Liste bei den relilab-Terminen (Issue da392383)"` mit Trailer.

---

### Task 6: README und ADRs

**Files:**
- Create: `docs/adr/README.md`, `docs/adr/0001-farbsystem.md`, `0002-instanzen-als-nachbau.md`, `0003-teilen-in-communities.md`, `0004-newsletter-als-nip-b0.md`, `0005-artikel-im-finden.md`
- Modify: `README.md`
- Test: `tests/index.test.ts`

- [ ] **Step 1: Test schreiben**

```ts
Deno.test('ADRs und README-Abschnitt', async () => {
  const readme = await Deno.readTextFile(new URL('../README.md', import.meta.url));
  assert(readme.includes('## Grundentscheidungen'));
  for (const f of ['0001-farbsystem','0002-instanzen-als-nachbau','0003-teilen-in-communities','0004-newsletter-als-nip-b0','0005-artikel-im-finden']) {
    const t = await Deno.readTextFile(new URL(`../docs/adr/${f}.md`, import.meta.url));
    for (const h of ['Status', 'Kontext', 'Entscheidung', 'Folgen']) assert(t.includes(`## ${h}`), `${f}: ${h}`);
    assert(readme.includes(f));
  }
  const alle = await Promise.all(['0001-farbsystem','0002-instanzen-als-nachbau','0003-teilen-in-communities','0004-newsletter-als-nip-b0','0005-artikel-im-finden'].map(f => Deno.readTextFile(new URL(`../docs/adr/${f}.md`, import.meta.url))));
  assert(!/Arbeitspaket|Meilenstein|Förderkennzeichen|01PO23012/.test(alle.join('\n') + readme));
});
```

- [ ] **Step 2: Test fehlschlagen sehen** — Run: `deno task test` · Expected: FAIL (Dateien fehlen).

- [ ] **Step 3: ADRs schreiben** — Vorlage in `docs/adr/README.md`: Titelzeile `# ADR-000N: <Titel>`, dann `## Status` (angenommen · 28.10.2026 · Entscheidung der Maintainer · Bezug: Issue `<id>`), `## Kontext`, `## Entscheidung`, `## Folgen` (inkl. „Ersetzt durch“-Hinweis als Konvention). Inhalte je ADR aus Spec Abschnitt 6, Alternativen bei 0004 aus Spec 4.5. Sprache Deutsch, keine Vornamen außer Prototyp-Urheber.

- [ ] **Step 4: README ergänzen** — Abschnitt `## Grundentscheidungen`: zwei Sätze (ADRs als Referenzpunkt; Änderung = neues ADR, das das alte ersetzt), Liste der fünf ADRs mit Titel und Status; darunter ein Satz zu `deno task test` (textbasierte Prüfungen über `index.html`, kein Build).

- [ ] **Step 5: Tests grün** — Run: `deno task test` · Expected: PASS, alle Tests.

- [ ] **Step 6: Commit** — `… commit -m "ADRs 0001–0005 und README-Abschnitt Grundentscheidungen"` mit Trailer.

---

### Task 7: Durchsicht, PR, Kommentar-Entwürfe

- [ ] **Step 1: Namens- und Begriffsprüfung** — `cd ~/repositories/reli-hub && git log --format=%B main..HEAD | grep -i -E 'Arbeitspaket|Meilenstein|01PO23012'` → leer; `git diff main..HEAD -- docs README.md tests` nach Vornamen aus `Website/content/de/unser-team/index.md` und nach den Handles der Maintainer durchsuchen (grep mit den Namen aus der Teamseite, nicht hier aufgeführt) → nur der Prototyp-Urheber darf vorkommen.
- [ ] **Step 2: Gesamte Sichtprüfung** — alle sieben alten Views plus `#oercommunity` einmal durchklicken, Konsolenfehler in den DevTools leer; Screenshots der Startseite, des Schaufensters und des Beitrags-Editors an Jörg.
- [ ] **Step 3: Freigabe abwarten**, dann `cd <FOERBICO>/tools/poutnik && deno task push pr/issues-runde-1 --as poutnik --cwd ~/repositories/reli-hub`; gitworkshop-Link nennen.
- [ ] **Step 4: Nach Jörgs Merge** (`ngit --signer joerg pr merge`, `deno task push main --as joerg`): fünf Kommentar-Entwürfe im Gespräch zeigen (Bezug, Änderung, Commit-Link auf gitworkshop, ADR-Link, offene Frage zum Weiterdenken), nach Freigabe je `ngit --signer poutnik issue comment --repo nostr://laoc.xyz/reli-hub <id> --body "…" -d --json`. Issues bleiben offen.
