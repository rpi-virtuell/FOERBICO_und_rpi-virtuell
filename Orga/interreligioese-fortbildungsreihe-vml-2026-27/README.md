# Interreligiöse Fortbildungsreihe VML × Ev. Schulreferate Düsseldorf und Köln

Arbeitsstand 19.10.2026. Der Verband Muslimischer Lehrkräfte (VML) bietet mit den
Evangelischen Schulreferaten Düsseldorf und Köln vier Online-Module für christliche
und muslimische Lehrkräfte an (Instagram-Ankündigung @verbandmuslimischerlehrkraefte,
Oktober 2026). Die Termine liegen hier als `kind 31923`-Events, publiziert mit dem
relilab-Schlüssel in die relilab-Community (`h`-Tag).

## Termine

| Modul | Termin | Datei | Quelle |
|---|---|---|---|
| Weihnachten in Schule und Unterricht gestalten | Do 12.11.2026, 16–19 Uhr, online | `events/31923-2026-11-12-weihnachten-religionssensibel.json` | ChurchDesk 53772182, Programm Düsseldorf S. 14, PTI 1048834, Programm Köln II/2026 |
| Ramadan in Schule und Unterricht gestalten | Mo 11.01.2027, 16–19 Uhr, online | `events/31923-2027-01-11-ramadan-in-der-schule.json` | ChurchDesk 53792023, Programm Düsseldorf S. 20, PTI 1049092, Programm Köln II/2026 |
| Abraham – Die Opfergeschichte in Islam und Christentum | **noch nicht veröffentlicht** | – | vermutlich 2. Schulhalbjahr 2026/27 |
| Multireligiöse Schulfeiern gestalten | **noch nicht veröffentlicht** | – | vermutlich 2. Schulhalbjahr 2026/27 |

Geprüft am 19.10.2026: ChurchDesk-Terminliste Düsseldorf (bis 19.02.2027), PTI-Kalender
der EKiR (bis April 2027), Programm-PDFs Düsseldorf (1. HJ 26/27) und Köln (II/2026),
vml-deutschland.de. Keine Quelle nennt Termine für Abraham und Schulfeiern. Sobald die
Halbjahresprogramme für Februar–Juli 2027 erscheinen (Düsseldorf: ChurchDesk-Blog
„Fortbildungsprogramm“, Köln: reli-koeln.de/programm), zwei weitere Dateien nach
demselben Muster anlegen.

Die Titel folgen den offiziellen Ausschreibungen („Weihnachten religionssensibel
gestalten“, „Den Ramadan in der Schule gestalten“), nicht den Kurzformen aus dem
Instagram-Post.

## Publizieren

```
cd events
read -rs NOSTR_SECRET_KEY && export NOSTR_SECRET_KEY   # relilab-nsec, Eingabe bleibt unsichtbar
for f in 31923-*.json; do nak event wss://relay.edufeed.org wss://amb-relay.edufeed.org < "$f"; done
unset NOSTR_SECRET_KEY
```

Ohne Relays am Ende ist es ein Trockenlauf (signiert, sendet nicht). Die `d`-Tags
sind stabil (`vml-schulreferat-<datum>-<thema>`), erneutes Publizieren ersetzt.

## Leitung und Kooperation (beide Termine)

| Person | Rolle | Haus |
|---|---|---|
| Yvonne Stegmann-Mangels | Leitung | Ev. Schulreferat Düsseldorf |
| Birgül Karaarslan | Kooperation | VML |
| Esra Kocaman | Kooperation | VML |
| Carmen Schmitt | Kooperation | Ev. Schulreferat Köln |

Alle vier stehen als `contributor` in den Events und zusätzlich als
`["participant", "<Name> (<Haus>)", "", "organizer"]`, der Form, die die edufeed-App
liest; `organizer:name` nennt die drei Institutionen. Niemand hat bisher einen
Nostr-Schlüssel, daher keine `p`-Tags.

## Anmeldung

- Düsseldorf: ChurchDesk-Formular (Weihnachten: `forms.churchdesk.com/f/AEfGxJXjrV`;
  Ramadan: Formular noch nicht freigeschaltet, daher Veranstaltungsseite verlinkt),
  alternativ schulreferat.duesseldorf@ekir.de, T 0211 95757-742.
- Köln: `reli-koeln.de/anmeldung` (so im Instagram-Post genannt).
- Fristen laut Programm Düsseldorf: 05.11.2026 bzw. 07.01.2027 (`registrationDeadline`).
- Kosten nennt keine Quelle, daher kein `price`-Tag.

## Offene Punkte

- **Bilder**: Die ChurchDesk-Motive (pixabay bzw. „rpi loccum“) tragen keine
  ausgewiesene Lizenz, daher kein `image:license:id`; Clients zeigen das
  Community-Fallback-Motiv. Bei Bedarf eigenes CC-Motiv auf Blossom legen und
  `1063`-Nachweis ergänzen (Muster: `Orga/relilab-impuls-2026-27`).
- **Ramadan-Anmeldelink** nachtragen, sobald ChurchDesk das Formular zeigt
  (`form.url` im Widget `n1DYOtuaMl6W` der Organisation 6587).
- **Abraham, Schulfeiern**: Termine ergänzen, wenn veröffentlicht.

Arbeitsweise und Verbesserungsvorschläge: `Orga/termine-als-nostr-kalender-events.md`.
