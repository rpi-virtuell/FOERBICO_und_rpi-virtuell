# Liste und Kriterien

Anbieter und Hostingentscheidung

Grundlage für transparente Entscheidungen

**Kriteriensammlung aus folgenden Perspektiven:**
- **Nutzer**: 
    - Zuverlässigkeit, Verfügbarkeit
    - Hochverfügbarkeit: ausfallsicherer Betrieb über mehrere Server (+ Load Balancer)
    - Performance, Leistungsumfang, Skalierbarkeit
    - Fehlertoleranz (klären)
- **Kosten**: 
    - Abwägung zwischen 
        - Selfhosting (Root-Server + Selbstadministration) => Personalkosten
        - Full-Managed-Services (IT-Partner) => Servicekosten
    - unbegrenzte Userzahl, Datenmenge und Bandbreite vs. Volume Limits e.g. per User/Month
- **Entwickler**: 
    - Anpassbarkeit, Root-Zugriff, Zugang zu Logs, 
    - Installation von Diensten/Bibliotheken, Zugriff auf API-Keys, etc.
    - Bereitstellung einer Sandbox (Testumgebung)
- **Support**: 
    - Freundlichkeit, Reaktionszeiten,    
    - Anpassung der SLA an Ihre Bedürfnisse
    - Lösungskompetenz bei Softwarefehlern, addHoc Hilfen
    - Möglichkeit individueller Vertragsbedingungen
- **Reputation**: 
    - Langfristige Verlässlichkeit und Marktposition des Hostingpartners
    - Förderung und Bereitstellung von Open-Source-Komponenten
    - Nachhaltige Energiequellen für den Serverbetrieb
- **Compliance:**
   - Einhaltung von Datenschutzgesetzen (z.B. DSGVO)
   - Zertifizierungen (ISO 27001, TÜV, etc.)
- **Skalierbarkeit und Flexibilität:**
   - Möglichkeit zur schnellen Anpassung der Ressourcen bei Bedarf
   - Flexible Vertragslaufzeiten und Anpassbarkeit der Dienstleistungen
- **Disaster Recovery und Backup-Strategien:**
   - Regelmäßige Backups und einfache Wiederherstellung
   - Notfallpläne und Redundanzen
- **Migration:**
    - Unterstützung beim Umzug bestehender Anwendungen
    - Minimierung von Ausfallzeiten während der Migration
- **Integration:**
    - Unabhängiger Service (z.B.: abweichende Dienste und Securitypolicies)
    - Intergration in vorhandene Serverstrukturen (z.B: weitere Instanz, Virtualisierung, Docker ...)
        - Komplexitätsreduktion im Blick auf Administration und Abhängigkeiten
---


#### **Kriterienmatrix:**

bei jedem Service, den wir anbieten, können wir folgende Liste gewichten, oder ein Kriterium ohne Gewichtung lassen, 
wenn dieses für den geplanten Service nicht relevant ist.


| **Perspektive** | **Kriterium**                                | **Gewichtung (1-5)** |
|-----------------|----------------------------------------------|----------------------|
| **Nutzer**      | Zuverlässigkeit, Hochverfügbarkeit           |                      |
|                 | Performance, Leistungsumfang, Skalierbarkeit |                      |
|                 | Fehlertoleranz                               |                      |
| **Kosten**      | Selfhosting oder Full-Managed-Services       |                      |
| **Entwickler**  | Anpassbarkeit, Root-Zugriff, Zugang zu Logs  |                      |
|                 | Installation von Diensten/Bibliotheken       |                      |
|                 | Zugriff auf API-Keys                         |                      |
|                 | Bereitstellung einer Sandbox (Testumgebung)  |                      |
| **Support**     | Freundlichkeit, Reaktionszeiten              |                      |
|                 | Anpassung der SLA an Ihre Bedürfnisse        |                      |
|                 | Lösungskompetenz, ad-hoc Hilfen              |                      |
|                 | Individuelle Vertragsbedingungen             |                      |
| **Reputation**  | Langfristige Verlässlichkeit                 |                      |
|                 | Open-Source-Förderung                        |                      |
|                 | Nachhaltige Energiequellen                   |                      |
| **Compliance**  | Einhaltung von Datenschutzgesetzen           |                      |
|                 | Zertifizierungen (ISO 27001, TÜV, etc.)      |                      |
| **Skalierbarkeit und Flexibilität** | Ressourcenanpassung bei Bedarf   |               |
|                 | Flexible Vertragslaufzeiten                  |                      |
| **Disaster Recovery und Backup-Strategien** | Regelmäßige Backups, einfache Wiederherstellung |   |
|                 | Notfallpläne und Redundanzen                 |                      |
| **Migration**   | Unterstützung beim Umzug bestehender Anwendungen |       |
|                 | Minimierung von Ausfallzeiten                |                      |
| **Integration** | Nutzung vorhandener Serverstruktur           |                      |
|                 | Unabhängiger Service                         |                      |


### Beispielanwendung zum Matrixserver

Die relevanten Kriterien wenden wir auf Angebote und eigene Optionen zum Hosting an.
Einfachheitshalber ist hier alles als wichtig (5) deklariert.


### **Ausgangsdaten**

#### **Kriterien, Gewichtungen und Bewertungen**

