# OpenEduHub + AMB: Religionspädagogisches Metadaten-Mapping
**Version 2.0 - AMB-konform**

*Vollständiges Mapping mit 28 OpenEduHub-Vokabularen, KIM-Standards und AMB-Compliance*

---

## 📋 Dokumentenübersicht

**Erstellt:** 13. Oktober 2025  
**Basis:** 
- AMB (Allgemeines Metadatenprofil für Bildungsressourcen) v20231019
- OpenEduHub Vokabulare (28 Vokabulare, 352K)
- KIM educationalLevel + HCRT
- Kompendium „Religionspädagogische Materialientwicklung, Kuration und Publikation"

**Ziel:** AMB-konforme Metadaten für religionspädagogische Bildungsressourcen mit maximal präziser Zuordnung zu Standardvokabularen

---

## 1. AMB Pflichtfelder (Minimale Compliance)

### 1.1 Grundstruktur

```json
{
  "@context": "https://w3id.org/kim/amb/context.jsonld",
  "id": "https://example.org/resource/rup-001",
  "name": "Gleichnisse Jesu verstehen",
  "type": ["LearningResource"]
}
```

**Pflichtfelder:**
| Feld | Typ | Beschreibung | Beispiel |
|------|-----|--------------|----------|
| `@context` | URI | AMB JSON-LD Kontext | `https://w3id.org/kim/amb/context.jsonld` |
| `id` | URI | Eindeutige Ressourcen-ID | DOI, Handle, URL |
| `name` | String/LocalizedString | Titel der Ressource | "Gleichnisse Jesu verstehen" |
| `type` | Array[String] | MUSS "LearningResource" enthalten | `["LearningResource"]` |

---

## 2. learningResourceType (AMB-VALIDIERT)

### 2.1 AMB-Anforderung
**JSON Schema Pattern:**
```regex
(^http://w3id.org/openeduhub/vocabs/new_lrt/.*|^https://w3id.org/kim/hcrt/.*)
```

### 2.2 Religionspädagogische Ressourcentypen → OpenEduHub new_lrt

#### 2.2.1 Dokumente und Texte

| Religionspäd. Typ | OpenEduHub new_lrt URI | Definition |
|-------------------|------------------------|------------|
| **Bibeltext** | `http://w3id.org/openeduhub/vocabs/new_lrt/ab5b99ea-551c-42f3-995b-e4b5f469ad7e` | Primärmaterial (biblische Quelle) |
| **Glaubenszeugnis** | `http://w3id.org/openeduhub/vocabs/new_lrt/ab5b99ea-551c-42f3-995b-e4b5f469ad7e` | Primärmaterial (persönliches Zeugnis) |
| **Kirchliches Dokument** | `http://w3id.org/openeduhub/vocabs/new_lrt/776652a6-de35-4d2f-817e-6130dd2fa248` | Handbuch, Dokumentation und Regularien |
| **Theologischer Fachartikel** | `http://w3id.org/openeduhub/vocabs/new_lrt/b98c0c8c-5696-4537-82fa-dded7236081e` | Artikel und Einzelpublikation |
| **Katechismus** | `http://w3id.org/openeduhub/vocabs/new_lrt/776652a6-de35-4d2f-817e-6130dd2fa248` | Handbuch, Dokumentation |
| **Bibelkommentar** | `http://w3id.org/openeduhub/vocabs/new_lrt/c022c920-c236-4234-bae1-e264a3e2bdf6` | Nachschlagewerk |
| **Lexikoneintrag (Religion)** | `http://w3id.org/openeduhub/vocabs/new_lrt/c022c920-c236-4234-bae1-e264a3e2bdf6` | Nachschlagewerk und Glossareintrag |

#### 2.2.2 Unterrichtsplanung

