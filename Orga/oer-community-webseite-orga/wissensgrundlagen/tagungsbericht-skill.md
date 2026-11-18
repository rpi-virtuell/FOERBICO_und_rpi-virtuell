---
name: "tagungsbericht-oer-community"
description: "Blogbeitrag für oer.community aus Transkript, Notizen, Pad oder Folien einer Tagungssession schreiben oder überarbeiten: Bericht in Markdown mit geprüften Links, anonymisierten Teilnehmenden, FOERBICO/edufeed-Perspektive und Freigabe-Mail."
---

# Tagungsbericht für oer.community

Aus dem Material zu einer Tagungssession (Vortrag, Workshop, Panel) entsteht ein Blogbeitrag in Markdown für oer.community. Der Beitrag erscheint aus der Perspektive des Comenius-Instituts und des Projekts FOERBICO. Geliefert wird eine `.md`-Datei, dazu ein kurzer Begleittext mit offenen Punkten und auf Wunsch eine Freigabe-Mail an die Referent:in.

## 1. Material sichten, bevor geschrieben wird

Reihenfolge der Verlässlichkeit: Pad und Folien, dann Ankündigungstext der Session, dann Transkript.

- Zuerst die Ankündigungsseite der Session und die Programmseite der Tagung abrufen. Dort stehen Titel, Zeitfenster, Leitfragen und oft der Link zum Pad.
- Fehlen Pad oder Folien, einmal danach fragen. Thesen, Leitfragen und Zahlen werden wörtlich nur aus schriftlichen Quellen übernommen. Thesen nie aus einem Transkript rekonstruieren, wenn es eine schriftliche Fassung geben könnte.
- Transkripte sind oft stark verhört. Fachbegriffe, Namen und Projekte aus dem Kontext rekonstruieren (Beispiele: "Scorn" ist SCORM, "ANB" ist AMB, "Örsi" ist OERSI). Was sich nicht sicher klären lässt, weglassen oder allgemein umschreiben.
- Fakten aus dem Transkript (Laufzeiten, Summen, Prozentzahlen, Namen von Diensten) gegen eine Quelle prüfen. Bei Widerspruch gilt die Quelle. Nicht belegbare Zahlen weglassen oder als Aussage der Referent:in kennzeichnen und eine belegte Zahl danebenstellen.

## 2. Aufbau des Beitrags

1. YAML-Frontmatter nach den bestehenden FOERBICO-Vorgaben, siehe Abschnitt 3.
2. Kursive Zeile: Format, Referent:in mit Einrichtung, Tagung, Datum, Ort. Der Titel steht im Frontmatter.
3. Einstieg mit Tagungskontext, Zeitfenster und vollem Sessiontitel, jeweils verlinkt.
4. Thematische Abschnitte mit sprechenden Zwischenüberschriften. Keine Nacherzählung des Ablaufs.
5. Schlussabschnitt "Was das für OER-Communities heißt" (Wortlaut anpassbar). Er ist Pflicht und resümiert den Community-Aspekt, siehe Abschnitt 5.

Keine Längenvorgabe. Der Stoff bestimmt die Länge.

## 3. YAML-Frontmatter: FOERBICO-Vorgaben anwenden, nicht neu erstellen

Für Frontmatter und Schlagworte gibt es im Projekt FOERBICO bereits klare, ausgearbeitete Vorgaben. Dieser Skill wendet sie an. Er formuliert sie nicht neu, baut sie nicht nach und ergänzt sie nicht.

- Quelle der Vorgaben: das FOERBICO-Repository, Ordner `Orga/oer-community-webseite-orga/`. Öffentlicher GitHub-Mirror: `rpi-virtuell/FOERBICO_und_rpi-virtuell` (das Forgejo-Original auf git.rpi-virtuell.de lässt sich meist nicht automatisch abrufen). Vor dem Schreiben des Frontmatters den Mirror klonen und den aktuellen Stand dieser Dateien lesen:
  - `YAML-FRONTMATTER-ASSISTENT-PROMPT.md`: Aufbau in den Blöcken `# commonMetadata` und `# staticSiteGenerator`, Beispiel, Ableitungsregeln, Slug-Regeln, Vorgehen ERSTELLEN und PRÜFEN.
  - `wissensgrundlagen/felder.yaml`: Schema, Pflichtfelder, erlaubte Werte, Standardwerte, dritter Block `bilder`.
  - `wissensgrundlagen/schlagworte.yaml` und `wissensgrundlagen/schlagwort-glossar.md`: kanonische Schlagworte, Zusammenführungen, gestrichene Begriffe.
  - `wissensgrundlagen/personen.yaml`: `creator`-Angaben mit ORCID und ROR.
  - `wissensgrundlagen/bildattribution.md`: Bildnachweise.
