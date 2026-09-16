# Issue-Entwürfe zum Arbeitsstand 02.–16.09.2026

Zum Gegenlesen. Noch nichts ist gepostet. Überarbeitete Fassung vom 16.09. (die erste vom 11.09. ist mit dem Sitzungsspeicher verschwunden); neu aufgenommen ist die Arbeit vom 14.–16.09.: Hub als „oer.community aus Nostr“, Umbenennung des Repos, Zweisprachigkeit, Kalender, Titelbild und PR für den KI-Beitrag, zweiter Build-Bruch.

Quellen: Git-Verlauf von `FOERBICO_und_rpi-virtuell`, `oer-community` (ehemals `community-hub`, [`docs/STATUS.md`](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/STATUS.md) und ADR-Index), `foerbico-editor`, `mdparser`; GitHub-Actions-Läufe des Nostr-Sync; Wissensgrundlagen unter [`Orga/oer-community-webseite-orga/`](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/src/branch/main/Orga/oer-community-webseite-orga/).

## Zuordnung

Offenes Repo [`Comenius-Institut/FOERBICO_und_rpi-virtuell`](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell) (mit Meilenstein):

| Nr. | Titel (Kurzform) | Meilenstein | Labels |
|---|---|---|---|
| A | Bildnachweise als Standard: `# bilder`-Block, Konvention, kind:1063 | [AP 4-2](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/88) Metadatenstandards weiterentwickeln | nostr, technik, oer.community |
| A' | Kommentar in [#191](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues/191) „Strukturierte Daten für Bilder“ | (hat [AP 4-2](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/88)) | |
| B | Bildmigration der oer.community-Beiträge auf Blossom | [AP 9-4](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/118) OER-Material-Metadaten überarbeiten | oer.community, Blog |
| C | Nostr-Sync: stille Fehlschläge behoben, Backfill, Bilder, Seiten, Listen | [AP 9-2](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/8) Techn. Infrastruktur weiterentwickeln (CI) | nostr, technik, CI |
| D | Redaktionswerkzeuge: md2blossom, blossom-bunker, foerbico-editor | [AP 4-3 + 4-4](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/90) Metadaten-Generator für OEP/OER | technik, nostr, oer.community |
| E1 | Hub: Artikel-Detailansicht mit Lizenznachweis, Demonstrator (02.–10.09.) | [AP 4-5](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/99) OER-Client für OEP/OER-Darstellung entwickeln | Community-Hub, nostr, technik |
| E2 | oer.community aus Nostr: Schaufenster live, Seiten, Feed, Zweisprachigkeit, Termine (14.–15.09.) | [AP 3-2 + 3-3](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/83) Konzept und Einsatz Community-Hub | Community-Hub, nostr, oer.community |
| F | Abstimmung mit edufeed: x-Tags, ai-Tag, Blossom, Lizenz-Relay | [AP 4-2](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/88) Metadatenstandards weiterentwickeln | nostr |
| G | Blogbeitrag „KI im evangelischen Religionsunterricht“ (Wiederveröffentlichung) | [AP 6-3](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/100) Formate OE/OER-Integration ALPIKA-Institute | Blog, oer.community |

Geschlossenes Repo [`Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen`](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen) (dort gibt es keine Meilensteine; AP-Nummer steht im Titel, Labels aus dem Bestand):

| Nr. | Titel (Kurzform) | Labels |
|---|---|---|
| H | [AP 6-3] Wiederveröffentlichung RPI Karlsruhe: Genehmigungen, Titelbild, Kontakt | Konzeption |
| I | [AP 9-4] Bildmigration: Abstimmung im Team, zwei Build-Brüche, Midjourney-Konto | rpi-virtuell |
| J | [AP 4-2] Personen auf Fotos in Bildnachweisen: Einwilligungen prüfen | Priorität/Hoch, Konzeption |
| K | [AP 9-2] Signatur-Infrastruktur: Amber-Bunker, Secrets, lokaler Key, Single Point of Failure | Server, Priorität/Hoch |
| L | [AP 4-2] Offene Fragen an edufeed (persönliche Kommunikation) | Konzeption |
| M | [AP 3-2] Betrieb oer-community: Server, Unit, DNS, Umschalttag | Server |

Offene Punkte für dich stehen am Ende.

---

## A · offen · Bildnachweise als Standard: `# bilder`-Block, Konvention `bildattribution.md`, kind:1063

