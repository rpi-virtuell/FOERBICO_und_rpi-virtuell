---
# commonMetadata
'@context': https://schema.org/
creativeWorkStatus: Draft
type: LearningResource
name: 'Ein Bild, das seine Lizenz kennt: Bildlizenzen in OER – ein FAQ für die Praxis und die Technik dahinter'
description: >-
  Sobald Bilder ins Spiel kommen, wird OER für viele kompliziert: Unsicherheit bei Lizenzen, Angst vor Abmahnungen. Teil 1 beantwortet die Fragen aus der Praxis (Google-Bilder, eigene Fotos, KI-Bilder, Canva, § 60a, freie Bilddatenbanken, richtiger Nachweis) und stellt ein Ampelsystem zur Diskussion. Teil 2 zeigt, wie FOERBICO und edufeed den Nachweis an das Bild selbst hängen: als signierten, maschinenlesbaren Nachweis am Fingerabdruck der Datei, der mitreist, wohin das Bild auch kopiert wird.
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
  - Urheberrecht
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
  Bilder machen OER kompliziert – müssen sie aber nicht. Teil 1: die Fragen aus der Praxis als FAQ, dazu ein Ampelsystem zur Diskussion. Teil 2: wie wir den Lizenznachweis an das Bild selbst hängen, maschinenlesbar und signiert, so dass er mitreist, wohin das Bild auch kopiert wird.
url: bildlizenzen-maschinenlesbar
tags:
  - OER
  - Bildlizenzen
  - Urheberrecht
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

Dieser Beitrag hat zwei Teile. **Teil 1** beantwortet die Fragen, die uns aus der Praxis am häufigsten begegnen: Was darf ich, was nicht, wo finde ich freie Bilder, wie weise ich richtig nach? **Teil 2** erklärt, was wir in FOERBICO und edufeed gebaut haben, damit der Nachweis nicht mehr neben dem Bild steht, sondern zu ihm gehört. Wer nur wissen will, was zu tun ist, kann nach Teil 1 aufhören. Wer wissen will, warum es funktioniert, liest weiter.

# Teil 1: Bilder in OER – die Fragen aus der Praxis

Die Erstellung von Open Educational Resources sollte niedrigschwellig, kreativ und unkompliziert sein. Doch sobald Bilder ins Spiel kommen, wird es für viele kompliziert: Unsicherheit bei Lizenzen, Angst vor Abmahnungen, die Sorge, etwas falsch zu machen. Das Ergebnis ist oft paradox: Materialien werden gar nicht erst veröffentlicht oder nur stark eingeschränkt genutzt, obwohl OER genau das Gegenteil ermöglichen soll.

Die gute Nachricht vorweg: Das „Bildlizenz-Dilemma“ ist kein OER-Problem. Es ist ein Problem digitaler Mediennutzung überhaupt, und OER ist der Teil davon, der eine Lösung hat.

### Muss ich bei OER besonders auf Bildrechte achten?

Nein, nicht *besonders*. Das Urheberrecht gilt immer, unabhängig davon, ob ein Material eine CC-Lizenz trägt oder nicht. Auch klassische Unterrichtsmaterialien, „normale“ Blogbeiträge, Präsentationen oder Websites können Rechte verletzen. Online-Verfügbarkeit bedeutet nicht Nutzungsrecht.

Ein Bild aus der Google-Suche oder von einer beliebigen Website zu übernehmen ist also nicht „sicherer“, nur weil es kein OER ist, im Gegenteil: Dort ist meist unklarer, was erlaubt ist, und das Risiko ist größer. Der Unterschied bei OER ist nicht, dass mehr Regeln gelten, sondern dass die Regeln sichtbar sind.

### Ich habe das Bild selbst fotografiert. Darf ich es verwenden?

Meistens ja, aber prüft kritisch, *was* oder *wer* abgebildet ist. Marken- und Personenrechte gelten unabhängig vom Urheberrecht. Sind Personen erkennbar, braucht es eine Fotofreigabe; sind Minderjährige abgebildet, die Zustimmung der Eltern. Sind Personen nicht erkennbar, dürft ihr das Bild auch ohne Freigabe verwenden.

Auch Coverbilder, Logos und Screenshots stehen unter Copyright und dürfen nicht ohne schriftliche Genehmigung verwendet werden, selbst wenn ihr den Screenshot selbst gemacht habt.

