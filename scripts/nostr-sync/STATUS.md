# Entwicklungsstand

Kurzfassung für den Einstieg. Das Warum steht in der
[Spec](../../docs/superpowers/specs/2026-09-14-md-to-nostr-sync-neu-design.md), die Bedienung
in der [README](README.md).

**Diese Datei so pflegen, dass ihr `git diff` erzählt, was passiert ist:** oben den Stand
in place ändern, unten im Verlauf einen datierten Eintrag anfügen — jeder mit *was* und *warum*.
Eine Aussage pro Zeile, damit Diffs klein und lesbar bleiben.

## Stand: 2026-09-16

- Tests: **156 grün**, 4 übersprungen (brauchen `node`), Laufzeit ~4 s
- Dry-Run über alle 96 Beiträge: 19 publiziert · 59 unverändert · 14 übersprungen · 4 blockiert
- Jede der 19 Änderungen ist begründet: 15 Sprachreparatur, 4 ohne Live-Event
- Längste Funktion: 81 Zeilen (`publish.py:publish_post`), längste Datei: 188 (`events.py`)
- Ohne `--dry-run` **nicht erprobt** — es wurde noch nie etwas publiziert

## Module

| Modul | Zeilen | Tests | Zustand |
|---|---|---|---|
| `models.py` | 151 | 5 | fertig |
| `frontmatter.py` | 100 | 11 | fertig |
| `references.py` | 73 | 13 | fertig |
| `error_checks.py` | 126 | 14 | fertig |
| `events.py` | 188 | 26 | fertig |
| `nak.py` | 134 | 12 | fertig |
| `images.py` | 177 | 10 | fertig |
| `publish.py` | 154 | 15 | fertig |
| `report.py` | 161 | 9 | fertig |
| `cli.py` | 141 | 10 | fertig |
| `warning_checks.py` | — | — | **fehlt** |
| Golden-Fixtures | — | 24 | fertig |
| Architektur-Tests | — | 11 | fertig |

## Was als Nächstes ansteht

1. **`warning_checks.py`** — Schlagworte im falschen Block (60 Beiträge), relative Bildpfade
   (197), unbekannte Frontmatter-Felder (8), fremder Pubkey am selben Slug.
   *Warum jetzt:* Das ist die halbe Daseinsberechtigung des Umbaus — sichtbar machen, was
   heute stillschweigend verlorengeht. Blockiert nichts, deshalb nach der laufenden Strecke.
2. **Abnahmekriterium `test_1063_byte_identical_to_md2blossom`** — Vergleich gegen
   `Website/scripts/md2blossom.mjs`, Marker `@pytest.mark.md2blossom`, in CI Pflicht.
   *Warum:* kind:1063 ist nicht ersetzbar; weichen die beiden ab, publizieren sie sich
   wechselseitig über. Setzt den fertigen Bilder-Pfad voraus — der steht jetzt.
3. **`.github/workflows/nostr-sync.yml` umbauen** — `mdparser`-Checkout raus, `nak` gepinnt
   mit Checksum rein, `git diff` als Vorfilter, `--log` als Artefakt.
   *Warum zuletzt:* Erst wenn alles andere läuft.
4. **Vier Beiträge redaktionell bereinigen** (NIP-23) — sonst werden sie nach der Umstellung
   nicht mehr aktualisiert. Liste in der Spec unter *Arbeitsliste vor dem Cutover*.

## Bekannte Lücken

- `publish.py:publish_post` hat 81 Zeilen und nähert sich der Grenze von 100. Kommt noch
  etwas hinzu, ist das das Signal zum Teilen.
- Ohne `--dry-run` ist nichts erprobt. Vor dem ersten echten Lauf: einzelnen Beitrag gegen
  einen lokalen `nak serve` publizieren, nicht gegen die produktiven Relays.
- `--relay` nimmt mehrere Relays, `MIN_RELAY_ACKS` ist aber auf 2 vorbelegt, während die
  Vorgabe nur ein Relay enthält. Wirkt heute nicht, weil `min(min_acks, len(relays))` greift —
  beim Hinzufügen eines zweiten Relays prüfen.

## Entscheidungen, die den Code binden

