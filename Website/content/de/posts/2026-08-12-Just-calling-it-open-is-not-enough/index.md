---
# commonMetadata
'@context': https://schema.org/
creativeWorkStatus: Published
type: LearningResource
name: 'Just calling it Open is not enough – Hürden öffentlicher Bildungsinfrastrukturen und erste Lösungsansätze mit Nostr'
description: >-
  OER sind offen lizenzierte Bildungsmaterialien, die meist unter einer Creative-Commons-Lizenz veröffentlicht werden. Sie lassen sich also nicht nur frei nutzen, sondern auch anpassen, weiterentwickeln und erneut veröffentlichen. Seit Jahren werden deshalb sowohl die Erstellung freier Materialien als auch Plattformen und Repositorien gefördert, die diese Materialien auffindbar machen sollen. Trotzdem lässt sich eine scheinbar simple Frage bis heute nicht eindeutig beantworten: Wo kann ich mein OER-Material veröffentlichen?.
license: https://creativecommons.org/licenses/by/4.0/deed.de
id: https://oer.community/just-calling-it-open-is-not-enough
creator:
    - givenName: Gina
    familyName: Buchwald-Chassée
    type: Person
    affiliation:
      name: Comenius-Institut
      id: https://ror.org/025e8aw85
      type: Organization
    - givenName: Steffen
    familyName: Roertgen
    type: Person
    affiliation:
      name: Comenius-Institut
      id: https://ror.org/025e8aw85
      type: Organization
    - givenName: Jannik
    familyName: Streek
    type: Person
    affiliation:
      name: B310 Digital GmbH
      type: Organization
inLanguage:
  - de
about:
  - https://w3id.org/kim/hochschulfaechersystematik/n0
learningResourceType:
  - https://w3id.org/kim/hcrt/text
  - https://w3id.org/kim/hcrt/web_page
image: https://open-educational-resources.de/wp-content/uploads/260811_Nostr_Protokoll.png
educationalLevel:
  - https://w3id.org/kim/educationalLevel/level_A
datePublished: '2026-08-12'
keywords:
  - Open Educational Resources (OER)
  - Open Educational Practices (OEP)
  - Metadaten
  - interoperabel
  - Vernetzung
  - dezentral

# staticSiteGenerator
author:
  - Gina Buchwald-Chassée
  - Steffen Rörtgen
  - Jannik Streek
title: 'Just calling it Open is not enough – Hürden öffentlicher Bildungsinfrastrukturen und erste Lösungsansätze mit Nostr'
cover:
  relative: true
  image: https://open-educational-resources.de/wp-content/uploads/260811_Nostr_Protokoll.png
  alt: 'Herausforderungen öffentlicher Bildungsinfrastrukturen. Bild: Steffen Rörtgen, Gina Buchwald-Chassée und Jannik Streek, KI-generiert'
  hiddenInSingle: false
summary: >-
  OER sind offen lizenzierte Bildungsmaterialien, die meist unter einer Creative-Commons-Lizenz veröffentlicht werden. Sie lassen sich also nicht nur frei nutzen, sondern auch anpassen, weiterentwickeln und erneut veröffentlichen. Seit Jahren werden deshalb sowohl die Erstellung freier Materialien als auch Plattformen und Repositorien gefördert, die diese Materialien auffindbar machen sollen. Trotzdem lässt sich eine scheinbar simple Frage bis heute nicht eindeutig beantworten: Wo kann ich mein OER-Material veröffentlichen?
url: just-calling-it-open-is-not-enough
tags:
  - Open Educational Resources (OER)
  - Open Educational Practices (OEP)
  - Metadaten
  - interoperabel
  - Vernetzung
  - dezentral
---

## Die Problematik

