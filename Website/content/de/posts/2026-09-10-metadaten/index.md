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

## 1. Was sind Metadaten überhaupt?

„Einfach ausgedrückt sind Metadaten Daten über Daten" (Krenn & Tiemann 2020, S. 4).  Metadaten beschreiben digitale Objekte und bilden die Voraussetzung für deren Identifikation, Auffindbarkeit und Nachnutzung. Vorschlag: Metadaten sind wie ein Personalausweis für digitale Objekte und ermöglichen ihre Identifikation, Auffindbarkeit und Nachnutzung. <!-- den Vorschlag finde ich gut. (FM) -->

Nach Riley (2017) können mindestens drei Metadatentypen voneinander unterschieden werden:
- **deskriptive** Metadaten, die den Inhalt eines Materials beschreiben (Titel, Fach, Sprache),
- **strukturelle** Metadaten, die den inneren Aufbau und die Beziehungen zwischen digitalen Objekten abbilden, sowie 
- **administrative** Metadaten, die rechtliche, technische und provenienzbezogene Informationen, wie z.B. die Lizenz des Materials, festhalten.

Mit Blick auf Open Educational Resources heißt das, dass deskriptive Metadaten wie Titel und Fach beschreiben *was* das Material ist, die strukturellen Metadaten klären, *wie das Material aufgebaut ist* und *in welchem Verbund es steht* – etwa ob es aus mehreren Dateien besteht oder Teil einer größeren Unterrichtsreihe ist –, und die administrativen Metadaten regeln *wie das Material genutzt werden darf* und *in welchem Format* es vorliegt – durch Lizenzangabe und Dateiformat. So gesehen wirken Metadaten zunächst wie neutrale Angaben, ähnlich einer universalen Sprache, die von allen verstanden wird.

Allerdings sind sie interpretationsbedürftige Artefakte. „Metadaten sind mehrfach gedeutete ‚Deuter'" (Krenn & Tiemann, 2020, S. 12). Sie entstehen aus sozialen und technischen Aushandlungsprozessen und benötigen zu ihrer eigenen Interpretation oftmals wiederum Domänenwissen. 
Wer bspw. ein Material mit dem Schlagwort „Grundschule" oder „Erstkommunionkatechese" versieht, trifft damit bereits eine kontextabhängige und institutionell geprägte Deutungsentscheidung. Welches Vorwissen, welche kirchliche Praxis, welches Alter hinter diesen Begriffen steht, prägt bereits die Auswahl und Vergabe der Metadaten.
> Kommentar: dieser Absatz kommt irgendwie aus dem nichts. Ich überlege mal nach einem guten Übergang von dem einen zum anderen Absatz. <!-- wäre mir jetzt beim Lesen gar nicht so krass vorgekommen. Denn nach der Erläuterung könnte man ja wirklich annehmen, es handelt sich um 'neutrale' Angaben, hab den einen Teil mal noch vorne hingestellt und ergänz. Vielleicht so besser? FM-->

## 2. Warum Metadaten wichtig sind

Metadaten bilden die Grundlage dafür, dass digitale Bildungsressourcen überhaupt gefunden und sinnvoll genutzt werden können. Sie machen ein Material für Suchmaschinen, OER-Repositorien und andere Informationssysteme maschinenlesbar, indem sie beschreiben, was das Material ist, für wen es gedacht ist und unter welchen Bedingungen es genutzt werden darf. 
Beim Eintragen eines OER-Materials werden die Metadaten im Hintergrund von Suchmaschinen und OER-Portalen ausgelesen. Sie entscheiden maßgeblich darüber, ob ein Material beispielsweise bei einer Suche nach „Schöpfung“, „Klasse 6“ oder „CC BY“ überhaupt in den Trefferlisten erscheint. 
Erst diese zusätzlichen Informationen ermöglichen es, Materialien zu indexieren, nach bestimmten Kriterien zu filtern, miteinander zu verknüpfen und in Suchergebnissen gezielt anzuzeigen. Metadaten bilden damit die Schnittstelle zwischen einer veröffentlichten Ressource und den Personen, die nach ihr suchen.

