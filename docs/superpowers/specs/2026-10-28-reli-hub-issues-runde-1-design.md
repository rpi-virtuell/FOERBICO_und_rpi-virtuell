# reli-hub-Prototyp: erste Issue-Runde (Design)

Stand 28.10.2026. Betrifft das Repo `reli-hub` auf gitworkshop (`nostr://laoc.xyz/reli-hub`, Klon `~/repositories/reli-hub`), Datei `index.html` (Prototyp 5, eine HTML-Datei, 2334 Zeilen). Dieses Dokument ist die Arbeitsgrundlage für den Umsetzungsplan; die dauerhaften Grundentscheidungen wandern als ADRs in das reli-hub-Repo selbst (Abschnitt 8).

## 1. Anlass

Die Co-Maintainerin `1bf3806b…` hat am 27./28.10.2026 fünf Issues in reli-hub angelegt (alle offen, ohne Kommentare):

| Issue-ID (Kurzform) | Titel | Kern |
|---|---|---|
| `390d2fa0…` | Finden → Artikel/News | Newsbeiträge und Artikel sollen bei „finden“ auftauchen; der Materialpool zeigt nur Lehr-/Lerninhalte |
| `da392383…` | Finden → Newsletter | Newsletter der verschiedenen Communities anzeigen |
| `ef87ccaa…` | Formular Artikel → in Communities teilen | Beitrags-Formular braucht „in Communities teilen“ |
| `fd31ec90…` | Farben überarbeiten | Barrierearmut (Kontrast), Farbwelt von CI, Communities, rpi-virtuell |
| `74b30cd5…` | FOERBICO abbilden | oer.community als Schaufenster im Hub |

Jörg hat entschieden, die Issues selbst zu beantworten: ein PR von Poutník mit einem Commit je Issue, Merge nach `main` durch Jörg, danach je Issue ein Kommentar mit der Änderung „zur Diskussion und zum Weiterdenken“. Die Issues bleiben offen, bis die Autorin reagiert.

## 2. Ziele, Nicht-Ziele, Anti-Ziele

**Ziele**
- Jedes der fünf Issues bekommt eine sichtbare, klickbare Antwort im Prototyp, die als Diskussionsgrundlage taugt.
- Grundentscheidungen (Farbsystem, Instanzen-Nachbau, Teilen-Modell, Newsletter-Form, Artikel im Finden) sind als ADRs im reli-hub-Repo festgehalten, damit sie auch bei späterer Änderung einen Referenzpunkt haben.
- Der Prototyp bleibt in seiner Bauweise: eine Datei, kein Build, kein Framework, keine externen Dateien außer Google Fonts und per URL verlinkten Bildern.

**Nicht-Ziele**
- Keine echte Nostr-Anbindung (keine Relay-Lese- oder Schreiboperationen); wie bisher zeigt der Prototyp Zielvokabular und Beispieldaten.
- Keine Änderung der Fünf-Funktionen-Ontologie der Steuerkonsole (fünf Kreise bleiben; neue Knospen sind erlaubt).
- Keine Umsetzung in Svelte oder in der edufeed-App; das kommt später auf den Prototyp drauf.
- Kein Nachbau aller 90 Blogbeiträge; ein Schnappschuss reicht.

**Anti-Ziele** (Fehlschlag, auch wenn es technisch läuft)
- Der Prototyp wird abhängig von Dateien neben `index.html` oder von einem Build-Schritt.
- Textkontraste bleiben unter 4,5:1 oder Fokus ist nicht sichtbar.
- Issue-Kommentare oder ADRs enthalten Arbeitspakete, Meilensteine, Förderkennzeichen oder Berichtsbezüge (Trennung der Projektdoku, siehe Skill-Abschnitt 5). Ausnahme: der Fuß des Schaufenster-Views spiegelt den Fuß der Webseite, der die Förderung nennt; das ist Nachbau, nicht Projektdoku.
- Bewertungen über Personen in Commit-Texten, ADRs oder Kommentaren.

## 3. Rahmenbedingungen

