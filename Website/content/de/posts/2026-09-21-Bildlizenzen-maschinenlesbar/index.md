---
# commonMetadata
'@context': https://schema.org/
creativeWorkStatus: Draft
type: LearningResource
name: 'Ein Bild, das seine Lizenz kennt: Wie wir Bildnachweise in edufeed und FOERBICO maschinenlesbar machen'
description: >-
  Bildnachweise sind in der OER-Praxis Handarbeit und gehen bei jeder Weitergabe verloren. FOERBICO und edufeed hängen die Lizenz jetzt an das Bild selbst: als signierten Nachweis, der über den Fingerabdruck der Datei gefunden wird, wohin auch immer sie kopiert wird. Der Beitrag erklärt für die OER-Community, was das für Autor:innen bedeutet, und für Entwickler:innen, wie es technisch funktioniert.
license: https://creativecommons.org/licenses/by/4.0/deed.de
id: https://oer.community/bildlizenzen-maschinenlesbar
creator:
  - givenName: Jörg
    familyName: Lohrer
    type: Person
    affiliation:
      name: Comenius-Institut
      type: Organization
  - givenName: Gina
    familyName: Buchwald-Chassée
    type: Person
    affiliation:
      name: Comenius-Institut
      type: Organization
  - givenName: Ludger
    familyName: Sicking
    type: Person
    affiliation:
      name: Comenius-Institut   # TODO: Affiliation prüfen
      type: Organization
  - givenName: Steffen
    familyName: Rörtgen
    type: Person
    affiliation:
      name: edufeed   # TODO: Affiliation prüfen
      type: Organization
inLanguage:
  - de
about:
  - https://w3id.org/kim/hochschulfaechersystematik/n0
learningResourceType:
  - https://w3id.org/kim/hcrt/text
  - https://w3id.org/kim/hcrt/web_page
educationalLevel:
  - https://w3id.org/kim/educationalLevel/level_C
datePublished: '2026-09-21'
keywords:
  - OER
  - Bildlizenzen
  - Creative Commons
  - Metadaten
  - edufeed
  - Nostr
  - KI-Kennzeichnung
  - FOERBICO

# staticSiteGenerator
author:
  - Jörg Lohrer
  - Gina Buchwald-Chassée
  - Ludger Sicking
  - Steffen Rörtgen
title: 'Ein Bild, das seine Lizenz kennt'
cover:
  relative: true
  image: TODO-titelbild.jpg
  alt: 'TODO – Alt-Text des Titelbilds'
  hiddenInSingle: false
summary: >-
  Bildnachweise in OER sind Handarbeit und gehen bei jeder Weitergabe verloren. Wir hängen die Lizenz jetzt an das Bild selbst: als signierten Nachweis, der über den Fingerabdruck der Datei gefunden wird. Was das für Autor:innen bedeutet, wie es aussieht und wie es technisch funktioniert.
url: bildlizenzen-maschinenlesbar
tags:
  - OER
  - Bildlizenzen
  - Creative Commons
  - Metadaten
  - edufeed
  - Nostr
  - KI-Kennzeichnung
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
# TODO: Titelbild anlegen (Vorschlag: Screenshot der Lizenzpille am Titelbild von Olav Richters Beitrag,
#       oder eigenes Motiv mit ai: generated) und Eintrag ergänzen.
bilder: {}
---

