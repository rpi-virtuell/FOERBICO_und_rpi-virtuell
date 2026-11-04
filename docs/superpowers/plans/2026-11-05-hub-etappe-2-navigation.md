# Hub als Nachweis, Etappe 2: Navigation rund schleifen. Umsetzungsplan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bis 16.11.2026 sind Startseite, Steuerkonsole und Leiste des reli_hub-Prototyps aus Nutzersicht konsistent: die acht Navigations-Issues der dritten Runde (03.11.), rpi-virtuell als eigene Instanz (Runde 4, Issue 17) und das Startseiten-Narrativ (Issue 18) sind als Pull Requests in `main` des Nostr-Repos reli-hub gemergt und unter https://hub.rpi-virtuell.net ausgeliefert; darunter liegt der Querschnitt Live-Abfrage mit Schnappschuss als Rückfall (Issue 13, ADR-0006). Abnahme mit dem UX-Gast am 25.11.2026.

**Architecture:** Eine HTML-Datei ohne Build (`index.html`), drei Inline-Skripte: die Steuerkonsole (Web Component, erstes Skript), neu die Leiste (Web Component, zweites Skript) und die Anwendung mit Routing, Kontextprofilen und Daten (letztes Skript). Die Datenschicht ist eine Funktion `hubFetch` im Anwendungsskript: ein gebündelter Filtersatz je Ansicht und Relay, Antworten im Browser gehalten, Schnappschuss als Startzustand, Datenstand sichtbar in jeder Ansicht. Jedes Issue wird ein PR-Branch `pr/<name>`, nacheinander gemergt, weil alle `index.html` ändern. Die Prüfungen bleiben textbasiert (`deno task test` über `index.html`, Regex ohne DOM).

**Tech Stack:** HTML/CSS/JavaScript ohne Framework, Custom Elements mit Shadow DOM, WebSocket zu Nostr-Relays (NIP-01 `REQ`/`EOSE`, Kinds 31923, 30023, 0, 10222), Deno 2 für Tests und das Schnappschuss-Skript, ngit 3.0.4 mit den Konten `poutnik` und `joerg` (Amber), Poutník-Wrapper `tools/poutnik`, Prüfwerkzeug `tools/nachweis/check.py`.

**Spec:** `docs/superpowers/specs/2026-11-02-hub-nachweis-gesamtkonzeption-design.md` (Abschnitte 3 Rahmenbedingungen, 4.5, 4.9, 4.11, 4.17, 4.20, 7 Hub-Issues, 8 Fahrplan zweite Zeile, 9 Konsens vom 03.11., 10 dem Bauenden überlassen). Konsens: `Hub-Entwicklung/2026-11-03-gespraech-relilab-hub-konsens.md`, `Hub-Entwicklung/2026-11-03-hub-erkundung-destillat.md`. Schlüssel: `Hub-Entwicklung/communities-schluessel.md`. Issue-Texte: `~/.config/poutnik/protokolle/issue-kommentare-2026-11-03/` (Runde 3, `NN-*.md`) und `…/issue-kommentare-2026-11-04/` (Runde 4, `13-live-abfrage.md`, `17-rpi-virtuell-instanz.md`, `18-startseiten-narrativ.md`; URLs in `neue-issues-urls.json`).

**Issue-Kurz-IDs** (erste acht Hex-Zeichen der Event-ID, für ADR-Bezüge und PR-Texte; vollständige nevent-Links in den JSON-Dateien): Runde 3: 01 Kreis-Klick `13c6ac15`, 02 Beschriftungen `e51cc5c8`, 03 direkt zur Aktion `6025ec95`, 04 dieselben Begriffe `d5f27c5d`, 05 Konsole auf der Startseite `30ac335b`, 06 Leiste als Widget `9cedc8b6`, 07 Leiste konfigurierbar `f1fd8eb3`, 08 mobil `f69558c8`. Runde 4: 13 Live-Abfrage `bc8d97d8`, 17 rpi-virtuell `353e3943`, 18 Narrativ `f7a8b1a5`, 05 Fortbildungskalender `0a7ccbf8`, 06 Personen `693c69cc`, 12 Klickweg `3c730194`. Stand 04.11.2026: alle offen, noch keine Antwort des Teams.

**Folgepläne (nicht Teil dieses Plans):** Etappe 3 bis 24.11. (Spielregeln, Material-Detail, Schaufenster live), Etappe 4 bis 07.12. (Sammlung, Kataloge, Kalender über alle Quellen, Personen), Etappe 5 bis 23.12. (Rest, Erschließungs-Layer), Etappe 6 Januar.

## Global Constraints

- Launch-Stack ist der HTML-Prototyp: eine Datei `index.html`, kein Build, kein Framework, keine externen Abhängigkeiten außer Google Fonts (Spec 3). Bis zum 25.11.2026 kein Svelte, kein Stack-Wechsel.
- Relays, von denen der Hub liest: `wss://relay.edufeed.org`, `wss://relay-rpi.edufeed.org`, `wss://amb-relay.edufeed.org`. Nie `wss://groups.edufeed.org`. Je Ansicht ein `REQ` pro Relay mit allen Filtern der Ansicht; höchstens drei offene Verbindungen zugleich; Zeitgrenze 8 s; Antworten in `sessionStorage`, Wiederholung derselben Abfrage frühestens nach 60 s (Spec 3 „Relay-Last auf der Tagung“, ADR-0006 Punkt 3).
- Jede Ansicht mit Inhalten zeigt sichtbar „live“, „Stand vom <Datum>“ oder „Nachbau“; nichts wird als echt ausgegeben, was es nicht ist (ADR-0006 Punkt 2).
- Farbsystem nach ADR-0001: Bereichsfarben nur in `:root`; jede neue Farbe als Fläche (`--c-*`/`--rv`) plus Textfarbe mit mindestens 4,5:1 auf `--paper`, `--card` und dem eigenen Hellton; keine Hex-Bereichsfarbe im Anwendungsskript; Fokus sichtbar.
- Die vier Hub-Ergänzungen je Instanz bleiben (ADR-0002 Punkte 2 bis 4): Vermerk „Teil des reli_hub“, Profil-Link, schwebende Konsole, Vorauswahl-Banner; Einstiege über Leiste, Partner-Kachel, Community-Bezug.
- Touch-Regel der Konsole bleibt: erstes Antippen aktiviert, zweites löst aus. Nicht Gebautes bleibt sichtbar (`data-todo`, Toast mit späterer URL), nie als toter Link.
- Texte im reli-hub-Repo (Code, Kommentare, Docs, ADRs, Commits, PR-Beschreibungen) und auf gitworkshop (Issue-Kommentare): keine Arbeitspakete, Meilensteine, AP-/M-Nummern, Förderkennzeichen, kein Projektträger, kein Zwischenbericht. Prüfung: `deno task test` (ADRs, README, `index.html`) und `python3 -I tools/nachweis/check.py gitworkshop <entwurfsordner>` über jeden Kommentar-Ordner vor der Veröffentlichung.
- Keine Vornamen von Partnern in Dateien, Commits oder Kommentaren; Rollen („der UX-Gast“, „der Leit-Maintainer“), Handles (`laoc42`), Pubkey-Präfixe. Erlaubt: „Jörg Lohrer“, „Jens Dechow“ (Entwurfsautor).
- Keine privaten Schlüssel, `nsec`, Bunker-Links oder Tokens in Dateien oder im Gespräch; nur `npub`.
- Hub-Texte auf Deutsch in Du-Ansprache (relidesk siezt weiter). Der Name der Startseite (reli_hub oder rpi-virtuell-Hub) bleibt offen (Faden „Selbstverständnis“): neue Texte nennen den Hub nicht beim Namen; die Wortmarke „reli_hub“ bleibt nur in Kopfzeile, Fuß und Konsole.
- Commits auf PR-Branches mit Author `Poutník <poutnik@users.noreply.edufeed.org>`; Branch `pr/<name>` ab dem aktuellen `main`; Push nur über `cd ~/repositories/FOERBICO_und_rpi-virtuell/tools/poutnik && deno task push pr/<name> --as poutnik --cwd ~/repositories/reli-hub`; nie `git push origin`. Bricht der Wrapper mit Patch-Rückfall ab: nicht wiederholen, Jörg melden.
- `main` wird nur `--as joerg` gepusht (ein Amber-Tipp am Handy), danach `git push forgejo main`; der Container unter hub.rpi-virtuell.net liefert `main` aus.
- Jeder Task endet gemergt, bevor der nächste beginnt (alle ändern `index.html`); PR-Diff und Seite werden Jörg vor dem Push gezeigt (Gate). Probeläufe mit ngit nur im Test-Repo `poutnik-test`.
- Die Tests der Etappe liegen in `tests/navigation.test.ts` (neu, Task 1); bestehende Tests in `tests/index.test.ts` bleiben grün; gemeinsame Helfer in `tests/helfer.ts`.
- Rückfallreihenfolge dieser Etappe (nach Spec 8, auf die Navigation übertragen): Gerät der 16.11. in Gefahr, fällt zuerst Task 11 (Leiste konfigurierbar, Spec 4.17 Stufe B) weg, dann in Task 7 die News-Spalte (bleibt gekennzeichneter Nachbau mit Link auf rpi-virtuell.de), dann Variante (3) in Task 9 (Hinweissatz). Nicht verhandelbar: Tasks 1 bis 6, 8, 10 und der Kern von Task 7 (Instanz mit Fortbildungen live), weil Startseite, Konsole und Leiste das Ergebnis der Etappe sind.

