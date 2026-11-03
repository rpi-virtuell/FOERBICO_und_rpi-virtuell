# Hub als Nachweis, Etappe 1: Buchführung und Backlog. Umsetzungsplan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bis 09.11.2026 steht die Buchführung (Nachweis-Issues je Hub-Meilenstein in Forgejo), der Hub-Backlog (18 Issues auf gitworkshop), das Ersatz-ADR für Live-Daten, der Entwurf des Erschließungs-Layers und die Liste der Community-Schlüssel.

**Architecture:** Drei Dokumentationswelten, drei Werkzeuge. Forgejo-Entwürfe liegen als Markdown mit Kopfzeilen in `Orga/nachweis-hub/` und werden von `tools/nachweis/post.py` über die Forgejo-API angelegt und verlinkt. gitworkshop-Entwürfe liegen im Poutník-Protokollordner und werden mit den vorhandenen Skripten `pub-issue.sh`/`pub-comment.sh` veröffentlicht. Ein gemeinsames Prüfwerkzeug `tools/nachweis/check.py` hält beide Welten sauber: keine Partner-Vornamen, keine Projektsprache in Hub-Texten, keine toten Verweise. Das reli_hub-Repo bekommt genau eine Änderung: ADR-0006 ersetzt ADR-0002.

**Tech Stack:** Python 3.13 (`python3 -I`, Standardbibliothek, `unittest`), zsh-Skripte, Forgejo REST-API mit Token aus `~/.config/forgejo/token.txt`, ngit 3.0.4 über die Poutník-Skripte, Deno für die reli_hub-Tests (`deno task test`).

**Spec:** `docs/superpowers/specs/2026-11-02-hub-nachweis-gesamtkonzeption-design.md` (Abschnitte 5, 5a, 6, 7, 8 Etappe 1, 9)

**Folgepläne (nicht Teil dieses Plans):** Etappe 2 Navigation rund schleifen bis 16.11. (Runde-3-Issues, rpi-virtuell-Instanz, Startseiten-Narrativ, Querschnitt Live-Abfrage); Etappe 3 Spielregeln, Material-Detail, Schaufenster live bis 24.11.; Etappe 4 Sammlung, Kataloge, Kalender, Personen bis 07.12.; Etappe 5 Rest und Erschließungs-Layer bis 23.12.; Etappe 6 Feinschliff und Launch-Kopie im Januar. Jede Etappe bekommt ihren eigenen Plan, wenn die vorige steht.

## Global Constraints

- Keine Vornamen von Partnern in Dateien oder Commits des offenen Repos; Rollen, Handles, Pubkey-Präfixe. Erlaubt: „Jörg Lohrer", „Jens Dechow" als Entwurfsautor.
- gitworkshop-Texte und das reli_hub-Repo kennen keine Arbeitspakete, Meilensteine, M-Nummern, Förderkennzeichen (Test in `tests/index.test.ts` prüft ADRs und README darauf).
- Keine Schlüssel, Bunker-Links oder Tokens in Dateien oder Chat; Token nur aus `~/.config/forgejo/token.txt` lesen.
- Poutník veröffentlicht erst nach Durchsicht der Entwürfe durch Jörg; Probeläufe nur in `poutnik-test`.
- Push ins reli_hub-Repo nur über `deno task push <branch> --as poutnik|joerg --cwd ~/repositories/reli-hub`, nie `git push` auf das Nostr-Remote; `main` danach nach Forgejo pushen (`git push forgejo main`).
- Nie von `wss://groups.edufeed.org` lesen.
- Python immer mit `-I`; Skripte liegen nicht im selben Ordner wie heruntergeladene Daten.
- Meilensteine in Forgejo werden nicht geschlossen; Nachweis-Issues bleiben offen.
- Entwürfe des Erschließungs-Layers liegen nicht unter `Website/content/`, damit Hugo und die Sync-Pipeline sie nicht vorzeitig veröffentlichen.

## Review Focus

