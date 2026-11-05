# Stand der Navigation im reli_hub: Nachricht an den UX-Gast und Abnahme-Checkliste

Stand: Entwurf vom 16.11.2026, nichts davon ist gesendet oder veröffentlicht.

## 1. Nachricht (Entwurf, Jörg sendet)

Betreff: reli_hub: die Rückmeldungen vom 03.11. sind eingearbeitet, magst du noch einmal durchspielen?

Hallo,

die aktuelle Fassung liegt unter https://hub.rpi-virtuell.net. Was sich seit unserem Gespräch am 03.11. geändert hat, je Punkt ein Satz:

- Kreis-Klick: Ein Kreis erklärt seinen Bereich sofort beim Überfahren oder Antippen, der zweite Klick auf den Menüpunkt entfällt.
- Beschriftungen: Auch das Wort neben dem Symbol ist klickbar, und die Knospen haben auf dem Handy größere Trefferflächen.
- Direkt zur Aktion: Wer die Konsole kennt, wählt „Verstanden, direkt loslegen“ und kommt mit dem Menüeintrag sofort zur Aktion; unter „Hilfe“ gibt es die Erklärung wieder.
- Begriffe und Farben: Startseite, Konsole und Leiste benutzen dieselben Begriffe, die Knospen tragen die Farbe ihres Bereichs, „Lerninhalte“ führen in den Materialpool.
- Konsole auf der Startseite: Sobald die große Blume aus dem Bild scrollt, folgt ihr die kleine Konsole unten rechts.
- Leiste als Widget: Unten links stehen die „Orte“ (Leiste), unten rechts die „Tätigkeiten“ (Konsole), als zwei getrennte Elemente.
- Leiste konfigurierbar: Über den Knopf ⋯ lassen sich Einträge der Leiste aus- und einblenden.
- Mobil: Die Erklärkarte öffnet sich auf dem Handy als Sheet über der Seite statt als Sprung nach unten, und das Antippen verzeiht kleine Abweichungen.

Dazu zwei Neuerungen: rpi-virtuell ist als eigene Instanz in der Leiste dabei (mit Fortbildungen und News, live von den Relays), und die Startseite trägt einen kurzen Text zum Selbstverständnis (Institute dahinter, Mitmachen als Einladung, Offenheit als Struktur).

Aufgaben zum Durchspielen, am liebsten einmal am Rechner und einmal auf dem Handy:
1. Eine Person finden.
2. Einer Community beitreten.
3. Ein Material veröffentlichen.
4. Eine Sammlung zusammenstellen und einbetten.
5. Den Katalog einer Community finden.
6. Eine Fortbildung nach Merkmal filtern.

Mich interessiert vor allem, wo du zögerst, danebenklickst oder suchst. Rückmeldung bitte bis zum 25.11.2026, dann besprechen wir sie bei unserem Termin.

Danke und Gruß
Jörg

## 2. Abnahme-Checkliste 25.11.2026

Die Aufgaben jeweils auf dem Desktop und bei 375 px Breite spielen und eintragen. Vergleichswert vom 03.11.: Kreis plus Menüpunkt, also 2 Klicks je Bereich. Der Stand nach der Umsetzung (Simulation): Tutorialmodus 3, Direktmodus 2 Klicks je Bereich.

| Aufgabe | Gerät | Tipps/Klicks vorher (03.11.) | Tipps/Klicks nachher (erwartet) | Tipps/Klicks nachher (gezählt) | Fehlgriffe | Befund |
|---|---|---|---|---|---|---|
| Person finden | Desktop | 2 je Bereich | Tutorial 3, Direkt 2 | | | |
| Person finden | 375 px | 2 je Bereich | Tutorial 3, Direkt 2 | | | |
| Community beitreten | Desktop | 2 je Bereich | Tutorial 3, Direkt 2 | | | |
| Community beitreten | 375 px | 2 je Bereich | Tutorial 3, Direkt 2 | | | |
| Material veröffentlichen | Desktop | 2 je Bereich | Tutorial 3, Direkt 2 | | | |
| Material veröffentlichen | 375 px | 2 je Bereich | Tutorial 3, Direkt 2 | | | |
| Sammlung zusammenstellen und einbetten | Desktop | – | | | | |
| Sammlung zusammenstellen und einbetten | 375 px | – | | | | |
| Katalog einer Community finden | Desktop | – | | | | |
| Katalog einer Community finden | 375 px | – | | | | |
| Fortbildung nach Merkmal filtern | Desktop | – | | | | |
| Fortbildung nach Merkmal filtern | 375 px | – | | | | |

Hinweis: Bei der Umsetzung ließ sich die Aufgabe „Person finden“ nicht bis zum Ziel durchspielen, weil der Personen-Knopf noch ein Platzhalter ist; das gehört in den Befund, nicht in die Fehlgriffe.

Weitere Prüfungen:

