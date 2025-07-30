# OER Remixen

## WLO und OERSI
Das Edusharingsystem durch das verlinken von Drittanbietern, versträrkt die frustration, da nicht direkt mit der Lernressource gearbeitet werden kann, sondern ein Plattformhopping entsteht.

```mermaid
graph LR
A[Material Suche]--Weiterleitung auf <br/>verschiedene Websiten--> B((Material ist nicht <br/>lizenzrechtlich <br/>ausgewiesen)) -->D(Ausweisung nur auf der Website<br/>Nicht auf dem Material)-->E{Frustration}
B --> C(Wir werden von Website zu Website geleitet)
C --> E
```

## RPI Materialpool
Ergebnisse können mit den **großen Playern* mithalten, die Materialreferenzsammlung führt den Suchenenden direkt zum Material, daraus ergibt sich weniger Plattform Hopping.
```mermaid
graph LR
A[Material Suche] -- OER Filter<br/>hat gefehlt --> B((Material ist nicht <br/>lizenzrechtlich <br/>ausgewiesen)) -->D(Ausweisung nur auf der Website<br/>Nicht auf dem Material)-->E{Frustration}
B --> C(Wir werden von <br/>Website zu Website geleitet)
C --> E
```

## OER-Communities
### reliLab
Nach der **ständigen Frustration** sind wir direkt zu einer Community gegangen, reliLab.org, und haben Ethik in die Suchmaske eingegeben und sind beim Berufsschuleintrag gelandet und sind sofort an ein Wissensbaustein gelandet.
```mermaid
graph LR
A{Frustration}-->G(Suche über relilab) -- Suchmaske<br/>ohne Filter<br/>Ethik eingegeben --> B((Ergebnisse <br/>in der ersten <br/>Suchreihe)) -->D(Wissensbaustein<br/>Fortbildung + <br/>Powerpoint)-->E(Erste Schritte zum<br/>Erstellen / Remixen)
D --> C(Es fehlt an Didaktischen <br/> Konzept und Umsetzung)
D --> F(Es ist noch kein <br/>fertiges Material)
```
Kleinere Datenbank und fachspezifische Ausrichtung führen zu einer schnelleren Orientierung und Findung von Material.

### Religglobal
Bei reliGlobal hat bei sich einen writer zur *Unterrichtsheinheiten* der auf eine Seite mit verschiedenen Entwürfen über die man zum Material gelangt.
Es fehlen Schlagworte auf der Übersichtsseite, nur weil wir Materialien bereits kennen, war eine Zuordung möglich. 
Jedes Material hat seine eigene Unterlizensierung.

```mermaid
graph LR
A((reliGlobal))-->B(Lizensierung auf der Materialseite<br/>nicht klar ersichtlich)
A --> C(Schlagworte waren im Unterrichtsentwurf)
A --> D(Didaktischer Kommentar<br/>Auffindbar unter Didaktik)
A --> E(Materialdownload eigener<br/>righter)
```

### reliMentar
Bei reliMentar in die Suche wurde Ethik eingegeben. Die Ergebnisseite, führte sofort zu Materialvorschlägen, mit bereits ersichtlicher Lizensierung. Wir sind auf Material zwei, Was der Baum des Zachhäus erzählt. Rechts der Steckbrief bietet eine Übersicht über die Materialressource, links ist ein Einblick in die Durchführung. Materialbausteine sind einzel ansteuerbar aber die Lizensierung ist nicht auf den Materialien vorhanden.
Die Quellennachweis lässt nicht nachvollziehen auf welche Bildmaterialien sich die Lizenz bezieht. 
```mermaid
graph LR
A((relimentar))-->B(Steckbrief mit<br/> einer Übersicht)
A --> C(Links ein möglicher<br/>Durchführung)
A --> D(Einzelne Materialbausteine)
A --> E(Lizenz beim Material<br/>nicht ersichtlich)
```

### narrt
In die Suchmaske Praxismaterialien eingegeben, bei Materialart. Klickt man auf ein Material, in diesem Beispiel Multiple Identitäten für die Sekundarstufe I und II.
Eine Kontaktmailadresse, eine Kurzbeschreibung und eine PDF, klickt man auf die PDF bekommt man Arbeitsblätter, kein Verlaufsplan und keine Lizenzierung.
Lizensierung ist allgemein nicht ersichtlich.
```mermaid
graph LR
A((narrt))-->B(Kurzbeschreibung)
A --> C(PDF)
A --> D(Keine Lizensierung <br/> ersichtlich)
A --> E(Keine einheitliche <br/> Präsentation der <br/> Materialien)
```