Meilenstein [AP 4-2](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/88) · Labels nostr, technik, oer.community · Bezug [#191](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues/191)

### Body

Seit dem 07.09.2026 trägt jeder oer.community-Beitrag seine Bildnachweise als dritten markierten Block im Frontmatter von `index.md`. Dieses Issue hält fest, was entschieden ist, und sammelt die nächsten Schritte.

**Stand 16.09.2026**

- Konvention: [`Orga/oer-community-webseite-orga/wissensgrundlagen/bildattribution.md`](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/src/branch/main/Orga/oer-community-webseite-orga/wissensgrundlagen/bildattribution.md). Felder `alt`, `imageUrl`, `title`, `sourceUrl`, `author`, `authorUrl`, `licence`, `licenceUrl`, `modification`, `ai`; Reihenfolge normativ. Caption-Zeile direkt unter dem Bild: `[title](sourceUrl), [author](authorUrl), [licence](licenceUrl), KI-Kennzeichnung, modification`.
- Der `# bilder`-Block ist Eingabe zum Prägen. Wahrheit ist der Lizenznachweis `kind:1063` auf dem Relay, adressiert über den SHA-256 des Bildes (x-Tag). Die Abbildungstabelle Block → 1063-Tags steht in der Konvention.
- Bilder liegen als Blossom-Hash-URL (`https://blossom.edufeed.org/<sha256>.<ext>`) in `commonMetadata.image`, `cover.image` (`relative: false`) und im Fließtext. `felder.yaml` beschreibt Zielform und lokale Übergangsform.
- KI-Kennzeichnung: `ai: generated | modified` nach dem edufeed-Wiki vom 10.09.2026 (EU-AI-Office-Icons), in der Caption als „KI-generiert“ oder „KI-verändert“ hinter der Lizenz. In allen vier Werkzeugen (mdparser/sync, md2blossom, foerbico-editor, oer-community) am selben Tag umgesetzt.
- Lizenzregeln: Eigene Fotos folgen der Footer-Regel (CC BY FOERBICO, `sourceUrl` = der Beitrag). Fremde Werke tragen Urheber:in, Quelle und deren Lizenz. Was nicht frei lizenziert werden darf, bekommt keinen CC-Eintrag.
- Zwei Präzedenzfälle vom 16.09.: rein KI-generierte Bilder erhalten `CC0 1.0` statt CC BY, weil ohne persönliche geistige Schöpfung (§ 2 UrhG) kein Recht einzuräumen ist (KI-im-RU-Beitrag); geschützte Logos erhalten `licence: ©` als Kurzform (hello-world). Beides gehört in die Konvention.
- Abschnitt „Stolpersteine beim händischen Bearbeiten“ (Doppelpunkt mit Leerzeichen, Anführungszeichen, `#`, Einrückung, Schlüssel = exakter Dateiname). Anlass: zwei Hugo-Build-Brüche am 10.09. und 16.09. durch unquotierte `alt`-Texte.

**Commits (Auswahl)**: 240ba8e, 3056ca9, fbc94d2, 3efa594, 9770638; mdparser 820f0d1, 56892f9, 01a4efa.

**Offen**

- [ ] Präzedenzfälle CC0 für KI-Bilder und © für Logos in `bildattribution.md` festschreiben.
- [ ] `content-lint` soll YAML-Gültigkeit und Blossom-Form vor dem Merge prüfen (Entscheidung 09.09.: ersetzt den Regression-Wächter). Zwei Build-Brüche in einer Woche zeigen den Bedarf.
- [ ] Konvention und FOERBICO-Zusatzfelder in die AMB-NIP-Diskussion einbringen ([#794](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues/794)).
- [ ] [#191](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues/191) ist damit beantwortet; Kommentar setzen und schließen.

---

## A' · offen · Kommentar in [#191](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues/191)

> Stand 16.09.2026: Beantwortet. Bildmetadaten stehen beitragsbezogen als `# bilder`-Block im Frontmatter (Konvention `bildattribution.md`), werden von der CI als `kind:1063` mit dem SHA-256 des Bildes publiziert und vom Hub live vom Relay gelesen. Details und offene Punkte in [#840](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues/840). Schema.org-Auszeichnung für Google Images ist damit nicht gemacht, wäre aber aus dem Block ableitbar. Vorschlag: dieses Issue schließen, Rest in [#840](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues/840).

---

## B · offen · Bildmigration der oer.community-Beiträge auf Blossom

Meilenstein [AP 9-4](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/118) (Alternative [AP 9-5](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/16)) · Labels oer.community, Blog

### Body

Alle Bilder der oer.community-Beiträge sollen mit Lizenznachweis auf Blossom liegen. Arbeitsliste mit fertigen Blockvorschlägen je Beitrag: [`Orga/oer-community-webseite-orga/bildmigration.md`](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/src/branch/main/Orga/oer-community-webseite-orga/bildmigration.md). Der Hub zeigt Cover ohne Nachweis seit 15.09. mit „Lizenz ungeklärt“ ([ADR-0032](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/)); Bilder von `oer.community` gelten als unaufgelöst ([ADR-0030](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/)). Damit ist die Migration sichtbar die Redaktionsliste des Hubs.

**Stand 16.09.2026**

| | Zahl |
|---|---|
| Beiträge migriert (auf main) | 16 |
| Bilder mit Nachweis auf Blossom | 24 plus Referenzpost und OERcamp-2026 |
| in Arbeit auf Branch `add-bildlizenzen` | 2 (hello-world, TikTok) |
| Beiträge offen | 70 |
| Bilder offen | 198 |
| Cover im Hub ohne Nachweis | 74 |

Migriert: die-kraft-der-gemeinschaft (Referenzpost), oercamp-2026, tagung-open-education (digiLL), am 10.09. dreizehn weitere: OER-Fachtag-Orca.NRW, OER-erklaert, OERcamp-Hamburg, OER-Brownbag, Raus-aus-den-Bubbles, Git-Treffen-Medienhaus, Austausch-digiLL, Bibel_OER, OER-Werkstatt, Workshop-KlimaOER, Canva, Rechtsfragen-Workshop, IT-Sommercamp-2025.

**So geht ein Beitrag**

1. Blockvorschlag aus `bildmigration.md` ins Frontmatter, Lizenz je Bild prüfen, `alt` und `title` ausfüllen. Werte mit Doppelpunkt oder `#` in Anführungszeichen.
2. `cd Website/scripts && node md2blossom.mjs ../content/de/posts/<ordner> --write` (kein Key nötig). Alternativ der foerbico-editor im Browser.
3. Branch, Pull Request, Merge. Die CI lädt die Blobs hoch und publiziert 1063 und 30023.

**Commits**: 69e28e1, 7cb1096, ea6bd16, 172436b, 6c0a8ae, 1340710, 8e51f83, 3efa594.

**Offen**

- [ ] 70 Beiträge nach Arbeitsliste; Reihenfolge nach der Liste „Lizenz ungeklärt“ im Hub-Blog.
- [ ] Branch `add-bildlizenzen` (hello-world, TikTok) mergen; Arbeitsliste auf Stand 16.09. bringen.
- [ ] OER-Fachtag-Orca.NRW: Cover ist eine externe KI-Bild-URL ohne Datei im Ordner. Datei beschaffen, dann `ai: generated`.
- [ ] Beiträge ohne vollständiges `commonMetadata` (creator, datePublished) übergeht die CI; bei der Migration mitprüfen.
- [ ] Nach Abschluss `workflow_dispatch` mit `force_all`.

---

## C · offen · Nostr-Sync: stille Fehlschläge behoben, Backfill, Bilder, Seiten und Listen in der CI

Meilenstein [AP 9-2](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/8) · Labels nostr, technik, CI

### Body

Die Pipeline [`.github/workflows/nostr-sync.yml`](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/src/branch/main/.github/workflows/nostr-sync.yml) (GitHub-Mirror → `mdparser/sync` → Relays) publiziert Inhalte aus [`Website/content/`](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/src/branch/main/Website/content/) als `kind:30023` und `kind:30142`. Statusbericht 02.–15.09.2026.

**Befund 02.09.**: Die Pipeline lief seit Monaten fast leer, ohne dass es sichtbar war. `keywords` war Pflichtfeld; 74 von 93 Dateien hatten keins und wurden übersprungen. Läufe waren grün, obwohl nichts publiziert wurde.

**Behoben und ausgebaut**

- `keywords` empfohlen statt Pflicht (78 statt 18 Dateien publizierbar). Job-Summary nennt publizierte, übersprungene und fehlgeschlagene Posts; ein Abbruch vor dem Publish-Step erscheint als Warnung (424cbe5, bd82037).
- Backfill `--force-all` am 02.09.: 81 publiziert, 13 übersprungen, 1 fehlgeschlagen (2025-07-07-oer-rel-paed, 131 KB, über der NIP-46-Grenze von 65535 Bytes für die verschlüsselte Signieranfrage; Protokollgrenze, der Post bleibt nur auf der Hugo-Site).
- 07.09.: `x`-Tags aus den Blossom-URLs (Cover zuerst, je Fließtextbild eins, kein `imeta`).
- 09.09.: Bilderschritt in `publish` ([`core/bilder.ts`](https://git.rpi-virtuell.de/Comenius-Institut/mdparser/src/branch/main/sync/core/bilder.ts)): Blob-Upload nach Blossom, wenn die Datei im Ordner liegt; Lizenznachweis aus dem `# bilder`-Block prägen, wenn auf dem Relay keiner oder ein abweichender liegt. Nichts davon blockiert das 30023, Git ist die Wahrheit.
- 10.09.: `ai`-Tag; unbekannter Wert ergibt keinen Tag und eine Warnung.
- 14.09.: Seiten (`type: page`) tragen das Selbst-Label `foerbico/typ=seite` (NIP-32), damit der Hub sie vom Blog trennt; `inLanguage` auch als String akzeptiert (19 Beiträge kamen als Sprache „d“ an). `sync navigation` publiziert Menü und Fußzeile als `kind:30004` aus `Website/navigation.yaml`; `sync redaktion` die Redaktionsliste `kind:30000`. Sieben deutsche Seiten und eine neue `startseite/index.md` publiziert (a362648).
- 15.09.: `workTranslation`/`translationOfWork` werden zum `a`-Tag mit Marker `translation`; drei englische Seiten und `en/startseite` publiziert (8fc3f39).
- Entscheidung 09.09.: kein Regression-Wächter. Ein Schreiber je Beitrag, Review in Git, `content-lint` vor dem Merge.

**Läufe seit 01.09.**: 27 Läufe. Rot: fünf Push-Läufe am 10.09. (09:36–09:40 UTC, ungültiges Frontmatter, ab 09:43 grün) und zwei `force_all`-Läufe (02.09., 07.09.), die am 131-KB-Post abbrechen. Seit 10.09. durchgehend grün.

**Vorfall 07.09.**: Ein Publish-Lauf hat den Referenzpost mit dem alten Git-Stand überschrieben. Konsequenz: Blossom-URLs stehen in Git, das Relay spiegelt Git.

**Offen**

- [ ] 13 übersprungene Dateien (Hugo-Seiten, `_index.md` ohne creator/datePublished): klären, welche als 30023 gehören. Sieben davon sind seit 14.09. als Seiten erledigt.
- [ ] Relay `theforest.nostr1.com` antwortet nicht; ersetzen.
- [ ] `content-lint` für YAML und Blossom-Form.
- [ ] Der Diff-Modus publiziert bei `workflow_dispatch` ohne `force_all` nichts; dokumentieren.
- [ ] Redaktion prüft Beschreibungen und `datePublished` der Seiten (aus Text und erstem Commit abgeleitet).

---

## D · offen · Redaktionswerkzeuge: md2blossom, blossom-bunker, foerbico-editor

Meilenstein [AP 4-3 + 4-4](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/90) · Labels technik, nostr, oer.community

### Body

Drei Werkzeuge, ein Ziel: Ein Beitrag mit Bildern kommt ohne lokalen Nostr-Key nach Git; alles, was den FOERBICO-Key braucht, macht die CI nach dem Merge.

**[`Website/scripts/md2blossom.mjs`](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/src/branch/main/Website/scripts/md2blossom.mjs)** (Node, seit 04.09., Tests `npm test`): hasht Bilder im Beitragsordner, ersetzt relative Pfade durch Blossom-URLs, schreibt Caption nach Konvention und `image`/`cover` um, legt unsignierte 30023/1063-Vorlagen und ein AMB-JSON ab. Bilder ohne Blockeintrag: `TODO:LICENSE`, Exit 2, Blockvorlage wird gedruckt. Kein Upload, keine Signatur.

**[`Website/scripts/blossom-bunker.ts`](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/src/branch/main/Website/scripts/blossom-bunker.ts)** (Deno, seit 09.09.): `upload` (BUD-01, Hash geprüft) und `publish` (1063 signieren) über den NIP-46-Bunker, nur für Sonderfälle seit dem CI-Bilderschritt.

**foerbico-editor** (SvelteKit, statisch, Repo [`Comenius-Institut/foerbico-editor`](https://git.rpi-virtuell.de/Comenius-Institut/foerbico-editor), seit 07.09.): Formular für einen Beitrag mit den drei Blöcken nach `felder.yaml` und `bildattribution.md`. Ausgang: Branch `beitrag/<kürzel>`, Commit, Pull Request unter dem eigenen Forgejo-Konto (persönliches Token). Bilder werden im Browser gehasht; liegt zum Hash ein 1063 auf `relay-rpi.edufeed.org`, werden die Angaben übernommen. Bestehende Beiträge lassen sich laden und migrieren. Am 09.09. wurde der Nostr-Entwurfsweg zugunsten des Git-Wegs entfernt. Woodpecker-Pipeline seit 08.09.

**Offen**

- [ ] Editor: Schriften lokal; Kürzel-Änderung legt neuen Ordner an; Bilddateien überleben ein Neuladen nicht; keine Bildverkleinerung.
- [ ] Wer aus dem Team testet den Editor an einem echten Beitrag? Die beiden Build-Brüche kamen aus dem Forgejo-Webeditor; der foerbico-editor schreibt gültiges YAML.
- [ ] Produktive Adresse des Editors festlegen und in `bildmigration.md` nennen.

---

## E1 · offen · Hub: Artikel-Detailansicht mit Lizenznachweis, Demonstrator „Beitrag live“ (02.–10.09.)

Meilenstein [AP 4-5](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/99) · Labels Community-Hub, nostr, technik

### Body

Repo [`Comenius-Institut/oer-community`](https://git.rpi-virtuell.de/Comenius-Institut/oer-community) (bis 15.09. `community-hub`; [`docs/STATUS.md`](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/STATUS.md) als Logbuch, Entscheidungen als ADR mit Index unter [`docs/entscheidungen/`](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/)). Erster Abschnitt 02.–10.09.: ein Beitrag mit nachgewiesener Bildlizenz als OER-Client-Durchstich.

**Erreicht**

- Artikelseite liest `kind:30023` von den Relays und zu jedem Bild den `kind:1063` über den Hash. Prüfkette in fünf Schritten gibt den Abbruchgrund zurück; „nicht erreichbar“ und „hat nichts“ werden unterschieden ([ADR-0013](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/)/0022).
- Entwickleransicht `…/json`: Beitrag und Nachweis nebeneinander mit lieferndem Relay und Prüfschritten ([ADR-0017](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/)).
- Bildlizenz wie edufeed, Attribution nach eigener Konvention: Bild immer ausgeliefert, Lizenzstand daran; Alt-Text aus dem `alt`-Tag ([ADR-0022](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/)). Fließtextbilder mit Hash-URL aufgelöst, hashlose entfernt ([ADR-0023](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/)/0015). KI-Marke aus dem `ai`-Tag ([ADR-0025](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/)).
- Designsystem in der Detailansicht: lokale Schriften, Kontrastwerte als Test ([ADR-0018](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/), später durch [ADR-0031](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/) ersetzt).
- Redaktionsmodell [ADR-0021](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/) (Entwürfe unter Redaktions-Keys, Freigabe per NIP-32-Label, FOERBICO-Key nur durch `sync adopt`), Status offen; [`docs/redaktion-longform.md`](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/redaktion-longform.md).
- Auslieferung rootlos, Dienst auf 127.0.0.1; Woodpecker-Pipeline seit 09.09.
- Demonstrator [`docs/beitrag-live.html`](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/src/branch/main/docs/beitrag-live.html) in diesem Repo (07.09.): eine HTML-Datei ohne Build, Beitrag mit Nachweisen live vom Relay, `?d=<slug>`.

**Offen**

- [ ] [ADR-0024](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/) (Vorrang des eigenen Keys bei konkurrierenden Nachweisen) umsetzen.
- [ ] [ADR-0021](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/) im Team bestätigen; Nachtrag zu Entwürfen (30024) liegt ungespeichert vor.
- [ ] Prüfwerkzeug für die Redaktion: Welche Beiträge tragen Bilder ohne Nachweis? Seit [ADR-0032](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/) im Blog sichtbar, eine Liste fehlt.

---

## E2 · offen · oer.community aus Nostr: Schaufenster live, Seiten, Feed, Zweisprachigkeit, Termine (14.–15.09.)

Meilenstein [AP 3-2 + 3-3](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/83) · Labels Community-Hub, nostr, oer.community

### Body

Zweiter Abschnitt im Repo [`Comenius-Institut/oer-community`](https://git.rpi-virtuell.de/Comenius-Institut/oer-community). Entscheidung [ADR-0026](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/): Das Vorhaben ist oer.community aus Nostr, FOERBICO statt relilab als Zuschnitt. Der eigentliche Community-Hub kommt später, auf den Erfahrungen dieses Schaufensters (Teambesprechung 15.09.).

**Erreicht, live unter `community-hub.rpi-virtuell.net` seit 14.09., 19:03 Uhr**

- Spiegel im Prozess statt Live-Abfrage ([ADR-0028](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/)): lädt 87 Artikel in rund 2 Sekunden, Standdatei auf der Platte, Architekturtest verbietet Relay-Zugriff außerhalb des Spiegels. Adressen sind das `d` des Beitrags, `naddr` leitet weiter ([ADR-0029](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/)).
- Seitenstruktur aus Nostr ([ADR-0027](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/)): Seiten per Selbst-Label, Menü und Fußzeile als Kuratierungslisten `kind:30004`, Startseite als Seite mit `d = startseite`, Profil-`about` als Fußtext. Blog und Themen als Ansichten.
- FOERBICO-Designsystem ([ADR-0031](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/), [`docs/designsystem.md`](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/designsystem.md)), Feed `application/rss+xml`, Sitemap, kanonische URLs auf `https://oer.community/…`.
- Lizenzpille ([ADR-0032](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/)): Lizenzstand als Overlay auf jedem Bild, auch in der Übersicht; Cover ohne Nachweis erscheinen mit „Lizenz ungeklärt“. Bilder von `oer.community` gelten als unaufgelöst ([ADR-0030](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/)).
- Zweisprachig DE/EN ([ADR-0033](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/), offen): `/en` als englische Startseite, Umschalter, `hreflang`, Übersetzungen als `a`-Tag mit Marker `translation`. Live geprüft am 15.09.
- Termine aus der Community ([ADR-0034](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/)): Quelle je Inhaltsart, Artikel und Seiten vom FOERBICO-Key, Termine (`kind:31922/31923`) aus der Communikey-Community rpi-virtuell mit `h`-Tag und Redaktionskreis (`kind:30000`); Seite `/termine`, „Nächste Termine“ auf beiden Startseiten. Erster Termin: Abschlusstagung „Offen. Vernetzt. Zukunft.“ (2.–3. Februar 2027, Frankfurt).
- Repo am 15.09. in `oer-community` umbenannt ([ADR-0011](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/)-Nachtrag). 422 Tests grün, `pnpm check` ohne Befund.

**Offen**

- [ ] [ADR-0033](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/) und [ADR-0034](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/) in der nächsten Besprechung bestätigen.
- [ ] Redaktion: Seitenbeschreibungen (abgeleitet), doppelte Überschrift auf der Startseite, Profil-`about`, Startseiten-Logos (relative Pfade, im Hub unsichtbar).
- [ ] Umschalttag oer.community → Hub festlegen (Cut-over-Bedingungen in [`redaktion-longform.md`](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/redaktion-longform.md)).
- [ ] Dunkelmodus, Logo bewusst offen gelassen.
- [ ] Betrieb nach Umbenennung: Server-Verzeichnis, Unit, DNS `oer-community.rpi-virtuell.net`, `.woodpecker.yml`, [`docs/betrieb.md`](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/betrieb.md) (Details im geschlossenen Repo).

---

## F · offen · Abstimmung mit edufeed: x-Tags, ai-Tag, Blossom-Freischaltung, Lizenz-Relay

Meilenstein [AP 4-2](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/88) · Labels nostr · Bezug [#794](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues/794)

### Body

Sammelissue für die Schnittstellen zu edufeed (Relays, Blossom, Wiki `license-events-nope`, edufeed-app). Persönliche Kommunikation liegt im geschlossenen Repo.

**Geklärt**

- 07.09.: Bild-Hashes als wiederholte `x`-Tags am 30023, kein `imeta`. Umgesetzt in mdparser und Hub.
- 10.09.: `ai`-Tag am 1063 (`generated | modified`, Wiki-Fassung 10.09.). Alle FOERBICO-Werkzeuge am selben Tag nachgezogen; die edufeed-app zeigt die Marke vor dem Lizenzkürzel, wir hinter dem Lizenz-Link.
- Lizenznachweise liegen auf `relay-rpi.edufeed.org` und `relay.edufeed.org`; Blossom `blossom.edufeed.org`; Upload mit dem FOERBICO-Key funktioniert (CI seit 09.09.).
- Termine kommen aus der Communikey-Community rpi-virtuell der edufeed-app (`kind:31922`, [ADR-0034](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/)).
- `relay-rpi.edufeed.org` war am 03./07.09. vorübergehend nicht erreichbar (Platte voll), seither stabil.

**Offen**

- [ ] `PUT /mirror` (BUD-04) auf Blossom für `sync adopt`.
- [ ] Bunker-Modell für Redaktions-Keys ([ADR-0021](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/)).
- [ ] Nimmt `relay.edufeed.org` dauerhaft 1063 an?
- [ ] Umschalttag oer.community → Hub gemeinsam festlegen.
- [ ] Konvention `bildattribution.md` und Zusatzfelder (`authorUrl`, `modification`) ins Wiki ([#794](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues/794)).

---

## G · offen · Blogbeitrag „Künstliche Intelligenz im evangelischen Religionsunterricht“ (Wiederveröffentlichung als OER)

Meilenstein [AP 6-3](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/100) (Alternative [AP 4-7](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/101)) · Labels Blog, oer.community · Bezug PR [#838](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues/838)

### Body

Branch `add-blogpost-ki-ru-baden`, PR [#838](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues/838) (WIP). Beitrag von Olav Richter (RPI Karlsruhe), zuerst in den Badischen Pfarrvereinsblättern 7/2026, mit Genehmigung von Autor und Redaktion unter CC BY 4.0 wiederveröffentlicht. Rund 4.900 Wörter. Erster Beitrag eines ALPIKA-Instituts, der als OER auf oer.community nachnutzbar wird.

**Stand 16.09.2026**

- 11.09.: Text übernommen, Frontmatter nach `felder.yaml`, `isBasedOn` auf die Erstveröffentlichung (af370ee).
- 16.09.: Titelbild vom Autor (KI-generiert, 13.09.), `# bilder`-Block gefüllt, `ai: generated`. Lizenz des Bildes `CC0 1.0`, weil rein maschinell erzeugte Bilder keine persönliche geistige Schöpfung nach § 2 UrhG sind; der Text bleibt CC BY 4.0 (9770638). Erster Nachweis mit `ai: generated` im Bestand.
- `creativeWorkStatus` noch `Draft`.

**Offen**

- [ ] Review gegen die Druckfassung (Fußnoten, Zitate).
- [ ] `md2blossom --write`, `creativeWorkStatus: Published`, PR [#838](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues/838) aus WIP nehmen, Merge. Die CI publiziert.
- [ ] Autor informieren; Beitrag über die ALPIKA-Kanäle streuen.

---

# Geschlossenes Repo

## H · [AP 6-3] Wiederveröffentlichung RPI Karlsruhe: Genehmigungen, Titelbild, Kontakt

Label Konzeption · Bezug: offenes Issue G, PR [#838](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues/838)

- Genehmigung zur Wiederveröffentlichung unter CC BY 4.0 von Olav Richter (Autor, Studienleitung Medienpädagogik, RPI Karlsruhe) und von der Redaktion der Badischen Pfarrvereinsblätter (Dr. Kunath). **Bitte ergänzen**: Datum und Form (Mail, Gespräch), Ablageort.
- 13.09.: Titelbild vom Autor geliefert (mit ChatGPT erzeugt). Auf Wunsch des Autors wurde der Name der Redaktion aus dem öffentlichen Wiederveröffentlichungshinweis entfernt (9770638); die Genehmigung selbst bleibt hier dokumentiert.
- Autorenangabe im Frontmatter: `authorUrl` zeigt auf `rpi-baden.de`. Eintrag in `personen.yaml`?
- Nach Veröffentlichung: Link an Autor und Redaktion, Dank.

## I · [AP 9-4] Bildmigration: Abstimmung im Team, zwei Build-Brüche, Midjourney-Konto

Label rpi-virtuell · Bezug: offenes Issue B

- Gina arbeitet im Forgejo-Webeditor auf Branch `add-bildlizenzen`: 10.09. zehn Beiträge (gemerged), 11.09. TikTok, 16.09. hello-world (offen).
- Zwei Build-Brüche durch unquotierte `alt`-Texte mit „: “: 10.09. Canva („Ausweis: Canva-Lizenz“, fünf rote CI-Läufe), 16.09. hello-world („Das FOERBICO Team: Phillip, …“). Jörg hat beide repariert (3efa594) und den Abschnitt „Stolpersteine“ ergänzt. Das YAML ist die Fehlerquelle, nicht die Person. Für die Webeditor-Arbeit: vorher YAML-Prüfer oder gleich den foerbico-editor. Besser: `content-lint` in der Woodpecker-Pipeline, damit der PR rot wird und nicht die Website.
- Aufteilung der 70 offenen Beiträge klären (wer, bis wann).
- OER-Fachtag-Orca.NRW: Cover nur im Midjourney-Konto von Jörg. Download, dann `ai: generated`. Liste auf weitere Midjourney-URLs prüfen.

## J · [AP 4-2] Personen auf Fotos in Bildnachweisen: Einwilligungen prüfen

Labels Priorität/Hoch, Konzeption · Bezug: offene Issues A, B · Datenschutz

Mit der Migration werden `alt`- und `title`-Texte als `kind:1063` auf öffentliche Relays publiziert. Relay-Events lassen sich nachträglich kaum zurückholen. Aktuell mit Klarnamen:

- tagung-open-education (digiLL): Joana Kadir und Matthias Kostrzewa in `alt` und `title` (Eröffnung), Foto FOERBICO, bereits publiziert.
- oercamp-2026: Gina Buchwald-Chassée in `alt`, bereits publiziert.
- hello-world (Branch): „Das FOERBICO Team: Phillip, Jörg, Ludger, Laura und Gina“ in `alt`; eigenes Team, Vornamen.
- Weitere Beiträge der Arbeitsliste zeigen Veranstaltungsfotos.

**Zu klären**

- [ ] Regel: Klarnamen in `alt`/`title` nur mit Einwilligung, sonst Funktion statt Name („Eröffnung durch das digiLL-Team“). Öffentlich in `bildattribution.md`, ohne Beispielnamen.
- [ ] Für bereits publizierte Nachweise: Einwilligung der Genannten einholen oder Nachweis neu prägen (der jüngste gewinnt) und Löschanfrage (`kind:5`) an die Relays.
- [ ] Fotoerlaubnis bei Veranstaltungen: Vorlage in [`Orga/`](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/src/branch/main/Orga/).
- [ ] Redaktionsliste `kind:30000` und Profil enthalten Pubkeys und Namen des Redaktionskreises; Einverständnis der Mitglieder festhalten.

## K · [AP 9-2] Signatur-Infrastruktur: Amber-Bunker, Secrets, lokaler Key, Single Point of Failure

Labels Server, Priorität/Hoch · Bezug: offenes Issue C

- Der FOERBICO-Key signiert über NIP-46. Bunker ist die Amber-App auf Jörgs privatem Handy. Fällt das Gerät aus oder ist offline, publiziert die CI nichts („Bunker connect timeout“); so im Juni und August 2026 (Ausfall über Wochen, erst am 02.09. sichtbar).
- Secrets (`BUNKER_URL`, `CLIENT_SECRET_HEX`, `AUTHOR_PUBKEY_HEX`) als GitHub-Repo-Secrets im Mirror `rpi-virtuell/FOERBICO_und_rpi-virtuell` und lokal in `mdparser/.env`; `blossom-bunker.ts` nutzt dieselbe Datei.
- Neu seit 14.09. (mdparser 451e6e4): `AUTHOR_SECRET_HEX` in der lokalen `.env` erlaubt `sync redaktion` und `sync navigation` ohne Bunker. Damit liegt der FOERBICO-Schlüssel im Klartext auf Jörgs Laptop. Die CI bleibt beim Bunker.
- Die CI läuft auf GitHub (Mirror), nicht auf der eigenen Forgejo/Woodpecker-Infrastruktur.

**Zu klären**

- [ ] Bunker als Dienst im Institut oder zweites Gerät als Fallback.
- [ ] Lokalen Klartext-Key wieder entfernen, sobald Menü und Redaktionsliste über die CI laufen; bis dahin Datei verschlüsselt ablegen.
- [ ] Wer außer Jörg kann im Notfall neu pairen? Runbook ([`mdparser/docs/SETUP-GUIDE.md`](https://git.rpi-virtuell.de/Comenius-Institut/mdparser/src/branch/main/docs/SETUP-GUIDE.md), Hürde 4) im Team bekannt machen.
- [ ] Redaktions-Keys nach [ADR-0021](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/): Verwahrung, Bunker-Modell, Verantwortliche.
- [ ] Umzug der Pipeline auf Woodpecker prüfen, damit Secrets im Haus bleiben.
- [ ] Benachrichtigung bei roten Läufen an mehr als eine Person.

## L · [AP 4-2] Offene Fragen an edufeed (persönliche Kommunikation)

Label Konzeption · Bezug: offenes Issue F

Ansprechpartner: Steffen Rörtgen (edufeed).

- 07.09.: Antwort zu `x`-Tags statt `imeta` erhalten und umgesetzt.
- 10.09.: `ai`-Tag im Wiki ergänzt; edufeed-app am selben Tag nachgezogen.
- Offen seit 04.09.: nimmt `relay.edufeed.org` 1063 an; `PUT /upload` für den FOERBICO-Key (praktisch bestätigt durch den CI-Upload am 09.09.).
- Offen: `PUT /mirror` für `sync adopt`; Bunker-Modell für Redaktions-Keys; nehmen die Relays `kind:30024` an; Umschalttag oer.community → Hub (mit Steffen und Ludger).
- **Bitte ergänzen**: Kanal (Matrix, Mail), Gesprächstermin.

## M · [AP 3-2] Betrieb oer-community: Server, Unit, DNS, Umschalttag

Label Server · Bezug: offenes Issue E2

Ergebnisse der Besprechung am 15.09. (Jörg, Gina, Ludger): Quelle je Inhaltsart (Artikel, Seiten, Listen, Profil vom FOERBICO-Key; Termine aus der Community rpi-virtuell), Umbenennung in oer-community, der eigentliche Community-Hub kommt später.

**Aufgaben Ludger**

- [ ] Server-Verzeichnis und systemd-Unit von `community-hub` auf `oer-community` umbenennen; `deploy-app.sh` anpassen.
- [ ] DNS `oer-community.rpi-virtuell.net` anlegen; danach `.woodpecker.yml` und [`docs/betrieb.md`](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/betrieb.md) nachziehen (Jörg).
- [ ] Woodpecker Repo 13: prüfen, ob Webhook und Clone nach der Umbenennung greifen.
- [ ] `COMMUNITY_PUBKEY` nicht setzen (rpi-virtuell ist Standard; ein gesetzter leerer Wert schaltet den Kalender ab).

**Offen im Team**

- [ ] Umschalttag oer.community → Hub: Entscheidung mit Steffen und Ludger, Cut-over-Bedingungen aus [`redaktion-longform.md`](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/redaktion-longform.md).
- [ ] [ADR-0033](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/), [ADR-0034](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/) und der Nachtrag zu [ADR-0021](https://git.rpi-virtuell.de/Comenius-Institut/oer-community/src/branch/main/docs/entscheidungen/) (Entwürfe als 30024) in der nächsten Runde bestätigen.

---

# Offene Punkte für dich

1. **Freigabe je Issue** und Korrekturen. Zuordnungen bei B ([AP 9-4](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/118) oder 9-5), E1/E2 (Aufteilung auf zwei Meilensteine) und G ([AP 6-3](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/100) oder 4-7) sind Vorschläge.
2. **Geschlossenes Repo**: keine Meilensteine vorhanden. Ich setze die AP-Nummer in den Titel und nutze die vorhandenen Labels. Einverstanden, oder soll ich dort Meilensteine anlegen?
3. **A'**: [#191](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues/191) schließen?
4. **H und L**: Datum und Kanal der Zusagen fehlen; ergänzst du sie, oder bleiben die Stellen als „bitte ergänzen“ stehen?
5. **K**: Der lokale Klartext-Key (`AUTHOR_SECRET_HEX`) ist neu; magst du, dass ich das so deutlich hineinschreibe?
6. **Posten**: Token liegt vor und funktioniert (Nutzer joerglohrer, Schreibrecht auf beiden Repos). Ich habe die Dateirechte der Token-Datei auf 600 gesetzt. Nach deinem Okay poste ich, ersetze `[#840](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues/840)` durch die echte Nummer und verlinke die geschlossenen Issues nur untereinander.

## Meilenstein-Links

| AP | offenes Repo | geschlossenes Repo |
|---|---|---|
| [AP 1-1 + 1-2](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/5) | [5](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/5) | [204](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/204) |
| [AP 1-2](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/6) | [6](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/6) | [205](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/205) |
| [AP 2-1](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/82) | [82](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/82) | [167](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/167) |
| [AP 2-2](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/84) | [84](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/84) | [169](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/169) |
| [AP 2-3](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/85) | [85](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/85) | [170](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/170) |
| [AP 2-4](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/121) | [121](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/121) | [206](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/206) |
| [AP 3-1](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/9) | [9](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/9) | [164](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/164) |
| [AP 3-2 + 3-3](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/83) | [83](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/83) | [182](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/182) |
| [AP 3](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/7) | [7](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/7) | [196](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/196) |
| [AP 4-1](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/80) | [80](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/80) | [166](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/166) |
| [AP 4-2](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/88) | [88](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/88) | [173](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/173) |
| [AP 4-3 + 4-4](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/90) | [90](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/90) | [175](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/175) |
| [AP 4-5](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/99) | [99](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/99) | [183](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/183) |
| [AP 4-6](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/115) | [115](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/115) | [200](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/200) |
| [AP 4-7](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/101) | [101](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/101) | [185](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/185) |
| [AP 5-1](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/89) | [89](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/89) | [174](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/174) |
| [AP 5-2](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/97) | [97](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/97) | [181](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/181) |
| [AP 6-1](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/91) | [91](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/91) | [176](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/176) |
| [AP 6-2](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/94) | [94](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/94) | [180](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/180) |
| [AP 6-3](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/100) | [100](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/100) | [184](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/184) |
| [AP 6-4](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/14) | [14](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/14) | [197](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/197) |
| [AP 7-1](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/86) | [86](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/86) | [171](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/171) |
| [AP 7-2](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/92) | [92](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/92) | [177](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/177) |
| [AP 7-3](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/102) | [102](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/102) | [187](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/187) |
| [AP 7-4](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/107) | [107](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/107) | [191](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/191) |
| [AP 7-5](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/105) | [105](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/105) | [190](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/190) |
| [AP 8-1](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/116) | [116](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/116) | [201](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/201) |
| [AP 8-2](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/93) | [93](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/93) | [178](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/178) |
| [AP 8-3](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/108) | [108](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/108) | [192](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/192) |
| [AP 8-4](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/103) | [103](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/103) | [188](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/188) |
| [AP 8-5](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/109) | [109](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/109) | [195](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/195) |
| [AP 8-6](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/13) | [13](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/13) | [193](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/193) |
| [AP 9-1](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/87) | [87](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/87) | [172](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/172) |
| [AP 9-2](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/8) | [8](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/8) | [198](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/198) |
| [AP 9-3](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/4) | [4](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/4) | [165](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/165) |
| [AP 9-4](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/118) | [118](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/118) | [202](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/202) |
| [AP 9-5](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/16) | [16](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/16) | [203](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/203) |
| [AP 10-1](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/95) | [95](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/95) | [179](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/179) |
| [AP 10-2](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/110) | [110](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/110) | [194](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/194) |
| [AP 11-1](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/10) | [10](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/10) | [168](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/168) |
| [AP 11-2](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/104) | [104](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/104) | [186](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/186) |
| [AP 11-3](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/106) | [106](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/106) | [189](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/189) |
| [AP 11-4](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/120) | [120](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/milestone/120) | [199](https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen/milestone/199) |