| Religionspäd. Typ | OpenEduHub new_lrt URI | Definition |
|-------------------|------------------------|------------|
| **Religionsunterricht (Stundenentwurf)** | `http://w3id.org/openeduhub/vocabs/new_lrt/0d23ff13-9d92-4944-92fa-2b5fe1dde80b` | Stundenentwurf |
| **Unterrichtsreihe Religion** | `http://w3id.org/openeduhub/vocabs/new_lrt/962560fe-d8d0-43e2-ad60-97f070b935c6` | Unterrichtsreihe (mehrere Wochen) |
| **Unterrichtseinheit Religion** | `http://w3id.org/openeduhub/vocabs/new_lrt/ef58097d-c1de-4e6a-b4da-6f10e3716d3d` | Unterrichtseinheit und -sequenz |
| **Unterrichtsbaustein Religion** | `http://w3id.org/openeduhub/vocabs/new_lrt/5098cf0b-1c12-4a1b-a6d3-b3f29621e11d` | Unterrichtsbaustein |
| **Go & Teach (Komplett)** | `http://w3id.org/openeduhub/vocabs/new_lrt/6ed79b37-c27c-4f53-9921-fb1a96da7160` | Go & Teach (vollständig ausgearbeitet) |

#### 2.2.3 Material und Medien

| Religionspäd. Typ | OpenEduHub new_lrt URI | Definition |
|-------------------|------------------------|------------|
| **Arbeitsblatt (Religion)** | `http://w3id.org/openeduhub/vocabs/new_lrt/36e68792-6159-481d-a97b-2c00901f4f78` | Arbeitsblatt |
| **Religiöse Kunst/Ikonographie** | `http://w3id.org/openeduhub/vocabs/new_lrt/e3ddae8a-d94c-40d8-b7f7-9bdaf0cb8325` | Gemälde, Kunstwerke und Zeichnungen |
| **Foto (religiös)** | `http://w3id.org/openeduhub/vocabs/new_lrt/f9630e1c-2247-42ed-87b0-b1e18e4ec02b` | Foto |
| **Erklärvideo (Religion)** | `http://w3id.org/openeduhub/vocabs/new_lrt/a0218a48-a008-4975-a62a-27b1a83d454f` | Erklärvideo und gefilmtes Experiment |
| **Meditation/Gebet (Audio)** | `http://w3id.org/openeduhub/vocabs/new_lrt/5dc0b5de-4c75-43aa-8366-fb6d7e3a7553` | Sprach- und Lernaudio |
| **Kirchenmusik** | `http://w3id.org/openeduhub/vocabs/new_lrt/9c23511c-73d0-407b-b443-c93e36364de2` | Musik |
| **Psalmen/Gebete (Audio)** | `http://w3id.org/openeduhub/vocabs/new_lrt/78cc5a71-5ae2-4fa3-be5f-5cef40c23328` | Klang und Tonaufnahme |

#### 2.2.4 Methoden und Aktivitäten

| Religionspäd. Typ | OpenEduHub new_lrt URI | Definition |
|-------------------|------------------------|------------|
| **Bibelgespräch (Methode)** | `http://w3id.org/openeduhub/vocabs/new_lrt/477115fd-5042-4174-ac39-7c05f8a24766` | Pädagogische Methode, Konzept |
| **Stilleübung** | `http://w3id.org/openeduhub/vocabs/new_lrt/477115fd-5042-4174-ac39-7c05f8a24766` | Pädagogische Methode |
| **Bodenb ild** | `http://w3id.org/openeduhub/vocabs/new_lrt/b0495f44-b05d-4bde-9dc5-34d7b5234d76` | Lernspiel |
| **Kirchenraumführung** | `http://w3id.org/openeduhub/vocabs/new_lrt/1cac68e6-dafe-4ce4-a52f-f33cde26da59` | Recherche- und Lernauftrag |
| **Rollenspiel (biblisch)** | `http://w3id.org/openeduhub/vocabs/new_lrt/ac82dc13-3be1-464d-9cdc-88e608d99c39` | Rollenspiel (Lehr- und Lernmaterial) |
| **Bibliolog** | `http://w3id.org/openeduhub/vocabs/new_lrt/477115fd-5042-4174-ac39-7c05f8a24766` | Pädagogische Methode |
| **Bildbetrachtung** | `http://w3id.org/openeduhub/vocabs/new_lrt/68a43516-889e-4ce9-8e03-248307bd99ff` | Offene und kreative Aktivität |

#### 2.2.5 Interaktive Medien

| Religionspäd. Typ | OpenEduHub new_lrt URI | Definition |
|-------------------|------------------------|------------|
| **Interaktive Bibel-App** | `http://w3id.org/openeduhub/vocabs/new_lrt/e5ed8ec2-2c7e-4f46-aba9-e67148ef6656` | Lern-App |
| **Bibelquiz** | `http://w3id.org/openeduhub/vocabs/new_lrt/7d591b84-9171-47cb-809a-74ef07f07261` | Quiz |
| **Virtual Church Tour** | `http://w3id.org/openeduhub/vocabs/new_lrt/518ae9d5-2420-4567-b32d-f75c27e2cf70` | Augmented Reality |
| **Simulation (religiös)** | `http://w3id.org/openeduhub/vocabs/new_lrt/2e4157ad-e29a-4f10-b4e6-370e0fd59d26` | Simulation |