1. Ein Nachweis-Entwurf nennt eine Issue-Nummer, die es nicht gibt (Tippfehler): `check.py` prüft jede `#NNN` gegen den Issue-Schnappschuss (Task 1, Test `test_tote_verweise`).
2. Eine nevent-URL in einem gitworkshop-Text ist abgeschnitten (wie am 03.11. bei einer Perl-Ersetzung): `check.py` verlangt `nevent1` plus mindestens 60 Bech32-Zeichen (Task 1, Test `test_nevent_laenge`).
3. Ein Vorname steckt in gebeugter Form im Text (Genitiv, Plural): die Namensprüfung matcht am Wortanfang, nicht nur das ganze Wort (Task 1, Test `test_namen_gebeugt`). Die Namensliste selbst liegt außerhalb des Repos in `~/.config/nachweis/namen.txt`, damit sie nicht im offenen Repo steht.
4. `post.py` läuft zweimal und legt das Label „Nachweis" oder ein Issue doppelt an: Label wird per Name gesucht, Issues über `ergebnis.json` übersprungen (Task 3, Tests `test_label_vorhanden`, `test_ergebnis_ueberspringt`).
5. Ein Erschließungs-Entwurf landet unter `Website/content/` und wird gebaut: `check.py erschliessung` lehnt Pfade unter `Website/content` ab (Task 1, Test `test_pfad_verbot`; Task 6 nutzt die CLI).

---

### Task 1: Prüfwerkzeug `tools/nachweis/check.py`

**Files:**
- Create: `tools/nachweis/check.py`
- Create: `tools/nachweis/test_check.py`
- Create: `tools/nachweis/README.md` (drei Absätze: Zweck, Aufrufe, Entwurfsformat)

**Interfaces:**
- Produces: `lade_namen(pfad: str = '~/.config/nachweis/namen.txt') -> tuple[str, ...]` (eine Zeile je Vorname; Zeilen der Form `Vorname Nachname` sind erlaubte Vollnamen, die nicht gemeldet werden); `find_namen(text: str, namen: tuple[str, ...], erlaubt: tuple[str, ...] = ()) -> list[str]`; `find_projektsprache(text: str) -> list[str]` (Treffer für `\bAP ?\d`, `\bM ?\d{1,2}\b`, `Meilenstein`, `Arbeitspaket`, `Förderkennzeichen`, `01PO23012`); `find_tote_verweise(text: str, vorhandene: set[int]) -> list[int]`; `find_kurze_nevents(text: str) -> list[str]`; `pfad_erlaubt(pfad: str) -> bool` (False für Pfade, die `Website/content` enthalten); `parse_entwurf(text: str) -> dict` mit Schlüsseln `titel`, `meilenstein` (int oder None), `labels` (list[str]), `id` (str oder None), `body` (Kopfzeilen `TITEL:`, `MEILENSTEIN:`, `LABEL:`/`LABELS:`, `ID:`; der Body beginnt nach der letzten Kopfzeile und einer Leerzeile).
- CLI: `python3 -I tools/nachweis/check.py forgejo <ordner> --issues <jsonl>`; `… gitworkshop <ordner>`; `… erschliessung <ordner>`. Exit 0 ohne Befund, Exit 1 mit Befundliste `datei: art: treffer`.

- [ ] **Step 1: Tests schreiben**

