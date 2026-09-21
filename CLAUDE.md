# Arbeitsregeln für dieses Repo

Dieses Repo enthält die Inhalte von [oer.community](https://oer.community) (Hugo) und die
Werkzeuge, die sie nach Nostr publizieren.

## Code-Stil

Die Regeln gelten für allen Code hier, besonders für `scripts/nostr-sync/`.

| Grenze | Wert |
|---|---|
| Funktion | höchstens 100 Zeilen — die meisten werden 10–30 lang |
| Datei | bis 300, im Ausnahmefall 400 Zeilen |

Nähert sich eine Funktion der Grenze, ist das kein Anlass zum Verdichten, sondern das Signal,
dass sie mehrere Schritte erledigt.

- **Eine Datei, eine Aufgabe. Nichts mischen.** Jedes Modul beginnt mit einem Docstring, der
  sagt, welche *eine* Frage es beantwortet und was es ausdrücklich **nicht** tut.
- **Wiederverwendbares in ein eigenes Modul**, nicht in eine Sammelkiste.
- Kleiner ist besser, aber nicht immer sinnvoller: Eine kohärente lange Datei schlägt zwei
  künstlich getrennte.
- **Bezeichner auf Englisch** (`extract_slug`, `tags_equal`). Deutsch bleibt den Texten
  vorbehalten — Docstrings, Logmeldungen, Job-Summary. Die richten sich an die Redaktion.
- Sprechende Namen statt Kommentare. Kommentare nur, wo das *Warum* nicht im Code steht:
  eine Protokollregel, ein Fallstrick, eine bewusste Abweichung.
- Keine verdichteten Einzeiler, keine mehrstufigen Comprehensions. Eine Schleife, die man laut
  vorlesen kann, schlägt einen cleveren Ausdruck.
- Flache Verschachtelung: früh zurückkehren statt `else`-Treppen.
- Typannotationen an allen öffentlichen Funktionen.

## Vorgehen

- **Testgetrieben.** Erst der Test, dann scheitern sehen, dann die minimale Umsetzung.
- **Gegen echte Daten gegenprüfen.** Unit-Tests haben hier mehrfach nichts gefunden, was ein
  Lauf über `Website/content/` und die produktiven Relays sofort zeigte. Wenn ein Werkzeug
  sich unerwartet verhält: mit einem zweiten, unabhängigen Weg nachmessen, bevor daraus eine
  Festlegung wird.
- **Nichts behaupten, was nicht geprüft ist.** Erst „fertig" sagen, wenn die Tests nachweislich
  grün sind.
- **Kein stiller Erfolg.** Ein grüner Lauf, der nichts getan hat, ist die gefährlichste
  Ausgabe. Wo nichts zu tun war, muss das benannt werden — sonst ist es ein Fehler.

## Testen

```bash
cd scripts/nostr-sync
.venv/bin/python -m pytest -q          # braucht kein Netz, keine Schlüssel
```

Die Integrationstests starten sich ihren Relay selbst (`nak serve` auf freiem Port, eigener
Wegwerf-Schlüssel je Test). `nak` muss installiert sein.

## Wo was steht

| Thema | Ort |
|---|---|
| Warum der Sync so gebaut ist, alle Entscheidungen mit Messdaten | `docs/superpowers/specs/2026-09-14-md-to-nostr-sync-neu-design.md` |
| Bedienung, Optionen, Exit-Codes | `scripts/nostr-sync/README.md` |
| Was in den drei Event-Typen steht | `docs/nostr-events/` |
| Bildmigration und Schlagwort-Glossar | `Orga/oer-community-webseite-orga/` |

## Was man wissen sollte, bevor man etwas ändert

- `scripts/nostr-sync/fixtures/` enthält eingefrorene Live-Events. Schlagen die Golden-Tests
  fehl, weicht das gebaute Event von dem ab, was auf den Relays steht — das ist fast immer
  ein Fehler und kein Grund, die Fixtures anzupassen.
- `Website/scripts/md2blossom.mjs` baut dieselben Events ein zweites Mal. Es wird bewusst
  **nicht** angefasst, bis der neue Sync läuft. Einzelheiten in der Spec.

Ergänzend gilt der `dev-principles`-Skill; diese Datei hat bei Widersprüchen Vorrang.
