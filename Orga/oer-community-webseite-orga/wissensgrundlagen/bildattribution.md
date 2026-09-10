# Strukturierte Bild-Metadaten und Konvention zur Bildattribution 

### Zuordnung im Beispiel

| Feld | Wert |
|---|---|
| `alt` | Rhabarberpflanze mit großen grünen Blättern und roten Stielen in einem Gartenbeet mit Mulch |
| `imageUrl` | https://inaturalist-open-data.s3.amazonaws.com/photos/71812633/medium.jpg |
| `title` | garden rhubarb, Speise-Rhabarber |
| `sourceUrl` | https://www.inaturalist.org/photos/71812633 |
| `author` | John Sankey |
| `authorUrl` | https://www.inaturalist.org/users/2831535 |
| `licence` | CC BY-SA 4.0 |
| `licenceUrl` | https://creativecommons.org/licenses/by-sa/4.0/ |
| `modification` | beschnitten |


### Markdown-Darstellung im Beispiel

```markdown=
![Rhabarberpflanze mit großen grünen Blättern und roten Stielen in einem Gartenbeet mit Mulch](https://inaturalist-open-data.s3.amazonaws.com/photos/71812633/medium.jpg)
[garden rhubarb, Speise-Rhabarber](https://www.inaturalist.org/photos/71812633), [John Sankey](https://www.inaturalist.org/users/2831535), [CC0](https://creativecommons.org/publicdomain/zero/1.0/), beschnitten
```