Schau dir das Titelbild von [Olav Richters Beitrag zu KI im Religionsunterricht](https://oer.community/ki-im-evangelischen-religionsunterricht/) an. Unten rechts steht eine kleine Zeile: *KI-generiert · CC0 1.0 · Olav Richter mit ChatGPT, 13.09.2026*. Beides verlinkt. Niemand hat sie getippt. Sie entsteht aus Angaben, die einmal am Bild hinterlegt sind, und sie erscheint überall, wo dieses Bild gezeigt wird: auf oer.community, im edufeed-Client, auf jeder Seite, die das Bild aus dem offenen Datenraum lädt.

Das klingt nach einer Kleinigkeit. Es ist der Unterschied zwischen einem Bildnachweis, der *bei* einem Bild steht, und einem, der *zu* einem Bild gehört.

## Das Problem, das jede OER-Autorin kennt

Wer offene Bildungsmaterialien erstellt, kennt die Regel: Titel, Urheber:in, Lizenz, Link, Ursprungsort. Die OER-Community hat dafür seit Jahren eine Merkhilfe, die TULLU-Regel, und wer sie befolgt, macht es richtig. Das ist der Gold-Standard.

Nur: Der Nachweis ist Text. Er steht in einer Bildunterschrift, in einem Impressum, in einer Fußnote. Sobald das Bild kopiert wird, in eine Präsentation wandert, auf einer anderen Website erscheint, in einem Kalender-Eintrag auftaucht, ist der Nachweis weg. Nicht aus Böswilligkeit, sondern weil er nie am Bild hing, sondern daneben stand.

In der Praxis führt das zu drei Zuständen, die wir alle kennen:

- **Nachweis vorhanden, aber unbrauchbar.** „Quelle: eigene Darstellung mit KI und Canva." Wer darf das Bild weiterverwenden? Unter welchen Bedingungen? Die Angabe sagt es nicht, und Stock-Material aus Canva oder iStock darf ohnehin nicht offen weitergegeben werden, auch wenn es durch einen KI-Filter gelaufen ist.
- **Nachweis vorhanden, aber nicht weitergabefähig.** „Mit freundlicher Genehmigung." Das ist eine Erlaubnis für eine Person an einem Ort. Wer das Bild an einem zweiten Ort zeigt, hat sie nicht.
- **Kein Nachweis.** Das Bild ist da, sonst nichts. Der häufigste Fall.

Alle drei haben dieselbe Ursache. Es gibt keinen Ort, an dem der Nachweis *am Bild* gespeichert ist, so dass jede Software ihn findet, ohne eine Bildunterschrift zu lesen.

## Was wir anders machen

Wir hängen die Lizenz an das Bild selbst. Nicht an die Datei im Sinne einer eingebetteten Notiz, die beim nächsten Speichern verloren geht, sondern an ihren **Fingerabdruck**.

Jede Datei hat einen: eine lange Zeichenfolge, die sich aus ihrem Inhalt berechnet (technisch: der SHA-256-Hash). Ändert sich ein einziges Pixel, ändert sich der Fingerabdruck. Zwei identische Kopien haben denselben. Das ist der Trick: **Wer die Bytes hat, hat den Fingerabdruck. Wer den Fingerabdruck hat, findet den Nachweis.**

Der Nachweis selbst ist ein kleiner, digital signierter Zettel im offenen Datenraum von edufeed. Er sagt: *Zu dem Bild mit diesem Fingerabdruck gehört diese Lizenz, diese Urheberin, diese Quelle, dieser Alt-Text, und es wurde so und so mit KI erzeugt.* Signiert von der Person oder Institution, die das bestätigt.

Wo das Bild liegt, ist dabei zweitrangig. Es kann auf unserem Bildserver liegen, auf dem einer Landeskirche, auf einer WordPress-Seite. Eine Adresse benennt einen Ort. Ein Fingerabdruck benennt den Inhalt. Ein Bild, das umzieht, behält seine Lizenz.

## Warum wir das Platin nennen

Der Gold-Standard sagt: Die Angaben sind vollständig. Wir gehen drei Schritte weiter.

**Maschinenlesbar.** Der Nachweis ist kein Fließtext, sondern strukturiert: ein Feld für die Lizenz-URL, eines für die Urheberin, eines für die Quelle, eines für den Alt-Text, eines für die KI-Kennzeichnung. Jeder Client kann ihn auslesen und anzeigen, ohne zu raten, was in der Bildunterschrift gemeint war.

**Signiert.** Der Nachweis trägt eine kryptografische Unterschrift. Man sieht, wer die Angabe gemacht hat, und dass sie seitdem nicht verändert wurde. Wer ein Bild nachnutzt, kann sich darauf berufen.

**Weiterverwendbar in einem Klick.** Im edufeed-Client steht am Bild das Lizenz-Badge, bei KI-Bildern mit der KI-Marke nach den Icons des EU AI Office. Wer das Bild in ein eigenes Material übernimmt, kopiert den vollständigen Lizenztext mit einem Klick, korrekt formatiert, mit allen Links. Die TULLU-Regel wird nicht mehr von Hand angewendet, sie wird ausgeliefert.

Und der Nachweis reist mit. Ein Bild, das aus einem Blogbeitrag in einen Kalendertermin wandert, in eine Materialsammlung, in einen Flyer, der aus dem Datenraum erzeugt wird: überall dieselbe Lizenzzeile, aus derselben Quelle.

## Was das für Autor:innen bedeutet

Konkret: eine Handvoll Zeilen pro Bild. Wer für oer.community schreibt, trägt zu jedem Bild ein:

```yaml
bilder:
  klassengespraech.jpg:
    alt: Zwei Jugendliche und eine Lehrerin am Tisch, dazwischen ein Tablet mit Chatbot-Dialog
    title: Urteilsbildung im Gespräch
    author: Olav Richter mit ChatGPT, 13.09.2026
    authorUrl: https://www.rpi-baden.de
    licence: CC0 1.0
    licenceUrl: https://creativecommons.org/publicdomain/zero/1.0/
    ai: generated
```

Der Rest passiert automatisch: Das Bild wird auf den Bildserver geladen, der Nachweis erzeugt und signiert, die Lizenzzeile gerendert. Für eigene Fotos gilt die Hausregel (CC BY FOERBICO), für fremde Werke stehen Urheber:in, Quelle und deren Lizenz im Block.

Drei Regeln haben sich dabei als die wichtigsten herausgestellt:

1. **Ohne Lizenz kein Bild im Datenraum.** Fehlt die Lizenzangabe, zeigt der Client ein neutrales Ersatzmotiv. Das ist keine Strafe, sondern ein Anreiz: Wer sein Bild überall sehen will, klärt die Lizenz. Es funktioniert besser als jede Ermahnung.
2. **KI-Kennzeichnung ist eigenes Feld, keine Lizenz.** `ai: generated` für vollständig KI-erzeugte Bilder, `ai: modified` für menschliche Bilder, die mit KI bearbeitet wurden. Die Kennzeichnung ersetzt weder Lizenz noch Urheber:in. Wer prompted, ist genannt. Und: Kein `ai`-Feld heißt „nicht deklariert", nicht „ohne KI".
3. **Eine Erlaubnis ist keine Lizenz.** „Mit freundlicher Genehmigung" darf so im Nachweis stehen, aber dann als das, was es ist: Rechte vorbehalten, Nutzung an diesem Ort erlaubt. Der Client zeigt das Bild, aber niemand wird zur Weitergabe eingeladen. Ehrlich ist besser als eine erfundene CC-Lizenz.

## Für Entwickler:innen: wie es unter der Haube aussieht

Der Datenraum von edufeed basiert auf dem Nostr-Protokoll. Der Lizenznachweis ist ein Event vom Typ `kind 1063`, das die Spezifikation [NIP-94](https://github.com/nostr-protocol/nips/blob/master/94.md) für Datei-Metadaten definiert, erweitert um Lizenz-Felder. Das echte Event zum Titelbild aus dem ersten Absatz:

```json
{
  "kind": 1063,
  "tags": [
    ["url", "https://blossom.edufeed.org/bb3dfcb3…8867d7b.jpg"],
    ["x", "bb3dfcb3815161763ed2e6250c11446c95934f0f1bed60c5c6dca80148867d7b"],
    ["m", "image/jpeg"],
    ["size", "250142"],
    ["title", "Urteilsbildung im Gespräch: Chatbot, Bibel und Klassenraum"],
    ["license", "https://creativecommons.org/publicdomain/zero/1.0/"],
    ["credit", "Olav Richter mit ChatGPT (OpenAI), 13.09.2026"],
    ["alt", "Zwei Jugendliche und eine Lehrerin sitzen im Klassenraum um ein Tablet …"],
    ["source", "https://oer.community/ki-im-evangelischen-religionsunterricht"],
    ["ai", "generated"]
  ]
}
```

Das `x`-Tag ist der Fingerabdruck. Jeder Client, der ein Bild anzeigen will, fragt die Relays: *Gibt es ein `kind 1063` mit `#x` gleich diesem Hash?* Gibt es mehrere, gewinnt das neueste. Die Bilder selbst liegen auf einem [Blossom](https://github.com/hzrd149/blossom)-Server, der Dateien über ihren Hash adressiert, weshalb die URL den Fingerabdruck bereits enthält. Das Bild kann aber ebenso gut anderswo liegen; der Nachweis gilt für die Bytes, nicht für den Ort.

Der Inhalt, der das Bild nutzt, etwa ein Blogbeitrag (`kind 30023`) oder ein Kalendertermin (`kind 31923`), trägt denselben Hash in einem eigenen `x`-Tag. So löst der Client den Nachweis auf, ohne die Bild-URL zu kennen, und so bleibt die Verbindung erhalten, wenn das Bild gespiegelt wird.

Die vollständige Konvention steht im edufeed-Wiki unter *License events for uploaded files*; die Autor:innen-Seite in unserer [Bildattributions-Konvention](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/src/branch/main/Orga/oer-community-webseite-orga/wissensgrundlagen/bildattribution.md). Beides ist offen und darf nachgebaut werden.

## Was noch nicht fertig ist

Wir sind ehrlich: Das ist ein Anfang, kein Abschluss.

- **Prompt und Modell.** Für KI-Bilder speichern wir bereits, mit welchem Prompt und welchem Modell sie entstanden sind. Im Nachweis stehen sie noch nicht, weil die Konvention dafür in Arbeit ist. Der Vorschlag: zwei weitere Felder, `prompt` und `ai-model`, mit der Regel, dass der Prompt *diese eine* Generierung dokumentiert, nicht jede mögliche.
- **Bilder im Fließtext.** Die Lizenzzeile erscheint bisher am Titelbild. Für Bilder im Text ist der Weg derselbe, aber noch nicht gebaut.
- **Der Bestand.** Von rund 90 Beiträgen auf oer.community tragen 16 den Nachweis. Die übrigen werden nach und nach nachgezogen, jedes Bild einzeln, weil jede Lizenz geprüft werden muss. Das ist Handarbeit, und sie lohnt sich nur einmal.

Wer das für die eigene Plattform übernehmen will, ob mit WordPress, TYPO3, Hugo oder etwas anderem: Die Bausteine sind offen, die Relays sind offen, und wir helfen gern. Der Fingerabdruck eines Bildes ist überall derselbe. Das ist die ganze Idee.
