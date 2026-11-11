# OE_COM-Transferworkshop 27.11.2026 – Entwurf für Kachel und Pitch

Online (Webex), 10:00–13:45. FOERBICO ist in **Block D**, zusammen mit VEStOR und MiKa.
Abgabe Conceptboard: **20.11.2026** (Bereich 1: Pitch, Bereich 2: Dokumentation).

Bitte im Team gegenlesen, vor allem die Teile, die TP 2 und TP 3 betreffen.

---

## Bereich 1: Pitch (1 Minute, ca. 140 Wörter gesprochen)

**Das hatten wir uns vorgenommen.**
Religionsbezogene OER-Communities (rpi-virtuell, relilab, reliGlobal, ALPIKA-Institute und weitere) sollten nicht mehr nebeneinander arbeiten, sondern als „Community of Communities“ ihre Materialien, Termine und Praktiken über einen gemeinsamen Community-Hub teilen.

**Das ist tatsächlich entstanden.**
Eine gemeinsame, offene Datenbasis auf dem Nostr-Protokoll mit AMB-Metadaten. Dazu Qualitätskriterien für religionspädagogische OER, WordPress-Plugins, mit denen Communities Materialien und Termine auf ihre eigene Seite holen, und der reli_hub als Prototyp, der im Februar 2027 startet.

**Das hat uns überrascht.**
Offene Praktiken gibt es in den Communities längst, nur heißen sie dort nicht so. Und die größte Hürde ist nicht die Technik, sondern die Angst vor Rechtsfragen.

**Darüber wollen wir gleich in unserer Breakout-Session sprechen.**
Wie bleibt eine Community-Infrastruktur nach Projektende lebendig? Wir zeigen, warum wir auf ein Protokoll statt auf eine Plattform setzen, und klicken gerne gemeinsam durch den Hub-Prototypen.

---

## Bereich 2: Kachel

### Projektstand – Wo stehen wir gerade? (lila Notizen)

- **Gemeinsame Datenbasis steht:** Materialien, Beiträge und Termine der Communities liegen als offene Nostr-Events auf den edufeed-Relays, beschrieben nach dem AMB-Metadatenstandard mit religionsbezogenen Vokabularen.
- **Qualitätskriterien veröffentlicht:** Handreichung mit vier Dimensionen (rechtlich, technisch, pädagogisch-didaktisch, religionspädagogisch), als Dialoginstrument, nicht als Prüfkatalog. → https://oer.community/qualitaet (CC BY 4.0)
- **Begleitforschung:** Literaturreview zu OER/OEP (19 Reviews, 2019–2025) und Interviewstudie mit Community-Verantwortlichen.
- **Werkzeuge für Communities:** vier WordPress-Plugins (Materialien, Artikel, Termine anzeigen; Beiträge veröffentlichen), im Einsatz bei ALPIKA-Arbeitsgruppen; ein Eingabeformular folgt im November.
- **reli_hub als Prototyp:** https://hub.rpi-virtuell.net – Communities, Materialpool, Termine, Spielregeln an einem Ort, live aus den Relays. Launch auf der Abschlusstagung.
- **Sichtbarkeit:** über 90 Beiträge auf oer.community seit 2024, Zwischenfazit-Tagung Februar 2026 in Nürnberg (Videoreihe „Mit OER zu einer Kultur des Teilens“ auf FAU.tv), HackathOERn 2026, OERcamp.

### Transferpotenzial – Was könnte für andere nützlich sein? (grüne Notizen)

- **Protokoll statt Plattform:** Nostr trennt Daten, Identitäten und Dienste. Jede Community behält ihren Schlüssel und ihre Seite und ist trotzdem im Verbund sichtbar. Das Muster lässt sich auf jede Fachcommunity übertragen.
- **Qualitätskriterien:** Die Handreichung ist fachspezifisch, ihr Aufbau (vier Dimensionen, Checklisten, Aushandlung statt Prüfung) ist auf andere Fächer übertragbar.
- **WordPress-Plugins:** frei nutzbar für alle Communities mit WordPress-Seite (Open Source). → git.edufeed.org/edufeed/wp-plugins-nostr
- **Metadaten:** AMB-konforme Erfassung mit eigenen Vokabularen; anschlussfähig an WLO, OERSI und andere Kataloge.
- **„Working out loud“:** Redaktionsabläufe, Entscheidungen und Issues liegen offen. Andere Projekte können Abläufe und Vorlagen direkt übernehmen.
- **Anknüpfungspunkte:** Projekte, die eigene Materialsammlungen pflegen und sie ohne neue Plattform in einen Verbund bringen wollen; Projekte zu Qualitätssicherung und KI-generierten Materialien.

