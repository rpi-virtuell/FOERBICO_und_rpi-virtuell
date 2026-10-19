# Termine als Nostr-Kalender-Events anlegen — Arbeitsweise

Stand 19.10.2026. Beschreibt, wie aus einer Terminankündigung (Flyer, Instagram-Post,
Programmheft, Mail) signierte `kind 31923`-Events im edufeed-Datenraum werden.
Abgeleitet aus zwei Durchläufen: `relilab-impuls-2026-27` (zehn Termine, drei
Landessysteme) und `interreligioese-fortbildungsreihe-vml-2026-27` (vier Module,
zwei Schulreferate, ChurchDesk). Die Tag-Semantik folgt dem edufeed-Guide
`calendar-integration.md` (Abschnitte 2.1–2.5, beschlossen) und der Ergänzung
`relilab-impuls-2026-27/calendar-integration-ergaenzung.md` (Abschnitte 2.6–2.13,
Entwurf). Was hier als „Vorschlag“ markiert ist, steht noch in keinem von beiden.

## 0. Grundsatz

Die Ankündigung, die den Anstoß gibt, ist fast nie die Quelle. Ein Instagram-Post
nennt Themen, keine Daten; ein Programmheft nennt Daten, keine Anmeldelinks; das
Anmeldesystem nennt Links und Fristen, aber keine Referent:innen. Die Arbeit besteht
darin, **je Feld die beste Quelle zu finden** und festzuhalten, woher der Wert stammt.
Ein Termin ohne belegbare Quelle für `start` wird nicht publiziert.

## 1. Ablauf

### Phase A — Anstoß sichten

Aus der Ankündigung extrahieren: Reihe/Titel, Veranstalter, Kooperationspartner,
Module/Themen, genannte Links, genannte Namen. Daraus eine Soll-Liste der Termine
bilden („vier Module“ = vier Events). Noch nichts anlegen.

### Phase B — Termine belegen (Quellenhierarchie)

In dieser Reihenfolge suchen, aufhören, sobald Datum, Uhrzeit, Ort und Dauer belegt sind:

1. **Anmeldesystem des Veranstalters** (eVEWA, ChurchDesk, Ekiba-Bildungsportal,
   sementis/guidecom). Hat Start, Ende, Frist, Formular-URL, oft Bild und Alt-Text.
2. **Programmheft (PDF)** des Halbjahres. Hat Datum, Uhrzeit, Anmeldefrist, Leitung,
   Referent:innen, Volltext. Mit `pdftotext -layout` extrahieren, dann nach Stichworten greifen.
3. **Verbundkalender** der Landeskirche oder des Instituts (PTI-Kalender der EKiR,
   relilab.org). Gut für Querprüfung, selten vollständig.
4. **Webseite des Veranstalters.** Vorsicht: Terminlisten sind oft per JavaScript
   geladen (Elementor-Shortcodes, ChurchDesk-Widgets, Event-Plugins) und für
   `curl`/WebFetch leer. Dann Browser nutzen oder die Datenquelle hinter dem Widget
   finden (siehe Abschnitt 3).
5. **Social Media / Flyer.** Nur Anstoß, nie alleinige Quelle.

Was nach Durchlauf aller fünf Ebenen ohne Datum bleibt, wird im README als „noch
nicht veröffentlicht“ geführt, mit Prüfdatum und Fundort für später. Keine
Platzhalter-Events.

### Phase C — Volltext, Personen, Institutionen

- **Beschreibung:** die offizielle Ausschreibung wörtlich in `content`, ergänzt um
  einen Absatz zur Reihe und zu Zielgruppe/Frist. Nicht paraphrasieren, nicht kürzen.
- **Titel:** die offizielle Ausschreibung, nicht die Kurzform des Anstoßes
  („Weihnachten religionssensibel gestalten“, nicht „Weihnachten in Schule und
  Unterricht gestalten“). Die Kurzform darf in `summary` oder `content` vorkommen.
