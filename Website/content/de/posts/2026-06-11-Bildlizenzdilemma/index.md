---
# commonMetadata
'@context': https://schema.org/
creativeWorkStatus: Draft
type: LearningResource
name: 'OER und das vermeintliche Bildlizenz-Dilemma – ein FAQ für die Praxis'
description: >-
  Sobald Bilder ins Spiel kommen, wird OER für viele kompliziert: Unsicherheit bei Lizenzen, Angst vor Abmahnungen, die Sorge, etwas falsch zu machen. Dieses FAQ beantwortet die Fragen, die uns aus der Praxis am häufigsten begegnen: Google-Bilder, eigene Fotos, KI-Bilder, Canva, die Schranke des § 60a UrhG, freie Bilddatenbanken und der richtige Nachweis. Dazu ein Ampelsystem für die Bildnutzung, das wir zur Diskussion stellen.
license: https://creativecommons.org/licenses/by/4.0/deed.de
id: https://oer.community/bildlizenz-dilemma
creator:
  - givenName: Gina
    familyName: Buchwald-Chassée
    type: Person
    affiliation:
      name: Comenius-Institut
      id: https://ror.org/025e8aw85
      type: Organization
  - givenName: Jörg
    familyName: Lohrer
    type: Person
    affiliation:
      name: Comenius-Institut
      id: https://ror.org/025e8aw85
      type: Organization
inLanguage:
  - de
about:
  - https://w3id.org/kim/hochschulfaechersystematik/n0
learningResourceType:
  - https://w3id.org/kim/hcrt/text
  - https://w3id.org/kim/hcrt/web_page
datePublished: '2026-06-11'   # TODO: beim Veröffentlichen auf das Erscheinungsdatum setzen
keywords:
  - OER
  - Bildlizenzen
  - Creative Commons
  - Urheberrecht
  - KI-Kennzeichnung
  - Bilddatenbanken
  - Bildnachweis
  - FOERBICO

# staticSiteGenerator
author:
  - Gina Buchwald-Chassée
  - Jörg Lohrer
title: 'OER und das vermeintliche Bildlizenz-Dilemma'
cover:
  relative: true
  image: TODO-titelbild.jpg
  alt: 'TODO – Alt-Text des Titelbilds'
  hiddenInSingle: false
summary: >-
  Bilder machen OER kompliziert – müssen sie aber nicht. Die Fragen aus der Praxis als FAQ: Was darf ich, was nicht, wo finde ich freie Bilder, wie weise ich richtig nach? Dazu ein Ampelsystem für die Bildnutzung zur Diskussion.
url: bildlizenz-dilemma
tags:
  - OER
  - Bildlizenzen
  - Urheberrecht
  - Creative Commons
  - KI-Kennzeichnung
# bilder  (Konvention: bildattribution.md · Schlüssel = Dateiname oder Hash-URL)
# Lizenz nach Footer von oer.community: CC BY FOERBICO, soweit nicht anders angegeben.
# TODO: Titelbild anlegen (Vorschlag: eigenes Motiv mit ai: generated, Prompt dokumentieren) und Eintrag ergänzen.
bilder: {}
---

Die Erstellung von Open Educational Resources sollte niedrigschwellig, kreativ und unkompliziert sein. Doch sobald Bilder ins Spiel kommen, wird es für viele kompliziert: Unsicherheit bei Lizenzen, Angst vor Abmahnungen, die Sorge, etwas falsch zu machen. Das Ergebnis ist oft paradox: Materialien werden gar nicht erst veröffentlicht oder nur stark eingeschränkt genutzt, obwohl OER genau das Gegenteil ermöglichen soll.

Die gute Nachricht vorweg: Das „Bildlizenz-Dilemma“ ist kein OER-Problem. Es ist ein Problem digitaler Mediennutzung überhaupt, und OER ist der Teil davon, der eine Lösung hat.