#### 2.2.6 Test und Assessment

| Religionspäd. Typ | OpenEduHub new_lrt URI | Definition |
|-------------------|------------------------|------------|
| **Selbsttest (Religion)** | `http://w3id.org/openeduhub/vocabs/new_lrt/29f0d682-38c6-4a64-a1fa-04e673c28128` | Selbst-Testaufgabe |
| **Klausur (Religion)** | `http://w3id.org/openeduhub/vocabs/new_lrt/9cf3c183-f37c-4b6b-8beb-65f530595dff` | Klausur, Klassenarbeit und Test |
| **Erwartungshorizont** | `http://w3id.org/openeduhub/vocabs/new_lrt/7c236821-bfae-4eeb-bc79-590bf8ea1d96` | Lösungs(beispiel) und Erwartungshorizont |

### 2.3 Beispiel: AMB-konform mit Erweiterung

```json
"learningResourceType": [
  {
    "id": "http://w3id.org/openeduhub/vocabs/new_lrt/0d23ff13-9d92-4944-92fa-2b5fe1dde80b",
    "prefLabel": {"de": "Stundenentwurf", "en": "Lesson plan"}
  },
  {
    "id": "https://w3id.org/relipaed/ressourcentyp/religionsunterricht-stundenentwurf",
    "prefLabel": {"de": "Religionsunterricht (Stundenentwurf)"},
    "broadMatch": ["http://w3id.org/openeduhub/vocabs/new_lrt/0d23ff13-9d92-4944-92fa-2b5fe1dde80b"]
  }
]
```

---

## 3. educationalLevel (AMB-VALIDIERT)

### 3.1 AMB-Anforderung
**JSON Schema Pattern:**
```regex
(^https://w3id.org/kim/educationalLevel/.*)
```

**NUR KIM educationalLevel erlaubt!**

### 3.2 Religionsunterricht → KIM educationalLevel

| Bildungsstufe | KIM URI | ISCED | Alter |
|---------------|---------|-------|-------|
| **Kindergarten/Kita** | `https://w3id.org/kim/educationalLevel/level_0` | Level 0 | 3-6 Jahre |
| **Grundschule** | `https://w3id.org/kim/educationalLevel/level_1` | Level 1 | 6-10 Jahre |
| **Sekundarstufe I** | `https://w3id.org/kim/educationalLevel/level_2` | Level 2 | 10-16 Jahre |
| **Sekundarstufe II** | `https://w3id.org/kim/educationalLevel/level_3` | Level 3 | 16-19 Jahre |
| **Berufsschule** | `https://w3id.org/kim/educationalLevel/level_4` | Level 4 | 16+ Jahre |
| **Hochschule (allgemein)** | `https://w3id.org/kim/educationalLevel/level_A` | Level 5-8 | 18+ Jahre |
| **Bachelor (Theologie)** | `https://w3id.org/kim/educationalLevel/level_6` | Level 6 | 18-21 Jahre |
| **Master (Theologie)** | `https://w3id.org/kim/educationalLevel/level_7` | Level 7 | 21-23 Jahre |
| **Promotion (Theologie)** | `https://w3id.org/kim/educationalLevel/level_8` | Level 8 | 23+ Jahre |
| **Referendariat (Lehramt Religion)** | `https://w3id.org/kim/educationalLevel/level_B` | - | 24-26 Jahre |
| **Fortbildung (Religionslehrkräfte)** | `https://w3id.org/kim/educationalLevel/level_C` | - | 25+ Jahre |

### 3.3 Beispiel

```json
"educationalLevel": [
  {
    "id": "https://w3id.org/kim/educationalLevel/level_2",
    "prefLabel": {
      "de": "Sekundarbereich I",
      "en": "Lower secondary education"
    },
    "altLabel": {
      "de": ["Sekundarstufe I", "ISCED 2011, Level 2"]
    }
  }
]
```

---

## 4. about (Fach/Thema)

