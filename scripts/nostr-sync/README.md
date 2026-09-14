# nostr-sync

Publiziert die Blogposts aus `Website/content/` als Nostr-Events. Ersetzt die bisherige
Lösung, die dafür das externe Repo `edufeed-org/mdparser` auscheckte.

**Status: im Aufbau.** Bisher existieren nur `requirements.txt` und die venv — noch kein
Produktivcode. Die Umsetzung erfolgt testgetrieben, Modul für Modul.

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

Die Integrationstests brauchen keinen Netzzugang — sie starten mit
`nak serve --blossom --port 10547` einen lokalen Relay samt Blossom-Server und publizieren
dagegen mit einem Wegwerf-Schlüssel aus `nak key generate`.

## Dry-Run gegen die echten Inhalte

```bash
.venv/bin/python sync.py --dry-run --all
```

Baut alle Events und vergleicht sie mit dem Live-Zustand der Relays, ohne etwas zu
publizieren oder zu signieren.

## Secrets des Workflows

| Variable | Zweck |
|---|---|
| `BUNKER_URL` | NIP-46-Verbindung zum Signer (`nak --sec`) |
| `AUTHOR_PUBKEY_HEX` | Unser Pubkey — für `a`-Tags und für die Idempotenz-Abfragen (`nak req -a`) |
| `CLIENT_SECRET_HEX` | Client-Schlüssel der Bunker-Verbindung (`nak --connect-as`) |

Der Sync publiziert ausschließlich unter diesem Pubkey. Events anderer Pubkeys werden nie
verändert, sondern nur gemeldet, wenn sie denselben Slug belegen.