```python
# tools/nachweis/test_check.py
import unittest, check

class Namen(unittest.TestCase):
    def test_namen_gebeugt(self):
        self.assertEqual(check.find_namen("Erikas Branch und Maxens Text", ("Erika", "Max")), ["Erikas", "Maxens"])
    def test_erlaubte_namen(self):
        self.assertEqual(check.find_namen("Max Mustermann schreibt", ("Max",), erlaubt=("Max Mustermann",)), [])
    def test_pfad_verbot(self):
        self.assertFalse(check.pfad_erlaubt("Website/content/de/erschliessung/az-1/index.md"))
        self.assertTrue(check.pfad_erlaubt("Hub-Entwicklung/erschliessung-entwurf/az-1.md"))

class Projektsprache(unittest.TestCase):
    def test_findet_ap_und_m(self):
        self.assertEqual(check.find_projektsprache("siehe AP 4-5 und M30"), ["AP 4", "M30"])
    def test_hub_sprache_sauber(self):
        self.assertEqual(check.find_projektsprache("Sammlung filtern und einbetten"), [])

class Verweise(unittest.TestCase):
    def test_tote_verweise(self):
        self.assertEqual(check.find_tote_verweise("#844 und #9999", {844}), [9999])
    def test_nevent_laenge(self):
        self.assertEqual(check.find_kurze_nevents("https://gitworkshop.dev/nevent1qqsabc"), ["nevent1qqsabc"])

class Entwurf(unittest.TestCase):
    def test_parse_forgejo(self):
        e = check.parse_entwurf("TITEL: Nachweis\nMEILENSTEIN: 99\nLABELS: Nachweis, Community-Hub\n\nText")
        self.assertEqual((e["titel"], e["meilenstein"], e["labels"], e["body"]), ("Nachweis", 99, ["Nachweis", "Community-Hub"], "Text"))
```

- [ ] **Step 2: Tests laufen lassen, Fehlschlag sehen**

Run: `cd tools/nachweis && python3 -I -m unittest -v test_check`
Expected: FAIL/ERROR mit `ModuleNotFoundError: No module named 'check'`

- [ ] **Step 3: `check.py` schreiben** mit den Signaturen aus dem Interfaces-Block und der CLI (argparse, drei Unterbefehle; die CLI lädt die Namen über `lade_namen`, bricht mit Hinweis ab, wenn die Datei fehlt). Namensprüfung: `\b(Name)\w*`, erlaubte Vollnamen werden vorher aus dem Text entfernt. Die Datei `~/.config/nachweis/namen.txt` wird vor Step 4 von Hand angelegt (Vornamen des Teams und der Partner aus den Gedächtnisnotizen, dazu die erlaubten Vollnamen „Jörg Lohrer" und „Jens Dechow"); sie steht nie im Repo.

- [ ] **Step 4: Tests laufen lassen**

Run: `cd tools/nachweis && python3 -I -m unittest -v test_check`
Expected: `OK` (8 Tests)

- [ ] **Step 5: README schreiben und committen**

```bash
git add tools/nachweis/check.py tools/nachweis/test_check.py tools/nachweis/README.md
git commit -m "Nachweis-Werkzeug: Prüfung auf Namen, Projektsprache und tote Verweise"
```

### Task 2: Nachweis-Entwürfe für Forgejo

**Files:**
- Create: `Orga/nachweis-hub/README.md` (Zweck, Format, Reihenfolge, Stand)
- Create: `Orga/nachweis-hub/NN-ap-<x>-<y>.md`, 15 Dateien nach der Tabelle in Spec Abschnitt 6: `01-ap-3-2-3-3.md` (Meilenstein 83), `02-ap-4-2.md` (88), `03-ap-4-3-4-4.md` (90), `04-ap-4-5.md` (99), `05-ap-4-6.md` (115), `06-ap-4-7.md` (101), `07-ap-5-1.md` (89), `08-ap-5-2.md` (97), `09-ap-6-3.md` (100), `10-ap-9-1.md` (87), `11-ap-9-2.md` (8), `12-ap-9-4.md` (118), `13-ap-9-5.md` (16), `14-ap-2-4.md` (121), `15-ap-3.md` (7). AP 6-4 (Meilenstein 14, geschlossen) bekommt kein eigenes Issue; Zeile 4.19 wird in `15-ap-3.md` mit dem Vermerk „Nachtrag zu M35" geführt.
- Create: `Orga/nachweis-hub/issues-snapshot.jsonl` (Kopie des Schnappschusses der offenen Issues aus dem Scratchpad vom 02.11., Felder `n`, `t`, `s`, `ms`)