- **Personen:** Rolle je Person klären (Leitung, Referent:in, Kooperation, Moderation)
  und Haus zuordnen. Zwei Formen, beide eintragen:
  1. `["participant", "<Name> (<Haus>)", "", "<rolle>"]` — das liest die edufeed-App
     (Wiki-Artikel `edufeed-calendar-event-tags`). Rollen der App: `speaker`,
     `organizer`, `moderator`, `participant`, `attendee`. Mapping: Referent:in →
     `speaker`, Leitung und Kooperation → `organizer`. Haus in Klammern, weil der Tag
     keinen Affiliations-Slot hat.
  2. `contributor:*`/`performer:*`-Flattening mit Rolle und `affiliation:name`
     (Ergänzung 2.8) — trägt die Affiliation strukturiert, die App ignoriert es,
     bewahrt es aber beim Bearbeiten. Bleibt, bis das Rollen-Issue entscheidet.
  `p`-Tag nur bei bekanntem Schlüssel.
- **Institutionen:** als `organizer:name`/`organizer:type` (Vorschlag, siehe 5.2).

### Phase D — Anmeldung, Frist, Kosten, Modus

- `registrationRequired` immer setzen, wenn die Quelle es hergibt.
- `registrationUrl` je Anmeldeweg (Region als ISO 3166-2 oder leer), Beschriftung
  sagt ehrlich, ob der Link ins Formular führt oder nur auf eine Einstiegsseite
  („Anmeldung dort suchen“, „Formular folgt dort“).
- `registrationDeadline` als Unix-Timestamp, Ende des genannten Tages in `start_tzid`
  (23:59). Quelle meist Programmheft. **Frist muss vor `start` liegen** — ein Tippfehler
  hier schaltet die Anmeldung still ab.
- `price` nur setzen, wenn eine Quelle Kosten nennt. Fehlt die Angabe, fehlt der Tag.
- `eventAttendanceMode` aus Ort ableiten; `location` bei Online-Terminen als Text
  („Online (Zoom), Zugangsdaten nach Anmeldung“), nie der Zoom-Link selbst.
- `eventStatus` immer `EventScheduled` setzen, damit eine spätere Absage ein Diff ist.

### Phase E — Bild

Nur mit ausgewiesener Lizenz `image:license:id` setzen. Pixabay, „© Haus XY“ oder
„mit freundlicher Genehmigung“ sind keine Weitergabelizenz; dann `image` mit
`image:creator:name` und `image:description` (Alt-Text aus der Quelle), aber ohne
Lizenz-Tag — Clients zeigen das Community-Fallback. Eigenes CC-Motiv: auf Blossom
hochladen, `kind 1063`-Nachweis anlegen (Muster in `relilab-impuls-2026-27/events/1063-*`).

### Phase F — Event bauen

- Ablage: `Orga/<reihe>/events/31923-<yyyy-mm-dd>-<slug>.json`, daneben `README.md`
  mit Quellentabelle, Publizierbefehl, Leitungstabelle, offenen Punkten.
- `d`-Tag: `<reihe>-<datum>-<thema>`, stabil, nie die Quell-URL (Begründung: Ergänzung 2.9).
- `h`-Tag: Community, in der der Termin erscheinen soll (relilab:
  `48706e894e64be57a250d3cd1f4c8a0f69ca900937936f8bd11a1329cd3c97e3`).
- `identifier:propertyID`/`identifier:value` je Quellsystem (eVEWA-Nummer,
  ChurchDesk-ID, Kufer-ID). Damit erkennt ein Konsument, dass Crawler-Event und
  kuratiertes Event dieselbe Sitzung meinen.
- `r`-Tags: Veranstaltungsseite, Verbundkalender, Programmseite.
- `t`-Tags: Themen plus Reihen-/Community-Marker (`relilab`).
- `educationalLevel` = Art der Veranstaltung (`level_C` Fortbildung); Schulstufe des
  Inhalts in `about`, Zielgruppe in `audience` (Ergänzung 2.12).
- Timestamps mit `zoneinfo`/`Europe/Berlin` berechnen und zur Kontrolle
  zurückformatieren (Sommer-/Winterzeit!).

### Phase G — Validieren

```
python3 -c 'import json,sys; json.load(open(sys.argv[1]))' events/<datei>.json
NOSTR_SECRET_KEY=$(nak key generate) nak event < events/<datei>.json | nak verify
```

