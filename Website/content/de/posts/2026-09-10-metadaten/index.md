---
# commonMetadata
'@context': https://schema.org/
creativeWorkStatus: Published
type: LearningResource
name: 'Metadaten – die unsichtbare Infrastruktur offener Bildung'
description: >-
  Metadaten entscheiden maßgeblich darüber, ob Open Educational Resources gefunden, eingeordnet und nachgenutzt werden können. Dieser Beitrag erläutert, was Metadaten sind, wie die Standards LOM, Dublin Core und das Allgemeine Metadatenprofil für Bildungsressourcen (AMB) die Auffindbarkeit von OER strukturieren und warum selbst gepflegte Metadatensätze Lücken aufweisen, etwa bei der kompetenzbezogenen Erschließung. Da Metadaten keine neutralen, sondern soziotechnisch geprägte Angaben sind, plädiert der Beitrag zudem dafür, ihren Entstehungskontext sichtbar zu machen. Abschließend werden Konsequenzen für den Aufbau eines interoperablen, religionspädagogischen OER-Ökosystems skizziert.
license: https://creativecommons.org/licenses/by/4.0/deed.de
id: https://oer.community/metadaten-die-unsichtbare-infrastruktur-offener-bildung
creator:
  - givenName: Laura
    familyName: Mößle
    id: https://orcid.org/0000-0001-5255-8063
    type: Person
    affiliation:
      name: Johann Wolfgang Goethe-Universität Frankfurt
      id: https://ror.org/04cvxnb49
      type: Organization
  - givenName: Phillip
    familyName: Angelina
    id: https://orcid.org/0000-0002-6905-5523
    type: Person
    affiliation:
      name: Friedrich-Alexander-Universität Erlangen-Nürnberg
      id: https://ror.org/00f7hpc57
      type: Organization
inLanguage:
  - de
about:
  - https://w3id.org/kim/hochschulfaechersystematik/n053
  - https://w3id.org/kim/hochschulfaechersystematik/n086
  - https://w3id.org/kim/hochschulfaechersystematik/n052
learningResourceType:
  - https://w3id.org/kim/hcrt/text
  - https://w3id.org/kim/hcrt/web_page
image: https://oer.community/metadaten-die-unsichtbare-infrastruktur-offener-bildung/metadata.jpg
educationalLevel:
  - https://w3id.org/kim/educationalLevel/level_A
datePublished: '2026-09-10'
keywords:
  - Open Educational Resources (OER)
  - Metadaten
  - interoperabel
  - Vernetzung
  - dezentral
  - Qualitätskriterien

# staticSiteGenerator
author:
  - Laura Mößle
  - Phillip Angelina