Der Grund ist eine stark fragmentierte Bildungslandschaft. Es existieren zahlreiche OER-Plattformen, auf denen sich Materialien hochladen lassen. Doch die Inhalte bleiben meist innerhalb der jeweiligen Plattform eingeschlossen und sind anderswo weder sichtbar noch weiterverwendbar. Viele Angebote sind zudem an bestimmte Bildungskontexte gebunden oder veröffentlichen Inhalte erst nach eigenen Prüf- und Freigabeprozessen. Einfaches, öffentliches und plattformübergreifendes Teilen ist dadurch kaum möglich.

Das verweist auf ein grundlegenderes Problem: Heute sind Infrastruktur und Plattform meist untrennbar verbunden. Wer die Infrastruktur betreibt, betreibt zugleich den Service – und kontrolliert damit nicht nur Funktionen und Interaktionen, sondern auch den Zugang zu Daten und Inhalten. So entstehen dieselben Lock-in-Effekte, die man von großen Medienplattformen kennt: Inhalte, Metadaten und Nutzer*innen bleiben an einzelne Systeme gebunden und können ihre Daten nicht einfach auf andere Plattformen mitnehmen.

Eine echte öffentliche Bildungsinfrastruktur müsste dagegen offen zugänglich sein und den freien Austausch von Daten ermöglichen – unabhängig davon, welche Services darauf aufsetzen. Plattformen könnten dann weiterhin unterschiedliche Oberflächen, Communities oder Zusatzfunktionen anbieten, ohne Inhalte voneinander abzuschotten.

## Der Ist-Zustand