Für OER-Erstellende bedeutet das, dass ein didaktisch hochwertiges und rechtssicher lizenziertes Arbeitsblatt seinen Nutzen nur dann entfaltet, wenn es auch gefunden werden kann. Fehlen aussagekräftige Angaben zu Titel, Fach, Zielgruppe, Sprache oder Lizenz, bleibt das Material für potenzielle Nachnutzende häufig unsichtbar, selbst wenn es öffentlich zugänglich ist. 
Umgekehrt erhöhen sorgfältig gepflegte Metadaten die Wahrscheinlichkeit, dass Lehrende das Material bei einer thematischen Suche entdecken, seine Eignung für die eigene Zielgruppe einschätzen und es rechtssicher nachnutzen oder weiterentwickeln können.

Wer Metadaten sorgfältig erfasst, dokumentiert daher nicht nur die Eigenschaften eines Materials, sondern bringt es zur Entfaltung und erhöht zugleich dessen Sichtbarkeit und Wiederverwendbarkeit. Metadaten sind eine zentrale Voraussetzung dafür, dass die Potenziale von OER, also das Teilen, Nachnutzen und gemeinsame Weiterentwickeln, in der Praxis tatsächlich wirksam werden.


## 3. Metadatenschemata und -profile im Überblick: LOM, Dublin Core und AMB

Für die Beschreibung digitaler Lernressourcen haben sich unterschiedliche Metadatenschemata und -profile etabliert. Sie verfolgen das gemeinsame Ziel, Bildungsressourcen standardisiert zu beschreiben und dadurch deren Auffindbarkeit und Nachnutzung zu erleichtern.
Im Folgenden werden mit dem *IEEE Learning Object Metadata Standard (LOM)*, *Dublin Core (DC)* und dem *Allgemeinen Metadatenprofil für Bildungsressourcen (AMB)* drei für den OER-Kontext besonders relevante Ansätze vorgestellt.

### IEEE Learning Object Metadata (LOM)

Einer der einflussreichsten Metadatenstandards für digitale Lernressourcen ist der *IEEE Learning Object Metadata Standard (LOM)*, der 2002 als internationaler Standard veröffentlicht wurde (vgl. Ochoa et al., 2011). Er dient der standardisierten Beschreibung digitaler Lernressourcen und bildet die Grundlage zahlreicher LOM-basierter Anwendungsprofile sowie vieler Bildungsrepositorien. 
Hierzu gliedert LOM Metadaten in neun hierarchisierten Kategorien:

| Kategorie | Beschreibung |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **1. General** | Allgemeine Angaben zum Lernobjekt, z. B. Titel, Sprache, Beschreibung und Schlagwörter |
| **2. Lifecycle** | Informationen zur Entstehung und zum Lebenszyklus, z. B. Version, Status, Autor:innen und Veröffentlichungsdatum |
| **3. Meta-Metadata** | Angaben zum Metadatensatz selbst, etwa Ersteller:in, verwendetes Metadatenschema oder Zeitpunkt der Erfassung |
| **4. Technical** | Technische Eigenschaften, z. B. Dateiformat, Größe, technische Voraussetzungen und Speicherort bzw. URL |
| **5. Educational** | Pädagogisch-didaktische Merkmale, z. B. Lernressourcentyp, Zielgruppe, Interaktivität, Schwierigkeitsgrad und typische Lernzeit |
| **6. Rights** | Informationen zu Urheberrecht, Kosten sowie Lizenz- und Nutzungsbedingungen |
| **7. Relation** | Beziehungen zu anderen Lernressourcen, z. B. Bestandteil einer Sammlung oder Verweise auf verwandte Materialien |
| **8. Annotation** | Kommentare, Bewertungen oder Nutzungserfahrungen, die im Laufe der Verwendung ergänzt werden |
| **9. Classification** | Fachliche oder systematische Einordnung anhand von Klassifikationen oder Taxonomien |