### 4.1 AMB-Anforderung
**JSON Schema Pattern:**
```regex
(^https://w3id.org/kim/hochschulfaechersystematik/.*|http://w3id.org/kim/schulfaecher/.*)
```

### 4.2 Fach: Religion

**Primär (AMB-konform):**
```json
"about": [
  {
    "type": "Concept",
    "id": "http://w3id.org/openeduhub/vocabs/discipline/520",
    "prefLabel": {"de": "Religion"}
  }
]
```

### 4.3 Erweitert: Religionsdidaktische Labels

**13 zentrale Konzepte aus dem Kompendium:**

| Nr. | Didaktisches Label | relipaed URI | Definition (Kurzform) |
|-----|-------------------|--------------|------------------------|
| 1 | **Subjektorientierung** | `https://w3id.org/relipaed/didaktik/subjektorientierung` | Lebenswelt der Lernenden als Ausgangspunkt |
| 2 | **Korrelationsdidaktik** | `https://w3id.org/relipaed/didaktik/korrelation` | Vermittlung zwischen Glaubenstradition und Lebenserfahrung |
| 3 | **Elementarisierung** | `https://w3id.org/relipaed/didaktik/elementarisierung` | Komplexe Inhalte auf Wesentliches reduzieren |
| 4 | **Performativer Religionsunterricht** | `https://w3id.org/relipaed/didaktik/performativ` | Religion durch Vollzug erfahrbar machen |
| 5 | **Theologisieren mit Kindern** | `https://w3id.org/relipaed/didaktik/theologisieren` | Kinder als theologische Gesprächspartner |
| 6 | **Interreligiöses Lernen** | `https://w3id.org/relipaed/didaktik/interreligioes` | Begegnung mit anderen Religionen |
| 7 | **Biblische Didaktik** | `https://w3id.org/relipaed/didaktik/biblisch` | Erschließung biblischer Texte |
| 8 | **Symboldidaktik** | `https://w3id.org/relipaed/didaktik/symbol` | Religiöse Symbole verstehen und deuten |
| 9 | **Kirchenraumpädagogik** | `https://w3id.org/relipaed/didaktik/kirchenraum` | Kirchenräume als Lernorte |
| 10 | **Ästhetisches Lernen** | `https://w3id.org/relipaed/didaktik/aesthetisch` | Sinnliche Zugänge zur Religion |
| 11 | **Inklusive Religionspädagogik** | `https://w3id.org/relipaed/didaktik/inklusiv` | Alle Lernenden mitnehmen |
| 12 | **Konfessionelle Kooperation** | `https://w3id.org/relipaed/didaktik/oekumenisch` | Ev.-kath. Zusammenarbeit im RU |
| 13 | **Digitale Religionsdidaktik** | `https://w3id.org/relipaed/didaktik/digital` | Digitale Medien im Religionsunterricht |

### 4.4 Beispiel: Kombiniert

```json
"about": [
  {
    "type": "Concept",
    "id": "http://w3id.org/openeduhub/vocabs/discipline/520",
    "prefLabel": {"de": "Religion"}
  },
  {
    "type": "Concept",
    "id": "https://w3id.org/relipaed/didaktik/subjektorientierung",
    "prefLabel": {"de": "Subjektorientierung", "en": "Student-centered approach"},
    "relatedMatch": ["http://w3id.org/openeduhub/vocabs/discipline/520"]
  },
  {
    "type": "Concept",
    "id": "https://w3id.org/relipaed/didaktik/korrelation",
    "prefLabel": {"de": "Korrelationsdidaktik", "en": "Correlation didactics"},
    "relatedMatch": ["http://w3id.org/openeduhub/vocabs/discipline/520"]
  }
]
```

---

## 5. audience (Zielgruppe)

### 5.1 OpenEduHub intendedEndUserRole

| Zielgruppe | OpenEduHub URI | Beschreibung |
|------------|----------------|--------------|
| **Religionslehrkräfte** | `http://w3id.org/openeduhub/vocabs/intendedEndUserRole/teacher` | Lehrende |
| **Schüler:innen** | `http://w3id.org/openeduhub/vocabs/intendedEndUserRole/learner` | Lernende |
| **Eltern** | `http://w3id.org/openeduhub/vocabs/intendedEndUserRole/parent` | Eltern/Erziehungsberechtigte |
| **Schulseelsorge** | `http://w3id.org/openeduhub/vocabs/intendedEndUserRole/counsellor` | Beratende |
| **Schulleitung** | `http://w3id.org/openeduhub/vocabs/intendedEndUserRole/manager` | Manager |

