# Hub-Erkundung 03.11.2026: UX/UI Beratung

Grundlage: Protokoll der gemeinsamen Erkundung des reli-hub-Prototyps (HTML-Fassung mit
Steuerkonsole) mit einem Gast mit Außenblick aus UX- und Design-Perspektive und dem FOERBICO-Projektteam. 

***tldr:*** Der Grundaufbau überzeugt: Hub als Klammer, Instanzen mit eigener Identität, fünf
Erschließungsmodi in der Blume. Die Arbeit der nächsten zwei Wochen liegt in der Navigation:
Blume, Leiste unten links und Startseite müssen klarer zueinander stehen, Klickwege kürzer
werden, und rpi-virtuell braucht einen eigenen Platz als Instanz. Folgetermin 25.11.2026.

## 1. Konsenspunkte

### Gesamtaufbau

- **Hub als Klammer, Instanzen mit eigenem Gesicht.** Die Startseite hat ihren Look, die
  Unterseiten (Materialpool, relilab, relidesk) treten in eigener Wortbildmarke und Farbe auf. Das erzeugt kein Störgefühl, sondern Lust, in die Bereiche hineinzugehen. Diese Offenheit
  erzählt die Haltung des Projekts bereits durch die Gestaltung selbst.
- **Jeder Zugang ist ein Startpunkt ins Ökosystem.** Wer relilab kennt, findet dort sofort sein
  Zuhause und braucht den Materialpool daneben zunächst nicht. Wer nur Material sucht, hat über den Materialpool einen geradlinigen Weg. Beide sind gut aufgehoben.
- **Fokussierte Bereiche funktionieren.** Der Materialpool ist klar, weil er auf eine Aufgabe
  fokussiert. Die anderen Frontends sollen nach demselben Prinzip ausgestaltet werden: Was ist die primäre Aufgabe, für die dieses Frontend gebraucht wird?
- **Mehrere Frontends auf demselben Datenbestand.** Das Grundverständnis, dass verschiedene Oberflächen dieselben Daten mit anderer Relevanz zeigen und dass Partner eigene Frontends beisteuern können, vermittelt sich schon beim Durchklicken, ohne die Technik zu kennen.
- **Die Fünfteiligkeit der Blume ist tragfähig.** Finden, Erstellen, Kooperieren,
  Veröffentlichen plus Hub als Organisationsform. Die Überlappungen zwischen den Modi sind
  konzeptionell gewollt: Ein Termin soll Leute zum Material führen, Material soll zum Mitmachen einladen, aus personaler Kommunikation sollen Communities entstehen.
- **Die Wendekarten gefallen.** Communities ohne Instanz dürfen gelistet sein, eine Instanz ist keine Voraussetzung.

### Zwei Navigationselemente, zwei Funktionen

- **Leiste unten links** = Instanzen, Communities, vorkonfigurierte Dinge. Sie ist das mitgehende Widget, das den Wechsel zwischen Instanzen ermöglicht und einen dennoch im Ökosystem hält: Man ist woanders und doch im Gleichen.
- **Blume unten rechts** = Erschließungsmodi (finden, erstellen, kooperieren, veröffentlichen), adaptiv auf die jeweilige Instanz bezogen.
- **Starkes Votum:** Die Leiste unten links als eigenständiges Widget so entwickeln, dass auch andere Software-Stacks eine Implementation davon machen können.

### rpi-virtuell im Hub

- rpi-virtuell ist nicht der Hub als Ganzes. Der Hub ist die Klammer um relilab, rpi-virtuell,
  relimentar, FÖRBICO und weitere.
- rpi-virtuell steht für die institutionelle Fortbildungslogik der religionspädagogischen Institute: Anmeldung, Kosten, Teilnahmebescheinigungen, komplementäre Kooperation der
  Institute. relilab ist der Experimentalraum: kostenfrei, anmeldefrei, informell, Laborcharakter.
- Die Wortbildmarke rpi-virtuell bleibt. Gestalterisch ist das Team frei, rpi-virtuell neu zu fassen.
- Die Startseite muss das Narrativ tragen: ein Institut und zugleich eine Mitmachmöglichkeit,
  Offenheit und offene Praktiken als strukturgebendes Prinzip, Einladung, sich zu zeigen und
  Inhalte zu teilen.

### Vorgehen

- Die nächsten zwei Wochen wird nur die HTML-Seite rund geschliffen, ohne Software-Stack. Ziel:
  Die Navigationslogiken sollen aus Nutzersicht konsistent und intuitiv sein, bevor die Programmierung mit größerem Stack beginnt.