### Herausforderungen & Learnings (rote Notizen)

- **Rechtsunsicherheit ist die größte Hürde:** In der Interviewstudie war die Angst vor Lizenzfehlern und Abmahnungen der meistgenannte Punkt. Lizenzkurse allein helfen wenig; besser funktioniert der Einstieg über ein inhaltliches Thema.
- **OEP gibt es schon, nur ohne Namen:** Communities teilen und arbeiten offen zusammen, ohne den Begriff zu kennen. Wir holen sie dort ab, statt Begriffe zu schulen.
- **Ehrenamt und Institution arbeiten verschieden:** Ehrenamtlich getragene Communities brauchen andere Angebote als Communities mit angestellten Mitarbeitenden.
- **Verteilte Systeme kosten Kraft:** Copy-and-paste zwischen Plattformen, viele Logins, Metasysteme sind Pflaster. Gemeinsame Standards sind mühsam, aber die eigentliche Lösung.
- **Hub und Infrastruktur auseinanderhalten:** Wir mussten lernen, den eigenen Community-Hub klar von der darunterliegenden technischen Infrastruktur (edufeed) zu unterscheiden, auch in der Kommunikation.
- **Nächster Schritt bis ins dritte Projektjahr:** Hub bis Ende 2026 fertigstellen, Kataloge der Communities mit echten Inhalten füllen, Launch auf der Abschlusstagung „Offen. Vernetzt. Zukunft.“ am 2./3. Februar 2027 in Frankfurt.

### Blick nach vorn (gelbe Notizen)

- **Was gut war:** offene Arbeitsweise, Verbund aus Praxis (Comenius-Institut) und Forschung (Frankfurt, Erlangen-Nürnberg), Austausch mit anderen OE_COM-Projekten (digiLL, HackathOERn).
- **Was wir anders machen würden:** früher mit den Communities an konkreten Problemen ansetzen („Welches Problem lösen wir mit OER?“), weniger mit Begriffen und Plattformen.
- **Was fehlt:** Förderung für den Betrieb danach. Kuratieren, Moderieren und Pflege der Infrastruktur enden heute mit der Projektlaufzeit.
- **Wunsch an künftiges Community-Building:** Infrastruktur als offene, gemeinsame Grundlage fördern (Protokolle, Standards, Relays), nicht jedes Projekt mit eigener Plattform; Anerkennung für Teilen und Kuratieren (z. B. Badges, Sichtbarkeit in Lehrkräftebildung).
- **Einladung:** Andere OE_COM-Projekte können ihre Materialien und Termine schon heute auf die gemeinsame Datenbasis bringen.

### Bilder und Links für die Kachel (Vorschläge)

- Screenshot der Hub-Startseite (https://hub.rpi-virtuell.net)
- Grafik „Community of Communities“ oder Ökosystem-Karte
- Tagungsbild Zwischenfazit Nürnberg bzw. Ankündigung Abschlusstagung (https://oer.community/foerbico-tagung-2027)
- Link Qualitätskriterien: https://oer.community/qualitaet

---

## Breakout Block D (20 Minuten) – Ablaufvorschlag

| Minuten | Was | Wer |
|---|---|---|
| 0–3 | Kurz ankommen: Wer ist da, aus welchem Projekt? | Moderation TP 1 |
| 3–10 | Live durch den Hub klicken: Communities, Materialpool mit Lizenzpille, Termine, Spielregeln | TP 1 |
| 10–13 | Ein Satz je Teilprojekt: Qualitätskriterien (TP 2), Begleitforschung (TP 3) | TP 2, TP 3 |
| 13–20 | Austausch: „Wie bleibt eure Community-Infrastruktur nach Projektende lebendig?“ Notizen direkt auf die Kachel | alle |

Rückfall, falls Relays oder Webex hängen: Screenshots auf der Kachel.

---

## Offen zu klären

- Wer pitcht (eine Minute im Plenum) und wer moderiert den Breakout-Raum?
- Sind die Links auf hub.rpi-virtuell.net zum 27.11. vorzeigbar? (UX-Termin am 25.11. liegt zwei Tage davor.)
