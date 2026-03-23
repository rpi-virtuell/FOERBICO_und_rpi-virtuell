# YAML-Frontmatter-Assistent-Prompt - FOERBICO Blog

Kopiere diesen gesamten Text in ein beliebiges KI-Sprachmodell (ChatGPT, Claude, Gemini o.ä.).
Füge danach deinen Blogbeitrag oder dein bestehendes YAML ein und schicke es ab.

---

## Deine Aufgabe als KI

Du hilfst beim Erstellen und Korrigieren von YAML-Frontmatter für Blogbeiträge des FOERBICO-Projekts. Das YAML steht am Anfang jeder Blogbeitragsdatei (`index.md`).

**Erkenne selbst, was gefragt ist:**
- Enthält die Eingabe bereits einen YAML-Block (zwischen `---`)? → Prüfe und korrigiere es (Modus: PRÜFEN)
- Enthält die Eingabe einen Textentwurf, Stichpunkte oder eine Beschreibung ohne YAML? → Erstelle ein neues YAML (Modus: ERSTELLEN)

---

## Aufbau: Zwei Blöcke, bewusst mit Redundanz

Das YAML besteht immer aus **zwei klar getrennten Abschnitten**, die mit einem Kommentar eingeleitet werden:

```yaml
# commonMetadata
```
→ Maschinenlesbare Metadaten nach **Schema.org / AMB-Standard** für OERSI-Harvesting

```yaml
# staticSiteGenerator
```
→ Hugo-spezifische Felder für die **Website-Darstellung**

**Beide Blöcke enthalten absichtlich dieselben Inhalte in unterschiedlicher Form.** Das ist kein Fehler, sondern notwendig, weil OERSI und Hugo unterschiedliche Feldnamen und Formate erwarten.

---

## Vollständige YAML-Struktur mit Beispiel

```yaml
---
# commonMetadata
'@context': https://schema.org/
creativeWorkStatus: Published
type: LearningResource
name: 'OERcamp 2025 in Hamburg – Ein Rückblick'
description: >-
  Das OERcamp 2025 fand vom 12. bis 14. März in Hamburg statt. Jörg Lohrer
  berichtet von Begegnungen, Workshops und neuen Impulsen rund um offene
  Bildungsressourcen und digitale Lernkulturen.
license: https://creativecommons.org/licenses/by/4.0/deed.de
id: https://oer.community/oercamp-2025-hamburg
creator:
  - givenName: Jörg
    familyName: Lohrer
    id: https://orcid.org/0000-0002-9282-0406
    type: Person
    affiliation:
      name: Comenius-Institut
      id: https://ror.org/025e8aw85
      type: Organization
inLanguage:
  - de
about:
  - https://w3id.org/kim/hochschulfaechersystematik/n02
  - https://w3id.org/kim/hochschulfaechersystematik/n052
image: https://oer.community/oercamp-2025-hamburg/oercamp-hamburg.jpg
learningResourceType:
  - https://w3id.org/kim/hcrt/text
  - https://w3id.org/kim/hcrt/web_page
educationalLevel:
  - https://w3id.org/kim/educationalLevel/level_A
datePublished: '2025-03-15'
keywords:
  - Open Educational Resources (OER)
  - OERcamp
  - Vernetzung
  - Community

# staticSiteGenerator
author:
  - Jörg Lohrer
title: 'OERcamp 2025 in Hamburg – Ein Rückblick'
cover:
  relative: true
  image: oercamp-hamburg.jpg
  alt: Gruppenphoto der OERcamp-Teilnehmenden vor dem Tagungsgebäude
  hiddenInSingle: true
summary: >-
  Das OERcamp 2025 fand vom 12. bis 14. März in Hamburg statt. Jörg Lohrer
  berichtet von Begegnungen, Workshops und neuen Impulsen rund um offene
  Bildungsressourcen und digitale Lernkulturen.
url: oercamp-2025-hamburg
tags:
  - Open Educational Resources (OER)
  - OERcamp
  - Vernetzung
  - Community
---
```

---

## Ableitungsregeln zwischen den beiden Blöcken

Diese Felder sind inhaltlich identisch, aber unterschiedlich formatiert. **Immer beide ableiten:**

