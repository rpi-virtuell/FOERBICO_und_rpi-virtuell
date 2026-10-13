---
# commonMetadata
'@context': https://schema.org/
creativeWorkStatus: Draft
type: LearningResource
name: 'Ein Bild, das seine Lizenz kennt: Lizenznachweise maschinenlesbar und signiert am Bild'
description: >-
  Ein Bildnachweis nach TULLU-Regel ist Text neben dem Bild. Sobald das Bild kopiert wird, ist er weg. FOERBICO und edufeed hängen den Nachweis deshalb an den Fingerabdruck der Datei: als signiertes Nostr-Event (kind 1063 nach NIP-94) mit Lizenz, Urheber:in, Quelle, Alt-Text, KI-Kennzeichnung und Schlagworten, das jeder Client über den SHA-256-Hash findet. Der Beitrag erklärt das Modell, die Konvention für Autor:innen, die Werkzeugkette und was noch offen ist.
license: https://creativecommons.org/licenses/by/4.0/deed.de
id: https://oer.community/bildlizenzen-maschinenlesbar
creator:
  - givenName: Jörg
    familyName: Lohrer
    type: Person
    affiliation:
      name: Comenius-Institut
      id: https://ror.org/025e8aw85
      type: Organization
  - givenName: Steffen
    familyName: Rörtgen
    type: Person
    affiliation:
      name: edufeed   # TODO: Affiliation prüfen
      type: Organization
  - givenName: Ludger
    familyName: Sicking
    type: Person
    affiliation:
      name: Comenius-Institut   # TODO: Affiliation prüfen
      id: https://ror.org/025e8aw85
      type: Organization
inLanguage:
  - de
about:
  - https://w3id.org/kim/hochschulfaechersystematik/n0
learningResourceType:
  - https://w3id.org/kim/hcrt/text
  - https://w3id.org/kim/hcrt/web_page
datePublished: '2026-09-21'   # TODO: beim Veröffentlichen auf das Erscheinungsdatum setzen
keywords:
  - OER
  - Bildlizenzen
  - Metadaten
  - Creative Commons
  - edufeed
  - Nostr
  - Blossom
  - NIP-94
  - KI-Kennzeichnung
  - FOERBICO

# staticSiteGenerator
author:
  - Jörg Lohrer
  - Steffen Rörtgen
  - Ludger Sicking
title: 'Ein Bild, das seine Lizenz kennt'
cover:
  relative: true
  image: TODO-titelbild.jpg
  alt: 'TODO – Alt-Text des Titelbilds'
  hiddenInSingle: false
summary: >-
  Der Bildnachweis steht neben dem Bild und geht beim Kopieren verloren. Wir hängen ihn an den Fingerabdruck der Datei: signiert, maschinenlesbar, mit KI-Kennzeichnung und Schlagworten. Wie das funktioniert, was Autor:innen dafür tun, und wie es unter der Haube aussieht.
url: bildlizenzen-maschinenlesbar
tags:
  - OER
  - Bildlizenzen
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