<!--FM: Beim Lesen habe ich mich gefragt, was mache ich jetzt mit dieser Info; Heißt das, ich muss für alle Kategorien das irgendwo ausfüllen? bedeutet das einfach nur, dass es unterschiedliche Kategorien gibt? Das würde ich mir als Leser wünschen, hier noch etwas mehr Klarheit zu bekommen. Mich würde auch interessieren: Wie sieht das in der Praxis aus? Könnte man das z.B. an einem Beispiel durchspielen? -->

### Dublin Core Metadate Element Set (DCMES)

Der einfacher strukturierte *Dublin Core Metadata Element Set (DCMES)* verfolgt demgegenüber einen generischeren Ansatz und wurde ursprünglich für die Beschreibung beliebiger digitaler Ressourcen entwickelt.
Er definiert 15 grundlegende Metadatenelemente, legt jedoch nicht verbindlich fest, wie die zugehörigen Werte zu formatieren oder zu kontrollieren sind (vgl. Simão de Deus & Barbosa, 2020, S. 123 f.).
Anders als LOM verzichtet Dublin Core auf eine hierarchische Kategorienstruktur, d.h.alle Elemente stehen gleichrangig nebeneinander und können unabhängig voneinander verwendet werden.

| Schlüssel | Beschreibung |
|---|---|
| **Title** | Titel des Materials |
| **Creator** | Person oder Institution, die das Material erstellt hat |
| **Subject** | Fach oder Thema des Materials |
| **Description** | Kurze inhaltliche Beschreibung |
| **Publisher** | Veröffentlichende Person oder Institution |
| **Contributor** | Weitere Mitwirkende |
| **Date** | Erstellungs- oder Veröffentlichungsdatum |
| **Type** | Art der Ressource (z. B. Arbeitsblatt, Video, Kurs) |
| **Format** | Dateiformat oder technisches Erscheinungsbild |
| **Identifier** | Eindeutige Kennung (z. B. URL oder DOI) |
| **Source** | Ursprungsressource, aus der das Material hervorgegangen ist |
| **Language** | Sprache des Materials |
| **Relation** | Beziehung zu anderen Ressourcen |
| **Coverage** | Zeitlicher oder räumlicher Geltungsbereich |
| **Rights** | Angaben zu Lizenz und Nutzungsrechten |


### Allgemeines Metadatenprofil für Bildungsressourcen (AMB)