### 5.2 Beispiel

```json
"audience": [
  {
    "type": "Concept",
    "id": "http://w3id.org/openeduhub/vocabs/intendedEndUserRole/teacher",
    "prefLabel": {"de": "Lehrende", "en": "Teachers"}
  }
]
```

---

## 6. teaches (Lernziele)

### 6.1 Prozessbezogene Kompetenzen (5 Kernkompetenzen)

| Kompetenz | relipaed URI | Beschreibung |
|-----------|--------------|--------------|
| **Wahrnehmungs- und Darstellungskompetenz** | `https://w3id.org/relipaed/kompetenz/wahrnehmung` | Religiöse Phänomene wahrnehmen und beschreiben |
| **Deutungskompetenz** | `https://w3id.org/relipaed/kompetenz/deutung` | Religiöse Sprache und Symbole verstehen |
| **Urteilskompetenz** | `https://w3id.org/relipaed/kompetenz/urteil` | Religiöse Fragen reflektieren und Position beziehen |
| **Dialogkompetenz** | `https://w3id.org/relipaed/kompetenz/dialog` | Respektvoll über Religion kommunizieren |
| **Gestaltungskompetenz** | `https://w3id.org/relipaed/kompetenz/gestaltung` | Religiöse Ausdrucksformen gestalten |

### 6.2 Inhaltsbezogene Kompetenzen (6 Inhaltsbereiche)

| Inhaltsbereich | relipaed URI | Beispielthemen |
|----------------|--------------|----------------|
| **Mensch und Welt** | `https://w3id.org/relipaed/inhalt/mensch-welt` | Schöpfung, Anthropologie, Theodizee |
| **Bibel** | `https://w3id.org/relipaed/inhalt/bibel` | AT, NT, Hermeneutik |
| **Gott** | `https://w3id.org/relipaed/inhalt/gott` | Gottesbilder, Trinität |
| **Jesus Christus** | `https://w3id.org/relipaed/inhalt/jesus-christus` | Leben Jesu, Christologie, Nachfolge |
| **Kirche** | `https://w3id.org/relipaed/inhalt/kirche` | Ekklesiologie, Ökumene, Kirchengeschichte |
| **Religionen und Weltanschauungen** | `https://w3id.org/relipaed/inhalt/religionen` | Interreligiosität, Weltreligionen |

### 6.3 Beispiel

```json
"teaches": [
  {
    "id": "https://w3id.org/relipaed/kompetenz/deutung",
    "prefLabel": {"de": "Deutungskompetenz"}
  },
  {
    "id": "https://w3id.org/relipaed/inhalt/jesus-christus",
    "prefLabel": {"de": "Jesus Christus"}
  }
]
```

---

## 7. competencyRequired (Voraussetzungen)

### 7.1 Religionspädagogische Voraussetzungen

| Voraussetzung | relipaed URI | Beschreibung |
|---------------|--------------|--------------|
| **Bibelkunde** | `https://w3id.org/relipaed/voraussetzung/bibelkunde` | Grundkenntnisse der Bibel |
| **Kirchengeschichte (Basis)** | `https://w3id.org/relipaed/voraussetzung/kirchengeschichte-basis` | Grundzüge der Kirchengeschichte |
| **Ethische Grundlagen** | `https://w3id.org/relipaed/voraussetzung/ethik-basis` | Grundlegende ethische Reflexion |
| **Gottesdienstverständnis** | `https://w3id.org/relipaed/voraussetzung/gottesdienst` | Liturgische Grundkenntnisse |

### 7.2 Beispiel

```json
"competencyRequired": [
  {
    "id": "https://w3id.org/relipaed/voraussetzung/bibelkunde",
    "prefLabel": {"de": "Bibelkunde"}
  }
]
```

---

## 8. aggregationLevel (Unterrichtsplanung)

### 8.1 OpenEduHub aggregationLevel

