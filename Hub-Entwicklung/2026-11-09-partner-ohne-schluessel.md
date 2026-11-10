# Partner ohne Schlüssel: Entscheidungsvorlage

Stand: 10.11.2026. Bezug: Gesamtkonzeption Abschnitt 4.7 (weitere Communities eingebunden), `Hub-Entwicklung/communities-schluessel.md` Fragen 5 und 6, Issue „Ökosystem-Karte“ (07, `e6875f0b`) und Issue „Eigene Instanz“ (11, `93b36056`) auf gitworkshop. Enthalten sind nur öffentliche Schlüssel; private Schlüssel, Bunker-Links und Zugangsdaten gehören nicht in diese Datei.

Entscheidung: Jörg Lohrer. Das Ergebnis fließt als Liste in `PARTNERS` (Partnerkacheln im Prototyp, `PARTNER_MIT_SCHLUESSEL`) beziehungsweise in neue Community-Schlüssel, die dann in `CY_HEX` und gegebenenfalls `CO_SCHLUESSEL` eingetragen werden.

## 1. Ausgangslage in drei Sätzen

Die Communities-Liste im Prototyp (`CY`, Stand 26.10.2026) enthält zehn Einträge, für die auf den Relays kein Community-Schlüssel (`kind:10222`) gefunden wurde. Dazu kommen zwei Partner aus Abschnitt 4.7, die im Prototyp noch gar nicht vorkommen. Seit die Communities-Liste live vom Relay kommt, erscheinen Einträge ohne Schlüssel hinter den Live-Communities als Partnerkacheln ohne Knöpfe (Stand-Zeile „… Partner ohne Schlüssel“); einen Link auf die Seite des Partners tragen sie noch nicht.

## 2. Die zwei Optionen

- **A · Schlüssel anlegen.** Die Community bekommt einen eigenen Schlüssel mit Profil (`kind:0`) und Community-Definition (`kind:10222`). Sie erscheint live, kann Inhalte per `h`-Tag sammeln, Mitglieder haben, im Beziehungsgefüge Kanten bilden und über den Zuschnitt `?c=<npub>` eine eigene Instanz bekommen. Zu klären ist, wer den Schlüssel hält: die Community selbst (Ansprechperson der Community) oder treuhänderisch das Projektteam bis zur Übergabe. Voraussetzung ist eine Kooperationsvereinbarung (Seite `kooperationsvereinbarung`).
- **B · Partnerkachel mit Link.** Kein Schlüssel; die Community steht als Kachel mit Kurztext und Link auf ihre eigene Seite. Sie ist sichtbar, aber nicht Teil des Gefüges: keine Mitglieder, kein Katalog, kein Zuschnitt. Später lässt sich jederzeit auf A wechseln.

## 3. Tabelle

| Eintrag | Herkunft | Heute im Prototyp | Option A: Schlüssel, gehalten von | Option B: Kachel, Link | Empfehlung |
|---|---|---|---|---|---|
| relimentar | `CY`, `PARTNERS`, Abschnitt 4.7 | Kachel ohne Link; Reihen „Bilderbuchstunde“ und „Café relimentar“ laufen im relilab | eigene Instanz für Elementarpädagogik; Schlüssel bei der Ansprechperson von relimentar oder treuhänderisch beim Projektteam | [Link von der Redaktion zu ergänzen] | **A**, weil relimentar in der Leiste als eigene Instanz genannt wurde und Material und Fortbildungen hat; bis zur Vereinbarung B |
| narrt | `CY`, `PARTNERS` | Kachel ohne Link | eigenes Netzwerk mit Austauschrunden, Tagungen und Materialkatalog; Schlüssel bei der Koordination des Netzwerks | [Link von der Redaktion zu ergänzen] | **A**, weil ein eigener Materialkatalog genau das ist, was eine Community im Datenraum sammelt; bis zur Vereinbarung B |
| Münchner Reli Room | `CY`, Reihe im relilab | Karte mit Newsletter und Reihen | Schlüssel bei der verantwortenden Fachstelle | Kachel mit Link auf die Seite der Reihe [von der Redaktion zu ergänzen] | **B** als Reihe im relilab; Termine kommen über den `h`-Tag relilab |
| relilab NRW | `CY`, Reihe im relilab | Karte mit Reihe „reli.werkstatt“ | Schlüssel bei der verantwortenden Stelle in NRW | Kachel mit Link [von der Redaktion zu ergänzen] | **B** als Reihe im relilab |
| #relilab Impulse | `CY`, Reihe im relilab | Karte mit zwei Reihen | Schlüssel bei einem der beiden tragenden Institute | Kachel mit Link [von der Redaktion zu ergänzen] | **B** als Reihe im relilab |
| relilab\|BRU | `CY`, Reihe im relilab | Karte mit Reihe | Schlüssel bei den tragenden Instituten | Kachel mit Link [von der Redaktion zu ergänzen] | **B** als Reihe im relilab |
| relilab\|Junior | `CY`, Reihe im relilab | Karte mit Reihe | Schlüssel bei den tragenden Stellen | Kachel mit Link [von der Redaktion zu ergänzen] | **B** als Reihe im relilab |
| relilab\|interreligiös | `CY`, Reihe im relilab | Karte mit Reihe (geschützter Moodle-Raum) | Schlüssel bei den tragenden Stellen | Kachel mit Link [von der Redaktion zu ergänzen] | **B** als Reihe im relilab; ein geschützter Raum passt nicht zu einer öffentlichen Community |
| Makerspace asynchrone Lernressourcen | `CY`, Reihe im relilab | Karte mit Reihe | Schlüssel bei der Moderation des Makerspace | Kachel mit Link [von der Redaktion zu ergänzen] | **B** als Reihe im relilab |
| relilab.Schulseelsorge | `CY`, Reihe im relilab | Karte mit Reihe | Schlüssel bei der Moderation der Reihe | Kachel mit Link [von der Redaktion zu ergänzen] | **B** als Reihe im relilab; **A** prüfen, falls die Reihe ein eigenes Material- und Austauschangebot aufbaut |
| rpp-katholisch | Abschnitt 4.7 | fehlt | Schlüssel bei der Redaktion von rpp-katholisch | [Link von der Redaktion zu ergänzen] | **B** jetzt, **A** im Gespräch anbieten; wichtig für die konfessionelle Breite |
| Konfessionskundliches Institut | Abschnitt 4.7 | fehlt | Schlüssel beim Institut | [Link von der Redaktion zu ergänzen] | **B** jetzt, **A** im Gespräch anbieten |

