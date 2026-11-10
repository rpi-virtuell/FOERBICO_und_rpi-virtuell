# Gesamtkonzeption: Der Hub als Nachweis der Antragszusagen

Entwurf vom 02.11.2026, ergänzt am 03.11.2026 um den Konsens aus dem Gespräch zu relilab und Hub. Gespräch Jörg Lohrer / Claude. Design-Dokument für die Prototyp-Entwicklung des reli_hub bis zum Launch auf der Fazit-Tagung (2./3. Februar 2027, Frankfurt) und für die Buchführung im Forgejo-Issue-Tracker bis zum Abschlussbericht (Projektende 30.04.2027, Schlussverwendungsnachweis 30.06.2027).

Quellen: Vorhabenbeschreibung FOERBICO (Fassung 19.12.2023, Meilensteine M-Nummern), verbindliche AP-/Meilensteinübersicht (Stand Juni 2025, Projektmonat 14), Zwischenberichte 2024 und 2025 samt Review, Positionspapier „Community Hub und Edufeed differenzieren" (22.04.2026), Endspurt-Auswertung (06.07.2026), beide Forgejo-Issue-Tracker (Stand 02.11.2026: 636 Issues offenes Repo, 180 geschlossenes Repo, 43 Meilensteine), reli_hub-Prototyp (`main` df6ffcb) mit Konstruktionsbeschreibung und ADRs, die 19 Fäden auf gitworkshop, Gesprächskonsens relilab und Hub vom 03.11.2026 mit Ergänzungen (`Hub-Entwicklung/2026-11-03-gespraech-relilab-hub-konsens.md`, main 773dca7), Destillat der Hub-Erkundung mit UX-Außenblick vom 03.11.2026 (`Hub-Entwicklung/2026-11-03-hub-erkundung-destillat.md`) und die daraus veröffentlichte dritte Issue-Runde auf gitworkshop (acht Issues zu Konsole, Leiste, Navigation, Startseite, mobil; vier Kommentare zu Blume, rpi-virtuell, Storytelling, Selbstverständnis).

## 1. Absicht

Am 2. Februar 2027 sitzt eine Person vom Projektträger vor dem Hub. Sie soll anklicken können, was der Antrag versprochen hat, und sagen: „Ja, das ist realisiert." Der Hub selbst ist der Nachweis. Nicht ein Bericht, der auf den Hub zeigt, sondern ein Hub, in dem jede Antragszusage einen Ort hat.

Das hat drei Gründe:

1. **Der Antrag hat den Hub als Ort definiert.** AP 3 nennt ihn „die online zugängliche Verbundstelle, die die Verknüpfung der Communities sichtbar werden lässt, die Ressourcen wechselseitig zugänglich macht, Verabredungen dokumentiert, technische Tools sowie Tutorials abrufbar zur Verfügung stellt, Öffentlichkeitsarbeit Community-übergreifend verknüpft und die Prozesse und Ergebnisse des Projektes nachhaltig dokumentiert." Jeder dieser Halbsätze ist eine prüfbare Zusage.
2. **Das Positionspapier verlangt Hub-Substanz jenseits von Edufeed.** Edufeed ist die separat geförderte technische Realisierungslinie. Der reli_hub ist FOERBICOs eigene Hub-Gestalt: der Entwurf von Jens Dechow auf dem edufeed-Unterbau, mit FOERBICO-Farben, FOERBICO-Schaufenster und den Spielregeln des Verbunds. Er ist der Beleg, den das Positionspapier für den Abschlussbericht fordert.
3. **Zwei Hub-Meilensteine sind (noch) leer.** AP 4-5 (OER-Client, fällig 08/2026) hat ein Issue, AP 4-6 (dezentrale Kataloge) und AP 9-1 (technische Bedarfe) haben keins. Die Endspurt-Auswertung vom Juli nennt das als dringendstes Handlungsfeld. Diese Konzeption füllt sie mit konkreten Hub-Elementen.

**Leitbild seit dem 03.11.2026:** Der Hub ist das integrative Ganze mit offenen Bildungspraktiken (OEP) als Herzstück. Er ist kein reines OER-Ökosystem, führt aber in seiner inneren Logik zu OER hin: Geschützte Materialien dürfen hinein (indexierte Mediatheken, Verlagsmaterial mit AMB-Metadaten), aber wer nicht offen lizenziert, kann die anderen Elemente nicht vollumfänglich nutzen, etwa das Weiterbearbeiten auf dem Schreibtisch oder in der Community. Das deckt sich mit dem Antrag, der von OEP/OER spricht, und der Hub macht es an jedem Material sichtbar (4.3, 4.13). Communities (ko-konstruktiv), Instanzen (rezeptiv genutzte Angebote wie Materialpool, Fortbildungskalender, relilab als Labor) und Ökosystem (die Gesamtheit) sind drei verschiedene Dinge; die Marken rpi-virtuell und relilab treten hinter die Strukturen zurück. Aus der Hub-Erkundung am selben Tag: Der Hub ist die Klammer, rpi-virtuell ist nicht der Hub als Ganzes, sondern eine eigene Instanz in der Leiste, die die rezeptive Logik bündelt (Materialpool, Fortbildungskalender, News) und für die institutionelle Fortbildung der Institute steht; relilab ist die Instanz des Labors. Der Grundaufbau (Klammer, Instanzen mit eigenem Gesicht, fünf Erschließungsmodi) hat den Außenblick bestanden.

Entscheidung aus dem Gespräch: **Echt, wo es geht.** Hinter den Hub-Elementen stecken Inhalte von den Relays, nicht eingebettete Schnappschüsse. Inhalte sind genug da; wo etwas fehlt, wird es nachgeliefert oder inhaltlich aufgefüttert. Nachbau ist zulässig, wird aber als solcher gekennzeichnet und nicht als echt ausgegeben.

## 2. Ziele, Nicht-Ziele, Anti-Ziele

**Ziele**

- Jede Hub-Zusage des Antrags (Abschnitt 4, 18 Zeilen) hat beim Launch einen anklickbaren Ort im Hub, mit echten Inhalten in der Stufe „Launch-Pflicht".
- Der Hub bekommt einen Erschließungs-Layer für den Projektträger: ein eigenes Schaufenster, das jede Zusage mit ihrem Ort im Hub und ihren Belegen verknüpft.
- Der Forgejo-Tracker hält die Buchführung: je Hub-Meilenstein ein Nachweis-Issue, das auf die Hub-Stelle und die Belege zeigt. Die leeren Meilensteine AP 4-5, 4-6 und 9-1 sind danach belegt.
- Die Hub-Entwicklung auf gitworkshop erhält daraus Issues in Hub-Sprache, ohne Arbeitspakete, Meilensteine oder Förderkennzeichen.

**Nicht-Ziele**

- Die WordPress-Plugins hat der edufeed-Entwickler im Rahmen seiner Anstellung am Comenius-Institut für FOERBICO gebaut (Eigenmittel des Instituts, nicht aus der Edufeed-Förderung, nicht aus dem FOERBICO-Personalplan; Stand 04.11.2026). Die WordPress-Zusagen (AP 4-4, M30, AP 9-5) sind durch die vier Plugins aus `git.edufeed.org/edufeed/wp-plugins-nostr` belegt (Stand 18.09.2026, Releases als Zips): `amb-nostr` zeigt AMB-Ressourcen mit Suche und Facettenfiltern, `longform-nostr` Artikel, `nostr-calendar` Termine, `nostr-publish` veröffentlicht WordPress-Beiträge als Nostr-Events; alle mit Block, Shortcode, `community`-Filter und Cache. Ein Eingabeformular als WordPress-Plugin folgt in der Woche ab dem 09.11.2026. Herkunft, sauber benannt: Die Plugins entstehen nicht in der Edufeed-Förderung und nicht im FOERBICO-Personalplan, sondern in der Anstellung des Entwicklers am Comenius-Institut; das Institut stellt sie dem Projekt als Open Source zur Verfügung. Der Hub zeigt sie als Einbettungsweg neben der Steuerkonsole. Im Abschlussbericht gelten sie als Beitrag des Comenius-Instituts aus Eigenmitteln, deren Einsatz, Anforderungen und Erprobung in den Communities (ALPIKA-Arbeitsgruppen, Institute) FOERBICO verantwortet und belegt.
- Keine neue Relay-Infrastruktur für den Launch. Der Hub liest von den edufeed-Relays (`relay-rpi.edufeed.org`, Kalender- und Communikey-Relay) und wird seit 03.11.2026 unter https://hub.rpi-virtuell.net aus einem Caddy-Container ausgeliefert (`Dockerfile`, `app.yaml` und `docs/betrieb.md` im reli_hub-Repo); GitHub Pages ist abgelöst.
- Keine Änderung an der edufeed-App in diesem Vorhaben.
- Keine Begleitforschungs-Meilensteine (AP 11) im Hub. AP 11-4 erscheint nur über das, was der Hub ohnehin dokumentiert.

**Anti-Ziele** (das wäre ein Scheitern, auch wenn es technisch läuft)

- Der Hub wird zur Berichtsseite: Arbeitspaket-Nummern in der Navigation, Meilenstein-Listen statt Angebote. Die Nachweis-Logik bleibt im Erschließungs-Layer, der Rest des Hubs bleibt Angebot für Nutzende.
- Arbeitspakete, Meilensteine oder Förderkennzeichen landen im reli_hub-Repo (Issues, ADRs, Code, Nostr-Seiten des Hub-Codes). Die Zuordnung lebt hier im FOERBICO-Repo und in Forgejo.
- Nachbau wird als echt präsentiert.
- Hub und Edufeed werden wieder gleichgesetzt. Sprachregelung: „der reli_hub als FOERBICOs Realisierung des Community-Hub-Konzepts auf edufeed-Basis".
- Personennamen von Partnern in Dokumenten oder Commits des offenen Repos. Rollen, Handles, Pubkey-Präfixe.