## Review Focus

1. Relay abweisend (403 nach der IP-Sperre), offline oder langsam: Die Ansicht zeigt weiter den Schnappschuss mit „Stand vom …“, kein Dauerladen, keine Fehlermeldung über der Seite, keine Konsolen-Ausnahme (Task 1, Test `Datenschicht: Grenzen und Rückfall`).
2. Tagungs-WLAN, viele Browser hinter einer IP: Ein Seitenaufruf öffnet höchstens eine Verbindung je Relay, und dieselbe Ansicht fragt vor Ablauf von 60 s nicht erneut (Task 1, derselbe Test: `MAX_CONN = 3`, `RETRY_MS = 60000`, `sessionStorage`).
3. Speicher gesperrt (privater Modus, Datei-URL, Vorschau): Lesen und Schreiben von `localStorage`/`sessionStorage` sind in `speicher()` gekapselt und fallen stumm auf den Standard zurück; Modus, Leiste und Cache funktionieren ohne Speicher (Task 4, Test `Konsole: Tutorial- und Direktmodus`, Zusicherung „speicher() fängt Ausnahmen“).
4. Unbekannter oder fehlender Tab in `#rpi-virtuell?tab=…`: die Ansicht öffnet den Tab „material“, kein leerer Bereich (Task 7, Test `rpi-virtuell: Tabs mit Standard`).
5. Touch: Das erste Antippen eines Kreises wechselt nur die Info-Box und navigiert nicht; erst das zweite löst aus. Das neue Aktivierungs-Ereignis darf die Touch-Regel nicht aushebeln (Task 2, Test `Konsole: Aktivieren meldet sich sofort` prüft `_touchAct = true`).

---

## Merge-Ablauf (gilt für jeden Task, wird dort nur referenziert)

Vorbereitung ab aktuellem `main`:

```bash
cd ~/repositories/reli-hub && git checkout main && git -c nostr.signer=joerg fetch origin main && git log --oneline main..origin/main
```

Ist die Ausgabe leer, ist `main` unverändert. Sonst `git merge --ff-only origin/main`, den PR-Branch darauf rebasen, Tests erneut laufen lassen und erneut pushen.

PR öffnen (nach Jörgs Ja zum Diff):

```bash
cd ~/repositories/FOERBICO_und_rpi-virtuell/tools/poutnik && deno task push pr/<name> --as poutnik --cwd ~/repositories/reli-hub
```

Erwartet: Ausgabe mit der PR-Adresse auf gitworkshop; kein Patch-Rückfall. Die PR-Beschreibung nennt das Issue (Kurz-ID und gitworkshop-Link), die Entscheidung in zwei Sätzen und den Prüfbefehl.

Mergen (Jörg, Amber am Handy):

```bash
cd ~/repositories/reli-hub && git checkout pr/<name> && ngit --signer joerg pr merge --offline
cd ~/repositories/FOERBICO_und_rpi-virtuell/tools/poutnik && deno task push main --as joerg --cwd ~/repositories/reli-hub
cd ~/repositories/reli-hub && git checkout main && git push forgejo main
```

Erwartet: `main` auf gitworkshop und Forgejo zeigt den Merge-Commit; `curl -sI https://hub.rpi-virtuell.net/ | head -1` liefert `200`; die Seite im Browser zeigt die Änderung. Danach in Forgejo `Comenius-Institut/hub` nichts weiter tun.

Prüfbefehl in jedem Task: `cd ~/repositories/reli-hub && deno task test` (alle Tests grün, Zahl steigt je Task).

---

### Task 1: Datenschicht mit Schnappschuss als Rückfall (Issue 13 `bc8d97d8`, ADR-0006)

**Files (Klon `~/repositories/reli-hub`, Branch `pr/datenschicht`):**
- Modify: `index.html` (Anwendungsskript nach `const cssVar …`; `:root`-nahe CSS für `.stand`; jede Ansicht außer `#v-start` bekommt direkt unter ihrer Kopfzeile `<p class="stand" aria-live="polite"></p>`; relilab-Termine `rtOpen`/`rtBase`/`#rtStand`; die Konstante `RT_EV` wird durch `RT_RAW` zwischen Markern ersetzt)
- Create: `tools/schnappschuss.ts`, `docs/daten.md` (Datenschicht: Relays, Filter je Ansicht, Zustände, Schnappschuss erneuern, Grenzen)
- Create: `tests/helfer.ts` (die Helfer `html`, `rootVars`, `contrast`, `consoleScript`, `appScript` aus `tests/index.test.ts` ziehen hierher um; `index.test.ts` importiert sie), `tests/navigation.test.ts`
- Modify: `deno.json` (Task `schnappschuss`), `README.md` (Absatz „Daten“: Live mit Rückfall, Schnappschuss vor Vorführungen erneuern), `docs/betrieb.md` (Schnappschuss-Schritt im laufenden Betrieb)

**Interfaces:**
- Produces: `const RELAYS = ['wss://relay.edufeed.org', 'wss://relay-rpi.edufeed.org', 'wss://amb-relay.edufeed.org']`, `const TIMEOUT_MS = 8000`, `const MAX_CONN = 3`, `const RETRY_MS = 60000`.
- `function hubFetch(name, filters, opts = {}) → Promise<Event[]>`: `name` ist der Cache-Schlüssel der Ansicht (`sessionStorage` `relihub:<name>` als `{t, events}`), `filters` ein Array von NIP-01-Filtern, die als ein `REQ` je Relay gesendet werden; `opts.relays` (Teilmenge von `RELAYS`, Standard alle). Dedupliziert nach `id`, schließt bei `EOSE` aller Relays oder nach `TIMEOUT_MS`, hält eine Warteschlange, damit nie mehr als `MAX_CONN` Sockets offen sind; innerhalb von `RETRY_MS` liefert sie den Cache ohne Netz; bei Fehlern (Verbindung, `NOTICE`, `CLOSED`) löst sie mit dem bis dahin Empfangenen auf, nie ab.
- `function datenstand(viewId, zustand, info)`: `zustand ∈ 'live' | 'stand' | 'nachbau'`, schreibt `live · <info>`, `Stand vom <info>` oder `Nachbau · <info>` in `#<viewId> .stand`. Startwert je Ansicht aus `data-stand="stand:26.10.2026"` bzw. `data-stand="nachbau:Persona Luca Beispiel"` am `div.view`, beim Laden einmal angewendet.
- `function npubToHex(npub) → string` (Bech32 nach NIP-19, 64 Hex-Zeichen), `function evToTermin(ev) → {id, k, t, s, e, x, l, g, i, u, src, a, n}` (Felder wie bisher in `RT_EV`: `d`-Tag, `title`, `start`, `end`, `content`, `location`, `t`-Tags, `image`, `r`; `a` = Absendername über `RT_SRC` aus dem `pubkey`).
- Schnappschuss: `let RT_RAW = [...]` und `let RT_STAND = '26.10.2026'` zwischen den Kommentaren `/* schnappschuss:termine */` und `/* /schnappschuss:termine */`; `let RT_EV = RT_RAW.map(evToTermin)`; `tools/schnappschuss.ts` ersetzt den Block (REQ `{"kinds":[31923],"authors":[…]}` auf `relay.edufeed.org` bis EOSE, 25 s; Events auf `id, pubkey, created_at, kind, tags, content` gekürzt). Die drei Absender in `RT_SRC` bekommen ihre vollständigen npubs (relilab `npub1fpcxaz2wvjl90gjs60x37ny2pa5u4yqfx7fklz73rgfjnnfujl3sr2fxgk`, relilab-impuls `npub1lde034983zllh2nhe48lt60q6p3a6lsxn0g90uemhg0906jsnzesh5vz8y`, relilab-Termine-Bot `npub17mq54dad6ewkrnunzx5xs4t4c0edur99gz7ymhu3dam0pz034fpsxjqk3d`, Quelle `Hub-Entwicklung/communities-schluessel.md`).
- Erster Verbraucher: `rtOpen` ruft einmal je Sitzung `hubFetch('relilab-termine', [{ kinds: [31923], authors: <drei Hex>, since: <jetzt − 30 Tage> }], { relays: ['wss://relay.edufeed.org'] })`; kommen Events, ersetzt `RT_EV` sie, `datenstand('v-relilab', 'live', '<n> Termine')`, `rtRender()`; sonst bleibt `Stand vom <RT_STAND>`.
- Tasks 7 und 11 nutzen `hubFetch`, `datenstand`, `npubToHex`; Task 6 nutzt `speicher` nicht (kommt in Task 4).

- [ ] **Step 1: Helfer auslagern und Tests schreiben**

`tests/helfer.ts` exportiert die fünf Helfer unverändert; `tests/index.test.ts` importiert sie (`import { html, rootVars, contrast, consoleScript, appScript } from './helfer.ts';`). `tests/navigation.test.ts`:

```ts
import { assert } from 'jsr:@std/assert@1';
import { html, appScript, consoleScript } from './helfer.ts';
const block = (re: RegExp) => (appScript().match(re) || [''])[0];   // Ausschnitt aus dem Anwendungsskript
const hblock = (re: RegExp) => (html.match(re) || [''])[0];         // Ausschnitt aus dem HTML

Deno.test('Datenschicht: Grenzen und Rückfall', () => {
  const s = appScript();
  assert(/const RELAYS = \[[^\]]*relay\.edufeed\.org[^\]]*relay-rpi\.edufeed\.org[^\]]*amb-relay\.edufeed\.org/.test(s), 'RELAYS');
  assert(!/groups\.edufeed\.org/.test(html), 'groups.edufeed.org darf nie gelesen werden');
  assert(/TIMEOUT_MS = 8000/.test(s) && /MAX_CONN = 3/.test(s) && /RETRY_MS = 60000/.test(s), 'Grenzen');
  const hf = block(/function hubFetch\(name, filters[\s\S]*?\n  \}/);
  assert(/sessionStorage/.test(hf) && /new WebSocket\(/.test(hf) && /'EOSE'/.test(hf) && /resolve\(/.test(hf) && !/reject\(/.test(hf), 'hubFetch löst immer auf');
  assert(/function datenstand\(viewId, zustand, info\)/.test(s) && /function npubToHex\(/.test(s) && /function evToTermin\(/.test(s), 'Signaturen');
  assert((html.match(/<div class="view"/g) || []).length - 1 === (html.match(/class="stand"/g) || []).length, 'jede Ansicht außer Start hat eine Stand-Zeile');
  assert(/schnappschuss:termine \*\/[\s\S]*let RT_RAW = \[[\s\S]*let RT_STAND = '\d\d\.\d\d\.\d{4}'[\s\S]*\/schnappschuss:termine/.test(s), 'Schnappschuss-Block');
  assert(/RT_EV = RT_RAW\.map\(evToTermin\)/.test(s), 'RT_EV aus RT_RAW');
  assert(/hubFetch\('relilab-termine'/.test(block(/function rtOpen[\s\S]*?\n  \}/)), 'relilab-Termine nutzen die Datenschicht');
  assert(!/Arbeitspaket|Meilenstein|Förderkennzeichen|Projektträger|Zwischenbericht/.test(html), 'Projektsprache in index.html');
});

Deno.test('Schnappschuss-Skript und Doku vorhanden', async () => {
  const t = await Deno.readTextFile(new URL('../tools/schnappschuss.ts', import.meta.url));
  assert(/schnappschuss:termine/.test(t) && /31923/.test(t) && !/groups\.edufeed\.org/.test(t));
  const d = await Deno.readTextFile(new URL('../docs/daten.md', import.meta.url));
  assert(/hubFetch/.test(d) && /Stand vom/.test(d) && /Nachbau/.test(d));
  const dj = JSON.parse(await Deno.readTextFile(new URL('../deno.json', import.meta.url)));
  assert(dj.tasks.schnappschuss, 'deno task schnappschuss fehlt');
});
```

- [ ] **Step 2: Tests laufen lassen, Fehlschlag sehen**

Run: `cd ~/repositories/reli-hub && deno task test`
Expected: die 13 bisherigen Tests grün (Import aus `helfer.ts` funktioniert), die zwei neuen FAIL (`RELAYS` fehlt, `tools/schnappschuss.ts` fehlt).

- [ ] **Step 3: Datenschicht, Stand-Zeilen, Schnappschuss-Block und Skript schreiben** mit den Signaturen aus dem Interfaces-Block. `hubFetch`: eine Warteschlange als Array von Funktionen, `laufend` als Zähler; je Relay ein Socket, `REQ` mit zufälliger Subscription-ID und allen Filtern, `EVENT` sammeln, `EOSE` oder Timer schließt den Socket. `RT_RAW` entsteht einmalig, indem das Skript gegen den heutigen Stand läuft (Step 4). CSS: `.stand{font-size:13px;color:var(--muted);margin:0 0 12px}`; in den Instanz-Ansichten in deren Fußfarbe.

- [ ] **Step 4: Schnappschuss erzeugen und Tests laufen lassen**

Run: `cd ~/repositories/reli-hub && deno task schnappschuss && deno task test`
Expected: Skript meldet `<n> Termine, Stand <Datum>` und schreibt den Block; alle Tests grün (15).

- [ ] **Step 5: Im Browser prüfen**

Run: `cd ~/repositories/reli-hub && deno run -A jsr:@std/http/file-server . -p 8787` und `http://localhost:8787/#relilab?tab=termine` öffnen.
Expected: Netzwerk-Tab zeigt genau einen WebSocket zu `relay.edufeed.org`; `.stand` wechselt von „Stand vom …“ auf „live · <n> Termine“; mit abgeschaltetem Netz (DevTools offline) bleibt „Stand vom …“ und die Liste ist gefüllt; keine Ausnahme in der Konsole.

- [ ] **Step 6: Committen, PR, Merge** (Merge-Ablauf oben, `pr/datenschicht`)

```bash
cd ~/repositories/reli-hub && git add index.html tools/schnappschuss.ts docs/daten.md docs/betrieb.md README.md deno.json tests && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "Datenschicht: Live-Abfrage mit Schnappschuss als Rückfall, Datenstand je Ansicht (ADR-0006)"
```

### Task 2: Kreis-Klick aktualisiert die Info-Box sofort (Issue 01 `13c6ac15`)

**Files:** Modify `index.html` (Konsolen-Skript: `activate()`, Doku-Kommentar im Kopf unter „Ereignis“; Anwendungsskript: Kontext `hub-start`), `tests/navigation.test.ts`. Branch `pr/konsole-aktivieren`.

**Interfaces:**
- Produces: Ereignis `relihub-activate` (bubbles, composed, nicht cancelable) mit `detail = { action, label, context, source }`, `source ∈ 'pointer' | 'keyboard'`, ausgelöst am Ende von `activate(f, fromKbd)`, nur wenn sich `this.active` geändert hat. Kontextprofile bekommen den optionalen Haken `onActivate(detail)`, der vor dem Ereignis aufgerufen wird. `hub-start` setzt `onActivate: d => explain(d.action)`; der `handler` (Klick auf Kreis oder Knospe) bleibt. Damit erklärt die Startseite schon beim Überfahren (Mouse-Over aus Issue 04) und beim ersten Antippen (mobil); der Klick auf den Menüpunkt ändert nichts mehr, was der Kreis nicht schon getan hat.

- [ ] **Step 1: Test schreiben**

```ts
Deno.test('Konsole: Aktivieren meldet sich sofort', () => {
  const c = consoleScript(), s = appScript();
  assert(/new CustomEvent\('relihub-activate'/.test(c), 'Ereignis fehlt');
  assert(/onActivate\(/.test(c), 'Profil-Haken onActivate fehlt');
  assert(/relihub-activate/.test((c.match(/\/\*\*[\s\S]*?\*\//) || [''])[0]), 'Doku-Kommentar nennt das Ereignis nicht');
  assert(/registerContext\('hub-start',\s*\{[\s\S]*?onActivate:/.test(s), 'hub-start nutzt onActivate nicht');
  assert(/_touchAct = true/.test(c), 'Touch-Regel verloren');
});
```

- [ ] **Step 2: Fehlschlag sehen**

Run: `cd ~/repositories/reli-hub && deno task test`
Expected: FAIL „Ereignis fehlt“.

- [ ] **Step 3: `activate()` ergänzen, Doku-Kommentar ergänzen, `hub-start` umstellen.** In `activate()` nach `this.markKbd()`: `detail` bauen, `CONTEXTS[this.ctx]?.onActivate?.(detail)`, dann `dispatchEvent`.

- [ ] **Step 4: Tests laufen lassen**

Run: `deno task test` · Expected: alle grün (16).

- [ ] **Step 5: Im Browser prüfen**: Startseite, Maus über den gelben Kreis: Karte wechselt sofort auf „erstellen“; mobil (375 px) ein Tipp: Karte wechselt, kein Sprung zu einer Unterseite.

- [ ] **Step 6: Committen, PR, Merge** (`pr/konsole-aktivieren`)

```bash
git add index.html tests/navigation.test.ts && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "Konsole: Aktivieren eines Kreises meldet sich sofort (relihub-activate), Startseite erklärt beim Überfahren"
```

### Task 3: Beschriftungen klickbar, Trefferflächen mobil (Issue 02 `e51cc5c8`)

**Files:** Modify `index.html` (Konsolen-CSS `.out`, Knospen-Rendering in `activate()`), `tests/navigation.test.ts`. Branch `pr/konsole-treffer`.

**Interfaces:**
- Produces: `const HIT = 44` im Konsolen-Skript; jede Knospe (`g.bud.act[data-action]`) enthält als erstes Kind einen unsichtbaren Treffer-Kreis `el('circle', { r: HIT, fill: 'transparent' }, bud)`; die Beschriftung (`text.out`) liegt innerhalb der Knospe und ist klickbar (`.out{pointer-events:auto;cursor:pointer}`); `.lbl{pointer-events:none}` bleibt (Beschriftung im Hauptkreis, der Kreis selbst ist das Ziel).

- [ ] **Step 1: Test schreiben**

```ts
Deno.test('Konsole: ganze Knospe samt Wort ist Trefferfläche', () => {
  const c = consoleScript();
  assert(/\.out\{[^}]*pointer-events:auto[^}]*cursor:pointer/.test(c), '.out nicht klickbar');
  assert(/\.lbl\{[^}]*pointer-events:none/.test(c), '.lbl verändert');
  assert(/const HIT = 44/.test(c) && /el\('circle', \{ r: HIT, fill: 'transparent' \}, bud\)/.test(c), 'Treffer-Kreis fehlt');
});
```