- Issues werden im Nostr-basierten Git gesammelt (gut 20 Stück vorhanden). Aus dem Blume-Feedback entstehen drei bis vier weitere.
- Was edufeed schon kann (KI-Unterstützung, Chatbot, Formulare), wird danach implementiert.

## 2. Ideen

### Blume und Steuerkonsole

- **Ein Klick weniger:** Wer einen Kreis aktiviert, bekommt sofort die zugehörige Info-Box.
  Heute bleibt die Box beim vorherigen Modus, bis man den Menüpunkt zusätzlich anklickt.
- **Farben der Startseite in die Konsole holen:** Material, Fortbildungen, Beiträge in der
  Konsole in der Farbe ihres Modus zeigen, damit die Verbindung zur Startseite entsteht.
- **Beschriftung klickbar machen:** Gelernt ist, auf den Menüpunkt zu klicken, nicht nur auf den Pfeil oder das Symbol. Mobil zusätzlich größere Trefferflächen.
- **Unmittelbarer Einstieg für Geübte:** Menü öffnen, „Beitrag erstellen" wählen, direkt im Editor landen. Nicht erst auf der Blume und dann noch einmal auf einer Blume.
- **Mouse-Over statt Klick** auf der Startseite, um die Modi zu erschließen.
- **Stängel oder Pfeil:** Eine Dynamik von der Ecke unten rechts zur mittleren Blume (oder
  umgekehrt), die sich zurückzieht, damit klar ist, dass die Blume einen begleitet und nicht erst auf einer Unterseite entdeckt werden muss.
- **Blume schon auf der Startseite einführen:** Platz unten rechts früh etablieren, damit das Element eingelernt ist. Die Startseiten-Erklärungen können darauf verweisen: „Diesen Button findest du immer hier."
- **Tutorial- und Navigationsmodus:** Vor Anmeldung erklärt die Konsole sich selbst wie ein Tutorial. Nach Anmeldung geht sie direkt in die Funktion. Die Erklärung bleibt unter Hilfe
  erreichbar.

### Leiste unten links

- **Konfigurierbar pro Community:** relilab kann auf seiner Seite andere Erweiterungen zeigen
  oder relidesk und FOERBICO ausblenden, weil sie für relilab-Leute nicht relevant sind.
- **Konfigurierbar pro Person:** Plus/Minus, Seiten-Konfiguration, per Drag-and-Drop den
  eigenen Hub zusammenstellen. Initial wird eine Auswahl angeboten.
- **Startbedingung statt Vollständigkeit:** Die Leiste ist mit FOERBICO am Ende der
  Fahnenstange (Platz limitiert). Für reliGlobal, relimentar und weitere braucht es entweder eine Regel, was hinein darf, oder die Leiste wird einmalig beim Start konfiguriert.

### rpi-virtuell und Startseite

- **rpi-virtuell als eigene Instanz bauen,** in der Farbgebung von rpi-virtuell, in der Leiste
  neben oder zwischen relilab und relidesk. So wird die Kontur zwischen Institutslogik und
  Laborlogik sichtbar, nicht nur in der Logo-Logik, sondern in der Ausrichtungslogik.
- **rpi-virtuell als globale Sicht unter Finden:** Fortbildungen = alle Fortbildungen aller
  Institute, Material = alles aus allen Instituten und dem gesamten Datenraum. Communitybezogene Materialsammlungen liegen wie ein Filter über dem globalen Datenraum.
- **Die fünf Modi als Haltung lesen:** Explorieren und Rumschauen, Anschluss finden und sich
  involvieren lassen, all in gehen mit eigenem Profil und eigenen Inhalten. Das wäre der
  Erschließungsmodus aus Nutzersicht.

## 3. Entwicklungsaufgaben

Kandidaten für Issues im reli-hub-Repo. Nummerierung nur für die Verständigung hier.

1. **Kreis-Klick aktualisiert die Info-Box sofort.** Desktop und mobil. Heute: gelber Kreis
   aktiv, Box zeigt noch rot „Kooperieren", erst Klick auf „Erstellen" wechselt.
2. **Beschriftungen klickbar, Trefferflächen vergrößern.** Klick auf „Personen" oder „Mein
   Profil" tut nichts, nur der Pfeil reagiert. Mobil ist das Element zu klein.
3. **Doppelte Blume beseitigen.** Klick auf die Blume führt zu einer Seite mit nochmals der
   Blume. Stattdessen: Menüeintrag führt direkt zur Aktion.
