# JSON-Datenstruktur für Social-Media-Profile und Organisationen

## Übersicht
Diese JSON-Datei speichert Social-Media-Profile von Personen und Organisationen, einschließlich ihrer Verknüpfungen mit Communities oder Labels wie **relilab** und **relimentar**. Zusätzlich ermöglicht die Struktur eine mehrfache Zuordnung von Personen zu Organisationen sowie Beziehungen zwischen Organisationen.

---

## Datenstruktur

### Personen (`persons`)
- **`name`** *(String)* – Name der Person
- **`profiles`** *(Array)* – Liste der Social-Media-Accounts der Person
  - **`platform`** *(String)* – Plattform (z.B. Twitter, Instagram, LinkedIn)
  - **`handle`** *(String)* – Benutzername/Handle auf der Plattform
  - **`mentionSyntax`** *(String)* – Syntax für Erwähnungen (`@handle` oder ID)
  - **`profileLink`** *(String)* – Direktlink zum Profil
  - **`category`** *(String)* – Einstufung (z.B. VIP, Bildung, BNE)
  - **`firstSeen`** *(String, ISO-Zeitformat)* – Zeitpunkt der Ersterfassung
  - **`lastUpdated`** *(String, ISO-Zeitformat)* – Letzte Aktualisierung
  - **`organizationIds`** *(Array)* – Liste der zugehörigen Organisationen anhand ihrer `orgId`

### Organisationen (`organizations`)
- **`orgId`** *(String)* – Eindeutige Abkürzung für die Organisation
- **`orgName`** *(String)* – Vollständiger Name der Organisation
- **`handles`** *(Array)* – Social-Media-Profile der Organisation
  - **`platform`** *(String)* – Plattform (z.B. Twitter, LinkedIn)
  - **`handle`** *(String)* – Benutzername/Handle der Organisation
  - **`mentionSyntax`** *(String)* – Erwähnungs-Syntax (`@handle` oder ID)
  - **`profileLink`** *(String)* – Direktlink zum Profil
- **`relatedOrgs`** *(Array, optional)* – Liste verwandter Organisationen anhand ihrer `orgId`

### Beispielhafte JSON-Struktur
```json
{
  "persons": [
    {
      "name": "Jörg Lohrer",
      "profiles": [
        {
          "platform": "Mastodon",
          "handle": "joerglohrer",
          "mentionSyntax": "@joerglohrer",
          "profileLink": "https://reliverse.social/@joerglohrer",
          "category": "Bildung",
          "firstSeen": "2025-02-01T09:00:00",
          "lastUpdated": "2025-02-10T14:00:00",
          "organizationIds": ["comenius", "relilab"]
        }
      ]
    }
  ],
  "organizations": [
    {
      "orgId": "comenius",
      "orgName": "Comenius-Institut",
      "relatedOrgs": ["relilab"],
      "handles": [
        {
          "platform": "Mastodon",
          "handle": "ComeniusInst",
          "mentionSyntax": "@ComeniusInst",
          "profileLink": "https://reliverse.social/ComeniusInst"
        }
      ]
    }
  ]
}
```

---

## Nutzung

### 1. **Abruf der Social-Media-Profile einer Person**
**Filtere nach `name` oder einem bestimmten `handle`**, um zu sehen, welche Plattformen eine Person nutzt.

### 2. **Organisationen einer Person ermitteln**
**Nutze das Feld `organizationIds`**, um alle zugehörigen Organisationen zu einer Person nachzuschlagen.

### 3. **Verknüpfte Organisationen abrufen**
Über das Feld **`relatedOrgs`** kann man nachsehen, mit welchen anderen Organisationen eine Organisation kooperiert.

### 4. **Automatisierte API-Integration**
Da die Datei in JSON-Format vorliegt, kann sie über **JavaScript (Node.js, fetch)** oder **Python (`json`-Modul)** verarbeitet werden.

#### Beispiel (JavaScript):
```js
fetch('https://raw.githubusercontent.com/user/repository/main/social_profiles.json')
  .then(response => response.json())
  .then(data => console.log(data.persons));
```

#### Beispiel (Python):
```python
import json
import requests

data = requests.get("https://raw.githubusercontent.com/user/repository/main/social_profiles.json").json()
print(data["persons"])
```

---

## Erweiterungsmöglichkeiten
- **Weitere Kategorien** wie „Dozenten“, „Referenten“, „Netzwerkpartner“
- **Mehrere Rollen innerhalb einer Organisation** (z.B. „Mitarbeiter“, „Community-Manager“)
- **Erweiterung um Aktivitätsdaten** (z.B. letzter Tweet, letzte Veranstaltung)

Diese JSON-Struktur ist flexibel erweiterbar und für verschiedene Anwendungsfälle anpassbar.
