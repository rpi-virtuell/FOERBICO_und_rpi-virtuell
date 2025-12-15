---
'@context': https://schema.org/
creativeWorkStatus: Draft
type: LearningResource
name: KI-Heilsbringer oder Zerstörer für OER
description: Dieser Artikel berichtet von unserer Teilnahme an der Veranstaltung „OER im
  Zeitalter von KI - jetzt erst recht oder Auslaufmodell?“. Die Veranstaltung
  fand Anfang November statt und gab viele wichtige Impulse zu der Thematik KI
  und OER.
license: https://creativecommons.org/licenses/by/4.0/deed.de
creator:
  - givenName: Phillip
    familyName: Angelina
    id: https://orcid.org/0000-0002-6905-5523
    type: Person
    affiliation:
      name: Friedrich-Alexander-Universität Erlangen-Nürnberg
      id: https://ror.org/00f7hpc57
      type: Organization
  - givenName: Jörg
    familyName: Lohrer
    id: https://orcid.org/0000-0002-9282-0406
    type: Person
    affiliation:
      name: Comenius-Institut
      id: https://ror.org/025e8aw85
      type: Organization
keywords:
  - OER
  - OEP
  - KI
inLanguage:
  - de
about:
  - https://w3id.org/kim/hochschulfaechersystematik/n02
  - https://w3id.org/kim/hochschulfaechersystematik/n03
learningResourceType:
  - https://w3id.org/kim/hcrt/web_page
educationalLevel:
  - https://w3id.org/kim/educationalLevel/level_A
datePublished: '2025-12-12'
#staticSiteGenerator:
author:
  - Phillip Angelina
  - Jörg Lohrer
title: KI-Heilsbringer oder Zerstörer für OER?
cover:
  relative: true
  hiddenInSingle: true
  image: oer-und-ki.jpg
summary: |
  Ein Informationspost über die Teilnahme an der Tagung „OER im Zeitalter von KI - jetzt erst recht oder Auslaufmodell?“.
url: ki-heilsbringer-zerstoerer
tags:
  - OER
  - OEP
  - KI
---

