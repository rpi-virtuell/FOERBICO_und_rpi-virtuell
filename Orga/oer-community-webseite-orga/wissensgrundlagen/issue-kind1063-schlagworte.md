# kind 1063: Schlagworte und Sachgebiete für Lizenznachweise von Bildern

## Anliegen

Die Lizenznachweise für hochgeladene Dateien (kind `1063`, siehe Wiki *License events for uploaded files in NOPE/edufeed*) tragen inzwischen eine vollständige Bildattribution: `license`, `credit`, `title`, `alt`, `source`, `authorUrl`, `ai`, `ai-tool`, `ai-training`. Dadurch entsteht auf den edufeed-Relays nebenbei eine wachsende Sammlung frei lizenzierter Bilder, die über den Hash eindeutig und mit Nachweis nutzbar sind.

Was fehlt, ist jede Form von **Erschließung**: Alle 211 kind-1063-Events des FOERBICO-Keys auf fünf Relays (12.10.2026, 199 eindeutige Bilder) enthalten kein einziges `t`-Tag und kein Vokabular-Attribut. Ein Bild ist heute nur auffindbar, wenn man seinen Hash oder die Seite kennt, in der es verwendet wird. Für eine künftige Bilddatenbank (Suche nach „Kirche“, „Barcamp“, Fach „Religion“, Bildungsstufe „Fortbildung“) reicht das nicht; `alt` und `title` sind Freitext und werden von Relays nicht indexiert.

**Frage:** Soll kind 1063 in NOPE um Schlagworte und Sachgebiete erweitert werden, und wenn ja, mit welchen Tags?

**Vorschlag:** Ja, additiv und optional, mit genau den Konventionen, die bei kind `30142` (NIP-AMB) und kind `31923` (Calendar, `educationalLevel:*`) schon gelten. Keine neuen Tag-Namen erfinden, wenn es dafür bereits eine übergreifende Lösung gibt.

## Rahmenbedingungen

- kind 1063 ist ein **reguläres, nicht ersetzbares Event**. Nachträgliches Verschlagworten heißt: ein neues 1063 mit demselben `x` veröffentlichen, das alle bisherigen Lizenz-Tags mitführt. Die Auflösungsregel aus dem Wiki (neuestes `created_at` gewinnt) deckt das bereits ab.
- Jeder Pubkey darf für jeden Hash attestieren. Schlagworte von Dritten sind damit technisch möglich, werfen aber die Vertrauensfrage auf (siehe offene Punkte).
- Relays indexieren nur einbuchstabige Tag-Namen. Nur solche Tags sind serverseitig filterbar (`#t`); mehrbuchstabige (`about:id`) werden clientseitig gefiltert, genau wie heute bei `educationalLevel:id` im Kalender.
- NIP-94 selbst kennt keine Schlagworte. NIP-24 definiert `t` aber kind-übergreifend als Hashtag (Wert zwingend lowercase), und NIP-68 (kind 20, Bild-Feeds) nutzt `t` für Bilder. Der `amb-nostr-converter` bildet AMB `keywords` bereits auf `t` ab.

## Lösungsvorschlag

### A. Freie Schlagworte: `t` (sofort umsetzbar)

```
["t", "barcamp"]
["t", "metadaten"]
["t", "holzbausteine"]
```

Regeln:

- Ein Schlagwort je Tag, beliebig oft wiederholt. Wert lowercase (NIP-24), ohne führendes `#`, Umlaute erlaubt (`kirche`, `fortbildung`, `grundschule`).
- Entspricht AMB `keywords` und damit demselben Tag wie auf kind 30142, 30023 und 3192x. Ein Client, der `t` dort liest, liest es hier genauso.
- Relay-Filter funktioniert ohne Erweiterung: `{"kinds":[1063], "#t":["barcamp"]}`.
- Kein Sprachmarker. Wer mehrsprachig erschließen will, setzt mehrere `t`-Tags (`kirche`, `church`).
- Leseregel: Duplikate einmal lesen, unbekannte Tags ignorieren, kein `t` heißt „nicht erschlossen“.

### B. Kontrollierte Sachgebiete: `about:*` (AMB-Flattening wie bei `educationalLevel`)

Für die Fachzuordnung wird nicht `t` zweckentfremdet, sondern das AMB-Feld `about` mit dem bereits vereinbarten Konzept-Tripel geschrieben, eine Gruppe je Konzept, Gruppen zusammenhängend:

```
["about:id", "http://w3id.org/kim/schulfaecher/s1055"]
["about:prefLabel:de", "Religion"]
["about:type", "Concept"]
["about:id", "https://w3id.org/kim/hochschulfaechersystematik/n052"]
["about:prefLabel:de", "Erziehungswissenschaft (Pädagogik)"]
["about:type", "Concept"]
```

- `:id` ist maßgeblich, `:prefLabel:<lang>` Anzeigekopie, Fallback letztes URI-Segment. Dieselben Leseregeln wie im Calendar-Wiki.
- Vokabulare: KIM `schulfaecher` und `hochschulfaechersystematik`, also die SKOS-Schemata (kind 39737), die das Fach-Feld des 30142-Formulars schon lädt. Kein neues Vokabular nötig.
- Optional nach derselben Regel: `educationalLevel:*` (für wen ist das Bild gedacht). Für Bilder zweitrangig, aber kostenlos, weil Vokabular und Parser existieren.