- [ ] **Step 2: Fehlschlag sehen** · Run: `deno task test` · Expected: FAIL „.out nicht klickbar“.

- [ ] **Step 3: CSS und Rendering ändern.** Der Treffer-Kreis kommt vor dem sichtbaren Kreis (r 31) in die Knospe, damit er darunter liegt.

- [ ] **Step 4: Tests laufen lassen** · Expected: grün (17).

- [ ] **Step 5: Im Browser prüfen**: Klick auf das Wort „Personen“ in der aufgeklappten Konsole löst dieselbe Aktion aus wie der Pfeil; mobil 375 px: Tipp 10 px neben die Knospe trifft noch.

- [ ] **Step 6: Committen, PR, Merge** (`pr/konsole-treffer`)

```bash
git add index.html tests/navigation.test.ts && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "Konsole: Beschriftungen klickbar, größere Trefferflächen für Finger"
```

### Task 4: Menüeintrag führt direkt zur Aktion, Tutorial- und Direktmodus (Issue 03 `6025ec95`)

**Files:** Modify `index.html` (Anwendungsskript: `speicher`, `MODUS`, `setModus`, `standardAktion`, alle acht `registerContext`-Handler, `explainDefault`, `route`; Kopfzeile von `#v-start`: Link „Hilfe“; CSS `.modus`), `tests/navigation.test.ts`. Branch `pr/konsole-direkt`.

**Interfaces:**
- Produces: `function speicher(key, value)` (ein Argument liest `localStorage`, zwei schreiben; jede Ausnahme wird gefangen und ergibt `null`), `let MODUS = speicher('relihub-modus') || 'tutorial'`, `function setModus(m)` (`'tutorial' | 'direkt'`, speichert, rendert die Karte neu). Umschalter: Betreten des Profils (`LOGGED = true`) setzt `direkt`; die Karte `explainDefault()` bietet den Knopf „Verstanden, direkt loslegen“ (`data-modus="direkt"`), im Direktmodus stattdessen „Konsole wieder erklären lassen“ (`data-modus="tutorial"`). Route `#hilfe`: Startansicht, scrollt zur Karte, zeigt `explainDefault()`. Kopfzeile von `#v-start`: `<a href="#hilfe">Hilfe</a>` vor „Ökosystem“.
- `function standardAktion(d, ctx) → false`: die gemeinsame Kette aller Kontexte in dieser Reihenfolge: `kooperieren.communities → go('communities')`; `veroeffentlichen.beitrag → openBlog(ctx)`; `veroeffentlichen.termin → openEvent(ctx)`; `veroeffentlichen.lerninhalte → openChooser(ctx)`; `hub → go(LOGGED ? 'profil' : 'start')`; `VIEW_OF[d.action] → navTo(…)`; `info(d)`; `later(d)`. Jeder Kontext-Handler behält nur seine Besonderheiten und endet mit `return standardAktion(d, '<ctx>')` (`hub-community` übergibt den Community-Namen). `hub-start`: `if (MODUS === 'direkt' && d.action.includes('.')) return standardAktion(d, 'hub'); explain(d.action); …` wie bisher.
- Task 7 und 9 registrieren neue Kontexte nach diesem Muster; Task 8 ändert `veroeffentlichen.lerninhalte` in `standardAktion`.

- [ ] **Step 1: Test schreiben**

```ts
Deno.test('Konsole: Tutorial- und Direktmodus, eine Standardkette', () => {
  const s = appScript();
  assert(/function speicher\(key, value\)/.test(s) && /try\s*\{[^}]*localStorage/.test(block(/function speicher[\s\S]*?\n  \}/)), 'speicher() fängt Ausnahmen');
  assert(/'relihub-modus'/.test(s) && /function setModus\(m\)/.test(s), 'Modus');
  assert(/function standardAktion\(d, ctx\)/.test(s), 'standardAktion fehlt');
  assert((s.match(/later\(d\); return false;/g) || []).length === 1, 'later() nur in standardAktion');
  assert((s.match(/return standardAktion\(d,/g) || []).length >= 9, 'nicht alle Kontexte enden in der Standardkette');
  assert(/MODUS === 'direkt'/.test(block(/registerContext\('hub-start'[\s\S]*?\n  \}\);/)), 'hub-start kennt den Direktmodus nicht');
  assert(html.includes('href="#hilfe"') && /data-modus="direkt"/.test(s) && /data-modus="tutorial"/.test(s), 'Umschalter');
  assert(/view === 'hilfe'/.test(block(/function route\(\)[\s\S]*?window\.scrollTo/)), 'route kennt hilfe nicht');
});
```

- [ ] **Step 2: Fehlschlag sehen** · Expected: FAIL „speicher() fängt Ausnahmen“.

- [ ] **Step 3: Umsetzen.** `standardAktion` vor den `registerContext`-Aufrufen; die acht Handler kürzen; `LOGGED = true` in `route()` um `setModus('direkt')` ergänzen; `explainDefault` um den Knopf; Klick-Handler `[data-modus]` neben `[data-ex]`.

- [ ] **Step 4: Tests laufen lassen** · Expected: grün (18), auch die alten Kontext-Tests in `index.test.ts`.

- [ ] **Step 5: Im Browser prüfen**: Tutorial: Knospe „Beitrag“ auf der Startseite erklärt; nach „Verstanden“ öffnet dieselbe Knospe den Beitrags-Editor; `#hilfe` zeigt die Erklärung wieder; im privaten Fenster läuft alles ohne Speicher.

- [ ] **Step 6: Committen, PR, Merge** (`pr/konsole-direkt`)

```bash
git add index.html tests/navigation.test.ts && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "Konsole: Tutorial- und Direktmodus, Menüeintrag führt direkt zur Aktion, eine Standardkette für alle Kontexte"
```

### Task 5: Konsole mobil: Karte als Sheet, Rückweg, Treffsicherheit (Issue 08 `f69558c8`)

**Files:** Modify `index.html` (CSS `@media (max-width:640px)`: `.explain.sheet`; Anwendungsskript `hub-start`-Handler, `explain()`, `kleinerSchirm()`; Konsolen-Skript `onDown`, `nearest`), `tests/navigation.test.ts`. Branch `pr/konsole-mobil`.

**Interfaces:**
- Produces: `function kleinerSchirm() → boolean` (`matchMedia('(max-width:640px)').matches`). Auf kleinen Schirmen öffnet ein Klick in der Start-Konsole die Karte als Sheet (`exEl.classList.add('sheet')`: `position:fixed;left:0;right:0;bottom:0;max-height:60vh;overflow:auto;z-index:9500;border-radius:18px 18px 0 0`) statt zu scrollen; `explain()` hängt im Sheet den Knopf `✕` (`data-sheet-close`) an; Schließen über den Knopf oder einen Tipp außerhalb von Karte und Konsole; die Seite bleibt, wo sie war. Konsole: `const TOUCH_SLACK = 18`; `nearest(p, slack)` liefert den Kreis, dessen Rand höchstens `slack` entfernt ist, wenn genau einer in Frage kommt; `onDown` (nur Touch) nutzt `this.exclusive(p) || this.nearest(p, TOUCH_SLACK)`.

- [ ] **Step 1: Test schreiben**

```ts
Deno.test('Konsole mobil: Sheet statt Sprung, Toleranz beim Tippen', () => {
  const c = consoleScript(), s = appScript();
  assert(/@media \(max-width:640px\)\{[\s\S]*?\.explain\.sheet\{[^}]*position:fixed/.test(html), 'Sheet-Regel fehlt');
  assert(/function kleinerSchirm\(\)/.test(s) && /data-sheet-close/.test(s), 'Sheet-Logik fehlt');
  assert(/const TOUCH_SLACK = 18/.test(c) && /nearest\(p, slack\)/.test(c) && /this\.exclusive\(p\) \|\| this\.nearest\(p, TOUCH_SLACK\)/.test(c), 'Toleranz fehlt');
});
```

- [ ] **Step 2: Fehlschlag sehen** · Expected: FAIL „Sheet-Regel fehlt“.

- [ ] **Step 3: Umsetzen.** `nearest` nach `exclusive` im Konsolen-Skript; Sheet-Logik im `hub-start`-Handler (`kleinerSchirm() ? sheet : scrollIntoView`).

- [ ] **Step 4: Tests laufen lassen** · Expected: grün (19).

- [ ] **Step 5: Drei Aufgaben mobil durchspielen (375 px) und Tipps zählen**: eine Person finden, einer Community beitreten, ein Material veröffentlichen (Aufgaben aus dem Faden „Blume als Menüführung irreführend“). Zahlen und Fehlgriffe in die PR-Beschreibung; Vergleichswert vom 03.11.: Kreis plus Menüpunkt = zwei Tipps je Bereich.

- [ ] **Step 6: Committen, PR, Merge** (`pr/konsole-mobil`)

```bash
git add index.html tests/navigation.test.ts && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "Konsole mobil: Erklärkarte als Sheet ohne Seitensprung, Toleranz beim Tippen"
```

### Task 6: Leiste unten links als eigenständiges Widget (Issue 06 `9cedc8b6`)