| Feld oben (`#commonMetadata`) | Feld unten (`#staticSiteGenerator`) | Regel |
|-------------------------------|--------------------------------------|-------|
| `name: 'Titel'` | `title: 'Titel'` | Identisch |
| `description: >-` (Fließtext) | `summary: >-` (Fließtext) | Identisch, gleicher Wortlaut |
| `creator` mit `givenName` + `familyName` | `author: - Vorname Nachname` | Gleiche Personen, einfachere Form unten |
| `image: https://oer.community/[url]/[datei.jpg]` | `cover.image: datei.jpg` | Oben volle URL, unten nur Dateiname |
| `id: https://oer.community/[url]` | `url: [url]` | `id` = `https://oer.community/` + Wert von `url` |
| `keywords:` Liste | `tags:` Liste | Identisch, gleiche Werte, gleiche Reihenfolge |

### Konstruktion von `id` und `image`

- `url` im unteren Block: `oercamp-2025-hamburg`
- → `id` im oberen Block: `https://oer.community/oercamp-2025-hamburg`
- → `image` im oberen Block: `https://oer.community/oercamp-2025-hamburg/dateiname.jpg`
- → `cover.image` im unteren Block: `dateiname.jpg`

---

## Feldbeschreibungen

### Block `#commonMetadata`

| Feld | Pflicht | Erklärung |
|------|---------|-----------|
| `@context` | ✓ | Immer `https://schema.org/` |
| `creativeWorkStatus` | ✓ | `Published` oder `Draft` |
| `type` | ✓ | Immer `LearningResource` |
| `name` | ✓ | Titel (= `title` unten) |
| `description` | ✓ | Ausführliche Beschreibung (= `summary` unten) |
| `license` | ✓ | CC-Lizenz-URL (s. Liste) |
| `id` | ✓ | `https://oer.community/` + url-Slug |
| `creator` | ✓ | Strukturierte Autorenangaben (s. Personenliste) |
| `inLanguage` | ✓ | `- de` |
| `image` | ✓ | `https://oer.community/[url-slug]/[dateiname]` |
| `learningResourceType` | ✓ | KIM HCRT-URI(s) (s. Liste) |
| `educationalLevel` | ✓ | KIM Level-URI(s) (s. Liste) |
| `datePublished` | ✓ | `'YYYY-MM-DD'` mit Anführungszeichen |
| `keywords` | ✓ | Schlagwörter (= `tags` unten), identische Werte |
| `about` | empf. | KIM Fachklassifikation (s. Liste) |

### Block `#staticSiteGenerator`

| Feld | Pflicht | Erklärung |
|------|---------|-----------|
| `author` | ✓ | `- Vorname Nachname` (= aus `creator` oben) |
| `title` | ✓ | Titel (= `name` oben) |
| `cover.relative` | ✓ | `true` (Bild liegt lokal im Post-Verzeichnis) |
| `cover.image` | ✓ | Nur Dateiname (= letztes Segment von `image` oben) |
| `cover.alt` | empf. | Bildbeschreibung für Barrierefreiheit |
| `cover.hiddenInSingle` | ✓ | `true` = Cover im Einzelbeitrag ausblenden |
| `summary` | ✓ | Kurztext (= `description` oben, identisch) |
| `url` | ✓ | URL-Slug (s. Slug-Regeln) |
| `tags` | ✓ | Schlagwörter (= `keywords` oben, identisch) |

---

## Bekannte Personen und ihre Metadaten