### C. Später, nicht Teil dieses Issues

- **Bildart** (Foto, Illustration, Icon, Diagramm, Screenshot, Logo): Dafür gibt es noch kein vereinbartes Vokabular. Übergangsweise als `t` (`foto`, `illustration`), später ggf. als `learningResourceType:*` oder eigenes Konzept.
- **Fremd-Verschlagwortung ohne Re-Attestierung**: NIP-32-Labels (kind 1985) mit `e`-Tag auf das 1063-Event wären der saubere Weg, damit andere ein Bild erschließen können, ohne den Lizenznachweis neu zu veröffentlichen. Erst sinnvoll, wenn es mehr als einen tagenden Akteur gibt.
- **Textsprache im Bild**: `["L","ISO-639-1"]`, `["l","de","ISO-639-1"]` wie in NIP-68, nur wenn Text im Bild steht.

## Beispiel (bestehendes FOERBICO-Event, erweitert)

```json
{
  "kind": 1063,
  "content": "",
  "tags": [
    ["url", "https://blossom.edufeed.org/0e857e78…0854.jpg"],
    ["x", "0e857e7892b60f5786bd00327d2e21f7de4c49e9575dc5d14ac59144761f0854"],
    ["m", "image/jpeg"],
    ["size", "1324280"],
    ["title", "Metadaten"],
    ["alt", "Holzbausteine, die das Wort „Metadaten“ bilden"],
    ["license", "https://unsplash.com/de/lizenz"],
    ["credit", "Markus Winkler"],
    ["authorUrl", "https://unsplash.com/de/@markuswinkler"],
    ["source", "https://unsplash.com/de/fotos/…-9DZsVF-qLaY"],

    ["t", "metadaten"],
    ["t", "holzbausteine"],
    ["t", "symbolbild"],
    ["about:id", "https://w3id.org/kim/hochschulfaechersystematik/n079"],
    ["about:prefLabel:de", "Informatik"],
    ["about:type", "Concept"]
  ]
}
```

Abfragen:

```json
{"kinds":[1063], "#t":["metadaten"]}
{"kinds":[1063], "#m":["image/jpeg","image/png","image/webp"]}
```

Die zweite Abfrage plus clientseitiger Filter auf `about:id` liefert „alle Bilder zum Fach X“; sobald das Relay mehrbuchstabige Tag-Namen indexiert (offener Punkt aus dem Calendar-Wiki), geht das serverseitig.

## Umsetzung (Vorschlag)

1. **Wiki `license-events-nope`** um einen Abschnitt „Erschließung“ ergänzen: `t` und `about:*` als optionale Tags in die Tabelle, Leseregeln, Abfragebeispiel.
2. **edufeed-app, Upload-Dialog**: Feld „Schlagworte“ (Chips, lowercase normalisiert) und Fach-Picker aus dem 30142-Formular wiederverwenden. Beim Nachbearbeiten eines fremden 1063 nur die eigenen Formular-Tags ersetzen, alles andere erhalten (dieselbe Regel wie bei Kalender-Events).
3. **edufeed-app, Lesen**: Bilder-Ansicht bzw. Medienauswahl nach `t` filtern; Badge für `about`.
4. **FOERBICO-Pipeline (`md2blossom`/`mdparser`)**: Im `# bilder`-Block zwei optionale Felder `keywords:` (Liste → `t`) und `about:` (Liste von Konzept-URIs → Tripel, Labels aus dem SKOS-Schema). Nicht `tags:` nennen, das ist in Hugo das Schlagwortfeld des Beitrags.
5. **Bestand**: Vorhandene 1063 bleiben gültig. Nachträgliche Erschließung durch erneutes Prägen unter demselben `x` mit allen bisherigen Tags.

## Zu entscheiden

- [ ] `t` für freie Schlagworte übernehmen (lowercase, kein Sprachmarker)?
- [ ] `about:*` mit KIM-Fächervokabularen als Sachgebiet, `educationalLevel:*` optional dazu?
- [ ] Leseregel bei mehreren 1063 je Hash: nur „neuestes gewinnt“ (wie Lizenz) oder Vereinigung der `t`/`about` aller vertrauenswürdigen Attestierer?
- [ ] Bildart und Fremd-Verschlagwortung (NIP-32) auf Follow-up vertagen?

## Nebenbefund

`ai-tool` nutzt bereits eine Vokabular-Referenz, aber in anderer Form (`["ai-tool", "<Label>", "<URI>"]`, zwei Slots) als das AMB-Tripel. Bei der Entscheidung zu B sollte festgehalten werden, dass neue Vokabular-Attribute auf 1063 dem Tripel folgen; `ai-tool` kann als dokumentierte Ausnahme bleiben.

## Quellen

- Wiki *License events for uploaded files in NOPE/edufeed* (d: `license-events-nope`)
- Wiki *Calendar events in edufeed* (d: `edufeed-calendar-event-tags`), Abschnitt Bildungsstufe und „Open follow-ups“
- NIP-24 (`t` kind-übergreifend, lowercase), NIP-68 (`t` auf Bild-Events), NIP-94
- `amb-nostr-converter.esm.js` in edufeed-examples: `keywords` → `t`, `about` → `about:id`/`about:prefLabel:<lang>`/`about:type`
- FOERBICO `bildattribution.md` (Abbildung `# bilder`-Block → 1063-Tags)