4. **Navigationspunkte abgleichen.** Startseite (Material, Fortbildungen, Beiträge), Blume und
   Leiste müssen dieselben Begriffe und Bezüge tragen. Fortbildungen fehlen in den Unterseiten.
   „Lerninhalte" führt nirgendwo in die Leiste; der Weg sollte in den Materialpool springen, dort
   wo man einen Eintrag macht.
5. **Farbkodierung der Konsole an die Startseite angleichen.**
6. **Blume auf der Startseite verankern.** Platz, Einführungs-Animation (Stängel oder Pfeil),
   Verweis aus den Erklärtexten.
7. **Steuerkonsole als eigenständiges, einbettbares Widget spezifizieren,** sodass andere
   Software-Stacks sie implementieren können.
8. **Leiste konfigurierbar machen:** Community-Ebene (Einträge ein- und ausblenden) und
   Personen-Ebene (Plus/Minus, Drag-and-Drop, initiale Auswahl).
9. **Leiste und Blume unterscheidbar machen.** Instanzen und Communities links, Modi rechts.
   Die Doppelnavigation ist sperrig, solange der Unterschied nicht sichtbar ist.
10. **rpi-virtuell-Instanz anlegen** in rpi-virtuell-Farben, Platz in der Leiste, mit der
    Institutslogik (Anmeldung, Kosten, Bescheinigungen) als Kontur gegenüber relilab.
11. **Startseiten-Narrativ überarbeiten:** Institut plus Mitmachen, Offenheit und offene
    Praktiken als Struktur, Einladung zum Zeigen und Teilen. Der Satz „Startplatz in die
    digitale Welt der Religionspädagogik" reicht nicht.
12. **Verben der fünf Modi nachschärfen.** Veröffentlichen und Erstellen liegen eng beieinander,
    ebenso Finden und Kooperieren. Alternativen: teilen, mitmachen, unterstützen.
13. **Mobiles Verhalten prüfen:** Sprung nach unten beim Klick, Rücksprung zum Schreibtisch,
    Treffsicherheit mit dem Finger, Wahrnehmbarkeit der Änderung unten.
14. **Tutorial- und Hilfe-Modus:** Selbsterklärung vor Anmeldung, direkte Funktion danach,
    Hilfe-Seite zum Nachschauen.
15. **Mouse-Over-Erschließung auf der Startseite** statt Klick-Pflicht.

### Veröffentlicht am 03.11.2026 als Poutník im reli-hub

Acht neue Issues, vier Kommentare zu bestehenden Issues, untereinander verlinkt. Texte und
JSON-Antworten unter `~/.config/poutnik/protokolle/issue-kommentare-2026-11-03/`.