![Rhabarberpflanze mit großen grünen Blättern und roten Stielen in einem Gartenbeet mit Mulch](https://inaturalist-open-data.s3.amazonaws.com/photos/71812633/medium.jpg)
[garden rhubarb, Speise-Rhabarber](https://www.inaturalist.org/photos/71812633), [John Sankey](https://www.inaturalist.org/users/2831535), [CC0](https://creativecommons.org/publicdomain/zero/1.0/), beschnitten

### Konstruktion des Markdown-Beispiels
```markdown
![alt](imageUrl)
[title](sourceUrl), [author](authorUrl), [licence](licenceUrl), KI-Kennzeichnung, modification
```
Die Caption-Zeile steht **auf der Zeile direkt nach dem Bild** (Zeilenumbruch, kein Leerzeichen dazwischen). Die KI-Kennzeichnung (`KI-generiert` oder `KI-verändert`, aus dem Feld `ai`) steht nur, wenn KI beteiligt war, und dann direkt hinter der Lizenz.

## Regeln
1. **Reihenfolge der Felder:** `alt`, `imageUrl`, `title`, `sourceUrl`, `author`, `authorUrl`, `licence`, `licenceUrl`, `modification`, `ai`. Die Reihenfolge ist **normativ**, damit Parser sich darauf verlassen können. In der Caption steht die KI-Kennzeichnung aus `ai` **vor** `modification`, direkt hinter der Lizenz (edufeed-Wiki: „AI-Marke neben dem Lizenz-Badge“).
2. **Trenner:** Komma + Leerzeichen (`, `) zwischen den Caption-Feldern. Einheitlich, kein Mix aus „von", „Autor", „Lizenz", usw.
3. **Verlinkungen:**
   - `title` → `sourceUrl`
   - `author` → `authorUrl`
   - `licence` → `licenceUrl`
4. **URL-Disziplin:** Alle URL-Felder sind absolut (`https://…`), niemals relativ.
5. **CC0 / Public Domain:** `sourceUrl` darf entfallen. Urheber:in und Lizenz bleiben aus Transparenzgründen empfohlen.
6. **Bearbeitungen:** Bei CC-BY-Lizenzen ist die Änderung anzugeben, sobald das Werk verändert wurde (Zuschnitt, Farbe, Skalierung, Kombination usw.). Bei CC0 optional.
7. **Barrierefreiheit:** `alt` ist formal optional, aber für WCAG/BITV-Konformität faktisch Pflicht. Leere eckige Klammern `![]` nur bei rein dekorativen Bildern.
8. **KI-Beteiligung:** `ai: generated` für vollständig KI-generierte Bilder (menschlich ist nur der Prompt), `ai: modified` für bestehende, von Menschen gemachte Bilder, die mit KI teilweise verändert wurden. Genau diese zwei Werte, höchstens einmal je Bild; sie folgen den Icons des EU AI Office für die Kennzeichnung nach EU AI Act (edufeed-Wiki `license-events-nope`, Fassung 2026-09-10). Kein `ai` heißt „nicht deklariert“, **nicht** „ohne KI“. Die Kennzeichnung ersetzt weder Lizenz noch Urheber:in: `author` nennt, wer geprompt oder bearbeitet hat.

## (Pflicht)-Felder

| Feld | Status | Bedeutung / Form |
|---|---|---|
| `licence` | **Pflicht** | Lizenz-Kurzform (`CC0`, `CC BY`, `CC BY-SA`, `©`, …) |
| `licenceUrl` | **Pflicht** | Kanonische Lizenz-URL, z. B. `https://creativecommons.org/publicdomain/zero/1.0/` |
| `imageUrl` | **Pflicht** | Absolute URL zur Bilddatei (sonst nicht renderbar) |
| `sourceUrl` | **Pflicht** außer bei CC0 | URL zur Quellseite|
| `author` | **Pflicht** außer bei CC0 | Name der Urheber:in |
| `authorUrl` | optional | Profil-/Homepage-URL der Urheber:in |
| `modification` | optional (Pflicht bei Bearbeitung von CC-BY-Werken) | Freitext zur Bearbeitung |
| `title` | optional | Titel des Werks |
| `alt` | optional (faktisch Pflicht für Accessibility) | Screen-Reader-Beschreibung |
| `ai` | optional (Pflicht bei KI-Beteiligung) | `generated` oder `modified`, sonst weglassen (Regel 8) |


### Minimale Beispieldarstellung
![](https://inaturalist-open-data.s3.amazonaws.com/photos/71812633/medium.jpg)
[CC0](https://creativecommons.org/publicdomain/zero/1.0/)

### Minimale Beispiel-Konstruktion
```markdown
![](imageUrl)
[licence](licenceUrl)
```
Die harte Mindestanforderung: **Bild + Lizenz-Link**. Alles andere darf weg, wenn es die Lizenz erlaubt (z. B. CC0).

## Der `# bilder`-Block im Frontmatter

Dieselben Feldnamen stehen als dritter markierter Block im Frontmatter von `index.md`, nach `# commonMetadata` und `# staticSiteGenerator`. Schlüssel ist der Dateiname im Beitragsordner oder, nach der Migration, die Blossom-Hash-URL. Der Block ist **Eingabe zum Prägen**: Aus ihm entsteht je Bild ein Lizenznachweis (`kind:1063`) unter dem FOERBICO-Key; das Event auf dem Relay ist die Wahrheit. Ableitbares (`imageUrl`, SHA-256, MIME, Größe) steht nicht im Block, das rechnet `md2blossom` bzw. `mdparser/sync` aus der Datei.

```yaml
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
bilder:
  Gina-OERcamp.jpeg:
    alt: Gina Buchwald-Chassée sitzt vor der OERcamp-Fotowand und zeigt den Daumen hoch.
    title: Gina beim OERcamp 2026
    sourceUrl: https://oer.community/oercamp-2026
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
  Canva-OER-KI-generiert.jpg:
    alt: "Illustration eines Laptops über einem aufgeschlagenen Buch, umgeben von Symbolen zu OER."
    title: Canva als Tool für OER?
    sourceUrl: https://oer.community/canva
    author: FOERBICO
    authorUrl: https://oer.community
    licence: CC BY 4.0
    licenceUrl: https://creativecommons.org/licenses/by/4.0/
    ai: generated
```

Abbildung auf die Tags des `kind:1063` (edufeed-kompatibel, FOERBICO-Zusatzfelder ohne NIP-Standard):

| Block | 1063-Tag | Herkunft |
|---|---|---|
| Schlüssel | `url`, `x`, `m`, `size` | aus der Datei berechnet |
| `title` | `title` | |
| `author` | `credit` | |
| `authorUrl` | `authorUrl` | Zusatzfeld |
| `licenceUrl` | `license` | |
| `sourceUrl` | `source` | |
| `alt` | `alt` | |
| `modification` | `modification` | Zusatzfeld |
| `pubkey` | `p` | optional |
| `ai` | `ai` | `generated` \| `modified`; anderer Wert → kein Tag (edufeed-Wiki 2026-09-10) |

Im Fließtext schreibt `md2blossom` aus dem Block die Caption-Zeile nach der Konstruktion oben direkt unter das Bild. Eigene Fotos folgen der Footer-Regel von oer.community (CC BY FOERBICO, `sourceUrl` = der Beitrag); fremde Werke tragen Urheber:in, Quelle und deren Lizenz. Was nicht frei lizenziert werden darf, bekommt keinen Eintrag und damit keinen Nachweis.

## Stolpersteine beim händischen Bearbeiten des Blocks

Der Block ist YAML und Teil des Hugo-Frontmatters. Ein Tippfehler bricht **den ganzen Website-Build**, nicht nur das eine Bild. Hugo meldet dann in der CI z. B. `mapping value is not allowed in this context` mit Zeile und Spalte. Was am häufigsten schiefgeht:

1. **Doppelpunkt + Leerzeichen im Text.** `alt: … mit dem Hinweis „Ausweis: Canva-Lizenz“ …` ist ungültig, weil YAML `Ausweis: ` als neues Feld liest. Lösung: den ganzen Wert in doppelte Anführungszeichen setzen:
   ```yaml
   alt: "Dreiteilige Grafik … mit dem Hinweis „Ausweis: Canva-Lizenz“ …"
   ```
   Dasselbe gilt für Titel wie `Canva für OER: Eine Entscheidungshilfe`. Ein Doppelpunkt **ohne** Leerzeichen danach (`https://…`, `12:30`) ist unproblematisch.
2. **Anführungszeichen im Wert.** Typografische `„…“` sind in einem in `"…"` eingefassten Wert erlaubt. Kommt ein gerades `"` im Text vor, den Wert stattdessen in einfache Anführungszeichen setzen; ein Apostroph darin wird verdoppelt (`'Ginas ''Tipp'''`).
3. **`#` im Text.** Leerzeichen + Raute beginnt einen Kommentar und schneidet den Rest der Zeile ab. Werte mit Raute in Anführungszeichen setzen.
4. **Einrückung.** Nur Leerzeichen, keine Tabs. Der Dateiname steht mit 2 Leerzeichen unter `bilder:`, seine Felder mit 4. Eine Zeile, die um ein Leerzeichen abweicht, gehört zum falschen Eintrag oder bricht den Block.
5. **Werte, die wie andere Typen aussehen.** `licence: CC BY 4.0` ist Text, gut. Ein Wert nur aus Ziffern, aus `ja`/`nein`/`true`/`false` oder ein Datum wird von YAML umgedeutet; im Zweifel in Anführungszeichen.
6. **Schlüssel = exakter Dateiname.** Groß-/Kleinschreibung und Endung müssen zur Datei im Ordner passen (`Foto.JPG` ≠ `foto.jpg`), sonst findet weder md2blossom noch die CI den Eintrag.
7. **`ai` ist ein eigenes Feld, keine Liste.** Richtig ist `ai: generated` oder `ai: modified`. Nicht `tags: ["ai", "generated"]`: `tags` bedeutet in Hugo die Schlagwörter des Beitrags, und die Werkzeuge suchen nach `ai`.
8. **Platz des Blocks.** Nach dem `# staticSiteGenerator`-Block, vor dem schließenden `---`. Die Markerzeile `# bilder …` ist ein Kommentar und muss so stehen bleiben, die Werkzeuge erkennen den Block daran.

**Vor dem Speichern prüfen:** Wer lokal arbeitet, baut mit `hugo -s Website -d /tmp/probe --logLevel error`; wer im Forgejo-Webeditor arbeitet, kopiert den Block vorher in einen YAML-Prüfer (z. B. yamllint.com). Ein Doppelpunkt mit Leerzeichen in einem unquotierten Wert ist immer ein Fehler.