### Ich habe das Bild mit KI erzeugt. Ist es dann gemeinfrei?

Nicht automatisch. Was mit einem KI-Bild erlaubt ist, hängt von den Bedingungen des jeweiligen Anbieters ab, und die unterscheiden sich. Ein KI-Bild, das auf Stock-Material aufsetzt (etwa aus der Canva-Bibliothek), darf nicht offen weitergegeben werden, auch wenn es durch einen KI-Filter gelaufen ist.

Was ihr in jedem Fall tun solltet: das Bild als KI-generiert ausweisen und nennen, wer geprompted hat. Das ist keine Formalie, sondern seit dem EU AI Act eine [Transparenzpflicht](https://artificialintelligenceact.eu/article/50/). Wie das bei uns konkret aussieht, steht in Teil 2.

### Canva, Pixabay, Unsplash – das ist doch alles kostenlos?

Kostenlos ist nicht frei. Bilder aus der Canva-Bibliothek, von Unsplash, Pixabay & Co. stehen unter der jeweiligen Anbieter-Lizenz, und die erlaubt meist die Nutzung im eigenen Design, aber nicht die Weitergabe des Bildes an Dritte. Für OER, die ja weitergegeben werden sollen, ist das ein Problem. Gekaufte Bilder von iStock oder Getty Images sind ebenfalls nicht weiterverwendbar; sie müssen ausgewiesen werden und dürfen nicht unter CC gestellt werden. Ausführlich dazu: unser Beitrag [„Canva für OER? Eine Entscheidungshilfe“](https://oer.community/canva/).

### Gibt es Ausnahmen für Unterricht und Lehre?

Ja: die [15%-Regel aus § 60a UrhG](https://open-educational-resources.de/ausnahmen-vom-urheberrecht/) für Unterricht und Lehre, und Entsprechendes für [Wissenschaft und Forschung](https://www.uni-bremen.de/urheberrecht/wissensplattform/6-sonderfall-wissenschaftliche-forschung). Ihr dürft danach etwa wissenschaftliche Abbildungen verwenden, aber auch die müssen korrekt ausgewiesen werden. Und: Die Schranke gilt für den geschützten Raum von Unterricht und Lehre, nicht für die offene Veröffentlichung als OER. Mehr dazu beim [Deutschen Bibliotheksverband](https://www.bibliotheksverband.de/sites/default/files/2024-08/Urheberrecht_Bildung_Wissenschaft_Kultur.pdf) und bei [irights.info](https://irights.info/artikel/cc-lizenz-und-gesetzliche-nutzungserlaubnisse/32561).

### Wo finde ich Bilder, die ich wirklich verwenden darf?

Hier liegt der eigentliche Vorteil von OER: Offene Lizenzen wie die von [Creative Commons](https://creativecommons.org/) sind klar definiert. Werden sie korrekt angewendet, entsteht Rechtssicherheit: Nutzung erlaubt, Bearbeitung erlaubt (je nach Lizenz), Weitergabe erlaubt, Bedingungen transparent.

Bilddatenbanken mit frei lizenzierten Bildern gibt es inzwischen viele:

- [Openverse](https://openverse.org/) – Suche über viele Quellen hinweg, mit Lizenzfilter
- [Wikimedia Commons](https://commons.wikimedia.org/wiki/Main_Page)
- [Coco Material](https://cocomaterial.com/) – handgezeichnete Illustrationen
- [Nappy.co](https://nappy.co/) – Fotos, die Vielfalt abbilden
- [pxhere](https://pxhere.com/), [StockSnap.io](https://stocksnap.io/), [Skitterphoto](https://skitterphoto.com) – Fotos
- [Public Domain Vectors](https://publicdomainvectors.org/), [Openclipart](https://openclipart.org/) – Vektorgrafiken
- [Humaaans](https://humaaans.com/) – Illustrationen von Menschen

Gesammelte Übersichten führen [ZUM](https://apps.zum.de/quellen), [ZOERR](https://www.zoerr.de/edu-sharing/components/render/30d941b7-c7b8-4cf0-9941-b7c7b88cf06d) und [OERinfo](https://open-educational-resources.de/oer_materialien/wo-finde-ich-kostenlose-bilder-eine-sammlung-von-quellen-fuer-frei-lizensierte-fotos-und-abbildungen/). Und in den Bildersuchen der großen Suchmaschinen lässt sich über den Suchfilter nach Creative-Commons-Lizenzen filtern.

Wenn kein passendes freies Bild zu finden ist: eigene Zeichnung, eigenes Foto, oder ein Link zum Bild statt der Bilddatei.

### Wie weise ich ein Bild richtig nach?

Mit der [TULLU-Regel](https://open-educational-resources.de/oer-tullu-regel/): **T**itel, **U**rheber:in, **L**izenz, **L**ink zur Lizenz, **U**rsprungsort. Das ist der [Gold-Standard](https://open-educational-resources.de/gold-standard/) der OER-Community, und wer ihn befolgt, macht es richtig. Bei bearbeiteten Bildern kommt die Angabe der Änderung dazu. Auch automatisch erzeugte Vorschaubilder müssen ausgewiesen werden.

Werkzeuge, die dabei helfen: der [Lizenzhinweisgenerator](https://lizenzhinweisgenerator.de/), der [CC-Stamper](https://ccstamper.edu-sharing.org/) und der [Bildmetadatengenerator](https://joerglohrer.github.io/bildmetagenerator/bildlizenzgenerator.html).

Mehr zu alldem in unserem [Lernmodul zu OER und OEP](https://oer.community/oer-und-oep/lernmodul/).

### Zur Diskussion: ein Ampelsystem für die Bildnutzung

Lizenzfragen sind komplex, Entscheidungen im Alltag müssen schnell gehen. Ein Ampelsystem könnte beides zusammenbringen. Wir haben es noch nicht umgesetzt, und wir stellen es hier bewusst als Vorschlag zur Diskussion: als Denkhilfe für Autor:innen, und perspektivisch als Element im Community-Hub, das beim Hochladen eines Bildes sofort anzeigt, woran man ist.

🔴 **Rot – geht nicht**

- Bilder unter Copyright ohne schriftliche Genehmigung
- Screenshots von Websites, Social Media oder Artikeln
- Bilder ohne erkennbare Lizenz oder Quelle: „kein Copyright-Hinweis = frei“ gilt nicht

Hohe Abmahngefahr, keine rechtliche Absicherung.

🟡 **Gelb – noch zulässig, aber eingeschränkt**

- Restriktive CC-Lizenzen: CC BY-NC (problematisch im kommerziellen Kontext) oder CC BY-ND (keine Bearbeitung, für viele OER-Szenarien ungeeignet)
- Gekaufte Stock-Bilder (iStock, Getty): ausweisen, nicht weiterverwendbar
- Anbieter-Lizenzen (Canva, Unsplash, Pixabay): nutzbar, aber nicht weitergabefähig

Lizenzbedingungen prüfen; Weitergabe oder Anpassung sind oft nicht möglich.

🟢 **Grün – Best Practice**

- CC BY, CC BY-SA, CC0 mit vollständigem Nachweis (Urheber:in, Lizenz, Quelle, ggf. Änderungen)

OER-konform, weitergabefähig, rechtssicher.

Passt diese Einteilung zu eurer Praxis? Fehlt eine Kategorie? Wir freuen uns über Rückmeldungen, bevor daraus ein Werkzeug wird.

# Teil 2: Wie der Nachweis am Bild bleibt

Wer Teil 1 gelesen hat, weiß jetzt, *was* in einen Bildnachweis gehört. Bleibt die Frage, *wo* er bleibt.

### Das Problem: Der Nachweis steht neben dem Bild

Die TULLU-Regel aus Teil 1 ist der Gold-Standard, und wer sie befolgt, macht es richtig. Nur: Der Nachweis ist Text. Er steht in einer Bildunterschrift, in einem Impressum, in einer Fußnote. Sobald das Bild kopiert wird, in eine Präsentation wandert, auf einer anderen Website erscheint, in einem Kalender-Eintrag auftaucht, ist der Nachweis weg. Nicht aus Böswilligkeit, sondern weil er nie am Bild hing, sondern daneben stand.

In der Praxis führt das zu drei Zuständen, die wir alle kennen:

- **Nachweis vorhanden, aber unbrauchbar.** „Quelle: eigene Darstellung mit KI und Canva." Wer darf das Bild weiterverwenden? Unter welchen Bedingungen? Die Angabe sagt es nicht, und Stock-Material aus Canva oder iStock darf ohnehin nicht offen weitergegeben werden, auch wenn es durch einen KI-Filter gelaufen ist.
- **Nachweis vorhanden, aber nicht weitergabefähig.** „Mit freundlicher Genehmigung." Das ist eine Erlaubnis für eine Person an einem Ort. Wer das Bild an einem zweiten Ort zeigt, hat sie nicht.
- **Kein Nachweis.** Das Bild ist da, sonst nichts. Der häufigste Fall.

Alle drei haben dieselbe Ursache. Es gibt keinen Ort, an dem der Nachweis *am Bild* gespeichert ist, so dass jede Software ihn findet, ohne eine Bildunterschrift zu lesen.

### Was wir anders machen

Wir hängen die Lizenz an das Bild selbst. Nicht an die Datei im Sinne einer eingebetteten Notiz, die beim nächsten Speichern verloren geht, sondern an ihren **Fingerabdruck**.

Jede Datei hat einen: eine lange Zeichenfolge, die sich aus ihrem Inhalt berechnet (technisch: der [SHA-256-Hash](https://de.wikipedia.org/wiki/SHA-2)). Ändert sich ein einziges Pixel, ändert sich der Fingerabdruck. Zwei identische Kopien haben denselben. Das ist der Trick: **Wer die Bytes hat, hat den Fingerabdruck. Wer den Fingerabdruck hat, findet den Nachweis.**

Der Nachweis selbst ist ein kleiner, digital signierter Zettel im offenen Datenraum von [edufeed](https://edufeed.org/). Er sagt: *Zu dem Bild mit diesem Fingerabdruck gehört diese Lizenz, diese Urheberin, diese Quelle, dieser Alt-Text, und es wurde so und so mit KI erzeugt.* Signiert von der Person oder Institution, die das bestätigt.

Wo das Bild liegt, ist dabei zweitrangig. Es kann auf unserem Bildserver liegen, auf dem einer Landeskirche, auf einer WordPress-Seite. Eine Adresse benennt einen Ort. Ein Fingerabdruck benennt den Inhalt. Ein Bild, das umzieht, behält seine Lizenz.

### Warum wir das Platin nennen

Der Gold-Standard sagt: Die Angaben sind vollständig. Wir gehen drei Schritte weiter.

**Maschinenlesbar.** Der Nachweis ist kein Fließtext, sondern strukturiert: ein Feld für die Lizenz-URL, eines für die Urheberin, eines für die Quelle, eines für den Alt-Text, eines für die KI-Kennzeichnung. Jeder Client kann ihn auslesen und anzeigen, ohne zu raten, was in der Bildunterschrift gemeint war.

**Signiert.** Der Nachweis trägt eine kryptografische Unterschrift. Man sieht, wer die Angabe gemacht hat, und dass sie seitdem nicht verändert wurde. Wer ein Bild nachnutzt, kann sich darauf berufen.

**Weiterverwendbar in einem Klick.** Im [edufeed-Client](https://edufeed.org/) steht am Bild das Lizenz-Badge, bei KI-Bildern mit der KI-Marke nach den Icons des EU AI Office, die die [Transparenzpflicht des EU AI Act](https://artificialintelligenceact.eu/article/50/) umsetzen. Wer das Bild in ein eigenes Material übernimmt, kopiert den vollständigen Lizenztext mit einem Klick, korrekt formatiert, mit allen Links. Die TULLU-Regel wird nicht mehr von Hand angewendet, sie wird ausgeliefert.

Und der Nachweis reist mit. Ein Bild, das aus einem Blogbeitrag in einen Kalendertermin wandert, in eine Materialsammlung, in einen Flyer, der aus dem Datenraum erzeugt wird: überall dieselbe Lizenzzeile, aus derselben Quelle.

### Was das für Autor:innen bedeutet

Konkret: eine Handvoll Zeilen pro Bild. Wer für oer.community schreibt, trägt zu jedem Bild ein:

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
```

Der Rest passiert automatisch: Das Bild wird auf den Bildserver geladen, der Nachweis erzeugt und signiert, die Lizenzzeile gerendert. Für eigene Fotos gilt die Hausregel (CC BY FOERBICO), für fremde Werke stehen Urheber:in, Quelle und deren Lizenz im Block.

Drei Regeln haben sich dabei als die wichtigsten herausgestellt:

1. **Ohne Lizenz kein Bild im Datenraum.** Fehlt die Lizenzangabe, zeigt der Client ein neutrales Ersatzmotiv. Das ist keine Strafe, sondern ein Anreiz: Wer sein Bild überall sehen will, klärt die Lizenz. Es funktioniert besser als jede Ermahnung.
2. **KI-Kennzeichnung ist eigenes Feld, keine Lizenz.** `ai: generated` für vollständig KI-erzeugte Bilder, `ai: modified` für menschliche Bilder, die mit KI bearbeitet wurden. Die Kennzeichnung ersetzt weder Lizenz noch Urheber:in. Wer prompted, ist genannt. Und: Kein `ai`-Feld heißt „nicht deklariert", nicht „ohne KI".
3. **Eine Erlaubnis ist keine Lizenz.** „Mit freundlicher Genehmigung" darf so im Nachweis stehen, aber dann als das, was es ist: Rechte vorbehalten, Nutzung an diesem Ort erlaubt. Der Client zeigt das Bild, aber niemand wird zur Weitergabe eingeladen. Ehrlich ist besser als eine erfundene CC-Lizenz.

### Für Entwickler:innen: wie es unter der Haube aussieht

Der Datenraum von edufeed basiert auf dem [Nostr-Protokoll](https://nostr.com/). Der Lizenznachweis ist ein Event vom Typ `kind 1063`, das die Spezifikation [NIP-94](https://github.com/nostr-protocol/nips/blob/master/94.md) für Datei-Metadaten definiert, erweitert um Lizenz-Felder. Das echte Event zum Titelbild aus dem ersten Absatz:

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

Die vollständige Konvention steht im edufeed-Wiki unter [*License events for uploaded files*](https://edufeed.org/c/npub1hhpplya3ut9h2cyvant6pgq2w7thnkfk0hyhnz7e7gflqmy4h3yqp2p4pk/wiki/naddr1qvzqqqrcvgpzp0wzr7fmrcktw4sgemxh5zsq5auh08vnvlwf0x9anusn7pkft0zgqyv8wumn8ghj7un9d3shjtn9v36kvet9vshx7un89uqsuamnwvaz7tmwdaejumr0dshsqymvd93k2mnnv5kk2an9de68xttwdacx2txs053); die Autor:innen-Seite in unserer [Bildattributions-Konvention](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/src/branch/main/Orga/oer-community-webseite-orga/wissensgrundlagen/bildattribution.md). Beides ist offen und darf nachgebaut werden.

### Was noch nicht fertig ist

Wir sind ehrlich: Das ist ein Anfang, kein Abschluss.

- **Prompt und Modell.** Für KI-Bilder speichern wir bereits, mit welchem Prompt und welchem Modell sie entstanden sind. Im Nachweis stehen sie noch nicht, weil die Konvention dafür in Arbeit ist. Der Vorschlag: zwei weitere Felder, `prompt` und `ai-model`, mit der Regel, dass der Prompt *diese eine* Generierung dokumentiert, nicht jede mögliche.
- **Bilder im Fließtext.** Die Lizenzzeile erscheint bisher am Titelbild. Für Bilder im Text ist der Weg derselbe, aber noch nicht gebaut.
- **Der Bestand.** Von rund 90 Beiträgen auf oer.community tragen 16 den Nachweis. Die übrigen werden nach und nach nachgezogen, jedes Bild einzeln, weil jede Lizenz geprüft werden muss. Das ist Handarbeit, und sie lohnt sich nur einmal.

Wer das für die eigene Plattform übernehmen will, ob mit WordPress, TYPO3, Hugo oder etwas anderem: Die Bausteine sind offen, die Relays sind offen, und wir helfen gern. Der Fingerabdruck eines Bildes ist überall derselbe. Das ist die ganze Idee.

### Fazit

Das „Bildlizenz-Dilemma“ ist weniger ein Problem von OER als ein allgemeines Problem digitaler Mediennutzung. OER ist nicht die Einschränkung von Kreativität durch Regeln, sondern die Befreiung von Unsicherheit durch Klarheit. Und wenn die Klarheit am Bild selbst hängt, statt in einer Bildunterschrift, dann bleibt sie auch dort, wo das Bild hingeht.