- Datei: `index.html` (264 KB). Struktur laut `docs/konstruktion.md` im reli-hub-Repo: sieben `div.view` mit Hash-Routing (`route()` Z. 2305–2321, `go()` 2283), Web Component `relihub-steuerkonsole` (Shadow DOM), Kontextprofile `registerContext` Z. 2200–2280, Funktionsontologie `FUNCS` 1103–1113 / `ROUTES` 1122–1134 / `EX` ~1506–1512 / `SUBL` 1541, Partner `PARTNERS` 1554–1567 (Rendering 1570–1575), Communities `CY` 1915–1934 (Kacheln `cyCards` 1941–1948, Raum `crRender` 2046–2060, Inhalte `CR` 1985–1996 / `crData` 1999–2007 / `crItem` 2017–2024), Beitrags-Editor `openBlog` 1866–1910, Profil-News `NEWS` 1592–1598, Prototyp-Leiste `nav.proto` Z. 1030, Farben `:root` Z. 10–15 und relidesk-Palette Z. 239. Zeilennummern gelten für `main` = `d130782` (Builder-Check: `route()` 2301–2325, `go()` 2286); sie verschieben sich mit jedem Commit und sind Orientierung, keine Vorgabe.
- Konventionen des Prototyps (müssen weiter gelten): `data-todo` für nicht Gebautes mit Toast, `later()` für Konsolen-Ziele ohne Ansicht, Persona „Luca Beispiel“, Fuß „Teil des reli_hub“ in jeder Instanz, Flip-Kacheln mit Touch-Regel, `prefers-reduced-motion`, `aria-live` für die Erklärkarte.
- Gestaltungsquellen: Styleguide `Website/Design/styleguide.md` (FOERBICO-Palette) und Theme `Website/assets/css/extended/zz001-foerbico-theme.css`; Webseiten-Struktur aus `Website/hugo.yaml`, `content/de/`, `layouts/_partials/footer.html`; Team aus `content/de/unser-team/index.md` (zehn Personen in drei Institutionen, öffentlich).
- Namen: Die Teamseite ist öffentlich, ihre Namen dürfen im Schaufenster-View erscheinen (Nachbau der Webseite). In Commit-Texten, ADRs, Issue-Kommentaren und in diesem Repo gilt: Rollen, Handles oder Pubkey-Präfixe statt Vornamen von Partnern (Ausnahme: Prototyp-Urheber Jens Dechow, freigegeben).
- Veröffentlichung nur über das Poutník-Werkzeug (`deno task push pr/<slug> --as poutnik`), Merge und Push nach `main` durch Jörg (`ngit --signer joerg pr merge`, `deno task push main --as joerg`), Issue-Kommentare als Poutník nach Freigabe im Gespräch.

## 4. Entscheidungen je Issue

### 4.1 Farben (Issue `fd31ec90…`) — weitestgehende Lösung

**Palette.** Die fünf Bereichsfarben bleiben als Ontologie erhalten; zwei Werte ändern sich:

| Variable | bisher | neu | Grund |
|---|---|---|---|
| `--c-hub` | `#233E99` | `#203A8F` | FOERBICO-Markenblau; Comenius-Logo-Blau gemessen `#1B3892`, praktisch gleich |
| `--c-erstellen` | `#F39200` | `#FFA500` | FOERBICO-Orange (Styleguide Farbe 2) |
| `--c-finden` | `#008C86` | `#007A75` | kein Text erreicht auf `#008C86` 4,5:1 (Weiß 4,1, `--ink` 4,1); `#007A75` trägt Weiß mit ≈5,0:1. Builder-Entscheid: abdunkeln statt Ausnahme für Konsolen-Labels |
| `--c-koop` | `#D6336C` | bleibt | Flächenfarbe; für Text siehe `--x-koop` |
| `--c-ver` | `#7B4FB8` | bleibt | 5,5:1 auf Weiß, in Ordnung |