| Planungseinheit | OpenEduHub URI | Zeitumfang |
|-----------------|----------------|------------|
| **Unterrichtsbaustein** | `http://w3id.org/openeduhub/vocabs/aggregationLevel/1` | Aktivitäten in 1 Stunde |
| **Unterrichtsstunde** | `http://w3id.org/openeduhub/vocabs/aggregationLevel/2` | 45-90 min |
| **Unterrichtseinheit** | `http://w3id.org/openeduhub/vocabs/aggregationLevel/unit` | Mehrere Stunden |
| **Unterrichtsreihe** | `http://w3id.org/openeduhub/vocabs/aggregationLevel/module` | 6-8 Wochen |
| **Kurs/Halbjahr** | `http://w3id.org/openeduhub/vocabs/aggregationLevel/3` | Halbjahr/Schuljahr |

### 8.2 Beispiel

```json
"aggregationLevel": {
  "id": "http://w3id.org/openeduhub/vocabs/aggregationLevel/unit",
  "prefLabel": {"de": "Unterrichtseinheit (mehrere Unterrichtsstunden)", "en": "Unit"}
}
```

---

## 9. license (Lizenz)

### 9.1 AMB-erlaubte Lizenzen

**JSON Schema oneOf Pattern:**
```regex
^http[s]?://creativecommons.org/(licenses|licences|publicdomain)/.*
^http[s]?://www.gnu.org/licenses/.*
^http[s]?://www.apache.org/licenses/.*
http[s]?://opensource.org/licenses/MIT
^http[s]?://www.opensource.org/licenses/BSD.*
```

### 9.2 Empfohlene Lizenzen für Religionspädagogik

| Lizenz | URI | Verwendung |
|--------|-----|------------|
| **CC0 1.0** | `https://creativecommons.org/publicdomain/zero/1.0/` | Public Domain, keine Rechte vorbehalten |
| **CC BY 4.0** | `https://creativecommons.org/licenses/by/4.0/` | Namensnennung |
| **CC BY-SA 4.0** | `https://creativecommons.org/licenses/by-sa/4.0/` | Namensnennung, Weitergabe unter gleichen Bedingungen |
| **CC BY-NC 4.0** | `https://creativecommons.org/licenses/by-nc/4.0/` | Namensnennung, nicht kommerziell |
| **CC BY-NC-SA 4.0** | `https://creativecommons.org/licenses/by-nc-sa/4.0/` | Namensnennung, nicht kommerziell, Weitergabe unter gleichen Bedingungen |

### 9.3 Beispiel

```json
"license": {
  "id": "https://creativecommons.org/licenses/by-sa/4.0/deed.de"
}
```

---

## 10. Weitere AMB-Felder

### 10.1 languageLevel (Sprachniveau nach GER)

**OpenEduHub languageLevel:**

| Niveau | OpenEduHub URI | GER |
|--------|----------------|-----|
| **A1 (Einstieg)** | `http://w3id.org/openeduhub/vocabs/languageLevel/A1` | Beginner |
| **A2 (Grundlagen)** | `http://w3id.org/openeduhub/vocabs/languageLevel/A2` | Elementary |
| **B1 (Mittelstufe)** | `http://w3id.org/openeduhub/vocabs/languageLevel/B1` | Intermediate |
| **B2 (gute Mittelstufe)** | `http://w3id.org/openeduhub/vocabs/languageLevel/B2` | Upper Intermediate |
| **C1 (fortgeschritten)** | `http://w3id.org/openeduhub/vocabs/languageLevel/C1` | Advanced |
| **C2 (exzellent)** | `http://w3id.org/openeduhub/vocabs/languageLevel/C2` | Proficiency |

**Verwendung:** Fremdsprachliche Bibeltexte, Latein, Griechisch, Hebräisch

### 10.2 keywords (Schlagwörter)

**Freitext (kein kontrolliertes Vokabular):**

```json
"keywords": [
  "Gleichnisse",
  "Neues Testament",
  "Bergpredigt",
  "Nächstenliebe",
  "Biblische Hermeneutik"
]
```

### 10.3 duration (Zeitbedarf)

**ISO 8601 Duration:**

```json
"duration": "PT45M"  // 45 Minuten
"duration": "PT2H"   // 2 Stunden
"duration": "PT90M"  // 90 Minuten
```

### 10.4 inLanguage (Sprache)

**ISO 639-1:**

```json
"inLanguage": ["de"]              // Deutsch
"inLanguage": ["de", "en"]        // Deutsch + Englisch
"inLanguage": ["grc", "he", "la"] // Altgriechisch, Hebräisch, Latein
```

