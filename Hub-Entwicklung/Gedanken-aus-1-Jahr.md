# Gedanken und Konsequenzen aus 1 Jahr Gesprächen · Issue #14

**Status:** Offen · **Erstellt von:** colibri · **vor ~5 Monaten**
**Beteiligte:** colibri (Autor:in/Owner), sicking (Owner)
**Labels:** `Konzeption`, `materialpool`

---

## 1) Kontext

* Sammlung von Eindrücken/Ideen nach Treffen beim **FWU EKD Beirat**.
* Einschätzung des **Materialpools** gab Anlass, Erfahrungen seit ca. Mai 2024 festzuhalten.
* Verweis: Matrix-Chat „rpi-virutell und foerbico“ (09.05.2025, 11:38 Uhr) · Pad: [https://pad.rpi-virtuell.de/p/FWU_EKD_Beirat](https://pad.rpi-virtuell.de/p/FWU_EKD_Beirat)

---

## 2) Fragen (Ausgangslage)

* Redaktion vorhanden, aber **kein definierter Workflow**.
* **Statistik** (Dienstleister?) fehlt / unklar.
* **„Materialklappe“**: Upload durch User – wie redaktionieren? (Workflow)

---

## 3) Fokus / Marke

* Fokus **RU** oder **allgemeine Religionspädagogik**?
* Newsletter breit (Konfi, EB, …), **Header mit „RU“** → Inkonsistenz.
* **„Handverlesen“** klären: Was ist Marke/USP?

---

## 4) Bereiche

* **Technik**
* **Didaktik**

---

## 5) Problem- und Zieldefinition

### Aktueller Zustand

* Materialpool wirkt wie **unspezifische „Zufallssuchmaschine“**.
* **Kein** zielgerichteter Support (Quereinsteiger/aktuelle Themen).
* Teilweise **mangelnde Qualität**, wenig rechtlich geprüfte/gut geführte Materialien.
* **Keine** datenbasierte Evaluation (Downloads, Wirkung).
* **Kein** aktiver/redaktioneller Auswahl- und Bewertungsprozess (bzw. zu wenig sichtbar).
* **Fehlende Nutzerführung** (Lernpfade, thematische Kuratierung).

### Zielbild

> **Anmeldefreier, rechtssicherer, KI-gestützter Material-Navigator**
> – hochwertige, offene Materialien; verlässliche Auffindbarkeit; Support für Quereinsteiger; Orientierung via Use-Cases & Lernpfade.

---

## 6) Technische Anforderungen

### a) KI-gestützte Empfehlungen

* LLM-Chat auf Startseite (Bedarfsabfrage, z. B. „9. Klasse, Antisemitismus“).
* **RAG** auf indexierten Metadaten (Zielgruppe, Thema, Lizenz, Medienart …).

### b) Metadaten & Filter

* Einheitliche Metadaten; Filter u. a.: **Zielgruppe**, **Fach/Thema**, **Format**, **Lizenzstatus**, **rechtliche Nutzbarkeit** (Jugendschutz/DSGVO).

### c) Offene Schnittstellen (API)

* Bereitstellung für Dritte, Kooperationen ermöglichen.

### d) Analytics (datensparsam)

* **Downloadzahlen**, **Nutzungszeit**, **Top-Suchen** zur Qualitätsentwicklung.
* Ohne Login (z. B. **cookielos**/Matomo).

---

## 7) Didaktisch-inhaltliche Anforderungen

### a) Kuratierte Lernpfade & Use-Cases

* „Starterkits“/Dossiers (z. B. Quereinstieg RU, Ökumene, Interreli, aktuelle Themen).
* Kooperationen: **alpika**, rpi Niedersachsen, rpi Bayern, …

### b) Qualitätskriterien & Redaktion

* Transparente Kriterien für „**hochwertig**“.
* Kuratierung durch Redaktion; **Feedback** (Bewertungen/Rezensionen).
* Positivbeispiele: **alpika**, **FWU**, **Sternsinger** (Qualitätslabel).

---

## 8) Anwenderorientierung & UX

* **Barrierefrei**, mobiloptimiert, DSGVO-konform.
* **Geführte Suche** (Chat, Themenzugänge) statt nur Freitext.
* **Kein Login**, **keine Paywall**; rechtssichere Inhalte priorisieren.
* **Mitmachen**: Upload-Formular mit **Lizenz-Assistent**, Format-Guides, Auto-Checks; redaktionelle Freigabe.

---

## 9) Handlungsempfehlungen (Kurzliste)

* **Prototyp KI-Chatberatung** (RAG auf Materialdaten).
* **Starterpakete** für definierte Use-Cases.
* **Metadaten & Filter** überarbeiten; **klare Lizenzkennzeichnung**.
* **Qualitätslabel** für geprüfte Inhalte.
* **Kooperationen priorisieren** (alpika, Sternsinger, …).
* **Integration** in Schul-/Fach-Plattformen.

---

## 10) Mögliche Use-Cases (Beispiele)

### Lehrkraft RU (7. Kl., Thema „Versöhnung“)

* Chat fragt **Stufe/Schwerpunkt/Dauer** → kuratierte Sequenz (Bibelarbeit, Kurzfilm, Gebetsimpuls).
* **Rechtlich geklärt**, optional konfessionell-kooperativ.

### Quereinsteiger*in RU (5. Kl.)

* „**Einstiegspaket RU 5**“ mit 5 Reihen (Was ist Religion?, Jesus, Kirchenjahr …).
* Lernpfade inkl. Zielkompetenzen; KI-Nachhilfe (Begriffe/Methodik).
* Nur Materialien mit **didaktischer Einordnung** & **CC-Lizenz**.

### Referendar*in/Studierende („Judentum heute“)

* KI klärt **Stufe/Zeit/Schwerpunkt** → geprüfte Materialien (rpi-Impulse, jüdische Perspektiven, lizenzgesicherte Videos).
* Hinweise zu **Methodik**/**Differenzierung**, **Hintergrundtexte**.

### Bildungsreferentin (Workshop Demokratie & Religion)

* Vorschläge: **Planspiel**, **Storytelling**, **Diskussion**.
* Materialmappe mit **Ablauf/Rollen/AB** + Lizenzen; Filter „außerschulisch/Konfi/Jugend“.

### Redakteur*in (Upload „Digitalität & Glaube“)

* **Materialklappe**: vereinfachter Upload (PDF/Video/AB/Kommentar).
* **Lizenz-Assistent**, **KI-Checks** (Bildquellen/Metadaten).
* **Redaktion** informiert → Freigabe → **Qualitätslabel** & Verschlagwortung.

---

## 11) Nächste Schritte (aus Kommentaren)

* Inhalte in **Einzel-Tickets** herunterbrechen (Corinna & Ludger).
* **Tracking/Download-Zahlen** prüfen (erste Recherchen laufen, komplex).
* Austausch Corinna/Ludger (Mi 14.05., 08:15 Uhr):

  * **Was ist der Materialpool?** (Sammelstelle · Bildungsplattform · redaktioneller Ort)
  * **5 Prüf-Kriterien** für Redaktion (Startbasis)
  * **Fokus-Optionen**: Alpika-Austausch · Material-DB · **KI-Basis für Unterrichtserstellung**

---

## 12) Qualitäts-/Beispiel-Links

* **Beispiel 1 (Qualitätseinordnung „nicht hochwertig“ – fehlende didaktische Einleitung):**
  [https://irp-freiburg.de/irp-aktuell/detail/nachricht/id/222176-irp-aktuell-35-papst-franziskus/?cb-id=12181540](https://irp-freiburg.de/irp-aktuell/detail/nachricht/id/222176-irp-aktuell-35-papst-franziskus/?cb-id=12181540)
* **Beispiel 2 (nicht direkt schultauglich – fehlt Verlaufsplan):**
  [https://material.rpi-virtuell.de/material/mutig-stark-und-beherzt-kinder-falten-friedenstauben/](https://material.rpi-virtuell.de/material/mutig-stark-und-beherzt-kinder-falten-friedenstauben/)
* **Religionspädagogische Kriterien (relimentar, Datei-Link):**
  [https://nextcloud.comenius.de/s/KBs2SibFfwqagWT?openfile=true](https://nextcloud.comenius.de/s/KBs2SibFfwqagWT?openfile=true)
* **Arbeits-Pad (FWU EKD Beirat):**
  [https://pad.rpi-virtuell.de/p/FWU_EKD_Beirat](https://pad.rpi-virtuell.de/p/FWU_EKD_Beirat)

---

## 13) Offene Punkte / To-Dos

* [ ] Redaktions-**Workflow** definieren (Rollen, Status, Freigaben, SLA).
* [ ] **5 Qualitätskriterien** minimal definieren und testen.
* [ ] **Metadaten-Schema** konsolidieren (Lizenz/DSGVO/Jugendschutz).
* [ ] **RAG-Prototyp** (KI-Chat) aufsetzen.
* [ ] **Analytics** (datensparsam) konzipieren & implementieren.
* [ ] **Materialklappe** + Lizenz-Assistent + Auto-Checks pilotieren.
* [ ] **Starterpakete** (Use-Cases) kuratieren und veröffentlichen.
* [ ] **Kooperationen** (alpika, FWU, Sternsinger …) priorisieren & binden.
* [ ] **Issue-Split**: Umsetzung in Teil-Tickets (Technik/Didaktik/UX/Koop).


