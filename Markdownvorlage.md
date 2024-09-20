# Vorlage
Ich habe Angefangen ein Vorlagendokument zu erstellen um nicht immer nach gewissen Coodierungen googlen zu müssen. Bitte gerne ergänzen.

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


## Mermaid-Chart

Live-Editor: https://mermaid.live/edit

### Flowchart
```mermaid
flowchart TD
    A[Inhalt] -->|Inhalt| B(Inhalt)
    B --> C{Inhalt}
    C -->|Inhalt| D[Inhalt]
    C -->|Inhalt| E[Inhalt]
    C -->|Inhalt| F[fa:fa-Inhalt Inhalt]
```
### Beispiel: Sequenz Diagramm
```mermaid
sequenceDiagram
    Alice->>+John: Hello John, how are you?
    Alice->>+John: John, can you hear me?
    John-->>-Alice: Hi Alice, I can hear you!
    John-->>-Alice: I feel great!
```
### Beispiel: Mindmap
```mermaid
mindmap
  root((Titel))
    Blase eins
      Wichtig 11
      Wichtig 12
        Wichtig 122
    Blase zwei
      wichtig 21 <br/>mit Zeilenbruch
      Wichtig 22
        Wichtig 23
            Wichtig 211
            Wichtig 212
            Wichtig 2113
    Blase drei
      Wichtig 32
      Wichtig 32
```