- Die Dateien werden bei jedem Beitrag neu gelesen und ihr Inhalt nicht in diesen Skill kopiert, weil sie im Projekt weiterentwickelt werden.
- Nach dem Erstellen die Konsistenzregeln aus dem Modus PRÜFEN durchgehen: `name` gleich `title`, `description` gleich `summary`, `keywords` gleich `tags` (gleiche Werte, gleiche Reihenfolge), `id` und `image` aus `url` abgeleitet, jedes Schlagwort in `schlagworte.yaml` enthalten.
- Widersprechen sich die Dateien untereinander, nichts selbst entscheiden: den Widerspruch im Begleittext nennen.
- Das gilt für alle Felder und ausdrücklich für die Schlagwortauswahl. `keywords` und `tags` enthalten nur Schreibweisen aus `schlagworte.yaml`. Passt kein Schlagwort, wird keines erfunden. Vorschläge für neue Schlagworte gehören in den Begleittext.
- Sind die Vorgaben in der Sitzung nicht verfügbar: den Beitrag ohne Frontmatter liefern und das im Begleittext sagen. Kein Schema, keine Feldwerte und keine Schlagworte aus einem einzelnen Beispielbeitrag oder aus dem Gedächtnis ableiten.
- Lizenz und Autorenangabe stehen im Frontmatter, nicht im Fließtext.

## 4. Schutz der Beteiligten

Diese Regeln gelten ab dem ersten Entwurf, nicht erst auf Nachfrage.

- Namentlich genannt werden nur Referent:innen und Moderation laut Programm.
- Teilnehmende vollständig anonymisieren: kein Name, keine Einrichtung, kein Geschlecht, keine Projekte oder Dienste, die auf eine Person schließen lassen. Formulierungen wie "aus der Runde", "in der Diskussion", "ein Hinweis aus dem Kreis der Teilnehmenden".
- Nicht aufnehmen, was erkennbar intern gemeint war: Finanzierungssorgen einzelner Einrichtungen, Aussagen über Ministerien, Spitzen gegen benennbare Dritte, Anekdoten über namentlich genannte Hochschulen oder Firmen, alles mit Zusätzen wie "das geht nicht nach außen".
- Kein Hinweis darauf, dass mitgeschnitten wurde. Keine Bemerkungen zur Tonqualität, kein "sinngemäß", kein "laut Aufzeichnung". In Mails und Begleittexten nach außen heißt die Grundlage "meine Notizen".
- Rekonstruktionen und Unsicherheiten gehören in den Begleittext an den Nutzer, nicht in den Beitrag.

## 5. Perspektive: Comenius-Institut, FOERBICO, edufeed

Der Bericht selbst bleibt fair und gibt die Positionen der Sprechenden unverfälscht wieder. Die eigene Perspektive steht erkennbar getrennt davon, vor allem im Schlussabschnitt, bei Bedarf mit ein oder zwei einordnenden Sätzen im Text.

Leitgedanken für die Einordnung:

- FOERBICO fördert offene Bildungspraktiken in religionsbezogenen Communities. Maßstab ist deshalb immer: Was bedeutet das Gehörte für Communities, die gemeinsam Material entwickeln, teilen und pflegen?
- Infrastruktur dient Communities, nicht umgekehrt. Standards entstehen aus Sprachgebrauch und Aushandlung in Communities und werden nicht von oben verordnet.
- edufeed-Logik: dezentrale Veröffentlichung über Nostr, offene Protokolle statt Plattformbindung, Metadaten nach AMB als signierte Events, mehrere Beschreibungen derselben Ressource durch verschiedene Fachgruppen sind ausdrücklich möglich, Inhalte fließen zwischen Diensten statt in Silos zu liegen.
- Wo eine Session Probleme benennt (Finanzierung, Standardisierung, Werkzeuge, Auffindbarkeit), im Schluss fragen: Wer trägt das als Community, wer wird beteiligt, wie sähe eine dezentrale oder community-getragene Antwort aus?
- Keine Werbung. Der Bezug zu edufeed oder Nostr wird nur hergestellt, wo er sachlich passt, und knapp gehalten.

