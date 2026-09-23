# Entwicklungsstand

Kurzfassung für den Einstieg. Das Warum steht in der
[Spec](../../docs/superpowers/specs/2026-09-14-md-to-nostr-sync-neu-design.md), die Bedienung
in der [README](README.md).

**Diese Datei so pflegen, dass ihr `git diff` erzählt, was passiert ist:** oben den Stand
in place ändern, unten im Verlauf einen datierten Eintrag anfügen — jeder mit *was* und *warum*.
Eine Aussage pro Zeile, damit Diffs klein und lesbar bleiben.

## Stand: 2026-09-21

- Tests: **246 grün**, 4 übersprungen, Laufzeit ~8 s
- CI-Ausgabe knapp: Bericht **45 statt ~500 Zeilen**, dazu Fortschritt je Beitrag
- Workflow umgebaut: kein `mdparser`-Checkout mehr, `nak` gepinnt mit Prüfsumme
- Dry-Run **nachweislich trocken**: 284 `nak`-Aufrufe, 0 Schreibversuche (siehe Verlauf)
- Abnahmekriterium erfüllt: **33 von 33 Bildern zeichengleich zu `md2blossom.mjs`**
- Dry-Run über alle 96 Beiträge: 19 publiziert · 59 unverändert · 14 übersprungen · 4 blockiert
- Jede der 19 Änderungen ist begründet: 15 Sprachreparatur, 4 ohne Live-Event
- Datenqualität sichtbar: 167 Warnungen in 6 Gruppen (Schlagworte, Bilder, Felder)
- Längste Funktion: 83 Zeilen (`publish.py:publish_post`), längste Datei: 204 (`warning_checks.py`)
- Ohne `--dry-run` **nicht erprobt** — es wurde noch nie etwas publiziert

## Module

| Modul | Zeilen | Tests | Zustand |
|---|---|---|---|
| `models.py` | 158 | 6 | fertig |
| `frontmatter.py` | 114 | 13 | fertig |
| `references.py` | 73 | 13 | fertig |
| `error_checks.py` | 126 | 14 | fertig |
| `warning_checks.py` | 204 | 16 | fertig, ohne Pubkey-Prüfung |
| `events.py` | 188 | 26 | fertig |
| `nak.py` | 134 | 12 | fertig |
| `images.py` | 177 | 10 | fertig |
| `publish.py` | 174 | 20 | fertig |
| `report.py` | 388 | 36 | fertig, Ausnahme bei der Dateigröße |
| `cli.py` | 262 | 23 | fertig |
| Golden-Fixtures | — | 24 | fertig |
| Architektur-Tests | — | 13 | fertig |
| `md2blossom`-Vergleich | — | 18 | fertig, braucht `node` |

## Was als Nächstes ansteht

1. **Den ersten Lauf in der CI starten — vollständig als Dry-Run.** Von Hand über
   *Run workflow* mit beiden Schaltern: *alle* und *dry-run*.
   *Vorbedingung:* Der Stand muss auf dem main-Branch der GitHub-Spiegelung liegen, dort
   läuft der Sync und dort liegen die Secrets.
   *Erwartung:* 19 publiziert · 59 unverändert · 14 übersprungen · 4 blockiert, Exit 1 wegen
   der vier NIP-23-Beiträge. Zu prüfen ist vor allem, was lokal nicht prüfbar war: ob der
   Bunker den Client-Schlüssel annimmt (Schritt *Signierstrecke prüfen* — läuft im Dry-Run
   allerdings **nicht**, siehe Bekannte Lücken).
2. **Vier Beiträge redaktionell bereinigen** (NIP-23) — sonst werden sie nach der Umstellung
   nicht mehr aktualisiert. Liste in der Spec unter *Arbeitsliste vor dem Cutover*.
3. **Fremder Pubkey am selben Slug** — der letzte offene Punkt der Warnliste.
   *Warum zurückgestellt:* Er braucht eine zweite Relay-Abfrage je Beitrag (ohne `-a`) und
   gehört damit in `publish.py`, nicht in das reine `warning_checks.py`. Rein informativ —
   bekannt ist genau ein Fall (`rueckblick-auftaktkonferenz-oer-im-blick`).