**Files:** Modify `index.html` (neues zweites `<script>` mit `<relihub-leiste>` zwischen Konsolen- und Anwendungsskript; `<nav class="proto">` wird `<relihub-leiste id="leiste" label="Orte"></relihub-leiste>`; `.proto`-CSS wandert in die Komponente; Anwendungsskript `LEISTE`, `leisteItems()`, `route()`; Konsolen-Popover bekommt die Überschrift „Tätigkeiten“), Create `docs/leiste.md`, Modify `tests/helfer.ts` (`leisteScript()` = zweites Skript), `tests/index.test.ts` (Syntax-Test um das zweite Skript; im Test „Schaufenster OER-Community“ die Leisten-Prüfung auf `LEISTE` umstellen), `tests/navigation.test.ts`, `README.md` (Satz zu Leiste und Konsole als zwei Elemente). Branch `pr/leiste-widget`.

**Interfaces:**
- Produces: Custom Element `relihub-leiste` (Shadow DOM, eigenes CSS mit den Variablen `--relihub-leiste-bg` (Standard `#1D1D1B`), `--relihub-leiste-fg` (`#FFFFFF`)); Attribute `current` (ID des aktiven Eintrags), `label` (Beschriftung links, Standard „Orte“); API `RelihubLeiste.setItems(items)` mit `item = { id, label, short?, href, kind }`, `kind ∈ 'instanz' | 'community'`; Communities stehen nach einem Trennstrich mit Ring-Symbol; `short` wird unter 640 px gezeigt. Klick löst `relihub-leiste-select` aus (bubbles, composed, cancelable, `detail = { id, href, kind }`); ohne `preventDefault` navigiert das Element zu `href`. Globales Objekt `window.RelihubLeiste = { version: '0.1.0', setItems }`.
- Anwendung: `const LEISTE = [ { id: 'start', label: 'Start', href: '#start', kind: 'instanz' }, { id: 'materialpool', label: 'Materialpool', short: 'Pool', href: '#materialpool', kind: 'instanz' }, { id: 'relilab', … }, { id: 'relidesk', … }, { id: 'oercommunity', label: 'FOERBICO', href: '#oercommunity', kind: 'instanz' } ]` (der Eintrag „Profil“ entfällt: Profil ist Tätigkeit der Konsole, `hub.profil`, und steht in der Kopfzeile). `function leisteItems() → item[]`: `LEISTE` plus, wenn `LOGGED`, die Communities der Persona aus `COMM` mit `cid` als `{ id: 'c-<cid>', label, href: '#community?c=<cid>', kind: 'community' }`. `route()` setzt `current` (`v`, bei `community` `c-<id>`) und ruft `setItems(leisteItems())` nach Anmeldung/Abmeldung. Ein Dokument-Listener auf `relihub-leiste-select` ruft `e.preventDefault(); go(e.detail.href.slice(1))`.
- Konsole: im Kompakt-Popover eine Zeile `<span class="cap">Tätigkeiten</span>` (CSS `.cap{position:absolute;top:14px;left:0;right:0;text-align:center;font-size:12px;letter-spacing:1.5px;text-transform:uppercase;color:#5F5E5A}`), damit Leiste („Orte“) und Konsole („Tätigkeiten“) als verschiedene Dinge lesbar sind.
- `docs/leiste.md`: Zweck (Klammer um Instanzen und Communities; wechseln und doch im Ökosystem bleiben), Daten, Attribute, Ereignis, CSS-Variablen, Einbettungs-Schnipsel (Skript-Datei `relihub-leiste.js` gedacht wie bei der Konsole), Abgrenzung zur Konsole, was fehlt (Konfiguration kommt mit Task 11, Profil-Daten mit der Personen-Ansicht).
- Task 7 fügt `rpi-virtuell` in `LEISTE` ein; Task 11 filtert `leisteItems()`.

- [ ] **Step 1: Tests schreiben und alten Test anpassen**

In `tests/helfer.ts`: `export function leisteScript(): string { return scripts[1]; }`. In `index.test.ts`, Test „Beide Inline-Skripte …“: zusätzlich `new Function(leisteScript())`; Test „Schaufenster …“: die Zeile mit `<nav class="proto"` ersetzen durch `assert(/id:\s*'oercommunity',\s*label:\s*'FOERBICO'/.test(s), 'Leisten-Eintrag fehlt');`. In `navigation.test.ts`:

```ts
Deno.test('Leiste: eigenständiges Widget, klar von der Konsole unterschieden', async () => {
  const l = leisteScript(), s = appScript(), c = consoleScript();
  assert(/customElements\.define\('relihub-leiste'/.test(l) && /relihub-leiste-select/.test(l) && /setItems\(items\)/.test(l), 'Widget');
  assert(/--relihub-leiste-bg/.test(l) && /label/.test(l), 'Variablen oder Beschriftung fehlen');
  assert(html.includes('<relihub-leiste id="leiste" label="Orte"') && !/class="proto"/.test(html), 'Leiste nicht ersetzt');
  assert(/const LEISTE = \[/.test(s) && !/id: 'profil'/.test(block(/const LEISTE = \[[\s\S]*?\n  \];/)), 'LEISTE oder Profil-Eintrag');
  assert(/function leisteItems\(\)/.test(s) && /kind: 'community'/.test(s) && /relihub-leiste-select/.test(s), 'Anwendung nutzt das Widget nicht');
  assert(/Tätigkeiten/.test(c) && /\.cap\{/.test(c), 'Konsole ohne Überschrift');
  const d = await Deno.readTextFile(new URL('../docs/leiste.md', import.meta.url));
  assert(/relihub-leiste-select/.test(d) && /setItems/.test(d) && /Tätigkeiten/.test(d), 'docs/leiste.md unvollständig');
});
```

- [ ] **Step 2: Fehlschlag sehen** · Expected: FAIL „Widget“ (und „Beide Inline-Skripte“ ERROR, weil `scripts[1]` noch die Anwendung ist).

- [ ] **Step 3: Widget, Anwendung, Konsolen-Überschrift und `docs/leiste.md` schreiben.** Das Widget-Skript trägt wie die Konsole einen Doku-Kommentar im Kopf.

- [ ] **Step 4: Tests laufen lassen** · Expected: grün (20).

- [ ] **Step 5: Im Browser prüfen**: Leiste zeigt „Orte“ und fünf Einträge, der aktive ist weiß; nach `#profil` erscheinen relilab und narrt als Communities hinter dem Strich; Konsolen-Popover trägt „Tätigkeiten“; mobil 375 px bleibt die Leiste einzeilig.

- [ ] **Step 6: Committen, PR, Merge** (`pr/leiste-widget`)

```bash
git add index.html docs/leiste.md README.md tests && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "Leiste unten links als eigenständiges Widget relihub-leiste, Orte gegen Tätigkeiten"
```

### Task 7: rpi-virtuell als eigene Instanz in der Leiste (Issue 17 `353e3943`)

**Files:** Modify `index.html` (`:root`: `--rv`, `--rv-x`, `--rv-soft`; CSS-Block „Ansicht 9: rpi-virtuell“; neue Ansicht `<div class="view" id="v-rpi-virtuell" data-stand="nachbau:Termine und News laden">`; Anwendungsskript: `rvOpen(qs)`, `rvRender()`, Kontext `rpi-virtuell`, `CTX_NAME`, `VIEW_OF`, `EX['finden.fortbildungen']`, `PARTNERS`, `LEISTE`, `CY`, `route()`), `tests/navigation.test.ts`, `docs/daten.md` (Filter der Ansicht). Branch `pr/rpi-virtuell-instanz`.