| **Kriterium**                          | **Gewichtung** | **Hosting A** | **Hosting B** | **Hosting C** |
|----------------------------------------|----------------|----------------|----------------|----------------|
| Zuverlässigkeit, Hochverfügbarkeit     | 5              | 3              | 4              | 3              |
| Datenschutzgesetze einhalten           | 5              | 5              | 5              | 4              |
| Anpassung der SLA an Ihre Bedürfnisse  | 5              | 1              | 5              | 3              |
| Lösungskompetenz, ad-hoc Hilfen        | 5              | 1              | 2              | 2              |
| Zugriff auf Config                     | 5              | 1              | 3              | 4              |
| Kosten                                 | 5              | 1              | 5              | 3              |
| Notfallpläne und Redundanzen           | 5              | 4              | 4              | 3              |

---

### **Berechnung der gewichteten Bewertungen**

#### **1. Hosting A**

| **Kriterium**                          | **Gewichtung** | **Bewertung** | **Gewichtete Bewertung** |
|----------------------------------------|----------------|---------------|--------------------------|
| Zuverlässigkeit, Hochverfügbarkeit     | 5              | 3             | 5 × 3 = 15               |
| Datenschutzgesetze einhalten           | 5              | 5             | 5 × 5 = 25               |
| Anpassung der SLA an Ihre Bedürfnisse  | 5              | 1             | 5 × 1 = 5                |
| Lösungskompetenz, ad-hoc Hilfen        | 5              | 1             | 5 × 1 = 5                |
| Zugriff auf Config                     | 5              | 1             | 5 × 1 = 5                |
| Kosten                                 | 5              | 1             | 5 × 1 = 5                |
| Notfallpläne und Redundanzen           | 5              | 4             | 5 × 4 = 20               |
| **Gesamtpunktzahl**                    |                |               | **80 Punkte**            |

#### **2. Hosting B**

| **Kriterium**                          | **Gewichtung** | **Bewertung** | **Gewichtete Bewertung** |
|----------------------------------------|----------------|---------------|--------------------------|
| Zuverlässigkeit, Hochverfügbarkeit     | 5              | 4             | 5 × 4 = 20               |
| Datenschutzgesetze einhalten           | 5              | 5             | 5 × 5 = 25               |
| Anpassung der SLA an Ihre Bedürfnisse  | 5              | 5             | 5 × 5 = 25               |
| Lösungskompetenz, ad-hoc Hilfen        | 5              | 2             | 5 × 2 = 10               |
| Zugriff auf Config                     | 5              | 3             | 5 × 3 = 15               |
| Kosten                                 | 5              | 5             | 5 × 5 = 25               |
| Notfallpläne und Redundanzen           | 5              | 4             | 5 × 4 = 20               |
| **Gesamtpunktzahl**                    |                |               | **140 Punkte**           |

#### **3. Hosting C**

| **Kriterium**                          | **Gewichtung** | **Bewertung** | **Gewichtete Bewertung** |
|----------------------------------------|----------------|---------------|--------------------------|
| Zuverlässigkeit, Hochverfügbarkeit     | 5              | 3             | 5 × 3 = 15               |
| Datenschutzgesetze einhalten           | 5              | 4             | 5 × 4 = 20               |
| Anpassung der SLA an Ihre Bedürfnisse  | 5              | 3             | 5 × 3 = 15               |
| Lösungskompetenz, ad-hoc Hilfen        | 5              | 2             | 5 × 2 = 10               |
| Zugriff auf Config                     | 5              | 4             | 5 × 4 = 20               |
| Kosten                                 | 5              | 3             | 5 × 3 = 15               |
| Notfallpläne und Redundanzen           | 5              | 3             | 5 × 3 = 15               |
| **Gesamtpunktzahl**                    |                |               | **110 Punkte**           |

---


### **Beispielhafte Auswertung der Ergebnisse**

Anreicherung der Ergbebnisse durch Fakten aus den Angeboten.

**Hosting B** erreicht mit **140 Punkten** und erfüllt somit die Kriterien am besten. Insbesondere zeichnet es sich aus durch:

- **Hohe Zuverlässigkeit** (Bewertung: 4)
- **Volle Einhaltung der Datenschutzgesetze** (Bewertung: 5)
- **Individuell anpassbare Service Level Agreements** (Bewertung: 5)
- **Kostengünstig Selfhosting + Freelancer** (Bewertung: 5)
- **geringe Lösungskompetenz für Matrixprobleme und Angebot von ad-hoc Hilfen** (Bewertung: 2)
- **Zugriff auf einige Konfigurationen** (Bewertung: 3)
- **Gute Notfallpläne und Redundanzen** (Bewertung: 4)

**Hosting C** liegt mit **110 Punkten** auf dem zweiten Platz mit:

- **Zuverlässikeit** (Bewertung: 3)
- **Gute Einhaltung der Datenschutzgesetze** (Bewertung: 4)
- **Anpassbare SLA** (Bewertung: 3)
- **Einfacher Zugriff auf Konfigurationen** (Bewertung: 4)
- **Moderate Kosten Full Managed Service** (Bewertung: 3)

**Hosting A** erreicht nur **80 Punkte** und erfüllt die Hauptkriterien weniger gut:

- **Keine Anpassbarkeit der SLA** (Bewertung: 1)
- **Hilfen für Matrix stehen nicht zur Verfügung** (Bewertung: 1)
- **Kein zugriff auf Konfigurationsdateien** (Bewertung: 1)
- **Höhere Kosten Full Managed Service** (Bewertung: 1)

---

## Fazit

Auf Basis einer solchen Entscheidungsmatrix lassen sich transparente Entscheidungen treffen.



ChatGPT: https://chatgpt.com/share/671a4a45-bc4c-8009-af64-579b93052c6e