## Bekannte Lücken

- `report.py` hat **388 Zeilen** und reißt damit die Zielgröße von 300 (`CLAUDE.md` erlaubt
  bis 400 im Ausnahmefall). Der Code selbst sind 198 Zeilen; die Differenz sind 95 Zeilen
  Docstrings mit Messwerten und Fallstricken. Ein Aufteilen nach Ausgabestufe wäre die dort
  ausdrücklich verworfene künstliche Trennung — eine kohärente Datei beantwortet weiter die
  eine Frage „Was ist in diesem Lauf passiert?". Beim nächsten Zuwachs neu bewerten.

- `publish.py:publish_post` hat 83 Zeilen und nähert sich der Grenze von 100. Kommt noch
  etwas hinzu, ist das das Signal zum Teilen.
- Übersprungene Beiträge bekommen keine Konventionswarnungen: 2 der 60 Schlagwort-Fälle
  tauchen deshalb im Bericht nicht auf (beiden fehlt `creator`). Bewusst so — von einem
  Beitrag, der gar nicht publiziert wird, erreichen auch die Schlagworte Nostr nicht.
- Der Bunker-Pfad ist **ungetestet**: Ob der Bunker den Client-Schlüssel aus
  `NOSTR_CLIENT_KEY` akzeptiert, zeigt erst ein echter CI-Lauf. **Lokal gibt es keine
  Zugangsdaten** — keine `.env` im Repo, und der Geschwisterordner `../mdparser/`, aus dem
  `blossom-bunker.ts` seine `.env` liest, existiert auf diesem Rechner nicht. Die Secrets
  liegen ausschließlich in der CI.
- **Der Dry-Run testet die Signierstrecke nicht.** Der Schritt *Signierstrecke prüfen* ist
  auf `inputs.dry_run != true` bedingt. Ein Dry-Run in der CI beweist also alles außer dem
  Bunker. Soll er das mitprüfen, muss die Bedingung fallen — dann braucht auch ein Dry-Run
  die Secrets.
- `cli.py` hat **keine `--blossom`-Option**. Für den Dry-Run ohne Belang (es wird nichts
  hochgeladen), aber ein Lauf ohne `--dry-run` spräche immer den produktiven Mediaserver an.
- Ein Lauf ohne `--dry-run` ist weiterhin durch nichts abgedeckt.
- Die Action-Versionen (`setup-python@v7`, `setup-node@v7`) sind neu im Repo; `checkout@v6`
  und `upload-artifact@v7` bleiben, wie sie vorher schon liefen.
- Der `md2blossom`-Vergleich braucht `Website/scripts/node_modules` (`npm ci`). Fehlt es,
  überspringt er sich — in der CI muss er deshalb **ohne** Skip laufen, sonst ist das
  Abnahmekriterium nur scheinbar erfüllt.
- Ohne `--dry-run` ist nichts erprobt. Vor dem ersten echten Lauf: einzelnen Beitrag gegen
  einen lokalen `nak serve` publizieren, nicht gegen die produktiven Relays.
- `--relay` nimmt mehrere Relays, `MIN_RELAY_ACKS` ist aber auf 2 vorbelegt, während die
  Vorgabe nur ein Relay enthält. Wirkt heute nicht, weil `min(min_acks, len(relays))` greift —
  beim Hinzufügen eines zweiten Relays prüfen.

## Bewusst nicht gemacht

**Der Bericht geht weiterhin an zwei Orte** (`cli.py:102-103`): auf die Standardausgabe und,
in der CI, zusätzlich in die Job-Summary. Der Plan sah vor, ihn auf **eine** Senke zu
reduzieren. Verworfen am 2026-09-23, aus zwei Gründen:

- Der Vorschlag entstand, als der Bericht **500 Zeilen** hatte. Seit der Kurzfassung sind es
  **45** — die Voraussetzung ist um 90 % geschrumpft, der Nutzen entsprechend.
- Der Preis wäre höher als der Gewinn: Das Verhalten hinge dann an einer Umgebungsvariablen,
  was eine Testisolation gegen `GITHUB_STEP_SUMMARY` nötig macht (sonst ist die Suite lokal
  grün und in der CI rot). Und die Fehler stünden **nicht mehr im Schritt-Log** — wer den
  Lauf über `gh run view` ansieht, müsste die Job-Summary-Seite öffnen.