**Interfaces:**
- Consumes: `hubFetch`, `datenstand`, `npubToHex`, `evToTermin` (Task 1); `standardAktion` (Task 4); `LEISTE` (Task 6).
- Produces: Route `rpi-virtuell` mit `?tab=material|fortbildungen|news`, Standard `material` (auch bei unbekanntem Wert); `function rvOpen(qs)` (Tab setzen, einmal je Sitzung laden), `function rvRender(termine, news)`. Ansicht in rpi-virtuell-Gestalt: Wortbildmarke „rpi-virtuell“ als Text in `--rv` (kein Logo-Bild: die Bildrechte sind nicht geklärt, ADR-0002 Punkt 3), Leitfarbe `--rv` und Textfarbe `--rv-x` aus dem Stylesheet von rpi-virtuell.de übernommen (die Textfarbe so weit abgedunkelt, dass sie 4,5:1 auf `--paper` und `--card` erreicht), Hellton `--rv-soft`; Schrift: die Schrift von rpi-virtuell.de, wenn sie bei Google Fonts liegt, sonst Inter. Kopfzeile mit den drei Tabs; Vermerk „Teil des reli_hub“, Profil-Link, schwebende Konsole `context="rpi-virtuell"`, Vorauswahl-Banner (vier Hub-Ergänzungen).
- Inhalt der Tabs: **Material**: Einstieg in den Materialpool (Karte mit Link `#materialpool`, Satz „Der Materialpool ist der Katalog von rpi-virtuell“), ohne eigene Liste. **Fortbildungen**: die globale Sicht, alle Absender: Liste der nächsten 40 Termine ab heute (Datum, Titel, Absender, Ort, Link auf `u`), Zeile darüber: „Fortbildung der Institute: mit Anmeldung, in klarer Verantwortung, mit Teilnahmebescheinigung. Zum Ausprobieren ohne Anmeldung: das relilab.“ mit Link `#relilab`. **News**: die zehn neuesten Beiträge (Titel, Datum, Zusammenfassung, Link) der News-Redaktion rpi-virtuell (`npub12jguyxp6sdanpafe3mjelezm7dtlzuxqwc4qczdkr260azqqsstq05rr6j`, Schlüsselliste Abschnitt 4; Absendername im Code, weil der Schlüssel kein Profil hat).
- Daten: ein Aufruf `hubFetch('rpi-virtuell', [{ kinds: [31923], since: <jetzt − 180 Tage>, limit: 300 }, { kinds: [30023], authors: [npubToHex('npub12jguy…')], limit: 10 }], { relays: ['wss://relay.edufeed.org', 'wss://relay-rpi.edufeed.org'] })`; Termine clientseitig auf `start ≥ jetzt` gefiltert und sortiert. Vor der Antwort: `Nachbau · Termine und News laden`; danach `live · <n> Termine · <m> News`; ohne Antwort: `Nachbau · Relay nicht erreichbar` und die Tabs zeigen den Satz „Gerade keine Verbindung zu den Relays; die Termine stehen auch unter rpi-virtuell.de“ mit Link.
- Kontext `rpi-virtuell` (nach dem Muster aus Task 4): `finden.fortbildungen → go('rpi-virtuell?tab=fortbildungen')` (ist man schon dort: Toast „Du bist bereits bei den Fortbildungen.“), `finden.material → go('materialpool')`, `erstellen.labor → go('relilab')`, Rest `standardAktion(d, 'rpi-virtuell')`; `CTX_NAME['rpi-virtuell'] = 'rpi-virtuell'`.
- Verdrahtung: `VIEW_OF['finden.fortbildungen'] = 'rpi-virtuell?tab=fortbildungen'` (der relilab-Kontext behält seine eigene Terminseite); `EX['finden.fortbildungen'].go = ['Zum Fortbildungskalender', '#rpi-virtuell?tab=fortbildungen']`; in `PARTNERS` ersetzt `['rpi-virtuell', 'Materialpool, Fortbildungen, News', 'finden', 'rv', '#rpi-virtuell', 'Die Angebote der religionspädagogischen Institute an einem Ort: Materialpool, Fortbildungskalender und Bildungsnews. Fortbildung mit Anmeldung und Bescheinigung; zum Ausprobieren gibt es das relilab.']` die Kachel „rpi-virtuell Fortbildungskalender“ (`'FK', null`); `LEISTE` bekommt `{ id: 'rpi-virtuell', label: 'rpi-virtuell', short: 'rpi', href: '#rpi-virtuell', kind: 'instanz' }` zwischen `relilab` und `relidesk`; `CY` bekommt die Community rpi-virtuell (`id: 'rpi-virtuell'`, `inst: ['rpi-virtuell', 'rpi-virtuell']`, 35 Mitglieder, Beschreibung: Redaktionskreis und Institute hinter den rezeptiven Angeboten; Schlüsselliste Abschnitt 2); `route()` kennt `rpi-virtuell` und ruft `rvOpen(qs)`; `document.title` „rpi-virtuell · Teil des reli_hub“.

- [ ] **Step 1: Tests schreiben**

```ts
Deno.test('rpi-virtuell: eigene Instanz in Leiste, Kachel, Konsole und Community', () => {
  const s = appScript(), v = rootVars();
  const view = hblock(/<div class="view" id="v-rpi-virtuell"[\s\S]*?<\/div>\s*\n<!--/);
  assert(view && /data-stand="nachbau:/.test(view), 'Ansicht fehlt');
  assert(v['rv'] && v['rv-x'] && contrast(v['rv-x'], v['paper']) >= 4.5 && contrast(v['rv-x'], v['card']) >= 4.5, 'rpi-virtuell-Textfarbe unter 4,5:1');
  assert(/'rpi-virtuell'/.test(block(/function route\(\)[\s\S]*?includes\(view\)/)) && /function rvOpen\(qs\)/.test(s), 'Route');
  assert(/registerContext\('rpi-virtuell'/.test(s) && /'rpi-virtuell': 'rpi-virtuell'/.test(s), 'Kontext');
  assert(/id: 'rpi-virtuell', label: 'rpi-virtuell'/.test(block(/const LEISTE = \[[\s\S]*?\n  \];/)), 'Leisten-Eintrag');
  assert(/\['rpi-virtuell', 'Materialpool, Fortbildungen, News', 'finden', 'rv', '#rpi-virtuell'/.test(s) && !/'FK', null/.test(s), 'Partner-Kachel');
  assert(/id: 'rpi-virtuell'[^}]*inst: \['rpi-virtuell', 'rpi-virtuell'\]/.test(block(/const CY = \[[\s\S]*?\n  \];/)), 'Community-Bezug');
  assert(/'finden\.fortbildungen': 'rpi-virtuell\?tab=fortbildungen'/.test(s) && /'#rpi-virtuell\?tab=fortbildungen'/.test(s), 'Fortbildungen haben ein Ziel');
  const rv = block(/function rvOpen[\s\S]*?hubFetch\('rpi-virtuell'[\s\S]*?\]\s*\)/);
  assert(/kinds: \[31923\]/.test(rv) && /kinds: \[30023\]/.test(rv) && /npubToHex\('npub12jguy/.test(rv) && !/amb-relay/.test(rv), 'Filter der Ansicht');
  assert(/mit Teilnahmebescheinigung/.test(view) && /href="#relilab"/.test(view), 'Institutslogik und Verweis auf das relilab');
});

Deno.test('rpi-virtuell: Tabs mit Standard', () => {
  const rv = block(/function rvOpen\(qs\)[\s\S]*?\n  \}/);
  assert(/\['material', 'fortbildungen', 'news'\]\.includes\(/.test(rv) && /: 'material'/.test(rv), 'unbekannter Tab fällt nicht auf material zurück');
});
```

- [ ] **Step 2: Fehlschlag sehen** · Expected: zwei FAIL („Ansicht fehlt“, „unbekannter Tab …“).

- [ ] **Step 3: Farben von rpi-virtuell.de ablesen** (Stylesheet der Startseite; Leitfarbe und Hellton notieren, Textfarbe abdunkeln bis `deno task test` den Kontrast bestätigt), dann Ansicht, Skript und Verdrahtung schreiben. `docs/daten.md` um die Filter der Ansicht ergänzen.

- [ ] **Step 4: Tests laufen lassen** · Expected: grün (22).

- [ ] **Step 5: Im Browser prüfen**: Leiste zeigt rpi-virtuell zwischen relilab und relidesk; `#rpi-virtuell?tab=fortbildungen` listet Termine mehrerer Absender, Stand-Zeile „live · …“; Konsole › finden › Fortbildungen führt von jeder Unterseite außer relilab hierher; `#rpi-virtuell?tab=xyz` öffnet Material; Netzwerk: ein WebSocket je Relay (zwei).

- [ ] **Step 6: Committen, PR, Merge** (`pr/rpi-virtuell-instanz`)

```bash
git add index.html docs/daten.md tests/navigation.test.ts && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "rpi-virtuell als eigene Instanz: Materialpool, Fortbildungen über alle Absender, News; Leiste, Kachel, Kontext, Community-Bezug"
```

### Task 8: Startseite, Konsole und Leiste: dieselben Begriffe, Farben, Ziele (Issue 04 `d5f27c5d`)

**Files:** Create `docs/navigation.md`; Modify `index.html` (Konsolen-Skript: Knospen-Beschriftung in Bereichs-Textfarbe, CSS `.out`; Anwendungsskript: `standardAktion` für `veroeffentlichen.lerninhalte`), `tests/navigation.test.ts`, `README.md` (Verweis auf `docs/navigation.md`). Branch `pr/navigation-begriffe`.

**Interfaces:**
- Consumes: `standardAktion` (Task 4), Ziel für Fortbildungen (Task 7).
- Produces: `docs/navigation.md` mit der Tabelle `| Begriff | Startseite | Konsole (Aktion) | Ziel (Route) | Leiste (Instanz) | Farbe | Stand |` und je einer Zeile für Material, Fortbildungen, Beiträge, Schreibtisch, Labor, Communities, Personen, Lerninhalte, Termin, Beitrag, Profil, Start, Hilfe; „Stand“ nennt „gebaut“ oder das Issue, mit dem es kommt (Personen: Issue 06 der Runde 4, Kurz-ID `693c69cc`). Die Tabelle ist die Referenz, an der die Ansichten der nächsten Etappen ihre Begriffe ausrichten (Kommentar vom 04.11. im Issue).
- Knospen-Beschriftung in der Bereichs-Textfarbe: `this.text(bud, s.label, …, f.ink, 'out')`; die CSS-Regel `.out` verliert `fill:` (das Attribut gilt), behält Halo, Gewicht und `paint-order`. So tragen die Menüpunkte der Konsole dieselbe Farbe wie die Bereiche auf der Startseite (Erklärkarte, Kacheln).
- „Lerninhalte“ führt dorthin, wo der Eintrag entsteht: in `standardAktion` wird `veroeffentlichen.lerninhalte → go('materialpool'); openChooser('materialpool')` (statt `openChooser(ctx)`); der Editor liegt dann über dem Materialpool. Das Ziel „Personen“ bleibt `data-todo` mit Toast bis zur Personen-Ansicht; alle anderen `EX`-Ziele sind gesetzt.

- [ ] **Step 1: Test schreiben**