title: 'Metadaten – die unsichtbare Infrastruktur offener Bildung'
cover:
  relative: true
  image: metadata.jpg
  alt: 'Holzbausteine, die das Wort „Metadaten" bilden, Foto von [Markus Winkler](https://unsplash.com/de/@markuswinkler?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
      auf [Unsplash](https://unsplash.com/de/fotos/ein-holzklotz-mit-der-aufschrift-metadaten-der-auf-einem-tisch-liegt-9DZsVF-qLaY?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)'
  hiddenInSingle: false
summary: >-
  Metadaten entscheiden maßgeblich darüber, ob Open Educational Resources gefunden, eingeordnet und nachgenutzt werden können. Dieser Beitrag erläutert, was Metadaten sind, wie die Standards LOM, Dublin Core und das Allgemeine Metadatenprofil für Bildungsressourcen (AMB) die Auffindbarkeit von OER strukturieren und warum selbst gepflegte Metadatensätze Lücken aufweisen, etwa bei der kompetenzbezogenen Erschließung. Da Metadaten keine neutralen, sondern soziotechnisch geprägte Angaben sind, plädiert der Beitrag zudem dafür, ihren Entstehungskontext sichtbar zu machen. Abschließend werden Konsequenzen für den Aufbau eines interoperablen, religionspädagogischen OER-Ökosystems skizziert.
url: metadaten-die-unsichtbare-infrastruktur-offener-bildung
tags:
  - Open Educational Resources (OER)
  - Metadaten
  - interoperabel
  - Vernetzung
  - dezentral
  - Qualitätskriterien
---



# Metadaten – die unsichtbare Infrastruktur offener Bildung


## 1. Metadaten – warum sollte mich das interessieren?

Wer selbst OER erstellt, kennt die entscheidende Frage, die sich nach der Veröffentlichung stellt: Wird meine Ressource überhaupt gefunden?

Diese Frage ist alles andere als hypothetisch, sondern stellt sich ganz praktisch, sobald ein Material online steht. OER-Erstellende investieren viel Zeit in gelungene Materialien und sorgen dafür, dass diese rechtssicher genutzt und geteilt werden können. All die Mühen sind jedoch vergebens, wenn das Material bei einer Suche gar nicht erst auftaucht.

Häufig liegt das Problem der fehlenden Auffindbarkeit von OER gar nicht an der inhaltlichen Qualität der Ressource, sondern an fehlenden oder unzureichenden Metadaten. 
Was zunächst trocken und technisch klingt, hat für OER eine kaum zu überschätzende Bedeutung: Metadaten bilden die Grundlage dafür, dass digitale Bildungsressourcen überhaupt gefunden und sinnvoll genutzt werden können. Sie machen ein Material für Suchmaschinen, OER-Repositorien und andere Informationssysteme maschinenlesbar, indem sie beschreiben, was das Material ist, für wen es gedacht ist und unter welchen Bedingungen es genutzt werden darf.


## 2. Was sind Metadaten überhaupt?

„Einfach ausgedrückt sind Metadaten Daten über Daten" (Krenn & Tiemann 2020, S. 4).  Metadaten funktionieren wie der Katalogeintrag einer Bibliothek: Sie beschreiben ein digitales Objekt, geben an, wo es zu finden ist, und ermöglichen dadurch seine Identifikation, Auffindbarkeit und Nachnutzung.

Nach Riley (2017) können mindestens drei Metadatentypen voneinander unterschieden werden:
- **deskriptive** Metadaten, die den Inhalt eines Materials beschreiben (Titel, Fach, Sprache),
- **strukturelle** Metadaten, die den inneren Aufbau und die Beziehungen zwischen digitalen Objekten abbilden, sowie 
- **administrative** Metadaten, die rechtliche, technische und provenienzbezogene Informationen, wie z.B. die Lizenz des Materials, festhalten.

Mit Blick auf OER heißt das, dass deskriptive Metadaten wie Titel und Fach beschreiben *was* das Material ist, die strukturellen Metadaten klären, *wie das Material aufgebaut ist* und *in welchem Verbund es steht* – etwa ob es aus mehreren Dateien besteht oder Teil einer größeren Unterrichtsreihe ist –, und die administrativen Metadaten regeln *wie das Material genutzt werden darf* und *in welchem Format* es vorliegt, durch den Vermerk auf Lizenzangabe und Dateiformat.

So verstanden wirken Metadaten wie ein reines Beschreibungswerkzeug. Tatsächlich stecken in ihrer Vergabe aber weitreichendere Entscheidungen, die nicht unbedingt selbsterklärend sind: Metadaten sind interpretationsbedürftige Artefakte, sog. „mehrfach gedeutete ‚Deuter‘" (Krenn & Tiemann, 2020, S. 12). Sie entstehen aus sozialen und technischen Aushandlungsprozessen und benötigen zu ihrer eigenen Interpretation oftmals wiederum Domänenwissen.

Wer bspw. ein Material mit dem Schlagwort „Grundschule" oder „Erstkommunionkatechese" versieht, trifft damit bereits eine kontextabhängige und institutionell geprägte Deutungsentscheidung. Welches Vorwissen, welche kirchliche Praxis, welches Altersverständnis hinter diesen Begriffen steht, prägt bereits die Vergabe der Metadaten.


## 3. Welchen Nutzen haben sorgfältig eingetragene Metadaten?

Beim Hochladen eines OER-Materials werden die Metadaten im Hintergrund von Suchmaschinen und OER-Portalen ausgelesen. Geben Suchende Schlagwörter oder Themen in eine Suchmaske ein, gleichen die Suchmaschinen diese Begriffe mit den hinterlegten Metadaten ab und liefern auf dieser Grundlage passgenaue Ergebnisse. Metadaten entscheiden deshalb maßgeblich darüber, ob ein Material beispielsweise bei einer Suche nach „Schöpfung", „Klasse 6" oder „CC BY" überhaupt in den Trefferlisten erscheint.

Erst diese zusätzlichen Informationen ermöglichen es, Materialien zu indexieren, nach bestimmten Kriterien zu filtern, miteinander zu verknüpfen und in Suchergebnissen gezielt anzuzeigen. Metadaten bilden damit die Schnittstelle zwischen einer veröffentlichten Ressource und den Personen, die nach ihr suchen.

Für OER-Erstellende bedeutet das, dass ein didaktisch hochwertiges, rechtssicher lizenziertes Arbeitsblatt seinen Nutzen nur dann entfaltet, wenn es auch gefunden werden kann. Fehlen aussagekräftige Angaben zu Titel, Fach, Zielgruppe, Sprache oder Lizenz, bleibt das Material für potenziell Nachnutzende häufig unsichtbar, selbst wenn es öffentlich zugänglich ist.

Sorgfältig gepflegte Metadaten erhöhen also die Wahrscheinlichkeit, dass Personen das Material bei einer thematischen Suche entdecken, die Eignung für die eigene Zielgruppe rasch einschätzen und es rechtssicher nachnutzen oder weiterentwickeln können.

Wer Metadaten sorgfältig erfasst, dokumentiert also nicht nur die Eigenschaften eines Materials, sondern macht es überhaupt erst sicht- und nutzbar. 
Metadaten sind damit eine bedeutsame Voraussetzung dafür, dass die Potenziale von OER, also Teilen, Nachnutzen und gemeinsames Weiterentwickeln von Materialien, in der Praxis tatsächlich wirksam werden.


## 4. Metadatenschemata und -profile im Überblick: LOM, Dublin Core und AMB

Für die Beschreibung digitaler Lernressourcen haben sich unterschiedliche Metadatenschemata und -profile etabliert. Sie verfolgen das gemeinsame Ziel, (Bildungs-)Ressourcen standardisiert zu beschreiben und dadurch deren Auffindbarkeit und Nachnutzung zu erleichtern.
Im Folgenden werden mit dem *IEEE Learning Object Metadata Standard (LOM)*, *Dublin Core (DC)* und dem *Allgemeinen Metadatenprofil für Bildungsressourcen (AMB)* drei für den OER-Kontext besonders relevante Ansätze vorgestellt. 

### IEEE Learning Object Metadata Standard (LOM) & Dublin Core (DC)
Einer der einflussreichsten Metadatenstandards für digitale Lernressourcen ist der *IEEE Learning Object Metadata Standard (LOM)*, der 2002 als internationaler Standard veröffentlicht wurde (vgl. Ochoa et al., 2011). 
Er dient der standardisierten Beschreibung digitaler Lernressourcen und bildet die Grundlage zahlreicher LOM-basierter Anwendungsprofile sowie vieler Bildungsrepositorien. Der einfacher strukturierte *Dublin Core (DC)* verfolgt demgegenüber einen generischeren Ansatz und wurde ursprünglich für die Beschreibung beliebiger digitaler Ressourcen entwickelt. Er definiert 15 grundlegende Metadatenelemente, legt jedoch nicht verbindlich fest, wie die zugehörigen Werte zu formatieren oder zu kontrollieren sind (vgl. Simão de Deus & Barbosa, 2020, S. 123 f.). Anders als LOM verzichtet Dublin Core auf eine hierarchische Kategorienstruktur, d.h. alle Elemente stehen gleichrangig nebeneinander und können unabhängig voneinander verwendet werden.

### Allgemeines Metadatenprofil für Bildungsressourcen (AMB)

Für den deutschsprachigen Kontext hat sich das *Allgemeine Metadatenprofil für Bildungsressourcen (AMB)* etabliert, das vom [Kompetenzzentrum Interoperable Metadaten (KIM) der DINI AG KIM](https://dini.de/standards) entwickelt wurde [(vgl. Pohl et al., 2023)](https://dini-ag-kim.github.io/amb/20231019/).
Anders als LOM oder Dublin Core handelt es sich hierbei nicht um ein eigenständiges Metadatenschema, sondern um ein Metadatenprofil. 
AMB legt fest, welche Elemente bestehender Webstandards verwendet werden, welche davon verpflichtend sind und wie Werte zu formatieren sind. Darüber hinaus integriert AMB kontrollierte Vokabulare, um eine möglichst einheitliche Beschreibung von Bildungsressourcen zu gewährleisten.

AMB basiert technisch auf [JSON-LD (JavaScript Object Notation for Linked Data)](https://json-ld.org). Dadurch können Informationen zu einer Lernressource, wie bspw. Titel, Fach, Zielgruppe oder Lizenz, direkt und maschinenlesbar in eine Webseite eingebunden werden. Dies erleichtert es Suchmaschinen und OER-Plattformen, die Materialien automatisiert zu erfassen und auffindbar zu machen.
AMB bildet unter anderem die Grundlage des Metadatenmodells [**Open Educational Resources Search Index (OERSI)**](https://oersi.org). 

Auch das im Aufbau befindliche Projekt **[Edufeed](https://comenius.de/2025/10/06/edufeed-dezentral-offen-interoperabel/)** – eine dezentrale, auf dem Nostr-Protokoll basierende OER-Infrastruktur des Comenius-Instituts – arbeitet mit AMB als Metadatenstandard zur plattformübergreifenden Abbildung von Bildungsmetadaten.
 
Um AMB genauer zu veranschaulichen, zeigt die folgende Tabelle die Metadaten dieses Blogartikels als Anwendungsfall.

| Felder | Funktion | Anwendungsfall |
|---|---|---|
| **name** | Titel der Ressource | Metadaten – die unsichtbare Infrastruktur offener Bildung|
| **description** | Kurzbeschreibung | Metadaten entscheiden maßgeblich darüber, ob Open Educational Resources gefunden, eingeordnet und nachgenutzt werden können. Dieser Beitrag erläutert, was Metadaten sind, wie die Standards LOM, Dublin Core und das Allgemeine Metadatenprofil für Bildungsressourcen (AMB) die Auffindbarkeit von OER strukturieren und warum selbst gepflegte Metadatensätze Lücken aufweisen, etwa bei der kompetenzbezogenen Erschließung. Da Metadaten keine neutralen, sondern soziotechnisch geprägte Angaben sind, plädiert der Beitrag zudem dafür, ihren Entstehungskontext sichtbar zu machen. Abschließend werden Konsequenzen für den Aufbau eines interoperablen, religionspädagogischen OER-Ökosystems skizziert.|
| **about** | Fach oder Thema |  https://w3id.org/kim/hochschulfaechersystematik/n053 </br>https://w3id.org/kim/hochschulfaechersystematik/n086 </br>https://w3id.org/kim/hochschulfaechersystematik/n052|
| **keywords** | Schlagwörter |  Open Educational Resources (OER), Metadaten, interoperabel, Vernetzung, dezentral, Qualitätskriterien|
| **creator** | Urheber:in | Laura Mößle </br> Phillip Angelina|
| **affiliation** | Institutionelle Zugehörigkeit | name: Johann Wolfgang Goethe-Universität Frankfurt id: https://ror.org/04cvxnb49 type: Organization </br> name: Friedrich-Alexander-Universität Erlangen-Nürnberg, id: https://ror.org/00f7hpc57, type: Organization|
| **learningResourceType** | Typ der Lernressource (z. B. Arbeitsblatt, Video, Kurs) | https://w3id.org/kim/hcrt/text, https://w3id.org/kim/hcrt/web_page|
| **audience** | Zielgruppe | https://w3id.org/kim/educationalLevel/level_A </br>https://w3id.org/kim/hcrt/web_page|
| **inLanguage** | Sprache | de|
| **license** | Lizenzangabe (maschinenlesbar referenziert) | https://creativecommons.org/licenses/by/4.0/deed.de|

Um die Erstellung von Metadaten zu erleichtern, bietet der [OERSI-Metadatengenerator](https://oersi.gitlab.io/metadata-form/metadata-generator.html) eine praktische Unterstützung.
Nutzer:innen werden schrittweise durch die Eingabe der relevanten Angaben geführt. 
Anschließend generiert das Tool daraus einen maschinenlesbaren Metadatensatz, der direkt kopiert und weiterverwendet werden kann.


## 5. Metadaten in der Praxis sind meist inkonsistent und kompetenzblind

Wie weit Anspruch und gelebte Praxis auseinanderfallen, zeigt eine Studie von Simão de Deus und Barbosa (2020): Von 280 identifizierten Metadatenschlüsseln in acht OER-Repositorien unterstützten die Suchfunktionen im Schnitt nur 78, also rund 28 % (Simão de Deus & Barbosa, 2020, S. 127, 129). Selbst Lizenzangaben, eigentlich das Kernversprechen der Rechtssicherheit, waren neben sauber vergebenen CC-Lizenzen (74 %) auch mit Werten wie „CustomLicense" oder schlicht „0" belegt (Simão de Deus & Barbosa, 2020, S. 130).

Ferner zeigen Fomin et al. (2026) auf, dass selbst wenn grundlegende Metadaten (Fach, Stufe, Lizenz) sauber in Materialien vergeben sind, eine strukturelle Lücke bei der fachlich-kompetenzbezogenen Erschließung offen bleibt. Die Studie identifiziert hierfür drei Ursachen:

1. Es existiert kein allgemein anerkannter Metadatenstandard zur Verschlagwortung von Kompetenzen
2. Die Verschlagwortung nach Kompetenzrahmen erfolgt manuell, uneinheitlich bzw. freiwillig
3. Bestehende LOM-Anpassungen unterscheiden sich je nach Region und politischem Kontext erheblich, was eine übergreifende Integration technisch wie politisch erschwert

Unlösbar ist das nicht. Die österreichische LOM-Anpassung der Universität Innsbruck nutzt das Feld `<classification>` bereits, um Materialien mit den UN-Nachhaltigkeitszielen zu verknüpfen. Die technische Infrastruktur für fachspezifische Taxonomien ist in LOM also angelegt, wird aber kaum gezielt genutzt.

An dieser Stelle setzen auch die FOERBICO-[Qualitätskriterien](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/src/branch/main/qualitaetskriterien/handreichung-qualitaetskriterien.md) an. 
Sie schlagen u.a. vor, die angestrebten Lernergebnisse und Kompetenzen zu Beginn des Materials klar auszuweisen und an Bildungsstandards bzw. Lehr- und Bildungsplänen auszurichten.


## 6. Was Metadaten nicht leisten können: Entstehungsbedingungen sichtbar machen

Braucht es also immer mehr und feinere Metadatenfelder? Krenn und Tiemann (2020) begegnen dieser Idee mit Skepsis. Metadaten sind keine objektiven Beschreibungen, sondern entstehen in spezifischen sozialen und technischen Kontexten.
Ohne Kenntnis dieser Entstehungsbedingungen bleibt ihre Aussagekraft „nur sehr eingeschränkt" (Krenn & Tiemann, 2020, S. 19). Damit sind mehr Metadaten nicht automatisch besser. 
Kategorien und Schlagwörter können für den Erstellenden zwar eindeutig erscheinen, werden aber unter Umständen von den Nachnutzenden unterschiedlich interpretiert.

Diese Einsicht deckt sich mit den Erkenntnissen aus der empirischen Begleitforschung des FOERBICO-Projekts. Standardisierte Metadaten erhöhen zwar die Sichtbarkeit von OER, können deren Entstehungskontext jedoch nur begrenzt abbilden. 
Für die Nachnutzung ist daher nicht allein relevant, was ein Material beschreibt, sondern auch warum, für wen und in welchem Kontext es entstanden ist.

Ergänzend zu standardisierten Metadaten können daher kontextbezogene Angaben sinnvoll sein. Dazu zählen bspw. Entstehungsort und -anlass, die didaktische Zielsetzung, die ursprünglich adressierte Lerngruppe oder der Rahmen, in dem das Material entwickelt wurde, wie z.B. auf einer Lehrer:innenfortbildung, in einem universitärer Seminar oder einer OER-Community Werkstatt. Solche Informationen unterstützen potenziell Nachnutzende dabei, die Eignung eines Materials für den eigenen Kontext einzuschätzen, und können damit wesentlich zur tatsächlichen Nachnutzung beitragen.


## 7. Konsequenzen für ein religionspädagogisches OER-Ökosystem

Aus den bisherigen Überlegungen lassen sich Handlungsperspektiven für den Aufbau eines religionspädagogischen OER-Ökosystems ableiten.

### Eine fachspezifische Metadatenlogik entwickeln

Bislang fehlt in der Theologie und Religionspädagogik eine einheitliche fachliche Systematik für die vergabe der Metadaten. Dazu gehören unter anderem auch einheitliche Bezeichnungen für die theologischen Fächergruppen, religionsdidaktische Modelle, überkonfessionelle sowie interreligiöse Vereinheitlichungen, Kompetenzformulierungen sowie religionspädagogische Themenfelder schulischer, außerschulischer und hochschulischer Bildung. 

Mit dem am Comenius-Institut angesiedelten Projekt **Edufeed** werden hierfür bereits wichtige Grundlagen geschaffen. Aufbauend auf AMB werden plattformübergreifende Metadatenstandards entwickelt und zugleich die im FOERBICO-Projekt erarbeiteten [**Qualitätskriterien**](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/src/branch/main/qualitaetskriterien/handreichung-qualitaetskriterien.md) berücksichtigt. Langfristig könnte daraus eine überfachliche Infrastruktur entstehen, die OER deutlich besser auffindbar und miteinander vernetzbar macht.

### Den Entstehungskontext sichtbar machen

Ebenso wichtig für die Metadaten ist die Dokumentation des Entstehungskontexts der Materialien. Religionspädagogische OER entstehen z.B. in Communitys of Practice oder in Rahmen von Lehrer:innenfortbildungen.
Diesen kollaborativen Entwicklungsprozess kann man in Metadaten, z.B. durch ein standardisiertes Metadatenfeld oder eine kurze redaktionelle Kontextbeschreibung sichtbar machen. Erweiterte Kontextangaben erleichtern potenziellen Nachnutzenden die Einschätzung der Zielsetzung und des Einsatzpotenzials für die eigene Lehrpraxis.



## Literatur

Angelina, P., Buchwald-Chassée, G., Gregorio Rodrigo, P., Mößle, L., & Ullmann, C. (2025). Open Educational Resources in der Religionspädagogik erstellen: Rechtliche, technische, pädagogisch-didaktische und religionspädagogische Qualitätskriterien. https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/src/branch/main/qualitaetskriterien/handreichung-qualitaetskriterien.md

Fomin, V. V., Kuzmuk, O., Mosakas, K., Raunig, M., Granitzer, M., & Dennerlein, S. (2026). *Metadata Gaps and Interoperability Failures in OER Retrieval: A Competence-Based Search Experiment.* Beitrag zur 30th EURAS Standardisation Conference, Graz, 24.–26. Juni 2026. https://www.researchgate.net/publication/405282300_Metadata_Gaps_and_Interoperability_Failures_in_OER_Retrieval_A_Competence-Based_Search_Experiment 

Krenn, K., & Tiemann, J. (2020). Metadaten im Kontext. Warum wir eine neue Datenkunde brauchen. In P. Klimczak, C. Petersen & S. Schilling (Hg.), *Maschinen der Kommunikation. Interdisziplinäre Perspektiven auf Technik und Gesellschaft im digitalen Zeitalter* (ars digitalis), Wiesbaden, S. 3-28. https://doi.org/10.1007/978-3-658-27852-6_1

Ochoa, X., Klerkx, J., Vandeputte, B., & Duval, E. (2011). On the use of learning object metadata: The globe experience. In C. D. Kloos, D. Gillet, R. M. Crespo García, F. Wild & M. Wolpers (Hg.), *Towards Ubiquitous Learning*, Berlin, Heidelberg, S. 271-284.

Pohl, A., Klinger, A., Hartmann, B., Schuurbiers, C., Steeg, F., Kummerländer, M., Oellers, M., Stengel, M., Hoffmann, M., Rörtgen, S., Kulla, S., & Bülte, T. (2023). *Allgemeines Metadatenprofil für Bildungsressourcen (AMB)* [Technische Spezifikation]. DINI AG KIM – Kompetenzzentrum Interoperable Metadaten. https://w3id.org/kim/amb/20231019/

Riley, J. (2017). *Understanding Metadata: What Is Metadata, and What Is It For?* Baltimore: National Information Standards Organization (NISO). 

Simão de Deus, W., & Barbosa, E. F. (2020). The Use of Metadata in Open Educational Resources Repositories: An Exploratory Study. In *2020 IEEE 44th Annual Computers, Software, and Applications Conference (COMPSAC)* IEEE, S. 123-132.https://doi.org/10.1109/COMPSAC48688.2020.00025