Damit entfällt auch die Testisolation: Sie wird erst gebraucht, *wenn* das Verhalten von der
Umgebung abhängt. Heute findet jeder Test den Bericht überall auf stdout.

**Wieder aufgreifen, falls** der Bericht wieder wächst oder das doppelte Markdown im
Schritt-Log stört.

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
- `@context` und `@type` sind **bekannte** Felder. Sie werden nicht publiziert, aber
  `@context` steht in 82 Beiträgen — als Warnung würde es jede echte Meldung zudecken.
- Konventionswarnungen werden im Bericht nach Regel und Fix gebündelt, nicht je Beitrag
  aufgelistet. Die vollständigen Befunde stehen im Log-Artefakt (`--log`).

## Verlauf

### 2026-09-23 — Gründe übersprungener Beiträge, und zwei Punkte verworfen

- **Punkt 8 umgesetzt:** Übersprungene Beiträge tragen ihren Grund in der Fortschrittszeile.
  Vorher stand er in der CI **nirgends** — die Kurzfassung hat den Abschnitt *Übersprungen*
  nicht, und „16 übersprungen" beantwortet nicht „warum ist mein Beitrag nicht auf Nostr".
  Am vollen Lauf geprüft: `uebersprungen  …/impressum/index.md — Pflichtfelder fehlen …`.
- **Punkte 6 und 9 verworfen**, Begründung unter *Bewusst nicht gemacht*. Kurz: Der Gewinn
  ist seit der Kurzfassung von 500 auf 45 Zeilen geschrumpft, der Preis wäre
  umgebungsabhängiges Verhalten und Fehler, die nicht mehr im Schritt-Log stehen.

Damit ist die Zehn-Punkte-Liste zum Umbau der CI-Ausgabe abgeschlossen: 3, 4, 5, 7, 8 und 10
umgesetzt; 6 und 9 begründet verworfen. **Der nächste offene Punkt ist der Cutover selbst**,
blockiert durch die Lernressourcen-Frage und die vier NIP-23-Beiträge.

### 2026-09-23 — Alle langen Abschnitte klappen auf

- Vorher klappten nur *Zur Nacharbeit* und *Unverändert* auf — ausgerechnet nicht die beiden
  längsten. 54 publizierte Beiträge mit je vier Zeilen füllten den Bericht mit ~280 offenen
  Zeilen. Jetzt klappen alle vier auf, einheitlich beschriftet mit „Betroffene Beiträge".
  Offen bleibt allein *Nicht publiziert*.
- Die vier `<details>`-Zeilen stehen nur noch **einmal** im Code (`_aufklappbar`), vorher
  zweimal kopiert. Gegengeprüft am vollen Lauf: 9 Menüs geöffnet, 9 geschlossen.
- Nebenbei behoben: „**1 Beitrag lagen** bereits so auf dem Relay" — der Satz um die Zahl
  herum entfällt mit der einheitlichen Beschriftung.
- Die Beschriftung ist die einzige Stelle im Ausgabetext mit Umlaut; der Rest benutzt
  ASCII-Umschrift. So gewünscht, aber ein Stilbruch — eine Umstellung des ganzen Textes
  wäre eine eigene Änderung.
- Betrifft nur `--verbose`; die Kurzfassung hat diese Abschnitte nicht.

**Geklärt: Warum der Dry-Run 54 statt 19 Änderungen meldet.** Die Ursache ist kein Fehler —
weder bei uns noch bei der alten Strecke:

`a`-Tag und AMB-Event entstehen **nur** bei `type: LearningResource` (`events.py:65`,
`publish.py:90`; dieselbe Regel in `mdparser`, siehe `docs/nostr-events/kind-30023.md:31`).

| Branch | Beiträge mit `type: LearningResource` |
|---|---|
| `origin/main` | **24** |
| `feat/md-to-nostr` (unser Branch) | **63** |

