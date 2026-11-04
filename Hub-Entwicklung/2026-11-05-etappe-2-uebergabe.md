# Übergabe Hub-Navigation (Etappe 2): Branch-Stapel, Merge-Ablauf, offene Schritte

Stand 04.11.2026: Alle 13 Branches sind als Pull Requests von Poutník auf gitworkshop (Spalte PR); alle 13 sind gemergt, `main` steht auf `21ae08b` (Nostr und Forgejo, 04.11.2026); die elf Kommentare auf den Issues sind am 04.11.2026 als Poutník veröffentlicht (nevent je Datei in `<datei>.json` im Entwurfsordner). Jeder Branch sitzt auf dem Kopf des vorigen, ein PR zeigt nach dem Merge der Vorgänger nur seinen eigenen Diff. Zahl = Issue der Kommentarentwürfe.

## 1. Branch-Stapel in Reihenfolge

| Nr. | Branch | Kopf-Commit | Was er tut | Issue | PR |
|---|---|---|---|---|---|
| 1 | `pr/datenschicht` | `063dfff` | Live-Abfrage der Relays mit Schnappschuss als Rückfall, Datenstand je Ansicht | 13 | [PR](https://gitworkshop.dev/nevent1qqste5u65dxv8ecry8pulnlepegu8khtdh445w69lqgctf2rqm5umvqpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mhzyjyd0) |
| 2 | `pr/konsole-aktivieren` | `4cfba48` | Kreis erklärt sofort beim Überfahren, Antippen oder per Tastatur (Ereignis `relihub-activate`) | 01 | [PR](https://gitworkshop.dev/nevent1qqsydm8xazmcu07hac0tu50xxrv7tf5e5khk7w0r4lpr9rgk6udzqzspz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mhfxdlsv) |
| 3 | `pr/konsole-treffer` | `8969bee` | Beschriftungen klickbar, größerer Trefferkreis je Knospe | 02 | [PR](https://gitworkshop.dev/nevent1qqsvymy2dcspg66vr85dgz39pd8tf9lm8y4vqgwdl5a7a9etmt27nccpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mh3eeg04) |
| 4 | `pr/konsole-direkt` | `d400392` | Tutorial- und Direktmodus, eine Standardkette für alle Kontexte, „Hilfe“ in der Kopfzeile | 03 | [PR](https://gitworkshop.dev/nevent1qqs0cehe7n02ekh270mqk6drdxjylhxsxd7zun2ae2jwd5jklw6faygpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mhw2ewvy) |
| 5 | `pr/konsole-mobil` | `407d9c9` | Erklärkarte mobil als Sheet, Toleranz beim Tippen | 08 | [PR](https://gitworkshop.dev/nevent1qqs0xr3ukqg842n0rmegg55j80humx0pumh3r5trljuzdad3ealvu0gpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mhgxqyn6) |
| 6 | `pr/leiste-widget` | `fe70c99` | Leiste unten links als Widget `relihub-leiste` („Orte“), Konsole „Tätigkeiten“ | 06 | [PR](https://gitworkshop.dev/nevent1qqsggv3vkc3c2dlc37pqmldflfwv62npsmj4glw4dqxcwsl6zevv36cpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mh9tvmf5) |
| 7 | `pr/rpi-virtuell-instanz` | `62c34b1` | rpi-virtuell als eigene Instanz mit Material, Fortbildungen, News | 17 | [PR](https://gitworkshop.dev/nevent1qqsp3c8etkyzwp82lpd6p0pwx9uv6c0v6gn49c97qucl92j9dvy3g6gpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mh8sw8jf) |
| 8 | `pr/navigation-begriffe` | `f9da225` | Begriffstabelle (docs/navigation.md), Knospen in Bereichsfarbe, Lerninhalte in den Materialpool | 04 | [PR](https://gitworkshop.dev/nevent1qqs9s6wca0lmhwwkg79qmswq4hfaftew9wv76sqvhgd63vdgu833dngpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mhq4tpzm) |
| 9 | `pr/konsole-startseite` | `f08e0a3` | Kleine Konsole folgt der großen auf der Startseite, Hinweis in der Karte | 05 | [PR](https://gitworkshop.dev/nevent1qqs0hjjnjwul4l5vl5fz2kewegly0jaedhny5yewde54p5j8jx2963gpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mh9tx36g) |
| 10 | `pr/startseite-narrativ` | `be1a1f5` | Startseitentext statt Slogan mit drei Einladungen | 18 | [PR](https://gitworkshop.dev/nevent1qqsdmus7kcnew97xk22lulqud5k8cc2ezvxmvdqufvum3s3k90lx6jcpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mh63m5fu) |
| 11 | `pr/leiste-konfigurierbar` | `2631c3f` | Knopf ⋯, Panel zum Ein- und Ausblenden von Leisten-Einträgen | 07 | [PR](https://gitworkshop.dev/nevent1qqstt99xt0d2hqn69pqug20e499huu95vlelrudpurzqeqm3gm9r40gpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mhqlkg4m) |
| 12 | `pr/doku-etappe-2` | `9c204e2` | README und Konstruktionsbeschreibung nachgeführt | – | [PR](https://gitworkshop.dev/nevent1qqsglz8kwpx4kg5kqrq6wtj4k2lanmehprtwaq8ga6k6xqh8hjjkvxcpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mhfmgzs4) |
| 13 | `pr/nacharbeit-review` | `4885f27` | Nacharbeit aus der Gesamt-Review: ehrliche Kennzeichnung der Community-Ansichten, Link-Prüfung für Relay-Daten, Fokus der Leiste, Karte bleibt nach Klick stehen, Verhaltenstests für `hubFetch` | – | [PR](https://gitworkshop.dev/nevent1qqsg8zuem90cg86ahq0ty0pf8lun3ges2wln59r7we68nguc30aa6lqpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mh8ep84f) |

Nicht im Stapel: `pr/prototyp-5` und `pr/issues-runde-1` sind frühere, bereits gemergte PRs.

## 2. Ablauf je Branch (Jörg, der Reihe nach)

Der Push als Poutník ist am 04.11.2026 für alle 13 Branches erledigt (`main` war noch `3fccf2e`). Die Merges sind am 04.11.2026 lokal per `ngit pr merge --offline` erfolgt (je ein No-ff-Merge-Commit), `main` einmal als joerg gepusht. Merge-Commits: datenschicht `792e2ce`, konsole-aktivieren `992e7fb`, konsole-treffer `26ac8cc`, konsole-direkt `4f36382`, konsole-mobil `bec2283`, leiste-widget `ccc8224`, rpi-virtuell-instanz `db292fa`, navigation-begriffe `658b7d7`, konsole-startseite `e778c35`, startseite-narrativ `12c3d33`, leiste-konfigurierbar `f3a37f9`, doku-etappe-2 `3f549e9`, nacharbeit-review `21ae08b`.

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
cd ~/repositories/FOERBICO_und_rpi-virtuell/tools/poutnik && deno task push main --as joerg --cwd ~/repositories/reli-hub
cd ~/repositories/reli-hub && git checkout main && git push forgejo main
```
Danach der nächste Branch; er enthält die vorigen schon, sein PR zeigt nur den eigenen Diff. Den gemergten `main`-Hash für den Kommentar notieren.

## 3. Schranken

- Narrativ-Wortlaut (gemergt, noch nicht gegengelesen): Vor dem Kommentar 18 den Wortlaut in `.superpowers/sdd/2026-11-05-hub-etappe-2-navigation/task-10-report.md` gegenlesen (besonders „geschütztes Material darf dazu, bleibt aber beim Ansehen“ und „persönlichen Ausgangspunkt“).
- Schnappschuss: Vor dem 16.11. auf frischem Branch `cd ~/repositories/reli-hub && git checkout -b pr/schnappschuss-2026-11-16 main && deno task schnappschuss && deno task test`, committen („Schnappschuss der relilab-Termine vom <Datum>“), dann Ablauf wie oben. `deno.lock` nie committen.
- Kommentare: am 04.11.2026 veröffentlicht. Entwürfe in `~/.config/poutnik/protokolle/issue-kommentare-2026-11-16/` (siehe `00-uebersicht.md`); Platzhalter `{{pr:<branch>}}` sind eingesetzt, `{{main}}` sind eingesetzt, danach je Datei `zsh tools/poutnik/skripte/pub-comment.sh <datei>` und `cd tools/poutnik && deno task threads --repo reli-hub --since 1` (elf Kommentare von Poutník).
- Nachricht an den UX-Gast: Entwurf und Abnahme-Checkliste in `Hub-Entwicklung/2026-11-16-stand-fuer-ux-gast.md`, Jörg sendet.

## 4. Restliche Schritte im FOERBICO-Repo

Spec-Fahrplan und Forgejo-Kommentar (Issue #879, Kommentar 14584) sind am 04.11.2026 erledigt.

1. Spec-Fahrplan in `docs/superpowers/specs/2026-11-02-hub-nachweis-gesamtkonzeption-design.md`: Zeile „bis 16.11.2026“ um „Erledigt am <Datum>: PRs …, main <hash>“ ergänzen.
2. Forgejo-Kommentar auf dem Nachweis-Issue zu Zeile 4.1/4.2/4.15/4.18: Nummer 879 (`Orga/nachweis-hub/ergebnis.json`, Schlüssel `01-ap-3-2-3-3`), mit den gemergten PRs und der Adresse https://hub.rpi-virtuell.net; Token aus `~/.config/forgejo/token.txt`.
3. Die beiden Dateien `Hub-Entwicklung/2026-11-16-stand-fuer-ux-gast.md` und `Hub-Entwicklung/2026-11-05-etappe-2-uebergabe.md` ablegen und committen; vorher `python3 -I tools/nachweis/check.py erschliessung Hub-Entwicklung` (Namensprüfung; die älteren Dateien im Ordner melden Namen, die beiden neuen sind frei von Befunden).
4. Abnahme am 25.11.2026 mit der Checkliste; Ergebnis in `Hub-Entwicklung/2026-11-25-abnahme-navigation.md`.