## 3. Rahmenbedingungen

- **Zeit:** Der Hub ist bis Weihnachten 2026 fertig (Stand 23.12.2026, alle Zeilen der Stufen A und B). Der Januar ist Feinschliff: Inhalte, Korrekturen, Probelauf, eingefrorene Kopie. Kein neuer Umbau nach dem 23.12.
- **Stack beim Launch:** der HTML-Prototyp (`index.html`, kein Build) mit Live-Abfrage der Relays und dem eingebetteten Schnappschuss als Rückfall. Der Svelte-Unterbau (Design „Repo hub" vom 26.10.2026) kommt danach und ist der Verstetigungspfad, nicht die Launch-Bedingung. Begründung: Der Prototyp ist heute lauffähig und ausgeliefert; ein Stack-Wechsel vor dem Launch würde die drei Monate aufzehren. Das ist meine Festlegung, von Jörg zu prüfen (Abschnitt 9).
- **Dokumentationswelten:** Forgejo (offenes Repo) trägt AP- und M-Nummern; gitworkshop trägt Hub-Sprache; das geschlossene Repo trägt Betrieb und Personen. Issues auf gitworkshop veröffentlicht Poutník, Entwürfe werden vorher gezeigt.
- **Fünf-Kreise-Diskussion:** Der Prototyp hat fünf Funktionen (hub, finden, erstellen, kooperieren, veröffentlichen). Auf gitworkshop liegt ein Vorschlag für fünf anders geschnittene Kreise (finden, nutzen, mitmachen, teilen, ich). Diese Konzeption ordnet den heutigen Funktionen zu; eine Umbenennung verschiebt Zeilen, nicht Inhalte. Aus dem Gespräch vom 03.11.: Die Steuerungslogik des Teams (Labor gegen Institutsfortbildung, Community gegen Instanz) gehört nicht in die Nutzernavigation; Organigramm und Navigation werden getrennt gedacht. Der Konsens wird erst ausformuliert, dann in eine Navigation überführt; dafür ist ein weiterer Termin vorgesehen. Bis dahin bleibt die Fünfgliedrigkeit die Organisationsform. Verabredung aus der Hub-Erkundung: Die ersten zwei Wochen (bis zum Folgetermin mit dem UX-Gast am 25.11.2026) wird nur die HTML-Seite rund geschliffen, ohne Software-Stack, damit Startseite, Konsole (Blume unten rechts, Erschließungsmodi) und Leiste (unten links, Instanzen und Communities) aus Nutzersicht konsistent sind, bevor die Inhaltszeilen aufgesetzt werden. Die acht Issues der dritten Runde (Kreis-Klick, Beschriftungen, direkt zur Aktion, Begriffe und Farben, Konsole auf der Startseite, Leiste als Widget, Leiste konfigurierbar, mobil) laufen deshalb vor den Zeilen dieser Konzeption, und die Zeilen bauen auf ihrem Ergebnis auf: dieselben Begriffe, dieselben Farben, dieselben Ziele.
- **Prüfbarkeit:** Jedes Hub-Element, das als „echt" gilt, hat eine Prüfung in `tests/` des reli_hub-Repos oder eine dokumentierte Relay-Abfrage, mit der man den Inhalt nachvollziehen kann.
- **Wer baut:** Ein Team aus fünf Personen und zwei Coding-Agenten. Jörg Lohrer (Community-Management, Maintainer); die technische Umsetzung am CI (Betrieb, CI/CD, Domain); Öffentlichkeitsarbeit und Redaktion sowie Konzeption (Inhalte, Texte, Spielregeln, Kataloge); der Entwickler von edufeed und relidesk (Leit-Maintainer des reli_hub-Repos, kann Code beitragen, besonders an den Nahtstellen zur edufeed-App); dazu die Coding-Agenten Poutník und antiope, die Code, Issues und Textentwürfe zuarbeiten. Der Entwurfsautor des Prototyps entwirft parallel weiter. Damit laufen Code-PRs und Inhaltsstrang parallel; die B-Zeilen sind eingeplant, die Rückfallreihenfolge in Abschnitt 8 bleibt als Sicherung.
- **Entscheidungsrecht:** Jörg ist seit 28.10.2026 bestätigter Maintainer des reli_hub-Repos. Er mergt PRs nach `main` und pusht nach Forgejo; die Issues auf gitworkshop sind der Ort, an dem der Leit-Maintainer und das Team einwenden können, so wie in der ersten Runde: zuerst umsetzen, dann im Issue zur Diskussion stellen. Der Launch-Stand ist `main`. ADR-0002 (Nachbau mit Schnappschuss) wird durch ein neues ADR ersetzt: Nachbau mit Live-Daten und Schnappschuss als Rückfall.
- **Relay-Last auf der Tagung:** Die edufeed-Relays sperrten IP-Adressen nach etwa zwanzig schnellen Anfragen; eine Ausnahmeregel gilt seit 23.09.2026 für die Pipeline, nicht für Tagungsgäste hinter einem gemeinsamen WLAN. Deshalb bündelt der Querschnitt (Abschnitt 7, Issue 13) die Abfragen je Ansicht, hält Antworten im Browser und lädt beim Start den Schnappschuss, der am Launch-Tag frisch erzeugt wird („Stand vom …" sichtbar). Live-Abfragen aktualisieren ihn, der Hub bleibt vorführbar, auch wenn das Relay abweist. Jörg bittet den Relay-Betreiber vor der Tagung um eine Lesefreigabe für die Tagungs-IP.
- **Prüfbarkeit nach dem Launch:** Der Schlussverwendungsnachweis ist am 30.06.2027 fällig, eine Prüfung kann später kommen. Deshalb wird der Launch-Stand nicht nur getaggt, sondern als eingefrorene Kopie mit eingebettetem Datenstand unter fester Adresse ausgeliefert (`…/hub/launch-2027-02/`, später unter der eigenen Domain). Erschließungs-Layer und Nachweis-Issues verlinken beide Adressen: die lebende und die eingefrorene.

## 4. Die Matrix: Antragszusage → Hub-Element

Spalten: Zusage mit M-Nummer und AP; Funktion im Hub; Hub-Element und Route; Datenquelle (echt) oder Nachbau; vorhandene Belege; Lücke; Stufe. Stufen: **A** Launch-Pflicht (echt), **B** Launch-Wunsch (echt oder gekennzeichneter Nachbau), **C** nach Launch.

Routen sind Hash-Routen des Prototyps (`#…`). Neue Routen sind Vorschläge und werden auf gitworkshop ausgehandelt.

### 4.1 Netzwerk sichtbar machen

| | |
|---|---|
| **Zusage** | M7 (AP 3-1): Für die Visualisierung der Netzwerkaktivitäten im Community-Hub sind die Voraussetzungen geschaffen. AP 3: Erfassung religionsbezogener Communities, Akteure, Aktivitäten, Kooperationen, Kompetenzen, Repositorien und deren Verknüpfung. |
| **Funktion** | kooperieren |
| **Hub-Element** | Ökosystem-Karte `#oekosystem`: Communities (Kreise, ko-konstruktiv), Instanzen (Kacheln, rezeptiv genutzt: rpi-virtuell mit Materialpool, Fortbildungskalender und News; relilab als Labor; relidesk; Partner-Instanzen), Akteure (Punkte), Kooperationen (Linien aus Mitgliedschaft und Folgen). Eine Community kann hinter einer Instanz stehen; die Karte zeigt beides getrennt. Heute: Partnerkacheln auf der Startseite, Communities-Ansicht `#communities`, Issue „Anordnung im Ökosystem". |
| **Echt** | Communities aus `kind:10222` (Communikey-Relay), Mitgliedschaften aus `kind:30000`/`h`-Tags, Akteure aus `kind:0`, Folgen aus `kind:3`. |
| **Belege** | #81 (OER-Worldmap, abgeschlossen), Communities-Ansicht im Prototyp, ADR-0002, Fäden „Ökosystembegriff", „Anordnung", „Blume". |
| **Lücke** | Keine Karte der Verknüpfungen; die Communities-Liste ist ein Schnappschuss. |
| **Stufe** | A: Communities-Liste live vom Relay. B: Karte der Kooperationen. |

### 4.2 Standards und Abläufe über den Hub zugänglich

| | |
|---|---|
| **Zusage** | M34 (AP 3-3): Zentrale Ergebnisse (Standards zu Metadaten, Redaktionsabläufen, Prozessabläufen) sind über den Community-Hub öffentlich zugänglich und weiter nutzbar. AZ 3: Qualitätskriterien werden „in den Community-Hub integriert". |
| **Funktion** | hub (Schaufenster FOERBICO) |
| **Hub-Element** | Bereich „Spielregeln" `#oercommunity/spielregeln` mit vier Seiten: Qualitätskriterien (Handreichung, vier Dimensionen, Checklisten); Metadatenprofil religionsbezogen (AMB-Mapping, SKOS-Vokabulare auf nocabs.edufeed.org, nostr-konform mit AMB-Passung); Redaktionsmodell (Entwürfe, Freigabe per NIP-32-Label, Bildnachweis-Konvention, Kalender-Konvention); Prozessabläufe (vom Beitrag im Git bis zum Relay, von der Webseite zum Termin). |
| **Echt** | Seiten als `kind:30023` vom FOERBICO-Schlüssel mit Seiten-Label, wie oer.community sie schon ausliefert (ADR-0027 im oer-community-Repo). Der Hub liest dieselben Events. |
| **Belege** | oer.community/qualitaet (CC BY 4.0), #543 (SKOS-Vokabular), #535 (AMB-Standards), #840 (Bildnachweise), #843/#844 (Redaktionsmodell ADR-0021), Kalender-Guide bei edufeed, Blogbeiträge „Working Out Loud". |
| **Lücke** | Im Hub gibt es den Bereich nicht; die Inhalte liegen verstreut auf oer.community, GitHub und in Issues. |
| **Stufe** | A. |

### 4.3 Erweiterter Metadatenstandard am Material sichtbar

| | |
|---|---|
| **Zusage** | M14 (AP 4-2): Eine Erweiterung OER-konformer Metadatenstandards steht bereit. AP 4-2: erweiterbare Schemata, Import/Export-Schnittstellen. |
| **Funktion** | finden |
| **Hub-Element** | Material-Detailansicht im Materialpool `#materialpool?d=…`: AMB-Felder (Fach, Bildungsstufe, Lernressourcentyp, Zielgruppe) mit Link auf das Vokabular, Lizenzpille, Bildnachweis, Rohdaten-Knopf (JSON-LD nach AMB, aus dem `kind:30142`). Der Lizenzstand bestimmt sichtbar, was geht: offen lizenziert = auf den Schreibtisch holen, in der Community weiterbearbeiten, in Sammlungen aufnehmen; geschützt = ansehen und verlinken. So wird die Hinführung zu OER im Hub erfahrbar, nicht nur erklärt. |
| **Echt** | `kind:30142` vom amb-Relay, Vokabular-Links auf nocabs.edufeed.org, AMB-Rückausgabe über amb-nostr-converter. |
| **Belege** | #543, #535, #846 (Abstimmung x-Tags, ai-Tag), #191/#30 (Bilddaten), amb-religionsbezogen (edufeed-org), Community-Call AMB-NIP 08.10.2025. |
| **Lücke** | Der Prototyp zeigt einen Schnappschuss ohne Vokabular-Links und ohne Rohdaten. |
| **Stufe** | A. |

### 4.4 Editor für maschinenlesbare OER

| | |
|---|---|
| **Zusage** | M23 (AP 4-3/4-4): Mit einem frei verfügbaren formularbasierten Editor oder als CMS-Plugin können Communities ihre OEP/OER erfassen und maschinenlesbar für Kataloge wie WLO bereitstellen. Usertutorial, open source. |
| **Funktion** | veröffentlichen |
| **Hub-Element** | `#veroeffentlichen/lerninhalte`: der Lerninhalt-Editor des Prototyps (Bereichswahl, sieben Schritte) führt beim Launch an den echten edufeed-Ressourceneditor (`/create/resource`) weiter; die Schritte des Prototyps bleiben als Erklärung davor, aber nur im Tutorial-Modus der Konsole. Wer die Konsole kennt (nach Anmeldung oder „verstanden"), landet direkt in der Aktion (Issue „Menüeintrag führt direkt zur Aktion"). Daneben die Werkzeugliste „Drei Wege zum Relay": Formular im Browser (edufeed), Git-Weg (foerbico-editor), aus WordPress (`nostr-publish` heute für Beiträge; das Eingabeformular-Plugin für AMB-Ressourcen kommt in der Woche ab dem 09.11.2026). Tutorial-Seite im Bereich Spielregeln. |
| **Echt** | Veröffentlichung in `kind:30142`/`30023` über den edufeed-Editor mit SKOS-Vokabular. Der eigene Hub-Editor bleibt bis zur Svelte-Stufe Nachbau mit Weiterleitung. |
| **Belege** | #843 (md2blossom, blossom-bunker, foerbico-editor), `nostr-publish` und das angekündigte Eingabeformular-Plugin (wp-plugins-nostr), #302 (OERSI-Routine), #310 (OERSI-Formular), #382 (OERSI-WordPress-Plugin), #312 (TeachCenter-Plugin), Kanban-Editor und LiaScript aus dem OE_Sprint (eigene Förderung, als Open Source nutzbar). |
| **Lücke** | Kein Tutorial; der Prototyp-Editor speichert nichts; das WordPress-Eingabeformular ist in Arbeit. |
| **Stufe** | A: Weiterleitung, Werkzeugliste und das WordPress-Eingabeformular als dritter Weg, sobald es veröffentlicht ist (erwartet Mitte November). B: Tutorial. C: eigener Editor im Svelte-Stack. |

### 4.5 Portal-Client: Sammlungen filtern und auf der eigenen Seite zeigen

| | |
|---|---|
| **Zusage** | M30 (AP 4-5): Ein frei verfügbares Plugin (Portal-Client) ermöglicht es, Sammlungen von OER aus den Communities zu filtern und auf der eigenen Instanz abzubilden. AP 4-5: OER filtern, abonnieren, als Sammlung auf einer Community-Webseite ausgeben. |
| **Funktion** | finden |
| **Hub-Element** | Ansicht „Sammlung" `#finden/sammlung?…`: Filter nach Community, Fach, Bildungsstufe, Lizenz; Ergebnis als Liste; drei Ausgänge: abonnieren (RSS/Atom und Nostr-Liste), einbetten (zwei Wege: Code-Schnipsel der Steuerkonsole mit `config-src`-Kontextprofil, das genau diesen Filter trägt, und der passende `[amb_nostr …]`-Shortcode für WordPress-Seiten), teilen (naddr). Das WordPress-Plugin `amb-nostr` ist der Portal-Client des Antrags: Sammlungen aus den Communities filtern und auf der eigenen Instanz abbilden; die Konsole als eigenständiges Skript ist die Hub-Fassung davon. Dazu kommt die Leiste als eigenständiges Widget (Issue „Leiste unten links als eigenständiges Widget"): die Klammer, die eine Partner-Instanz mit anderem Software-Stack einbindet und sie im Ökosystem hält. |
| **Echt** | `kind:30142` gefiltert über Relay-Abfragen; Sammlungen als `kind:30004`-Kuratierungslisten; Feed wie auf oer.community (ADR im oer-community-Repo). |
| **Belege** | `amb-nostr`, `longform-nostr`, `nostr-calendar` (wp-plugins-nostr, Releases, Editor-Anleitung für Themenseiten, im Einsatz bei ALPIKA-Arbeitsgruppen), #844 (Artikel-Detailansicht als OER-Client-Durchstich), #845 (Feed, Sitemap), oer-finder-plugin (WordPress, NLQ), NavigatOER (HackathOERn 2026), Steuerkonsole als Web Component mit `config-src`-Attribut (vorgesehen, ungenutzt). |
| **Lücke** | Meilenstein AP 4-5 hat nur #844; die Plugins sind dort nicht als Beleg eingetragen. Keine Filteransicht, keine Einbettung, kein Abonnement im Hub. |
| **Stufe** | A: Sammlung mit Filtern und Einbetten-Schnipsel. B: Abonnieren als Nostr-Liste. |

### 4.6 Dezentrale Kataloge je Community

| | |
|---|---|
| **Zusage** | AP 4-6: Implementierung dezentraler, zielgruppenorientierter OER-Kataloge auf der gemeinsamen Datenbasis; plattformunabhängige Zusammenstellung, redaktionelle Aufbereitung, kontinuierliche Aktualisierung über den Hub. |
| **Funktion** | finden, kooperieren |
| **Hub-Element** | Katalog-Seite je Community `#community?c=…&zu=katalog`: kuratierte Sammlungen der Community (Redaktionskreis pflegt `kind:30004`), Stand und Aktualisierungsdatum sichtbar, derselbe Einbetten-Schnipsel wie in 4.5. Der Materialpool ist der Katalog der Community rpi-virtuell. |
| **Echt** | Fünf Kataloge beim Launch mit echten Listen: rpi-virtuell (Materialpool), FOERBICO (Beiträge und Seiten von oer.community), reliGlobal, relilab und ALPIKA Grundschule mit ihren bestehenden Community-Schlüsseln (Schlüssel beim Projektteam; Bestand und Aktivität in `Hub-Entwicklung/communities-schluessel.md`). Der Materialpool-Katalog wächst mit den von Hand neu angelegten Materialien; der Erstimport wurde verworfen (04.11.2026). |
| **Belege** | Materialpool-Entwicklung (Svelte-Schaufenster, Formularentwicklung), #845 (Kuratierungslisten `kind:30004` für Menü und Fußzeile), Community-Struktur bei edufeed (Reposts mit `h`-Tag), reliGlobal- und KuRU-Anbindung. |
| **Lücke** | Meilenstein AP 4-6 ist leer. Kein Katalog-Begriff im Hub. |
| **Stufe** | A: fünf echte Kataloge. B: Redaktionsoberfläche für Listen im Hub. |

### 4.7 Weitere Communities eingebunden

| | |
|---|---|
| **Zusage** | AP 4-7: Gewinnung und Einbindung weiterer OER-Communities; freiwillige Öffnung und Bereitstellung von Metadaten; Moderation gemeinsamer Kataloge. AZ 1: auch andere Konfessionen, nicht-religionsbezogene Communities. |
| **Funktion** | kooperieren |
| **Hub-Element** | Communities-Ansicht `#communities` mit echten Communities und ihrem Status (Mitglied, folge ich, Partner ohne Schlüssel). Partnerkacheln für Communities ohne eigenen Schlüssel. |
| **Echt** | `kind:10222` je Community; Partner ohne Schlüssel als Kachel mit Link. |
| **Belege** | Zwischenbericht 2025 (rpp-katholisch, Konfessionskundliches Institut, EKD-Fachstelle Friedensbildung, relimentar, reliGlobal), Communities reliGlobal und KuRU bei edufeed, #822 (narrt), efabi, BiK-Termine, Partnerliste im Prototyp. |
| **Lücke** | Welche Partner einen eigenen Schlüssel bekommen, ist nicht entschieden; die Prototyp-Liste ist ein Schnappschuss. |
| **Stufe** | A: Liste live, Partner als Kacheln. |

### 4.8 Unterstützung nach Bedarf

| | |
|---|---|
| **Zusage** | M14/M26 (AP 5): Bedarfe und Standards bilden die Grundlage konkreter Unterstützungsmaßnahmen; Zwischenevaluation liegt vor. AP 5-2: Werkzeuge und Ressourcen in Community-Plattformen, Schulungen, Nutzenden-Feedback. AP 2-4: technische Unterstützung, Verweis auf Fortbildungen, Good Practices. |
| **Funktion** | kooperieren (Vorschlag: mitmachen) |
| **Hub-Element** | Servicepoint `#servicepoint`: Beratung (Kontaktweg, Sprechstunde), Werkzeugkasten (die Werkzeuge aus 4.4 plus Vorlagen), Good Practices (Blogbeiträge mit Marker), Feedback (Kommentare nach NIP-22 aus dem Vertrauenskreis, Spec liegt im oer-community-Repo). |
| **Echt** | Werkzeuge und Good Practices als Nostr-Seiten und Listen; Feedback als `kind:1111`. |
| **Belege** | Faden „Servicepoint / Chatbot", Faden „Braucht es noch Tools?", #362 (KI-Kompetenzen-Workshop), #667 (Forum/Chat openreli), #512 (Onboarding-Anleitung reliGlobal), Beratungen laut Zwischenbericht (RPI EKKW/EKHN, PTI, PI Villigst, AKD, Nelson-Mandela-Schule), M26-Zwischenevaluation: Blogbeitrag „Was die Communities brauchten" aus den Beratungs-Issues. |
| **Lücke** | Kein Servicepoint im Hub; die Zwischenevaluation M26 ist nicht als Text vorhanden. |
| **Stufe** | A: Servicepoint-Seite mit Kontakt und Werkzeugkasten. B: Feedback per Kommentar. C: Chatbot. |

### 4.9 Fortbildung: zwei Logiken, ein Kalender

| | |
|---|---|
| **Zusage** | M28 (AP 6-3): Die ALPIKA-Institute haben OER in Fortbildung und Publikationspraxis implementiert. M17 (AP 6-1): Formate ausgerollt. AZ 5: OER-erfahrene Akteure erschließen anderen die Potentiale. |
| **Funktion** | finden (Fortbildungen), kooperieren |
| **Hub-Element** | Fortbildungskalender über alle Quellen `#finden/fortbildungen` (heute „später" außerhalb des relilab-Kontexts). Zwei Logiken, bewusst unterschieden, nicht hart getrennt: die institutionelle Fortbildung über rpi-virtuell als virtuelles Fortbildungsinstitut (Anmeldung, klare Verantwortung, Fachperson vermittelt, Teilnahmebescheinigung, territorial gebunden) und die Laborlogik des relilab (offen ohne Anmeldung, kostenfrei, online, Impuls und Werkstatt, Unfertiges erlaubt, Ergebnisse unter freier Lizenz). Die Steuerung läuft über Relayzuordnung und Taxonomien (Felder für Anmeldung, Kosten, Präsenz/Online/Hybrid aus #696), nicht über getrennte Kalender; Laborformate erscheinen auch unter Fortbildungen. Die Instanz rpi-virtuell ist der Einstieg zu den Institutsformaten und zeigt unter „finden" die globale Sicht: alle Fortbildungen aller Institute. „Fortbildungen" bekommt in der Konsole denselben Platz wie auf der Startseite (Issue „dieselben Begriffe"). Administrative Bedürfnisse (Anmeldelisten, Bescheinigungen) werden in der Institutslogik bedient, nicht im Labor. Community-Seite ALPIKA mit sechsstufiger OER-Checkliste und den Institutsangeboten. |
| **Echt** | `kind:31922/31923` vom Kalender-Relay, Kalender-Konvention von edufeed. |
| **Belege** | #293 (ALPIKA-Leitendentagung 09/2025), #538/#505 (PTZ, Schuldekane), #692 (relilab-Termine nach edufeed), BiK-Import, KuRU-Anbindung, #696 (Kalender-Formate), #199 (Community-Kalender), Gesprächskonsens 03.11.2026 (Kriterien beider Logiken), `nostr-calendar` als Ausgabeweg für Institutsseiten. |
| **Lücke** | Kein Kalender über alle Quellen im Hub; ALPIKA Grundschule hat seit 11.09.2026 Community und Schlüssel, aber noch keine Seite im Hub; die Taxonomie für die beiden Logiken ist noch nicht in der Kalender-Konvention. |
| **Stufe** | A: Kalender live. B: ALPIKA-Community-Seite. |

### 4.10 Personen und Profile

| | |
|---|---|
| **Zusage** | M34 (AP 9-5): Communities und Akteure erstellen eindeutige, standardisierte Profile, vernetzen sich darüber, verweisen auf eigene OEP/OER, verbinden das Profil mit sozialen Netzwerken wie Mastodon; json-ld, w3id. M36 (AP 2-4): Community-Management etabliert. |
| **Funktion** | hub (Profil), kooperieren (Personen) |
| **Hub-Element** | Personen-Ansicht `#kooperieren/personen` (heute „später"): Profile aus dem Netzwerk mit Rolle, Community-Zugehörigkeit, eigenen Veröffentlichungen, Folgen-Knopf. Profil-Ansicht `#profil` mit echtem Profil statt Kunstfigur; Personas als echte Nostr-Profile (Faden vom 02.11.). Mastodon-Verbindung über die Nostr-ActivityPub-Brücke (mostr) als Hinweis im Profil. |
| **Echt** | `kind:0`, `kind:3`, Veröffentlichungen per Autor-Abfrage; Web-ID = npub; Vokabulare auf nocabs.edufeed.org (der w3id-Anlauf wurde verworfen). |
| **Belege** | Faden „Personas als echte Nostr-Profile", Faden „Mehrwert", #26 (dezentrales ID-Verfahren), keycloak-nostr-plugin (Onboarding bestehender rpi-virtuell-Konten), Onboarding-Tool aus dem OE_Sprint, `nostr-publish` (wp-plugins-nostr). |
| **Lücke** | Personen-Ansicht fehlt; Anmeldung ist ein Link. Der WordPress-Multisite-Profildienst wird nicht gebaut; an seine Stelle treten Nostr-Profile plus `nostr-publish`, das Beiträge einer WordPress-Seite automatisch mit dem Hub verbindet, genau die Zusage aus M34 (AP 9-5). |
| **Stufe** | A: Personen-Ansicht mit den Profilen der hauptamtlichen Teams (CI, rpi-virtuell, Verbund), weitere Personen nach Einverständnis. B: Anmeldung per Signer (NIP-07/NIP-46). |

### 4.11 Kerndienste von rpi-virtuell im Hub

| | |
|---|---|
| **Zusage** | M34 (AP 9-2): Kerndienste von rpi-virtuell (Zielgruppen, Praxismaterialien, Bildungsnews, Blogs) sind vollständig mit dem Hub verbunden; OER, Communities, Akteure haben Web-IDs, sind standardisiert beschrieben, automatisch verlinkt und über API in beliebige Portale importierbar. |
| **Funktion** | alle (Instanzen-Kacheln) |
| **Hub-Element** | Instanzen als Nachbau (ADR-0002) mit echten Daten. Neu: rpi-virtuell als eigene Instanz in der Leiste, in rpi-virtuell-Farben, die die rezeptive Logik bündelt und die Kerndienste des Antrags genau abbildet: Materialpool (`#materialpool`, Quelle: Svelte-Schaufenster material.rpi-virtuell.net und amb-Relay), Fortbildungskalender (4.9), Bildungsnews und Blogs; relilab als Labor (`#relilab`, Trias Materialien, Menschen, Mitmachen: Praxisentwürfe und Unterrichtsversuche aus dem Labor gleichrangig neben Institutsprodukten, offene Veranstaltungen, öffentlicher Kommunikationsraum aus 4.19), daneben relilab als Labor und relidesk (`#relidesk`, Nachbau gekennzeichnet). Beiträge in `#finden/beitraege`; communitybezogene Sammlungen liegen wie ein Filter über dem globalen Datenraum. API-Weg sichtbar: „Diese Daten holen" mit Relay-Filter und AMB-Rückausgabe, OERSI-Brücke. |
| **Echt** | Relays plus amb-nostr-converter; Bildungsnews und Blogs über `nostr-publish` auf den WordPress-Instanzen von rpi-virtuell. |
| **Belege** | Materialpool-Neustart (Svelte, seit 28.09.2026), #842 (Nostr-Sync der Beiträge), #692 (relilab-Termine), #772 (OERSI-Brücke), #120/#121 (OER-Worldmap, OERinfo), Hub-Entwicklung „Gedanken aus 1 Jahr". |
| **Lücke** | rpi-virtuell gibt es noch nicht als Instanz in der Leiste; Bildungsnews und Blogs von rpi-virtuell sind nicht nach Nostr syndiziert; relidesk hat keine Datenquelle. |
| **Stufe** | A: Materialpool und relilab echt, Beiträge von oer.community echt. B: Bildungsnews/Blogs per `nostr-publish`. C: relidesk. |

### 4.12 Materialpool-Metadaten überarbeitet

| | |
|---|---|
| **Zusage** | M36 (AP 9-4): Praxishilfen im Materialpool sind überarbeitet und berücksichtigen die vereinbarten Metastandards; maschinenlesbar, bei jedem Material sichtbar; json-ld; API-Kompatibilität mit Redaktionssystem und WLO. |
| **Funktion** | finden |
| **Hub-Element** | In 4.3 enthalten; zusätzlich ein Zähler im Materialpool „n von m Materialien mit vollständigen Metadaten" und der Hinweis „Vorschlag per KI, geprüft von der Redaktion" (Kuratierungstool). |
| **Echt** | `kind:30142` der migrierten Materialien; Zähler aus der Relay-Abfrage. |
| **Belege** | #670 (Erfassungsoberfläche), #841/#865 (Bildmigration), #286 (Nostr-Experimente), #341 (OERSI), Formularentwicklung an Beispielmaterialien, KI-Kuratierungstool laut Zwischenbericht 2025. |
| **Lücke** | Anteil migrierter Materialien unbekannt; der Zähler macht ihn sichtbar und ehrlich. |
| **Stufe** | A: Zähler und Detailansicht. |

### 4.13 Qualitätskriterien im Gebrauch

| | |
|---|---|
| **Zusage** | M18/M33 (AP 7): Standards in evaluierter Fassung; Endergebnisse des DBR-Prozesses zur Fazit-Tagung. AZ 3: Rating-Tools, Feedback-Prozesse. |
| **Funktion** | finden, veröffentlichen |
| **Hub-Element** | Lizenzpille an jedem Bild und Material (vorhanden auf oer.community, ADR-0032), Qualitätskriterien-Seite (4.2), Checkliste als Schritt im Editor (4.4), Marker „geprüft nach Kriterien" an Materialien mit NIP-32-Label. |
| **Echt** | Labels `kind:1985` oder Label-Tags am Event durch den Redaktionskreis. |
| **Belege** | Handreichung oer.community/qualitaet, TiRU (OER-Preis HessenHub 2025), #787 (Syslex), Qualitätsdimensionen im geschlossenen Repo (rechtlich, technisch, methodisch-didaktisch, religionspädagogisch), OER-Ampel. |
| **Lücke** | Kein Prüf-Marker im Hub. |
| **Stufe** | A: Lizenzpille und Kriterien-Seite. B: Prüf-Marker. |

### 4.14 Open-Access-Zeitschriften im Hub

| | |
|---|---|
| **Zusage** | M25 (AP 8-5): Kontakt zu den Open-Access-Publikationsformaten etabliert, für OER/OEP sensibilisiert; OJS-zu-OERSI-Wege. |
| **Funktion** | finden |
| **Hub-Element** | Artikel in `#finden/beitraege` (ADR-0005): Theo-Web, WiReLex, RpB, ÖRF als Quellen mit Lizenzstand. |
| **Echt** | `kind:30142` der Zeitschriftenartikel (amb-sitemap-parser), sonst gekennzeichnete Beispielartikel. |
| **Belege** | Austausch 20.03.2025 (Zwischenbericht), Theo-Web-Artikel, amb-sitemap-parser bei edufeed-org, #772 (OERSI-Brücke). |
| **Lücke** | Ob Zeitschriftenartikel als Events vorliegen, ist zu prüfen. |
| **Stufe** | B. |

### 4.15 Prozesse und Ergebnisse dokumentiert

| | |
|---|---|
| **Zusage** | AP 3: der Hub „dokumentiert die Prozesse und Ergebnisse des Projektes nachhaltig". M4 (AP 1-3/1-4): Kommunikationsstrategie. AP 11-4: Monitoring der Vernetzungs- und Entwicklungsprozesse. |
| **Funktion** | hub (Schaufenster FOERBICO) |
| **Hub-Element** | Schaufenster `#oercommunity` mit Blog (Working Out Loud, 90+ Beiträge), Tagungen, Team, Termine-Archiv (vergangen und anstehend, #199), Erschließungs-Layer (Abschnitt 5), Link auf den Issue-Tracker als offenes Projektlogbuch. |
| **Echt** | Beiträge, Seiten, Termine vom FOERBICO-Schlüssel; Schaufenster-Inhalte heute als Schnappschuss `OC_POSTS`/`OC_TAGUNGEN`/`OC_TEAM`. |
| **Belege** | #845 (oer.community aus Nostr), #842 (Sync), 42 Blogbeiträge 2025 laut Zwischenbericht, Issue-basierte Steuerung (410 Issues 2025). |
| **Lücke** | Schnappschuss statt Relay; Termine-Archiv fehlt; die Erschließungs-Layer gibt es nicht. |
| **Stufe** | A. |

### 4.16 Kollaborationsumgebung

| | |
|---|---|
| **Zusage** | M4 (AP 9-3): dezentral nutzbare Kommunikations- und Kollaborationsumgebung (Chat, Projektmanagement, Git, Entwicklungsserver, Schnittstellen, KI-Zugänge). |
| **Funktion** | hub |
| **Hub-Element** | Fußzeile „Mitarbeiten": Forgejo, Matrix, gitworkshop (Hub-Entwicklung über Nostr), Entwicklungsserver-Hinweis. |
| **Echt** | Links. |
| **Belege** | #82 (Git), #1 (Adressbuch), #130 (Ordnerstruktur), #551/#559 (Entwicklungsserver), Poutník-Werkzeug und ngit. |
| **Lücke** | Keine. |
| **Stufe** | A, trivial. |

### 4.17 Technische Bedarfe und konfigurierbare Umgebung

| | |
|---|---|
| **Zusage** | AP 9-1: technische Entwicklungsbedarfe der Communities erheben; prüfen, ob ein generisches Framework Communities erlaubt, „ihre OEP/OER-Umgebung per Klick auszuwählen und zu konfigurieren". |
| **Funktion** | kooperieren |
| **Hub-Element** | Seite „Eigene Instanz" `#eigene-instanz`: Kontextprofil wählen (Partner), Vorschau von Steuerkonsole und Leiste mit diesem Profil, Schnipsel zum Einbetten; die Leiste als spezifiziertes Widget (Daten: Instanzen, Communities, aktuelle Instanz, Profil), konfigurierbar je Community (was auf der eigenen Instanz erscheint) und je Person (Plus, Minus, Anordnung), mit Vorauswahl beim Start; Verweis auf White-Label-Betrieb der edufeed-App über Umgebungsvariablen und auf die WordPress-Plugins als Weg für Communities mit eigener WordPress-Seite. Bedarfserhebung als Seite: Ergebnis der Konsultation (#276) und der Konzeptionstage. Dazu eine Vorlage „Kooperationsvereinbarung": technisch (Daten rein und raus: Relay, Plugins, Schlüssel) und als Arbeitsbündnis (Ansprechpersonen, Kanäle, Mitverantwortung), damit das Onboarding der Institute in geteilte digitale Räume einen festen Rahmen hat. |
| **Echt** | `config-src`-Kontextprofile als JSON je Partner; Vorschau echt im Browser. |
| **Belege** | Konstruktionsbeschreibung (Kontextprofile, `config-src`), Design „Repo hub" (White-Label, 118 Umgebungsvariablen), Issues „Leiste als eigenständiges Widget" und „Leiste konfigurierbar" (starkes Votum des UX-Gastes: so bauen, dass andere Stacks sie implementieren können), #276 (Konsultation, offen), #144/#331 (Konzeptionstage), #174 (technischer Entwicklungsschwerpunkt). |
| **Lücke** | Meilenstein AP 9-1 ist leer. Die Konsultation (#276) hat nicht stattgefunden. Welche Regel über die Aufnahme in die Leiste entscheidet, ist offen (Faden „Anordnung"). |
| **Stufe** | B: Seite mit Kontextprofilen. Die Bedarfserhebung läuft über die Fäden auf gitworkshop, die Rückmeldungen der Zwischenfazit-Tagung und Beobachtungen; #276 wird damit belegt und geschlossen. Eine Konsultation im Januar bleibt optional als Feinschliff. |

### 4.18 Fazit-Tagung und Launch

| | |
|---|---|
| **Zusage** | M34 (AP 10-2): Fazit-Tagung durchgeführt; M33/M34: Standards und Hub-Ergebnisse dort öffentlich nutzbar; idealiter Auftakt der assoziierten AG. |
| **Funktion** | hub |
| **Hub-Element** | Launch-Pfad: eine Startseiten-Variante `#start?tour=traeger` mit geführtem Klickweg durch die Zeilen 4.1 bis 4.20 (Gallery Walk, #780). Der Klickweg nutzt den Tutorial-Modus der Konsole (Issue „Menüeintrag führt direkt zur Aktion"): dieselbe Mechanik, die Neue durch den Hub führt, führt die Person vom Projektträger durch die Zusagen. |
| **Echt** | Der Hub selbst. |
| **Belege** | #779 (Launch), #777 (Wrap-Up), #780 (Gallery Walk), #781 (Outcomes). |
| **Lücke** | Kein geführter Pfad. |
| **Stufe** | A. |

### 4.19 Öffentlicher Kommunikationsraum

| | |
|---|---|
| **Zusage** | AP 3: Community-übergreifende Kommunikations- und Kollaborationsinstrumente, „die über den Hub zugänglich gemacht werden". M35 (AP 6-4): Kommunikations- und Vernetzungsstrukturen sind etabliert. AP 2-4: Community-Management regt Diskussionen an, bringt Akteure zusammen. |
| **Funktion** | kooperieren (Vorschlag: mitmachen) |
| **Hub-Element** | Öffentlicher Raum `#mitmachen`: der offene Gesprächsfaden des Ökosystems als Nachfolger des früheren öffentlichen Raums, aus dem das relilab entstand. Beiträge, Rückfragen und Rückmeldungen zu Materialien, Terminen und Artikeln an einem Ort, nach Community filterbar; „Mitmachen" im relilab-Schaufenster zeigt denselben Raum im Labor-Zuschnitt. Der gemeinsame Datenraum macht sichtbar, was im Labor entsteht und was sich bei den Instituten bewegt. |
| **Echt** | Kommentare nach NIP-22 (`kind:1111`) an Materialien, Terminen und Artikeln; kurze Beiträge (`kind:1`) mit Community-Bezug (`h`-Tag); Lesen ohne Anmeldung, Schreiben mit Schlüssel. Spec und ADR-0041 für Kommentare liegen im oer-community-Repo (ungemergt). |
| **Belege** | Gesprächskonsens 03.11.2026 (Abschnitt 7), Faden „rpi-virtuell eigene Community?", #140 (Kommentare auf oer.community), #667 (Forum/Chat openreli), Communikey-Community rpi-virtuell mit Redaktionskreis. |
| **Lücke** | Kein öffentlicher Raum im Hub; die Kommunikation ist über Instagram, Newsletter, Chat und Webseite verstreut. Brücken: zum Fediverse über die Nostr-ActivityPub-Brücke vorhanden, zu Instagram keine; offene Frage aus dem Konsens. |
| **Stufe** | B: Lesen und Filtern; Schreiben über die edufeed-App. C: Schreiben im Hub. |

### 4.20 Startseite und Onboarding: die Haltung erzählen

| | |
|---|---|
| **Zusage** | AP 3-3: Bewerbung des Hubs und Vermittlung seiner Funktionalität in die Communities hinein. AZ 5: niederschwellige Angebote, OER-erfahrene Akteure erschließen anderen die Potentiale. AZ 1: Verständnis für offene Praktiken erweitern. |
| **Funktion** | hub |
| **Hub-Element** | Startseite `#start` mit einem Narrativ, das die Haltung trägt: ein Institut und zugleich eine Mitmachmöglichkeit; Offenheit und offene Praktiken als das, was das Ganze strukturiert; Einladung, sich zu zeigen, Inhalte zu teilen, zu Terminen einzuladen; Hinführung zu OER als Weg, nicht als Bedingung. Konsole schon auf der Startseite verankert (Issue „Konsole auf der Startseite verankern"), Modi per Mouse-Over erschließbar, Tutorial-Modus vor der Anmeldung, direkter Einstieg danach. Onboarding mit Schlüssel über das edufeed-Onboarding-Tool und keycloak-nostr-plugin für bestehende rpi-virtuell-Konten. |
| **Echt** | Texte als Nostr-Seite vom FOERBICO-Schlüssel oder im Hub-Code (Produkttexte); Onboarding echt über edufeed. |
| **Belege** | Fäden „Storytelling fehlt" (mit Kommentar vom 03.11.: Institut plus Mitmachen), „Mehrwert", „Slogan", „Personas als echte Nostr-Profile", Issues „Konsole auf der Startseite", „direkt zur Aktion"; Beobachtung des UX-Gastes: die Gestaltung erzählt die Haltung schon, der Text muss nachziehen. |
| **Lücke** | Der heutige Satz „Startplatz in die digitale Welt der Religionspädagogik" beschreibt einen Ort, keine Haltung. Name der Startseite (reli_hub oder rpi-virtuell-Hub) offen. |
| **Stufe** | A: Narrativ und Konsole auf der Startseite. B: Mouse-Over, Animation zwischen Konsole und Blume. |

## 5. Der Erschließungs-Layer für den Projektträger

Arbeitstitel „Erschließungs-Layer"; der endgültige Titel ist offen (Abschnitt 9). Kein Hub-Inhalt für alle, sondern ein eigenes Schaufenster mit eigener Navigation, das dem Fördermittelgeber separat bereitgestellt wird: erreichbar über einen direkten Link und aus dem FOERBICO-Schaufenster, nicht aus der Steuerkonsole.

Aufbau:

- Eigene Ansicht `#erschliessung` in der schwarzen Prototyp-Leiste neben dem FOERBICO-Schaufenster, mit eigener Navigation: die sechs Arbeitsziele des Antrags als Gliederung, darunter die Zusagen (Abschnitt 4) als Einträge.
- Je Zusage ein Eintrag: die Zusage in den Worten des Antrags (M-Nummer klein in Klammern), „Im Hub:" mit Link auf die Route, die sich in der Hauptansicht öffnet, „Belege:" mit Links auf Blogbeiträge, Nachweis-Issues, Repos, ADRs; bei Stufe B oder C der Vermerk „in Arbeit, Stand <Datum>" oder „Nachbau, gekennzeichnet".
- Einleitung in drei Sätzen (was FOERBICO versprochen hat, was der Hub ist, wie man liest) und Schluss: was über den Antrag hinausging und was anders kam als geplant, mit Verweis auf den Zwischenbericht 2025. Die Einleitung trägt das Leitbild: OEP als Herzstück, Hinführung zu OER, Communities und Instanzen als Bausteine, Marken hinter Strukturen.
- Ein Knopf „Klickweg starten" führt den geführten Weg aus Zeile 4.18.

Inhalt und Code bleiben getrennt: Der Hub-Code rendert eine Gliederung aus `kind:30023`-Seiten mit Label (eine Seite je Arbeitsziel, vom FOERBICO-Schlüssel über die Sync-Pipeline). Arbeitspakete und M-Nummern stehen im Inhalt, nicht im Code. Die Seiten liegen als Markdown im FOERBICO-Repo unter `Website/content/de/seiten/` und erscheinen damit auch auf oer.community, dort aber nicht in der Navigation.

## 5a. Inhaltsstrang: wer liefert, wer signiert

„Echt" braucht Events, die teils noch fehlen. Der Inhaltsstrang läuft neben dem Code-Strang mit eigenen Fristen:

| Inhalt | Form | Schlüssel und Weg | Wer schreibt | Frist |
|---|---|---|---|---|
| Spielregeln-Seiten (4.2): Qualitätskriterien, Metadatenprofil, Redaktionsmodell, Prozessabläufe | vier `kind:30023`-Seiten mit Seiten-Label | FOERBICO-Schlüssel über die Sync-Pipeline (Markdown im FOERBICO-Repo, Signatur in der CI) | Claude entwirft aus den vorhandenen Texten (Handreichung, SKOS-Repo, ADR-0021, Konventionen), Jörg und die Redaktion lesen gegen | 30.11.2026 |
| Erschließungs-Layer (5) | sechs `kind:30023`-Seiten, eine je Arbeitsziel | wie oben | Claude entwirft, Jörg liest gegen | Entwurf 09.11., final 23.12.2026, Stände im Januar nachgeführt |
| Katalog FOERBICO (4.6) | `kind:30004`-Listen | FOERBICO-Schlüssel, Listen aus der Pipeline wie Menü und Fußzeile von oer.community | Claude legt an, Redaktion kuratiert | 21.12.2026 |
| Katalog rpi-virtuell (4.6) | `kind:30004`-Listen | Community-Schlüssel rpi-virtuell (Communikey-Community mit Redaktionskreis `kind:30000`, besteht seit 09/2026) | Materialpool-Redaktion (rpi-virtuell-Team); Materialien werden nach dem verworfenen Erstimport qualitätskriteriengeleitet von Hand neu angelegt | 21.12.2026 |
| Kataloge reliGlobal, relilab und ALPIKA Grundschule (4.6) | `kind:30004` | bestehende Community-Schlüssel (beim Projektteam, Stand 04.11.2026) | Community mit Begleitung durch Community-Management und Redaktion | 23.12.2026 |
| Servicepoint, Werkzeugkasten, Good Practices (4.8) | Seiten und Listen | FOERBICO-Schlüssel | Claude entwirft, Jörg liest gegen | 15.01.2027 |
| M26-Text „Was die Communities brauchten" (4.8) | Blogbeitrag | FOERBICO-Schlüssel | Claude entwirft aus den Beratungs-Issues beider Repos, ohne Personennamen; Jörg liest gegen | 15.01.2027 |
| Termine ALPIKA und Institute (4.9) | `kind:31923` | bestehende Importe (BiK, KuRU, relilab); ALPIKA-Termine über den FOERBICO-Schlüssel, bis ALPIKA einen eigenen hat | Jörg sammelt, Claude trägt ein | laufend |
| Zähler migrierter Materialien (4.12) | keine neuen Events; Abfrage | amb-Relay | Materialpool-Entwicklung | 30.11.2026 |
| Echte Profile (4.10) | `kind:0` der Personen | eigene Schlüssel der Personen | zuerst die hauptamtlichen Teams, weitere nach Einverständnis (wird gerade geklärt) | 23.12.2026 |

Solange es im Hub keine Redaktionsoberfläche für Listen gibt (Stufe B), pflegt Claude die Listen des FOERBICO-Schlüssels über die Pipeline; die rpi-virtuell-Listen pflegt das Team mit der edufeed-App.

Community-Management und Redaktion sind personeller Aufwand neben der Technik (Gespräch 03.11.). Der Inhaltsstrang braucht deshalb eine feste Wochenzeit der Rollen Öffentlichkeitsarbeit/Redaktion und Community-Management; ob Strukturen vital werden, hängt von der Resonanz der Beteiligten ab und lässt sich nicht durch Technik ersetzen.

## 6. Buchführung in Forgejo

Je Hub-Meilenstein ein offenes Nachweis-Issue im offenen Repo (Label `Nachweis`, Meilenstein gesetzt), nach der Regel aus der Nachweislogik (Meilensteine bleiben offen, Nachweis-Issues tragen die Checkliste):

| Meilenstein (Forgejo-ID) | Nachweis-Issue enthält |
|---|---|
| AP 3-2 + 3-3 (83) | Zeilen 4.1, 4.2, 4.15, 4.18; Links auf reli_hub-Repo, Pages-URL, ADRs, Konstruktionsbeschreibung, Fäden |
| AP 4-2 (88) | Zeile 4.3; SKOS-Vokabular, AMB-Mapping, Community-Call |
| AP 4-3 + 4-4 (90) | Zeile 4.4; Werkzeuge, `nostr-publish`, Eingabeformular-Plugin mit Herkunftsvermerk (Beitrag des Comenius-Instituts aus Eigenmitteln) |
| AP 4-5 (99) | Zeile 4.5; #844, `amb-nostr` als Portal-Client (Repo, Releases, Einsatz bei ALPIKA), Sammlung und Einbettung |
| AP 4-6 (115), bisher leer | Zeile 4.6; die Kataloge |
| AP 4-7 (101) | Zeile 4.7; Community-Liste mit Status |
| AP 5-1 + 5-2 (89, 97) | Zeile 4.8; Beratungs-Issues als Belege, M26-Text |
| AP 6-3 (100) | Zeile 4.9 |
| AP 9-1 (87), bisher leer | Zeile 4.17; Kontextprofile, White-Label, Konsultation |
| AP 9-2 (8) | Zeile 4.11 |
| AP 9-4 (118) | Zeile 4.12 |
| AP 9-5 (16) | Zeile 4.10; `nostr-publish` als Profil-Plugin, Begründung Nostr-Profile statt Multisite |
| AP 2-4 (121) | Zeile 4.8, 4.10 und 4.19 (Community-Management) |
| AP 3 (7) | Zeile 4.19; Kommunikationsinstrumente über den Hub |
| AP 6-4 (14), geschlossen | Zeile 4.19 als Nachtrag zu M35; Meilenstein bleibt geschlossen, das Nachweis-Issue verweist |

Vorhandene Issues (#844, #845, #843, #842, #199, #696, #276, #700) werden den Nachweis-Issues verlinkt, nicht verschoben. Issues ohne Meilenstein, die Belege sind (z. B. #789 Blogbeiträge CI in Edufeed), bekommen rückwirkend den Meilenstein. Das geschlossene Repo bekommt nichts Neues aus dieser Konzeption; Betriebsfragen (Relay, Server, Domain) bleiben dort.

## 7. Issues auf gitworkshop (Hub-Sprache)

Die acht Issues der dritten Runde (03.11.2026: Kreis-Klick, Beschriftungen, direkt zur Aktion, Begriffe und Farben, Konsole auf der Startseite, Leiste als Widget, Leiste konfigurierbar, mobil) liegen schon im Repo und kommen zuerst. Aus den Zeilen dieser Konzeption entstehen weitere Issues, formuliert als Angebot für Nutzende, ohne AP- oder M-Nummern, jeweils mit Verweis auf die Runde-3-Issues, an die sie anschließen. Vorschlag der Titel, je ein Issue:

1. Sammlung: filtern, abonnieren, einbetten (4.5)
2. Katalog je Community mit Stand und Pflege (4.6)
3. Spielregeln: Qualitätskriterien, Metadatenprofil, Redaktion, Abläufe als Hub-Seiten (4.2, 4.13)
4. Material-Detail: AMB-Felder, Vokabular-Links, Rohdaten, Zähler (4.3, 4.12)
5. Fortbildungskalender über alle Quellen mit zwei Logiken in einer Taxonomie (4.9)
6. Personen-Ansicht und echte Profile (4.10, ergänzt den Personas-Faden)
7. Ökosystem-Karte aus Communities, Mitgliedschaften, Folgen (4.1, ergänzt die Fäden Anordnung und Ökosystem)
8. Veröffentlichen: Weiterleitung an den echten Editor, drei Wege zum Relay, Tutorial (4.4)
9. Servicepoint: Beratung, Werkzeugkasten, Good Practices, Feedback (4.8, ergänzt den Servicepoint-Faden)
10. Schaufenster live vom Relay: Beiträge, Seiten, Termine-Archiv (4.15)
11. Eigene Instanz: Kontextprofil wählen, Konsole einbetten (4.17)
12. Erschließungs-Layer als eigenes Schaufenster mit geführtem Klickweg (5, 4.18)
13. Live-Abfrage der Relays mit Schnappschuss als Rückfall, Kennzeichnung „Nachbau" (Querschnitt)
14. Öffentlicher Raum „Mitmachen": Kommentare und Beiträge lesen und filtern (4.19)
15. Lizenzstand bestimmt, was mit einem Material geht (4.3, Leitbild)
16. relilab-Schaufenster als Labor: Materialien, Menschen, Mitmachen (4.11)
17. rpi-virtuell als eigene Instanz in der Leiste: Materialpool, Fortbildungskalender, News gebündelt, in rpi-virtuell-Farben (4.11, 4.9; aus dem Kommentar im Faden „rpi-virtuell eigene Community?")
18. Startseiten-Narrativ: Institut und Mitmachen, Offenheit als Struktur (4.20; aus dem Kommentar im Faden „Storytelling fehlt")

Anschlüsse: 1 und 11 an „Leiste als Widget" und „Leiste konfigurierbar"; 5 an „dieselben Begriffe" (Fortbildungen in der Konsole); 7 an „Anordnung"; 12 an „direkt zur Aktion" (Tutorial-Modus); 17 an die Leisten-Issues; 18 an „Konsole auf der Startseite".

Jedes Issue verweist auf die betroffenen ADRs und schlägt vor, ob ein neues ADR nötig ist (sicher für 13, 1 und 3). Veröffentlichung durch Poutník nach Durchsicht der Entwürfe.

## 8. Fahrplan bis zum Launch

| Wann | Was | Ergebnis |
|---|---|---|
| bis 09.11.2026 | Nachweis-Issues in Forgejo (Abschnitt 6), gitworkshop-Issues (Abschnitt 7), Ersatz-ADR für 0002, Entwurf des Erschließungs-Layers, Community-Schlüssel für reliGlobal und relilab anlegen | Buchführung und Hub-Backlog stehen, leere Meilensteine belegt, Arbeit verteilt. **Erledigt am 04.11.2026:** Nachweis-Issues #879 bis #893 in Forgejo; 18 Hub-Issues und 6 Kommentare auf gitworkshop (Runde 4); ADR-0006 gemergt; Erschließungs-Entwurf `Hub-Entwicklung/erschliessung-entwurf/`; Schlüsselliste `Hub-Entwicklung/communities-schluessel.md` (die Schlüssel bestanden bereits, anzulegen sind nur die Katalog-Listen) |
| bis 16.11.2026 | Navigation rund schleifen: die acht Runde-3-Issues (Konsole, Leiste, Startseite, mobil), rpi-virtuell als Instanz (17), Startseiten-Narrativ (18); parallel Querschnitt 13 (Live-Abfrage mit Rückfall) | Startseite, Konsole und Leiste konsistent; 17./18.11. Fachtagung Frankfurt, Team vor Ort. **Erledigt am 04.11.2026:** 13 Pull Requests von Poutník auf gitworkshop gemergt (`main` 21ae08b, live unter hub.rpi-virtuell.net): Datenschicht mit Live-Abfrage und Schnappschuss (13), Konsole aktivieren/treffer/direkt/mobil/startseite (01, 02, 03, 08, 05), Leiste als Widget und konfigurierbar (06, 07), rpi-virtuell-Instanz (17), Begriffstabelle (04), Narrativ (18), Doku und Nacharbeit aus der Gesamt-Review; elf Kommentare auf den Issues (Runde 5). Plan `docs/superpowers/plans/2026-11-05-hub-etappe-2-navigation.md`, Übergabe `Hub-Entwicklung/2026-11-05-etappe-2-uebergabe.md`. Offen: Schnappschuss-Erneuerung vor dem 16.11., Abnahme mit dem UX-Gast am 25.11. |
| bis 24.11.2026 | Zeilen 4.2, 4.3, 4.15 (Spielregeln, Material-Detail, Schaufenster live); Inhaltsstrang: Spielregeln-Seiten; 25.11. Stand an den UX-Gast und Folgetermin | Der Hub zeigt echte Inhalte. **Erledigt am 04.11.2026:** 7 Pull Requests von Poutník auf gitworkshop gemergt (`main` 255b295, live unter hub.rpi-virtuell.net): Inhalte aus Events mit sicherer Markdown-Darstellung und Lizenzstand (ADR-0007), Schaufenster live mit Seiten, Beiträgen und Termine-Archiv (10), Bereich Spielregeln (03), Materialpool live als kind:30142 mit Zähler für vollständige Metadaten und Material-Detail mit Vokabular-Links, Rohdaten und Lizenzstand als Schalter für die Aktionen (04, 15), Doku und Nacharbeit aus der Gesamt-Review; vier Kommentare auf den Issues (Runde 6). Die vier Spielregeln-Seiten liegen als Entwurf unter `Website/content/de/spielregeln-*/`, Gegenlesen bis 30.11., bis dahin zeigt der Bereich „in Vorbereitung“. Plan `docs/superpowers/plans/2026-11-06-hub-etappe-3-inhalte.md`, Übergabe `Hub-Entwicklung/2026-11-24-etappe-3-uebergabe.md`. Offen: Schnappschuss-Erneuerung vor dem 16.11., Abnahme mit dem UX-Gast am 25.11. |
| bis 07.12.2026 | Zeilen 4.5, 4.6, 4.9, 4.10 (Sammlung, Kataloge, Kalender, Personen); Inhaltsstrang: Kataloglisten, Profile | Die leeren Meilensteine haben ihr Hub-Element. **Erledigt am 05.11.2026:** 7 Pull Requests von Poutník auf gitworkshop gemergt (`main` 2ea71041, Nostr und Forgejo): Community-Inhalte über den `h`-Tag als Grundschicht der Kataloge (Kuratierungslisten `kind:30004` als zweite Schicht, keine Rollenprüfung, Entfernen-Label nur vom Community-Schlüssel, ADR-0008), Sammlung `#finden/sammlung` mit Filtern, Teilen, Einbetten (Shortcode, Kontextprofil) und Abonnieren als Nostr-Filter (1), Katalog-Tab je Community (2), Fortbildungskalender `#finden/fortbildungen` über 14 Quellen plus Community-Zuordnung mit Labor- und Institutslogik als Merkmalen (5), Personen `#kooperieren/personen` und `#person` aus einer Personen-Liste mit Einverständnis (6), Doku und Nacharbeit aus der Gesamt-Review; vier Kommentare auf den Issues (Runde 7). Korrektur zur Konzeption: Kataloge brauchen keine angelegten Listen, das Geteilte der Communities ist die Grundschicht (Gespräch 05.11.). Plan `docs/superpowers/plans/2026-11-07-hub-etappe-4-sammlung-kataloge.md`, Übergabe `Hub-Entwicklung/2026-12-07-etappe-4-uebergabe.md`, Bedarf `Hub-Entwicklung/2026-11-07-etappe-4-bedarf-team.md`. Offen: Personen-Liste und Profile (Team), FOERBICO-Katalog über `navigation.yaml`, Repost-Vorschläge, Env-Datei, Schnappschuss vor dem 16.11. |
| bis 23.12.2026 | Zeilen 4.1, 4.4, 4.7, 4.8, 4.17, 4.18 und Erschließungs-Layer (5); Stufe B; Inhaltsstrang: Servicepoint, M26-Text, Termine | **Hub fertig.** Alle A- und B-Zeilen echt oder gekennzeichnet. **Teil 5a erledigt am 10.11.2026:** 8 Pull Requests von Poutník auf gitworkshop gemergt (`main` a1a1d836, Nostr und Forgejo, ausgeliefert): Beziehungsgefüge aus den Events und Ansicht „Ökosystem“ `#oekosystem` mit vier Reihen, Communities-Liste live mit Partnerkacheln (4.1, 4.7); Raum „Mitmachen“ `#mitmachen` mit Aktivitätsprotokoll als einziger dauerhafter Subscription (4.19); relilab als Labor (4.11); Zuschnitt des Hubs über `?c=<npub>` und Seite „Eigene Instanz“ (4.17); Anmeldung per NIP-07 mit Folgen, Beitreten, Zusagen, Gefällt mir und Sammlung als Liste (Stufe B von 4.5, 4.10, 4.19; Listen nur nach vollständiger Antwort aller drei Relays, Folgen mit Rückfrage); ADR-0009. 6 Kommentare auf gitworkshop (Runde 8), 7 Kommentare auf den Nachweis-Issues. Offen aus 5a: Durchlauf des Sendens von Hand, Partnerentscheidung zu 4.7, Kooperationsvereinbarung und Bedarfsseite (Entwürfe). **Teil 5b offen:** 4.4, 4.8, 4.16, 4.18, Erschließungs-Layer (5), Konsole als eigenständiges Skript. Übergabe: `Hub-Entwicklung/2026-12-07-etappe-5a-uebergabe.md` |
| Januar 2027 | Feinschliff: Probelauf mit einer außenstehenden Person, Korrekturen, Stände im Erschließungs-Layer nachgeführt, Nachweis-Issues aktualisiert, optional Konsultation; 29.01. Tag und eingefrorene Kopie | Launch-fähig |
| 2./3.02.2027 | Launch auf der Fazit-Tagung | Hub-Launch (#779), Gallery Walk (#780) |
| Feb.–Apr. 2027 | Stufe C, Svelte-Unterbau, Domain, Nachweis-Issues schließen den Kreis zum Abschlussbericht | Verstetigung |

Jede Zeile wird einzeln als PR nach `main` gemergt und nach Forgejo gepusht; der Container unter hub.rpi-virtuell.net liefert aus. Am 29.01.2027 wird der Stand getaggt und als eingefrorene Kopie abgelegt (Abschnitt 3).

Rückfallreihenfolge, wenn der 23.12. in Gefahr gerät: Zuerst fallen 4.17 (eigene Instanz), 4.1 (Karte) und 4.8 (Servicepoint) auf gekennzeichneten Nachbau zurück, dann 4.4 (Veröffentlichen bleibt Weiterleitung) und 4.10 (Personen als Liste ohne Folgen). Nicht verhandelbar sind 4.2, 4.3, 4.5, 4.6, 4.9 und 4.15, weil sie die leeren Meilensteine und M34 tragen.

## 9. Entscheidungen von Jörg und offene Punkte

Entschieden am 02.11.2026:

- Der Hub ist der Nachweis; die Person vom Projektträger klickt sich durch.
- Echt, wo es geht; Inhalte werden nachgeliefert oder aufgefüttert; Nachbau gekennzeichnet.
- Fertig bis Weihnachten 2026, Januar nur Feinschliff.
- Team: fünf Personen (Community-Management, technische Umsetzung, Öffentlichkeitsarbeit und Redaktion, Konzeption, edufeed-/relidesk-Entwickler) und die Coding-Agenten Poutník und antiope.
- Die WordPress-Plugins aus wp-plugins-nostr sind Beleg, mit klarem Herkunftsvermerk: Beitrag des Comenius-Instituts aus Eigenmitteln (Anstellung des Entwicklers), nicht Edufeed, nicht FOERBICO-Personal; das Eingabeformular-Plugin folgt in der Woche ab dem 09.11.
- Community-Schlüssel für reliGlobal, relilab und ALPIKA Grundschule bestehen und liegen beim Projektteam (Stand 04.11.2026); ALPIKA Grundschule ist damit der fünfte Katalog.
- Bedarfserhebung über gitworkshop, Tagungsrückmeldungen und Beobachtungen; Konsultation im Januar optional.
- Echte Profile: zuerst die hauptamtlichen Teams, weitere werden gerade abgeklärt.
- Der Nachweis ist ein eigenes Schaufenster mit eigener Navigation, separat für den Fördermittelgeber bereitgestellt (Erschließungs-Layer, Titel offen).

Konsens des Teams vom 03.11.2026 (Gespräch zu relilab und Hub):

- Hub = integratives Ganzes mit OEP als Herzstück; Hinführung zu OER statt Eintrittsbedingung.
- relilab = Experimentalraum im Hub mit festen Kriterien; institutionelle Fortbildungslogik über rpi-virtuell; fließende Übergänge über Relays und Taxonomien.
- Communities, Instanzen, Ökosystem sind drei Dinge; Marken treten hinter Strukturen zurück.
- Der öffentliche Kommunikationsraum kommt über Nostr zurück (Trias Materialien, Menschen, Mitmachen).
- Steuerungslogik gehört nicht in die Nutzernavigation; Fünfgliedrigkeit bleibt, Benennung offen.

Konsens aus der Hub-Erkundung mit UX-Außenblick vom 03.11.2026:

- Grundaufbau bestätigt: Hub als Klammer, Instanzen mit eigenem Gesicht, fünf Erschließungsmodi; Überlappungen der Modi sind gewollt.
- Zwei Navigationselemente mit zwei Funktionen: Leiste (Instanzen, Communities) und Konsole (Modi), als verschiedene Dinge erkennbar; die Leiste als eigenständiges Widget für andere Stacks.
- rpi-virtuell als eigene Instanz in der Leiste (rezeptive Bündelung, Institutslogik), relilab als Labor-Instanz; Wortbildmarke rpi-virtuell bleibt.
- Zwei Wochen HTML-Prototyp ohne Stack, dann Stand an den Gast; Folgetermin 25.11.2026.

Meine Festlegungen (Claude), die Jörg beim Lesen prüft:

- Launch-Stack ist der HTML-Prototyp mit Live-Abfrage, nicht der Svelte-Unterbau (Abschnitt 3).
- Die WordPress-Plugins sind FOERBICOs Plugins, gebaut vom edufeed-Entwickler in seiner Anstellung am Comenius-Institut (Eigenmittel); die vier Plugins aus wp-plugins-nostr belegen die WordPress-Zusagen, das Eingabeformular-Plugin kommt als Stufe A dazu (Abschnitt 2, 4.4, 4.5).
- Der Erschließungs-Layer liest seine Inhalte als Nostr-Seiten vom FOERBICO-Schlüssel; der Hub-Code kennt keine Arbeitspakete (Abschnitt 5).
- Vier echte Kataloge beim Launch (Abschnitt 4.6).
- Nachweis-Issues nur im offenen Repo; das geschlossene bleibt Betrieb (Abschnitt 6).
- Jörg mergt als Maintainer; Einwände laufen über die gitworkshop-Issues, nicht vor dem Merge (Abschnitt 3).
- Querschnitt mit gebündelten Abfragen und frischem Schnappschuss am Launch-Tag wegen der Relay-Sperre (Abschnitt 3).
- Eingefrorene Launch-Kopie unter fester Adresse für Prüfungen nach dem Launch (Abschnitt 3).
- Inhaltsstrang mit Zuständigkeiten und Schlüsseln (Abschnitt 5a); Claude entwirft die Texte, Jörg und die Redaktion lesen gegen.
- Rückfallreihenfolge im Fahrplan (Abschnitt 8).

Offen, nur Jörg kann entscheiden:

- Der Titel des Erschließungs-Layers („Was wir versprochen haben" gefällt nicht). Vorschläge: „Antrag und Hub", „Zusagen", „Nachweis", „Vom Antrag zum Hub".
- Ob weitere Partner (rpp-katholisch, Konfessionskundliches Institut, relimentar) bis zum 23.12. einen Schlüssel bekommen oder als Partnerkachel ohne Schlüssel erscheinen (Fragen 4 bis 6 in `Hub-Entwicklung/communities-schluessel.md`).

Offen im Team (aus dem Gespräch vom 03.11., nicht in dieser Konzeption zu entscheiden):

- Wie viel Community-Management künftig ins relilab fließt.
- Die Relation relilab zu rpi-virtuell.
- Eine gemeinsame Definition von „Ökosystem" (Faden „Ökosystembegriff nicht passend").
- Der Termin, an dem der Konsens ausformuliert und in die Navigation überführt wird; bis dahin bauen wir Inhalte und Elemente, keine endgültige Benennung.
- Die Verben der fünf Modi (Faden „Blume", Kommentar vom 03.11.: Modi als Haltung lesen: explorieren, Anschluss suchen, all in gehen).
- Welche Regel über die Aufnahme in die Leiste entscheidet und was die Vorauswahl ist.
- Der Name der Startseite: reli_hub oder rpi-virtuell-Hub (Faden „Selbstverständnis").
- Brücken des öffentlichen Raums zu Instagram und Fediverse.

## 10. Was dem Bauenden überlassen bleibt

- Die Relay-Abfragen im Prototyp: Bibliothek oder roher WebSocket, Zeitlimits, Reihenfolge der Relays, Form des Rückfalls. Vorgabe: ohne Build, eine Datei, Rückfall auf den Schnappschuss, Kennzeichnung sichtbar.
- Gestaltung der neuen Ansichten innerhalb des Farbsystems (ADR-0001) und der Konsolen-Logik.
- Aufteilung der Issues in PRs; Reihenfolge innerhalb einer Fahrplan-Stufe.
- Form der Einbetten-Schnipsel und des `config-src`-JSON.
- Wortlaut der Hub-Texte; die Antragsformulierungen erscheinen nur auf der Erschließungs-Layer.