Auf `main` wurden die Felder bei 39 Beiträgen **absichtlich entfernt** — Merge-Commit
`040e4bc` vom 22.09. 13:58: *„Lernressourcen-Felder bleiben entfernt … `learningResourceType`
und `educationalLevel` wie auf dem Branch entfernt."* Der Workflow-Lauf um 14:35 gehört zu
diesem Commit und hat folgerichtig 24 AMB-Events und 24 Artikel mit `a`-Tag erzeugt. Exakte
Übereinstimmung mit dem Live-Stand.

**Die Konsequenz ist redaktionell, nicht technisch.** Unser Branch trägt die
Lernressourcen-Felder noch. Wird er nach `main` gemerged, kämen sie zurück, und der Sync
stellt 39 AMB-Events und 39 `a`-Tags wieder her — er macht damit eine bewusste Entscheidung
rückgängig. Genau das sind die 54 Änderungen im Dry-Run.

**Vor dem Cutover zu klären: Sollen diese 39 Beiträge Lernressourcen sein oder nicht?**

*Lehre aus der Fehlmessung:* Der erste Befund an dieser Stelle war falsch — er behauptete,
das Frontmatter sei „unangetastet", weil auf **unserem Branch** gemessen wurde. `main` und
`feat/md-to-nostr` laufen im Content auseinander. **Zahlen aus `Website/content/` ohne
Angabe des Branches sind hier wertlos.**

### 2026-09-21 — Probelauf kenntlich, Abstürze abgefangen

Zwei der fünf offenen Punkte aus dem Umbau der CI-Ausgabe.

- **Der Probelauf war nicht von einem echten Lauf zu unterscheiden.** „dry-run — nichts
  gesendet" hing an jedem publizierten Beitrag und erschien nur im Abschnitt *Publiziert* —
  genau dem, den die Kurzfassung weglässt. Beide Läufe meldeten „publiziert 19"; bei einem
  davon ist nichts passiert.
  Jetzt dreifach sichtbar: im Titel (`## Nostr-Sync — PROBELAUF`), als `[!IMPORTANT]`-Block
  **vor** dem `[!CAUTION]`-Block, und als erste Zeile im Schritt-Log. `IMPORTANT`, weil die
  Farben belegt sind: rot = blockiert, gelb = Datenqualität, violett = Probelauf.
- **Ein unerwarteter Fehler löschte alles.** Eine Ausnahme, die nicht `NakFailed` war, fiel
  durch `main()` durch — kein Bericht, keine Summary, **kein Protokoll**, und der
  Artefakt-Schritt lief in `if-no-files-found: warn`. Jetzt wird der Abbruch zu einem
  Ergebnis (`FAILED` mit Grund), das Teil-Protokoll ist gesichert, der Stacktrace geht nach
  stderr.
- **Angehalten wird bewusst**, nicht weitergemacht: Ein unerwarteter Fehler heißt, dass eine
  Annahme nicht stimmt. Die übrigen 90 Beiträge unter dieser Annahme zu publizieren wäre
  schlechter als anzuhalten.
- Nachgezogen: Fehlgeschlagene Beiträge tragen ihren Grund in der Fortschrittszeile, sonst
  stand an der Abbruchstelle nur „fehlgeschlagen <pfad>". Übersprungene bleiben davon
  unberührt — das ist Punkt 8 und weiter zurückgestellt.
- **Gegengeprüft mit einem echten Fehler**, nicht nur im Test: ein `nak`, das bei `req`
  Unsinn mit Exit 0 liefert, erzeugt einen `JSONDecodeError` tief in `fetch_event`.
  Ergebnis: 4 Beiträge im Teil-Protokoll, der fünfte als Abbruch benannt, Stacktrace auf
  stderr, Exit 1, Lauf angehalten.
- Voller Dry-Run unverändert: 19 publiziert · 60 unverändert · 16 übersprungen · 4 blockiert.
  Bericht 49 statt 45 Zeilen (der Hinweisblock).

**Weiter zurückgestellt:** Punkt 8 (Gründe übersprungener Beiträge in der Fortschrittszeile),
Punkt 6 (Bericht in genau eine Senke) und Punkt 9 (Testisolation gegen
`GITHUB_STEP_SUMMARY`, nur mit Punkt 6 nötig).

