# nostr-sync

Publiziert die Blogposts aus `Website/content/` als Nostr-Events. Ersetzt die bisherige
Lösung, die dafür das externe Repo `edufeed-org/mdparser` auscheckte.

**Status: im Aufbau.** Bisher existieren nur `requirements.txt` und die venv — noch kein
Produktivcode. Die Umsetzung erfolgt testgetrieben (Test schreiben → scheitern sehen →
minimal implementieren), Modul für Modul in dieser Reihenfolge:

| # | Modul | Inhalt |
|---|---|---|
| 1 | `frontmatter.py` | Drei-Block-Format lesen, Werte normalisieren — `models.py` entsteht dabei mit |
| 2 | `references.py` | Slug, SHA-256 aus Blossom-URL, `a`-Koordinate, Bildliste |
| 3 | `error_checks.py` | Prüfungen, die blockieren (NIP-01/23/94) |
| 4 | `warning_checks.py` | Prüfungen, die nur melden (unsere Konventionen) |
| 5 | `events.py` | Events bauen (30023, 30142, 1063) und vergleichen |
| 6 | `nak.py` | Die einzige Subprozess-Grenze, gegen `nak serve` getestet |
| 7 | `publish.py` | Pro Beitrag entscheiden: publizieren, überspringen, scheitern |
| 8 | `report.py` | Job-Summary mit Schweregrad, Herkunft und `naddr`-Links |
| 9 | `cli.py` | Einstieg: Argumente, Verdrahtung, Exit-Code |
| 10 | `.github/workflows/nostr-sync.yml` | Umbau des Workflows zum Schluss |

Grenzen: Funktionen höchstens 100 Zeilen, Dateien bis 300 (im Ausnahmefall 400).
Abhängigkeiten zeigen in eine Richtung — **kein reines Modul importiert `nak`**, abgesichert
durch einen Test. Begründung in der Spec unter *Architektur* und *Code-Stil*.

> Diese Tabelle und der Status-Hinweis darüber sind Bauzustand, keine Dokumentation.
> **Wenn Punkt 10 erledigt ist, beides hier löschen** — was das Skript tut und warum,
> steht in der Spec, wie man es bedient in den Abschnitten unten.

## Warum das so gebaut ist

Die vollständige Begründung samt Messdaten steht in der Spec:
[`docs/superpowers/specs/2026-09-14-md-to-nostr-sync-neu-design.md`](../../docs/superpowers/specs/2026-09-14-md-to-nostr-sync-neu-design.md)

Die drei Kernentscheidungen in Kürze:

- **`nak` macht das Protokoll.** Signieren (NIP-46 Bunker), Publizieren, Abfragen und
  Blossom-Upload übernimmt das `nak`-Binary. Eigener Code gibt es nur für
  Frontmatter → Nostr-Tags. Alle Subprozess-Aufrufe stecken in `nak.py` — wird `nak`
  einmal ersetzt, ist nur dieses Modul betroffen.
- **Das Relay ist die Wahrheit.** Vor jedem Publizieren wird das bestehende Event abgefragt
  und verglichen. Kein Zustand in Git, keine Änderungserkennung aus der History. Ein Lauf
  ist damit beliebig oft wiederholbar.
- **Spezifikationsverletzungen brechen ab.** Ein Event, das gegen NIP-01/23/94 verstößt,
  wird nicht publiziert — es würde auf dem Relay die funktionierende Vorversion ersetzen.
  Verstöße gegen unsere *eigenen* Konventionen (Schlagworte, Bilder) werden dagegen nur
  sichtbar protokolliert.

Was die drei Event-Typen enthalten, steht in
[`docs/nostr-events/`](../../docs/nostr-events/README.md).

## Einrichten

