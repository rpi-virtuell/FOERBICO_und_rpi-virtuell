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
[title](sourceUrl), [author](authorUrl), [licence](licenceUrl), modification
```
Die Caption-Zeile steht **auf der Zeile direkt nach dem Bild** (Zeilenumbruch, kein Leerzeichen dazwischen).

## Regeln
1. **Reihenfolge der Felder:** `alt`, `imageUrl`, `title`, `sourceUrl`, `author`, `authorUrl`, `licence`, `licenceUrl`, `modification`. Die Reihenfolge ist **normativ**, damit Parser sich darauf verlassen können.
2. **Trenner:** Komma + Leerzeichen (`, `) zwischen den Caption-Feldern. Einheitlich, kein Mix aus „von", „Autor", „Lizenz", usw.
3. **Verlinkungen:**
   - `title` → `sourceUrl`
   - `author` → `authorUrl`
   - `licence` → `licenceUrl`
4. **URL-Disziplin:** Alle URL-Felder sind absolut (`https://…`), niemals relativ.
5. **CC0 / Public Domain:** `sourceUrl` darf entfallen. Urheber:in und Lizenz bleiben aus Transparenzgründen empfohlen.
6. **Bearbeitungen:** Bei CC-BY-Lizenzen ist die Änderung anzugeben, sobald das Werk verändert wurde (Zuschnitt, Farbe, Skalierung, Kombination usw.). Bei CC0 optional.
7. **Barrierefreiheit:** `alt` ist formal optional, aber für WCAG/BITV-Konformität faktisch Pflicht. Leere eckige Klammern `![]` nur bei rein dekorativen Bildern.

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


### Minimale Beispieldarstellung
![](https://inaturalist-open-data.s3.amazonaws.com/photos/71812633/medium.jpg)
[CC0](https://creativecommons.org/publicdomain/zero/1.0/)

### Minimale Beispiel-Konstruktion
```markdown
![](imageUrl)
[licence](licenceUrl)
```
Die harte Mindestanforderung: **Bild + Lizenz-Link**. Alles andere darf weg, wenn es die Lizenz erlaubt (z. B. CC0).