# Vorlage
Ich habe Angefangen ein Vorlagendokument zu erstellen um nicht immer nach gewissen Coodierungen googlen zu müssen. Bitte gerne ergänzen.

## Links im Dokument
Siehe [Fußnoten](#Fußnoten) für mehr Details

## Bild einbetten
![](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO/raw/branch/main/design/logos/fOERbico.svg)

## Tabelle
<table>
  <thead>
    <tr>
      <th>Spalte 1</th>
      <th>Spalte 2</th>
      <th>Spalte 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Inhalt</td>
      <td>Inhalt</td>
      <td>Inhalt</td>
    </tr>
    <tr>
      <td>Inhalt</td>
      <td>Inhalt</td>
      <td>Inhalt</td>
    </tr>
  </tbody>
</table>

### Spaltenbündig
| Linksbündig | Zentriert | Rechtsbündig |
| :---         |     :---:      |          ---: |
| Inhalt  | Inhalt     | Inhalt    |
| Inhalt   | Inhalt      | Inhalt      |


## Textformatierung

**Fett**  
*kursiv*  
~~Durchgestrichen~~  
_**Fett und Kursiv**_
> Dies ist ein Zitat.

Ein Emoji :smile: und noch eines :rocket:.

## Checklisten
- [x] Erledigte Aufgabe
- [ ] Unerledigte Aufgabe

## Fußnoten
Ein Beispieltext mit einer Fußnote[^1].




## Mermaid-Chart

Live-Editor: https://mermaid.live/edit

### Flowchart
```mermaid
flowchart TD
    A[Idee] --> B[Inhaltserstellung]
    B --> C[Rechtsprüfung]
    C --> D{Freigabe erteilt?}
    D -- Ja --> E[OER Veröffentlichen]
    D -- Nein --> F[Überarbeitung]
    F --> B
    E --> G[Feedback von Nutzern]
    G --> H[Verbesserungen umsetzen]
```
### Beispiel: Sequenz Diagramm
```mermaid
sequenceDiagram
    Autor->>Rechtsabteilung: Reicht OER zur Prüfung ein
    Rechtsabteilung-->>Autor: Feedback / Korrekturen
    Autor->>Rechtsabteilung: Überarbeitet und reicht erneut ein
    Rechtsabteilung-->>Autor: Freigabe erteilt
    Autor->>Plattform: Lädt OER auf Plattform hoch
    Plattform-->>Nutzer: Stellt OER zur Verfügung
    Nutzer->>Plattform: Nutzt OER und gibt Feedback
    Plattform-->>Autor: Feedback der Nutzer
```
### Beispiel: Mindmap
```mermaid
mindmap
  root((FOERBICO))
    OER
      Inhalte
      Erstellung
    Rechtsfragen
      Urheberrecht
      Lizenzen
    Technik
      Plattformentwicklung
      Wartung
        wichtig 21 <br/>mit Zeilenbruch
    Pädagogik
      Lernziele
        Wichtig 23
            Wichtig 211
            Wichtig 212
            Wichtig 2113
      Zielgruppen
```
### Gantt-Diagramm
```mermaid
gantt
    dateFormat  YYYY-MM-DD
    title Zeitplan FOERBICO

    section Planung
    Projektstart           :a1, 2024-01-01, 30d
    Inhaltsentwicklung     :a2, 2024-02-01, 60d

    section Entwicklung
    Technische Entwicklung :b1, 2024-04-01, 90d
    Beta-Test              :b2, 2024-07-01, 30d
  

    section Veröffentlichung
    Öffentliches Release   :c1, 2024-08-01, 20d
    Feedbackphase          :c2, 2024-09-01, 30d
```

### Beispiel Hinweisbox
| :zap:        Hinweisbox  |
|-|

[^1]: Hier ist die Fußnote.