Dazu Sichtprüfung: `start` < `end`, `registrationDeadline` < `start`, Datum und
Uhrzeit gegen zwei Quellen, Titel wörtlich, alle Personen mit Haus.

### Phase H — Publizieren

```
cd events
read -rs NOSTR_SECRET_KEY && export NOSTR_SECRET_KEY
for f in 31923-*.json; do nak event wss://relay.edufeed.org wss://amb-relay.edufeed.org < "$f"; done
unset NOSTR_SECRET_KEY
```

Ohne Relays = Trockenlauf. Alternativ `--prompt-sec` je Aufruf. Der signierende
Schlüssel muss im Roster (`kind 39002`) der Community stehen, sonst bleibt das
Event in der Community-Ansicht unsichtbar.

### Phase I — Nachpflege

- Fehlende Termine: Prüfdatum und Fundort im README, erneut prüfen, wenn das nächste
  Halbjahresprogramm erscheint.
- Fehlende Anmeldelinks (Formular noch nicht freigeschaltet): nachtragen, erneut
  publizieren — gleicher `d`-Tag ersetzt.
- Absage: `eventStatus` auf `EventCancelled`, nicht löschen.
- Crawler-Duplikate: solange Bot und Kurator im Roster stehen, erscheint der Termin
  doppelt; Bot aus dem Roster nehmen, wenn die kuratierten Events vollständig sind.

## 2. Klärungscheckliste je Termin

| Frage | Antwort muss stehen in |
|---|---|
| Offizieller Titel? | `title` |
| Datum, Beginn, Ende, Zeitzone belegt? | `start`, `end`, `*_tzid`, README-Quelle |
| Online, Präsenz, hybrid? Ort? | `eventAttendanceMode`, `location` |
| Anmeldung nötig? Wo, bis wann, je Region? | `registrationRequired`, `registrationUrl`, `registrationDeadline` |
| Kosten genannt? | `price` oder weglassen |
| Wer leitet, wer referiert, aus welchem Haus? | `contributor:*`, `performer:*` |
| Welche Institutionen tragen den Termin? | `organizer:*` |
| Welche Community zeigt ihn? | `h` |
| Externe IDs? | `identifier:*` |
| Bild mit Lizenz? | `image:*` |
| Reihe: welche Module fehlen noch? | README |

## 3. Fundorte und Mechaniken (Erfahrungswerte)

- **ChurchDesk** (viele EKiR-Einrichtungen, z. B. Ev. Schulreferat Düsseldorf):
  Webseite bindet Widgets per iframe ein. Widget-URL
  `https://widget.churchdesk.com/de/w/<org>/event/<widgetId>/<seite>/<siteId>`;
  die Seite liefert in `<script id="__NEXT_DATA__">` ein JSON mit `items[]`
  (Titel, `startDate`/`endDate` in UTC, `contributor`, `url` Landingpage,
  `image.altText`, `image.credits`, `form.url` Anmeldeformular). Seitennummer
  hochzählen, bis `items` leer ist. Landingpage
  `https://landing.churchdesk.com/de/e/<id>` enthält den Volltext. Programmhefte
  liegen als `https://api2.churchdesk.com/files/<uuid>/view`.
- **eVEWA** (Rheinland-Pfalz): Direktlinks brauchen `va_id`, `m` und
  `ev_workflow2_guid`, sonst „Fehlerhafte Parameter“.
- **PTI-Kalender EKiR** (`pti.ekir.de/thema/termine-schulreferate-und-bezirksbeauftragungen/`):
  listet alle rheinischen Schulreferate inkl. Online-Termine, Detail über `?ID=`.
  Gut zum Finden, dünn im Detail.
- **reli-koeln.de**: Terminliste ist ein nicht gerenderter Shortcode, WordPress-Suche
  findet keine Termine. Einzige brauchbare Quelle ist das Programm-PDF
  (`/wp-content/uploads/<jahr>/<monat>/Programm-*.pdf`).
- **WordPress allgemein**: `/wp-json/wp/v2/pages?per_page=100&_fields=slug` zeigt,
  welche Seiten existieren (z. B. `veranstaltungen`, `programm-detail`); `/wp-json/wp/v2/types`
  verrät Event-Plugins.