- [ ] Sheet mobil: Die Erklärkarte öffnet sich als Sheet ohne Seitensprung, schließt mit ✕, mit Tipp daneben, mit Zurück und bei jedem Routenwechsel.
- [ ] Leiste „Orte“ gegen Konsole „Tätigkeiten“: Wird der Unterschied ohne Erklärung verstanden? Wirkt es noch wie eine doppelte Navigation?
- [ ] rpi-virtuell live-Stand: Die Ansicht zeigt „live“ mit Anzahl der Termine und News, Fortbildungen und News erscheinen, ohne Netz erscheint „Relay nicht erreichbar“ mit Verweis auf rpi-virtuell.de.
- [ ] Hilfe und Direktmodus-Umschalter: „Verstanden, direkt loslegen“ schaltet um, „Hilfe“ und „Konsole wieder erklären lassen“ schalten zurück, die Wahl bleibt nach dem Neuladen.
- [ ] Knospenfarben der Konsole entsprechen den Bereichsfarben der Startseite (im Browser noch nicht gegengeprüft).
- [ ] Kleine Konsole auf der Startseite erscheint erst, wenn die große aus dem Bild ist, und es gibt nie zwei sichtbare.
- [ ] Leiste anpassen (⋯): Ausblenden wirkt sofort und nach Neuladen; „Start“ lässt sich nicht ausblenden.
- [ ] Narrativ auf der Startseite: Wortlaut verständlich, Umbruch bei 375 px unauffällig.
- [ ] Vor jedem Durchlauf localStorage und sessionStorage leeren (Entwicklerwerkzeuge › Anwendung › Speicher löschen), damit Modus, Leiste und Zwischenspeicher frisch starten.
- [ ] Hover-Prüfung am Desktop: Nach einem Klick auf einen Kreis der großen Konsole bleibt die Erklärkarte stehen, wenn die Maus über einen anderen Kreis zur Karte fährt; nach Verlassen der Konsole reagiert das Überfahren wieder.
- [ ] Eine Ansicht offline laden (z. B. relilab-Termine mit abgeschaltetem Netz): Die Stand-Zeile zeigt weiter „Stand vom …“ und springt nicht auf „live“.
- [ ] Ein Material finden und seine Lizenz deuten: Im Materialpool eines öffnen; die Pille, der Satz dazu und die ausgegrauten Aktionen sagen, was man damit darf, ohne dass man nachfragen muss.
- [ ] Die Spielregeln finden: Im Menü des Schaufensters zu „Spielregeln“, vier Kacheln, je „in Vorbereitung“ oder „Lesen“; verständlich, was schon da ist und was noch kommt.
- [ ] Einen Beitrag im Schaufenster öffnen und eine Seite lesen (`#oercommunity/qualitaet`): Der Weg dorthin ist ohne Hilfe zu finden, der Text ist lesbar, der Rückweg ist klar.

Ergebnis kommt nach `Hub-Entwicklung/2026-11-25-abnahme-navigation.md` (Befunde ohne Personennamen). Einwände werden Issue-Kommentar oder neues Issue, nicht Nacharbeit ohne Faden.

## 3. Offen nach dieser Runde

Fragen, die für die Bedienung zählen und am 25.11. mit dem UX-Gast zu klären sind:

- Verben der Modi: Passt „Verstanden, direkt loslegen“ und „Konsole wieder erklären lassen“, oder gibt es klarere Worte für Tutorial und Direktmodus?
- Name der Startseite: Der Eintrag „Hilfe“ in der Kopfzeile führt auf die Startseite mit Erklärkarte; stimmt der Name, oder soll es „Erklärung“ oder etwas anderes heißen?
- Direktmodus „hub.home“ („Ökosystem“): Der Eintrag lädt im Direktmodus nur die Startseite neu, statt zu einer Übersicht zu führen. Soll er anderswohin?
- Kartentext zur Hilfe: Der Satz verspricht ein Umschalten, das erst der Knopf tut.
- Knospen-Trefferfläche mobil: Bei 375 px ist sie klein (etwa 18 mal 13 Pixel im Layout, Toleranz etwa 6 Pixel über den Rand); größere Kreise würden sich überlappen. Reicht das mit echtem Finger, oder muss die kleine Konsole mobil größer werden?
- Profil-Eintritt überschreibt die Tutorial-Wahl: Wer sich mit einem Profil anmeldet, landet im Direktmodus, auch wenn er das Tutorial bewusst gewählt hatte.
- Leiste: Sollen auch gefolgte Communities erscheinen oder nur Mitgliedschaften? Und: Kollidiert die Leiste auf dem Handy mit Hinweisen?
- Narrativ: Wortlaut des Startseitentextes („geschütztes Material darf dazu, bleibt aber beim Ansehen“) ist knapp; gegenlesen.
- Auf einem echten Touch-Gerät: Nach dem Antippen eines Kreises und dem Auslösen über die Karte wechselt der nächste Vorschau-Tipp auf einen anderen Kreis die Karte sofort (Sperre nach dem Klick darf nicht hängen bleiben).