Dieses FAQ sammelt die Fragen, die uns in Workshops und Beratungen am häufigsten begegnen. Wer wissen will, wie wir in FOERBICO und edufeed den Lizenznachweis technisch *an das Bild selbst* hängen, maschinenlesbar und signiert, liest danach den Beitrag [„Ein Bild, das seine Lizenz kennt“](https://oer.community/bildlizenzen-maschinenlesbar/).

## Muss ich bei OER besonders auf Bildrechte achten?

Nein, nicht *besonders*. Das Urheberrecht gilt immer, unabhängig davon, ob ein Material eine CC-Lizenz trägt oder nicht. Auch klassische Unterrichtsmaterialien, „normale“ Blogbeiträge, Präsentationen oder Websites können Rechte verletzen. Online-Verfügbarkeit bedeutet nicht Nutzungsrecht.

Ein Bild aus der Google-Suche oder von einer beliebigen Website zu übernehmen ist also nicht „sicherer“, nur weil es kein OER ist, im Gegenteil: Dort ist meist unklarer, was erlaubt ist, und das Risiko ist größer. Der Unterschied bei OER ist nicht, dass mehr Regeln gelten, sondern dass die Regeln sichtbar sind.

## Ich habe das Bild selbst fotografiert. Darf ich es verwenden?

Meistens ja, aber prüft kritisch, *was* oder *wer* abgebildet ist. Marken- und Personenrechte gelten unabhängig vom Urheberrecht. Sind Personen erkennbar, braucht es eine Fotofreigabe; sind Minderjährige abgebildet, die Zustimmung der Eltern. Sind Personen nicht erkennbar, dürft ihr das Bild auch ohne Freigabe verwenden.

Auch Coverbilder, Logos und Screenshots stehen unter Copyright und dürfen nicht ohne schriftliche Genehmigung verwendet werden, selbst wenn ihr den Screenshot selbst gemacht habt.

## Ich habe das Bild mit KI erzeugt. Ist es dann gemeinfrei?

Nicht automatisch. Was mit einem KI-Bild erlaubt ist, hängt von den Bedingungen des jeweiligen Anbieters ab, und die unterscheiden sich. Ein KI-Bild, das auf Stock-Material aufsetzt (etwa aus der Canva-Bibliothek), darf nicht offen weitergegeben werden, auch wenn es durch einen KI-Filter gelaufen ist.

Was ihr in jedem Fall tun solltet: das Bild als KI-generiert ausweisen und nennen, wer geprompted hat. Das ist keine Formalie, sondern seit dem EU AI Act eine [Transparenzpflicht](https://artificialintelligenceact.eu/article/50/). Wie wir die KI-Kennzeichnung als eigenes Feld im Lizenznachweis führen, steht im [Technik-Beitrag](https://oer.community/bildlizenzen-maschinenlesbar/#was-das-für-autorinnen-bedeutet).

## Canva, Pixabay, Unsplash – das ist doch alles kostenlos?

Kostenlos ist nicht frei. Bilder aus der Canva-Bibliothek, von Unsplash, Pixabay & Co. stehen unter der jeweiligen Anbieter-Lizenz, und die erlaubt meist die Nutzung im eigenen Design, aber nicht die Weitergabe des Bildes an Dritte. Für OER, die ja weitergegeben werden sollen, ist das ein Problem. Gekaufte Bilder von iStock oder Getty Images sind ebenfalls nicht weiterverwendbar; sie müssen ausgewiesen werden und dürfen nicht unter CC gestellt werden. Ausführlich dazu: unser Beitrag [„Canva für OER? Eine Entscheidungshilfe“](https://oer.community/canva/).

## Gibt es Ausnahmen für Unterricht und Lehre?

Ja: die [15%-Regel aus § 60a UrhG](https://open-educational-resources.de/ausnahmen-vom-urheberrecht/) für Unterricht und Lehre, und Entsprechendes für [Wissenschaft und Forschung](https://www.uni-bremen.de/urheberrecht/wissensplattform/6-sonderfall-wissenschaftliche-forschung). Ihr dürft danach etwa wissenschaftliche Abbildungen verwenden, aber auch die müssen korrekt ausgewiesen werden. Und: Die Schranke gilt für den geschützten Raum von Unterricht und Lehre, nicht für die offene Veröffentlichung als OER. Mehr dazu beim [Deutschen Bibliotheksverband](https://www.bibliotheksverband.de/sites/default/files/2024-08/Urheberrecht_Bildung_Wissenschaft_Kultur.pdf) und bei [irights.info](https://irights.info/artikel/cc-lizenz-und-gesetzliche-nutzungserlaubnisse/32561).

## Wo finde ich Bilder, die ich wirklich verwenden darf?

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

## Wie weise ich ein Bild richtig nach?

Mit der [TULLU-Regel](https://open-educational-resources.de/oer-tullu-regel/): **T**itel, **U**rheber:in, **L**izenz, **L**ink zur Lizenz, **U**rsprungsort. Das ist der [Gold-Standard](https://open-educational-resources.de/gold-standard/) der OER-Community, und wer ihn befolgt, macht es richtig. Bei bearbeiteten Bildern kommt die Angabe der Änderung dazu. Auch automatisch erzeugte Vorschaubilder müssen ausgewiesen werden.

Werkzeuge, die dabei helfen: der [Lizenzhinweisgenerator](https://lizenzhinweisgenerator.de/), der [CC-Stamper](https://ccstamper.edu-sharing.org/) und der [Bildmetadatengenerator](https://joerglohrer.github.io/bildmetagenerator/bildlizenzgenerator.html).

<!-- TODO (Gina): Inhalte aus dem ZOERR-Workshop zum Bildnachweis hier ergänzen? Stand im ersten Entwurf als Platzhalter. -->

Mehr zu alldem in unserem [Lernmodul zu OER und OEP](https://oer.community/oer-und-oep/lernmodul/).

## Und wie bleibt der Nachweis am Bild, wenn es kopiert wird?

Das ist die Frage, an der die TULLU-Regel an ihre Grenze kommt. Der Nachweis ist Text: Er steht in einer Bildunterschrift, in einem Impressum, in einer Fußnote. Sobald das Bild in eine Präsentation wandert oder auf einer anderen Website erscheint, ist der Nachweis weg, weil er nie *am* Bild hing, sondern daneben stand.

In FOERBICO und edufeed hängen wir den Nachweis deshalb an den Fingerabdruck der Bilddatei: als signierten, maschinenlesbaren Datensatz, den jeder Client findet, sobald er das Bild hat. Für Autor:innen auf oer.community heißt das: eine Handvoll Zeilen pro Bild, der Rest passiert automatisch. Wie das funktioniert, warum wir das „Platin“ nennen und wie es unter der Haube aussieht, erklärt der Beitrag [„Ein Bild, das seine Lizenz kennt“](https://oer.community/bildlizenzen-maschinenlesbar/).

## Zur Diskussion: ein Ampelsystem für die Bildnutzung

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

## Fazit

Das „Bildlizenz-Dilemma“ ist weniger ein Problem von OER als ein allgemeines Problem digitaler Mediennutzung. OER ist nicht die Einschränkung von Kreativität durch Regeln, sondern die Befreiung von Unsicherheit durch Klarheit.

Und wer die Klarheit nicht nur in die Bildunterschrift, sondern an das Bild selbst hängen will: [„Ein Bild, das seine Lizenz kennt“](https://oer.community/bildlizenzen-maschinenlesbar/).