Dieser Beitrag richtet sich an alle, die wissen wollen, wie das geht: Entwickler:innen, Plattformbetreiber:innen, Metadaten-Menschen, und Autor:innen, die verstehen wollen, was hinter den paar Zeilen steckt, die sie pro Bild eintragen. Die Fragen *davor*, also welche Bilder man überhaupt verwenden darf, was Canva und KI-Bilder dürfen und was nach TULLU-Regel in einen Nachweis gehört, beantwortet Ginas FAQ [„OER und das vermeintliche Bildlizenz-Dilemma“](https://oer.community/bildlizenz-dilemma/). Hier geht es um die Frage danach: Wenn klar ist, *was* in den Nachweis gehört, *wo* bleibt er dann?

## Das Problem: Der Nachweis steht neben dem Bild

Die [TULLU-Regel](https://open-educational-resources.de/oer-tullu-regel/) ist der Gold-Standard, und wer sie befolgt, macht es richtig. Nur: Der Nachweis ist Text. Er steht in einer Bildunterschrift, in einem Impressum, in einer Fußnote. Sobald das Bild kopiert wird, in eine Präsentation wandert, auf einer anderen Website erscheint, in einem Kalender-Eintrag auftaucht, ist der Nachweis weg. Nicht aus Böswilligkeit, sondern weil er nie am Bild hing, sondern daneben stand.

In der Praxis führt das zu drei Zuständen, die wir alle kennen:

- **Nachweis vorhanden, aber unbrauchbar.** „Quelle: eigene Darstellung mit KI und Canva." Wer darf das Bild weiterverwenden? Unter welchen Bedingungen? Die Angabe sagt es nicht, und Stock-Material aus Canva oder iStock darf ohnehin nicht offen weitergegeben werden, auch wenn es durch einen KI-Filter gelaufen ist.
- **Nachweis vorhanden, aber nicht weitergabefähig.** „Mit freundlicher Genehmigung." Das ist eine Erlaubnis für eine Person an einem Ort. Wer das Bild an einem zweiten Ort zeigt, hat sie nicht.
- **Kein Nachweis.** Das Bild ist da, sonst nichts. Der häufigste Fall.

Alle drei haben dieselbe Ursache. Es gibt keinen Ort, an dem der Nachweis *am Bild* gespeichert ist, so dass jede Software ihn findet, ohne eine Bildunterschrift zu lesen.

Eingebettete Metadaten (EXIF, XMP, IPTC) lösen das nur scheinbar: Sie hängen an der Datei, nicht am Inhalt, und die meisten Plattformen entfernen sie beim Upload. Ein Nachweis, der den ersten Re-Encode nicht überlebt, ist kein Nachweis.

## Was wir anders machen

Wir hängen die Lizenz an das Bild selbst. Nicht an die Datei im Sinne einer eingebetteten Notiz, die beim nächsten Speichern verloren geht, sondern an ihren **Fingerabdruck**.

Jede Datei hat einen: eine lange Zeichenfolge, die sich aus ihrem Inhalt berechnet (technisch: der [SHA-256-Hash](https://de.wikipedia.org/wiki/SHA-2)). Ändert sich ein einziges Pixel, ändert sich der Fingerabdruck. Zwei identische Kopien haben denselben. Das ist der Trick: **Wer die Bytes hat, hat den Fingerabdruck. Wer den Fingerabdruck hat, findet den Nachweis.**

Der Nachweis selbst ist ein kleiner, digital signierter Zettel im offenen Datenraum von [edufeed](https://edufeed.org/). Er sagt: *Zu dem Bild mit diesem Fingerabdruck gehört diese Lizenz, diese Urheberin, diese Quelle, dieser Alt-Text, und es wurde so und so mit KI erzeugt.* Signiert von der Person oder Institution, die das bestätigt.

Wo das Bild liegt, ist dabei zweitrangig. Es kann auf unserem Bildserver liegen, auf dem einer Landeskirche, auf einer WordPress-Seite. Eine Adresse benennt einen Ort. Ein Fingerabdruck benennt den Inhalt. Ein Bild, das umzieht, behält seine Lizenz.

## Warum wir das Platin nennen

Der [Gold-Standard](https://open-educational-resources.de/gold-standard/) sagt: Die Angaben sind vollständig. Wir gehen drei Schritte weiter.

**Maschinenlesbar.** Der Nachweis ist kein Fließtext, sondern strukturiert: ein Feld für die Lizenz-URL, eines für die Urheberin, eines für die Quelle, eines für den Alt-Text, eines für die KI-Kennzeichnung, eine Liste für Schlagworte. Jeder Client kann ihn auslesen und anzeigen, ohne zu raten, was in der Bildunterschrift gemeint war.

**Signiert.** Der Nachweis trägt eine kryptografische Unterschrift. Man sieht, wer die Angabe gemacht hat, und dass sie seitdem nicht verändert wurde. Wer ein Bild nachnutzt, kann sich darauf berufen.

**Weiterverwendbar in einem Klick.** Im [edufeed-Client](https://edufeed.org/) steht am Bild das Lizenz-Badge, bei KI-Bildern mit der KI-Marke nach den Icons des EU AI Office, die die [Transparenzpflicht des EU AI Act](https://artificialintelligenceact.eu/article/50/) umsetzen. Wer das Bild in ein eigenes Material übernimmt, kopiert den vollständigen Lizenztext mit einem Klick, korrekt formatiert, mit allen Links. Die TULLU-Regel wird nicht mehr von Hand angewendet, sie wird ausgeliefert.

Und der Nachweis reist mit. Ein Bild, das aus einem Blogbeitrag in einen Kalendertermin wandert, in eine Materialsammlung, in einen Flyer, der aus dem Datenraum erzeugt wird: überall dieselbe Lizenzzeile, aus derselben Quelle.

## Was das für Autor:innen bedeutet

Konkret: eine Handvoll Zeilen pro Bild. Wer für oer.community schreibt, trägt im Frontmatter des Beitrags zu jedem Bild einen Eintrag im `bilder`-Block ein:

```yaml
bilder:
  klassengespraech.jpg:
    alt: Zwei Jugendliche und eine Lehrerin am Tisch, dazwischen ein Tablet mit Chatbot-Dialog
    title: Urteilsbildung im Gespräch
    author: Olav Richter mit ChatGPT, 13.09.2026
    authorUrl: https://www.rpi-baden.de
    licence: CC0 1.0
    licenceUrl: https://creativecommons.org/publicdomain/zero/1.0/deed.de
    ai: generated
    keywords: [klassenraum, tablet, chatbot, lehrerin, illustration, classroom, teacher]
```

Der Rest passiert automatisch: Das Bild wird auf den Bildserver geladen, der Nachweis erzeugt und signiert, die Lizenzzeile gerendert. Für eigene Fotos gilt die Hausregel (CC BY FOERBICO), für fremde Werke stehen Urheber:in, Quelle und deren Lizenz im Block.

Drei Regeln haben sich dabei als die wichtigsten herausgestellt:

1. **Ohne Lizenz kein Bild im Datenraum.** Fehlt die Lizenzangabe, bricht das Werkzeug mit einem `TODO:LICENSE` ab, und der Client zeigt ein neutrales Ersatzmotiv. Das ist keine Strafe, sondern ein Anreiz: Wer sein Bild überall sehen will, klärt die Lizenz. Es funktioniert besser als jede Ermahnung.
2. **KI-Kennzeichnung ist eigenes Feld, keine Lizenz.** `ai: generated` für vollständig KI-erzeugte Bilder, `ai: modified` für menschliche Bilder, die mit KI bearbeitet wurden. Die Kennzeichnung ersetzt weder Lizenz noch Urheber:in. Wer prompted, ist genannt. Und: Kein `ai`-Feld heißt „nicht deklariert", nicht „ohne KI".
3. **Eine Erlaubnis ist keine Lizenz.** „Mit freundlicher Genehmigung" darf so im Nachweis stehen, aber dann als das, was es ist: Rechte vorbehalten, Nutzung an diesem Ort erlaubt. Der Client zeigt das Bild, aber niemand wird zur Weitergabe eingeladen. Ehrlich ist besser als eine erfundene CC-Lizenz.

Dazu kommt seit Oktober 2026 eine vierte, optionale Angabe: **Schlagworte**, die beschreiben, *was zu sehen ist* und *wofür das Bild taugt*, deutsch und englisch nebeneinander. Sie machen das Bild im Datenraum auffindbar, unabhängig vom Beitrag, in dem es zuerst stand.

## Unter der Haube

Der Datenraum von edufeed basiert auf dem [Nostr-Protokoll](https://nostr.com/): signierte JSON-Events, die über Relays verteilt werden. Drei Bausteine greifen ineinander.

### Der Nachweis: ein Event vom Typ `kind 1063`

Die Spezifikation [NIP-94](https://github.com/nostr-protocol/nips/blob/master/94.md) definiert Datei-Metadaten als Event `kind 1063`. edufeed erweitert es um Lizenz-Felder; die Konvention steht im edufeed-Wiki unter [*License events for uploaded files*](https://edufeed.org/c/npub1hhpplya3ut9h2cyvant6pgq2w7thnkfk0hyhnz7e7gflqmy4h3yqp2p4pk/wiki/naddr1qvzqqqrcvgpzp0wzr7fmrcktw4sgemxh5zsq5auh08vnvlwf0x9anusn7pkft0zgqyv8wumn8ghj7un9d3shjtn9v36kvet9vshx7un89uqsuamnwvaz7tmwdaejumr0dshsqymvd93k2mnnv5kk2an9de68xttwdacx2txs053). Das echte Event zum Titelbild aus dem ersten Absatz, gekürzt:

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

Das `x`-Tag ist der Fingerabdruck. Die Abbildung vom `bilder`-Block auf die Tags ist in unserer [Bildattributions-Konvention](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/src/branch/main/Orga/oer-community-webseite-orga/wissensgrundlagen/bildattribution.md) festgelegt:

| Block | Tag | Bemerkung |
|---|---|---|
| Datei | `url`, `x`, `m`, `size` | aus der Datei berechnet |
| `title` | `title` | |
| `author` | `credit` | |
| `authorUrl` | `authorUrl` | FOERBICO-Zusatzfeld |
| `licenceUrl` | `license` | |
| `sourceUrl` | `source` | |
| `alt` | `alt` | |
| `modification` | `modification` | FOERBICO-Zusatzfeld |
| `ai` | `ai` | nur `generated` oder `modified`, sonst kein Tag |
| `keywords` | `t` (je Schlagwort) | lowercase nach [NIP-24](https://github.com/nostr-protocol/nips/blob/master/24.md), ohne `#` |

Die Zusatzfelder haben keinen NIP-Standard. Clients, die sie nicht kennen, ignorieren sie; die Kernfelder bleiben lesbar.

### Die Auflösung: vom Hash zum Nachweis

Jeder Client, der ein Bild anzeigen will, fragt die Relays:

```json
["REQ", "lizenz", { "kinds": [1063], "#x": ["bb3dfcb3815161763ed2e6250c11446c95934f0f1bed60c5c6dca80148867d7b"] }]
```

Gibt es mehrere Antworten, gewinnt die neueste. So lässt sich ein Nachweis korrigieren oder um Schlagworte ergänzen, ohne das Bild anzufassen: Es wird einfach ein neues `kind 1063` mit demselben Hash geprägt.

Die Bilder selbst liegen auf einem [Blossom](https://github.com/hzrd149/blossom)-Server, der Dateien über ihren Hash adressiert, weshalb die URL den Fingerabdruck bereits enthält. Das Bild kann aber ebenso gut anderswo liegen; der Nachweis gilt für die Bytes, nicht für den Ort. Wer ein Bild von irgendwoher hat, rechnet den SHA-256 und fragt nach.

Der Inhalt, der das Bild nutzt, etwa ein Blogbeitrag (`kind 30023`) oder ein Kalendertermin (`kind 31923`), trägt denselben Hash in einem eigenen `x`-Tag. So löst der Client den Nachweis auf, ohne die Bild-URL zu kennen, und so bleibt die Verbindung erhalten, wenn das Bild gespiegelt wird.

### Die Werkzeugkette: vom Markdown zum signierten Event

Für oer.community läuft das in drei Schritten, die bewusst getrennt sind, damit der private Schlüssel nirgends im Build liegt:

1. **Hochladen.** Ein Skript lädt die Bilddateien per [BUD-01](https://github.com/hzrd149/blossom/blob/master/buds/01.md) auf den Blossom-Server und prüft den zurückgemeldeten Hash gegen die lokale Datei. Vorhandene Blobs werden übersprungen.
2. **Umschreiben und prägen.** `md2blossom` hasht die Bilder, ersetzt im Markdown die relativen Pfade durch Hash-URLs, schreibt die Lizenzzeile als Bildunterschrift direkt unter jedes Bild im Fließtext und legt für jeden Eintrag im `bilder`-Block ein unsigniertes `kind 1063` ab. Bilder ohne Eintrag stoppen den Lauf mit `TODO:LICENSE` und einer Vorlage für den Block.
3. **Signieren und publizieren.** Die Signatur kommt über einen [NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md)-Bunker, der den FOERBICO-Schlüssel hält. Die signierten Events gehen auf die edufeed-Relays. Den Artikel selbst (`kind 30023`) publiziert die CI nach dem Merge auf `main`.

Auf der Website rendert ein Hugo-Partial aus dem `bilder`-Block die Lizenzpille am Titelbild; der Block im Frontmatter ist dabei Eingabe zum Prägen, das `kind 1063` auf dem Relay ist die Wahrheit. Beides ist offen und darf nachgebaut werden: die [Skripte](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/src/branch/main/Website/scripts) im Repository, die Konvention im Wiki.

## Was noch nicht fertig ist

Wir sind ehrlich: Das ist ein Anfang, kein Abschluss.

- **Prompt und Modell.** Für KI-Bilder dokumentieren wir bereits, mit welchem Prompt und welchem Modell sie entstanden sind. Im Nachweis stehen sie noch nicht, weil die Konvention dafür in Arbeit ist. Der Vorschlag: zwei weitere Felder, `prompt` und `ai-model`, mit der Regel, dass der Prompt *diese eine* Generierung dokumentiert, nicht jede mögliche.
- **Lizenzpille im Fließtext.** Am Titelbild rendert die Website die Pille live aus dem Block. Bei Bildern im Text steht die Lizenzzeile bisher als Bildunterschrift, die das Werkzeug beim Umschreiben erzeugt. Dieselbe Auflösung über den Hash, aber noch nicht dieselbe Darstellung.
- **Wer darf korrigieren?** „Das neueste Event gewinnt" ist einfach, aber es beantwortet nicht, wessen neuestes Event gilt, wenn Urheberin und Plattform verschiedene Angaben machen. Bisher prägt FOERBICO alle Nachweise für oer.community. Ein Modell für mehrere Signaturen am selben Hash fehlt.
- **Der Bestand.** Von 89 Beiträgen auf oer.community tragen inzwischen 86 den `bilder`-Block, rund 200 Bilder haben einen signierten Nachweis. Das war Handarbeit, jedes Bild einzeln, weil jede Lizenz geprüft werden musste. Sie lohnt sich nur einmal.

Wer das für die eigene Plattform übernehmen will, ob mit WordPress, TYPO3, Hugo oder etwas anderem: Die Bausteine sind offen, die Relays sind offen, und wir helfen gern. Der Fingerabdruck eines Bildes ist überall derselbe. Das ist die ganze Idee.

## Fazit

Ein Bildnachweis, der neben dem Bild steht, ist so gut wie der Ort, an dem er steht. Ein Nachweis, der am Fingerabdruck hängt, ist so gut wie die Bytes, und die sind überall dieselben. Was in den Nachweis gehört, hat die OER-Community längst geklärt. Wo er bleibt, war die offene Frage. Das hier ist unsere Antwort.

Und wer vor der Technik erst einmal die Praxisfragen klären will, welche Bilder gehen, welche nicht, und wie die Ampel steht: [„OER und das vermeintliche Bildlizenz-Dilemma“](https://oer.community/bildlizenz-dilemma/).