Ändert sich eine davon, gehört die Begründung in die Spec und der Verweis hierher.

- `nak` ist die einzige Subprozess-Grenze; kein reines Modul importiert es (Architektur-Test).
- Fehlende AMB-Pflichtfelder → **übersprungen**, nicht fehlgeschlagen. Job bleibt grün.
- NIP-Verstoß im `content` → **blockiert**. Ein kaputtes Event ersetzt die gute Vorversion.
- Unbekannte Frontmatter-Felder → Warnung, kein Fehler.
- `inLanguage: de` als Skalar wird als `["de"]` gelesen — repariert 19 Live-Events.
- Halb publiziert ist nicht publiziert: Geht das AMB-Event nicht durch, fällt der Beitrag durch.
- Passt die lokale Bilddatei nicht zum attestierten Hash → Nachweis unangetastet lassen.
- Nachweis mit `client`-Tag stammt aus dem Edufeed-Editor → unangetastet lassen.
- `md2blossom.mjs` wird nicht angefasst, bis dieser Sync läuft.

## Verlauf

### 2026-09-16 — AMB-Event und Bilder-Schritt verdrahtet

- `publish.py` gleicht jetzt zwei Events ab (30023 und 30142, je eigenes Relay).
  Die Abgleichlogik steckt in `_sync_event`, weil sie für beide identisch ist.
- Festgelegt: **halb publiziert ist nicht publiziert.** Grund: Der nächste Lauf sieht den
  Artikel als unverändert und holt das fehlende Event nach — die Strecke heilt sich selbst.
- Neues Modul `images.py` statt Ausbau von `publish.py`: „sorge für Blob und Nachweis" ist
  eine andere Aufgabe als „entscheide über den Beitrag".
- Dry-Run mit Bilderschritt: genau **eine** Warnung (`nostr-schrein`, veraltete Datei).
  Gesamtzahlen unverändert — der Bilderschritt blockiert den Artikel nie.

### 2026-09-16 — `CLAUDE.md` angelegt

- Die Stilregeln lagen nur in der Spec und damit nur im Gesprächsverlauf. `CLAUDE.md` wird
  zu Sitzungsbeginn automatisch gelesen — der `dev-principles`-Skill erwartet sie ohnehin.

### 2026-09-16 — CLI dokumentiert, zwei stille Fehler behoben

- Vom Repo-Wurzelverzeichnis fand der Lauf nichts und endete mit **Exit 0**. Ursache: relativer
  Vorgabepfad. Behoben, und `--all` ohne Fundstellen ist jetzt Exit 2.
- Aufruf ohne `--all` und ohne Pfade war ebenfalls ein stiller Erfolg. Jetzt Exit 2.
- Neu: `--show-events` (Event als JSON) und `--log` (vollständiges Protokoll, CI-Artefakt).
  Vorher war nicht nachsehbar, was das Werkzeug tun würde.
- `--help` hatte zwei Optionen ohne Hilfetext; ein Test hält das jetzt fest.

### 2026-09-15 — Golden-Fixtures eingefroren

- Sechs Beiträge samt publizierter Events unter `fixtures/`, 160 KB, hermetisch.
  Vorher existierte der Abgleich nur als Wegwerf-Skript im Gesprächsverlauf.
- Dabei gefunden: ein **dritter** Erzeuger von Lizenznachweisen (Edufeed-Browser-Editor,
  erkennbar am `client`-Tag). Berührt heute nichts, Vorsorge ist im Code.

### 2026-09-15 — Kern gebaut (TDD)

- `frontmatter`, `models`, `references`, `error_checks`, `events`, `nak`, `publish`, `report`, `cli`.
- Gefunden und behoben: `input=""` ist nicht `DEVNULL` — `nak req` lieferte stillschweigend
  nichts mit Exit 0, der Sync hätte jeden Lauf alles neu publiziert.
- Gefunden: 19 Live-Events tragen `["inLanguage","d"]` statt `"de"`.
- Gefunden: `Creator.id` (ORCID) fehlte im Schema — hätte `creator:id` aus allen Events entfernt.
- Gefunden: `2026-01-27-pilgern-im-ru/index.md` ist 0 Byte und ließ den Parser abstürzen.