```ts
Deno.test('Navigation: Tabelle, Farben in der Konsole, Lerninhalte in den Materialpool', async () => {
  const c = consoleScript(), s = appScript();
  const d = await Deno.readTextFile(new URL('../docs/navigation.md', import.meta.url));
  assert(/\| Begriff \| Startseite \| Konsole \(Aktion\) \| Ziel \(Route\) \| Leiste \(Instanz\) \| Farbe \| Stand \|/.test(d), 'Tabellenkopf');
  for (const b of ['Material', 'Fortbildungen', 'Beiträge', 'Schreibtisch', 'Labor', 'Communities', 'Personen', 'Lerninhalte', 'Termin', 'Beitrag', 'Profil', 'Start', 'Hilfe']) assert(new RegExp(`\\| ${b} \\|`).test(d), `Zeile ${b} fehlt`);
  assert(/this\.text\(bud, s\.label[^;]*f\.ink, 'out'\)/.test(c) && !/\.out\{[^}]*fill:/.test(c), 'Knospen nicht in Bereichsfarbe');
  assert(/veroeffentlichen\.lerninhalte'\) \{ go\('materialpool'\); openChooser\('materialpool'\)/.test(block(/function standardAktion[\s\S]*?\n  \}/)), 'Lerninhalte springen nicht in den Materialpool');
  const nullZiele = [...block(/const EX = \{[\s\S]*?\n  \};/).matchAll(/go:\['[^']*',null\]/g)].length;
  assert(nullZiele === 1, `offene Ziele in EX: ${nullZiele}, erlaubt ist nur Personen`);
});
```

- [ ] **Step 2: Fehlschlag sehen** · Expected: FAIL „Tabellenkopf“.

- [ ] **Step 3: Tabelle schreiben, Konsole und Standardkette ändern.**

- [ ] **Step 4: Tests laufen lassen** · Expected: grün (23); der Kontrast-Test in `index.test.ts` bleibt grün, weil `f.ink` die geprüfte Textfarbe ist.

- [ ] **Step 5: Im Browser prüfen**: Knospen-Wörter in Türkis, Orange-Dunkel, Pink-Dunkel, Violett; Konsole › veröffentlichen › Lerninhalte aus dem relilab öffnet den Materialpool mit dem Editor darüber.

- [ ] **Step 6: Committen, PR, Merge** (`pr/navigation-begriffe`)

```bash
git add docs/navigation.md index.html README.md tests/navigation.test.ts && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "Navigation: Tabelle Startseite × Konsole × Leiste, Knospen in Bereichsfarbe, Lerninhalte führen in den Materialpool"
```

### Task 9: Konsole auf der Startseite verankern (Issue 05 `30ac335b`)

**Files:** Modify `index.html` (`#v-start`: `<relihub-steuerkonsole id="startFloat" floating size="58" popover-size="210" context="hub-start-float" hidden>` vor dem Fuß; Anwendungsskript: `IntersectionObserver` auf `#startFlower`, Kontext `hub-start-float`, `explainDefault`), `tests/navigation.test.ts`. Branch `pr/konsole-startseite`.

**Interfaces:**
- Consumes: `MODUS`, `standardAktion`, `kleinerSchirm` (Tasks 4, 5).
- Produces: Variante (1) und (3) aus dem Issue. Die schwebende Konsole erscheint auf der Startseite genau dann, wenn die große Konsole aus dem Bild gescrollt ist (`new IntersectionObserver(…).observe(document.getElementById('startFlower'))`, `hidden` wird umgeschaltet; fehlt der Observer im Browser, bleibt sie sichtbar), an derselben Stelle wie auf allen Unterseiten. Kontext `hub-start-float`: im Tutorial-Modus `explain(d.action)` und Karte zeigen (Sheet auf kleinen Schirmen, sonst `scrollIntoView`), im Direktmodus `standardAktion(d, 'hub')`. `explainDefault()` bekommt den Satz „Diesen Knopf findest du auf jeder Seite unten rechts.“ Variante (2), die Dynamik zwischen Ecke und Blume, ist Stufe B (Spec 4.20) und nicht Teil dieser Etappe; der PR-Text sagt das.

- [ ] **Step 1: Test schreiben**

```ts
Deno.test('Konsole auf der Startseite verankert', () => {
  const s = appScript(), start = hblock(/id="v-start"[\s\S]*?<!-- =+ Ansicht 2/);
  assert(/<relihub-steuerkonsole id="startFloat" floating[^>]*context="hub-start-float"/.test(start), 'schwebende Konsole fehlt auf der Startseite');
  assert(/new IntersectionObserver\(/.test(s) && /\.observe\(document\.getElementById\('startFlower'\)\)/.test(s), 'Observer fehlt');
  assert(/registerContext\('hub-start-float'/.test(s) && /MODUS === 'direkt'/.test(block(/registerContext\('hub-start-float'[\s\S]*?\n  \}\);/)), 'Kontext fehlt');
  assert(/unten rechts/.test(block(/function explainDefault[\s\S]*?\n  \}/)), 'Hinweissatz fehlt');
});
```

- [ ] **Step 2: Fehlschlag sehen** · Expected: FAIL „schwebende Konsole fehlt“.

- [ ] **Step 3: Umsetzen.**

- [ ] **Step 4: Tests laufen lassen** · Expected: grün (24).

- [ ] **Step 5: Im Browser prüfen**: Startseite scrollen bis die große Blume verschwindet, unten rechts erscheint die kleine; Klick darauf im Tutorial erklärt, nach „Verstanden“ führt „Communities“ direkt zu `#communities`.

- [ ] **Step 6: Committen, PR, Merge** (`pr/konsole-startseite`)

```bash
git add index.html tests/navigation.test.ts && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "Konsole auf der Startseite verankert: schwebende Konsole folgt der großen, Hinweis in der Erklärkarte"
```

### Task 10: Startseiten-Narrativ: Institut und Mitmachmöglichkeit, Offenheit als Struktur (Issue 18 `f7a8b1a5`)

**Files:** Modify `index.html` (`#v-start`: `h1`, `.eyebrow`, `brand small`, neuer Abschnitt `<section class="narrativ">` zwischen `.stage` und `.partners`; CSS `.narrativ`, `.einladung`), `tests/navigation.test.ts`. Branch `pr/startseite-narrativ`.

**Interfaces:**
- Produces: drei Absätze und eine Einladung statt des Slogans. Verbindlich ist die Struktur, der Wortlaut ist Vorschlag und wird von Jörg gegengelesen (Spec 10: Wortlaut der Hub-Texte bleibt den Bauenden überlassen; Jörg entscheidet, bevor der PR geht). Der Satz „Startplatz in die digitale Welt der Religionspädagogik“ und das `<small>Startplatz Religionspädagogik</small>` verschwinden; `small` wird „offen · vernetzt · digital“, die Eyebrow-Zeile entfällt. Der Hub wird im Text nicht beim Namen genannt (Name offen).
- Vorschlag: `h1`: „Religionspädagogik, offen geteilt“. Absatz 1 (Institut und Mitmachen): „Hinter diesem Ort stehen Institute, die Fortbildung und Material verantworten. Und er ist eine Einladung: Wer Religion unterrichtet oder vermittelt, kann hier mitmachen, nicht nur abholen.“ Absatz 2 (Offenheit als Struktur, OER als Weg): „Offene Praktiken sind hier nicht ein Thema unter vielen, sondern das, was alles ordnet: Material wird weitergegeben, weiterbearbeitet und zurückgespielt. Was offen lizenziert ist, lässt sich auf den Schreibtisch holen und in der Community weiterentwickeln; geschütztes Material darf dazu, bleibt aber beim Ansehen. Die offene Lizenz ist der Weg, nicht die Eintrittskarte.“ Absatz 3 (Einladung): „Zeig dich mit deinem Profil. Teile, was du hast: ein Material, einen Beitrag, einen Termin. Lade andere ein, daran weiterzuarbeiten.“ Darunter `<p class="einladung">` mit drei Links: „Profil anlegen“ (`#profil`), „Etwas teilen“ (`data-open="lerninhalt"`), „Zu einem Termin einladen“ (`data-open="termin"`).
- Der Absatz „reli_hub ist keine weitere Plattform …“ im Ökosystem-Abschnitt bleibt.

- [ ] **Step 1: Test schreiben**

```ts
Deno.test('Startseite erzählt die Haltung', () => {
  const start = hblock(/id="v-start"[\s\S]*?<!-- =+ Ansicht 2/);
  assert(!/Startplatz/.test(html), 'Slogan noch da');
  const n = (start.match(/<section class="narrativ">[\s\S]*?<\/section>/) || [''])[0];
  assert(n && (n.match(/<p>/g) || []).length >= 3, 'drei Absätze fehlen');
  assert(/class="einladung"[\s\S]*href="#profil"[\s\S]*data-open="lerninhalt"[\s\S]*data-open="termin"/.test(n), 'Einladung mit drei Wegen fehlt');
  assert(/<small>offen · vernetzt · digital<\/small>/.test(start) && !/class="eyebrow"/.test(start), 'Marke und Eyebrow');
  assert(/offen lizenziert/.test(n) && /Institute/.test(n) && /mitmachen/.test(n), 'Kernaussagen fehlen');
});
```

- [ ] **Step 2: Fehlschlag sehen** · Expected: FAIL „Slogan noch da“.

- [ ] **Step 3: Text an Jörg zur Durchsicht** (Gate; Wortlaut kann sich ändern, die Prüfungen bleiben), dann Abschnitt und CSS schreiben (`.narrativ{max-width:760px;margin:0 auto;padding:32px 24px}`, Absätze 19 px, `.einladung a` als `btn btn-ghost` in `--c-hub`). `data-open="lerninhalt"` ist in der vorhandenen `[data-open]`-Weiche der Fall „sonst“ (`openChooser('hub')`).