Neu je Bereich eine **Textfarbe** `--x-<bereich>` mit mindestens 4,5:1 auf `--paper`, `--card` und dem eigenen Tint `--t-<bereich>`: `--x-hub: #203A8F`, `--x-finden: #00605C`, `--x-erstellen: #8A4C00`, `--x-koop: #7A1A3E`, `--x-ver: #5A3590` (Werte sind Startwerte; der Builder prüft rechnerisch und passt an, bis alle drei Kombinationen ≥ 4,5:1 sind). Tints `--t-*` bleiben, `--t-erstellen` wird auf `#FFF1D6` angepasst, falls der Kontrast der Textfarbe es verlangt.

Zusätzlich die FOERBICO-Hilfsfarben als Variablen für den Schaufenster-View: `--fo-blau #203A8F`, `--fo-orange #FFA500`, `--fo-titel #002366`, `--fo-text #333333`, `--fo-hell #F0F8FF`, `--fo-kopf #E6F2FF`, `--fo-rahmen #D3D3D3`.

**Regeln.**
- Farbtext (Quellenangaben `.src`, Daten `.mat .th`, `.ev .date`, `.cr-date`, `.cr-ev small`, `.cy-back small`, `.cr-badge`, `.eyebrow i`, Follow-Schalter) benutzt `--x-*`, nie `--c-*`.
- Weißer Text liegt nur auf `--c-hub`, `--c-ver`, `--c-koop` (4,6:1 auf Weiß, knapp) und `--c-finden` (neu, ≈5,0:1) und auf `--ink`; auf `--c-erstellen` liegt dunkler Text (`#2B1A00`, 7:1). `FUNCS` hat dafür bereits das Feld `text` je Funktion (erstellen steht schon auf `#2B1A00`); es bleibt die einzige Quelle für Label-Farben der Konsole.
- Kleine Schrift (< 14 px) auf farbigem Grund nur, wenn der Kontrast ≥ 4,5:1 bleibt; sonst Größe oder Farbe anpassen (betroffen: `.rd-ey` 11 px, Platzhalter `#8A8378`, `#7A808A`, `.reco .img`, `.rd-toggle`, relidesk-Hero).
- Nachbau-Paletten (`--mp-*`, `--rd-*`, relilab-Magenta) bleiben als Instanzfarben, werden aber auf dieselbe Kontrastregel gebracht, ohne ihren Charakter zu ändern (Abdunkeln der Textvarianten).
- Fokus: generische Regel `button:focus-visible, [tabindex]:focus-visible, a:focus-visible, .btn:focus-visible { outline: 3px solid var(--ink); outline-offset: 2px }`; innerhalb der Konsole die vorhandene `.mini:focus-visible`-Regel beibehalten.

**Zentralisierung.** Für die Prototyp-Anwendung (zweites Skript) stehen alle Hex-Werte der Bereichsfarben nur noch in `:root`: `C`/`T` (Z. 1490–1491), `TINT`/`TINK` (1568–1569), Petals (1496), `rtPre` (2162), `SHIELD` (1913), der CampusCom-Eintrag in `CY` (1920) und der `crItem`-Fallback lesen über eine Hilfsfunktion `cssVar(name)` (`getComputedStyle(document.documentElement).getPropertyValue`). Die **Konsole** (erstes Skript, später eigenständige Datei `relihub-steuerkonsole.js`, die auch auf fremden Seiten ohne Hub-`:root` laufen muss) behält ihre eigenen Standardwerte in `FUNCS` als Fallback und liest beim Verbinden mit dem Dokument die Custom Properties `--relihub-c-<id>` und `--relihub-text-<id>` vom Host-Element (`getComputedStyle(this)`); sind sie gesetzt, überschreiben sie Farbe und Labelfarbe, bevor `mix()` und die SVG-`fill`-Attribute berechnet werden. Das Hub-Dokument setzt diese Properties in `:root` aus den `--c-*`/`--x-*`-Werten. Ergebnis: ein Theme-Wechsel ist ein Austausch von `:root`; die Konsole bleibt allein lauffähig.