### 2026-09-21 — CI-Ausgabe knapp, Fortschritt sichtbar

Auslöser: Der Bericht war für einen CI-Lauf unbrauchbar. Vorgabe des Nutzers — im CI nur
eine kurze Übersicht der laufenden Prozesse, Einzelheiten nur bei Problemen; lokal die
ausführliche Form über ein Flag.

- **Fortschritt je Beitrag**, sofort ausgegeben: Ausgang, Pfad, Slug. Vorher arbeitete eine
  stumme Listen-Comprehension alle 99 Beiträge ab — minutenlang keine Zeile, und niemand
  konnte unterscheiden, ob der Lauf arbeitet oder hängt. `flush=True` ist dabei Pflicht:
  In der CI ist stdout kein Terminal, Python puffert sonst 8 KB.
- **`render_brief`**: Kopf, Zähler, ein Warnungszähler, die blockierten Beiträge mit Datei,
  Zeilen, Regel und Fix. Gemessen **45 statt ~500 Zeilen**. Sie wächst nur im Umfang des
  Problems: ~11 Zeilen ohne Fehler, ~8 je blockiertem Beitrag.
- **`--verbose`** schaltet den vollen Bericht ein. Über den Umfang entscheidet allein das
  Flag — die Umgebung nie. `GITHUB_STEP_SUMMARY` bleibt ein reiner Ausgabeort.
- Gefunden: `publish.py` hängt einem blockierten Beitrag auch seine Konventionswarnungen an.
  Gibt die Kurzfassung sie mit aus, ist sie bei vier blockierten Beiträgen wieder ~90 Zeilen
  lang. `_failures` filtert deshalb auf `Severity.ERROR`.
- Beim Gegenlesen des eigenen Ergebnisses korrigiert: Der Warnungszähler stand **hinter** den
  Fehler-Einzelheiten, also 30 Zeilen weiter unten. Jetzt stehen alle Zahlen beieinander,
  bevor die erste Einzelheit kommt. Und „in 80 Beitraege" war der falsche Kasus.
- Beide Renderer teilen `_head`, damit die Reihenfolge nicht zwischen den Stufen
  auseinanderläuft.
- Nebenbefund: `.venv` und `Website/scripts/node_modules` waren verschwunden und wurden
  wiederhergestellt — ohne das zweite überspringt sich das Abnahmekriterium stillschweigend.
- Zahlen verschoben sich, weil Inhalte hinzukamen: **99 Beiträge** (vorher 96),
  60 unverändert, 16 übersprungen. Publiziert und blockiert unverändert 19 und 4.

**Zurückgestellt** (Punkte 6–10 des Plans, in dieser Reihenfolge): Probelauf in der
Kurzfassung kennzeichnen · unerwartete Abbrüche abfangen · Gründe übersprungener Beiträge ·
Tests von `GITHUB_STEP_SUMMARY` isolieren · Bericht in genau eine Senke.

### 2026-09-21 — Erster Lauf vorbereitet: trocken, vollständig, lesbar

Festgelegt: Das Repo bleibt auf Forgejo und wird nach GitHub gespiegelt, **der Sync läuft
vorerst auf GitHub Actions**, dort liegen auch die Secrets. Der Umzug nach Woodpecker kommt
später und steht als *Ausbaustufe 4* in der Spec.

- **Nachgewiesen, dass der Dry-Run trocken ist** — auch beim Blossom-Teil. Dafür ein `nak`
  im PATH, das jede schreibende Operation (`event <relay>`, `blossom upload`) protokolliert
  und mit Exit 99 verweigert. Voller Lauf über alle 96 Beiträge: **284 Aufrufe,
  0 Schreibversuche** (169 `req`, 82 `encode`, 33 `blossom check`).
- Neuer Test hält die Verdrahtung fest: `publish_post` reicht `dry_run` an den Bilderschritt
  durch. Vorher war das nur durch Lesen belegt.
- **`naddr` und `acks` wurden nie gefüllt.** `nak.encode_naddr` war gebaut und getestet,
  `report.py` rendert die Habla-/Yakihonne-Links — nur setzte sie niemand. Damit fehlten in
  jeder Job-Summary die Links, und „publiziert" hieß nur „wir haben es versucht".
  `cli.py` setzt jetzt die Adresse, `publish.py` reicht die Bestätigungen durch.