- **Instagram**: nicht abrufbar; Text vom Nutzer einfügen lassen.

## 4. Was diese Reihe neu eingeführt hat (noch in keiner Spezifikation)

| Tag | Verwendung hier | Status |
|---|---|---|
| `organizer:name`, `organizer:type` | drei tragende Institutionen, AMB-Flattening wie `contributor:*` | Vorschlag |
| `contributor:role` = „Kooperation“ | Partnerinstitution, die mitgestaltet, aber nicht leitet | Vorschlag, Rollenliste fehlt |
| `participant` + `contributor:*` doppelt | App-lesbare Kurzform neben strukturierter Langform, seit 19.10.2026 in allen zwölf Events | Praxis, Entscheidung im Rollen-Issue |
| `registrationUrl` mit Beschriftung „Formular folgt dort“ | Anmeldeweg bekannt, Formular noch nicht frei | Praxis |
| `identifier:propertyID` = „ChurchDesk“ | Event-ID des Quellsystems | Praxis, analog eVEWA/Kufer |

## 5. Verbesserungsvorschläge, iterativ

Sortiert nach Aufwand. Jede Stufe ist für sich nutzbar.

### 5.1 Sofort: Anmeldefrist in den Wiki-Eintrag heben

`registrationDeadline` existiert bereits als Entwurf (Ergänzung 2.7) und steht in
allen zwölf publizierten Events. Der beschlossene Guide (2.1) sagt dagegen ausdrücklich,
Fristen gehörten in den Beschreibungstext. Das ist der eigentliche offene Punkt: die
Ergänzung ist nicht im Wiki. Vorschlag für den Wiki-Text, präziser als bisher:

```
["registrationDeadline", "<unix seconds>"]
```

- Zeitpunkt, bis zu dem eine Anmeldung angenommen wird, inklusive. Nennt die
  Quelle nur ein Datum, gilt 23:59 in `start_tzid`.
- Muss vor `start` liegen; Clients ignorieren eine Frist nach `start` und melden sie.
- Fehlt der Tag, gilt: anmelden bis Beginn, sofern `registrationRequired` gesetzt ist.
- Clients zeigen „Anmeldung bis …“ und blenden den Anmeldelink nach Ablauf aus
  oder markieren ihn.

Dazu `registrationUrl` mit den drei Positionen (URL, Region, Beschriftung) aus 2.7
übernehmen. Beides als Antwort in edufeed-app#13 und als Edit am `30818`-Eintrag.

### 5.2 Kurzfristig: Rollen und Institutionen festziehen (eigenes Issue)

Die App kennt bereits `participant` mit fünf Rollen, ohne Affiliation. Unsere
Events tragen seit 19.10.2026 beide Formen. Das Issue muss klären: Affiliations-Slot
für `participant` oder Flattening als Zweitform; Rollen als nocabs-Vokabular;
Institutionen als Beteiligte. Getrennt vom Anmelde-Issue (5.1, 5.3), weil es ein
Vokabular braucht und nicht nur drei Tags.

- Rollenliste für `contributor:role` vereinbaren, am besten als kleines SKOS-Vokabular
  auf nocabs: Leitung, Referent:in, Moderation, Kooperation, Kontakt. Solange frei
  getextet wird, driftet es („Leitung“ vs. „Gesamtleitung“ vs. „Koordination“).
- `organizer:*`-Flattening in 2.8 aufnehmen, parallel zum `p`-Tag mit Rolle
  `organizer`. Grund: Institutionen haben noch seltener Schlüssel als Personen.
- Konvention: `performer` nur, wer referiert; wer leitet und referiert, bekommt
  beides (heute uneinheitlich zwischen den beiden Reihen).

### 5.3 Kurzfristig: Anmeldezustand

Fälle aus der Praxis, die `registrationRequired` + `registrationDeadline` nicht abdecken:

- Formular noch nicht freigeschaltet (Ramadan-Termin): heute nur als Beschriftung.
- Warteliste, ausgebucht, Anmeldung geschlossen vor Frist.
- Anmeldung öffnet erst ab Datum X (Halbjahresprogramm erscheint, Frist läuft später).

