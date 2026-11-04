# Übergabe Hub-Inhalte (Etappe 3): Branch-Stapel, Merge-Ablauf, offene Schritte

Stand 04.11.2026: Die sieben Branches sind lokal fertig und geprüft (49 Tests grün; der siebte ist die Nacharbeit aus der Gesamt-Review), am 04.11.2026 als PRs von Poutník auf gitworkshop (Spalte PR) und gemergt; `main` steht auf `255b295` (Nostr und Forgejo, 04.11.2026). Die vier Kommentare sind am 04.11.2026 abends veröffentlicht (Links in `00-uebersicht.md` des Protokollordners); hub.rpi-virtuell.net liefert den Stand seit 18:41 Uhr aus. Jeder Branch sitzt auf dem Kopf des vorigen, ein PR zeigt nach dem Merge der Vorgänger nur seinen eigenen Diff. Zahl = Issue der Kommentarentwürfe.

## 1. Branch-Stapel in Reihenfolge

| Nr. | Branch | Kopf-Commit | Was er tut | Issue | PR |
|---|---|---|---|---|---|
| 1 | `pr/inhalte-aus-events` | `ba5c49e` | Sichere Markdown-Darstellung, Schaufenster-Daten in einer Abfrage, Lizenzlabel und Lizenzstand (offen, geschützt, unbekannt) | 10 | [PR](https://gitworkshop.dev/nevent1qqsxnkyllderyrnh6t3s5uz6s72s52fg79wrzs459vckve27qfm5s4qpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mhhcupak) |
| 2 | `pr/schaufenster-live` | `d091c99` | Menü aus der Navigationsliste, Seiten unter `#oercommunity/<d>`, zwölf neueste Beiträge live, Termine-Archiv mit ehrlichem Satz, Logbuch-Link, Schnappschuss der Beiträge | 10 | [PR](https://gitworkshop.dev/nevent1qqsrwkghuv26hgq8ky5f678rcfvhjjenh6ca6n6vmvqhmpru2ft4mzgpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mhy2u378) |
| 3 | `pr/spielregeln` | `2d9a7cf` | Bereich `#oercommunity/spielregeln` mit vier Kacheln, „in Vorbereitung“ bis die Seiten liegen, fünfte Kachel zum Tutorial | 03 | [PR](https://gitworkshop.dev/nevent1qqsfun6gxae5e3v235yua0e702mdfd8hr6mlkp9rw6nhql2de8wly7cpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mht00y5u) |
| 4 | `pr/materialpool-live` | `87f4ba6` | Materialien live als kind:30142 von drei Relays, Suche, Vorauswahl, Lizenzpille, Zähler für vollständige Metadaten | 04 | [PR](https://gitworkshop.dev/nevent1qqsp8vh7s3svl7x5nef9skcsr6x947xzxgcqae04dq0yqe9xcv9kmfcpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mh3fwn02) |
| 5 | `pr/material-detail` | `568b91f` | Detailansicht `#materialpool?d=…&p=…` mit Vokabular-Links, Lizenzpille, Rohdaten als JSON-LD; der Lizenzstand bestimmt die Aktionen, ausgegraute bleiben sichtbar | 04, 15 | [PR](https://gitworkshop.dev/nevent1qqsq5h7ugwhg7utgee9gckd83nxeh8sg4vypflyhf33vjk74lm7g04gpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mh394y7m) |
| 6 | `pr/doku-etappe-3` | `e5b0777` | ADR-0007, README und Konstruktionsbeschreibung nachgeführt | – | [PR](https://gitworkshop.dev/nevent1qqszeqasgx7mejfrqudg54u8hhh90keed3zgeg4pu5ytgxgjdkrqxzcpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mhga8vp7) |
| 7 | `pr/nacharbeit-etappe-3` | `a4afb78` | Nacharbeit aus der Gesamt-Review: Herausgeber-Schlüssel als 64-Hex geprüft, Schnappschuss-Texte im Community-Raum maskiert, Relay-Ausfall ehrlich benannt (statt „in Vorbereitung“/„nicht gefunden“), Lizenzsatz „nicht erkannt“, Zähler „abgefragt bei 3 Relays“, Doku nachgeführt, Test mit feindlichem Relay-Text | 04, 10, 15 | [PR](https://gitworkshop.dev/nevent1qqsd0v7l2827p8fw9045c66mhqphk5ag6w0dytqvw8p5uqnd3gddwtqpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mhs4gs62) |
**Bedingung:** Die Nacharbeit (Branch 7) behebt einen Critical-Befund (unmaskierter Herausgeber-Schlüssel im Kartenlink aus Branch 4/5). Den Stapel deshalb in einer Sitzung vollständig mergen und erst danach `main` pushen, wie in Etappe 2; einzelne frühere PRs ohne Branch 7 nicht ausliefern.

Basis ist `main` `21ae08b`. Nicht im Stapel: die gemergten Branches der Etappe 2 (siehe `Hub-Entwicklung/2026-11-05-etappe-2-uebergabe.md`).

Merge-Commits (04.11.2026): inhalte-aus-events `45aa1fc`, schaufenster-live `046051d`, spielregeln `abd6438`, materialpool-live `c91e6ca`, material-detail `4216a18`, doku-etappe-3 `45bf29d`, nacharbeit-etappe-3 `255b295`. `{{main}}` in den Kommentar-Entwürfen ist eingesetzt.

## 2. Ablauf je Branch (Jörg, der Reihe nach)

```bash
cd ~/repositories/reli-hub && git checkout main && git -c nostr.signer=joerg fetch origin main && git log --oneline main..origin/main
```
Leere Ausgabe heißt: `main` unverändert. Sonst `git merge --ff-only origin/main`, den Branch (und die folgenden) darauf rebasen, `deno task test`, erneut prüfen.

```bash
cd ~/repositories/FOERBICO_und_rpi-virtuell/tools/poutnik && deno task push pr/<name> --as poutnik --cwd ~/repositories/reli-hub
```
Die PR-Beschreibung nennt das Issue (Kurz-ID und gitworkshop-Link), die Entscheidung in zwei Sätzen und den Prüfbefehl `deno task test`. Dann Jörg mit Amber:

```bash
cd ~/repositories/reli-hub && git checkout pr/<name> && ngit --signer joerg pr merge --offline
```
Das macht man für jeden der sechs Branches in der Reihenfolge der Tabelle. Danach einmal `main` pushen:

```bash
cd ~/repositories/FOERBICO_und_rpi-virtuell/tools/poutnik && deno task push main --as joerg --cwd ~/repositories/reli-hub
cd ~/repositories/reli-hub && git checkout main && git push forgejo main
```
Den gemergten `main`-Hash je Branch für die Kommentare notieren.

## 3. Schranken

- Spielregeln-Seiten: Die vier Seitentexte liegen untracked im FOERBICO-Arbeitsbaum unter `Website/content/de/spielregeln-*/index.md` (qualitaetskriterien, metadatenprofil, redaktion, ablaeufe). Die Redaktion liest bis 30.11. gegen; danach Commit auf Branch `spielregeln-seiten` und Merge, die Pipeline veröffentlicht sie, und der Bereich zeigt „4 von 4 Seiten“ ohne Codeänderung. Bis dahin steht dort „in Vorbereitung“.
- Kommentare: am 04.11.2026 veröffentlicht (Reihenfolge 10, 03, 04, 15; nevents in `00-uebersicht.md`). Entwürfe in `~/.config/poutnik/protokolle/issue-kommentare-2026-11-24/` (siehe `00-uebersicht.md`). Erst nach den Merges die Platzhalter `{{pr:…}}` und `{{main}}` ersetzen, dann je Datei `zsh tools/poutnik/skripte/pub-comment.sh <datei>` in der Reihenfolge 10, 03, 04, 15 und `cd tools/poutnik && deno task threads --repo reli-hub --since 1` (vier Kommentare von Poutník).
- Schnappschuss: Vor der Tagung am 17./18.11. erneuern: auf frischem Branch `cd ~/repositories/reli-hub && git checkout -b pr/schnappschuss-2026-11-16 main && deno task schnappschuss && deno task test`; der Schnappschuss besteht jetzt aus zwei Blöcken (Termine und Beiträge). Committen („Schnappschuss vom <Datum>“), dann Ablauf wie oben. `deno.lock` nie committen.
- Nachgereichtes, nicht blockierend: die zurückgestellten kleinen Befunde stehen in `.superpowers/sdd/2026-11-06-hub-etappe-3-inhalte/progress.md` (unter anderem: Suche und Vorauswahl greifen vor den Live-Daten nicht auf den Schnappschuss, ein Netzfehler im Material-Detail liest sich als „nicht gefunden“).

## 4. Restliche Schritte im FOERBICO-Repo

1. Spec-Fahrplan in `docs/superpowers/specs/2026-11-02-hub-nachweis-gesamtkonzeption-design.md`: dritte Zeile um „Erledigt am <Datum>: PRs …, main <hash>“ ergänzen.
2. Forgejo-Kommentar auf dem Nachweis-Issue (Nummern in `Orga/nachweis-hub/ergebnis.json`, Schlüssel `01-ap-3-2-3-3` für die Zeilen 4.2 und 4.15, Schlüssel der Metadaten-Zeile für 4.3 und 4.12), mit den gemergten PRs und der Adresse https://hub.rpi-virtuell.net; Token aus `~/.config/forgejo/token.txt`, als eigener Aufruf, nicht mit dem Commit kombiniert.
3. Diese Datei und `Hub-Entwicklung/2026-11-16-stand-fuer-ux-gast.md` committen; vorher `python3 -I tools/nachweis/check.py erschliessung <Ordner mit den neuen Dateien>`.
4. Abnahme am 25.11.2026 mit der Checkliste; Ergebnis in `Hub-Entwicklung/2026-11-25-abnahme-navigation.md`.