Unter dem Titel „OER im Zeitalter von KI - jetzt erst recht oder Auslaufmodell?“ veranstalteten das Multimedia Kontor Hamburg ([MMKH](https://www.mmkh.de)), das niedersächsische OER-Portal [twillo](https://www.twillo.de/) in Partnerschaft mit [HIS-HE](https://his-he.de/), [KNOER](https://kn-oer.de/) und der Hamburg Open Online University ([HOOU](https://portal.hoou.de/)) am 6. November 2025 eine [Online-Fachtagung](https://www.mmkh.de/digitale-lehre/oer-und-knoer/oer-im-zeitalter-von-ki) zur Rolle von Künstlicher Intelligenz (KI) für offene Bildungsressourcen.

Die Veranstaltungsankündigung fasst den Ausgangspunkt prägnant zusammen:

> Die Entwicklungen der letzten zweieinhalb Jahre zeigen ganz deutlich, dass Künstliche Intelligenz (KI) alle Hochschulbereiche tangiert und signifikant verändern wird. Dies betrifft vor allem auch den Bereich der Hochschullehre und damit die Produktion von Lehr- und Lernmaterialien. Seitdem es mit wenigen Prompts möglich ist, Lehr- und Lernmaterialien quasi per Knopfdruck zu erstellen und da diese Inhalte dann auch als gemeinfreie Werke gelten - sofern nicht durch kreative Promptketten und eigenständige Nachbearbeitungen eine Schaffenshöhe erreicht wird, die ein individuelles Urheberrecht begründen -, ergeben sich Fragestellungen nach den Auswirkungen dieser Entwicklungen auf Open Educational Resources (OER).

Welche potentiellen Auswirkungen KI auf OER hat, wurde im Rahmen des Fachtags aus unterschiedlichen wissenschaftlichen und praktischen Perspektiven beleuchtet. Im Zentrum stand dabei weniger die Suche nach einer einfachen Antwort, sondern eine vielschichtige Auseinandersetzung mit Chancen, Spannungsfeldern und offenen Fragen rund um Offenheit, Qualität und Verantwortung in der Hochschulbildung.

## Einblick in die Tagung

### Empirische Perspektive auf OER- und KI-Nutzung
Funda Seyfeli-Özhizalan (HIS-HE) präsentierte erste empirische Ergebnisse zu Einsatzfeldern von KI-Anwendungen bei Erstellung und Verbreitung von OER (Veröffentlichung bei twillo, angekündigt für Ende 2025). Die Studie folgt einem Mixed-Methods-Ansatz (quantitative Befragung, vertiefende Interviews, Expert:inneninterviews) und zeigt:
- KI wird vor allem unterstützend eingesetzt (z.B. für Textoptimierung, Strukturierung, Bildgenerierung), weniger zur vollständigen Generierung von Materialien.
- KI wird in der Erstellung und Anpassung von OER als potentiell entlastendes Werkzeug wahrgenommen.
- Gleichzeitig bestehen erhebliche rechtliche Unsicherheiten (AGB-Änderungen, Unklarheiten bzgl. Trainingsdaten, Lizenzierung) sowie Sorgen hinsichtlich Qualitätsverlusten.
- Hemmnisse für OER und KI umfassen u.a. fehlende Sicherheit im Umgang mit Lizenzen, Unsicherheit über die Rolle der eigenen didaktischen Expertise und ein „übermäßiges Vertrauen“ in KI-Systeme.

In der Diskussion wurde deutlich, dass sich viele Lehrende zwischen Entlastung und Verunsicherung bewegen: KI eröffnet pragmatische Unterstützungsmöglichkeiten, verstärkt zugleich aber das Bewusstsein für rechtliche Graubereiche und die Notwendigkeit, die eigene didaktische Expertise nicht an automatisierte Systeme zu delegieren.

### KI-generierte Metadaten und OERSI
Im ersten Lightning Talk zeigte Axel Klinger (TIB Hannover), wie KI bei der Generierung von Metadaten für das OER-Suchportal [OERSI](https://oersi.org/) eingesetzt werden kann. Ein erheblicher Teil der indexierten Materialien weist unvollständige oder fehlende Metadaten auf; dies erschwert Auffindbarkeit, Nachnutzbarkeit und inhaltliche Einordnung. Genannt wurden u.a. zehntausende Materialien ohne Beschreibung, fehlende Fachzuordnungen sowie uneinheitliche Sprachangaben.

Als Antwort darauf wird eine modulare Pipeline erprobt, die auf Open-Source-Sprachmodellen basiert. Nach einem Modellvergleich (u.a. Qwen und Phi) fiel die Wahl auf Qwen 2.5 im lokalen Betrieb mit großem Kontextfenster. Fokussiert werden vorerst:
- Open Textbooks und Videos (über Transkripte),
- Materialien mit fehlenden Beschreibungen,
- testweise vor allem offen lizenzierte Inhalte (z.B. CC BY).

Aus den Volltexten werden automatisiert erzeugt:
- Zusammenfassungen für Detailseiten (ähnlich Abstracts),
- prägnante Kurzbeschreibungen für Trefferlisten,
- Vorschläge für Titel, Schlagworte und Fachzuordnungen.

Die transkribierten Inhalte werden bei Bedarf in Abschnitte zerlegt, um Kontextfenstergrenzen einzuhalten; anschließend werden Teilsummaries wieder zu Gesamtsummaries zusammengeführt. Erste Testläufe mit einer begrenzten Menge von Materialien zeigen grundsätzlich brauchbare Zusammenfassungen und Kurzbeschreibungen, zugleich aber typische Probleme:
- fehlerhafte Eigennamen und Fachbegriffe,
- Kontextverschiebungen bei stark segmentierten Texten,
- unzureichend präzise Fachzuordnungen, insbesondere auf feineren Ebenen.

Der Ansatz unterstreicht zwei zentrale Punkte: Zum einen kann KI helfen, OER-Systeme wie OERSI sichtbarer und besser nutzbar zu machen; zum anderen bleibt eine qualifizierte, menschliche Qualitätssicherung unverzichtbar - etwa durch Metadatenvorschläge, die Autor:innen beim Upload prüfen und korrigieren können. Die zugrundeliegenden Prompts und Konfigurationen werden offen bereitgestellt (vgl. <https://gitlab.com/oersi/sidre/metadata-optimization>) und sind damit selbst Teil einer offenen Infrastruktur für OER-Metadaten.

### OER als Grundlage für einen KI-Chatbot (iMooX)
Im zweiten Lightning Talk präsentierte PD Dr. Martin Ebner (TU Graz) den Einsatz eines KI-gestützten Chatbots auf Basis von OER-Materialien der nationalen MOOC-Plattform iMooX.

Ausgangspunkt ist der [Kurs „Informatik-Fit“](https://imoox.at/course/InfoFit25), der Studieninteressierte bereits vor Studienbeginn beim Aufbau grundlegender Informatikkompetenzen unterstützt. Der Kurs ist offen lizenziert, wird in ein Blended-/Flipped-Classroom-Szenario eingebettet und umfasst u.a. Videos, Transkripte, Kursunterlagen und Webinhalte.

Auf dieser Basis wurde ein Retrieval-Augmented-Generation-System (RAG) implementiert. Ein RAG ist nach Zhao et. Al:
> In particular, RAG introduces the information retrieval process, which enhances the generation process by retrieving relevant objects
from available data stores, leading to higher accuracy and better robustness ([Zhao et. Al 2024: 1](https://doi.org/10.48550/arXiv.2402.19473)).

Ein RAG verbessert Antwortgenerierung der KI. Denn das RAG identifiziert anhand der Eingabefrage relevante Datenquellen und interagiert mit dem Generator, um robuste und genaue Antworten zu generieren. Es ist wie ein Datenspürhund, welches aus einem Datenset die relevanten Informationen herausholt. Für den Kurs „Informatik-Fit“ bedeutet das konkret:
- Sämtliche OER-Kursmaterialien werden in einer Vektordatenbank abgelegt und bilden den primären Antwortkontext.
- Lernende können nach aktiver Zustimmung einen Chatbot nutzen, der Fragen zum Kurs stellt und Antworten auf Grundlage dieser OER-Inhalte generiert.
- Als zugrundeliegendes Sprachmodell kommt (Stand der Präsentation) ein kommerzielles LLM (ChatGPT 4.0 mini) zum Einsatz, das nach Tests eine hohe Antwortqualität (Validität von über 97 % in Stichproben) zeigte.

Die begleitende Evaluation zeigt u.a.:
- Der Chatbot wird vor allem für Verständnisfragen, Zusammenfassungen und Prüfungsvorbereitung genutzt.
- Ein Teil der Lernenden verzichtet bewusst auf den Chatbot; teils, weil sie ihn nicht benötigen, teils aus Unsicherheit oder fehlender Routine im Umgang mit KI.
- Auffällig ist eine Tendenz zur technologischen Überschätzung bei Nicht-Nutzenden, die dem System teils mehr zutrauen als diejenigen, die es erprobt haben.

Für die OER-Perspektive sind zwei Aspekte zentral:
Die ausschließliche Nutzung offen lizenzierter Kursmaterialien als Wissensbasis ermöglicht einen rechtlich transparenten Einsatz des Chatbots. Gleichzeitig bleibt ein Spannungsfeld, solange das zugrundeliegende LLM proprietär und dessen Trainingsdaten intransparent sind. Als mögliche Perspektive werden offene und europäisch betriebene Sprachmodelle genannt (z.B. Academic Cloud, Apertus), die langfristig zu mehr digitaler Souveränität beitragen könnten.

Das Beispiel iMooX zeigt damit konkret, wie OER die Grundlage für KI-gestützte, lernendennahe Unterstützungssysteme bilden können - unter der Bedingung, dass Qualitätssicherung, Transparenz und reflektierter Einsatz mitgedacht werden.

### Vom Lehrbuch zum Kurzvideo mit KI-Unterstützung
Im dritten Lightning Talk stellte Prof. Dr. Martin Erdmann (RWTH Aachen) ein Projekt vor, in dem ein Lehrbuch mit Unterstützung von KI in kurze Lehrvideos für die Hochschullehre transformiert wurde.

Wesentliche Beobachtungen:
- Die Videos wurden von einem signifikanten Teil der Studierenden genutzt, insbesondere zur Vor- und Nachbereitung.
- Die Videos ergänzen Lehrbuch und Lehrveranstaltung, ersetzen diese jedoch nicht.
- KI-Werkzeuge kamen u.a. bei der sprachlichen Anpassung (Schriftsprache zu gesprochener Sprache) zum Einsatz, die inhaltliche Strukturierung, Schwerpunktsetzung sowie didaktische Entscheidungen blieben klar in menschlicher Verantwortung.
- Das Projekt unterstreicht, dass Bildung ein sozialer, relationaler Prozess bleibt: KI kann hier unterstützen, nicht substituieren.

Das Bildung ein sozialer Prozess ist, zeigte sich nach Prof. Dr. Erdmann deutlich anhand des gemeinsamen Schauens der Videos vor den einzelnen Sitzungen. Ein signifikanter Teil der Studierenden kamen 15 Minuten vor der Vorlesung, um gemeinsam die Videos zu sehen. Das Projekt zeigt aber auch, welche Kosten bei der Nutzung von KI verbunden sein können. Denn für die KI Software, welche für die Video-Generierung verwendet wurde, mussten neben der Arbeitszeit auch finanzielle Ressourcen aufgebracht werden.

### Zwiegespräch: Zuspitzung der Leitfrage

Im abschließenden Zwiegespräch zwischen Dr. Sandra Schön (TU Graz) und PD Dr. Malte Persike (RWTH Aachen), moderiert von Dr. Klaus Wannemacher (HIS-HE/twillo), wurden die Eindrücke der Vorträge zusammengeführt und in eine grundsätzliche Debatte über den Stellenwert von KI und OER überführt.

Zentrale Akzente aus dem Gespräch waren:
- KI-generierte Lehrmaterialien sind aktuell nicht hinreichend verlässlich, um ohne menschliche Qualitätssicherung eingesetzt zu werden. Die Beiträge von Axel Klinger, Martin Ebner und Martin Erdmann verdeutlichen vielmehr, wie arbeitsintensiv es bleibt, gute Bildungsressourcen zu erstellen - auch mit KI.
- KI sollte daher primär als Werkzeug verstanden werden, das OER-Produktion und -Nutzung unterstützt, nicht als Ersatz für pädagogische Expertise. Die Verantwortung von Lehrenden verschiebt sich eher hin zu Kuratierung, Prüfung und reflektierter Gestaltung.
- OER besitzen im Unterschied zu vielen KI-Systemen eine klare gemeinwohlorientierte und rechtlich transparente Grundlage. Für rechtssichere KI-Szenarien werden offene, nachnutzbare Materialien und transparente Trainingsdaten zunehmend zur Voraussetzung.
- Gleichzeitig wird betont, dass KI nicht alle positiven Effekte von OER teilt: Kommerzielle Modelle und intransparente Datenpraktiken bergen Risiken für digitale Souveränität, Teilhabe und Urheberrecht. Die „Euphorie“ über KI sollte deshalb kritisch gebrochen werden.
- Offen bleibt die Frage, wie weit Qualitätsprozesse automatisiert werden können, ohne die Verantwortung an „Agentensysteme“ abzugeben, deren Entscheidungen selbst kaum überprüfbar sind.

Kritisch rückblickend formuliert Malte Persike eine gewisse „OER-Desillusionierung“: OER und OEP sollten an Hochschulen Selbstverständlichkeit sein, tatsächlich fehlen aber häufig verlässliche Daten zu Nutzung, Wirkung und Nachnutzung. Zugleich wird darauf hingewiesen, dass Lernende KI bereits breit für individuelles Lernen einsetzen - oft weit sichtbarer als institutionelle OER-Angebote. Hier entsteht ein Spannungsfeld zwischen gelebter Praxis, offenen Bildungsansprüchen und noch offenen Forschungsfragen.

## Fazit: OER im Zeitalter von KI - jetzt erst recht

Zusammenfassend lässt sich aus den Beiträgen des Fachtags festhalten:
OER und KI können sich gegenseitig unterstützen und voranbringen. KI kann zur Unterstützung der OER-Produktion beitragen, etwa bei Qualitätssicherung, Sprachüberarbeitung, Übersetzungen, Metadatenanreicherung und der didaktischen Aufbereitung von Materialien.OER bieten gleichzeitig eine zentrale Grundlage, um KI-Anwendungen für Bildung rechtskonform, transparent und gemeinwohlorientiert zu gestalten. Es bleiben jedoch offene Fragen insbesondere in Bezug auf Urheberrecht, Lizenzierung von KI-gestützten Materialien, Transparenz von Trainingsdaten sowie nachhaltige Infrastrukturen für offene Bildung.
Ohne menschliche Verantwortung, kritische Reflexion und Community-getragene Qualitätsprozesse kann weder KI noch OER ihr Potenzial für eine offene, souveräne Bildungslandschaft entfalten.

## Eigene Learnings

Für unsere Arbeit - insbesondere im Kontext von OER-Communities und Initiativen wie FOERBICO - war der Fachtag eine Gelegenheit, Einblicke in laufende Forschungs- und Praxisprojekte zu gewinnen und diese mit eigenen Erfahrungen zu verschränken. Er bestätigt mehrere zentrale Einsichten:
- KI ist kein Allheilmittel, sondern ein Werkzeug, das bewusst, reflektiert und ressourcensensibel eingesetzt werden muss.
- Offen lizenzierte Bildung ist nicht kostenfrei in der Erstellung: Zeit, Expertise und Infrastruktur bleiben entscheidend - auch dann, wenn KI einzelne Arbeitsschritte erleichtert.
- Fragen der digitalen Souveränität, der gerechten Zugänglichkeit von KI-Werkzeugen und der Rolle offener Infrastrukturen (inklusive Vektordatenbanken und RAG-Systemen auf OER-Basis) werden für die zukünftige OER-Landschaft zentral sein.
- Die Weiterentwicklung von OER kann nur gemeinsam mit aktiven Communities, offenen Werkzeugen und einer klaren bildungspolitischen und institutionellen Unterstützung gelingen.

Vor diesem Hintergrund erscheint die Leitfrage „Heilsbringer oder Zerstörer?“ verkürzt. Im Lichte der Tagungsbeiträge wird deutlich: KI entscheidet nicht über die Zukunft von OER - vielmehr entscheidet die Art, wie Bildungsakteur:innen Offenheit, Verantwortung und technologische Gestaltungsspielräume zusammenführen.

## Materialien und weiterführende Links

- Ausschreibung und Dokumentation des Fachtags „OER im Zeitalter von KI - jetzt erst recht oder Auslaufmodell?“: https://www.mmkh.de/digitale-lehre/oer-und-knoer/oer-im-zeitalter-von-ki
- Multimedia Kontor Hamburg (MMKH): https://www.mmkh.de
- OER-Portal twillo: https://www.twillo.de
- HIS-HE: https://his-he.de
- KNOER - Kompetenznetzwerk OER: https://kn-oer.de
- Hamburg Open Online University (HOOU): https://portal.hoou.de
- OERSI - Open Educational Resources Search Index: https://oersi.org
- OERSI-Metadatenoptimierung (Prompts/Beispiele): https://gitlab.com/oersi/sidre/metadata-optimization
- iMooX-Kurs „Info-Fit“: https://imoox.at/course/InfoFit25
- Publikation zum iMooX-Chatbot-Einsatz (Hinweis aus den Tagungsnotizen): https://link.springer.com/chapter/10.1007/978-3-031-93567-1_4
- Vortragsfolien „Vom Lehrbuch zum Kino: Erfahrungen mit KI-gestützten Kurzvideos in der Hochschullehre“ (Prof. Dr. Erdmann): https://www.mmkh.de/fileadmin/veranstaltungen/OER-KI/2025-11-06_KI-Lehrbuch-Videos_Erdmann.pdf
- Deskilling-Diskurs (Hinweis aus der Diskussion): https://hochschulforumdigitalisierung.de/wp-content/uploads/2023/10/HFD_DP_25_Deskilling.pdf
- Initiative für europäische Sprachmodelle (Hinweis aus den Materialien): https://hessian.ai/de/occiglot-neue-initiative-fuer-europaeische-sprachmodelle-gestartet/