Der heutige Zustand ist ungefähr so, als würde jeder Autohersteller eigene Straßen bauen – und zwar nur für die eigenen Fahrzeuge. Einzelne Verbindungsstraßen existieren bereits, beispielsweise zwischen [OERSI](https://oersi.org/) und [twillo](https://www.twillo.de/) sowie diversen anderen Hochschulrepositorien. Doch ein allgemeiner, offener „Verkehrsraum“ für Bildung fehlt.

Diese Fragmentierung zeigt sich an vielen Stellen. Lade ich ein Material auf Plattform A hoch, bleibt es meist auch dort. Nutzer*innen müssen sich entweder auf vielen Plattformen parallel registrieren und Inhalte mehrfach hochladen oder akzeptieren, dass ihre Materialien nur in einzelnen Ökosystemen sichtbar sind. Aggregatoren wie der Open Educational Resources Search Index (OERSI) mildern das Problem, indem sie Metadaten verschiedener Plattformen zentral indexieren. Doch auch dieser Ansatz bleibt begrenzt: Er funktioniert nur für Quellen, die aktiv eingebunden werden, fokussiert bestimmte Bildungsbereiche und beruht auf einem aufwändigen Pull-Prinzip, bei dem Plattformen Inhalte gegenseitig crawlen und importieren müssen.

Ähnlich verhält es sich bei Kuration und Metadaten. Sammlungen oder Listen, die auf einer Plattform entstehen, lassen sich selten auf andere übertragen oder dort kollaborativ weiterführen. Metadaten werden meist zentral vergeben, oft einmalig beim Upload durch Redaktionen oder Einzelpersonen. Nutzer*innen können ihr eigenes Wissen über Materialien kaum ergänzen oder alternative Nutzungskontexte sichtbar machen, obwohl genau darin ein großes Potenzial gemeinschaftlicher Wissensproduktion liegt.

Auch Suche und Indexierung sind ineffizient organisiert: Viele Plattformen entwickeln eigene Crawler, Schnittstellen und Suchindizes, oft parallel und redundant. Kleine Akteure ohne technische Ressourcen bleiben außen vor. Und selbst plattformübergreifende Zusammenarbeit – etwa bei Qualitätssicherung, Peer-Review oder gemeinsamen Empfehlungen – ist technisch kaum möglich, obwohl offene Bildungspraktiken (#OEP) intensiv diskutiert werden. Dasselbe gilt zunehmend für KI-Dienste: Werkzeuge zur automatischen Verschlagwortung, Suche oder Empfehlung funktionieren meist nur innerhalb der Plattform, für die sie entwickelt wurden, und entstehen vielerorts parallel.

So unterschiedlich diese Probleme wirken – fehlende Interoperabilität, doppelte Erschließung, isolierte Plattformen, nicht-portable Sammlungen, plattformgebundene KI-Services –, sie haben dieselbe strukturelle Ursache. Die meisten heutigen Bildungsplattformen koppeln drei Dinge eng aneinander:

   - User – die Menschen und Communities,
   - Services – Oberflächen und Anwendungen,
   - Daten – Inhalte, Metadaten, Sammlungen und Interaktionen.

Nutzer*innen interagieren über einen Service mit Daten, die innerhalb derselben Plattform gespeichert und kontrolliert werden. Genau daraus entstehen die bekannten Lock-in-Effekte. Für kommerzielle Plattformen ist das oft Teil des Geschäftsmodells. Für öffentliche Bildungsinfrastrukturen ist es jedoch problematisch, weil so genau die Silostrukturen reproduziert werden, die offene Bildung eigentlich überwinden will.

## Von Plattformen zu Protokollen

Ein alternativer Ansatz besteht darin, diese drei Ebenen zu entkoppeln und statt auf isolierte Plattformen auf offene Protokolle zu setzen. Genau hier wird das Nostr-Protokoll für den Bildungsbereich interessant. [Nostr](https://nostr.com/) steht für „Notes and Other Stuff Transmitted by Relays“ und ist ein offenes, dezentrales Protokoll, das ursprünglich für soziale Netzwerke entwickelt wurde. Im Kern beschreibt es kein konkretes Produkt und keine einzelne Plattform, sondern eine gemeinsame Sprache für den Austausch von Daten.

Der entscheidende Unterschied zu klassischen Plattformarchitekturen: Identität, Datenhaltung und Services werden voneinander entkoppelt. Ein Service besitzt die Daten nicht mehr exklusiv, sondern wird zur Oberfläche auf einer gemeinsamen Infrastrukturbasis. Nutzer*innen können dieselben Daten über verschiedene Anwendungen hinweg verwenden, ohne ihre Inhalte, Metadaten oder sozialen Beziehungen zu verlieren. Plattformen konkurrieren dann nicht mehr um exklusive Datenbestände, sondern um die besseren Interfaces, Communities oder Zusatzfunktionen.
Identitäten statt Accounts

In klassischen Plattformen wird Identität über Benutzerkonten organisiert: Die Plattform verwaltet Login, Passwort und Profil und bindet die Identität damit an sich.
Nostr verfolgt einen anderen Ansatz. Nutzer*innen besitzen ihre Identität selbst, in Form eines kryptografischen Schlüsselpaars aus einem Private Key und einem Public Key. Der Private Key bleibt geheim und funktioniert wie eine digitale Unterschrift: Mit ihm signieren Nutzer*innen Daten und beweisen, dass ein bestimmtes Event tatsächlich von ihnen stammt. Der Public Key ist die öffentliche Identität; andere können damit die Gültigkeit einer Signatur prüfen, ohne den privaten Schlüssel zu kennen, ähnlich einer E-Mail-Signatur.

Dieses Prinzip steckt bereits in vielen alltäglichen Technologien, etwa in HTTPS, Messengern oder digitalen Zertifikaten. Nostr nutzt es konsequent als Grundlage für digitale Identität in einem offenen Netzwerk. Dadurch gehört die Identität nicht mehr einer Plattform, sondern den Nutzer*innen selbst. Wer von Service A zu Service B wechselt, behält dieselbe Identität – und ebenso Inhalte, Kontakte und Interaktionen, sofern die verwendeten Relays die jeweiligen Daten bereitstellen.
Events statt proprietärer Datenmodelle

Die eigentlichen Daten werden bei Nostr als sogenannte Events gespeichert und verteilt. Ein Event ist ein signierter Datensatz in einem standardisierten JSON-Format; vereinfacht gesagt wird jede Aktion im Netzwerk als Event beschrieben – etwa ein veröffentlichter Beitrag, Metadaten zu einem OER-Material, eine Materialsammlung, ein Kommentar, eine Annotation, eine Bewertung oder ein Verweis auf externe Dateien wie PDFs oder Videos.

Jedes Event enthält unter anderem den öffentlichen Schlüssel des Urhebers, einen Zeitstempel, einen Typ (das „kind“, also etwa Termin oder Blogbeitrag), den eigentlichen Inhalt, zusätzliche Metadaten sowie eine kryptografische Signatur. Diese Signatur stellt sicher, dass ein Event nicht unbemerkt verändert werden kann und eindeutig einer Identität zugeordnet ist. Weil Events standardisiert aufgebaut sind, können unterschiedliche Anwendungen dieselben Daten lesen, interpretieren und weiterverarbeiten – unabhängig davon, von welchem Service sie ursprünglich veröffentlicht wurden.
NIPs: Gemeinsame Regeln für Interoperabilität

Damit unterschiedliche Anwendungen dieselben Daten verstehen, definiert Nostr sogenannte NIPs („Nostr Implementation Possibilities“). Das sind offene Spezifikationen, die beschreiben, wie bestimmte Eventtypen oder Funktionen strukturiert sein sollen – etwa wie Profile aussehen, wie Kommentare referenziert werden, wie Listen und Sammlungen funktionieren, wie Medien eingebunden oder wie Suchanfragen formuliert werden.

Interoperabilität entsteht so nicht über zentrale Plattformen oder proprietäre APIs, sondern über gemeinsam genutzte Protokollregeln. Sammlungen, Annotationen, Metadaten oder Qualitätssiegel lassen sich dadurch unabhängig von der konkreten Anwendung plattformübergreifend verstehen und weiterverarbeiten.

## Relays als gemeinsame Infrastruktur

Verteilt werden die Events über sogenannte Relays: vergleichsweise einfache Server, die Events entgegennehmen, speichern und an andere Teilnehmer*innen weitergeben. Sie bilden die gemeinsame Transport- und Verteilungsschicht der Infrastruktur.

Wichtig ist: Relays sind keine Plattformen im klassischen Sinn. Sie definieren weder Benutzeroberflächen noch Geschäftslogiken oder Nutzungsszenarien. Unterschiedliche Anwendungen können dieselben Relays nutzen und dieselben Daten unterschiedlich darstellen. Dadurch werden Services austauschbar: Eine Plattform ist nicht länger der Ort, an dem Daten existieren, sondern nur noch eine Oberfläche, die Daten sichtbar und nutzbar macht.

Das hat erhebliche Folgen für Nachhaltigkeit und Resilienz. Im heutigen Plattformmodell verschwinden Inhalte häufig gemeinsam mit der Plattform: Wird ein Projekt eingestellt, läuft eine Förderung aus oder verschwindet eine Institution, gehen oft auch Inhalte, Metadaten, Sammlungen und Interaktionen verloren. In einer relaybasierten Infrastruktur sind Daten dagegen verteilt gespeichert und nicht an eine einzelne Anwendung gebunden. Mehrere Relays können dieselben Events halten und weiterverteilen; fällt ein Relay oder ein Service aus, bleiben die Daten an anderer Stelle verfügbar, und neue Anwendungen können jederzeit darauf zugreifen.

Gerade für öffentlich finanzierte Bildungsressourcen ist das relevant. Wenn Materialien als Gemeingut verstanden werden, sollte ihre Verfügbarkeit nicht davon abhängen, ob eine bestimmte Plattform oder Förderung weiterhin existiert.
Binärdaten und Medieninhalte

Für größere Dateien wie Bilder, Videos oder PDFs gibt es ergänzende Ansätze wie sogenannte Blossom-Server („Blobs stored simply on mediaservers“). Dabei liegen die Binärdaten auf spezialisierten Medienservern, während Metadaten, Referenzen und Interaktionen weiterhin über Nostr-Events verteilt werden. Auch hier bleibt das Grundprinzip erhalten: Daten und Services sind voneinander entkoppelt, und Anwendungen greifen nicht auf proprietäre Silos zu, sondern auf gemeinsam verfügbare Inhalte.

## Offenheit als Infrastrukturprinzip

Ein protokollbasierter Ansatz bedeutet nicht, dass alle Anwendungen gleich aussehen oder dieselben Funktionen bieten müssen. Unterschiedliche Communities können weiterhin eigene Plattformen, Qualitätsprozesse, Suchoberflächen oder KI-Dienste entwickeln. Der Unterschied: Diese Services operieren nicht mehr auf isolierten Datensilos, sondern auf einem gemeinsamen offenen Datenraum. Offenheit findet damit nicht nur auf der Ebene der Lizenzierung statt, sondern auch auf der Ebene der Infrastruktur selbst.
Vom Infrastrukturprinzip zur Anwendung – erste Prototypen auf Nostr-Basis

Der beschriebene Ansatz ist nicht rein theoretisch. Im Rahmen der Förderlinien OE_Space und OE_Sprint des Bundesministeriums für Bildung, Familie, Senioren, Frauen und Jugend (BMBFSFJ) sind bereits erste Anwendungen entstanden, die den Einsatz des Nostr-Protokolls in offenen Bildungsinfrastrukturen praktisch erproben:

   - ComCal – ein verteilter Veranstaltungskalender zur Vernetzung von Communities und Terminen,

   - ein Onboarding-Tool für niedrigschwellige Zugänge zu Nostr-basierten Bildungsanwendungen,

   - ein kollaboratives Kanban-Board für Inhaltsmanagement und Zusammenarbeit,

   - ein OER-Finder-Plugin zur plattformübergreifenden Suche offener Bildungsressourcen,

   - sowie der Edugraph zur Visualisierung von Inhalts- und Beziehungsnetzwerken.

Die folgenden Beispiele zeigen, wie Anwendungen auf Basis offener, protokollbasierter Bildungsinfrastrukturen aussehen können – Werkzeuge, die nicht in geschlossenen Datensilos operieren, sondern auf einem dezentralen, offenen Fundament aufsetzen. Perspektivisch soll das Nostr-Protokoll auch als infrastrukturelle Grundlage für den im [FOERBICO-Projekt](https://oer.community/) entstehenden Community-Hub dienen, der als „Community of Communities“ unterschiedliche Akteure und Netzwerke offener (religionsbezogener) Bildung verbinden soll.

## ComCal – ein interoperabler Community-Kalender

Mit ComCal entstand in OE_Space ein erster Community-Kalender auf Basis des Nostr-Protokolls. Ausgangspunkt war eine vertraute Beobachtung: Veranstaltungen werden meist in geschlossenen Kalendersilos organisiert, häufig gekoppelt an einzelne Webseiten, Content-Management-Systeme oder Plattformen. Das führt zu Medienbrüchen, Mehrfacheingaben und Lock-in-Effekten. Wer Termine sichtbar machen will, pflegt sie oft parallel in mehreren Kalendern, und die Daten bleiben an einzelne Plattformen gebunden.

ComCal versteht Veranstaltungen stattdessen als offene, portable Datenobjekte innerhalb eines gemeinsamen Netzwerks. Unterschiedliche Anwendungen können auf dieselben Veranstaltungsdaten zugreifen, sie darstellen, filtern oder weiterverarbeiten. Ein Termin muss damit idealerweise nur einmal erstellt werden und lässt sich anschließend in verschiedenen Clients, Webseiten oder Kalenderanwendungen nutzen.

Technisch baut ComCal auf der Spezifikation NIP-52 auf, die standardisierte Eventtypen für Kalender- und Veranstaltungsdaten definiert – darunter zeitgebundene Veranstaltungen, Event-Sammlungen sowie Zu- und Absagen (RSVPs). Veranstaltungen werden als signierte Events über Relays verteilt und können von unterschiedlichen Anwendungen konsumiert werden. Erprobt wurden bereits diverse Funktionen: Communities pflegen gemeinsame Kalender, machen Veranstaltungen abonnierbar und integrieren Termine über Formate wie .ics in bestehende Desktop-Kalender. Veranstaltungen lassen sich mit Metadaten wie Ort, Zeit, Personen, Bildern, Tags oder Einschreibungsinformationen anreichern und nach Format (online, hybrid, vor Ort), Themen oder Zielgruppen filtern.

Eine besondere Herausforderung liegt in der Integration bestehender Systeme. Auf dem letzten [HackathOERn](https://oer.community/hackathoern-2026/) wurde diesbezüglich ein Chat-Bot entwickelt, der Termine aus WordPress-Instanzen ausliest und als Nostr-Event veröffentlichen kann. Umgekehrt ist die Frage zu lösen, wie bestehende Plattformen sich leichtgewichtig an diese interoperable Infrastruktur so anschließen, dass sie Daten nicht nur abgeben, sondern die offen zugänglichen Daten anderer Anbieter in ihrer bisher geschlossenen technischen Konfiguration nutzen. Erkennbar wird damit aber jetzt schon, dass und wie bestehende Plattformen nicht abgelöst, sondern um eine interoperable Infrastrukturebene ergänzt werden.

Der Prototyp ist mittlerweile weiterentwickelt worden und unter [https://dev.edufeed.org/discover?type=events](https://dev.edufeed.org/discover?type=events) erreichbar.

## Onboarding-Tool – ein niedrigschwelliger Einstieg

Dezentrale Systeme sind strukturell leistungsfähig, scheitern in der Praxis aber oft an der ersten Hürde: dem Einstieg. Besonders der Umgang mit kryptografischen Schlüsselpaaren und das Verständnis eines nicht-plattformgebundenen Identitätsmodells sind für viele Bildungsakteur*innen eine Einstiegsschwelle. Das in OE_Sprint entwickelte Onboarding-Tool setzt hier an und führt Nutzer*innen schrittweise, intuitiv und interaktiv durch die erste Nutzung. Der Umgang mit dem eigenen Schlüsselpaar wird dabei erklärt und begleitet, sodass die Idee einer selbstverwalteten digitalen Identität verständlich wird ohne technisches Vorwissen.

Ergänzend bietet das Tool „Follow-Packs“: didaktisch und thematisch kuratierte Einstiegspakete, die erste sinnvolle Kontakte, relevante Accounts und passende Inhalte vorschlagen. Sie erleichtern den Aufbau eines initialen Netzwerks und helfen, sich schnell in thematische Communities einzufinden. Damit fungiert das Tool als zentraler Einstiegsknotenpunkt gerade für Lehrkräfte und Bildungsakteur*innen, die mit klassischen Plattformen vertraut sind, aber wenig Erfahrung mit dezentralen Systemen haben. Ziel ist, die Einstiegshürde insgesamt zu senken und die Motivation zu erhöhen, sich aktiv in eine offene, vernetzte OER-Landschaft einzubringen.

Der erste Prototyp ist unter [https://onboarding.edufeed.org/](https://onboarding.edufeed.org/) verfügbar; der Open-Source-Code steht unter [https://github.com/edufeed-org/onboarding-tool](https://github.com/edufeed-org/onboarding-tool) zur Nachnutzung bereit.

Mehr dazu auch unter: [https://oer.community/edufeed-pitch/](https://oer.community/edufeed-pitch/)

![Onboarding-Tool](https://open-educational-resources.de/wp-content/uploads/d93403fc-28e8-4b20-87b6-1b57149ca152-768x581.png)

Onboarding-Tool-Screenshot; Comenius-Institut Münster e.V., [CC BY 4.0-Lizenz](http://creativecommons.org/licenses/by/4.0/)

## Kanban-Board – kollaboratives Arbeiten ohne Silos

Ebenfalls in OE_Sprint entstand ein lokal im Browser laufender Kanban-Editor als offenes Gegenstück zu proprietären Plattformen wie TaskCards oder Padlet. Wo solche Systeme geschlossene Arbeitsräume erzeugen, in denen Boards und Inhalte an die Plattform gebunden bleiben, verfolgt dieser Prototyp einen protokollbasierten Ansatz: Inhalte werden nicht zentral gespeichert, sondern lassen sich über das Nostr-Protokoll als portable, nachnutzbare Datenstrukturen teilen.

Nutzer*innen können Inhalte erstellen, flexibel strukturieren und ganze Board-Arrangements plattformübergreifend verfügbar machen. Aus einem klassischen Projektmanagement-Tool wird so zugleich ein Werkzeug für Lernorganisation, Unterrichtsplanung und kollaborative Inhaltsentwicklung im OER-Kontext. Der Editor unterstützt KI-gestützte Zusammenfassungen und Vorschläge sowie Exporte nach Markdown, HTML oder JSON, sodass sich Inhalte leicht weiterverwenden oder in andere Systeme überführen lassen. Lehrende und Lernende können gemeinsam an Lernarrangements arbeiten und etwa Inhalte aus OER-Quellen wie OERSI oder edu-sharing direkt in Boards integrieren. Eine Integration in den LiaScript-Editor verbindet die dezentral gespeicherten Inhalte zusätzlich mit konkreten Lernanwendungen.

Der Kanban-Editor versteht sich damit als experimentelle Infrastrukturkomponente für offene Bildungspraktiken, die kollaboratives Arbeiten ermöglicht, ohne Inhalte in geschlossenen Plattformstrukturen zu isolieren. Ein eigenes Board lässt sich unter https://kanban.edufeed.org/ anlegen; der Code steht Open Source unter https://github.com/edufeed-org/kanban-editor bereit.

![](https://open-educational-resources.de/wp-content/uploads/481038a1-39bb-4133-82c7-0396ce330217-768x663.png)

Kanban-Screenshot; Comenius-Institut Münster e.V., [CC BY 4.0-Lizenz](http://creativecommons.org/licenses/by/4.0/)

## OER-Finder-Plugin – die Suche kommt zur Anwendung

Wer schon einmal eine passende offene Bildungsressource für einen Kurs gesucht hat, kennt das Muster: Plattform durchsuchen, Lizenz prüfen, Bild herunterladen, Tab wechseln, Datei hochladen, Format prüfen und dann dasselbe noch einmal für die nächste Ressource auf der nächsten Plattform.

Dabei ist das OER-Ökosystem in den letzten Jahren bemerkenswert gewachsen: ARASAAC liefert Piktogramme für unterstützte Kommunikation, Wikimedia stellt Millionen frei lizenzierter Medien bereit, und über das Nostr-Edufeed-Netzwerk fließen Bildungsinhalte dezentral zusammen. An Material mangelt es also nicht. Das Problem ist, dass jede Plattform in ihrem eigenen Silo lebt mit eigenen Suchmasken, APIs und Metadatenformaten. Wer Inhalte integrieren will, muss jede Quelle einzeln anbinden; wer Inhalte finden will, jede Plattform einzeln durchforsten.

Das fehlende Puzzlestück ist eine bessere Verzahnung von Quellen und Anwendungen. Das [OER-Finder-Plugin](https://github.com/edufeed-org/oer-finder-plugin) setzt genau hier an: Statt Nutzende zu den Quellen zu schicken, kommen die Quellen in die Anwendung. Ein wiederverwendbarer JavaScript-Baustein bringt die Suche über mehrere OER-Anbieter hinweg direkt in die Lernumgebung. Nach der Integration können Nutzende aus der Anwendung heraus über verschiedene Quellen suchen, ohne die Plattform zu verlassen, unter anderem über OpenVerse, ARASAAC, Wikimedia und das Nostr-Edufeed-Netzwerk. Einzelne Quellen lassen sich aktivieren oder deaktivieren, das Look & Feel ist konfigurierbar. Für Entwicklungsteams ist die Einstiegshürde bewusst niedrig: Dokumentation für die Integration in React, Angular und Svelte sind bereits im Projekt zu finden.

Offene Bildungsressourcen entfalten ihren Wert erst, wenn sie genutzt werden. Jeder zusätzliche Schritt zwischen dem reinen Wunsch und dem Finden einer korrekt lizenzierten Ressource verringert diese Wahrscheinlichkeit. Das Plugin verkürzt den Weg und setzt dabei auf Offenheit in beide Richtungen: Der Baustein selbst ist Open Source und aggregiert offene Quellen. Neue Anbieter lassen sich ergänzen, ohne dass Nutzende ihr Verhalten ändern müssen. So entsteht eine gemeinsame, integrierte Suche in der fragmentierten OER-Landschaft. Im Kanban-Board ist das bereits umgesetzt und wird aktuell verprobt: Dort lassen sich Bilder nun direkt zu Karten hinzufügen. Der Code  für das Plugin befindet sich auf [GitHub](https://github.com/edufeed-org/oer-finder-plugin).

## Edugraph – inhaltsbezogene Kommunikation sichtbar gemacht

Der ebenfalls in OE_Sprint entwickelte Edugraph macht die dezentrale Struktur des Nostr-Protokolls für einen inhaltsbezogenen Austauschraum nutzbar. Die Idee: Kommunikation nicht losgelöst von Inhalten zu betrachten, sondern direkt an OER-Materialien, Kurs-URLs, Tags oder Klassifikationen zu koppeln. So entsteht ein protokollbasierter Kommunikationsraum rund um Lerninhalte, in dem Lehrende und Lernende unmittelbar am jeweiligen Material diskutieren, ergänzen und kontextualisieren statt in isolierten Kommentarspalten einzelner Plattformen.

Der Edugraph visualisiert diese Interaktionen als Netzwerke, Cluster oder Wolken: Thematisch verwandte Inhalte rücken visuell zusammen, Diskussionsräume verdichten sich um bestimmte Ressourcen, und Beziehungen zwischen Materialien werden als dynamische Graphen erfahrbar. Damit wird die Grundidee der dezentralen Infrastruktur auch auf der Anwendungsebene sichtbar: Inhalte sind nicht isoliert, sondern Teil eines vernetzten Wissensraums, der sich durch Nutzung, Austausch und Kontextualisierung weiterentwickelt.

![Bild Edugraph](https://open-educational-resources.de/wp-content/uploads/970d2f7e-3233-45e9-9e76-e9c56ed80619.png)

Edugraph-Screenshot; Comenius-Institut Münster e.V., [CC BY 4.0-Lizenz](http://creativecommons.org/licenses/by/4.0/)

Der erste Prototyp ist unter [https://map.edufeed.org](https://map.edufeed.org) verfügbar, der Open-Source-Code unter [https://github.com/edufeed-org/nostr-graph-explorer](https://github.com/edufeed-org/nostr-graph-explorer).

Dieser Text steht unter der [CC BY 4.0-Lizenz](http://creativecommons.org/licenses/by/4.0/). Der Name des Urhebers soll bei einer Weiterverwendung wie folgt genannt werden: Steffen Rörtgen & Gina Buchwald-Chassée, [Comenius-Institut](https://comenius.de/), und Jannik Streek, [B310 Digital GmbH](https://b310.de/), für [OERinfo – Die Informationsstelle OER](https://www.o-e-r.de/).


      