**Nachweis.** Eine kleine Prüfseite ist nicht nötig; stattdessen enthält der Commit-Text die berechneten Kontrastwerte der zehn wichtigsten Kombinationen (Textfarbe je Bereich auf paper/card/tint, Weiß auf hub/ver/koop). Der Builder berechnet mit der WCAG-Formel (relative Luminanz, (L1+0,05)/(L2+0,05)).

### 4.2 OER-Community als Schaufenster (Issue `74b30cd5…`)

**Einstieg.** Die schwarze Prototyp-Leiste unten links (`nav.proto`, Z. 1030) bekommt als sechsten Eintrag „FOERBICO“, Ziel `#oercommunity`. Im Ökosystem (`PARTNERS`) eine Kachel `['OER-Community', 'Schaufenster des Projekts FOERBICO', 'hub', 'OC', '#oercommunity', '<Rückseitentext>']` mit Bereich `hub`. In `CY` ein Community-Eintrag „OER-Community“ (Typ `netz`, `inst: ['OER-Community', 'oercommunity']`, Bio aus dem Startseitentext, `series` leer, Newsletter-Feld siehe 4.5), damit `cyRel` den Instanz-Bezug zeigt. Die Persona **folgt** dieser Community (Eintrag in `cyFollow`, nicht `mine`; die Liste „Meine Communities“ `COMM` im Profil bleibt unverändert), damit ihre Artikel im Profil-Panel (4.3) erscheinen, ohne die Persona zum Projektmitglied zu machen.

**Der View `#v-oercommunity`.** Ein Nachbau von oer.community im Stil der anderen Instanzen (Regel 3 der Konstruktionsbeschreibung: nachbauen, nicht neu gestalten; der Hub fügt nur Vermerk, Profil-Link, schwebende Konsole und Vorauswahl-Banner hinzu).

- Schrift Roboto Condensed (schon geladen in 600/700, Z. 8; Gewicht 400 für Fließtext ergänzen), Hintergrund Weiß, Text `--fo-text`, Überschriften `--fo-titel`, Kopfzeile `--fo-kopf` mit 2 px Linie `--fo-orange` darunter, Karten mit 1 px Rahmen `--fo-orange` und Radius 5 px (wie die PaperMod-Post-Entries der Webseite).
- Kopfzeile: Wortmarke „oer.community“ (Text, kein Logo-Bild), Menü: Tagungen, Was ist OER?, Qualität, Team, Blog. Menüpunkte springen per Anker innerhalb des Views (keine Unterseiten).
- Abschnitt **Start**: Logo `https://oer.community/images/FOERBICO.png` (per URL), H1 „FOERBICO“, H2 „Förderung offener Bildungspraktiken und Ressourcen im Kontext des religionspädagogischen OER-Ökosystems“ (Wortlaut der Startseite übernehmen), die beiden Einladungsabsätze gekürzt, Link „Space OERcommunity“ (Element/Matrix) als externer Link.
- Abschnitt **Blog**: die fünf neuesten Beiträge (Stand 29.09.2026, Titel, Datum, Tags, erster Satz, Titelbild per Blossom-URL aus dem Frontmatter, Lizenzpille unten rechts am Bild wie auf der Webseite). Jeder Beitrag verlinkt extern auf die Webseite. Zusätzlich sind diese fünf Beiträge als Typ „Artikel“ in der neuen Community „OER-Community“ (4.4) hinterlegt, damit sie im Profil-Panel „Artikel aus deinen Communities“ erscheinen können.
- Abschnitt **Tagungen**: zwei Karten (Abschlusstagung „Offen. Vernetzt. Zukunft“ 2./3.2.2027 Frankfurt, Anmeldung bis 22.1.2027; Zwischenfazit-Tagung 2026 Nürnberg mit Rückblick-Link). Daten zusätzlich als zwei Termine im Hub-Datensatz `EVENTS`, Quelle „OER-Community“, damit sie im Profil unter „Passende Veranstaltungen“ auftauchen können.
- Abschnitt **Was ist OER? / Qualität**: zwei Teaser-Kacheln mit zwei Sätzen und externem Link (Lernmodul, Qualitätskriterien-PDF).
- Abschnitt **Team**: drei Gruppen (Comenius-Institut, Goethe-Universität Frankfurt, FAU Erlangen-Nürnberg) mit den zehn Personen der Teamseite: Name, Funktion, Porträt per URL `https://oer.community/unser-team/<Datei>` mit Initialen-Fallback bei Ladefehler. Keine Mailadressen.
- Fuß: „CC BY 2024–2026 FOERBICO – soweit nicht anders angegeben · Impressum & Datenschutz“ (externe Links), darunter die Hub-Zeile „Teil des reli_hub · Datenstand 29.09.2026“.
- Schwebende Konsole mit Kontext `oer-community`: `hub.home` → `go('start')`, `finden.material` → Materialpool mit `thema=OER`, `veroeffentlichen.beitrag` → `openBlog('OER-Community')`, `kooperieren.communities` → `#community?c=oercommunity`, alles andere `later()`.
- Route `#oercommunity` in `route()`, Eintrag in der Prototyp-Leiste, Hover-/Flip-Text der Partner-Kachel.