**Interfaces:**
- Consumes: `parse_entwurf` und CLI `check.py forgejo` aus Task 1.
- Produces: Entwurfsformat, das Task 3 liest: Kopfzeilen `TITEL:`, `MEILENSTEIN: <id>`, `LABELS: Nachweis, Community-Hub[, weitere Labelnamen]`, Leerzeile, Body. Querverweise auf andere Nachweis-Issues als Platzhalter `{{nachweis:04-ap-4-5}}` (Dateiname ohne `.md`), die Task 3 durch URLs ersetzt.

Body-Aufbau je Entwurf (verbindlich, in dieser Reihenfolge): (1) ein Absatz „Was der Antrag zusagt" mit dem Meilenstein-Wortlaut aus der Spec-Matrix; (2) „Wo es im Hub steht": die Zeilen der Matrix mit Route und Stufe; (3) „Checkliste" als `- [ ]`/`- [x]` je Hub-Element und je Beleg, erledigte Belege angehakt; (4) „Belege" mit Links auf Issues (`#NNN`), Repos, Blogbeiträge, ADRs; (5) „Abweichungen vom Antrag" (nur wo die Spec eine nennt: 4.4, 4.5, 4.10, 4.17); (6) „Verweise" auf verwandte Nachweis-Issues als Platzhalter. Keine Personennamen. Titel: `Nachweis AP x-y: <Kurzform der Zusage>`.

- [ ] **Step 1: Schnappschuss ablegen und Prüfung auf den leeren Ordner laufen lassen**

Run: `python3 -I tools/nachweis/check.py forgejo Orga/nachweis-hub --issues Orga/nachweis-hub/issues-snapshot.jsonl`
Expected: Exit 1 mit „keine Entwürfe gefunden"

- [ ] **Step 2: Die 15 Entwürfe schreiben** aus Spec Abschnitt 4 und 6; jeder nennt alle Belege seiner Zeilen aus der Matrix.

- [ ] **Step 3: Prüfung laufen lassen**

Run: `python3 -I tools/nachweis/check.py forgejo Orga/nachweis-hub --issues Orga/nachweis-hub/issues-snapshot.jsonl && ls Orga/nachweis-hub/*.md | grep -c -- '-ap-'`
Expected: Exit 0, dann `15`

- [ ] **Step 4: Committen und Jörg zum Gegenlesen geben** (Gate: Veröffentlichung erst nach seinem Ja)

```bash
git add Orga/nachweis-hub
git commit -m "Nachweis-Hub: 15 Entwürfe für die Nachweis-Issues je Hub-Meilenstein"
```

### Task 3: `tools/nachweis/post.py` und Veröffentlichung in Forgejo

**Files:**
- Create: `tools/nachweis/post.py`
- Create: `tools/nachweis/test_post.py`
- Create (zur Laufzeit): `Orga/nachweis-hub/ergebnis.json`
- Modify: `Orga/nachweis-hub/README.md` (Stand nach Veröffentlichung)

**Interfaces:**
- Consumes: `parse_entwurf` (Task 1); Entwürfe und Platzhalter (Task 2).
- Produces: `label_id(name: str, labels: list[dict]) -> int | None`; `ersetze_verweise(body: str, mapping: dict[str, str]) -> str` (Platzhalter `{{nachweis:<datei>}}` durch die URL aus `mapping`; unbekannte Platzhalter bleiben stehen und werden gemeldet); `zu_ueberspringen(datei: str, ergebnis: dict) -> bool`. CLI: `python3 -I tools/nachweis/post.py --dry` (zeigt Aufrufe), `… --run` (legt an), `… --verknuepfe` (zweiter Durchlauf: Bodies mit URLs patchen, Kommentare auf bestehende Issues setzen, #789 Meilenstein 16 geben, #276 mit Kommentar schließen).

Konstanten in `post.py`: Repo `Comenius-Institut/FOERBICO_und_rpi-virtuell`, API `https://git.rpi-virtuell.de/api/v1`, Label-Name `Nachweis` (Farbe `#1B3892`, wird angelegt, wenn er fehlt), zusätzliche Label-IDs nach Namen aufgelöst. Kommentartext auf bestehende Issues: „Dieses Issue ist Beleg im Nachweis-Issue <URL> (Hub als Nachweis der Antragszusagen)."; Liste der bestehenden Issues: 844→04, 845→01, 843→03, 842→11, 199→01, 696→09, 700→01, 789→13, 276→10 (Kommentar und Schließen: „Die Bedarfserhebung läuft über die gitworkshop-Fäden, die Rückmeldungen der Zwischenfazit-Tagung und Beobachtungen; Beleg im Nachweis-Issue <URL>.").