### 10.5 datePublished (Veröffentlichungsdatum)

**ISO 8601:**

```json
"datePublished": "2025-10-13"
```

### 10.6 creator (Urheber)

**Person oder Organization:**

```json
"creator": [
  {
    "type": "Person",
    "name": "Dr. Maria Schmidt",
    "affiliation": "Universität Tübingen"
  }
]
```

### 10.7 description (Beschreibung)

**LocalizedString:**

```json
"description": {
  "de": "Diese Unterrichtseinheit führt Schüler:innen der Sekundarstufe I in die Gleichnisse Jesu ein. Durch Subjektorientierung und Korrelationsdidaktik werden biblische Texte mit der Lebenswelt der Lernenden verknüpft.",
  "en": "This teaching unit introduces secondary school students to the parables of Jesus. Through student-centered approaches and correlation didactics, biblical texts are connected to the learners' world of experience."
}
```

---

## 11. Vollständiges AMB-Beispiel

### 11.1 Religionspädagogische Ressource: "Gleichnisse Jesu verstehen"

```json
{
  "@context": "https://w3id.org/kim/amb/context.jsonld",
  "id": "https://example.org/relipaed/gleichnisse-jesu-001",
  "type": ["LearningResource"],
  "name": {
    "de": "Gleichnisse Jesu verstehen",
    "en": "Understanding the Parables of Jesus"
  },
  "description": {
    "de": "Diese Unterrichtseinheit führt Schüler:innen der Sekundarstufe I in die Gleichnisse Jesu ein. Durch Subjektorientierung und Korrelationsdidaktik werden biblische Texte mit der Lebenswelt der Lernenden verknüpft. Die Einheit umfasst 6 Unterrichtsstunden mit Arbeitsblättern, Bildbetrachtungen und kreativen Gestaltungsaufgaben.",
    "en": "This teaching unit introduces secondary school students to the parables of Jesus. Biblical texts are connected to students' everyday experiences through student-centered and correlation didactics. The unit includes 6 lessons with worksheets, image analysis, and creative design tasks."
  },
  "about": [
    {
      "type": "Concept",
      "id": "http://w3id.org/openeduhub/vocabs/discipline/520",
      "prefLabel": {"de": "Religion"}
    },
    {
      "type": "Concept",
      "id": "https://w3id.org/relipaed/didaktik/subjektorientierung",
      "prefLabel": {"de": "Subjektorientierung", "en": "Student-centered approach"}
    },
    {
      "type": "Concept",
      "id": "https://w3id.org/relipaed/didaktik/korrelation",
      "prefLabel": {"de": "Korrelationsdidaktik", "en": "Correlation didactics"}
    },
    {
      "type": "Concept",
      "id": "https://w3id.org/relipaed/didaktik/biblisch",
      "prefLabel": {"de": "Biblische Didaktik", "en": "Biblical didactics"}
    }
  ],
  "learningResourceType": [
    {
      "id": "http://w3id.org/openeduhub/vocabs/new_lrt/ef58097d-c1de-4e6a-b4da-6f10e3716d3d",
      "prefLabel": {"de": "Unterrichtseinheit und -sequenz", "en": "Teaching unit and sequence"}
    }
  ],
  "educationalLevel": [
    {
      "id": "https://w3id.org/kim/educationalLevel/level_2",
      "prefLabel": {"de": "Sekundarbereich I", "en": "Lower secondary education"},
      "altLabel": {"de": ["Sekundarstufe I", "ISCED 2011, Level 2"]}
    }
  ],
  "audience": [
    {
      "type": "Concept",
      "id": "http://w3id.org/openeduhub/vocabs/intendedEndUserRole/teacher",
      "prefLabel": {"de": "Lehrende", "en": "Teachers"}
    }
  ],
  "teaches": [
    {
      "id": "https://w3id.org/relipaed/kompetenz/deutung",
      "prefLabel": {"de": "Deutungskompetenz"}
    },
    {
      "id": "https://w3id.org/relipaed/kompetenz/dialog",
      "prefLabel": {"de": "Dialogkompetenz"}
    },
    {
      "id": "https://w3id.org/relipaed/inhalt/jesus-christus",
      "prefLabel": {"de": "Jesus Christus"}
    },
    {
      "id": "https://w3id.org/relipaed/inhalt/bibel",
      "prefLabel": {"de": "Bibel"}
    }
  ],
  "competencyRequired": [
    {
      "id": "https://w3id.org/relipaed/voraussetzung/bibelkunde",
      "prefLabel": {"de": "Bibelkunde (Grundkenntnisse)"}
    }
  ],
  "aggregationLevel": {
    "id": "http://w3id.org/openeduhub/vocabs/aggregationLevel/unit",
    "prefLabel": {"de": "Unterrichtseinheit (mehrere Unterrichtsstunden)", "en": "Unit"}
  },
  "duration": "PT270M",
  "inLanguage": ["de"],
  "keywords": [
    "Gleichnisse",
    "Neues Testament",
    "Jesus",
    "Bildsprache",
    "Bibeldidaktik",
    "Hermeneutik"
  ],
  "license": {
    "id": "https://creativecommons.org/licenses/by-sa/4.0/deed.de"
  },
  "creator": [
    {
      "type": "Person",
      "name": "Dr. Maria Schmidt",
      "affiliation": "Universität Tübingen, Institut für Religionspädagogik"
    }
  ],
  "datePublished": "2025-10-13",
  "isAccessibleForFree": true
}
```