Vorschlag: `["registrationStatus", "<wert>"]` mit `open`, `notYetOpen`, `waitlist`,
`full`, `closed`, optional `["registrationOpens", "<unix seconds>"]`. Fehlt der
Tag: `open`, solange die Frist nicht abgelaufen ist. Kleiner Eingriff, großer
Nutzen für Clients, die sonst auf ein totes Formular verlinken.

### 5.4 Mittelfristig: Reihe als eigenes Objekt

Vier Module, zwei davon noch ohne Datum, gehören als Reihe zusammen. Heute steht
das nur im `content`-Absatz. Zwei Wege aus Ergänzung 2.13:

- **Kalender `kind 31924`** „Interreligiöse Fortbildungsreihe VML 2026/27“ mit
  `a`-Verweisen auf jedes `31923`. Nachträglich erweiterbar, wenn Abraham und
  Schulfeiern kommen.
- **Community** für die Reihe (eigener Schlüssel, `kind 10222`), Termine per `h`.
  Lohnt erst, wenn die Reihe über ein Jahr hinaus läuft.

Für diese Reihe: `31924` anlegen, sobald der dritte Termin feststeht.

### 5.5 Mittelfristig: Quelle statt Hand-JSON

Die JSON-Dateien entstehen heute aus einem Python-Block in der Session. Besser nach
dem Prinzip der Wissensgrundlagen (`felder.yaml`): eine `events.yaml` je Reihe mit
den menschlichen Feldern (Datum als `2026-11-12 16:00–19:00`, Frist als Datum,
Personen mit Rolle und Haus, Quellen je Feld) und ein Generator, der daraus die
`31923`-JSONs schreibt. Vorteile: Timestamps werden nie von Hand gerechnet,
Validierung (Frist < Start, Ende > Start, Pflichttags, Zeitzone) läuft im Generator,
die Quellentabelle im README wird mitgeneriert. Zweiter Schritt: Scraper für
ChurchDesk-Widgets und eVEWA, die eine `events.yaml` vorbefüllen.

### 5.6 Mittelfristig: Lizenznachweis der Bilder

Wie beim relilab-Impuls bleibt die Bildfrage offen. Zwei Standardwege festlegen:
(a) Veranstalter liefert CC-Motiv, wir laden auf Blossom und prägen `1063`;
(b) Community-Fallback. Dazu die Regel in 2.11 um einen Satz ergänzen: Ein `image`
ohne `image:license:id` darf vom Client angezeigt, aber nicht weiterverbreitet
werden — das deckt den heutigen Zustand ehrlich ab.

### 5.7 Längerfristig: Dubletten und Status relay-seitig

- Der Crawler (`relilab-Termine-Bot`) und kuratierte Events laufen parallel. Mit
  `identifier:*` können Clients sie zusammenführen; der Wiki-Eintrag sollte das als
  Lesevorschrift festhalten (gleicher `identifier` = gleiche Sitzung, kuratiert
  schlägt gecrawlt).
- `eventStatus`, `registrationDeadline`, `h` sollten vom Kalender-Relay indiziert
  werden (Folgepunkt zu „Kalender-Relay anpassen“ in Guide Abschnitt 6).
- „Bevorstehend“ ist relay-seitig nicht filterbar (`since`/`until` greifen auf
  `created_at`). Ein Relay-Index auf `start` wäre der nächste Schritt.

## 6. Übernahme in den Wiki-Eintrag

Reihenfolge, die am wenigsten Diskussion braucht:

1. 2.7 Anmeldung (URL je Region, Frist) — beschlossen anmutende Felder, zwölf Events als Beleg.
2. 2.9 Identifier, 2.10 Status — unstrittig, kleine Tags.
3. 2.8 Personen inkl. `organizer:*` und Rollenliste — braucht Vokabular.
4. 2.11 Bildlizenz, 2.12 about/audience — braucht Fallback-Regel bzw. Vokabular auf nocabs.
5. 2.13 Reihen, 5.3 Anmeldezustand — neu, zuerst als Vorschlag in edufeed-app#13.