```bash
cd scripts/nostr-sync
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

Zusätzlich wird das [`nak`](https://github.com/fiatjaf/nak)-Binary gebraucht
(entwickelt gegen v0.17.3).

## Tests

```bash
.venv/bin/python -m pytest -q
```

Die Integrationstests brauchen keinen Netzzugang: Ein Fixture startet `nak serve --blossom`
auf einem freien Port, jeder Test signiert mit einem eigenen Wegwerf-Schlüssel.

Der Vergleichstest gegen `md2blossom` braucht zusätzlich `node` und dessen
npm-Abhängigkeiten — einmalig:

```bash
cd Website/scripts && npm ci
```

Fehlt eines von beidem, wird er lokal übersprungen; `-m "not md2blossom"` schließt ihn auch
bewusst aus. **In der CI ist er Pflicht** — er sichert, dass unsere `kind:1063` zeichengleich
zu `md2blossom.mjs` bleiben. Wären sie es nicht, würden sich beide Werkzeuge wechselseitig
überpublizieren: 1063 ist nicht ersetzbar, die Nachweise häufen sich an.

## Aufrufen

```bash
scripts/nostr-sync/.venv/bin/python scripts/nostr-sync/cli.py [Optionen] [Pfade…]
```

Das Arbeitsverzeichnis ist egal. Entweder `--all` **oder** einzelne `index.md`-Pfade angeben —
ohne beides gibt es keinen Auftrag und der Aufruf endet mit Exit 2.

### Optionen

| Option | Bedeutung |
|---|---|
| `--all` | alle Beiträge unter `--content-root` |
| `--dry-run` | entscheiden und berichten, aber **nichts senden**. Braucht keinen Signer |
| `--show-events` | die gebauten Events als JSON ausgeben — zeigt, was gesendet würde |
| `--log DATEI` | vollständiges Ergebnis maschinenlesbar als JSON (das CI-Artefakt) |
| `--content-root PFAD` | Wurzel der Beiträge für `--all`. Vorgabe: `Website/content` im Repo |
| `--pubkey HEX` | unser Pubkey. Sonst aus `AUTHOR_PUBKEY_HEX` |
| `--relay URL` | Relay für kind:30023, mehrfach angebbar. Vorgabe: `relay-rpi.edufeed.org` |
| `--amb-relay URL` | Relay für die AMB-Metadaten (kind:30142) |
| `--help` | alle Optionen mit Hilfetext |

### Umgebungsvariablen

| Variable | Wofür | Pflicht |
|---|---|---|
| `AUTHOR_PUBKEY_HEX` | unser Pubkey; ohne ihn ist der Idempotenz-Check blind | immer (oder `--pubkey`) |
| `BUNKER_URL` | NIP-46-Signer | nur ohne `--dry-run` |
| `NOSTR_CLIENT_KEY` | liest **`nak` selbst** (`--connect-as`): der feste Client-Schlüssel der Bunker-Verbindung. Fehlt er, nimmt `nak` jedes Mal einen neuen, und der Bunker verlangt eine neue Freigabe | in der CI |
| `GITHUB_STEP_SUMMARY` | setzt die CI; dorthin geht die Zusammenfassung zusätzlich | nein |

### Exit-Codes

| Code | Bedeutung |
|---|---|
| 0 | alle Beiträge publiziert, unverändert oder erklärt übersprungen |
| 1 | mindestens ein Beitrag blockiert (Spezifikationsverletzung, zu wenige Bestätigungen, Relay nicht abfragbar) |
| 2 | Bedienung oder Konfiguration: kein Auftrag, `--all` ohne Fundstellen, fehlender Pubkey oder Signer |

`--all` ohne gefundene Beiträge ist mit Absicht ein Fehler und kein stiller Erfolg: Ein grüner
Lauf, der nichts bearbeitet hat, verdeckt genau die Störung, die er melden soll.

## Typische Aufrufe

```bash
export AUTHOR_PUBKEY_HEX=5a12b41ec15b466321e88c371be2dc47d9193f9c8bba4ab09fc50045bd35aedf

# Alles ansehen, nichts senden
… cli.py --all --dry-run

# Einen Beitrag ansehen, mit dem Event im Klartext
… cli.py --dry-run --show-events Website/content/de/posts/<ordner>/index.md