Für den deutschsprachigen Kontext hat sich das *Allgemeine Metadatenprofil für Bildungsressourcen (AMB)* etabliert, das vom [Kompetenzzentrum Interoperable Metadaten (KIM) der DINI AG KIM](https://dini.de/standards) entwickelt wurde [(vgl. Pohl et al., 2023)](https://dini-ag-kim.github.io/amb/20231019/).
Anders als LOM oder Dublin Core handelt es sich hierbei nicht um ein eigenständiges Metadatenschema, sondern um ein Metadatenprofil. AMB legt fest, welche Elemente bestehender Webstandards verwendet werden, welche davon verpflichtend sind und wie Werte zu formatieren sind. Darüber hinaus integriert AMB kontrollierte Vokabulare, um eine möglichst einheitliche Beschreibung von Bildungsressourcen zu gewährleisten.

Technisch basiert AMB auf JSON-LD und kann dadurch unmittelbar in Webseiten eingebettet werden. Dies erleichtert die maschinelle Verarbeitung von Metadaten durch Suchmaschinen und OER-Infrastrukturen.
AMB bildet unter anderem die Grundlage des Metadatenmodells des [**Open Educational Resources Search Index (OERSI)**](https://oersi.org). Auch das im Aufbau befindliche Projekt **[Edufeed](https://comenius.de/2025/10/06/edufeed-dezentral-offen-interoperabel/)** – eine dezentrale, auf dem Nostr-Protokoll basierende OER-Infrastruktur des Comenius-Instituts – arbeitet mit AMB als Metadatenstandard zur plattformübergreifenden Abbildung von Bildungsmetadaten.


| Beispielhafte Felder | Funktion |
|---|---|
| **name** | Titel der Ressource |
| **description** | Kurzbeschreibung |
| **about** | Fach oder Thema |
| **keywords** | Schlagwörter |
| **creator** | Urheber:in |
| **affiliation** | Institutionelle Zugehörigkeit |
| **learningResourceType** | Typ der Lernressource (z. B. Arbeitsblatt, Video, Kurs) |
| **audience** | Zielgruppe |
| **inLanguage** | Sprache |
| **license** | Lizenzangabe (maschinenlesbar referenziert) |
| **isPartOf / hasPart** | Beziehungen zwischen zusammenhängenden Ressourcen |

<!--Vielleicht könnte man ja z.B. die Metadaten dieses Beitrags hier offen legen und daran darstellen, wie so eine Auszeichnung mit Metadaten stattfinden und funktioniert, FM -->

## 4. Kompetenzen bislang wenig sichtbar

Wie weit Anspruch und gelebte Praxis dieser Standards auseinanderfallen können, zeigt eine breit angelegte Studie von Simão de Deus und Barbosa (2020): Von 280 identifizierten Metadatenschlüsseln in acht internationalen OER-Repositorien unterstützten die jeweiligen Suchfunktionen im Schnitt nur 78 – also rund 28 % (Simão de Deus & Barbosa, 2020, S. 127, 129). Selbst bei Lizenzangaben, dem Kernversprechen der Rechtssicherheit, fanden sich neben sauber vergebenen Creative-Commons-Lizenzen (74 %) auch Werte wie „CustomLicense" oder schlicht „0" (vgl. Simão de Deus & Barbosa, 2020, S. 130).

Ferner zeigen Fomin et al. (2026) auf, dass selbst wenn grundlegende Metadaten (Fach, Stufe, Lizenz) sauber in Materialien vergeben sind, eine strukturelle Lücke bei der fachlich-kompetenzbezogenen Erschließung offen bleibt. Die Studie identifiziert hierfür drei Ursachen:

1. Es existiert kein allgemein anerkannter Metadatenstandard zur Verschlagwortung von Kompetenzen
2. Die Verschlagwortung nach Kompetenzrahmen erfolgt manuell, uneinheitlich bzw. freiwillig
3. Bestehende LOM-Anpassungen unterscheiden sich je nach Region und politischem Kontext erheblich, was eine übergreifende Integration technisch wie politisch erschwert

Bemerkenswert ist, dass diese Lücke nicht grundsätzlich unlösbar ist. Die österreichische LOM-Anpassung der Universität Innsbruck nutzt das Feld `<classification>` bereits konkret, um Materialien mit den UN-Nachhaltigkeitszielen (SDGs) zu verknüpfen, mitsamt mehrsprachiger Klartext-Bezeichnung und stabiler URI (vgl. Fomin et al., 2026). <!-- Was ist eine URI? Ich glaube, es ist sinnvoll, das zu erklären - ich weiß auch nicht, was das ist -->
Die technische Infrastruktur für fachspezifische Taxonomien ist im LOM-Standard also bereits angelegt. Sie wird bislang jedoch kaum gezielt genutzt.


## 5. Was Metadaten nicht leisten können: Entstehungsbedingungen sichtbar machen

Reicht es also als Maßnahme, einfach immer mehr und immer feinere Metadatenfelder einzuführen? Krenn und Tiemann (2020) begegnen dieser Idee mit Skepsis. Aus ihrer Perspektive sind Metadaten keine objektiven oder neutralen Beschreibungen, sondern soziotechnische Artefakte, die immer in einem bestimmten Entstehungskontext erzeugt werden. Ohne Kenntnis dieses Kontexts bleibt ihre Aussagekraft „nur sehr eingeschränkt“ (Krenn & Tiemann, 2020, S. 19). Wer ein Material nachnutzt, verfügt häufig nicht mehr über das Hintergrundwissen der Person, die es erstellt und verschlagwortet hat. Kategorien oder Schlagwörter erscheinen dann zwar eindeutig, können aber unterschiedlich interpretiert werden. Standardisierte Metadaten schaffen deshalb zwar mehr Vergleichbarkeit, sie können den Entstehungskontext eines Materials jedoch nicht vollständig abbilden.

Als Ergänzung zu standardisierten Metadatenschemata schlagen die Autor:innen unter Rückgriff auf Bick und Müller (1984) den sozialwissenschaftlichen Ansatz der Datenkunde vor.
Ziel dieses Ansatzes ist es, Daten nicht isoliert zu betrachten, sondern ihre Entstehungsbedingungen mitzudenken. Vereinfacht lassen sich dabei drei Perspektiven unterscheiden, die die Vergabe von Metadaten prägen:

- **Institutionelle Logik:** die Rahmenbedingungen und Zielsetzungen der Organisation, in der ein Material entsteht.
- **Logik der Ersteller:innen:** die Entscheidungen, Routinen und Annahmen der Personen, die ein Material erstellen und verschlagworten.
- **Logik der Nutzenden:** die Erwartungen, Suchstrategien und Bedarfe der Personen, die das Material später finden und verwenden möchten.


Z.B. liefern die Schlagworte „Religion“, „Sekundarstufe I“ und „CC BY“ wichtige Informationen über Materialien, beantworten aber noch nicht die Frage, warum ein Material entstanden ist und für welchen Einsatzkontext es entwickelt wurde. Aussagekräftiger wird ein Material, wenn zusätzlich festgehalten wird, ob es beispielsweise im Rahmen einer Lehrer:innenfortbildung, eines universitären Seminars oder einer communitybasierten OER-Werkstatt entstanden ist, welche didaktische Zielsetzung das Material verfolgt und für welche Lerngruppe es ursprünglich konzipiert wurde.
Solche Kontextinformationen helfen potenziellen Nachnutzenden, die Eignung eines Materials besser einzuschätzen und entscheiden oft darüber, ob eine Ressource als passend wahrgenommen und tatsächlich weiterverwendet wird.


## 6. Konsequenzen für ein religionspädagogisches OER-Ökosystem

Aus den bisherigen Überlegungen lassen sich Handlungsperspektiven für den Aufbau eines religionspädagogischen OER-Ökosystems ableiten.

### Eine fachspezifische Metadatenlogik entwickeln

Bislang fehlt in der Theologie und Religionspädagogik eine einheitliche fachliche Systematik für die vergabe der Metadaten. Dazu gehören unter anderem auch einheitliche Bezeichnungen für die theologischen Fächergruppen, religionsdidaktische Modelle, überkonfessionelle sowie interreligiöse Vereinheitlichungen, Kompetenzformulierungen sowie religionspädagogische Themenfelder schulischer, außerschulischer und hochschulischer Bildung. 

Mit dem am Comenius-Institut angesiedelten Projekt **Edufeed** werden hierfür bereits wichtige Grundlagen geschaffen. Aufbauend auf dem Allgemeinen Metadatenprofil für Bildungsressourcen (AMB) werden plattformübergreifende Metadatenstandards entwickelt und zugleich die im FOERBICO-Projekt erarbeiteten [**Qualitätskriterien**](https://oer.community/offenheit-ist-kein-gegensatz-zu-qualität/) berücksichtigt. Langfristig könnte daraus eine überfachliche Infrastruktur entstehen, die OER deutlich besser auffindbar und miteinander vernetzbar macht.

### Den Entstehungskontext sichtbar machen

Metadaten sollten sich nicht auf die Beschreibung formaler Eigenschaften eines Materials beschränken. Ebenso wichtig ist die Dokumentation seines Entstehungskontexts. Religionspädagogische OER entstehen z.B. in Communitys of Practice oder in Rahmen von Lehrer:innenfortbildungen.
Diesen kollaborativen Entwicklungsprozess kann man in Metadaten, z.B. durch ein standardisiertes Metadatenfeld oder eine kurze redaktionelle Kontextbeschreibung sichtbar machen. Erweiterte Kontextangaben erleichtern potenziellen Nachnutzenden die Einschätzung der Zielsetzung und des Einsatzpotenzials für die eigene Lehrpraxis.

### Metadaten als Instrument didaktischer Reflexion

Metadaten können über die reine Beschreibung von Materialien hinaus auch didaktische Entscheidungen dokumentieren. Wer digitale Lehr-Lernmaterialien veröffentlicht, legt beispielsweise fest, welche Lernziele verfolgt werden, welche Zielgruppen angesprochen sind oder auf welchen religionsdidaktischen Überlegungen das Material basiert. Werden solche Informationen als Metadaten erfasst, erleichtern sie nicht nur das Auffinden, sondern auch die Einordnung und Nachnutzung eines Materials.

Gerade in der Religionspädagogik mit ihren unterschiedlichen didaktischen Zugängen können entsprechende Metadaten dazu beitragen, die didaktische Ausrichtung eines Materials transparent zu machen. 

## Literatur

Bick, W., & Müller, P. J. (1984). Sozialwissenschaftliche Datenkunde für prozeßproduzierte Daten: Entstehungsbedingungen und Indikatorenqualität. In W. Bick, R. Mann & P. J. Müller (Hg.), *Sozialforschung und Verwaltungsdaten*, Stuttgart, S. 123–159.

Fomin, V. V., Kuzmuk, O., Mosakas, K., Raunig, M., Granitzer, M., & Dennerlein, S. (2026). *Metadata Gaps and Interoperability Failures in OER Retrieval: A Competence-Based Search Experiment.* Beitrag zur 30th EURAS Standardisation Conference, Graz, 24.–26. Juni 2026. https://www.researchgate.net/publication/405282300_Metadata_Gaps_and_Interoperability_Failures_in_OER_Retrieval_A_Competence-Based_Search_Experiment 

Krenn, K., & Tiemann, J. (2020). Metadaten im Kontext. Warum wir eine neue Datenkunde brauchen. In P. Klimczak, C. Petersen & S. Schilling (Hg.), *Maschinen der Kommunikation. Interdisziplinäre Perspektiven auf Technik und Gesellschaft im digitalen Zeitalter* (ars digitalis), Wiesbaden, S. 3-28. https://doi.org/10.1007/978-3-658-27852-6_1

Ochoa, X., Klerkx, J., Vandeputte, B., & Duval, E. (2011). On the use of learning object metadata: The globe experience. In C. D. Kloos, D. Gillet, R. M. Crespo García, F. Wild & M. Wolpers (Hg.), *Towards Ubiquitous Learning*, Berlin, Heidelberg, S. 271-284.

Pohl, A., Klinger, A., Hartmann, B., Schuurbiers, C., Steeg, F., Kummerländer, M., Oellers, M., Stengel, M., Hoffmann, M., Rörtgen, S., Kulla, S., & Bülte, T. (2023). *Allgemeines Metadatenprofil für Bildungsressourcen (AMB)* [Technische Spezifikation]. DINI AG KIM – Kompetenzzentrum Interoperable Metadaten. https://w3id.org/kim/amb/20231019/

Riley, J. (2017). *Understanding Metadata: What Is Metadata, and What Is It For?* Baltimore: National Information Standards Organization (NISO). 

Simão de Deus, W., & Barbosa, E. F. (2020). The Use of Metadata in Open Educational Resources Repositories: An Exploratory Study. In *2020 IEEE 44th Annual Computers, Software, and Applications Conference (COMPSAC)* IEEE, S. 123-132.https://doi.org/10.1109/COMPSAC48688.2020.00025