Nicht in der Tabelle, weil schon mit Schlüssel: CampusCom (`npub1deah5w4wj5ke43580cp4n33zx8433gevey5xv8lfxxzf8qwyl3ss06nnst`), reliGlobal, Konfiarbeit EKD, Friedenspädagogik (vermutlich die in 4.7 genannte Fachstelle Friedensbildung; zu bestätigen), KuRU und Schuldek.de, KPH Wien/NÖ, RPI EKKW/EKHN, AG Didaktische Metadaten. Bei KuRU, RPI EKKW/EKHN und KPH Wien ist offen, wer den Schlüssel hält (Frage 1 in `communities-schluessel.md`).

Ebenfalls zu entscheiden: **InkRV** steht in `PARTNERS` als Partner „in Überarbeitung“ ohne Schlüssel. Empfehlung: **B** beibehalten, bis die Plattform wieder erreichbar ist.

## 4. Die relilab-Reihen

Acht der zehn Einträge sind Reihen im relilab. Ihre Termine kommen schon heute über den relilab-Schlüssel und den `h`-Tag relilab in den Kalender, und die relilab-Ansicht zeigt sie als Teil der Labor-Trias. Eigene Schlüssel würden das Gefüge zersplittern, ohne dass die Reihen etwas gewinnen, solange sie kein eigenes Material und keine eigene Mitgliedschaft pflegen. Empfehlung: Sie bleiben als Reihen im relilab sichtbar und werden in der Communities-Liste als Kacheln mit Verweis auf das relilab geführt. Ein Wechsel auf A ist möglich, wenn eine Reihe es selbst will und die Haltung des Schlüssels geklärt ist.

## 5. FOERBICO als Community (Frage 6)

Der Schaufenster-Schlüssel (`npub1tgftg8kptdrxxg0g3sm3hckuglv3j0uu3way4vylc5qyt0f44m0s3gun6e`) hat kein `kind:10222`. Optionen: **A** eine Community-Definition veröffentlichen, damit Beiträge und Kommentare ihm per `h`-Tag zugeordnet werden und die OER-Community live in der Liste erscheint; **B** bei der reinen Kuratierungsliste vom Profil-Schlüssel bleiben, wie Abschnitt 5a der Gesamtkonzeption es vorsieht. Empfehlung: **A**, weil die OER-Community als „Community of Communities“ sonst die einzige Community ohne Kanten im Gefüge bleibt; der Katalog als Liste bleibt davon unberührt.

## 6. Was nach der Entscheidung passiert

1. Für jede B-Entscheidung: Name, Kurztext und Link in `PARTNERS` beziehungsweise an der Partnerkachel in `CY`; Einträge ohne Link bleiben Kacheln ohne Ziel.
2. Für jede A-Entscheidung: Kooperationsvereinbarung, Schlüssel anlegen (nicht in diesem Repository), Profil und `kind:10222` veröffentlichen, den npub in `CY_HEX` eintragen; mit Katalog zusätzlich in `CO_SCHLUESSEL`.
3. Die Schlüsselliste `communities-schluessel.md` wird um die neuen npubs ergänzt.

[von Jörg Lohrer zu entscheiden: Liste der Einträge mit A, Liste mit B, Haltung der Schlüssel]