# Mit vollständigem Protokoll zum Nachlesen
… cli.py --all --dry-run --log /tmp/nostr-lauf.json
```

Zum gefahrlosen Ausprobieren: eine Kopie nach `/tmp` legen und dort ändern. Der `d`-Tag kommt
aus `commonMetadata.id`, nicht aus dem Ordnernamen — die Kopie wird also gegen dasselbe
Live-Event verglichen wie das Original.

```bash
cp -r Website/content/de/posts/<ordner> /tmp/probe
# in /tmp/probe/index.md etwas ändern
… cli.py --dry-run /tmp/probe/index.md
```

## Zwei Ausgaben: Bericht und Protokoll

| | Job-Summary (`GITHUB_STEP_SUMMARY`, stdout) | Protokoll (`--log`, CI-Artefakt) |
|---|---|---|
| Adressat | Redaktion | Nachforschung |
| Form | Markdown, gruppiert, einklappbar | JSON, ein Eintrag je Beitrag |
| Enthält | jeden Beitrag: blockiert, publiziert, unverändert, übersprungen — mit Adresse, Links, Bestätigungen, Befunden samt Zeilen und Fundstellen | zusätzlich die **vollständigen Events** (gebaut und der Relay-Stand) |

Beide nennen jeden Beitrag. Der einzige Unterschied: Ändert sich ein Tag, zeigt der Bericht
**nur den abweichenden Wert**, nicht den ganzen Tag. Sonst stünden für eine Sprachreparatur
1400 Zeichen Zusammenfassungstext da, um einen einzigen Buchstaben zu zeigen. Das
vollständige Event steht im Protokoll.

## Secrets des Workflows

| Variable | Zweck |
|---|---|
| `BUNKER_URL` | NIP-46-Verbindung zum Signer (`nak --sec`) |
| `AUTHOR_PUBKEY_HEX` | Unser Pubkey — für `a`-Tags und für die Idempotenz-Abfragen (`nak req -a`) |
| `CLIENT_SECRET_HEX` | Client-Schlüssel der Bunker-Verbindung; der Workflow reicht ihn als `NOSTR_CLIENT_KEY` durch, `nak` liest ihn von dort |

Der Sync publiziert ausschließlich unter diesem Pubkey. Events anderer Pubkeys werden nie
verändert, sondern nur gemeldet, wenn sie denselben Slug belegen.

## Was der Workflow tut

`.github/workflows/nostr-sync.yml`, zwei Jobs:

1. **Tests** — die gesamte Suite, danach der Vergleich gegen `md2blossom` in einem eigenen
   Lauf. Wird er übersprungen, fällt der Job: Ein Skip wäre hier kein Erfolg, sondern ein
   ungeprüftes Abnahmekriterium.
2. **Publizieren** — läuft nur, wenn die Tests grün sind.

Zwei Hilfsteile, weil beide Jobs bzw. mehrere Fälle sie brauchen:

| Datei | Aufgabe |
|---|---|
| `.github/actions/install-nak/` | `nak` in gepinnter Version installieren und die SHA-256 prüfen |
| `.github/scripts/select-posts.sh` | aus dem Git-Diff die betroffenen `index.md` ermitteln |

**Der Git-Diff ist nur ein Vorfilter für die Laufzeit.** Ob publiziert wird, entscheidet der
Vergleich mit dem Relay — ein Lauf mit *alle* muss zum selben Ergebnis führen wie einer mit
Diff. Die Auswahl geht deshalb im Zweifel zu weit statt zu kurz:

- Ein geändertes **Bild** wählt seinen Beitrag mit aus (Blob und Lizenznachweis hängen daran).
- Ist der Vorgängercommit nicht auswertbar (neuer Branch, Force-Push, erneuter Lauf), werden
  **alle** Beiträge angesehen — mit sichtbarem Hinweis, nicht stillschweigend.
- Gehört zu keiner Änderung eine `index.md`, wird nichts publiziert; auch das steht als
  Hinweis in der Zusammenfassung.

Von Hand starten (*Run workflow*) mit zwei Schaltern: **alle** Beiträge ansehen und
**dry-run** (entscheiden, nichts senden). Für den ersten Einsatz beides zusammen.