| Kandidat oben | Ort |
|---|---|
| 1 Kreis-Klick | [Issue „Konsole: Klick auf einen Kreis aktualisiert die Info-Box sofort“](https://gitworkshop.dev/nevent1qqsp834vzk0hje2g9r07qe3ku6le2fp2en8c2p073hq7pnkpuzvqdwcpz3mhxue69uhhyetvv9ujumn8d96zuer9wcsjwgxp) |
| 2 Beschriftungen | [Issue „Konsole: Beschriftungen klickbar machen“](https://gitworkshop.dev/nevent1qqsw28x9epe2g3yqm4g8wlg9nauzes74ekq38fnnzwa0fe05565xgtgpz3mhxue69uhhyetvv9ujumn8d96zuer9wct6py7w) |
| 3, 14 Doppelte Blume, Tutorial-Modus | [Issue „Konsole: Menüeintrag führt direkt zur Aktion“](https://gitworkshop.dev/nevent1qqsxqf0vjkzcwyzhmnvxd3xvj6slwv4m7pjgck3gyle9efe3hcka0xqpz3mhxue69uhhyetvv9ujumn8d96zuer9wcfl7k8a) |
| 4, 5, 15 Begriffe, Farben, Mouse-Over | [Issue „Startseite, Konsole und Leiste: dieselben Begriffe“](https://gitworkshop.dev/nevent1qqsdtunutkfmkyd0a089njasw0vzwcsdhrzmke45hlgzxyrjvdvxu3qpz3mhxue69uhhyetvv9ujumn8d96zuer9wcudxxnd) |
| 6 Blume auf der Startseite | [Issue „Konsole auf der Startseite verankern“](https://gitworkshop.dev/nevent1qqsrptpnt0aa66ud5cq5vglz5jzf3dgsp3388xfhgv25ddlsdegzy9qpz3mhxue69uhhyetvv9ujumn8d96zuer9wchfaufg) |
| 7, 9 Widget, Abgrenzung | [Issue „Leiste unten links als eigenständiges Widget“](https://gitworkshop.dev/nevent1qqsfemwgkmvzwuh0mjfu0zqrrw9dlrs30qgp63utjdd4urr53u7gh4qpz3mhxue69uhhyetvv9ujumn8d96zuer9wcdym00l) |
| 8 Konfigurierbar | [Issue „Leiste konfigurierbar: pro Community und pro Person“](https://gitworkshop.dev/nevent1qqs0rlvwkw67ws7k7hge2g63zlavmct6e6gf6z66jewxyjv3lsx4jygpz3mhxue69uhhyetvv9ujumn8d96zuer9wc5k79nv) |
| 13 Mobil | [Issue „Konsole mobil“](https://gitworkshop.dev/nevent1qqs0d92cequxrlprjydys5ldykcffc09n6d8x526jayu2kev4yup6xgpz3mhxue69uhhyetvv9ujumn8d96zuer9wcp6v528) |
| 12 Verben | [Kommentar im Issue „Blume als Menüführung irreführend“](https://gitworkshop.dev/nevent1qqs8zkxcqgtukg3mq4ktywdkdah0gnr0h06sfkvle8ymwftegs0anmspz3mhxue69uhhyetvv9ujumn8d96zuer9wcscazz9) |
| 10 rpi-virtuell-Instanz | [Kommentar im Issue „rpi-virtuell eigene Community?“](https://gitworkshop.dev/nevent1qqsrrrwdycn0cgssz3sw0w7xhh2rms7cdmm9jmk67jele6wamqe7tfqpz3mhxue69uhhyetvv9ujumn8d96zuer9wcgnsvmx) |
| 11 Startseiten-Narrativ | [Kommentar im Issue „Storytelling fehlt“](https://gitworkshop.dev/nevent1qqsvggznc8ku46fu69dc98wfrqu6gtcy0qsgz3knagjz9jum4nxzqqqpz3mhxue69uhhyetvv9ujumn8d96zuer9wc2zlzm8) |
| Name der Startseite (offene Frage) | [Kommentar im Issue „Profil / Selbstverständnis klären“](https://gitworkshop.dev/nevent1qqsq698etkl573austf2l9ln5rdx5mcwncyawfsg37eld54m7kfsazspz3mhxue69uhhyetvv9ujumn8d96zuer9wc9htuqk) |

## 4. Offene Fragen

- **Welche Verben für die fünf Modi?** Wie werden Finden und Kooperieren, Erstellen und
  Veröffentlichen trennscharf, ohne die gewollten Überlappungen zu verlieren? Das Team hat den
  Schlüssel noch nicht. 
- **Was darf in die Leiste?** Welcher Unterscheidungsfaktor entscheidet über Aufnahme, wenn
  reliGlobal, relimentar und weitere dazukommen?
- **Konfiguration über Community, über Person oder beides?** Und was wird initial angeboten?
- **Wie stehen Blume und Leiste zueinander?** Stängel, Dynamik, Rückzug: Was macht die Beziehung
  sichtbar, ohne zu viel zu werden?
- **Blume auf der Startseite:** Dient sie dort dem Überblick, dem Schnellzugriff oder beidem? Ist
  das dann schon wieder etwas anderes als auf den Unterseiten?
- **Ist die Anmeldung der Umschalter** zwischen erklärender und direkter Konsole?
- **Wo liegt rpi-virtuell in der Blume?** Unter Kooperieren, als globale Sicht unter Finden, als
  eigene Instanz in der Leiste, oder mehreres zugleich? Wortmarken und Symbole sind noch nicht
  trennscharf.
- **Name der Startseite:** reli-hub, weil er in mehr hineinführt als rpi-virtuell, oder
  rpi-virtuell-Hub, weil die Marke bleiben soll? Im Gespräch wurde beides gesagt und nicht
  entschieden.
- **Partner-Frontends in der Nostr-Welt:** Wie zeigt sich das Ökosystem, wenn ein Partner ein
  eigenes Frontend auf denselben Datenbestand setzt?

## 5. Verabredungen

- Zwei Wochen HTML-Prototyp rund schleifen, dann dem Gast einen Stand schicken.
- Fachtagung in Frankfurt am 17. und 18.11.2026, Projektteam vor Ort. Am Abend des 17.11.
  möglicherweise ein Get-Together als Meetup, Gast gibt Bescheid.
- Folgetermin: **25.11.2026, 9:30 bis 10:30 Uhr** (vor dem edufeed-Meeting um 10:30 Uhr).