- [ ] **Step 1: Tests schreiben**

```python
# tools/nachweis/test_post.py
import unittest, post

class Label(unittest.TestCase):
    def test_label_vorhanden(self):
        self.assertEqual(post.label_id("Nachweis", [{"id": 9, "name": "Nachweis"}]), 9)
    def test_label_fehlt(self):
        self.assertIsNone(post.label_id("Nachweis", [{"id": 9, "name": "nostr"}]))

class Verweise(unittest.TestCase):
    def test_ersetzt(self):
        self.assertEqual(post.ersetze_verweise("siehe {{nachweis:04-ap-4-5}}", {"04-ap-4-5": "https://x/1"}), "siehe https://x/1")
    def test_unbekannt_bleibt(self):
        self.assertEqual(post.ersetze_verweise("{{nachweis:99-x}}", {}), "{{nachweis:99-x}}")

class Ergebnis(unittest.TestCase):
    def test_ergebnis_ueberspringt(self):
        self.assertTrue(post.zu_ueberspringen("04-ap-4-5", {"04-ap-4-5": {"number": 900}}))
```

- [ ] **Step 2: Fehlschlag sehen**

Run: `cd tools/nachweis && python3 -I -m unittest -v test_post`
Expected: ERROR `No module named 'post'`

- [ ] **Step 3: `post.py` schreiben** (urllib wie im früheren Skript `post_issues.py` auf dem Branch `issue-ueberarbeitung`; `--dry` druckt Methode, URL, Bytes).

- [ ] **Step 4: Tests laufen lassen**

Run: `cd tools/nachweis && python3 -I -m unittest -v test_post test_check`
Expected: `OK` (13 Tests)

- [ ] **Step 5: Trockenlauf**

Run: `python3 -I tools/nachweis/post.py --dry`
Expected: 1 Label-Aufruf (falls fehlend), 15 POST-Zeilen, keine Fehler

- [ ] **Step 6: Nach Jörgs Ja anlegen und verknüpfen**

Run: `python3 -I tools/nachweis/post.py --run && python3 -I tools/nachweis/post.py --verknuepfe`
Expected: `ergebnis.json` mit 15 Nummern; zweiter Lauf meldet 15 gepatchte Bodies, 9 Kommentare, 1 Meilenstein gesetzt, 1 Issue geschlossen; Kontrolle: `curl` auf Meilenstein 99, 115, 87 zeigt je `open_issues` ≥ 1

- [ ] **Step 7: Committen**

```bash
git add tools/nachweis/post.py tools/nachweis/test_post.py Orga/nachweis-hub/ergebnis.json Orga/nachweis-hub/README.md
git commit -m "Nachweis-Hub: Issues angelegt und verknüpft, leere Meilensteine AP 4-5, 4-6, 9-1 belegt"
```

### Task 4: ADR-0006 im reli_hub-Repo: Live-Daten mit Schnappschuss als Rückfall