- [ ] **Step 4: Tests laufen lassen** · Expected: grün (25).

- [ ] **Step 5: Prüfung der Hub-Sprache**: `cd ~/repositories/reli-hub && grep -n "Projektträger\|Arbeitspaket\|Meilenstein\|Zwischenbericht" index.html` · Expected: keine Treffer.

- [ ] **Step 6: Committen, PR, Merge** (`pr/startseite-narrativ`)

```bash
git add index.html tests/navigation.test.ts && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "Startseite: Narrativ statt Slogan, Institut und Mitmachmöglichkeit, Offenheit als Struktur, Einladung"
```

### Task 11: Leiste konfigurierbar pro Community und pro Person (Issue 07 `f1fd8eb3`)

**Files:** Modify `index.html` (Leisten-Skript: Knopf `⋯` mit `data-cfg`, Ereignis `relihub-leiste-config`; Anwendungsskript: `LEISTE_KONTEXT`, `leisteItems()`, Panel `#leisteCfg`; CSS `.leiste-cfg`), `docs/leiste.md` (Abschnitt Konfiguration), `tests/navigation.test.ts`. Branch `pr/leiste-konfigurierbar`.

**Interfaces:**
- Consumes: `LEISTE`, `leisteItems()`, Widget-API (Task 6); `speicher` (Task 4).
- Produces: zwei Ebenen. (1) Community: `const LEISTE_KONTEXT = { relilab: { aus: ['relidesk', 'oercommunity'] } }` (Beispiel aus dem Issue; andere Instanzen ohne Eintrag zeigen alles); `leisteItems()` blendet auf der Instanz `v` die Einträge aus `LEISTE_KONTEXT[v].aus` aus. (2) Person: `speicher('relihub-leiste-aus')` hält als JSON die IDs, die die Person abgewählt hat; das Widget rendert am Ende den Knopf `⋯` (`aria-label="Leiste anpassen"`), der `relihub-leiste-config` auslöst; die Anwendung öffnet das Panel `#leisteCfg` (ein Kästchen je Instanz aus `LEISTE`, Communities nicht abwählbar, Knopf „Fertig“), speichert und ruft `setItems(leisteItems())`. Vorauswahl beim Start: alle Instanzen. Reihenfolge per Drag-and-drop und die Aufnahmeregel für neue Instanzen bleiben offen (Faden „Anordnung“); das Panel sagt „Reihenfolge ändern folgt“.

- [ ] **Step 1: Test schreiben**

```ts
Deno.test('Leiste konfigurierbar: pro Community und pro Person', async () => {
  const l = leisteScript(), s = appScript();
  assert(/data-cfg/.test(l) && /relihub-leiste-config/.test(l) && /Leiste anpassen/.test(l), 'Knopf oder Ereignis fehlt');
  assert(/const LEISTE_KONTEXT = \{[\s\S]*relilab: \{ aus: \['relidesk', 'oercommunity'\] \}/.test(s), 'Community-Konfiguration');
  assert(/speicher\('relihub-leiste-aus'/.test(s) && /LEISTE_KONTEXT\[/.test(block(/function leisteItems\(\)[\s\S]*?\n  \}/)), 'leisteItems filtert nicht');
  assert(html.includes('id="leisteCfg"') && /Reihenfolge ändern folgt/.test(html), 'Panel');
  const d = await Deno.readTextFile(new URL('../docs/leiste.md', import.meta.url));
  assert(/relihub-leiste-config/.test(d) && /LEISTE_KONTEXT|pro Community/.test(d), 'Doku');
});
```

- [ ] **Step 2: Fehlschlag sehen** · Expected: FAIL „Knopf oder Ereignis fehlt“.

- [ ] **Step 3: Umsetzen.**

- [ ] **Step 4: Tests laufen lassen** · Expected: grün (26).

- [ ] **Step 5: Im Browser prüfen**: im relilab fehlen relidesk und FOERBICO in der Leiste; `⋯` öffnet das Panel, Materialpool abwählen, nach Neuladen bleibt er weg; im privaten Fenster bleibt alles sichtbar.

- [ ] **Step 6: Committen, PR, Merge** (`pr/leiste-konfigurierbar`)

```bash
git add index.html docs/leiste.md tests/navigation.test.ts && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "Leiste konfigurierbar: Einträge je Instanz und je Person, Panel zum Anpassen"
```

### Task 12: Abschluss der Etappe: Schnappschuss, Issue-Kommentare, Stand an den UX-Gast, Buchführung

**Files:**
- reli-hub: `index.html` (Schnappschuss erneuert, Branch `pr/schnappschuss-2026-11-16`), `README.md` (Ansichten-Liste um rpi-virtuell, Hinweis auf `docs/navigation.md`, `docs/leiste.md`, `docs/daten.md`)
- `~/.config/poutnik/protokolle/issue-kommentare-2026-11-16/`: `00-uebersicht.md`, je Issue ein Kommentar-Entwurf `NN-kommentar-<slug>.md` (`ZIEL:`/`ID:` + Leerzeile + Text; Event-IDs sind die Kurz-IDs oben in voller Länge aus den JSON-Antworten der Runden 3 und 4), elf Dateien: die acht Runde-3-Issues, 13, 17, 18
- FOERBICO-Repo: `Hub-Entwicklung/2026-11-16-stand-fuer-ux-gast.md` (Entwurf der Nachricht, die Jörg sendet, plus Abnahme-Checkliste für den 25.11.); `docs/superpowers/specs/2026-11-02-hub-nachweis-gesamtkonzeption-design.md` (Fahrplanzeile „bis 16.11.2026“ um „Erledigt am <Datum>: PRs …, main <hash>“ ergänzen); Kommentar auf dem Nachweis-Issue zu Zeile 4.1/4.2/4.15/4.18 (Nummer in `Orga/nachweis-hub/ergebnis.json` unter `01-ap-3-2-3-3`) mit den gemergten PRs und der Adresse

**Interfaces:**
- Consumes: alle Tasks gemergt; `tools/poutnik/skripte/pub-comment.sh`; `python3 -I tools/nachweis/check.py gitworkshop <ordner>`.
- Produces: Kommentartext je Issue: „Umgesetzt in PR <gitworkshop-Link> (main <hash>): <Entscheidung in einem Satz>. Ausprobieren: https://hub.rpi-virtuell.net/#<route>. Offen bleibt: <ein Satz oder „nichts“>.“ Die Issues bleiben offen bis zum Folgetermin am 25.11.2026, damit das Team einwenden kann (Spec 3: zuerst umsetzen, dann im Issue zur Diskussion stellen). Die Nachricht an den UX-Gast: Link, je Runde-3-Punkt ein Satz, die drei Aufgaben zum Durchspielen (Person finden, Community beitreten, Material veröffentlichen), Bitte um Rückmeldung bis 25.11. Die Abnahme-Checkliste: dieselben drei Aufgaben auf Desktop und 375 px, Tipps gezählt, Vergleich mit dem 03.11.

- [ ] **Step 1: Schnappschuss erneuern und als PR mergen**

Run: `cd ~/repositories/reli-hub && git checkout -b pr/schnappschuss-2026-11-16 main && deno task schnappschuss && deno task test`
Expected: neuer `RT_STAND`, Tests grün; dann Commit („Schnappschuss der relilab-Termine vom <Datum>“), Merge-Ablauf.

- [ ] **Step 2: Kommentar-Entwürfe schreiben und prüfen**

Run: `cd ~/repositories/FOERBICO_und_rpi-virtuell && python3 -I tools/nachweis/check.py gitworkshop ~/.config/poutnik/protokolle/issue-kommentare-2026-11-16`
Expected: Exit 0.

- [ ] **Step 3: Jörg liest Kommentare und die Nachricht an den UX-Gast** (Gate).

- [ ] **Step 4: Veröffentlichen**

Run: je Datei `zsh tools/poutnik/skripte/pub-comment.sh <datei>`; danach `cd tools/poutnik && deno task threads --repo reli-hub --since 1`
Expected: je Aufruf `"command_status": "ok"`; elf Zeilen „Kommentar“ von Poutník mit heutigem Datum.

- [ ] **Step 5: Buchführung im FOERBICO-Repo**: Spec-Fahrplan ergänzen, Nachweis-Issue kommentieren (Forgejo-API, Jörgs Token aus `~/.config/forgejo/token.txt`), Stand-Datei ablegen; Prüfung `python3 -I tools/nachweis/check.py erschliessung Hub-Entwicklung` (Namensprüfung) · Expected: Exit 0.

```bash
cd ~/repositories/FOERBICO_und_rpi-virtuell && git add docs/superpowers/specs Hub-Entwicklung/2026-11-16-stand-fuer-ux-gast.md && git commit -m "Spec: Etappe 2 erledigt, Navigation rund geschliffen; Stand für den UX-Gast und Abnahme-Checkliste"
```

- [ ] **Step 6: Abnahme am 25.11.2026**: Checkliste durchgehen, Ergebnis in `Hub-Entwicklung/2026-11-25-abnahme-navigation.md` (Befunde ohne Personennamen); was der Gast einwendet, wird Issue-Kommentar oder neues Issue (Runde 5), nicht Nacharbeit ohne Faden.