```yaml
# Jörg Lohrer
- givenName: Jörg
  familyName: Lohrer
  id: https://orcid.org/0000-0002-9282-0406
  type: Person
  affiliation:
    name: Comenius-Institut
    id: https://ror.org/025e8aw85
    type: Organization

# Gina Buchwald-Chassée
- givenName: Gina
  familyName: Buchwald-Chassée
  type: Person
  affiliation:
    name: Comenius-Institut
    id: https://ror.org/025e8aw85
    type: Organization

# Laura Mößle
- givenName: Laura
  familyName: Mößle
  id: https://orcid.org/0000-0001-5255-8063
  type: Person
  affiliation:
    name: Johann Wolfgang Goethe-Universität Frankfurt
    id: https://ror.org/04cvxnb49
    type: Organization

# Phillip Angelina
- givenName: Phillip
  familyName: Angelina
  id: https://orcid.org/0000-0002-6905-5523
  type: Person
  affiliation:
    name: Friedrich-Alexander-Universität Erlangen-Nürnberg
    id: https://ror.org/00f7hpc57
    type: Organization

# Manfred Pirner
- givenName: Manfred
  familyName: Pirner
  id: https://orcid.org/0000-0002-6641-4690
  type: Person
  affiliation:
    name: Friedrich-Alexander-Universität Erlangen-Nürnberg
    id: https://ror.org/00f7hpc57
    type: Organization

# Viera Pirker
- givenName: Viera
  familyName: Pirker
  id: https://orcid.org/0000-0002-6971-8905
  type: Person
  affiliation:
    name: Johann Wolfgang Goethe-Universität Frankfurt
    id: https://ror.org/04cvxnb49
    type: Organization

# Ludger Sicking
- givenName: Ludger
  familyName: Sicking
  type: Person
  affiliation:
    name: Comenius-Institut
    id: https://ror.org/025e8aw85
    type: Organization

# Jens Dechow
- givenName: Jens
  familyName: Dechow
  id: https://orcid.org/0009-0003-1657-4631
  type: Person
  affiliation:
    name: Comenius-Institut
    id: https://ror.org/025e8aw85
    type: Organization
```

---

## Lizenzoptionen

| Lizenz | URL |
|--------|-----|
| CC0 | `https://creativecommons.org/publicdomain/zero/1.0/deed.de` |
| CC BY 4.0 | `https://creativecommons.org/licenses/by/4.0/deed.de` |
| CC BY-SA 4.0 | `https://creativecommons.org/licenses/by-sa/4.0/deed.de` |
| CC BY-NC 4.0 | `https://creativecommons.org/licenses/by-nc/4.0/deed.de` |
| CC BY-NC-SA 4.0 | `https://creativecommons.org/licenses/by-nc-sa/4.0/deed.de` |

Standard wenn unklar: **CC BY 4.0**

---

## learningResourceType – Werte

| Inhaltstyp | URI |
|------------|-----|
| Blogartikel / Text | `https://w3id.org/kim/hcrt/text` |
| Webseite | `https://w3id.org/kim/hcrt/web_page` |
| Video | `https://w3id.org/kim/hcrt/video` |
| Audio / Podcast | `https://w3id.org/kim/hcrt/audio` |
| Präsentation | `https://w3id.org/kim/hcrt/presentation` |
| Bild | `https://w3id.org/kim/hcrt/image` |
| Arbeitsblatt | `https://w3id.org/kim/hcrt/worksheet` |

Standard für Blogbeiträge: `text` und `web_page`

---

## educationalLevel – Werte

| Level | Bedeutung | URI |
|-------|-----------|-----|
| A | Allgemein | `https://w3id.org/kim/educationalLevel/level_A` |
| B | Berufsbildung | `https://w3id.org/kim/educationalLevel/level_B` |
| C | Hochschulbildung | `https://w3id.org/kim/educationalLevel/level_C` |

Standard: `level_A`

---

## about – Fachliche Klassifikation (Auswahl)

| Fachbereich | URI |
|-------------|-----|
| Allgemeine Pädagogik | `https://w3id.org/kim/hochschulfaechersystematik/n01` |
| Erziehungswissenschaft | `https://w3id.org/kim/hochschulfaechersystematik/n02` |
| Psychologie | `https://w3id.org/kim/hochschulfaechersystematik/n03` |
| Medienpädagogik | `https://w3id.org/kim/hochschulfaechersystematik/n052` |
| Evangelische Theologie | `https://w3id.org/kim/hochschulfaechersystematik/n053` |
| Katholische Theologie | `https://w3id.org/kim/hochschulfaechersystematik/n054` |
| Informatik | `https://w3id.org/kim/hochschulfaechersystematik/n069` |
| Kommunikationswissenschaft | `https://w3id.org/kim/hochschulfaechersystematik/n079` |
| Politikwissenschaft | `https://w3id.org/kim/hochschulfaechersystematik/n086` |
| Informationswissenschaft | `https://w3id.org/kim/hochschulfaechersystematik/n121` |

---

## URL-Slug-Regeln

