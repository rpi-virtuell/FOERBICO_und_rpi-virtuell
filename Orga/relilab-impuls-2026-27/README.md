# relilab Impuls 2026/27 — Termine im offenen Datenraum

Arbeitsstand 17.09.2026. Die zehn Termine der Reihe liegen als signierte
Nostr-Kalender-Events auf den edufeed-Relays; die Dateien hier sind die Quelle,
aus der sie publiziert wurden.

## Schlüssel

| Rolle | npub | Funktion |
|---|---|---|
| Publisher | `npub1lde034983zllh2nhe48lt60q6p3a6lsxn0g90uemhg0906jsnzesh5vz8y` | signiert die Events (`relilab-impuls`) |
| Community | `npub1fpcxaz2wvjl90gjs60x37ny2pa5u4yqfx7fklz73rgfjnnfujl3sr2fxgk` | `relilab`, Zuordnung über `h`-Tag |

Der Publisher steht im NIP-29-Roster (`kind 39002`) der Community; die
Kalender-Sektion verlangt `access: members`, damit werden seine Events angezeigt.

## Publizieren

```
read -rs NOSTR_SECRET_KEY && export NOSTR_SECRET_KEY   # Eingabe bleibt unsichtbar
cd events
for f in 1063-*.json 31923-*.json; do
  cat "$f" | nak event wss://relay.edufeed.org wss://amb-relay.edufeed.org
done
unset NOSTR_SECRET_KEY
```

Ohne Relays am Ende ist es ein Trockenlauf (signiert, sendet nicht). Die `d`-Tags
bleiben stabil, ein erneutes Publizieren ersetzt also und dupliziert nicht.

Das AMB-Relay lehnt `kind 1063` ab (`blocked: kind not accepted`) — die
Lizenznachweise liegen auf `relay.edufeed.org`, das genügt.

## Ansicht

`docs/relilab-impuls-kalender.html` lädt die Events live von den Relays.
Über GitHub Pages: `https://rpi-virtuell.github.io/FOERBICO_und_rpi-virtuell/relilab-impuls-kalender.html`

## Datenherkunft

Kein System führt den vollständigen Stand — je Termin stammt der beste Text aus
einer anderen Quelle (siehe `quellen-volltexte.json`):

| Quelle | Termine |
|---|---|
| relilab.org | Zweifeln, Haltung zeigen, Arolsen, Verschwörungen, Wehrpflicht |
| religionsunterricht-pfalz.de (eVEWA) | Kirchengeschichte, Philemon, Schule für alle, Kurzfilme |
| ekiba.de | Ostern (in keiner anderen Quelle) |

Fünf der zehn Termine haben auf relilab.org keine Seite. Referent:innen stehen in
den Landessystemen meist nur im Fließtext, nicht als Datenfeld.

## Offene Punkte

- **Alt-Texte**: alle Events tragen `image:description: "TODO Alt-Text"`.
- **Arolsen-Motiv**: „©Arolsen Archives, mit freundlicher Genehmigung“ — Erlaubnis
  für relilab.org, nicht für die Weitergabe an Dritte. Rückfrage bei Boberg nötig;
  Copyright im 1063 ist zulässig, CC nicht erforderlich. Bis dahin Reihen-Logo.
- **Kunst des Zweifelns**: Bildlizenz auf relilab.org nicht ausgewiesen.
- **Zwei Dienstagstermine** (03.11.2026, 24.11.2026) widersprechen der Regel
  „donnerstags oder freitags“. Gegen die bestehenden Bot-Events geprüft: die
  Zeitstempel stimmen überein, die Abweichung ist real.
- **Ostern (19.02.2027)** hat keinen eVEWA-Eintrag, daher keinen RLP-Anmeldelink.
- **Bot-Ablösung**: Der `relilab-Termine-Bot` publiziert dieselben Termine gecrawlt
  aus WordPress. Solange beide im Roster stehen, erscheinen sie doppelt. Entfernt man
  den Bot aus `kind 39002`, verschwinden seine Events aus der Community-Ansicht,
  bleiben aber auf den Relays.

## Spezifikation

`calendar-integration-ergaenzung.md` enthält die Abschnitte 2.6–2.13 für
`edufeed-examples/calendar-integration.md` — die Felder, die diese Termine brauchen
und die der Guide noch nicht kennt (Anmeldewege je Region, `performer`,
`identifier`, `eventStatus`, Bildlizenz, `about`/`audience`). Antwort auf
edufeed-org/edufeed-app#13.