**Bilder.** Per URL eingebunden (oer.community, Blossom). Fällt ein Bild aus, zeigt `onerror` einen Platzhalter in `--fo-hell` mit Initialen oder Titel. Die Datei bleibt damit allein lauffähig, auch offline (dann ohne Bilder).

**Offen gelassen, bewusst.** Keine Tag-Übersicht, keine Hell/Dunkel-Umschaltung, keine Suche (die Webseite hat auch keine).

### 4.3 Finden → Artikel (Issue `390d2fa0…`) — mittlere Lösung

- Dritte Knospe `finden.beitraege` („Beiträge“) in `FUNCS`, `ROUTES` (`/finden/beitraege`), `EX`. Nebenwirkung, gewollt: mit drei Knospen wechselt das Popover von finden von Halbkreisen (zwei Subs) auf Knospen (drei Subs), wie bei veröffentlichen. (Erklärtext: „Artikel und Nachrichten aus deinen Communities und Instanzen; Lehr- und Lerninhalte findest du im Materialpool“), `SUBL`. Ziel im Hub: Profil, Scroll zum neuen Panel. In den Instanz-Kontexten `later()`.
- Neues Panel **„Artikel aus deinen Communities“** im Profil (`#v-profil`, neben `#news`): sammelt alle Einträge vom Typ „Artikel“ aus `CR`/`crData` aller Communities, in denen die Persona Mitglied ist oder denen sie folgt (`cyFollow`), sortiert nach `ago`, Darstellung mit `crItem` (Typ-Pille, Community-Name als Quelle, Link in den Raum-Tab „Artikel“). Leerzustand: „Folge Communities, um hier Artikel zu sehen.“
- Das bestehende Panel `#news` bleibt (Nachrichten aus dem Netz); der Unterschied steht im Panel-Untertitel.
- Der Materialpool bleibt unverändert; die Erklärkarte von `finden` sagt das ausdrücklich.

### 4.4 In Communities teilen (Issue `ef87ccaa…`) — wie in der edufeed-App