---

## 12. Zusammenfassung: AMB-Compliance-Checkliste

### 12.1 Pflicht (MUSS)

- [x] `@context` = `https://w3id.org/kim/amb/context.jsonld`
- [x] `id` = URI (DOI, Handle, URL)
- [x] `name` = Titel (String oder LocalizedString)
- [x] `type` = Array mit "LearningResource"

### 12.2 Empfohlen (SOLLTE)

- [x] `about` mit `discipline/520` (Religion) + religionsdidaktische Labels
- [x] `learningResourceType` mit OpenEduHub new_lrt URI
- [x] `educationalLevel` mit KIM educationalLevel URI (PFLICHT-Vokabular!)
- [x] `audience` mit intendedEndUserRole
- [x] `license` mit erlaubter Lizenz-URI (CC, GNU, Apache, MIT, BSD)
- [x] `description` mit Inhaltsbeschreibung
- [x] `creator` mit Urheberangabe
- [x] `inLanguage` mit ISO 639-1 Code

### 12.3 Optional (KANN)

- [x] `teaches` mit Lernzielen (prozess- und inhaltsbezogen)
- [x] `competencyRequired` mit Voraussetzungen
- [x] `aggregationLevel` mit Planungseinheit
- [x] `languageLevel` mit GER-Niveau (für Fremdsprachen)
- [x] `keywords` mit Freitext-Schlagwörtern
- [x] `duration` mit ISO 8601 Duration
- [x] `datePublished` mit ISO 8601 Date
- [x] `isAccessibleForFree` mit Boolean

---

## 13. Validierung

### 13.1 JSON Schema Validierung

**Online:**
- https://w3id.org/kim/amb/ (AMB Validator)

**CLI (ajv):**
```bash
npm install -g ajv-cli
ajv validate \
  -s https://w3id.org/kim/amb/20231019/schemas/schema.json \
  -d gleichnisse-jesu-001.json
```

**Python:**
```python
import jsonschema
import requests

schema = requests.get("https://w3id.org/kim/amb/20231019/schemas/schema.json").json()
data = {...}  # Ihre Metadaten
jsonschema.validate(data, schema)
```

### 13.2 Compliance-Levels

**Level 1 (Minimal):** Pflichtfelder
**Level 2 (Best Practice):** Pflicht + Empfohlen
**Level 3 (Vollständig):** Pflicht + Empfohlen + Optional

---

## 14. Ressourcen

### 14.1 Standards

- AMB: https://w3id.org/kim/amb/
- KIM educationalLevel: https://w3id.org/kim/educationalLevel/
- KIM HCRT: https://w3id.org/kim/hcrt/
- OpenEduHub: http://w3id.org/openeduhub/vocabs/

### 14.2 Dokumentation

- DINI-AG-KIM: https://dini.de/ag/kim/
- LRMI: https://www.dublincore.org/specifications/lrmi/
- Schema.org LearningResource: https://schema.org/LearningResource
- SKOS: https://www.w3.org/2004/02/skos/

---

**Erstellt:** 13. Oktober 2025  
**Version:** 2.0 (AMB-konform, vollständig)  
**Autor:** GitHub Copilot + Jörg Lohrer  
**Lizenz:** CC BY-SA 4.0