- Bericht vervollständigt: **unveränderte Beiträge werden aufgelistet** (eingeklappt, vorher
  nur gezählt), Warnungen tragen **Zeilennummern und Fundstellen**, publizierte Beiträge
  nennen die Zahl der Relay-Bestätigungen — im Dry-Run stattdessen den Grund, denn
  „0 Bestätigungen" sähe aus wie ein Fehlschlag.
- Bericht lesbar gemacht: Bei einer Tag-Änderung steht jetzt **nur der abweichende Wert** da.
  Vorher wurden für eine Sprachreparatur 1400 Zeichen Zusammenfassungstext ausgegeben, um
  einen einzigen Buchstaben zu zeigen — aus `- summary: neu ['700 Zeichen…', 'de'] · bisher
  ['700 Zeichen…', 'd']` wird `- summary: Wert 2: neu 'de' · bisher 'd'`.
- Pfade im Bericht sind **relativ zum Arbeitsverzeichnis**. Sonst stünde in jeder Zeile der
  CI-Laufpfad `/home/runner/work/…`.
- Gegenprobe nach allen Änderungen: dieselben 19/59/14/4, weiterhin 0 Schreibversuche,
  Bericht 498 Zeilen, Log 2,3 MB mit allen 96 Beiträgen und 171 Befunden.

### 2026-09-21 — Dokumente auf den gemessenen Stand gebracht

- Spec, Planfile und Event-Doku trugen Zahlen aus der ersten Erhebung. Nachgemessen und
  korrigiert: **189 statt 197 relative Fließtextbilder** (228 statt 236 insgesamt) — die
  Bildmigration arbeitet den Rest ab; **59 statt 61 Schlagwort-Befunde**; die Cutover-
  Erwartung „unchanged für alle" ist durch die tatsächlichen 19/59/14/4 ersetzt.
- Im Planfile standen zudem zu niedrige Zahlen für die NIP-23-Stellen (digiLL 14→**18**,
  impressum 7→**10**, datenschutz 1→**2**). Ursache: Sie stammten von vor dem Verwerfen der
  Adress-Ausnahme. Die Spec war hier schon richtig.
- Die 14 übersprungenen Beiträge sind jetzt namentlich aufgeschlüsselt (1 ohne Frontmatter,
  10 Seiten, 3 mit Datenfehlern); der bislang namenlose dritte Datenfehler ist
  `2025-03-20-dezentrale-oer-infrastrukturen`.
- Gefunden: Der Verweis auf einen `SETUP-GUIDE` mit „Hürde 4" im Workflow-Kommentar ging ins
  Leere — **das Dokument existiert nicht**, auch nicht in der Git-Historie. Aus dem alten
  Workflow übernommen. Zeigt jetzt auf den README-Abschnitt *Secrets des Workflows*.
- `docs/nostr-events/README.md` beschrieb noch den `mdparser/sync`-Weg als den aktuellen.
- Das Planfile trägt jetzt einen Kopf, der sagt, was es noch ist: Entstehungsgeschichte,
  nicht Quelle. Verbindlich sind Spec und diese Datei.

### 2026-09-21 — Workflow umgebaut

- `mdparser`-Checkout und Deno sind raus. Der Workflow hat jetzt zwei Jobs: **Tests als Tor**,
  dann Publizieren. Ohne grüne Tests wird nichts publiziert.
- `nak` kommt gepinnt (v0.17.3) **mit SHA-256-Prüfung** — sonst würde ein ausgetauschtes
  Binary unsere Events signieren. Prüfsumme selbst gebildet, das Release hat keine.
- Eigene Composite-Action `install-nak`, weil beide Jobs sie brauchen und eine Kopie
  auseinanderläuft.
- `select-posts.sh` bildet den Git-Diff auf Beiträge ab. Gegengeprüft an echten Commits und
  fünf Sonderfällen: geändertes Bild wählt seinen Beitrag · Pfad mit Leerzeichen ·
  nur `_index.md` · gelöschter Beitrag · mehrere Dateien desselben Beitrags.