- Im Beitrags-Editor `openBlog` unterhalb der Hashtags ein Abschnitt **„Mit Communities teilen (optional)“**, Untertitel „Communities auswählen“: scrollbare Liste (max. ~160 px) aller Communities, in denen die Persona Mitglied ist oder denen sie folgt (`cyFollow`), je Zeile Avatar-Kreis, Name, Checkbox, dahinter Status „(wird geteilt)“; Buttons „Alle auswählen“ / „Alle abwählen“. Communities, denen die Persona nur folgt (kein `mine`, z. B. relimentar und OER-Community), erscheinen deaktiviert mit 🔒 „Nur Mitglieder“; Mitglieds-Communities sind wählbar. (`ver` in `CY` bedeutet „verifiziert“ und spielt hier keine Rolle.) Vorbelegt ist die Kontext-Community, wenn der Editor aus einem Raum geöffnet wurde (`ctx` = Community-Name) oder aus einer Instanz, die über `inst` mit einer Community verbunden ist (relilab → relilab-Community); die Vorbelegung greift nur, wenn die Community wählbar ist.
- Beim Veröffentlichen: der Beitrag wird als `T_('Artikel', titel, {who:'Luca Beispiel', ago:'jetzt', x: zusammenfassung, tags})` in `CR[id].act` jeder gewählten Community vorn eingefügt und, falls ein Raum offen ist, neu gerendert. Zusätzlich landet er im Profil-Panel aus 4.3.
- Toast nennt die Zielform: „würde jetzt als Nostr-Langform-Artikel veröffentlicht (NIP-23, kind 30023) und mit einem Repost (kind 16) mit h-Tags an N Communities geteilt: A, B“. Wurde der Editor aus einem Raum geöffnet, erhält der Artikel selbst ein h-Tag dieser Community (Hinweis im Toast), wie in der edufeed-App; aus einer Instanz heraus gibt es nur die Vorbelegung, kein h-Tag.
- Der Termin-Editor bekommt denselben Abschnitt (die edufeed-App hat ihn dort; Mehraufwand gering, Komponente wird geteilt). Der Lerninhalt-Editor bleibt in dieser Runde unverändert (Hinweis im Issue-Kommentar).

### 4.5 Newsletter (Issue `da392383…`) — Nostr-konform

- **Form auf Nostr:** je Newsletter ein Web-Lesezeichen nach NIP-B0 (kind 39701), veröffentlicht vom Community-Schlüssel: `d` = Anmelde-URL ohne Schema, `title` = Name des Newsletters, `content` = Rhythmus/Beschreibung, `t` = `newsletter` (plus Themen-Tags). Clients fragen `{kinds:[39701], authors:[community], '#t':['newsletter']}`. Begründung: kein eigener Kind nötig, Anmelde-URLs fremder Systeme (Mailchimp, Listmonk, CleverReach, Matrix-Räume) passen, NIP-22-Kommentare möglich, löschbar per kind 5. Verworfen: NIP-51-Sets (nur Nostr-Referenzen, keine URLs), Feld im kind 10222 (dort bedeutet `r` Relay), Feld im kind 0 (nur eine `website`).
- **Im Prototyp:** optionales Feld `nl: [[name, rhythmus, url], …]` je Community in `CY`. Startdaten: relilab-Newsletter (relilab.org, monatlich), „Münchner Reli Room-Newsletter“ (4–6 Mal im Jahr, aus `series` übernehmen), OER-Community (noch keiner; Eintrag ohne `nl`). Darstellung: Pille „Newsletter“ auf der Community-Kachel (neben `.cy-ser`), Link-Zeile im Raum-Kopf („Newsletter: Name · Rhythmus · anmelden“, externer Link), und unter der Knospe `finden.fortbildungen` im relilab-Terminbereich eine Seitenleisten-Box „Newsletter der Communities“ (`CY.filter(c => c.nl)`). Fußnote in der Box: „Nostr: NIP-B0-Lesezeichen (kind 39701) des Community-Schlüssels, Tag newsletter“.

## 5. Ablauf der Veröffentlichung

1. Branch `pr/issues-runde-1` ab `main` (`d130782`). Fünf Commits, Author `Poutník <poutnik@users.noreply.edufeed.org>`, Reihenfolge: Farben → Schaufenster → Teilen → Finden-Artikel → Newsletter; ein sechster Commit für README und ADRs. Jeder Commit-Text nennt die Issue-ID (Kurzform) und bei Farben die Kontrastwerte.
2. Vor dem Push: Diff und Ansicht im Browser (Preview über `python3 -m http.server` im Klon oder Datei direkt) Jörg zeigen; Freigabe abwarten.
3. `deno task push pr/issues-runde-1 --as poutnik --cwd ~/repositories/reli-hub`; Merge und `main`-Push durch Jörg.
4. Je Issue ein Kommentar von Poutník (nach Freigabe im Gespräch): Bezug in einem Satz, was geändert wurde, Link auf den Commit auf gitworkshop und auf das ADR, dann die offene Frage zum Weiterdenken (z. B. bei Farben: „Soll das relilab-Magenta ebenfalls an die Hub-Palette heranrücken?“). Keine Signaturzeile. Issues bleiben offen.