Der Schlussabschnitt beantwortet jeweils: Was nehmen OER-Communities aus dieser Session mit, und wo liegt die Verbindung zu community-getragener, offener Infrastruktur?

## 6. Ton

- Sachlich berichten, Positionen zuordnen ("Rempis hält ...", "aus der Runde kam ...").
- Keine Zuspitzungen, die mehr behaupten, als gesagt wurde, und keine Sätze, die Lehrenden oder Einrichtungen Kompetenz absprechen.
- Mehrdeutige Formulierungen vermeiden.
- Wörtliche Zitate nur aus schriftlichen Quellen (Pad, Folien, Ankündigung).

## 7. Links

Hohe Linkdichte ist erwünscht, sie lädt zum Weiterforschen ein.

- Jede Einrichtung, jeden Standard, jedes Projekt, jede Software und jede Studie beim ersten Auftreten verlinken, bevorzugt die offizielle Quelle. Dazu Hintergrundartikel, wenn sie eine Aussage belegen oder vertiefen.
- Material der Session verlinken: Ankündigung, Pad, Folien, Folgeveranstaltungen.
- Jeden Link abrufen und auf Erreichbarkeit, Inhalt und Relevanz prüfen. Links nicht aus dem Gedächtnis setzen.
- Links, die Teilnehmende erkennbar machen würden, weglassen.
- Nicht prüfbare Links (Bot-Sperre, Serverfehler) im Begleittext einzeln benennen.

## 8. Bilder

- Kein Stock-Material (Canva, iStock und Ähnliches), es lässt sich nicht offen lizenzieren.
- Bilder der Referent:in nur mit CC-Lizenz. Darum wird in der Freigabe-Mail gebeten.
- KI-generierte Bilder stehen unter CC0, werden als KI-generiert gekennzeichnet, das Werkzeug wird im Nachweis genannt.
- Nachweise im Block `bilder` des Frontmatters nach `wissensgrundlagen/bildattribution.md`.

## 9. Begleittext zur Datei

Kurz und als Liste:

- Stellen, die rekonstruiert oder unsicher sind und gegengelesen werden sollten.
- Was bewusst weggelassen oder anonymisiert wurde.
- Nicht prüfbare Links.
- Offene Platzhalter im Text.
- Ob das Frontmatter nach den FOERBICO-Vorgaben erstellt wurde oder fehlt, weil die Vorgaben nicht vorlagen.

## 10. Freigabe-Mail an die Referent:in

Auf Wunsch im Stil des Nutzers:

- Du-Form, Anrede "Lieber/Liebe Vorname", Schluss "Vielen Dank und freundlicher Gruß" plus Vorname.
- Dank mit einem konkreten inhaltlichen Bezug zur Session.
- Hinweis, dass aus den eigenen Notizen ein Beitrag für oer.community entstanden ist, mit Link zum Entwurf im Pad.
- Bitte, auf richtige Wiedergabe der Positionen und der Sachangaben zu schauen und zu sagen, was nicht öffentlich stehen soll. Korrekturen per Mail oder als Kommentar im Pad.
- Bitte um zeitnahe Rückmeldung, solange die Tagung frisch ist.
- Bitte um ein Bild unter CC-Lizenz, zum Beispiel aus den Folien.
- Fehlt der Pad-Link, einen Platzhalter setzen und darauf hinweisen.

## 11. Überarbeitungen

- Änderungen gezielt in der bestehenden Datei vornehmen und die Datei erneut senden.
- Nach jeder Anonymisierung oder Streichung die betroffenen Absätze erneut lesen, damit keine Bezüge wie "er" oder "sein Rat" ins Leere laufen.
- Neue Quellen (Pad, Folien) haben Vorrang vor früheren Rekonstruktionen. Abweichungen offen benennen und korrigieren.