- Gefunden: **ein Beitragspfad enthält Leerzeichen** (`2025-10-10 Offenheit braucht Tiefe
  TiRU Projekt`). Eine interpolierte Argumentliste hätte ihn in fünf nicht existierende
  Pfade zerlegt. Übergabe läuft deshalb zeilenweise über `posts.txt` und `xargs -d '\n'` —
  das schließt zugleich Template-Injection aus.
- Gefunden: `nak` liest den Client-Schlüssel selbst aus `$NOSTR_CLIENT_KEY`. Damit bleibt
  `nak.py` unverändert; der Workflow reicht `CLIENT_SECRET_HEX` unter diesem Namen durch.
- Neuer Schritt *Signierstrecke prüfen*: signiert ein Event **ohne Relay**, bevor irgendetwas
  publiziert wird. Leere Secrets werden vorher beim Namen genannt.
- `concurrency: nostr-sync` — zwei gleichzeitige Läufe würden doppelte kind:1063 hinterlassen.

### 2026-09-21 — Abnahmekriterium: kind:1063 gegen `md2blossom`

- `test_md2blossom.py` vergleicht für alle 16 Beiträge mit `# bilder`-Block die 1063-Tags
  beider Werkzeuge. Ergebnis: **33 von 33 Bildern zeichengleich.**
- Eigene Datei statt `test_events.py` (so stand es im Plan): Er braucht `node`, npm-Pakete
  und echte Bilddateien. `test_events.py` bleibt hermetisch und schnell.
- Unsere Seite läuft über `sync_images` statt direkt über `build_attestation` — so wird
  dieselbe Strecke geprüft wie im Betrieb, samt der Entscheidung, *ob* ein Nachweis entsteht.
- Drei Zusicherungen statt einer: gleiche Tags · genug verglichene Bilder · wir lassen einen
  Nachweis nur aus, wenn die Datei fehlt. Die zweite fängt den stillen Fall ab, dass eine
  Seite nichts mehr baut und der Vergleich trotzdem grün ist.
- Einzige Abweichung ist `2025-07-02-nostr-schrein`, und nur in der Menge: `md2blossom` baut
  dort einen Nachweis ohne `size`, wir bauen keinen. Bekannt und im dritten Test festgehalten.
- Gegengeprüft, dass der Test anschlägt: `.upper()` auf `credit` färbt 4 Beiträge rot,
  ein unterdrückter Nachweisbau lässt Test 2 und 3 fallen.
- `Website/scripts/node_modules` war nicht installiert (`npm ci`), der Test hätte sich
  stillschweigend übersprungen. In der README als Voraussetzung ergänzt.

### 2026-09-16 — `warning_checks.py`: sichtbar machen, was verlorengeht

- Neues Modul mit drei Prüfungen: Schlagworte im falschen Block, Bilder ohne auflösbare
  URL, unbekannte Frontmatter-Felder. Keine blockiert.
- `frontmatter.py` gibt jetzt den `# staticSiteGenerator`-Block heraus (`site_generator`).
  Ohne ihn war der Schlagwort-Vergleich nicht möglich; in ein Event wandert er weiterhin nicht.
  Die Blockzerlegung steckt dabei in `_block`, weil sie zweimal gebraucht wird.
- Gefunden: **`@context` steht in 82 Beiträgen** und wurde als unbekanntes Feld gemeldet —
  82 Warnungen, die die 7 echten zugedeckt hätten. Beide JSON-LD-Schlüssel sind jetzt bekannt.
- `report.py` bündelt Warnungen nach Regel und Fix. Vorher: eine Liste je Beitrag, 602 Zeilen
  Job-Summary. Jetzt 394, mit 6 Gruppen und aufklappbarer Pfadliste.
- Gegengeprüft: 58 + 1 Schlagwort-Befunde statt der gemessenen 60 + 1. Die Differenz sind
  genau zwei übersprungene Beiträge ohne `creator` — kein Fehler in der Prüfung.
- Der Abschnitt *Publiziert* ist vor und nach dem Umbau **zeichengleich**: Die Warnungen
  ändern nichts daran, was publiziert wird.

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