**Files (im Klon `~/repositories/reli-hub`, Branch `pr/adr-0006-live-daten` von `main`):**
- Create: `docs/adr/0006-live-daten-mit-rueckfall.md`
- Modify: `docs/adr/0002-instanzen-als-nachbau.md` (Status: „angenommen · 28.10.2026 · Punkt 1 ersetzt durch ADR-0006 am <Datum>")
- Modify: `docs/adr/README.md` (Listenzeile 0006), `README.md` (Tabellenzeile 0006)
- Modify: `tests/index.test.ts:107` (`ADRS` um `'0006-live-daten-mit-rueckfall'` ergänzen; neuer Test prüft, dass 0002 den Text `ersetzt durch ADR-0006` enthält)

**Interfaces:**
- Produces: ADR-Text, auf den Etappe 2 (Querschnitt Live-Abfrage) verweist. Entscheidung in Hub-Sprache: Instanzen und Ansichten laden ihre Inhalte von den Relays; der eingebettete Schnappschuss ist Rückfall und Startzustand; jede Ansicht zeigt sichtbar „Stand vom <Datum>" oder „live"; Nachbau ohne Datenquelle trägt die Kennzeichnung „Nachbau"; Abfragen werden je Ansicht gebündelt und im Browser gehalten. Bezug: Issue „Leiste unten links als eigenständiges Widget" und Faden „rpi-virtuell eigene Community?" (als nevent-Kurz-IDs wie in ADR-0002). Kein Wort zu Tagung, Projektträger, Meilensteinen.

- [ ] **Step 1: Test ergänzen**

```ts
// tests/index.test.ts, nach dem ADR-Test
Deno.test('ADR-0002 verweist auf ADR-0006', async () => {
  const t = await Deno.readTextFile(new URL('../docs/adr/0002-instanzen-als-nachbau.md', import.meta.url));
  assert(/ersetzt durch ADR-0006/.test(t), 'ADR-0002 ohne Ersatzvermerk');
});
```
und `'0006-live-daten-mit-rueckfall'` in `ADRS` eintragen.

- [ ] **Step 2: Fehlschlag sehen**

Run: `cd ~/repositories/reli-hub && deno task test`
Expected: 2 Fehlschläge (Datei 0006 fehlt; Ersatzvermerk fehlt)

- [ ] **Step 3: ADR-0006 schreiben, 0002 ergänzen, beide README-Listen ergänzen**

- [ ] **Step 4: Tests laufen lassen**

Run: `cd ~/repositories/reli-hub && deno task test`
Expected: alle Tests grün (bisher 12 plus 1)

- [ ] **Step 5: Committen, als PR pushen, mergen, nach Forgejo pushen**

```bash
cd ~/repositories/reli-hub && git add docs/adr README.md tests/index.test.ts && git commit -m "ADR-0006: Live-Daten mit Schnappschuss als Rückfall, ersetzt Punkt 1 von ADR-0002"
cd ~/repositories/FOERBICO_und_rpi-virtuell/tools/poutnik && deno task push pr/adr-0006-live-daten --as joerg --cwd ~/repositories/reli-hub
```
Dann `ngit pr merge` nach Jörgs Ja, `git checkout main && git merge --ff-only origin/main && git push forgejo main`.

### Task 5: Hub-Backlog: 18 Issues auf gitworkshop

`2026-11-0X` steht in diesem Task für das Datum des Veröffentlichungstags (Ordnername wie bei den Runden vom 02.11. und 03.11.).

**Files:**
- Create: `tools/poutnik/skripte/pub-issue.sh`, `tools/poutnik/skripte/pub-comment.sh` (Kopien der Skripte aus dem Protokollordner vom 03.11., Pfade unverändert; ein Satz in `tools/poutnik/setup/PROBELAUF.md` verweist darauf)
- Create: `~/.config/poutnik/protokolle/issue-kommentare-2026-11-0X/00-uebersicht.md`, `01-sammlung.md` … `18-startseiten-narrativ.md` (Titel nach Spec Abschnitt 7, Reihenfolge wie dort), `19-kommentar-…` bis `2N-kommentar-…` für die Anschlüsse an Runde-3-Issues (Spec Abschnitt 7, Absatz „Anschlüsse": je ein Kommentar auf „Leiste als Widget", „Leiste konfigurierbar", „dieselben Begriffe", „Anordnung", „direkt zur Aktion", „Konsole auf der Startseite")
- Create: `Hub-Entwicklung/2026-11-0X-hub-backlog-entwurf.md` (Durchsichtsdatei für Jörg: alle Texte hintereinander; wird nach der Veröffentlichung gelöscht, wie am 02.11.)

**Interfaces:**
- Consumes: `check.py gitworkshop` (Task 1); Entwurfsformat der Skripte: Issue `TITEL:`/`LABEL:` + Leerzeile + Body; Kommentar `ZIEL:`/`ID:` + Leerzeile + Body.
- Produces: `neue-issues-urls.json` (`{"01": "<url>", …}`) für die Folgepläne; Labels je Issue aus: `finden`, `kooperieren`, `veroeffentlichen`, `hub`, `schaufenster`, `daten`, `leiste`, `konsole`, `startseite`.

Body-Aufbau je Issue: **Beobachtung** (was der Prototyp heute zeigt), **Erwartung** (was Nutzende erleben sollen), **Vorschlag** (Hub-Element mit Route aus der Spec-Matrix, Datenquelle als Nostr-Kinds), **Anschluss** (Links auf Runde-3-Issues und Fäden, URLs aus `neue-issues-urls.json` vom 03.11. und `links.json` vom 02.11.). Keine AP-/M-Nummern, keine Namen, kein Projektträger. Reihenfolge der Veröffentlichung: zuerst 13 (Querschnitt), dann 1 bis 12, dann 14 bis 18; spätere Issues verlinken frühere mit der URL aus der JSON-Antwort.

- [ ] **Step 1: Skripte kopieren, Entwürfe schreiben, Durchsichtsdatei erzeugen**

Run: `cat ~/.config/poutnik/protokolle/issue-kommentare-2026-11-0X/[0-9][0-9]-*.md > Hub-Entwicklung/2026-11-0X-hub-backlog-entwurf.md`

- [ ] **Step 2: Prüfung**

Run: `python3 -I tools/nachweis/check.py gitworkshop ~/.config/poutnik/protokolle/issue-kommentare-2026-11-0X`
Expected: Exit 0

- [ ] **Step 3: Jörg liest die Durchsichtsdatei** (Gate)

- [ ] **Step 4: Veröffentlichen in der festgelegten Reihenfolge**

Run: je Datei `zsh tools/poutnik/skripte/pub-issue.sh <datei>` bzw. `pub-comment.sh`; nach jedem Issue die URL aus der JSON-Antwort in `neue-issues-urls.json` eintragen und in den noch offenen Entwürfen einsetzen (Python, nicht perl).
Expected: je Aufruf `"command_status": "ok"`; `.err`-Dateien nennen höchstens die bekannten Relay-Ablehnungen (groups.edufeed.org, nos.lol)

- [ ] **Step 5: Kontrolle und Aufräumen**

Run: `cd tools/poutnik && deno task threads --repo reli-hub --since 1`
Expected: 18 Zeilen „angelegt" und 6 Zeilen „Kommentar" von Poutník mit heutigem Datum. Dann `git rm Hub-Entwicklung/2026-11-0X-hub-backlog-entwurf.md` (falls committet) oder löschen; `git add tools/poutnik/skripte tools/poutnik/setup/PROBELAUF.md && git commit -m "Poutník: Veröffentlichungsskripte für Issues und Kommentare im Werkzeug"`.

### Task 6: Entwurf des Erschließungs-Layers

**Files:**
- Create: `Hub-Entwicklung/erschliessung-entwurf/README.md` (Zweck, Zielpfad `Website/content/de/erschliessung/<az>/index.md` nach Freigabe, Seitenformat wie `Website/content/de/qualitaet/index.md`)
- Create: `Hub-Entwicklung/erschliessung-entwurf/00-einleitung.md`, `az-1.md` … `az-6.md`, `99-schluss.md`

**Interfaces:**
- Consumes: `check.py erschliessung` (Task 1).
- Produces: sieben Texte im Seitenformat (Frontmatter mit `name`, `description`, `datePublished`, `creator` FOERBICO, `license` CC BY 4.0, `id https://oer.community/erschliessung/<slug>`, `url: erschliessung/<slug>`; Body nach Spec Abschnitt 5). Je Zusage ein Absatz mit „Im Hub:" (Route) und „Belege:" (Nachweis-Issue-URL aus `ergebnis.json`, Blogbeiträge, Repos). Zeilen der Stufe B/C mit „in Arbeit, Stand 2026-11-0X". Der Arbeitstitel „Erschließungs-Layer" steht nur im README; die Seiten tragen den Titel, den Jörg wählt, bis dahin „Vom Antrag zum Hub".

- [ ] **Step 1: Prüfung auf Pfadverbot sehen** (Test `test_pfad_verbot` in Task 1 deckt die Funktion; hier die CLI)

Run: `python3 -I tools/nachweis/check.py erschliessung Website/content/de`
Expected: Exit 1 „Entwürfe dürfen nicht unter Website/content liegen"

- [ ] **Step 2: Texte schreiben** aus Spec Abschnitt 4 (eine Zusage je Absatz, 20 Zusagen auf sechs Arbeitsziele verteilt: AZ 1: 4.7, 4.8, 4.20; AZ 2: 4.1, 4.6, 4.11, 4.16, 4.17, 4.19; AZ 3: 4.2, 4.3, 4.12, 4.13; AZ 4: 4.14; AZ 5: 4.4, 4.9, 4.10; AZ 6: 4.5, 4.15, 4.18).

- [ ] **Step 3: Prüfung**

Run: `python3 -I tools/nachweis/check.py erschliessung Hub-Entwicklung/erschliessung-entwurf && grep -c "Im Hub:" Hub-Entwicklung/erschliessung-entwurf/az-*.md | awk -F: '{s+=$2} END {print s}'`
Expected: Exit 0, dann `20`

- [ ] **Step 4: Committen und Jörg zum Gegenlesen geben**

```bash
git add Hub-Entwicklung/erschliessung-entwurf
git commit -m "Erschließungs-Layer: Entwurf der sechs Seiten nach Arbeitszielen"
```

### Task 7: Community-Schlüssel: Bestand und Übergabe

**Files:**
- Create: `Hub-Entwicklung/communities-schluessel.md`

**Interfaces:**
- Produces: Tabelle Community · Instanz dazu · Schlüssel vorhanden (npub, aus `docs/relihub-prototypen.json`, dem Prototyp `CY` und den Gedächtnisnotizen zu reliGlobal, KuRU, rpi-virtuell) · fehlt (relilab, ALPIKA-Grundschule) · wer anlegt (Jörg in der edufeed-App, Bunker-Signer; nichts davon in Dateien) · Katalog-Liste vorhanden (ja/nein). Keine privaten Schlüssel, keine Bunker-Links.

- [ ] **Step 1: Bestand erheben** aus Prototyp (`grep -n "npub" ~/repositories/reli-hub/index.html`), `docs/relihub-prototypen.json` und den Notizen; Tabelle schreiben.

- [ ] **Step 2: Prüfung**

Run: `python3 -I tools/nachweis/check.py erschliessung Hub-Entwicklung && grep -c "nsec\|bunker://" Hub-Entwicklung/communities-schluessel.md`
Expected: Exit 0, dann `0`

- [ ] **Step 3: Committen**

```bash
git add Hub-Entwicklung/communities-schluessel.md
git commit -m "Hub: Bestand der Community-Schlüssel und Übergabeliste für relilab und ALPIKA-Grundschule"
```

### Task 8: Abschluss der Etappe

- [ ] **Step 1: Spec-Fahrplan nachführen**: in `docs/superpowers/specs/2026-11-02-hub-nachweis-gesamtkonzeption-design.md` die Zeile „bis 09.11.2026" um „erledigt am <Datum>: Nachweis-Issues #… bis #…, 18 Hub-Issues, ADR-0006, Erschließungs-Entwurf, Schlüsselliste" ergänzen.

- [ ] **Step 2: Gesamtprüfung**

Run: `cd tools/nachweis && python3 -I -m unittest -q test_check test_post && cd ~/repositories/reli-hub && deno task test`
Expected: beide grün

- [ ] **Step 3: Committen und pushen** (FOERBICO main nach origin, nach Jörgs Ja)

```bash
git add docs/superpowers/specs && git commit -m "Spec: Etappe 1 erledigt, Stand und Issue-Nummern nachgetragen"
```