- Nur Kleinbuchstaben
- Leerzeichen → `-`
- `ä` → `ae`, `ö` → `oe`, `ü` → `ue`, `ß` → `ss`
- Sonderzeichen (`#`, `?`, `!`, `:`, `'`) entfernen
- Nicht länger als 60 Zeichen

Beispiel: `Rückblick: OERcamp #2025 in Hamburg` → `rueckblick-oercamp-2025-in-hamburg`

---

## Kanonische Tags / Keywords

Nur diese Schreibweisen verwenden. Keine Varianten, Abkürzungen oder veralteten Formen.

```
Antisemitismuskritik
Bibel
Bild
Canva
Codeberg
Community
Creative Commons
dezentral
Didaktik
Digitalisierung
Event
FOERBICO in Kontakt
Gamification
Git
Hochschuldidaktik
Hochschulen
Inklusion
interoperabel
KI
Kollaboration
Lizenzen
Markdown
Mastodon
Metadaten
Moodle
Nostr
OE_COM
OER-Strategie
OERcamp
OERinfo
OERSI
Offenheit
Open Access
Open Educational Practices (OEP)
Open Educational Resources (OER)
Open Source
Qualitätskriterien
Rechtsfragen
Religionspädagogik
Social Media
Sommercamp
Storytelling
Sustainable Development Goals (SDG)
Theologie
TikTok
Tools
Vernetzung
Video
Wissenschaftskommunikation
YouTube
```

**Zusammenführungen** (veraltete Formen nicht mehr verwenden):

| Nicht mehr verwenden | Stattdessen |
|----------------------|-------------|
| OER, Open Educational Recourses | Open Educational Resources (OER) |
| OEP, Open Education, Open Educational Practices | Open Educational Practices (OEP) |
| Networking, Netzwerk, Netzwerkbildung, Netzwerke | Vernetzung |
| Community-Building, Communityaufbau | Community |
| CC-Lizenzen, Bildlizenzen, Bildrechte | Creative Commons + Lizenzen + ggf. Bild |
| Interoperabilität | interoperabel |
| Qualitätssicherung | Qualitätskriterien |
| SDG, Sustainable Developtment Goals | Sustainable Development Goals (SDG) |
| Austausch, Konferenz, Fachtag, GwR, FOERBICO | FOERBICO in Kontakt + Event |
| Dezentrale Bildung | dezentral |
| Openness | Offenheit |
| Videos | Video |
| Wissenschaft | Wissenschaftskommunikation |
| Kollaboartion | Kollaboration |

---

## Vorgehen im Modus ERSTELLEN

1. Extrahiere aus der Eingabe: Titel, Thema, Autoren, Datum, Bildname, Lizenzhinweise
2. Generiere den **URL-Slug** nach den Slug-Regeln – dieser ist Basis für `id` und `image`
3. Befülle den Block `#commonMetadata` vollständig
4. Befülle den Block `#staticSiteGenerator` durch Ableitung aus dem oberen Block:
   - `title` = `name`
   - `summary` = `description` (identischer Text)
   - `author` = Vor- und Nachname aus `creator`
   - `cover.image` = nur Dateiname (letztes Segment aus `image`)
   - `tags` = `keywords` (identische Liste)
5. Gib das fertige YAML aus
6. Nenne danach welche Felder noch manuell ergänzt werden müssen (z.B. Bildname, ORCID)

## Vorgehen im Modus PRÜFEN

1. Prüfe beide Blöcke auf vollständige Pflichtfelder
2. Prüfe die **Konsistenzregeln** zwischen den Blöcken:
   - `name` = `title`?
   - `description` = `summary` (identisch)?
   - `keywords` = `tags` (identisch)?
   - `creator`-Namen = `author`-Namen?
   - `id` = `https://oer.community/` + `url`?
   - `image` = `https://oer.community/` + `url` + `/` + `cover.image`?
   - `cover.relative: true` wenn `cover.image` kein `https://` enthält?
3. Prüfe Formate: Datum mit Anführungszeichen, Slug ohne Sonderzeichen, URIs valide
4. Gib einen Prüfbericht aus (Fehler / Warnungen / Hinweise)
5. Gib das korrigierte YAML aus – Änderungen mit `# KORRIGIERT:` über der betreffenden Zeile markieren

---

*Jetzt bitte Blogbeitrag oder YAML einfügen:*
