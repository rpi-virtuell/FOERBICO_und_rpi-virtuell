<!--
Arbeitsplan aus der Claude-Code-Sitzung vom 2026-09-14.
Enthaelt zusaetzlich zum Vorhaben den Arbeitsablauf (Umsetzungsreihenfolge, Stand).
Die bereinigte Fassung ohne Ablaufteile liegt als Spec unter:
docs/superpowers/specs/2026-09-14-md-to-nostr-sync-neu-design.md
-->

# Markdown → Nostr Publishing neu aufsetzen (Greenfield)

## Kontext

Heute publiziert `.github/workflows/nostr-sync.yml` die Blogposts aus `Website/content/`
nach Nostr, indem es ein **externes Repo** (`edufeed-org/mdparser`) auscheckt und dessen
Deno-Modul `sync/` ausführt. Drei Probleme motivieren den Neubau:

**1. Fragile Änderungserkennung.** `mdparser/sync/core/change-detection.ts` rekonstruiert
„was hat sich geändert" aus der Git-History (`GITHUB_EVENT_BEFORE`, `fetch-depth: 0`). Das
bricht bei Squash-Merges, Force-Pushes und manuellen Re-Runs. Der Code enthält deshalb in
`core/summary.ts` eine eigene „still gescheitert"-Erkennung — der Kommentar dort beschreibt
den Fall wörtlich: *„Redaktion pusht einen Post, die Action meldet Erfolg, auf Nostr kommt
nichts an."* Das Symptom wird gemeldet, die Ursache bleibt.

**2. Viel eigener Protokoll-Code.** Signieren (NIP-46), Relay-Publishing, Blossom-Upload
(BUD-01), Hashing — über 1000 Zeilen, die gepflegt werden müssen, obwohl sie nichts
projektspezifisches tun.