## 6. README und ADRs im reli-hub-Repo

- `README.md` bekommt einen Abschnitt **„Grundentscheidungen“**: zwei Sätze, was ADRs hier sind (Referenzpunkt, auch wenn sich Entscheidungen ändern; Änderung = neues ADR, das das alte ersetzt), dann eine Liste der ADRs mit Titel und Status.
- `docs/adr/README.md`: Format (Nummer, Titel, Status: vorgeschlagen / angenommen / ersetzt durch, Datum, Kontext, Entscheidung, Folgen, Bezug auf Issue-IDs), ein Satz zur Sprache (Deutsch) und zur Regel „keine Personenbewertungen“.
- ADRs dieser Runde (Status „angenommen“, Datum 28.10.2026, Entscheider: Maintainer, Bezug: Issue-ID):
  - `0001-farbsystem.md`: Fünf-Bereiche-Ontologie bleibt; FOERBICO-Blau und -Orange als Hub- und Erstellen-Farbe; Flächen- vs. Textfarben; Kontrastregel 4,5:1; alle Werte in `:root`; Nachbau-Paletten bleiben Instanzfarben.
  - `0002-instanzen-als-nachbau.md`: Eine Instanz kommt als eigener View im eigenen Design in den Prototyp; der Hub fügt nur Vermerk, Profil-Link, schwebende Konsole und Vorauswahl-Banner hinzu; Einstieg über Prototyp-Leiste und Partner-Kachel; Bilder per URL; OER-Community ist die erste Instanz, die nach dieser Regel neu hinzukommt.
  - `0003-teilen-in-communities.md`: Teilen folgt dem edufeed-Modell (Auswahl eigener Communities beim Veröffentlichen; Artikel mit einem h-Tag bei Kontext, sonst kind-16-Repost mit mehreren h-Tags; keine Freigabe-Stufe, Moderation nachträglich).
  - `0004-newsletter-als-nip-b0.md`: Newsletter einer Community sind kind-39701-Lesezeichen des Community-Schlüssels mit Tag `newsletter`; Alternativen und warum verworfen.
  - `0005-artikel-im-finden.md`: „finden“ umfasst Material, Fortbildungen und Beiträge; Beiträge kommen aus Communities und Instanzen, nicht aus dem Materialpool; Darstellung im Profil.
- Die ADRs enthalten keine Arbeitspakete, Meilensteine oder Förderbezüge.

## 7. Was der Builder entscheidet

- Exakte Textfarbwerte `--x-*` und ggf. Tint-Anpassung nach Kontrastrechnung.
- Kürzung der Startseitentexte und Rückseitentexte der Kacheln (Sinn erhalten, Wortlaut der Webseite bevorzugen).
- Aufbau der geteilten „Communities auswählen“-Komponente (eine Render-Funktion für Beitrags- und Termin-Editor).
- Wo im Profil das neue Panel steht (Vorschlag: direkt nach „Neue Materialien für dich“, vor `#news`).
- Wie `cssVar()` in den Shadow DOM der Konsole kommt (Attribut je Farbe oder Vererbung von Custom Properties); Bedingung: keine Hex-Werte mehr außerhalb von `:root`.

## 8. Verweise

- Issues: gitworkshop.dev/laoc.xyz/relay.ngit.dev/reli-hub (IDs oben).
- Konstruktionsbeschreibung: `docs/konstruktion.md` im reli-hub-Repo.
- Styleguide und Theme der Webseite: `Website/Design/styleguide.md`, `Website/assets/css/extended/zz001-foerbico-theme.css`.
- edufeed-Teilen-Modell: Fork `~/repositories/hub`, `src/lib/helpers/communityRepost.js`, `src/lib/components/shared/CommunityShare.svelte`, `src/lib/components/calendar/CommunitySelector.svelte`.
- Poutník-Skill: `.claude/skills/poutnik/SKILL.md`.
