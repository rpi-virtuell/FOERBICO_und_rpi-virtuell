# Übergabe Hub-Sammlung und Kataloge (Etappe 4): Branch-Stapel, Merge-Ablauf, offene Schritte

Stand 05.11.2026 (PRs am 05.11.2026 um 19:34 Uhr als Poutník auf gitworkshop, 5/7 Relays): Die sieben Branches sind lokal fertig und geprüft (65 Tests grün; der siebte ist die Nacharbeit aus der Gesamt-Review). Noch nichts gepusht, gemergt oder kommentiert; die PR-Spalte bleibt „–“, bis Jörg die Branches als Poutník gepusht hat. Jeder Branch sitzt auf dem Kopf des vorigen, ein PR zeigt nach dem Merge der Vorgänger nur seinen eigenen Diff. Zahl = Issue der Kommentarentwürfe.

## 1. Branch-Stapel in Reihenfolge

| Nr. | Branch | Kopf-Commit | Was er tut | Issue | PR |
|---|---|---|---|---|---|
| 1 | `pr/community-inhalte` | `3cc017b2` | Geteilte Inhalte über den `h`-Tag, Reposts aufgelöst, Kuratierungslisten und Entfernen-Label der fünf Hub-Communities; Nacharbeit: Schlüssel aus Events nur als 64-Hex in Links und Auflösung | 02, 01 | [PR](https://gitworkshop.dev/nevent1qqsfamvxnx9d0p3v8w5p3jqm3g8ptvkqyayswnhs63fzxup74tk3w0qpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mhpkas29) |
| 2 | `pr/sammlung` | `d3f03a3d` | Sammlung nach Community, Fach, Stufe und Lizenz filtern, geteilte Materialien nachladen, teilen, einbetten (Shortcode, Kontextprofil), abonnieren als Nostr-Filter; ehrlicher Fehlerpfad, Fokus der Lizenz-Pillen | 01 | [PR](https://gitworkshop.dev/nevent1qqsvz9luc3g3zvxl94jq7msumn0j2dmwedcea7l6na90uvg52j6dn4spz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mhnxf6je) |
| 3 | `pr/kataloge` | `159dd93a` | Katalog je Community mit Stand-Zeile, geteilte Inhalte als Grundschicht, Kuratierungslisten darüber, ehrliche Zustände, Teilen und Einbetten, Materialpool als Katalog der Instanz | 02 | [PR](https://gitworkshop.dev/nevent1qqspqujucd7vjq40vee5dlx8364even8h0jznp63hk7ar90lhenwatspz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mhq6ax0t) |
| 4 | `pr/kalender` | `e2add792` | Fortbildungskalender über alle Quellen: Labor- und Institutslogik als Merkmale, feste Quellenliste, Relay-Grenze sichtbar, 120-Tage-Fenster, Schnappschuss aller Quellen | 05 | [PR](https://gitworkshop.dev/nevent1qqs02musc94tyzn3kajwv69hkqmwmcpdvh8t5fesfw9u7mxw6e6eqkcpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mhtwccwn) |
| 5 | `pr/personen` | `7845ac6d` | Echte Profile aus der Personen-Liste mit Einverständnis, Profilseite mit Veröffentlichungen, Teamseite als Rückfall, Folgen bis zur Anmeldung deaktiviert | 06 | [PR](https://gitworkshop.dev/nevent1qqsz0cun5cden3yjjk6mzzun9zz53rq4svc2g7gya4w5y25qas3vlpgpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mhenua75) |
| 6 | `pr/doku-etappe-4` | `61877310` | ADR-0008 (Community-Inhalte und Listen), README und Konstruktionsbeschreibung nachgeführt | – | [PR](https://gitworkshop.dev/nevent1qqs0pa8572pwmak2up5rdmm4t4ltaux3rj322krtepe4k8u54lz2evspz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mhfmlq0f) |
| 7 | `pr/nacharbeit-etappe-4` | `1716f98f` | Nacharbeit aus der Gesamt-Review: leere Antwort von keiner Antwort unterschieden, Cache-Schlüssel gehasht, Profilseite im Funkloch ehrlich, Doku nachgezogen, Schnappschuss je Gruppe, Hub-Name aus neuen Fußzeilen und Titeln entfernt, Knopftext, vollständiger Name in der Konstruktion | 01, 02, 05, 06 | [PR](https://gitworkshop.dev/nevent1qqs8g8c2ek23gl4aatuapvjnp5a3uzpmqgnm87t86e6hqvgx9zsqvmspz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mhtxhcsa) |
**Bedingung:** Die Nacharbeit (Branch 7) behebt Befunde aus den Branches 1 bis 5. Den Stapel deshalb in einer Sitzung vollständig mergen und erst danach `main` pushen, wie in Etappe 3; einzelne frühere PRs ohne Branch 7 nicht ausliefern.

Basis ist `main` `f68a3fdb`. Nicht im Stapel: die gemergten Branches der Etappen 2 und 3 (siehe `Hub-Entwicklung/2026-11-05-etappe-2-uebergabe.md` und `Hub-Entwicklung/2026-11-24-etappe-3-uebergabe.md`). Die Merge-Commits je Branch hier nach dem Merge nachtragen.

Merge-Commits (05.11.2026, 19:36 Uhr): community-inhalte `300e220d`, sammlung `0faf29aa`, kataloge `d4243763`, kalender `0eda63f0`, personen `6634c053`, doku-etappe-4 `c3e34d21`, nacharbeit-etappe-4 `2ea71041`. `main` 2ea71041 am 05.11.2026 als joerg nach Nostr gepusht (7 Statusmeldungen „gemergt“); `{{main}}` in den Kommentar-Entwürfen ist eingesetzt.

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
Das macht man für jeden der sieben Branches in der Reihenfolge der Tabelle. Danach einmal `main` pushen:

```bash
cd ~/repositories/FOERBICO_und_rpi-virtuell/tools/poutnik && deno task push main --as joerg --cwd ~/repositories/reli-hub
cd ~/repositories/reli-hub && git checkout main && git push forgejo main
```
Den gemergten `main`-Hash je Branch für die Kommentare notieren.

## 3. Schranken

- Inhaltsstrang im FOERBICO-Checkout (aus Task 7, noch nicht committet): `Website/navigation.yaml` ist geändert (Liste `katalog`), dazu liegen `tools/listen/` (Skript und README) und `Hub-Entwicklung/kataloge/` (Vorlagen und Entscheidungstabelle) untracked. Jörg liest gegen und committet auf einem Branch `kataloge-und-personen`. Die FOERBICO-Liste geht über `mdparser sync navigation` live (Lauf von Hand).
- Schlüsseldatei: `~/.config/nachweis/listen.env` (Rechte 600) mit den fünf Variablen `NSEC_RPI_VIRTUELL`, `NSEC_RELILAB`, `NSEC_RELIGLOBAL`, `NSEC_ALPIKA_GS`, `NSEC_FOERBICO` legt Jörg selbst an; ohne sie laufen die Listen-Skripte nicht.
- Personen-Liste: Sie braucht die npubs der Personen mit Einverständnis. Bis sie liegt, zeigt die Ansicht die Teamseite und Folgen ist deaktiviert.
- Repost-Vorschläge: Welche Inhalte die Communities per Repost teilen, sind Entscheidungen für Jörg und die Redaktion (`Hub-Entwicklung/kataloge/teilen-vorschlaege.md`), nicht vorweggenommen.
- Kommentare: Entwürfe in `~/.config/poutnik/protokolle/issue-kommentare-2026-12-07/` (siehe `00-uebersicht.md`). Erst nach den Merges die Platzhalter `{{pr:…}}` und `{{main}}` ersetzen (Skript aus der Etappe-2-Übergabe), die Texte lesen, dann je Datei `zsh tools/poutnik/skripte/pub-comment.sh <datei>` in der Reihenfolge 01, 02, 05, 06 und `cd tools/poutnik && deno task threads --repo reli-hub --since 1` (vier Kommentare von Poutník). Nichts davon ist bisher veröffentlicht.
- Schnappschuss: bereits am 05.11.2026 erneuert (49 Termine). Vor der Tagung am 17./18.11. noch einmal auf frischem Branch: `cd ~/repositories/reli-hub && git checkout -b pr/schnappschuss-2026-11-16 main && deno task schnappschuss && deno task test`; er läuft jetzt je Gruppe (drei Abfragen), die Quellen stehen im Branch `pr/kalender`. Committen („Schnappschuss vom <Datum>“), dann Ablauf wie oben. Spätestens alle 120 Tage erneuern. `deno.lock` nie committen.
- Relay-Lesen für die Tagung: Die Ausnahmeregel für die IP des Tagungsortes (Relays und Blossom sperren sonst nach rund 20 schnellen Abfragen) ist vor dem 17.11. zu klären (die Ausnahmeregel der Betreiber gilt seit 23.09.2026 für die Pipeline, nicht für Gäste hinter einem gemeinsamen WLAN; Jörg Lohrer bittet den Relay-Betreiber um eine Lesefreigabe für die Tagungs-IP); die Kalenderansicht fragt mehrere Quellen gleichzeitig ab.
- Bedarf: Was die Partner liefern müssen (Schlüssel, Tags an Terminen, Einverständnisse), steht in `Hub-Entwicklung/2026-11-07-etappe-4-bedarf-team.md`.
- Zurückgestellt (kleine Befunde, die Gesamt-Review ordnete sie als „kann warten“ ein; Einzelheiten in `.superpowers/sdd/2026-11-07-hub-etappe-4-sammlung-kataloge/progress.md`, soweit nicht in Branch 7 behoben):
  - Auflösung und Listen: Ziele können jedes Kind auflösen, Reposts auf entfernte oder schon vorhandene Adressen werden nicht zusammengeführt, Listen werden nicht clientseitig auf den Herausgeber geprüft.
  - Sammlung: Kartenmarkup doppelt zu `mpRender`, Mehrfachwerte in der URL zeigen nur den ersten, Shortcode-Zeichen nur teilweise maskiert, Fokus nach Neuschreiben der Auswahlfelder ungeprüft, Fehlerpfade nur manuell belegt.
  - Katalog: Community ohne Eintrag im Nachbau wirft einen Fehler (vorbestehend), Fehlermeldung bei Render-Fehlern irreführend, Mehr-Zustand geht beim Neuzeichnen verloren, Doku zu http-Links ungenau, kein Test für Tab-Wechsel.
  - Kalender: „bevorstehend“ wird an drei Stellen unterschiedlich gezählt, Stand-Zeile zeigt die ungefilterte Zahl, Online-Erkennung trifft Ortsnamen mit „Online“, Grenzzählung kann nahe 500 Fehlalarm geben, vierter Filter fehlt in der Abfragetabelle der Doku.
  - Personen: kurzes Flackern von Teamseite zu Karten, Entitäten wie `&#39;` ungeprüft, Testtiefe gering.
  - Listen-Skript: bei AUTH/NOTICE vergehen die vollen 15 s, die Vorschläge für rpi-virtuell sind ältere Impulse statt neu angelegter Materialien, Themenzuordnung nicht gegen Relays geprüft, `content: null` ungeregelt.

## 4. Restliche Schritte im FOERBICO-Repo

1. Spec-Fahrplan in `docs/superpowers/specs/2026-11-02-hub-nachweis-gesamtkonzeption-design.md`: Zeile „bis 07.12.2026“ um „Erledigt am <Datum>: PRs …, main <hash>“ ergänzen.
2. Forgejo-Kommentare auf den Nachweis-Issues (Nummern in `Orga/nachweis-hub/ergebnis.json`): #882 (Zeile 4.5, Sammlung), #883 (4.6, Kataloge), #887 (4.9, Kalender), #891 und #892 (4.10, Personen), jeweils mit den gemergten PRs und der Adresse https://hub.rpi-virtuell.net; Token aus `~/.config/forgejo/token.txt`, je Kommentar als eigener Aufruf, nicht mit dem Commit kombiniert.
3. Diese Datei, den Inhaltsstrang (siehe Schranken) und `Hub-Entwicklung/2026-11-16-stand-fuer-ux-gast.md` committen; vorher `python3 -I tools/nachweis/check.py erschliessung <Ordner mit den neuen Dateien>`.
4. Abnahme am 25.11.2026 mit der Checkliste; sie enthält jetzt drei zusätzliche Aufgaben (Sammlung zusammenstellen und einbetten, Katalog einer Community finden, Fortbildung nach Merkmal filtern). Ergebnis in `Hub-Entwicklung/2026-11-25-abnahme-navigation.md`.