**3. Schlagwort-Datenlage ist unbemerkt inkonsistent.** `core/parser.ts` liest ausschließlich
den `# commonMetadata`-Block und verwirft den `# staticSiteGenerator`-Block ausdrücklich
(„Hugo-Reste, werden ignoriert"). Publiziert werden nur `commonMetadata.keywords`. Die
Konvention dazu steht im Repo — `Orga/oer-community-webseite-orga/wissensgrundlagen/schlagworte.yaml`:

> *„Kanonische Liste aller gültigen Tags/Keywords. Nur diese Schreibweisen verwenden – in
> `keywords` (commonMetadata) und identisch in `tags` (staticSiteGenerator)."*

Auswertung über alle 98 Posts mit Frontmatter zeigt, dass diese Konvention selten eingehalten wird:

| | Posts | Wirkung |
|---|---|---|
| A — `commonMetadata.keywords` gefüllt und konsistent | 22 | `t`-Tags landen im Event |
| B — Schlagworte vorhanden, aber **nicht** in `commonMetadata.keywords` | **60** | erreichen Nostr nicht |
| C — beide Felder gefüllt, aber inhaltlich abweichend | 1 | teils publiziert, teils nicht |
| D — gar keine Schlagworte | 15 | nichts zu übertragen |

Verteilung der Felder: `commonMetadata.keywords` 23×, `commonMetadata.tags` 2×,
`staticSiteGenerator.keywords` 1×, **`staticSiteGenerator.tags` 81×** — die Schlagworte
leben faktisch im Hugo-Block. Nachprüfbar an den Live-Events: `2025-06-02-RPT25`
(Slug `ki-und-religionspaedagogik`) hat 6 Schlagworte in der Datei, das Relay-Event hat
`t_tags: []`.

**Ziel:** Eine skriptbasierte, modulare Lösung in diesem Repo, die deutlich weniger eigenen
Code hat, idempotent ist (grün heißt: nachweislich publiziert) und Datenprobleme wie oben
**sichtbar macht**, statt sie stillschweigend zu übergehen.

## Getroffene Entscheidungen

| Thema | Entscheidung |
|---|---|
| Ort | **Dieses Repo**, `scripts/nostr-sync/` — kein externes Repo-Checkout mehr |
| Umfang | **Volle Parität**: kind:30023, kind:30142, kind:1063 + Blossom, Änderungserkennung, Job-Summary |
| Signing | **NIP-46 Bunker beibehalten** → Publisher-Identität (Pubkey) bleibt unverändert |
| Protokoll-Engine | **`nak`** (Version gepinnt), gekapselt in **genau einem** Modul |
| Zustandsmodell | **Relay ist die Wahrheit** (idempotent); Git-Diff nur noch Vorfilter in der Workflow-YAML |
| Frontmatter-Schema | **Unverändert** |
| Schlagworte | **Keine Zusammenführung.** `t`-Tags kommen weiterhin ausschließlich aus `commonMetadata.keywords`. Abweichungen werden **protokolliert** (siehe unten) |
| Schema-Validierung | **Pflicht** — fehlplatzierte/unbekannte Felder werden gemeldet, nicht verschluckt |
| Publisher | **Immer unser Pubkey** (`AUTHOR_PUBKEY_HEX` via Bunker). Events fremder Pubkeys werden nie angefasst, nie ersetzt, nur gemeldet |
| Bilder | **Verhalten unverändert.** Blossom-Upload und kind:1063 nur für Hash-URLs. Relative Pfade und Nicht-Hash-URLs werden **protokolliert** (siehe unten) |
| Glue-Sprache | **Python 3 + Pydantic** (entschieden), `pytest` für Tests, `requirements.txt` im CI |

### Sprachentscheidung: Python 3 + Pydantic

Gewählt, weil das Team weder Python noch TypeScript aktiv schreibt: Der Code wird überwiegend
**gelesen und reviewt**, nicht täglich geändert. Dafür ist Python die zugänglichere Sprache,
und der Subprozess-Aufruf an `nak` ist damit knapper als mit Denos `Command`-API.

Pydantic übernimmt die Schema-Validierung des Frontmatters — das ist der eigentliche Gewinn,
weil statische Typen allein die Klasse von Fehlern, die hier real auftritt (Feld steht im
falschen Block, YAML liefert ein `Date` statt eines Strings), **nicht** abfangen.

Stack: Python 3.13, `pydantic`, `PyYAML`, `pytest`, projektlokale venv unter
`scripts/nostr-sync/.venv` (gitignored), Abhängigkeiten gepinnt in
`scripts/nostr-sync/requirements.txt`.

## Schlagwort-Abweichungen protokollieren (statt zusammenführen)

Der Sync **ändert nichts** am publizierten Ergebnis: `t`-Tags entstehen wie bisher nur aus
`commonMetadata.keywords`. Zusätzlich liest er den `# staticSiteGenerator`-Block **nur zum
Vergleich** und schreibt ein Protokoll, wenn die Felder der dokumentierten Konvention
widersprechen:

| Fall | Meldung | Erwartete Menge |
|---|---|---|
| `commonMetadata.keywords` leer, aber Schlagworte in `commonMetadata.tags` / `staticSiteGenerator.keywords` / `staticSiteGenerator.tags` | „Schlagworte vorhanden, erreichen Nostr aber nicht" | 60 Posts |
| Beide gefüllt, Inhalte weichen ab | „Felder weichen voneinander ab" + Differenzmenge in beide Richtungen | 1 Post (`2026-06-25-Personal-Learning-Environments`) |

Das Protokoll gehört in die Job-Summary (kompakte Zähler + betroffene Slugs) und vollständig
in das Run-Log-Artefakt. **Es blockiert das Publizieren nicht** — es ist ein Datenqualitäts-
Signal für die Redaktion, kein Fehler.

## Bilder: was genau passiert

Der Bilder-Schritt läuft **nach** dem Publizieren des Artikels und blockiert ihn nie
(„Git ist die Wahrheit, die URL steht schon im Beitrag"). Er betrachtet Cover
(`commonMetadata.image`) und alle Fließtextbilder, aber er **greift nur bei URLs mit einem
SHA-256 im Pfad** (`https://blossom.edufeed.org/<64-hex>.jpg`):

1. `nak blossom check` → liegt der Blob schon auf dem Mediaserver?
2. Wenn nicht: Datei mit demselben Hash im Post-Ordner suchen → `nak blossom upload`
   (BUD-01, Auth-Event kind:24242, signiert über den Bunker). Datei fehlt → Warnung.
3. Passenden Eintrag im `# bilder`-Block suchen (über Dateiname oder URL). Fehlt er, oder
   fehlt darin `licenceUrl` → Warnung, **kein** 1063.
4. kind:1063 bauen, jüngsten vorhandenen Nachweis per `nak req -k 1063 -a <pubkey> -t x=<hash>`
   holen, Tags vergleichen → nur bei Abweichung publizieren.

### Was mit welchem URL-Typ passiert

| URL-Typ | `x`-Tag im 30023 | Blossom-Upload | kind:1063 | Ergebnis für Leser*innen |
|---|---|---|---|---|
| `https://blossom.edufeed.org/<hash>.jpg` | ja | ja | ja (wenn `# bilder`-Eintrag vorhanden) | auflösbar, lizenzbelegt |
| andere absolute URL (`https://oer.community/…`) | nein | nein | nein | auflösbar, ohne Nachweis |
| relativer Pfad (`bild.jpg`) | nein | nein | nein | **im Nostr-Client kaputt** |

### Die Cover-`x`-Konvention (positionsabhaengig — Vorsicht)

`events/article.ts` schreibt die `x`-Tags in genau dieser Reihenfolge:

1. `["image", <url>]`, direkt gefolgt von `["x", <cover-hash>]` — **das erste `x` IST der Cover-Hash**
2. danach je ein `x` pro Fließtextbild mit Hash-URL, in Auftretensreihenfolge, dedupliziert
   (zeigt der Text das Cover erneut, gibt es trotzdem nur ein `x`)

Es gibt kein Label und keinen Marker — die Bedeutung entsteht **allein aus der Position**.
edufeeds ArticleView und der Hub lesen das erste `x` als Cover. Wird die Tag-Reihenfolge
irgendwo sortiert oder umgruppiert, ist still ein anderes Bild das Cover. Deshalb ist im
Vorab-Check bestaetigt, dass `nak` die Tags unveraendert durchreicht.

**Risikonotiz:** Der `x`-Tag ist in einem 30023 nicht standardisiert — nostrbook kennt keine
`x`-Tag-Doku; `x` ist in NIP-94 als SHA-256 einer Datei **im kind:1063** definiert. Die
Verwendung im Artikel-Event ist eine edufeed-Absprache vom 07.09.2026. Robuster waere die von
NIP-94 fuer den `image`-Tag bereits vorgesehene Form `["image", <url>, <hash>]`. Aenderbar ist
das nur gemeinsam mit edufeed, da ArticleView und Hub auf der jetzigen Form aufsetzen.

### NIP-94-Abweichungen unserer 1063-Events

NIP-94 fuehrt `url`, `m` und `x` als **required**. `bilder.ts` setzt `m` und `size` aber nur,
wenn die Datei bekannt ist — fehlt die Bilddatei im Post-Ordner, entsteht ein 1063 **ohne
`m`** und verletzt die Spezifikation. Beim Neubau: `m` aus der URL-Endung ableiten, wenn die
Datei fehlt, sonst den Nachweis gar nicht erst schreiben. Nicht standardisiert (aber erlaubt)
sind zusaetzlich `title`, `license`, `credit`, `authorUrl`, `modification`, `ai`; `alt` und
`summary` sind NIP-94-konform.

### Datenlage (alle 98 Posts gemessen)

| | Anzahl |
|---|---|
| Posts mit `# bilder`-Block | 16 |
| Posts mit mindestens einer Blossom-Hash-URL | **16** — nur hier tut der Blossom-Schritt überhaupt etwas |
| Cover-Bilder (`commonMetadata.image`) | 80 — davon 15 Blossom, 64 andere URLs (65× `oer.community`), 1 relativ |
| Fließtextbilder | 236 — davon 25 Blossom, **197 relative Pfade** |

Live-Beleg: Der Publisher `5a12b41e…` hat am 07.09.2026 das Event
`rueckblick-auftaktkonferenz-oer-im-blick` publiziert, dessen Inhalt `![…](OER-im-Blick-2.jpg)`
enthält — ein relativer Pfad. Auf der Hugo-Website funktioniert das (Page Bundle), in einem
Nostr-Client nicht.

### Entscheidung: nur protokollieren

Der Sync **ändert am Bildverhalten nichts** — konsistent zur Schlagwort-Entscheidung: erst
sichtbar machen, dann in einer eigenen Ausbaustufe beheben. Protokolliert wird pro Post:

| Fall | Meldung |
|---|---|
| Relative Bildpfade im Content | „N relative Bildpfade — im Nostr-Event nicht auflösbar" |
| Absolute Nicht-Hash-URLs | „N Bilder ohne Blossom-Hash — kein Lizenznachweis möglich" |
| Hash-URL ohne `# bilder`-Eintrag oder ohne `licenceUrl` | „kein Nachweis für <hash>" (wie bisher) |
| Hash-URL, Blob fehlt und keine Datei mit dem Hash im Ordner | „Blob fehlt auf Blossom" (wie bisher) |

Auch hier gilt: **kein Fehler, kein Abbruch** — ein Datenqualitäts-Signal für die Redaktion.

## Fremde Pubkeys: nur melden, nichts ändern

Zum Slug `rueckblick-auftaktkonferenz-oer-im-blick` liegen zwei 30023-Events von zwei
verschiedenen Pubkeys auf dem Relay: unseres (`5a12b41e…`) und ein älteres (`5491c218…`) mit
absoluten `news.rpi-virtuell.de`-URLs. Technisch kollidieren sie nicht, weil der Pubkey Teil
der Adresse `kind:pubkey:d` ist — Leser*innen sehen den Beitrag aber doppelt.

**Festlegung:**

- Der Sync publiziert **ausschliesslich unter unserem Pubkey** (`AUTHOR_PUBKEY_HEX`, signiert
  ueber den Bunker). Events fremder Pubkeys werden nie ueberschrieben, geloescht oder sonstwie
  angefasst — das ist kryptografisch ohnehin unmoeglich.
- Der Idempotenz-Check fragt deshalb **immer mit `-a <unser-pubkey>`** ab. Ein fremdes Event
  zum selben `d`-Wert darf niemals als bereits publiziert durchgehen.
- Findet der Sync zu einem Slug zusaetzlich Events **anderer** Pubkeys, meldet er das in der
  Job-Summary: `Slug X existiert auch unter Pubkey Y (created_at Z)`. Rein informativ, kein
  Fehler, keine Aktion.
- Ob und wie alte Publisher bereinigt werden, ist eine eigene redaktionelle Frage ausserhalb
  dieses Umbaus.

## Wie Events eindeutig wiedererkannt werden

Grundlage des Idempotenz-Checks:

**30023 und 30142** sind *addressable/replaceable events* (Kind 30000–39999). Identität ist
ein Dreier-Tupel, nicht ein einzelner Tag:

```
kind : pubkey : d-Wert          z.B.  30023:5a12b41e…aedf:just-calling-it-open-is-not-enough
```

- Der `d`-Tag allein ist **nicht** eindeutig — erst zusammen mit `kind` und `pubkey`. Genau
  deshalb duerfen 30023 und 30142 denselben `d`-Wert tragen.
- **Der `a`-Tag hat mit der Identitaet nichts zu tun.** Laut nostrbook ist 30023 *Addressable*
  allein durch den Kind-Bereich 30000-39999 plus `d`-Tag; der `a`-Tag ist dort als *optional*
  gelistet und bedeutet *Referenced addressable events* — ein Zeiger auf ein **anderes**
  Event. In unseren Events existiert er nur als Querverweis 30023 <-> 30142 mit den
  edufeed-eigenen Markern `amb-metadata` / `content`.
- Ein neues Event mit demselben Tupel **ersetzt** das alte; das Relay behält nur das jüngste.
- Der `d`-Wert ist das letzte Pfadsegment von `commonMetadata.id`. **Damit ist das `id`-Feld
  der Identitätsanker.** Wird es geändert, entsteht ein neues Event und das alte bleibt als
  Waise auf dem Relay.

**1063** ist ein *regular event* — nicht ersetzbar, keine Adresse. Wiedererkennung nur über
die Kombination `pubkey` + `x`-Tag (SHA-256 des Bildes), wobei das **jüngste `created_at`
gewinnt**. Das Relay behält alle 1063 zum selben Hash — deshalb muss vor dem Publizieren
verglichen werden, sonst sammeln sich Duplikate.

Die Event-`id` ist global eindeutig, ändert sich aber bei jedem Republish — als
Wiedererkennung für „derselbe Post" unbrauchbar.

## Architektur

Sechs Module unter `scripts/nostr-sync/`, jedes mit einem Zweck, je ein `test_*.py` daneben.

| Modul | Zweck | Seiteneffekte |
|---|---|---|
| `sync.py` | Einstieg/CLI: Argumente, Orchestrierung, Exit-Code | ruft die anderen |
| `frontmatter.py` | Markdown lesen, Blöcke zerlegen, **Pydantic-Schema validieren**, Schlagwort-Abweichungen erkennen | keine (rein) |
| `events.py` | Metadaten → Event-Dicts für die drei Kinds; `tags_equal()`; Spec-Checks | keine (rein) |
| `images.py` | Bild-Hashes aus Frontmatter+Content sammeln, Blossom-Schritt orchestrieren | via `nak.py` |
| `nak.py` | **Die einzige Stelle mit `subprocess`-Aufrufen** — die austauschbare Grenze | ja |
| `summary.py` | GitHub-Step-Summary-Markdown rendern (inkl. Protokolle) | keine (rein) |

**Warum `nak` gekapselt wird:** Fällt `nak` weg oder ändert Flags, tauscht man dieses eine
Modul gegen eine Bibliothek (`nostr-tools`/`nostr-sdk`) — ein Tagewerk, kein Rewrite. Die
Domänenlogik (Frontmatter → Nostr-Tags), der einzige projektspezifische Teil, bleibt
unberührt. Keine weiteren Abstraktionsschichten: insbesondere **kein**
Dependency-Injection-Gerüst wie `BilderDeps`/`standardDeps` im heutigen Code — Tests laufen
gegen einen echten lokalen Relay.

### Datenfluss

```
Workflow-YAML
  ├─ push:   git diff --name-only <before>..<sha> -- Website/content  → geänderte index.md
  └─ manual: --all                                                    → alle index.md
       ↓ Pfade als Argumente
sync
  pro Post:
    1. frontmatter  →  { metadata, bilder, content } + Schema-Validierung
                       + Schlagwort-Abweichungen protokollieren (ohne Wirkung auf das Event)
    2. events       →  30023  [+ 30142 wenn type == LearningResource]
    3. nak req      →  bestehendes Event vom Relay holen
    4. tags_equal   →  identisch? → skip "unchanged"
    5. nak event    →  signieren + publishen, EIN Aufruf pro Relay (ein Exit-Code pro Relay)
    6. images       →  pro Bild: nak blossom check → ggf. upload
                       → 1063 bauen, gegen jüngsten Nachweis vergleichen, ggf. publishen
    7. Ergebnis sammeln
  → summary → GITHUB_STEP_SUMMARY
  → Exit-Code ≠ 0, wenn ein ausgewählter Post nicht nachweislich auf den Relays liegt
```

Der Git-Diff ist damit nur **Performance-Vorfilter**, nicht Korrektheits-Mechanismus. Ein
Lauf mit `--all` muss zum selben Ergebnis führen.

### Idempotenz je Event-Typ

| Kind | Abfrage | Regel |
|---|---|---|
| 30023 | `nak req -k 30023 -a <pubkey> -d <slug> <relay>` | replaceable → Tag-Sets vergleichen, bei Gleichheit skip. **`-a` ist Pflicht**, sonst gilt ein fremdes Event faelschlich als publiziert |
| 30142 | `nak req -k 30142 -a <pubkey> -d <slug> <amb-relay>` | dito |
| 1063 | `nak req -k 1063 -a <pubkey> -t x=<hash> <relay>` | nicht replaceable → jüngsten holen, vergleichen, nur bei Abweichung neu publizieren |

Verglichen werden **nur Tags und `content`**, nie `created_at`/`id`/`sig`. Dieselbe Regel,
die `mdparser/sync/core/bilder.ts:nachweisGleich` heute schon für 1063 anwendet — hier auf
alle Kinds verallgemeinert.

## Schweregrade: Spezifikationsverletzungen brechen ab

Drei Stufen, klar getrennt nach *wer* die Regel aufgestellt hat:

| Stufe | Ausloeser | Verhalten |
|---|---|---|
| **FEHLER** | **Spezifikationsverletzung** (NIP/BUD) oder Betriebsfehler | Event wird **nicht publiziert**. Post gilt als fehlgeschlagen. Job-Exit != 0. In der Summary ganz oben als `> [!CAUTION]`-Block mit Datei, Feld und verletzter Regel |
| **WARNUNG** | Verletzung **unserer eigenen** Konventionen | Wird publiziert, aber mit eigenem, sichtbarem Abschnitt in der Job-Summary (`> [!WARNING]`) |
| **HINWEIS** | Datenqualitaet, informativ | Zeile im Log-Artefakt |

**Warum eine Spezifikationsverletzung nicht publiziert werden darf:** 30023 und 30142 sind
*replaceable*. Ein fehlerhaftes Event **ersetzt die bisher funktionierende Version** auf dem
Relay und liegt dort dauerhaft. Ein kaputtes Event zu publizieren ist damit schlechter, als
gar nichts zu tun — es zerstoert einen guten Stand.

**Kein Abbruch des ganzen Laufs:** Der betroffene Post wird uebersprungen, die uebrigen laufen
weiter, am Ende steht der Exit-Code != 0. Sonst blockiert ein einziger kaputter Post alle
nachfolgenden.

### Prueflisten

**Spezifikations-Checks vor dem Signieren (Verstoss = FEHLER):**

| Regel | Quelle |
|---|---|
| Alle Tag-Werte sind Strings — kein Date-Objekt, keine Zahl, kein `null` | NIP-01 |
| `d`-Tag vorhanden und nicht leer | NIP-01 (addressable) |
| `published_at` ist eine positive Ganzzahl als String (nie `NaN`, nie leer) | NIP-23 |
| `datePublished` liegt strikt als `YYYY-MM-DD` vor | intern, siehe Fallstrick 3 |
| kind:1063 hat `url`, `m` **und** `x` | NIP-94 (alle drei *required*) |
| `x` ist genau 64 Hex-Zeichen in Kleinschreibung | NIP-94 |
| `a`-Tag-Wert hat die Form `kind:pubkey:d` | NIP-01 |
| `content` ist ein String | NIP-01 |

**Konventions-Checks (Verstoss = WARNUNG):** Schlagworte im falschen Block, Schlagwort-Felder
weichen voneinander ab, relative Bildpfade, Bild-URL ohne Blossom-Hash, Hash-URL ohne
`# bilder`-Eintrag oder ohne `licenceUrl`, Slug existiert zusaetzlich unter fremdem Pubkey.

### Drei Fallstricke, empirisch bestaetigt

Alle drei wuerden heute unbemerkt durchgehen — sie sind der Grund fuer die Spec-Checks oben:

1. **YAML-Autotyping macht aus Datumsangaben Objekte.** `datePublished: 2026-08-12`
   (ohne Anfuehrungszeichen) liefert mit Denos `@std/yaml` ein **`Date`-Objekt**, nicht den
   String `"2026-08-12"`. Im Tag stuende dann `"2026-08-12T00:00:00.000Z"` — oder das Event
   waere gleich ungueltig. Dass die Live-Events heute sauber aussehen, liegt allein daran,
   dass `mdparser` das npm-Paket `yaml` nutzt, das Zeitstempel als String zurueckgibt.
   **Die YAML-Bibliothek ist also keine neutrale Wahl.** Das `frontmatter`-Modul muss alle
   Werte explizit zu Strings normalisieren und nicht-konvertierbare ablehnen.
2. **Zahlen in Listen bleiben Zahlen.** `keywords: [2026, Bibel]` ergibt `[2026, "Bibel"]` —
   ein numerischer Tag-Wert verletzt NIP-01.
3. **`Date.parse` raet stillschweigend falsch.** `Date.parse("12.08.2026")` — gemeint als
   12. August — ergibt den **7./8. Dezember 2026**. Vier Monate daneben, ohne jede Meldung.
   `Date.parse("")` ergibt `NaN`, und `String(NaN/1000)` schreibt woertlich `"NaN"` in den
   `published_at`-Tag. Deshalb: striktes `YYYY-MM-DD`-Parsing, kein `Date.parse` als Fallback.

### Fehlerbehandlung — der „silent no-op"-Fix

Kernregel: **Jeder ausgewählte Post muss in genau einem von zwei Zuständen enden** —
„publiziert (mit ≥ `MIN_RELAY_ACKS` Bestätigungen)" oder „nachweislich unverändert auf dem
Relay". Alles andere ist ein harter Fehler mit Exit-Code ≠ 0.

- `nak`-Exit-Code ≠ 0 pro Relay → wird gezählt; `acks < MIN_RELAY_ACKS` (2) → Post gilt als
  fehlgeschlagen.
- **Relay bei der Idempotenz-Abfrage nicht erreichbar → harter Fehler.** Nicht „dann
  publiziere ich sicherheitshalber" (Spam) und nicht „dann nehme ich unverändert an"
  (stiller Verlust).
- Schema- und Spezifikationsverletzungen → Post wird nicht publiziert, Grund als
  `> [!CAUTION]`-Block in der Summary, Exit-Code != 0.
- Konventionsverletzungen (Schlagworte, Bilder) → **sichtbare Warnung**, aber publiziert.

Damit wird der Fall, den `summary.ts` heute nachträglich meldet, strukturell unmöglich.

## Kritische Dateien

**Neu:**
- `scripts/nostr-sync/` — die sechs Module oben plus Tests
- optional `docs/superpowers/specs/2026-09-14-md-to-nostr-neu-design.md` (Design im Repo)

**Umbauen:**
- `.github/workflows/nostr-sync.yml` — externes `mdparser`-Checkout entfernen; `nak`-Binary
  in gepinnter Version + Checksum installieren; geänderte Pfade per `git diff --name-only`
  ermitteln und als Argumente übergeben; `--all` bei `workflow_dispatch`. Secrets bleiben:
  `BUNKER_URL`, `AUTHOR_PUBKEY_HEX` (für `a`-Tags und 1063-Abfragen), `CLIENT_SECRET_HEX`
  (→ `nak --connect-as`).

**Als Referenz lesen (nicht kopieren):**
- `docs/nostr-events/kind-30023.md`, `kind-30142.md`, `kind-1063.md` — dokumentierte
  Feld-Mappings plus echte Live-Events, dienen als Golden Fixtures
- `Orga/oer-community-webseite-orga/wissensgrundlagen/schlagworte.yaml` — kanonische
  Schlagwortliste (50 Begriffe) und die dokumentierte Konvention
- `Website/content/de/posts/2026-08-12-Just-calling-it-open-is-not-enough/index.md` —
  Referenz-Frontmatter mit drei Creators
- `Website/content/de/posts/2026-06-25-Personal-Learning-Environments/index.md` — der
  einzige Post mit abweichenden Schlagwort-Listen (Testfall Fall C)
- `Website/content/de/posts/2026-03-03-OER-erstellen/index.md` — Sonderfall: **keine**
  Block-Marker, ganzes Frontmatter gilt als commonMetadata (Testfall für den Parser)

## Domänenwissen aus `mdparser` übernehmen

Nicht den Code portieren, aber diese Regeln sind hart erarbeitet und müssen erhalten bleiben
(Quelle: `github.com/edufeed-org/mdparser`, Ordner `sync/`):

| Quelle | Zu übernehmende Regel |
|---|---|
| `core/parser.ts` | Block-Marker-Logik, `extractSlug` (Slug = letztes Pfadsegment von `id`) |
| `events/article.ts` | `hashAusUrl` (SHA-256 aus Blossom-URL); Cover-`x` zuerst, direkt nach `image`; Fließtextbilder dedupliziert; **kein** `x` bei URL ohne Hash im Pfad |
| `events/amb.ts` | Reihenfolge und Namen der `creator:*`-Tags; `license:id`, `about:id`, `learningResourceType:id`, `educationalLevel:id` |
| `core/bilder.ts` | `nachweisEvent`-Tag-Mapping (`title`/`license`/`credit`/`alt`/`source`/`authorUrl`/`modification`/`p`/`ai`); `licenceUrl` ist Pflicht; KI-Werte nur `generated`/`modified` |
| `core/validation.ts` | Pflichtfelder (`id`, `name`, `description`, `license`, `creator`, `inLanguage`, `datePublished`); `id` muss mit `https://oer.community/` beginnen |
| `core/summary.ts` | `isSilentNoop`-Idee, Aufbau der Job-Summary, Relay-ohne-Bestätigung-Abschnitt |

## Teststrategie

1. **Unit (rein):** Block-Zerlegung inkl. Edge-Cases (kein Marker vorhanden, fehlender
   `# bilder`-Block, auskommentiertes Frontmatter); **Schlagwort-Abweichungserkennung**
   (Fälle A–D); Event-Builder (Tag-Reihenfolge, `x`-Tags dedupliziert und Cover zuerst,
   kein 30142 ohne `LearningResource`); `tags_equal`; Summary-Rendering.
2. **Golden-Fixture-Regression:** Aus dem Referenz-Post die Events bauen und gegen die
   Live-Tag-Sets aus `docs/nostr-events/` vergleichen (`created_at`/`id`/`sig` ausgenommen).
   Muss **Byte-gleiche Tag-Sets** ergeben — das Publikationsergebnis ändert sich nicht.
3. **Integration, offline:** `nak serve --blossom --port 10547` starten, mit Wegwerf-Key
   (`nak key generate`) gegen `ws://localhost:10547` publishen, mit `nak req` verifizieren;
   zweiter Lauf muss „unchanged" ergeben. Kein Mocking, kein DI-Gerüst nötig.
4. **Schema-Validierung:** Fehlplatzierte oder unbekannte Felder erzeugen einen klaren,
   benannten Hinweis in der Summary statt still zu verschwinden.

## Was wegfällt

- Checkout des externen `edufeed-org/mdparser`-Repos
- Eigenes Change-Detection-Modul → eine Zeile `git diff` in der Workflow-YAML
- DI-Gerüst (`BilderDeps`, `standardDeps`) → echter lokaler Relay in Tests
- Eigener Signer-, Relay- und Blossom-Code → `nak`
- Der komplette `applesauce`-Abhängigkeitsbaum

## Vorab-Checks gegen `nak serve` — erledigt (nak v0.17.3)

| Frage | Ergebnis |
|---|---|
| Füllt `nak event` bei einem Teil-Event auf stdin `pubkey`/`id`/`sig`? | **Ja.** Wir liefern nur `kind`, `tags`, `content`. Tags bleiben in exakt der übergebenen Reihenfolge erhalten. |
| Wird ein falsch gesetzter `pubkey` überschrieben? | **Ja**, durch den Pubkey des Signers — kein Mismatch-Risiko. |
| Bleibt ein selbst gesetztes `created_at` erhalten? | **Ja.** Weglassen = jetzt. Wir lassen es weg. |
| `nak blossom check` | Blob fehlt → **Exit 2** + klare stderr-Meldung; vorhanden → Exit 0, Hash auf stdout. |
| `nak blossom upload` | Erfolg → Exit 0 + **JSON-Blob-Descriptor** auf stdout (`url`, `sha256`, `size`, `type`, `uploaded`) — maschinenlesbar. |
| `nak req -k 1063 -a <pub> -t x=<hash>` | Findet den Nachweis wie erwartet, Exit 0. |
| Publish-Rückmeldung | Exit 0, stderr `publishing to ws://… success.` je Relay. |

**Wichtige Fallstricke für das `nak`-Modul:**

1. **stdin muss bei JEDEM Aufruf explizit gesetzt werden.** Erbt `nak` ein Nicht-TTY-stdin
   (wie in jedem Skript-Subprozess), hält es das für eine Pipe und bricht ab:
   `do not pass arguments when piping from stdin` (Exit 1). Also: Event-JSON für `nak event`,
   `/dev/null` für alle anderen Aufrufe.
2. **`-s/--server` und `--sec` gehören an das Elternkommando `nak blossom`**, vor das
   Unterkommando: `nak blossom -s <url> --sec <key> upload <datei>`.

## Stand der Umsetzung

Bereits angelegt (vor dem Zurückwechseln in den Plan-Modus):

- `scripts/nostr-sync/.venv/` — projektlokale venv mit `pydantic`, `PyYAML`, `pytest` (gitignored)
- `scripts/nostr-sync/requirements.txt` — gepinnte Abhängigkeiten
- `.gitignore` — Einträge für venv, `__pycache__`, `.pytest_cache`

Noch kein Produktivcode. Die Umsetzung folgt testgetrieben (Test schreiben → scheitern sehen →
minimal implementieren), Modul für Modul in dieser Reihenfolge:

1. `frontmatter.py` — Blockzerlegung, Pydantic-Schema, String-Normalisierung, Schlagwort-Abweichungen
2. `events.py` — die drei Event-Builder, `tags_equal`, Spec-Checks
3. `nak.py` — Subprozess-Grenze (gegen `nak serve` getestet)
4. `images.py` — Hash-Ermittlung und Blossom-Schritt
5. `summary.py` — Job-Summary mit den drei Schweregraden
6. `sync.py` — Orchestrierung, Exit-Code
7. `.github/workflows/nostr-sync.yml` — Umbau zum Schluss

## Diesen Plan als Spec ins Repo schreiben

Der Plan liegt bisher nur unter `~/.claude/plans/` und ist damit weder für das Team sichtbar
noch versioniert. Er wird als Markdown-Dokument ins Repo übernommen, damit die getroffenen
Entscheidungen samt Begründung und Messdaten nachvollziehbar bleiben — insbesondere die
Befunde zu Schlagworten (60 Posts), Bildern (197 relative Pfade) und den drei
Spezifikations-Fallstricken.

**Zwei Dateien:**

1. `docs/superpowers/specs/2026-09-14-md-to-nostr-sync-neu-design.md` — die vollständige Spec.
   Dieselbe Konvention, die `mdparser` bereits nutzt (dort liegt die Vorgänger-Spec unter
   `docs/superpowers/specs/2026-03-30-md-to-nostr-sync-design.md`).
2. `scripts/nostr-sync/README.md` — kurz: wozu der Ordner da ist, wie man Tests und Dry-Run
   startet, welche Secrets der Workflow braucht, plus Verweis auf die Spec.

Beim Übernehmen zu bereinigen: Die Abschnitte „Stand der Umsetzung" und dieser Abschnitt
selbst gehören nicht in die Spec — sie beschreiben den Arbeitsablauf, nicht das Vorhaben.

## Cutover

1. Neues Skript mit `--dry-run --all` über alle 98 Posts laufen lassen.
2. **Erwartung: „unchanged" für alle Posts.** Das Publikationsergebnis ist identisch zur
   heutigen Lösung — die Schlagwort-Regel wurde absichtlich *nicht* geändert. Jede
   Abweichung ist verdächtig und einzeln zu prüfen. Zusätzlich erwartet: 61
   Schlagwort-Protokolleinträge (60× Fall B, 1× Fall C) sowie die Bild-Protokolle
   (197 relative Pfade, 64 Nicht-Hash-Cover).
3. Erst wenn die Abweichungsliste leer bzw. erklärt ist, die Workflow-YAML umstellen.

## Später: Ausbaustufe 2 — Schlagwort-Übernahme mit Glossar-Abgleich

Separates Skript, eigener PR, **nicht** Teil dieses Umbaus. Aufgabe: die Schlagworte der
60 Posts aus Fall B nach `commonMetadata.keywords` übernehmen, damit sie nach Nostr gelangen.

Vorgehen:
1. Quelle wählen: Fehlt `commonMetadata.tags`, aber `staticSiteGenerator.keywords`/`tags` ist
   gefüllt, dann von dort übernehmen (und umgekehrt).
2. **Gegen das Glossar abgleichen** (`Orga/oer-community-webseite-orga/wissensgrundlagen/schlagworte.yaml`,
   50 kanonische Begriffe). Befund der Vorab-Analyse: von 93 tatsächlich verwendeten Begriffen
   sind **44 nicht im Glossar**. Darunter:
   - reine Schreibweisen-Abweichungen, z. B. `Dezentral` vs. kanonisch `dezentral`
   - ein **leerer** Schlagwort-Eintrag (irgendwo ein leeres Listenelement)
   - inhaltlich neue Begriffe (`Bildungsinfrastruktur`, `Interoperabilität`, `Edufeed`,
     `Künstliche Intelligenz`, …), über die redaktionell entschieden werden muss:
     ins Glossar aufnehmen oder auf einen bestehenden Begriff abbilden
3. `Orga/oer-community-webseite-orga/wissensgrundlagen/schlagwort-glossar.md` enthält bereits
   redaktionelle Überarbeitungsvorschläge (z. B. „CC-Lizenzen → Creative Commons + Lizenzen",
   „Community-Building → Community") — diese Mapping-Tabelle ist die Grundlage für die
   Normalisierung und sollte maschinenlesbar werden.
4. Ausgabe zuerst als Vorschlag (Diff/Report) zur redaktionellen Prüfung, erst danach
   schreibend über die Content-Dateien.

Erst wenn das gelaufen ist, publiziert der Sync die zusätzlichen `t`-Tags — als normale
Änderung, die der Idempotenz-Check von selbst erkennt.

## Später: Ausbaustufe 3 — Bilder nach Blossom überführen

Separates Vorhaben, eigener PR, **nicht** Teil dieses Umbaus. Ziel: die 197 relativen
Bildpfade und 64 Nicht-Hash-Cover auflösbar und lizenzbelegt machen.

Der eigentliche Engpass ist nicht die Technik, sondern die **Lizenzdaten**: ein `# bilder`-
Eintrag mit `licenceUrl` existiert erst für 16 von 98 Posts. Ohne ihn darf kein kind:1063
entstehen. Das ist redaktionelle Arbeit, kein Skript-Problem — dieselbe Form wie bei den
Schlagworten.

Vorgehen:
1. Inventar: pro Post die Bilddateien im Page-Bundle auflisten, SHA-256 berechnen, mit den
   im Markdown referenzierten Pfaden abgleichen.
2. Lizenzdaten erfassen — hier hilft das bereits vorhandene `docs/bildlizenzgenerator.html`
   („OER Bildlizenzgenerator – TULLU+B"), das genau die Felder produziert, die der
   `# bilder`-Block braucht (Titel, Urheber, Lizenz, Link, Ursprungsort, Bearbeitung).
3. Blobs nach Blossom hochladen (`nak blossom upload`), Markdown-Referenzen und
   `commonMetadata.image` auf die Hash-URLs umschreiben.
4. Erst danach publiziert der Sync `x`-Tags und kind:1063 — als normale Änderung, die der
   Idempotenz-Check von selbst erkennt.

Hinweis: In `mdparser/sync/core/bilder.ts` wird ein Werkzeug `md2blossom` erwähnt, das
dieselbe Bild-Regex und Tag-Form verwendet. Falls es existiert, ist es der natürliche
Ausgangspunkt für Schritt 3 — Fundort ist noch zu klären (unter `edufeed-org` öffentlich
nicht auffindbar).

## Verifikation

```bash
# Unit- und Golden-Fixture-Tests
cd scripts/nostr-sync && .venv/bin/python -m pytest -q

# Integrationstest offline
nak serve --blossom --port 10547 &
#   Skript gegen ws://localhost:10547 mit Wegwerf-Key laufen lassen
nak req -k 30023 -d just-calling-it-open-is-not-enough ws://localhost:10547 | jq

# Dry-Run gegen echte Daten, ohne zu publizieren
#   Skript mit --dry-run --all → erwartet: ausschließlich "unchanged"
#                                 + 61 Schlagwort-Protokolleinträge

# Live-Zustand zum Vergleich
nak req -k 30023 -d just-calling-it-open-is-not-enough wss://relay-rpi.edufeed.org | jq '.tags'
nak req -k 30142 -d just-calling-it-open-is-not-enough wss://amb-relay.edufeed.org  | jq '.tags'
```

## Voraussetzung

`nostrbook.dev`-MCP ist eingerichtet (`claude mcp add nostrbook -- npx -y @nostrbook/mcp@latest`),
damit NIP-Spezifikationen (NIP-23, NIP-46, NIP-94, BUD-01) beim Implementieren nachgeschlagen
werden statt aus dem Gedächtnis.
