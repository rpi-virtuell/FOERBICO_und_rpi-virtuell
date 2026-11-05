# Hub als Nachweis, Etappe 4: Sammlung, Kataloge, Kalender, Personen. Umsetzungsplan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bis 07.12.2026 hat jede der vier Zeilen 4.5, 4.6, 4.9 und 4.10 der Spec ihr Hub-Element mit Live-Daten: eine Ansicht „Sammlung“ filtert Materialien nach Community, Fach, Stufe und Lizenz und bietet Teilen, Einbetten und Abonnieren (Issue 01); jede der fünf Katalog-Communities hat eine Katalog-Seite, die zeigt, was mit ihr geteilt wurde (`h`-Tag, Reposts), darüber ihre Kuratierungslisten `kind:30004` mit Stand, und ehrlich sagt, wenn noch nichts geteilt ist (Issue 02); ein Fortbildungskalender über alle religionspädagogischen Quellen unterscheidet Labor- und Institutslogik über Merkmale, nicht über getrennte Kalender (Issue 05); eine Personen-Ansicht zeigt echte Profile aus einer Personen-Liste mit Einverständnis, dazu eine Profilseite je Person (Issue 06). Der Inhaltsstrang liefert parallel die Personen-Liste, gepflegte Profile, den FOERBICO-Katalog und beispielhaft geteilte Materialien (Spec 5a); Kataloge brauchen keine Lieferung, weil das Geteilte der Communities schon da ist; was vor der Fachtagung am 17./18.11.2026 fehlt, zeigt der Hub als gekennzeichneten Rückfall.

**Architecture:** Eine HTML-Datei ohne Build (`index.html`), drei Inline-Skripte; alles Neue kommt ins Anwendungsskript und nutzt die Datenschicht (`hubFetch`, `datenstand`, `npubToHex`, `naddr`, `sichereUrl`, `istHex64`, ADR-0006) und die Inhalte-Bausteine aus Etappe 3 (`mpLaden`/`mpDaten`, `mpMaterial`, `mpPasst`, `ambWerte`, `lizenzStand`, `lizenzLabel`, `ocLaden`, `tagWert`, `tagWerte`, `evToTermin`, ADR-0007). Neu ist ein Block „Community-Inhalte und Listen“: Inhalte, die mit einer Community geteilt sind (Events mit `h`-Tag und Reposts `kind:16` mit `h`-Tag, nach dem edufeed-Wiki „Sharing and reading community content“), Kuratierungslisten `kind:30004` (NIP-51) als zweite Schicht, Entfernen-Label `kind:1985` des Community-Schlüssels, eine Follow-Liste `kind:30000` als Personen-Liste, eine feste Quellenliste für den Kalender. Vier neue Hub-Ansichten (`v-sammlung`, `v-fortbildungen`, `v-personen`, `v-person`) und ein Katalog-Tab im Community-Raum. Jedes Issue wird ein PR-Branch `pr/<name>`, gestapelt, weil alle `index.html` ändern. Prüfungen bleiben textbasiert (`deno task test`), Verhaltenstests schneiden Funktionen aus dem Skript wie in `tests/inhalte.test.ts`.

**Tech Stack:** HTML/CSS/JavaScript ohne Framework, WebSocket zu Nostr-Relays (NIP-01; Kinds 0, 16, 1985, 30000, 30004, 30023, 30142, 31923; NIP-18 Reposts, NIP-32 Labels, NIP-19 npub/naddr), Deno 2 für Tests und Schnappschuss, ngit 3.0.4 (Konten `poutnik` und `joerg`, Amber), Wrapper `tools/poutnik`, Prüfwerkzeug `tools/nachweis/check.py`. Inhaltsstrang: `Website/navigation.yaml` im FOERBICO-Repo (mdparser `sync navigation` publiziert jede Liste darin als `kind:30004`), die edufeed-App für Listen der Community-Schlüssel (sie legt `kind:30000` und `kind:30004` an), WordPress-Plugin `amb-nostr` für den Einbetten-Schnipsel.

**Spec:** `docs/superpowers/specs/2026-11-02-hub-nachweis-gesamtkonzeption-design.md` (Abschnitte 3, 4.5, 4.6, 4.9, 4.10, 5a Inhaltsstrang, 7 Issues 1/2/5/6, 8 Fahrplan vierte Zeile, 9, 10). Vorbilder für Form und Ablauf: `docs/superpowers/plans/2026-11-06-hub-etappe-3-inhalte.md`, Übergabe `Hub-Entwicklung/2026-11-24-etappe-3-uebergabe.md`. Issue-Texte: `~/.config/poutnik/protokolle/issue-kommentare-2026-11-04/` (`01-sammlung.md`, `02-katalog-je-community.md`, `05-fortbildungskalender.md`, `06-personen.md`; nevent-Links in den `.fertig.json`). Schlüsselliste: `Hub-Entwicklung/communities-schluessel.md` (Stand 04.11.2026). Listen aus der Pipeline: `~/repositories/mdparser/sync/subcommands/navigation.ts` (jede Liste in `navigation.yaml` wird ein `kind:30004` mit `d` = Listenname und `a`-Tags auf `30023` desselben Autors). Shortcode-Attribute: `~/repositories/wp-plugins-nostr/shared/src/Query/QueryAttributes.php` (`community`, `authors`, `tags`, `search`, `limit`, `relays`) und `amb-nostr/src/SearchShortcode.php` (`fixed_level`, `fixed_subject`, `fixed_resource_type`, `filters`). Community-Logik von edufeed: Wiki-Artikel „Sharing and reading community content in edufeed“ (`kind:30818`, `d=edufeed-community-content-sharing`, Edufeed-Schlüssel `bdc21f93…`): Inhalt gehört zur Community über den `h`-Tag, Vorhandenes über `kind:16`-Reposts mit `a`/`e` und `h`, Lesen über `#h`, Entfernen über `kind:1985`-Label. Bedarf an das Team: `Hub-Entwicklung/2026-11-07-etappe-4-bedarf-team.md`.

**Issue-Kurz-IDs** (erste acht Hex-Zeichen der Event-ID): 01 Sammlung `b68eaaa5`, 02 Katalog `017a1143`, 05 Fortbildungskalender `0a7ccbf8`, 06 Personen `693c69cc`; Querschnitt 13 Live-Abfrage `bc8d97d8` (erledigt in Etappe 2), 17 rpi-virtuell-Instanz `353e3943` (erledigt), 11 eigene Instanz `93b36056` (Etappe 5), 07 Ökosystem-Karte `e6875f0b` (Etappe 5). Stand 05.11.2026: alle vier offen, ohne Antwort des Teams.

**Befund vom 05.11.2026 (Sondierung von `relay.edufeed.org`, Grundlage der Entscheidungen unten):**

- Listen `kind:30004`: im Projektumfeld gibt es nur Hauptmenü und Fußzeile des Schaufenster-Schlüssels (`d=navigation`, `d=fusszeile`, `a`-Tags auf `30023`). Keine der vier Communities rpi-virtuell, relilab, reliGlobal, ALPIKA Grundschule hat eine Katalog-Liste. Die übrigen 31 Listen auf dem Relay stammen aus fremden Apps (Musikprofile, Lesezeichen) und sind für den Hub bedeutungslos: Listen werden deshalb nur von den fünf bekannten Schlüsseln gelesen, nie global.
- Geteilte Inhalte über den `h`-Tag (Sondierung 05.11., 500 Events, Grenze erreicht): rpi-virtuell 26 Material-Reposts, 2 Beiträge, 8 Termine; relilab 16 Material-Reposts, 61 Artikel, 386 Termine (47 bevorstehend); reliGlobal 5 Material-Reposts, 1 Beitrag, 4 Termine; ALPIKA Grundschule 4 Material-Reposts, 4 Termine. Material kommt fast immer als `kind:16`-Repost mit `a`-Tag, Termine und Artikel meist direkt mit `h`-Tag. Jede Community hat damit heute schon einen sichtbaren Katalog; die Kuratierungsliste ist die zweite Schicht, nicht die Voraussetzung. Die Rollenprüfung moderierter Communities braucht die Mitgliederliste vom Gruppen-Relay, das der Hub nie liest; der Hub zeigt deshalb „wie geteilt, ohne Rollenprüfung“ und lässt nur weg, was die Community mit ihrem eigenen Schlüssel entfernt hat.
- Mitgliedschaften `kind:30000` mit `d=communities` (`p`-Tags = Community-Schlüssel): 167 Listen; Mitglieder der Hub-Communities: rpi-virtuell 34, relilab 25, Friedenspädagogik 8, ALPIKA Grundschule 6, reliGlobal 4, Konfiarbeit 3, KuRU 2; zusammen 53 Personen, 51 davon mit Profil `kind:0` (`name` 51, `about` 33, `picture` 33, `website` 24, `nip05` 11, `bot` 4). Darunter Personas („… (Persona)“), Versuchsprofile und hauptamtliche Personen mit `nip05`. Mitgliedschaft ist deshalb kein Einverständnis für eine Personen-Ansicht; dafür braucht es eine Liste.
- Folgen `kind:3`: die Community-Schlüssel folgen zwei bis drei Profilen. Folgen ist für den Launch ohne Signer nicht umsetzbar (Spec 8: „Personen als Liste ohne Folgen“ ist der zulässige Rückfall).
- Termine `kind:31923`: die 150 neuesten Events sind zu 139 Stück ein Import des Deutschen Bildungsservers; eine globale Abfrage ohne Absenderfilter würde den Fortbildungskalender mit fachfremden Terminen fluten. Religionspädagogische Absender und ihre Tags: relilab-Termine-Bot (369 Termine, davon 27 bevorstehend, `t=relilab` immer, `location` meist `Zoom: https://relilab.org/live`), relilab-impuls (10, `registrationUrl`, `contributor:*`), relilab (2, `registrationUrl`), reliGlobal (4, `price=0 EUR`, `h`, `educationalLevel:*`), Jörg Lohrer (11, darunter ptz-Termine, `h`, `price`), KPH Wien (1), ALPIKA Grundschule (1), rpi-virtuell (2), BiK-Import (`p … organizer`, keine neuen seit 21.01.2026). Merkmale für die zwei Logiken sind also vorhanden, aber uneinheitlich: `registrationUrl` (Anmeldung), `price` (Kosten), `location` mit Zoom/URL (online), `t=relilab` und Absender (Labor).
- Profile der Community-Schlüssel: rpi-virtuell, reliGlobal, ALPIKA Grundschule mit `name` und `about`; relilab und FOERBICO nur `name`; News-Redaktion und BiK-Import ohne Profil.

**Folgepläne (nicht Teil dieses Plans):** Etappe 5 bis 23.12. (Zeilen 4.1, 4.4, 4.7, 4.8, 4.17, 4.18, Erschließungs-Layer, Stufe B: Redaktionsoberfläche für Listen, Abonnieren als Nostr-Liste mit Signer, Folgen), Etappe 6 Januar.

## Global Constraints

- Launch-Stack ist der HTML-Prototyp: eine Datei `index.html`, kein Build, kein Framework, keine externen Abhängigkeiten außer Google Fonts (Spec 3).
- Relays, von denen der Hub liest: `wss://relay.edufeed.org`, `wss://relay-rpi.edufeed.org`, `wss://amb-relay.edufeed.org`. Nie `wss://groups.edufeed.org`. Je Ansicht ein `REQ` pro Relay mit allen Filtern der Ansicht, `MAX_CONN = 3`, `TIMEOUT_MS = 8000`, `RETRY_MS = 60000`, Cache in `sessionStorage` über `hubFetch(name, filters, opts)` (ADR-0006, `docs/daten.md`). Erlaubte Ausnahme dieser Etappe: eine zweite, abhängige Abfrage je Ansicht, wenn ihre Filter erst aus der ersten Antwort folgen (Katalog-Einträge, Personen-Profile); nie eine Subscription je Eintrag. Community-Inhalte werden nur mit `#h` auf die fünf festen Schlüssel gelesen, Listen, Labels und Profile nur mit `authors` aus festen Schlüsselmengen, nie global.
- Jede Ansicht zeigt sichtbar „live · …“, „Stand vom <Datum>“ oder „Nachbau · …“ über `datenstand(viewId, zustand, info)`; nichts wird als echt ausgegeben, was nicht vom Relay kam. Fehlende Inhalte (eine Community, mit der noch nichts geteilt ist; eine Personen-Liste, die noch nicht angelegt ist) erscheinen als „noch nichts geteilt“ oder „noch nicht angelegt“ mit Einladung und Verweis, nie als leere Seite und nie als toter Link. Keine Antwort der Relays heißt „Die Relays antworten gerade nicht“, nicht „noch nichts geteilt“. Community-Inhalte tragen den Zusatz „ohne Rollenprüfung“, weil der Hub das Gruppen-Relay nicht liest.
- Inhalte vom Relay sind fremder Text: Namen, `about`, Titel, Listen-Titel werden mit `esc()` maskiert; `href` und `src` nur über `sichereUrl()`; Schlüssel aus Events nur über `istHex64()` in Adressen und Filter; `a`-Tags werden erst nach Prüfung auf das Muster `^\d+:[0-9a-f]{64}:` ausgewertet, `e`-Tags nur mit 64 Hex.
- Farbsystem nach ADR-0001: Bereichsfarben nur in `:root`; neue Farben als Fläche plus Textfarbe mit mindestens 4,5:1 auf `--paper`, `--card` und dem eigenen Hellton; Fokus sichtbar. Sammlung und Kalender tragen die Farbe „finden“, Personen die Farbe „kooperieren“.
- Die vier Hub-Ergänzungen je Instanz bleiben (ADR-0002 Punkte 2 bis 4); Porträts unter © werden nicht übernommen (ADR-0002 Punkt 3): Profilbilder kommen nur aus `kind:0` `picture` der Person selbst, die Teamseite bleibt Schnappschuss mit Initialen.
- Lizenzregel aus Etappe 3 (ADR-0007 Punkt 5) gilt in Sammlung und Katalog: Pille je Eintrag, Lizenzfilter mit den drei Ständen `offen`, `geschuetzt`, `unbekannt`; „In Sammlung aufnehmen“ bleibt nur bei `offen` aktiv.
- Keine Arbeitspakete, Meilensteine, AP-/M-Nummern, Förderkennzeichen, kein Projektträger, kein Zwischenbericht in Code, Docs, ADRs, Commits, PR-Texten, Issue-Kommentaren. Prüfung: `deno task test` und `python3 -I tools/nachweis/check.py gitworkshop <ordner>` über jeden Entwurfsordner vor der Veröffentlichung.
- Keine Vornamen von Partnern in Dateien, Commits oder Kommentaren; Rollen („die Redaktion“, „der Leit-Maintainer“, „der UX-Gast“), Handles, Pubkey-Präfixe. Erlaubt: „Jörg Lohrer“, „Jens Dechow“. Namen, die ein Event selbst trägt (`kind:0` `name`), werden angezeigt, nicht in den Code geschrieben; die einzige Ausnahme bleibt der Name der News-Redaktion, weil ihr Schlüssel kein Profil hat.
- Keine privaten Schlüssel, `nsec`, Bunker-Links oder Tokens in Dateien oder im Gespräch; nur `npub` und Hex-Pubkeys.
- Hub-Texte auf Deutsch in Du-Ansprache; neue Texte nennen den Hub nicht beim Namen (Faden „Selbstverständnis“ offen).
- Konsolen-Struktur bleibt (fünf Funktionen, zwölf Aktionen): keine neue Knospe für „Sammlung“; die Sammlung wird aus dem Materialpool, aus den Katalogen und aus der Erklärkarte `finden.material` erreicht. `finden.fortbildungen` und `kooperieren.personen` bekommen ihre Ziele; `later()` bleibt nur in `standardAktion` und wird danach von keiner Aktion mehr erreicht.
- Commits auf PR-Branches mit Author `Poutník <poutnik@users.noreply.edufeed.org>`; Branch `pr/<name>` ab dem Kopf des vorigen Branches (gestapelt), der erste ab `main` (`255b295`); Push nur über `cd ~/repositories/FOERBICO_und_rpi-virtuell/tools/poutnik && deno task push pr/<name> --as poutnik --cwd ~/repositories/reli-hub`, nie `git push origin`. `deno.lock` im Klon nie committen; Dateiserver für Browserprüfungen außerhalb des Repos starten (`cd /tmp && deno run --allow-net --allow-read jsr:@std/http/file-server ~/repositories/reli-hub`).
- Merge und Push von `main` nur durch Jörg (Ablauf unten). Nichts wird veröffentlicht, gepusht oder kommentiert ohne sein Ja.
- Tests dieser Etappe liegen in `tests/sammlung.test.ts` (Tasks 1 bis 3) und `tests/kalender-personen.test.ts` (Tasks 4 und 5); die 49 Tests aus `index`, `navigation`, `datenschicht`, `inhalte` bleiben grün. Zwei bestehende Zusicherungen ändern sich bewusst: `navigation.test.ts` erwartet für `kooperieren.personen` kein Ziel mehr (Task 5 ersetzt die Zeile), und die Zählung „jede Ansicht außer Start hat eine Stand-Zeile“ bleibt gültig, weil jede neue Ansicht eine bekommt. Prüfbefehl in jedem Task: `cd ~/repositories/reli-hub && deno task test`.
- Schnittregel der Tests: Funktionen des Anwendungsskripts beginnen mit zwei Leerzeichen (`  function name(…) {`) und enden mit `\n  }`; innere Zeilen sind tiefer eingerückt. Funktionen, die ein Test mit `new Function` baut (`aTagLesen`, `repostZiel`, `listeEintraege`, `entferntAus`, `coEintraege`, `sammlungFilter`, `sammlungPasst`, `terminLogik`, `terminMerkmale`, `shortcodeAus`, `kontextprofilAus`, `profilAus`), rufen außer `esc`, `sichereUrl`, `istHex64`, `tagWert`, `tagWerte` und den im Test mitgeschnittenen Blöcken (`aTagLesen`, `repostZiel`, `mpPasst`, `bech32`, `CO_SCHLUESSEL`, `KAL_HEX`, `RL_HEX`, `RELAYS`) nichts aus dem Skript auf.
- Rückfallreihenfolge dieser Etappe (Spec 8, auf Inhalte übertragen): Gerät der 07.12. in Gefahr, fällt zuerst in Task 2 das Abonnieren-Panel weg (Teilen und Einbetten bleiben), dann in Task 5 die Profilseite `#person` (die Liste bleibt), dann in Task 4 die Merkmal-Chips (die zwei Logik-Filter bleiben). Nicht verhandelbar: Task 1 (geteilte Inhalte lesen), Task 2 (Sammlung mit Filtern und Einbetten), Task 3 (fünf Katalog-Seiten mit Grundschicht), Task 4 (Kalender über alle Quellen mit zwei Logiken), Task 5 (Personen-Liste), weil sie die Zeilen 4.5, 4.6, 4.9, 4.10 tragen; Task 7 ist Inhalt, kein Code, und kann nach dem 07.12. nachlaufen.

## Was der Hub ohne Listen und Profile zeigt (gekennzeichneter Rückfall)

Die Fachtagung am 17./18.11.2026 liegt vor der Frist dieser Etappe. Wird ein Branch vorher gemergt, gilt je Zeile dieser Zustand, solange das Team die Inhalte nicht geliefert hat (Bedarfsliste in `Hub-Entwicklung/2026-11-07-etappe-4-bedarf-team.md`). Kataloge brauchen keine Liste mehr: Was die Communities über den `h`-Tag teilen, ist heute schon ihr Katalog.

| Zeile | Ohne Inhalt vom Team | Kennzeichnung | Sobald geliefert |
|---|---|---|---|
| 4.5 Sammlung | voll nutzbar: Filter über die Materialien der drei Relays (`mpDaten`), Teilen, Einbetten, Abonnieren-Panel; der Community-Filter greift auf das, was die Community geteilt hat | `live · <n> Materialien · abgefragt bei 3 Relays` | mehr geteilte Materialien je Community |
| 4.6 Kataloge | je Community die Grundschicht „In der Community geteilt“ (Stand 05.11.: reliGlobal 5 Materialien und 4 Termine, relilab 16 Materialien, 61 Artikel, 47 bevorstehende Termine, rpi-virtuell 26 Materialien, ALPIKA Grundschule 4 Materialien und 4 Termine); keine Kuratierungsliste; bei rpi-virtuell zusätzlich der Materialpool mit Zähler | `live · <n> geteilt · 0 Listen · ohne Rollenprüfung` | Schicht „Vom Redaktionskreis zusammengestellt“ mit Stand der Liste |
| 4.9 Kalender | voll nutzbar: Termine der bekannten Absender; Merkmale nur, wo Tags vorhanden sind (sonst „keine Angabe“) | `live · <n> Termine · <k> Quellen` | mehr Quellen (ALPIKA, Institute), vollständigere Merkmale |
| 4.10 Personen | Teamseite als Schnappschuss mit Initialen (`OC_TEAM`), Satz „Die Personen-Liste ist noch nicht angelegt“; `#person?p=<npub>` zeigt jedes echte Profil, dessen npub man kennt | `Stand vom 04.11.2026 · Teamseite, Personen-Liste fehlt` | Karten aus `kind:0` mit Bild, Rolle, Communities, Profilseite |

## Review Focus

1. Ein `a`-Tag einer Liste oder eines Reposts mit fremdem Kind, kaputtem Schlüssel oder leerem `d` (`30023:abc:`, `kind:5a12…:x` ohne 64 Hex): `aTagLesen` liefert `null`, `repostZiel` lässt den Repost aus, `listeEintraege` zählt den Eintrag als „nicht auflösbar“; nichts landet in einem Filter (Task 1, Test `aTagLesen, repostZiel und listeEintraege: nur gültige Adressen`).
2. Listen-Titel, Profilname oder `about` mit HTML oder `</script>`: alle Texte gehen durch `esc()`, `picture` und `website` nur über `sichereUrl()`; ein `data:`-Bild wird Platzhalter mit Initiale (Task 3 Test `Katalog-Tab: … Titel maskiert`, Task 5 Test `profilAus: maskiert, sichere Adressen, Bots erkannt`).
3. Relays antworten nicht, während eine Katalog-Seite oder die Personen-Ansicht offen ist: „Die Relays antworten gerade nicht“ statt „noch nichts geteilt“ beziehungsweise Teamseite als Schnappschuss; die Stand-Zeile springt nicht auf „live“ (Task 3 Test `Katalog-Tab: … drei Zustände`, Task 5 Test `Personen: Rückfall Teamseite`).
4. Ein Entfernen-Label eines fremden Schlüssels oder ein Repost auf ein gelöschtes Event: das Label zählt nicht (nur der Community-Schlüssel), der Repost ergibt die Karte „nicht auflösbar“ ohne Link statt einer leeren Stelle; ein Termin ohne `location`, `registrationUrl` und `price` bleibt im Kalender mit „keine Angabe“ (Task 1 Test `coEintraege und entferntAus`, Task 4 Test `terminLogik und terminMerkmale: fehlende Tags`).
5. Relay-Last auf der Tagung: Sammlung nutzt `mpDaten` und, nur mit Community-Filter, den Cache von `coLaden`; eine Katalog-Seite liest ihre Community mit einem `REQ` je Relay und löst Einträge zuerst aus `mpDaten` und `ocDaten`, danach mit genau einer Nachfrage; Kalender und rpi-virtuell-Tab teilen sich die Abfrage `kalender`; Personen brauchen höchstens zwei `REQ` je Relay (Task 1 Test `coLaden: ein REQ je Community`, Task 2 Test `Sammlung: keine eigene Abfrage`, Task 4 Test `kalLaden: eine Abfrage für Kalender und rpi-virtuell`, Task 5 Test `peLaden: zwei Abfragen, feste Autoren`).

---

## Merge-Ablauf (gilt für jeden Task, wird dort nur referenziert)

Vorbereitung vor dem ersten Push: `cd ~/repositories/reli-hub && git checkout main && git -c nostr.signer=joerg fetch origin main && git log --oneline main..origin/main` (leer heißt: `main` unverändert, sonst `git merge --ff-only origin/main` und den Stapel rebasen).

PR öffnen (nach Jörgs Ja zum Diff): `cd ~/repositories/FOERBICO_und_rpi-virtuell/tools/poutnik && deno task push pr/<name> --as poutnik --cwd ~/repositories/reli-hub` (ausgecheckt muss der Branch sein). Erwartet: `posting proposal as PR event`, kein Patch-Rückfall. PR-Beschreibung: Issue mit Kurz-ID und gitworkshop-Link, Entscheidung in zwei Sätzen, Prüfbefehl `deno task test`.

Mergen (Jörg): `cd ~/repositories/reli-hub && git checkout pr/<name> && ngit --signer joerg pr merge --offline`, nach allen Merges einmal `cd ~/repositories/FOERBICO_und_rpi-virtuell/tools/poutnik && deno task push main --as joerg --cwd ~/repositories/reli-hub` (Amber) und `cd ~/repositories/reli-hub && git push forgejo main`. Erwartet: gitworkshop zeigt die PRs als erledigt, `curl -s https://hub.rpi-virtuell.net/ | grep -c coLaden` ist größer als 0 (Auslieferung dauert bis zu 30 Minuten).

Wie in Etappe 3 gilt: Bringt die Gesamt-Review am Ende eine Fix-Welle, kommt sie als eigener Branch `pr/nacharbeit-etappe-4` auf den Stapel, und der Stapel wird in einer Sitzung vollständig gemergt.

---

### Task 1: Community-Inhalte und Listen: geteilte Inhalte über den `h`-Tag, Reposts auflösen, Kuratierungslisten, Entfernen-Label (Querschnitt für Issues 01, 02, 06)

**Files:** Modify `index.html` (Anwendungsskript, direkt nach dem Block „Inhalte aus Events“: neuer Block „Community-Inhalte und Listen (ADR-0008)“; Konstante `CY`: neuer Eintrag `alpika-gs`), Create `tests/sammlung.test.ts`, Modify `docs/daten.md` (Abschnitt „Community-Inhalte und Listen“). Branch `pr/community-inhalte` ab `main`.

**Interfaces:**
- Consumes: `hubFetch`, `npubToHex`, `istHex64`, `tagWert`, `tagWerte`, `esc`, `sichereUrl`, `mpLaden`/`mpDaten`, `mpMaterial`, `ocLaden`/`ocDaten`, `FO_HEX`, `naddr`, `evToTermin`, `beitragUrl`, `bech32`.
- Produces:
  - `const CO_SCHLUESSEL = [ { id: 'rpi-virtuell', n: 'rpi-virtuell', npub: 'npub14esenw6rt4c2pmxwvyey4jqw0sjdahetq6qvh5lffxp7w4thg63ql480z2', pool: true }, { id: 'relilab', n: 'relilab', npub: 'npub1fpcxaz2wvjl90gjs60x37ny2pa5u4yqfx7fklz73rgfjnnfujl3sr2fxgk' }, { id: 'religlobal', n: 'reliGlobal', npub: 'npub12atlgghwe2qwkps9sgm9z4je825hskh47ef7kc28zzgn5tztgtyqyveeqs' }, { id: 'alpika-gs', n: 'ALPIKA Grundschule', npub: 'npub10gyagq3eev0vcnqks69gewz22kvpe2989c5zua88huarjwwl04dqdzrmzr' }, { id: 'oercommunity', n: 'FOERBICO', npub: 'npub1tgftg8kptdrxxg0g3sm3hckuglv3j0uu3way4vylc5qyt0f44m0s3gun6e', eigene: true } ]`, je Eintrag `hex` = `npubToHex(npub)` beim Laden ergänzt; `id` ist die `CY`-Kennung, `pool: true` markiert die Community, deren Katalog zusätzlich der Materialpool ist (Spec 4.6), `eigene: true` den Schaufenster-Schlüssel ohne Community: seine Grundschicht sind die eigenen Events aus `ocDaten`, nicht der `h`-Tag. `CY` bekommt den Eintrag `{ id: 'alpika-gs', n: 'ALPIKA Grundschule', ab: 'AG', col: C.kooperieren, ty: 'netz', bio: 'Arbeitsgruppe der religionspädagogischen Institute für die Grundschule.', back: 'Dozentinnen und Dozenten der Pädagogischen Institute und Zentren arbeiten hier an Material und Vokabular für den Religionsunterricht in der Grundschule.', m: 6 }`.
  - `function aTagLesen(wert)` → `{ kind: number, pk: string, d: string } | null`: nur bei Muster `^(\d+):([0-9a-f]{64}):(.+)$`, sonst `null`.
  - `function repostZiel(ev)` → `{ adr: '<kind>:<pk>:<d>', kind, pk, d } | { adr: 'e:<id>', id, kind } | null`: zuerst der erste `a`-Tag über `aTagLesen`, sonst der erste `e`-Tag mit 64 Hex; `kind` bei `e`-Zielen aus dem `k`-Tag (Zahl) oder `0`.
  - `function listeEintraege(ev)` → `{ d, titel: tagWert('title') || d, beschreibung: tagWert('description'), bild: sichereUrl(tagWert('image')), stand: ev.created_at, eintraege: [{ adr, kind, pk, d }], unaufloesbar: number }` aus den `a`-Tags in Reihenfolge, Duplikate entfernt.
  - `function entferntAus(labels, hex)` → `Set<string>` der Werte aus `e`- (als `e:<id>`) und `a`-Tags (als Adresse) aller `kind:1985`-Events, die `pubkey === hex` haben und `['l','remove','communikey.moderation']` tragen; Labels anderer Absender zählen nicht (die Rollen der Moderation stehen auf dem Gruppen-Relay, das der Hub nie liest).
  - `function coLaden(hex)` → `Promise<{ antwort: boolean, direkt: ev[], reposts: ev[], listen: listeEintraege[], entfernt: Set<string> }>`, einmal je Community und Sitzung (`coDaten` Map; leere Antwort nicht gehalten): für `eigene: true` aus `ocLaden()` (`direkt` = Seiten, Beiträge, Termine des Schlüssels, `reposts` leer, Listen aus `ocDaten.listen` plus Listen mit `d` `katalog…`); sonst `hubFetch('community:' + hex, [{ kinds: [30142, 30023, 31923], '#h': [hex], limit: 150 }, { kinds: [6, 16], '#h': [hex], limit: 150 }, { kinds: [30004], authors: [hex], limit: 20 }, { kinds: [1985], '#h': [hex], '#L': ['communikey.moderation'], authors: [hex], limit: 100 }])` auf allen drei Relays; adressierbare Events je `kind:pubkey:d` auf das neueste `created_at` gekürzt; `listen` = Listen mit `d` gleich `katalog` oder beginnend mit `katalog-` (Konvention des Inhaltsstrangs), `katalog` zuerst, dann nach `created_at` absteigend; `antwort` = mindestens ein Event kam.
  - `function coEintraege(daten)` → `[{ adr, kind, pk, d, ev: ev|null, geteilt: pk|null, zeit }]`: direkte Events (`adr` aus Kind, Pubkey, `d`; `zeit` = `created_at`; `geteilt` = `null`; `ev` gesetzt) und Repost-Ziele (`repostZiel`; `geteilt` = Pubkey des Reposts; `zeit` = `created_at` des Reposts; `ev` = `null`, bis `eintraegeAufloesen` es setzt); je Adresse ein Eintrag (der neueste `zeit` gewinnt); Einträge, deren `adr` oder `e:<id>` in `entfernt` liegt, fallen weg; sortiert nach `zeit` absteigend. Keine Rollenprüfung: Was mit dem `h`-Tag geteilt wurde, gilt als geteilt (Grenze in ADR und Stand-Zeile).
  - `function eintraegeAufloesen(eintraege)` → `Promise<Map<adr, ev>>`: zuerst aus `mpDaten` (Feld `ev`) und `ocDaten`; was fehlt, in **einer** Abfrage `hubFetch('aufloesen:' + <Verkettung der fehlenden Adressen, gekürzt auf 200 Zeichen>, [{ kinds: [30142, 30023, 31923], authors: [<distinct pk>], '#d': [<distinct d>] }, { ids: [<e-Ziele>] }])` (zweiter Filter nur bei `e`-Zielen; Obermenge, danach clientseitig auf die exakten Adressen gefiltert; `limit` = Zahl der Adressen plus 10); kein zweiter Aufruf je Eintrag.
  - `function eintragKarte(e)` → HTML-String einer Karte je Kind: `30142` über `mpMaterial(e.ev)` mit Lizenzpille und Link `#materialpool?d=…&p=…`; `30023` mit Titel, Datum, Link `beitragUrl` (Schaufenster-Schlüssel) oder `https://edufeed.org/<naddr>` (andere); `31923` über `evToTermin` mit Datum und Link `e.u`; `e.geteilt` ergibt die Zeile „geteilt von <Name aus CO_SCHLUESSEL oder gekürzter npub>“; `ev === null` ergibt „nicht auflösbar: <adr>“ ohne Link. Alle Texte über `esc`.

- [ ] **Step 1: Tests schreiben** (`tests/sammlung.test.ts`; Technik aus `tests/inhalte.test.ts`: `block`, `bau`, `esc`, `sichereUrl`, zusätzlich `istHex64`, `tagWert`, `tagWerte` mitgeben)

```ts
import { assert, assertEquals } from 'jsr:@std/assert@1';
import { appScript, html } from './helfer.ts';
const s = appScript();
const block = (re: RegExp) => (s.match(re) || [''])[0];
const esc = (t: string) => String(t).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]!));
const sichereUrl = (u: string) => /^https?:\/\//.test(u || '') ? u : '';
const istHex64 = (x: string) => /^[0-9a-f]{64}$/.test(x || '');
const tagWert = (ev: any, n: string) => (ev.tags.find((t: string[]) => t[0] === n) || [])[1] || '';
const tagWerte = (ev: any, n: string) => ev.tags.filter((t: string[]) => t[0] === n).map((t: string[]) => t[1]);
const fn = (name: string) => block(new RegExp(`  function ${name}\\([^)]*\\) \\{[\\s\\S]*?\\n  \\}`));
const bau = (name: string, extra = '') => new Function('esc', 'sichereUrl', 'istHex64', 'tagWert', 'tagWerte', extra + fn(name) + `; return ${name};`)(esc, sichereUrl, istHex64, tagWert, tagWerte);

Deno.test('Community-Inhalte: Konstanten, Signaturen, Doku', async () => {
  const k = block(/const CO_SCHLUESSEL = \[[\s\S]*?\n  \];/);
  for (const id of ['rpi-virtuell', 'relilab', 'religlobal', 'alpika-gs', 'oercommunity']) assert(k.includes(`id: '${id}'`), id);
  assert(/pool: true/.test(k) && /eigene: true/.test(k) && (k.match(/npub1[0-9a-z]{58}/g) || []).length === 5, 'fünf npubs, Pool- und Schaufenster-Markierung');
  for (const f of ['aTagLesen(wert)', 'repostZiel(ev)', 'listeEintraege(ev)', 'entferntAus(labels, hex)', 'coLaden(hex)', 'coEintraege(daten)', 'eintraegeAufloesen(eintraege)', 'eintragKarte(e)']) assert(s.includes('function ' + f), f);
  assert(/id: 'alpika-gs'/.test(block(/const CY = \[[\s\S]*?\n  \];/)), 'ALPIKA Grundschule in CY');
  const d = await Deno.readTextFile(new URL('../docs/daten.md', import.meta.url));
  assert(/coLaden/.test(d) && /'#h'/.test(d) && /ohne Rollenprüfung/.test(d) && /katalog-/.test(d), 'docs/daten.md');
});

Deno.test('aTagLesen, repostZiel und listeEintraege: nur gültige Adressen', () => {
  const a = bau('aTagLesen'), rz = bau('repostZiel', fn('aTagLesen')), le = bau('listeEintraege', fn('aTagLesen'));
  const pk = 'ab'.repeat(32), id = 'cd'.repeat(32);
  assertEquals(a(`30142:${pk}:https://x.org/r`), { kind: 30142, pk, d: 'https://x.org/r' });
  assertEquals(a('30023:abc:x'), null); assertEquals(a(`30023:${pk}:`), null); assertEquals(a(`kind:${pk}:x`), null);
  assertEquals(rz({ tags: [['e', id], ['a', `30142:${pk}:m1`], ['k', '30142']] }), { adr: `30142:${pk}:m1`, kind: 30142, pk, d: 'm1' }, 'a vor e');
  assertEquals(rz({ tags: [['e', id], ['k', '31923']] }), { adr: `e:${id}`, id, kind: 31923 });
  assertEquals(rz({ tags: [['e', 'kaputt']] }), null);
  const ev = { kind: 30004, pubkey: pk, created_at: 5, content: '', tags: [['d', 'katalog'], ['title', '<b>Katalog</b>'], ['a', `30142:${pk}:m1`], ['a', `30142:${pk}:m1`], ['a', '30023:kaputt:x'], ['a', `31923:${pk}:t1`], ['image', 'javascript:alert(1)']] };
  const l = le(ev);
  assertEquals(l.eintraege.length, 2); assertEquals(l.unaufloesbar, 1); assertEquals(l.bild, ''); assertEquals(l.stand, 5); assertEquals(l.titel, '<b>Katalog</b>');
});

Deno.test('coEintraege und entferntAus: Reposts aufgelöst, Entfernen nur vom Community-Schlüssel', () => {
  const co = 'ee'.repeat(32), pk = 'ab'.repeat(32), id = 'cd'.repeat(32);
  const ea = bau('entferntAus'), ce = bau('coEintraege', fn('aTagLesen') + fn('repostZiel'));
  const labels = [
    { kind: 1985, pubkey: co, tags: [['L', 'communikey.moderation'], ['l', 'remove', 'communikey.moderation'], ['h', co], ['e', id], ['a', `30142:${pk}:weg`]] },
    { kind: 1985, pubkey: pk, tags: [['L', 'communikey.moderation'], ['l', 'remove', 'communikey.moderation'], ['h', co], ['a', `30142:${pk}:bleibt`]] }
  ];
  const ent = ea(labels, co);
  assert(ent.has(`e:${id}`) && ent.has(`30142:${pk}:weg`) && !ent.has(`30142:${pk}:bleibt`), 'nur der Community-Schlüssel entfernt');
  const daten = { antwort: true, entfernt: ent, listen: [],
    direkt: [{ id: 'x1', kind: 31923, pubkey: pk, created_at: 10, tags: [['d', 't1']] }, { id: 'x2', kind: 30142, pubkey: pk, created_at: 11, tags: [['d', 'weg']] }],
    reposts: [{ kind: 16, pubkey: co, created_at: 20, tags: [['a', `30142:${pk}:m1`], ['k', '30142']] }, { kind: 16, pubkey: co, created_at: 21, tags: [['a', `30142:${pk}:m1`]] }, { kind: 16, pubkey: co, created_at: 22, tags: [['e', id], ['k', '30023']] }] };
  const e = ce(daten);
  assertEquals(e.map((x: any) => x.adr), [`30142:${pk}:m1`, `31923:${pk}:t1`], 'entfernt weg, Duplikat einmal, neueste zuerst');
  assertEquals(e[0].geteilt, co); assertEquals(e[0].zeit, 21); assertEquals(e[1].geteilt, null); assertEquals(e[0].ev, null);
});

Deno.test('coLaden: ein REQ je Community, h-Tag statt Autoren, Listen und Labels mitgeholt', () => {
  const k = fn('coLaden');
  assert(/hubFetch\('community:' \+ hex, \[/.test(k) && /kinds: \[30142, 30023, 31923\], '#h': \[hex\]/.test(k) && /kinds: \[6, 16\], '#h': \[hex\]/.test(k), 'Inhalt und Reposts über h');
  assert(/kinds: \[30004\], authors: \[hex\]/.test(k) && /kinds: \[1985\], '#h': \[hex\], '#L': \['communikey\.moderation'\], authors: \[hex\]/.test(k), 'Listen und Labels nur vom Schlüssel');
  assert(/eigene/.test(k) && /ocLaden\(\)/.test(k), 'Schaufenster ohne Community aus ocDaten');
  assert(!/kinds: \[30004\] \}/.test(k) && !/groups\.edufeed\.org/.test(html), 'nie global, nie das Gruppen-Relay');
  const e = fn('eintraegeAufloesen');
  assert(/mpDaten/.test(e) && /ocDaten/.test(e) && e.indexOf('mpDaten') < e.indexOf('hubFetch') && (e.match(/hubFetch\(/g) || []).length === 1, 'Cache vor Netz, eine Nachfrage');
  assert(/kinds: \[30142, 30023, 31923\]/.test(e) && /'#d'/.test(e) && /ids: /.test(e), 'Obermenge nach Kind, Autor, d und ids');
});
```

- [ ] **Step 2: Fehlschlag sehen** · Run: `deno task test` · Expected: vier FAIL in `sammlung.test.ts`, 49 PASS.

- [ ] **Step 3: Block „Community-Inhalte und Listen“ schreiben** (Konstante, acht Funktionen, `coDaten`-Halter), `CY`-Eintrag, `docs/daten.md` um den Abschnitt „Community-Inhalte und Listen“ ergänzen (die vier Filter, Konvention `d=katalog`/`katalog-<thema>`, Auflösung Cache vor Netz, Regel „ohne Rollenprüfung“ und Entfernen-Label nur vom Community-Schlüssel, Grenze `limit` 150 je Art bei großen Communities).

- [ ] **Step 4: Tests laufen lassen** · Expected: grün (53).

- [ ] **Step 5: Committen, PR** (`pr/community-inhalte`)

```bash
git add index.html tests/sammlung.test.ts docs/daten.md && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "Community-Inhalte und Listen: geteilte Inhalte über den h-Tag, Reposts aufgelöst, Kuratierungslisten und Entfernen-Label der fünf Hub-Communities"
```

### Task 2: Sammlung: filtern, teilen, einbetten, abonnieren (Issue 01 `b68eaaa5`, Spec 4.5)

**Files:** Modify `index.html` (neue Ansicht `<div class="view" id="v-sammlung" data-stand="nachbau:Materialien laden">` nach `v-materialpool`; Anwendungsskript: `sammlungFilter`, `sammlungPasst`, `shortcodeAus`, `kontextprofilAus`, `saOpen(qs)`, `saRender()`; `route()`: Zweig `finden/<sub>`; Materialpool-Kopf: Knopf „Sammlung zusammenstellen ›“; `EX['finden.material']`: zweiter Satz mit Link; Material-Detail: Aktion „In Sammlung aufnehmen“ führt zu `#finden/sammlung?q=<Titel>` statt Toast; CSS-Block „Sammlung“), Modify `tests/sammlung.test.ts`, `docs/daten.md`, `docs/navigation.md` (Zeile „Sammlung“). Branch `pr/sammlung` ab `pr/community-inhalte`.

**Interfaces:**
- Consumes: `mpLaden`, `mpDaten` (Felder `t, x, art, stufe, fach, lic, stand, pk, d, ev`), `mpPasst`, `ambWerte`, `lizenzStand`, `lizenzLabel`, `coLaden`, `coEintraege`, `CO_SCHLUESSEL`, `datenstand`, `rtCopy`, `toast`, `naddr`, `bech32`.
- Produces:
  - Route `#finden/sammlung?c=<community-id>&fach=<prefLabel>&stufe=<prefLabel>&lizenz=offen|geschuetzt|unbekannt&q=<begriffe>`; `route()` bildet `finden/<sub>` auf die Ansicht `v-<sub>` ab (`sammlung`, ab Task 4 auch `fortbildungen`), unbekannter `sub` führt zur Startseite mit Toast.
  - `function sammlungFilter(qs)` → `{ c: string, fach: string[], stufe: string[], lizenz: string, q: string[] }` aus `URLSearchParams` (`fach` und `stufe` mehrfach, `q` an Leerzeichen getrennt; unbekannter `lizenz`-Wert wird `''`).
  - `function sammlungPasst(m, f, coAdressen)` → boolean: `fach` trifft, wenn ein `about:prefLabel:de` gleich ist (ohne Groß-/Kleinschreibung), `stufe` ebenso auf `educationalLevel:prefLabel:de`, `lizenz` auf `m.stand`, `q` über `mpPasst(m, f.q)`; `c` trifft, wenn `m.pk` der Schlüssel der Community ist oder `30142:<pk>:<d>` in `coAdressen` liegt (Set der Adressen aller mit der Community geteilten Materialien aus `coEintraege(coLaden(hex))`, Task 1; dieselbe Logik wie der Shortcode-Parameter `community` des WordPress-Plugins).
  - `function saRender()`: Kopf „Sammlung“ mit Satz „Stelle dir aus den Materialien der Communities eine Auswahl zusammen und nimm sie mit auf deine Seite.“; Filterleiste: Auswahlfelder Community (aus `CO_SCHLUESSEL`; nach dem Laden steht die Zahl der geteilten Materialien dahinter), Fach und Stufe (Werte aus den vorhandenen Materialien gesammelt, alphabetisch), Lizenz (drei Stände mit Pillenfarbe), Suchfeld; jede Änderung schreibt die Route (`history.replaceState`) und rendert neu; Trefferliste als `mp-card`-Karten (wie `mpRender`, alle Treffer, nach Datum), leer: „Nichts gefunden; Filter lockern.“; Stand-Zeile `live · <n> von <m> Materialien · abgefragt bei 3 Relays`, ohne Daten `Nachbau · Materialien laden` beziehungsweise nach Fehlschlag `Nachbau · Relays nicht erreichbar`. Drei Ausgänge als Knöpfe über der Liste: **Teilen** (`rtCopy(location.href, 'Link zu dieser Sammlung kopiert.')`); **Einbetten** öffnet `<details id="saEinbetten">` mit zwei Schnipseln und Kopierknöpfen: (a) WordPress `shortcodeAus(f)`, (b) Kontextprofil `kontextprofilAus(f)` als JSON mit Satz „Für die Steuerkonsole als eigenständiges Skript (`config-src`); das Skript folgt mit dem Issue ‚Eigene Instanz‘.“; **Abonnieren** öffnet `<details id="saAbo">` mit dem Nostr-Filter als `REQ`-JSON zum Kopieren („in jeder Nostr-App als Abfrage nutzbar“), einem deaktivierten Knopf „Als Nostr-Liste speichern“ (`disabled aria-disabled="true"`, Hinweis „braucht Anmeldung mit Schlüssel, folgt“) und dem ehrlichen Satz „Ein Feed zu einem beliebigen Filter braucht einen Server; der Hub hat keinen.“
  - `function shortcodeAus(f)` → String: `[amb_nostr_search` plus `community="<npub>"` (bei `c`), `search="<q>"`, `fixed_level="<id>"` und `fixed_subject="<id>"` (die Vokabular-Kennungen der gewählten Begriffe aus `ambWerte`, erste Treffer), `limit="12"`, `button="Suchen"]`; Werte mit `"` werden entfernt; ohne Filter `[amb_nostr limit="12"]`. Lizenz hat im Plugin kein Attribut: der Schnipsel bekommt die Kommentarzeile `<!-- Lizenzfilter: <stand>; das Plugin zeigt die Lizenz je Treffer -->`.
  - `function kontextprofilAus(f)` → Objekt `{ name: 'Sammlung', version: 1, actions: { 'finden.material': { params: { thema: f.q, stufe: f.stufe } } }, sammlung: { community: <npub|null>, fach: f.fach, stufe: f.stufe, lizenz: f.lizenz, q: f.q, relays: RELAYS } }`, als `JSON.stringify(…, null, 2)`.
  - `function saOpen(qs)`: aus `route()`; zeigt sofort die Filterleiste, ruft `mpLaden()` und, nur wenn `f.c` gesetzt ist, `coLaden(hex der Community)` (parallel, `Promise.all`), rendert danach; mit Daten im Cache ohne Netz.
  - `docs/navigation.md`: neue Zeile „Sammlung | – | – (über Materialpool und Erklärkarte) | `#finden/sammlung` | – | finden | gebaut“.

- [ ] **Step 1: Tests ergänzen**

```ts
Deno.test('sammlungFilter und sammlungPasst', () => {
  const KAT = block(/const CO_SCHLUESSEL = \[[\s\S]*?\n  \];/);
  const sf = bau('sammlungFilter'), sp = bau('sammlungPasst', KAT + fn('mpPasst'));
  const f = sf('c=religlobal&fach=Ethik&fach=Religion&stufe=Sekundarstufe%20I&lizenz=offen&q=Frieden%20Schule&lizenz=kaputt');
  assertEquals(f.c, 'religlobal'); assertEquals(f.fach, ['Ethik', 'Religion']); assertEquals(f.stufe, ['Sekundarstufe I']); assertEquals(f.q, ['Frieden', 'Schule']);
  assertEquals(sf('lizenz=kaputt').lizenz, '');
  const pk = 'cd'.repeat(32), m = { t: 'Frieden in der Schule', x: '', fach: 'Religion', stufe: 'Sekundarstufe I', art: 'Arbeitsblatt', stand: 'offen', pk, d: 'm1', ev: { tags: [['about:prefLabel:de', 'Religion'], ['educationalLevel:prefLabel:de', 'Sekundarstufe I'], ['keywords', 'Frieden']] } };
  assert(sp(m, { c: '', fach: ['religion'], stufe: [], lizenz: 'offen', q: ['frieden'] }, new Set()));
  assert(!sp(m, { c: '', fach: ['Ethik'], stufe: [], lizenz: '', q: [] }, new Set()));
  assert(!sp(m, { c: 'religlobal', fach: [], stufe: [], lizenz: '', q: [] }, new Set()), 'nicht geteilt und fremder Schlüssel: kein Treffer');
  assert(sp(m, { c: 'religlobal', fach: [], stufe: [], lizenz: '', q: [] }, new Set([`30142:${pk}:m1`])), 'mit der Community geteilt: Treffer');
});

Deno.test('shortcodeAus und kontextprofilAus', () => {
  const KAT = block(/const CO_SCHLUESSEL = \[[\s\S]*?\n  \];/);
  const sc = bau('shortcodeAus', KAT), kp = bau('kontextprofilAus', KAT + "const RELAYS = ['wss://relay.edufeed.org'];");
  assertEquals(sc({ c: '', fach: [], stufe: [], lizenz: '', q: [] }), '[amb_nostr limit="12"]');
  const out = sc({ c: 'religlobal', fach: ['Ethik'], stufe: [], lizenz: 'offen', q: ['Frieden"x'] });
  assert(/^\[amb_nostr_search /.test(out) && /community="npub12atlg/.test(out) && /search="Friedenx"/.test(out) && /Lizenzfilter: offen/.test(out) && !/fixed_level/.test(out));
  const j = JSON.parse(kp({ c: '', fach: ['Ethik'], stufe: ['Primarstufe'], lizenz: '', q: ['Frieden'] }));
  assertEquals(j.actions['finden.material'].params, { thema: ['Frieden'], stufe: ['Primarstufe'] }); assertEquals(j.sammlung.community, null);
});

Deno.test('Sammlung: Ansicht, Route, keine eigene Abfrage, drei Ausgänge', async () => {
  assert(/id="v-sammlung" data-stand="nachbau:/.test(html), 'Ansicht mit Stand-Zeile');
  const r = block(/function route\(\)[\s\S]*?window\.scrollTo/);
  assert(/'finden'/.test(r) && /saOpen\(/.test(r), 'Route finden/sammlung');
  const o = block(/function saOpen\(qs\)[\s\S]*?\n  \}/) + block(/function saRender\(\)[\s\S]*?\n  \}/);
  assert(/mpLaden\(\)/.test(o) && /coLaden\(/.test(o) && /f\.c/.test(o) && !/hubFetch\(/.test(o), 'nur Caches, Community nur bei Filter, keine eigene Abfrage');
  assert(/id="saEinbetten"/.test(o) && /id="saAbo"/.test(o) && /Als Nostr-Liste speichern/.test(o) && /disabled aria-disabled="true"/.test(o) && /braucht einen Server/.test(o), 'Ausgänge ehrlich');
  assert(/Sammlung zusammenstellen/.test(html), 'Knopf im Materialpool');
  assert(/#finden\/sammlung/.test(block(/function lizenzAktionen\(stand, m\)[\s\S]*?\n  \}/)), 'In Sammlung aufnehmen führt zur Sammlung');
  assert(/Sammlung/.test(await Deno.readTextFile(new URL('../docs/navigation.md', import.meta.url))), 'docs/navigation.md');
});
```

- [ ] **Step 2: Fehlschlag sehen** · Expected: drei FAIL, 53 PASS.

- [ ] **Step 3: Ansicht, Funktionen, Route, Knopf, Erklärkarte, Material-Detail-Aktion, CSS (`.sa-filter` Felder in `--card`, Pillen wie `.lic-*`, Fokus sichtbar) und Doku schreiben.**

- [ ] **Step 4: Tests laufen lassen** · Expected: grün (56).

- [ ] **Step 5: Im Browser prüfen**: `#finden/sammlung` zeigt Stand-Zeile „live · … von … Materialien“, Filter füllen sich aus den Daten; `?lizenz=offen&q=Schöpfung` filtert; Einbetten zeigt beide Schnipsel, Kopieren meldet per Toast; Abonnieren zeigt das Filter-JSON und den deaktivierten Knopf; `?c=religlobal` zeigt die fünf geteilten Materialien; Netzwerk: keine zusätzliche WebSocket-Verbindung ohne Community-Filter, wenn der Materialpool vorher offen war; 375 px: Filter untereinander.

- [ ] **Step 6: Committen, PR** (`pr/sammlung`)

```bash
git add index.html tests/sammlung.test.ts docs/daten.md docs/navigation.md && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "Sammlung: Materialien nach Community, Fach, Stufe und Lizenz filtern; teilen, einbetten (Shortcode, Kontextprofil), abonnieren als Nostr-Filter"
```

### Task 3: Katalog je Community: geteilte Inhalte als Grundschicht, Kuratierung darüber, Stand und Pflege (Issue 02 `017a1143`, Spec 4.6)

**Files:** Modify `index.html` (Community-Raum: Navigationseintrag „Katalog“ in `crRender` unter „Inhalte“, Tab `katalog` in `crMain`; `route()`: `zu=katalog` → `crOpen(c, 'katalog')`; `katRender(c)`; Stand-Zeile von `v-community` je Tab; Communities-Kacheln: Zeile „Katalog ›“ für `CO_SCHLUESSEL`-Communities; rpi-virtuell-Instanz: Tab „Material“ bekommt den Satz mit Link zum Katalog der Community; CSS `.kat-*`), Modify `tests/sammlung.test.ts`, `docs/daten.md`. Branch `pr/kataloge` ab `pr/sammlung`.

**Interfaces:**
- Consumes: `coLaden`, `coEintraege`, `eintraegeAufloesen`, `eintragKarte`, `CO_SCHLUESSEL`, `mpLaden`, `datenstand`, `naddr`, `rtCopy`, `shortcodeAus`, `CY`, `crOpen`, `crRender`, `crMain`.
- Produces:
  - Route `#community?c=<id>&zu=katalog` (Alias zu `tab=katalog`; `zu` gewinnt, weil die Spec die Form nennt). `crMain(c)` liefert für `crTab === 'katalog'` den Platzhalter `<section id="katRoot">`, den `katRender(c)` füllt; die anderen Tabs bleiben Nachbau.
  - `function katRender(c)`: Kopf „Katalog von <c.n>“ mit Satz „Was diese Community aus dem gemeinsamen Datenraum teilt und zusammenstellt.“ Zwei Schichten:
    1. **„In der Community geteilt“** (Grundschicht): `coEintraege` auf `coLaden(hex)`, aufgelöst über `eintraegeAufloesen`, gruppiert nach Art (Material, Beiträge, Termine; Termine nur bevorstehende, vergangene als Zahl „und <n> vergangene“), je Gruppe die neuesten zwölf Karten über `eintragKarte` und ein Knopf „mehr“, der die Gruppe aufklappt; Zeile unter dem Kopf: „zuletzt geteilt am <TT.MM.JJJJ des neuesten Eintrags> · ohne Rollenprüfung“.
    2. **„Vom Redaktionskreis zusammengestellt“** (Kuratierung, nur wenn `listen` nicht leer): je Liste `<section class="kat-liste">` mit Titel (`esc`), Beschreibung, Bild (`sichereUrl`, sonst keins), Zeile „Stand vom <TT.MM.JJJJ aus created_at> · <n> Einträge“ (plus „· <u> nicht auflösbar“ nur wenn `u > 0`), Karten über `eintragKarte`, Knopf „Teilen“ (`rtCopy` der Adresse `nostr:` + `naddr(d, hex, 30004)`).
    Zustände: (a) `coDaten` noch nicht da: „Katalog wird geladen …“; (b) Antwort ohne Einträge und ohne Liste: „In dieser Community wurde noch nichts geteilt.“ mit Einladung „Teile Material, Beiträge oder Termine in der edufeed-App in diese Community; sie erscheinen hier ohne Umweg.“ und Link `https://edufeed.org/c/<npub>`; bei `pool: true` immer zusätzlich der Abschnitt „Der Materialpool als Katalog der Instanz“ mit dem Zähler aus `mpDaten` („<m> Materialien bei 3 Relays“) und Link `#materialpool`; (c) keine Antwort der Relays: „Die Relays antworten gerade nicht.“ mit demselben App-Link. Knöpfe über der Grundschicht: „Teilen“ (`rtCopy(location.href, 'Link zum Katalog kopiert.')`) und „Einbetten“ (`<details>` mit `shortcodeAus({ c: c.id, fach: [], stufe: [], lizenz: '', q: [] })` und dem Satz „Der Shortcode zeigt dieselben geteilten Materialien auf einer WordPress-Seite.“).
  - Hinweiszeile am Fuß: „Gezeigt wird, was mit dieser Community geteilt wurde, ohne Prüfung der Mitgliederrollen; weggelassen ist nur, was die Community selbst entfernt hat.“
  - Stand-Zeile `v-community`: bei Tab `katalog` `live · <n> geteilt · <k> Listen · ohne Rollenprüfung` / `live · noch nichts geteilt` / `Nachbau · Relays nicht erreichbar`; bei jedem anderen Tab zurück auf `nachbau:Beispielinhalte` (Test in `navigation.test.ts` Zeile 145 bleibt gültig, weil das Attribut unverändert bleibt).
  - Communities ohne Eintrag in `CO_SCHLUESSEL` zeigen den Tab „Katalog“ mit dem Satz „Kataloge gibt es für Communities mit eigenem Schlüssel im Datenraum.“ und Link `#communities`.
  - Communities-Kachel (`cyCards`): für `CO_SCHLUESSEL`-Communities ein Link `Katalog ›` (`#community?c=<id>&zu=katalog`) neben „Community-Raum öffnen“.

- [ ] **Step 1: Tests ergänzen**

```ts
Deno.test('Katalog-Tab: Route, zwei Schichten, drei Zustände, Titel maskiert, Pool', () => {
  assert(/zu=katalog|'zu'/.test(block(/function route\(\)[\s\S]*?window\.scrollTo/)), 'zu=katalog');
  const k = fn('katRender');
  assert(/coLaden\(/.test(k) && /coEintraege\(/.test(k) && /eintraegeAufloesen\(/.test(k) && /eintragKarte\(/.test(k), 'Grundschicht aus geteilten Inhalten');
  assert(/In der Community geteilt/.test(k) && /zusammengestellt/.test(k) && /ohne Rollenprüfung/.test(k), 'zwei Schichten, Grenze benannt');
  assert(/noch nichts geteilt/.test(k) && /antworten gerade nicht/.test(k) && /Stand vom/.test(k) && /nicht auflösbar/.test(k), 'Zustände');
  assert(/esc\(l\.titel\)|esc\(liste\.titel\)/.test(k) && /naddr\([^)]*30004\)/.test(k) && /shortcodeAus\(/.test(k), 'maskiert, Teilen, Einbetten');
  assert(/pool/.test(k) && /#materialpool/.test(k), 'Materialpool als Katalog der Instanz rpi-virtuell');
  assert(/'katalog'/.test(fn('crRender')), 'Navigationseintrag im Raum');
  assert(/zu=katalog/.test(block(/function cyCards\([\s\S]*?\n  \}/)), 'Link auf der Kachel');
  assert(html.includes('id="v-community" data-stand="nachbau:Beispielinhalte"'), 'Startwert der Ansicht bleibt Nachbau');
});
```

- [ ] **Step 2: Fehlschlag sehen** · Expected: ein FAIL, 56 PASS.

- [ ] **Step 3: Tab, `katRender`, Route, Kachel-Link, Stand-Zeile je Tab, CSS schreiben**; `docs/daten.md`: Verbraucher „Katalog je Community“ (zwei Schichten, Zustände, Konvention, Pool, Grenze der Rollenprüfung).

- [ ] **Step 4: Tests laufen lassen** · Expected: grün (57).

- [ ] **Step 5: Im Browser prüfen**: `#community?c=religlobal&zu=katalog` zeigt fünf Materialien und vier Termine als geteilt (Stand 05.11.), keine Liste; `#community?c=relilab&zu=katalog` zeigt Artikel, Material und bevorstehende Termine mit „mehr“; `#community?c=rpi-virtuell&zu=katalog` zusätzlich den Materialpool-Zähler; `#community?c=oercommunity&zu=katalog` die eigenen Seiten und Beiträge und nach Task 7 die Liste `katalog`; offline: „Relays antworten gerade nicht“; Netzwerk: drei WebSockets für `community:<hex>`, danach höchstens eine Nachfrage; 375 px: Karten einspaltig.

- [ ] **Step 6: Committen, PR** (`pr/kataloge`)

```bash
git add index.html tests/sammlung.test.ts docs/daten.md && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "Katalog je Community: geteilte Inhalte als Grundschicht, Kuratierungslisten darüber, ehrliche Zustände, Teilen und Einbetten, Materialpool als Katalog der Instanz"
```

### Task 4: Fortbildungskalender über alle Quellen, zwei Logiken in einer Taxonomie (Issue 05 `0a7ccbf8`, Spec 4.9)

**Files:** Modify `index.html` (neue Ansicht `<div class="view" id="v-fortbildungen" data-stand="stand:…">`; Anwendungsskript: `KAL_QUELLEN`, `kalLaden()`, `terminLogik(ev)`, `terminMerkmale(ev)`, `kaOpen(qs)`, `kaRender()`; `rvOpen`: Termine aus `kalLaden` statt eigener Abfrage; `RT_EV`: nur relilab-Schlüssel aus `RT_RAW`; `VIEW_OF['finden.fortbildungen'] = 'finden/fortbildungen'`; `EX['finden.fortbildungen'].go`; Kontext `rpi-virtuell`: `finden.fortbildungen` bleibt der Tab; CSS `.ka-*`), Modify `tools/schnappschuss.ts` (Autoren = `KAL_QUELLEN`), Create `tests/kalender-personen.test.ts`, Modify `docs/daten.md`, `docs/navigation.md` (Zeile Fortbildungen). Branch `pr/kalender` ab `pr/kataloge`.

**Interfaces:**
- Consumes: `hubFetch`, `npubToHex`, `evToTermin`, `RT_RAW`, `RT_STAND`, `RT_HEX`, `RT_SRC`, `rtIcs`, `rtCopy`, `datenstand`, `rvRender`, `tagWert`, `tagWerte`, `sichereUrl`, `CO_SCHLUESSEL`.
- Produces:
  - `const KAL_QUELLEN = [ { npub: 'npub17mq54dad6ewkrnunzx5xs4t4c0edur99gz7ymhu3dam0pz034fpsxjqk3d', n: 'relilab.org', logik: 'labor' }, { npub: 'npub1lde034983zllh2nhe48lt60q6p3a6lsxn0g90uemhg0906jsnzesh5vz8y', n: 'relilab-impuls', logik: 'labor' }, { npub: 'npub1fpcxaz2wvjl90gjs60x37ny2pa5u4yqfx7fklz73rgfjnnfujl3sr2fxgk', n: 'relilab', logik: 'labor' }, { npub: 'npub14esenw6rt4c2pmxwvyey4jqw0sjdahetq6qvh5lffxp7w4thg63ql480z2', n: 'rpi-virtuell', logik: 'institut' }, { npub: 'npub12atlgghwe2qwkps9sgm9z4je825hskh47ef7kc28zzgn5tztgtyqyveeqs', n: 'reliGlobal', logik: 'institut' }, { npub: 'npub10gyagq3eev0vcnqks69gewz22kvpe2989c5zua88huarjwwl04dqdzrmzr', n: 'ALPIKA Grundschule', logik: 'institut' }, { npub: 'npub1vkn99j7kufchmgcly98lg9uexfste9epxe6jhgdt20wn4adzrvpqxhac4w', n: 'KPH Wien/NÖ', logik: 'institut' }, { npub: 'npub1wak8hljj3szpe5g3fmak6jqspvhyn4867flrq8anlq7xfg5xjn6qtmtpsw', n: 'RPI EKKW/EKHN', logik: 'institut' }, { npub: 'npub10dxgwerwfmjsyu9lq97pxdu4q0w3efycykhv3a9j2ut7y5l4xhkqyclpt8', n: 'KuRU & Schuldek.de', logik: 'institut' }, { npub: 'npub1jt62efpmw02uuj58fqzgss2nxe2wvsjx48x6etvdrpa4prtp8l2s0zld3w', n: 'Konfiarbeit EKD', logik: 'institut' }, { npub: 'npub1vsnck0crdcjdczggrlp7ng7tn6fawpdauts2wdwetsnh8s7dkcqsumc7zj', n: 'Friedenspädagogik', logik: 'institut' }, { npub: 'npub12g780vegprsdangl7ypfhjqf7rytwuws5ka4wwd6trexcjea007qqlu3mw', n: 'bildung-kirchen.de', logik: 'institut' }, { npub: 'npub12j35qpeve33929kg64etvw9g9rzms4c8g5gnqta58yhjdc6wryfse3phmu', n: 'rpi-virtuell (Kalender)', logik: 'institut' }, { npub: 'npub1tgftg8kptdrxxg0g3sm3hckuglv3j0uu3way4vylc5qyt0f44m0s3gun6e', n: 'FOERBICO', logik: 'institut' } ]`, `KAL_HEX` = Map hex → Eintrag. Die ptz-Termine liegen unter dem persönlichen Schlüssel von Jörg Lohrer und werden nicht als Quelle eingetragen; sie kommen über den `h`-Filter, wenn sie einer Hub-Community zugeordnet sind (Bedarf an das Team: eigener ptz-Schlüssel oder `h`-Tag).
  - `function kalLaden()` → `Promise<ev[]>`, einmal je Sitzung (`kalDaten`): `hubFetch('kalender', [{ kinds: [31923], authors: [...KAL_HEX.keys()], since: <jetzt − 365 Tage>, limit: 500 }, { kinds: [31923], '#h': CO_SCHLUESSEL.map(k => k.hex), limit: 200 }], { relays: ['wss://relay.edufeed.org', 'wss://relay-rpi.edufeed.org'] })`; je Adresse (`pubkey:d`) das neueste `created_at`; gemischt mit `RT_RAW` (Schnappschuss) wie in `rtOpen`; Ergebnis sind rohe Events.
  - `const RL_HEX = npubToHex('npub1fpcxaz2wvjl90gjs60x37ny2pa5u4yqfx7fklz73rgfjnnfujl3sr2fxgk')` (relilab).
  - `function terminLogik(ev)` → `'labor' | 'institut'`: `labor`, wenn `KAL_HEX.get(ev.pubkey)?.logik === 'labor'` oder ein `t`-Tag `relilab` (ohne Groß-/Kleinschreibung) oder ein `h`-Tag gleich `RL_HEX`; sonst `institut` (auch unbekannte Absender über `h`). Liest außer `KAL_HEX` und `RL_HEX` nichts aus dem Skript.
  - `function terminMerkmale(ev)` → `{ online: true|false|null, anmeldung: true|null, kostenfrei: true|false|null }`: `online` `true` bei `location` mit `zoom`, `online`, `http(s)://`, `teams`, `bbb`, `jitsi` (ohne Groß-/Kleinschreibung), `false` bei anderer nicht-leerer `location`, `null` ohne; `anmeldung` `true` bei Tag `registrationUrl` mit `sichereUrl`, sonst `null` (fehlende Angabe ist keine Aussage); `kostenfrei` `true` bei `price` mit Betrag `0`, `false` bei Betrag größer 0, `null` ohne Tag.
  - `function kaOpen(qs)`: Parameter `logik=labor|institut`, `merkmal=online|praesenz|anmeldung|kostenfrei` (mehrfach), `q`, `quelle=<npub>`; zeigt sofort den Schnappschuss (`RT_RAW`, Stand `RT_STAND`), ruft `kalLaden()`, rendert mit `kaRender()`.
  - `function kaRender()`: Kopf „Fortbildungen“ mit zwei Sätzen: „Hier stehen die Fortbildungen der Institute und die Laborformate nebeneinander. Institute: Anmeldung, klare Verantwortung, Bescheinigung. Labor: offen, kostenfrei, online, Unfertiges erlaubt.“; Chips „Alle · Institute und Communities · Labor“ (Filter `logik`), Merkmal-Chips „online · Präsenz · mit Anmeldung · kostenfrei“ (Filter `merkmal`, nur Termine mit der Angabe treffen; ohne gesetzten Filter fällt kein Termin heraus), Quellenliste als Auswahlfeld (Namen aus `KAL_QUELLEN`, unbekannte Absender „weitere (über Community)“), Suchfeld; Liste bevorstehender Termine nach Monat gruppiert: Datum, Zeit, Titel (Link `e.u`), Absender, Logik-Pille („Labor“ in `--c-erstellen`-Hellton, „Institut“ in `--c-finden`-Hellton, Texte mit 4,5:1), Merkmale als kleine Wörter oder „keine Angabe“; je Termin Knöpfe „.ics“ (`rtIcs([e], …)`) und „nostr:“ (`rtCopy`); oben „Alle als .ics“ und „Link teilen“. Stand-Zeile: `Stand vom <RT_STAND>` → `live · <n> Termine · <k> Quellen` (k = Zahl verschiedener Absender in der Antwort); ohne Antwort bleibt der Stand.
  - `rvOpen(qs)`: nutzt `kalLaden()` (dieselbe Abfrage `kalender`), filtert auf `terminLogik(ev) === 'institut'`, zeigt darunter den Link „Alle Fortbildungen, auch Laborformate ›“ (`#finden/fortbildungen`); News-Abfrage bleibt in `rvOpen` als eigener `hubFetch('rpi-virtuell-news', …)` (ein Filter). `rtOpen` (relilab) bleibt bei seiner Abfrage `relilab-termine`, aber `RT_EV` entsteht aus `RT_RAW.filter(ev => RT_HEX[ev.pubkey])`, weil der Schnappschuss nun alle Quellen trägt.
  - `tools/schnappschuss.ts`: Autorenliste des Terminblocks = die 14 Hex-Schlüssel aus `KAL_QUELLEN` (im Skript als Konstante gespiegelt, Kommentar nennt die Quelle im Anwendungsskript), Filter zusätzlich `since` = heute − 30 Tage auf `created_at` entfällt (bleibt wie bisher: alle, dann nach Ende gefiltert); Ausgabe unverändert.
  - Konsole: `VIEW_OF['finden.fortbildungen'] = 'finden/fortbildungen'`; `EX['finden.fortbildungen'].go = ['Zum Fortbildungskalender', '#finden/fortbildungen']`; Kontext `rpi-virtuell` behält seinen Tab, Kontext `relilab` seine Termine (unverändert). `docs/navigation.md`: Zeile Fortbildungen → Ziel `#finden/fortbildungen`, Leiste „rpi-virtuell (Institute)“.

- [ ] **Step 1: Tests schreiben** (`tests/kalender-personen.test.ts`, Kopf wie `sammlung.test.ts`)

```ts
Deno.test('terminLogik und terminMerkmale: fehlende Tags', () => {
  const relilab = '48706e89'.padEnd(64, '0');
  const extra = `const KAL_HEX = new Map([['${'f6'.repeat(32)}', { logik: 'labor' }], ['${'65'.repeat(32)}', { logik: 'institut' }]]); const RL_HEX = '${relilab}';`;
  const tl = bau('terminLogik', extra), tm = bau('terminMerkmale');
  const ev = (pk: string, tags: string[][]) => ({ pubkey: pk, tags });
  assertEquals(tl(ev('f6'.repeat(32), [])), 'labor');
  assertEquals(tl(ev('65'.repeat(32), [['t', 'Relilab']])), 'labor', 't=relilab zählt als Labor');
  assertEquals(tl(ev('65'.repeat(32), [['h', relilab]])), 'labor');
  assertEquals(tl(ev('65'.repeat(32), [])), 'institut'); assertEquals(tl(ev('00'.repeat(32), [])), 'institut');
  assertEquals(tm(ev('', [])), { online: null, anmeldung: null, kostenfrei: null });
  assertEquals(tm(ev('', [['location', 'Zoom: https://relilab.org/live'], ['registrationUrl', 'https://x.org/a'], ['price', '0', 'EUR']])), { online: true, anmeldung: true, kostenfrei: true });
  assertEquals(tm(ev('', [['location', 'Evangelische Akademie Frankfurt'], ['price', '25', 'EUR'], ['registrationUrl', 'javascript:x']])), { online: false, anmeldung: null, kostenfrei: false });
});

Deno.test('kalLaden: eine Abfrage für Kalender und rpi-virtuell, feste Quellen', async () => {
  const q = block(/const KAL_QUELLEN = \[[\s\S]*?\n  \];/);
  assertEquals((q.match(/npub1[0-9a-z]{58}/g) || []).length, 14); assert(!/npub1f7jar/.test(q), 'kein persönlicher Schlüssel als Quelle');
  const k = block(/function kalLaden\(\)[\s\S]*?\n  \}/);
  assert(/hubFetch\('kalender', \[/.test(k) && /authors: \[\.\.\.KAL_HEX\.keys\(\)\]/.test(k) && /'#h': CO_SCHLUESSEL\.map/.test(k) && /RT_RAW/.test(k), 'zwei Filter, Schnappschuss gemischt');
  assert(!/amb-relay/.test(k) && !/groups\.edufeed\.org/.test(html));
  const rv = block(/function rvOpen\(qs\)[\s\S]*?\n  \}/);
  assert(/kalLaden\(\)/.test(rv) && !/kinds: \[31923\]/.test(rv) && /terminLogik\(/.test(rv) && /#finden\/fortbildungen/.test(rv), 'rpi-virtuell teilt die Abfrage');
  assert(/RT_RAW\.filter\(ev => RT_HEX\[ev\.pubkey\]\)/.test(s), 'relilab filtert den Schnappschuss');
  assert(/'finden\.fortbildungen': 'finden\/fortbildungen'/.test(s), 'Konsole');
  assert(/id="v-fortbildungen"/.test(html) && /keine Angabe/.test(block(/function kaRender\(\)[\s\S]*?\n  \}/)), 'Ansicht und ehrliche Merkmale');
  const t = await Deno.readTextFile(new URL('../tools/schnappschuss.ts', import.meta.url));
  assert(new Set(t.match(/[0-9a-f]{64}/g) || []).size >= 14, 'Schnappschuss kennt alle Quellen');
  assert(/#finden\/fortbildungen/.test(await Deno.readTextFile(new URL('../docs/navigation.md', import.meta.url))));
});
```

- [ ] **Step 2: Fehlschlag sehen** · Expected: zwei FAIL in `kalender-personen.test.ts`, 57 PASS.

- [ ] **Step 3: Konstanten, `kalLaden`, `terminLogik`, `terminMerkmale`, Ansicht mit `kaOpen`/`kaRender`, Umbau `rvOpen` und `RT_EV`, Konsole, Schnappschuss-Skript, CSS (`.ka-logik-labor`, `.ka-logik-institut` als Hellton plus Textfarbe in `:root` mit `--ka-*`), Doku schreiben**; einmal `deno task schnappschuss` laufen lassen (nicht wiederholen; Ausgabe muss mehr Termine als vorher zeigen); `docs/daten.md`: Verbraucher „Fortbildungskalender“ (Quellen, zwei Filter, Logikregel, Merkmalregel, gemeinsamer Cache mit rpi-virtuell, relilab-Filter auf dem Schnappschuss).

- [ ] **Step 4: Tests laufen lassen** · Expected: grün (59); `navigation.test.ts` bleibt grün (Stand-Zeile der neuen Ansicht vorhanden).

- [ ] **Step 5: Im Browser prüfen**: `#finden/fortbildungen` zeigt zuerst „Stand vom <Datum>“, dann „live · n Termine · k Quellen“; Chip „Labor“ zeigt relilab-Formate, „Institute und Communities“ die übrigen; `?merkmal=kostenfrei` lässt nur Termine mit `price=0`; Konsole `finden.fortbildungen` führt von der Startseite hierher, im rpi-virtuell-Kontext zum Tab; `#rpi-virtuell?tab=fortbildungen` zeigt keine Laborformate mehr und den Link; `#relilab?tab=termine` unverändert; offline bleibt der Schnappschuss; Netzwerk: eine Verbindung je Relay für `kalender`, der rpi-virtuell-Tab öffnet danach keine neue für Termine.

- [ ] **Step 6: Committen, PR** (`pr/kalender`)

```bash
git add index.html tools/schnappschuss.ts tests/kalender-personen.test.ts docs/daten.md docs/navigation.md && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "Fortbildungskalender über alle Quellen: Labor- und Institutslogik als Merkmale, feste Quellenliste, gemeinsame Abfrage mit rpi-virtuell, Schnappschuss aller Quellen"
```

### Task 5: Personen-Ansicht und echte Profile (Issue 06 `693c69cc`, Spec 4.10)

**Files:** Modify `index.html` (neue Ansichten `<div class="view" id="v-personen" data-stand="stand:04.11.2026 · Teamseite, Personen-Liste fehlt">` und `<div class="view" id="v-person" data-stand="nachbau:Profil laden">`; Anwendungsskript: `PERSONEN_LISTE`, `peLaden()`, `profilAus(ev)`, `peOpen()`, `peRender()`, `prOpen(qs)`, `prRender()`; `route()`: `kooperieren/personen` → `v-personen`, `person` → `v-person`; `VIEW_OF['kooperieren.personen'] = 'kooperieren/personen'`; `EX['kooperieren.personen'].go`; Community-Raum Tab „Mitglieder“ bleibt Nachbau; CSS `.pe-*`), Modify `tests/kalender-personen.test.ts`, `tests/navigation.test.ts` (Zeile zu `kooperieren.personen`), `docs/daten.md`, `docs/navigation.md` (Zeile Personen). Branch `pr/personen` ab `pr/kalender`.

**Interfaces:**
- Consumes: `hubFetch`, `npubToHex`, `bech32`, `istHex64`, `esc`, `sichereUrl`, `FO_HEX`, `CO_SCHLUESSEL`, `CY`, `OC_TEAM`, `ini`, `datenstand`, `naddr`, `evToTermin`, `mpMaterial`, `beitragUrl`, `eintragKarte`.
- Produces:
  - `const PERSONEN_LISTE = { d: 'personen', autoren: [FO_HEX, npubToHex('npub14esenw6rt4c2pmxwvyey4jqw0sjdahetq6qvh5lffxp7w4thg63ql480z2')] }`: die Liste ist ein `kind:30000` (Follow-Liste) mit `d=personen` und `p`-Tags; sie gilt als Einverständnis der Genannten und wird nur vom Schaufenster-Schlüssel oder vom Community-Schlüssel rpi-virtuell angenommen (beide beim Team). Liegen beide vor, gewinnt das neuere `created_at`; die Pflege ist Sache des Inhaltsstrangs (Task 7).
  - `function peLaden()` → `Promise<{ liste: ev|null, profile: Map<hex, profil>, mitglied: Map<hex, string[]> }>`, einmal je Sitzung: Abfrage 1 `hubFetch('personen', [{ kinds: [30000], authors: PERSONEN_LISTE.autoren, '#d': [PERSONEN_LISTE.d], limit: 2 }])`; ohne Liste endet es hier (`liste: null`); sonst Abfrage 2 `hubFetch('personen:profile', [{ kinds: [0], authors: <p-Tags, nur istHex64, höchstens 150> }, { kinds: [30000], authors: <dieselben>, '#d': ['communities'] }])`: `profile` aus `kind:0` (`profilAus`), `mitglied` aus den `p`-Tags der Mitgliedschaftslisten, abgebildet auf `CO_SCHLUESSEL`-/`CY`-Namen über die Hex-Schlüssel der Hub-Communities (unbekannte Communities zählen nicht).
  - `function profilAus(ev)` → `{ pk, npub, name, about, bild, web, nip05, bot } | null`: `JSON.parse(ev.content)` in `try`, bei Fehler `null`; `name` = `display_name` oder `name` (`esc`, höchstens 80 Zeichen), leer → `null`; `about` `esc`, gekürzt auf 160 Zeichen am Wortende; `bild` = `sichereUrl(picture)`; `web` = `sichereUrl(website)`; `nip05` nur bei Muster `^[^@\s]+@[^@\s]+$` (`esc`); `bot` = `content.bot === true`; `npub` über `bech32('npub', …)`.
  - `function peRender(daten)`: Kopf „Personen“ mit Satz „Menschen, die im Ökosystem sichtbar sein wollen: Lehrkräfte, Fortbildende, Forschende, Teams der Institute.“; Zustände: (1) `daten.liste === null` nach Antwort: Satz „Die Personen-Liste ist noch nicht angelegt; bis dahin stehen hier die Teams aus dem Schaufenster.“ und die Karten aus `OC_TEAM` mit Initialen (`ini`), Funktion, Gruppe (Schnappschuss, Stand-Zeile unverändert); (2) Liste vorhanden: Karten aus `profile` ohne `bot` und ohne `name === null`, in Reihenfolge der `p`-Tags: Bild (`sichereUrl`, sonst Initiale in Bereichsfarbe), Name, `about`, `nip05`, Communities als Chips, Knopf „Profil ansehen ›“ (`#person?p=<npub>`), Knopf „Folgen“ als `disabled aria-disabled="true"` mit Hinweis „braucht Anmeldung mit Schlüssel, folgt“; Stand-Zeile `live · <n> Personen · Liste vom <TT.MM.JJJJ>`; (3) keine Antwort: „Die Relays antworten gerade nicht.“ plus Teamseite, Stand-Zeile bleibt. Hinweiszeile unter der Liste: „Wer hier stehen möchte, sagt es dem Community-Management; die Liste pflegt das Team. Profile mit Mastodon-Brücke erscheinen hier wie alle anderen.“
  - `function prOpen(qs)`: `p` = npub (über `npubToHex`, Fehler → „Kein gültiges Profil in der Adresse.“ mit Rückweg); zuerst `peLaden()`-Cache, sonst `hubFetch('person:' + hex, [{ kinds: [0], authors: [hex], limit: 1 }, { kinds: [30142, 30023, 31923], authors: [hex], limit: 30 }, { kinds: [30000], authors: [hex], '#d': ['communities'], limit: 1 }])`; `prRender()`: Kopf mit Bild, Name, `about`, `web` als Link (`rel="noopener"`), `nip05`, Communities; Abschnitte „Materialien“, „Beiträge“, „Termine“ aus den Veröffentlichungen über `eintragKarte` (neueste 10 je Abschnitt), leere Abschnitte sagen „noch nichts veröffentlicht“; Knopf „Folgen“ deaktiviert wie oben; Link „Bei edufeed ansehen ›“ `https://edufeed.org/<npub>` nur als Text ohne Link, bis die App-Route geklärt ist (im Doku-Abschnitt vermerkt); Stand-Zeile `live · Profil vom <TT.MM.JJJJ>` oder `Nachbau · Profil nicht gefunden`. Die Ansicht `#profil` (Persona, Dashboard) bleibt Nachbau und bekommt den Satz „Dein eigenes Profil kommt mit der Anmeldung per Schlüssel; echte Profile findest du unter Personen.“ mit Link.
  - `tests/navigation.test.ts`: die Zusicherung, dass `kooperieren.personen` kein Ziel hat (Toast), wird ersetzt durch `assert(/'kooperieren\.personen': 'kooperieren\/personen'/.test(s))`. `docs/navigation.md`: Zeile Personen → Ziel `#kooperieren/personen`, Stand „gebaut“.

- [ ] **Step 1: Tests ergänzen**

```ts
Deno.test('profilAus: maskiert, sichere Adressen, Bots erkannt', () => {
  const pa = bau('profilAus', block(/  function bech32\([^)]*\) \{[\s\S]*?\n  \}/));
  const ev = (c: unknown) => ({ pubkey: 'ab'.repeat(32), content: typeof c === 'string' ? c : JSON.stringify(c), tags: [] });
  const p = pa(ev({ name: '<b>Ada</b>', about: 'x'.repeat(400), picture: 'data:image/png;base64,AAA', website: 'https://ada.example', nip05: 'ada@example.org', bot: true }));
  assert(p.name === '&lt;b&gt;Ada&lt;/b&gt;' && p.about.length <= 162 && p.bild === '' && p.web === 'https://ada.example' && p.nip05 === 'ada@example.org' && p.bot === true && /^npub1/.test(p.npub));
  assertEquals(pa(ev('{kaputt')), null); assertEquals(pa(ev({ about: 'ohne Namen' })), null);
  assertEquals(pa(ev({ name: 'A', nip05: 'kein mail' })).nip05, '');
});

Deno.test('peLaden: zwei Abfragen, feste Autoren; Personen und Person: Rückfall Teamseite, Folgen deaktiviert', () => {
  const l = block(/function peLaden\(\)[\s\S]*?\n  \}/);
  assert(/hubFetch\('personen', \[\{ kinds: \[30000\], authors: PERSONEN_LISTE\.autoren, '#d': \[PERSONEN_LISTE\.d\]/.test(l), 'Liste nur von festen Autoren');
  assert(/hubFetch\('personen:profile'/.test(l) && /kinds: \[0\]/.test(l) && /'#d': \['communities'\]/.test(l) && (l.match(/hubFetch\(/g) || []).length === 2, 'zweite Abfrage abhängig, keine dritte');
  assert(/istHex64\(/.test(l) && /150/.test(l), 'Schlüssel geprüft, gedeckelt');
  const r = block(/function peRender\(daten\)[\s\S]*?\n  \}/);
  assert(/OC_TEAM/.test(r) && /noch nicht angelegt/.test(r) && /antworten gerade nicht/.test(r) && /disabled aria-disabled="true"/.test(r) && /\.bot/.test(r), 'Zustände, Teamseite, Folgen, Bots');
  const o = block(/function prOpen\(qs\)[\s\S]*?\n  \}/);
  assert(/npubToHex\(/.test(o) && /kinds: \[30142, 30023, 31923\]/.test(o) && /Kein gültiges Profil/.test(o), 'Profilseite');
  assert(/id="v-personen" data-stand="stand:04\.11\.2026/.test(html) && /id="v-person" data-stand="nachbau:/.test(html), 'Ansichten mit Stand');
  assert(/'kooperieren\.personen': 'kooperieren\/personen'/.test(s) && /'person'/.test(block(/function route\(\)[\s\S]*?window\.scrollTo/)), 'Konsole und Route');
});
```

- [ ] **Step 2: Fehlschlag sehen** · Expected: zwei FAIL, 59 PASS; nach dem Austausch der Zeile in `navigation.test.ts` dort ein FAIL mehr, bis Step 3 fertig ist.

- [ ] **Step 3: Konstante, `peLaden`, `profilAus`, beide Ansichten, `peRender`, `prOpen`/`prRender`, Route, Konsole, Satz im Persona-Profil, CSS (`.pe-card` mit Bild 64 px, Initiale in `--c-koop`-Hellton), Doku schreiben**; `docs/daten.md`: Verbraucher „Personen“ und „Person“ (Liste als Einverständnis, zwei Abfragen, Bot-Regel, Rückfall Teamseite, offene App-Route).

- [ ] **Step 4: Tests laufen lassen** · Expected: grün (61).

- [ ] **Step 5: Im Browser prüfen**: `#kooperieren/personen` zeigt am 05.11. die Teamseite mit dem Satz „noch nicht angelegt“ (Stand-Zeile bleibt „Stand vom 04.11.2026“); nach Anlegen der Liste (Task 7) Karten mit Bildern und Communities, Stand „live · n Personen“; `#person?p=npub1f7jar…` (öffentlicher Schlüssel von Jörg Lohrer, mit `nip05` sichtbar) zeigt Profil und Veröffentlichungen; `#person?p=kaputt` zeigt den Fehlersatz; Konsole `kooperieren.personen` führt hierher, kein Toast „später“ mehr; Netzwerk: zwei Verbindungen je Relay nacheinander, nicht mehr.

- [ ] **Step 6: Committen, PR** (`pr/personen`)

```bash
git add index.html tests/kalender-personen.test.ts tests/navigation.test.ts docs/daten.md docs/navigation.md && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "Personen: echte Profile aus der Personen-Liste mit Einverständnis, Profilseite mit Veröffentlichungen, Teamseite als Rückfall, Folgen bis zur Anmeldung deaktiviert"
```

### Task 6: ADR-0008 „Community-Inhalte und Listen“ und Doku der Etappe

**Files:** Create `docs/adr/0008-community-inhalte-und-listen.md`, Modify `README.md` (ADR-Tabelle, Ansichten-Liste: Sammlung, Kataloge, Fortbildungen, Personen), `docs/konstruktion.md` (Abschnitt „Community-Inhalte und Listen (Etappe 4)“ nach „Inhalte aus Events“; Tabelle „Offene Stellen“: Zeilen `finden.fortbildungen` und `kooperieren.personen` als gebaut streichen, neue Zeilen „Folgen“, „Abonnieren als Liste“, „Redaktionsoberfläche für Listen“), `tests/kalender-personen.test.ts`. Branch `pr/doku-etappe-4` ab `pr/personen`.

**Interfaces:**
- Consumes: Entscheidungen der Tasks 1 bis 5.
- Produces: ADR-0008 nach der Vorlage in `docs/adr/README.md` (Status: angenommen · <Datum> · Entscheidung der Maintainer · Bezug: Issues `b68eaaa5…`, `017a1143…`, `0a7ccbf8…`, `693c69cc…`), Entscheidung in fünf Punkten: (1) Der Katalog einer Community ist, was mit ihr geteilt wurde: Events mit `h`-Tag und Reposts `kind:6`/`16` mit `h`-Tag, gelesen über `#h` auf die fünf bekannten Schlüssel, nie global; der Hub prüft keine Mitgliederrollen (das Gruppen-Relay wird nie gelesen) und sagt das sichtbar; weggelassen wird nur, was die Community mit ihrem eigenen Schlüssel per `kind:1985`-Label entfernt hat; Kuratierungslisten `kind:30004` mit `d=katalog` oder `d=katalog-<thema>` unter dem Community-Schlüssel sind die zweite Schicht; der Materialpool ist zusätzlich der Katalog der Instanz rpi-virtuell; (2) die Sammlung filtert den Datenraum ohne eigene Abfrage, der Community-Filter folgt derselben `h`-Logik wie der Shortcode-Parameter `community`, und der Filter wird als Shortcode und Kontextprofil weitergegeben; Abonnieren ist ein kopierbarer Nostr-Filter, bis ein Signer Listen schreiben kann; (3) der Fortbildungskalender liest feste Quellen plus Community-Zuordnung (`h`), nie global, und unterscheidet Labor und Institut über Absender, `t=relilab` und `h`, Merkmale über `location`, `registrationUrl`, `price`; fehlende Angaben bleiben „keine Angabe“; (4) die Personen-Ansicht zeigt nur, wen eine Personen-Liste `kind:30000` `d=personen` des Schaufenster- oder rpi-virtuell-Schlüssels nennt; die Liste ist das Einverständnis; Mitgliedschaft allein zeigt niemanden; Bots werden ausgelassen; (5) Folgen, Speichern als Liste und Redaktionsoberfläche warten auf die Anmeldung per Schlüssel (Stufe B). Verworfen: eine Listenpflicht als Voraussetzung für einen Katalog (das Geteilte ist schon da, die Liste wäre Doppelpflege); Rollenprüfung über das Gruppen-Relay (nie gelesen; ein halb geprüfter Katalog wäre unehrlicher als ein gekennzeichnet ungeprüfter); globale Listen- oder Terminabfragen (fremde Apps, Bildungsserver-Import); Personen aus Mitgliedschaften (kein Einverständnis); getrennte Kalender je Logik (die Spec will eine Taxonomie); Lizenzfilter als Shortcode-Attribut erfinden (das Plugin kennt keines). Folgen: Der Inhaltsstrang liefert die Personen-Liste, den FOERBICO-Katalog und beispielhaft Geteiltes; Etappe 5 baut auf `coLaden` und `peLaden` für Ökosystem-Karte und eigene Instanz auf.

- [ ] **Step 1: Test ergänzen**

```ts
Deno.test('ADR-0008 und README nennen die Etappe', async () => {
  const adr = await Deno.readTextFile(new URL('../docs/adr/0008-community-inhalte-und-listen.md', import.meta.url));
  assert(/^# ADR-0008/.test(adr) && /## Status/.test(adr) && /## Entscheidung/.test(adr) && /b68eaaa5/.test(adr) && /693c69cc/.test(adr) && /d=personen/.test(adr) && /d=katalog/.test(adr) && /ohne Rollenprüfung|Mitgliederrollen/.test(adr));
  assert(!/Arbeitspaket|Meilenstein|Förderkennzeichen|Projektträger|Zwischenbericht/.test(adr), 'Projektsprache');
  const r = await Deno.readTextFile(new URL('../README.md', import.meta.url));
  assert(/0008-community-inhalte-und-listen/.test(r) && /Sammlung/.test(r) && /Personen/.test(r), 'README');
});
```

- [ ] **Step 2: Fehlschlag sehen** · Expected: ein FAIL, 61 PASS.
- [ ] **Step 3: ADR, README, Konstruktionsbeschreibung schreiben** (prüfen: `python3 -I ~/repositories/FOERBICO_und_rpi-virtuell/tools/nachweis/check.py gitworkshop docs`).
- [ ] **Step 4: Tests laufen lassen** · Expected: grün (62).
- [ ] **Step 5: Committen, PR** (`pr/doku-etappe-4`)

```bash
git add docs/adr/0008-community-inhalte-und-listen.md README.md docs/konstruktion.md tests/kalender-personen.test.ts && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "ADR-0008: Community-Inhalte und Listen (geteilte Inhalte als Katalog, Kuratierung, Kalenderquellen, Personen-Liste); README und Konstruktion nachgeführt"
```

### Task 7: Inhaltsstrang: Personen-Liste, FOERBICO-Katalog, beispielhaftes Teilen (Spec 5a, Fristen 21./23.12., Bedarf vor dem 17.11.)

**Files (FOERBICO-Repo, Branch `kataloge-und-personen` ab `main`):** Modify `Website/navigation.yaml` (neue Liste `katalog`), Create `tools/listen/veroeffentlichen.ts` (signiert eine unsignierte Event-Vorlage mit einem Schlüssel aus einer Env-Datei außerhalb des Repos und sendet sie an die drei Relays), `tools/listen/README.md`, `Hub-Entwicklung/kataloge/README.md`, `Hub-Entwicklung/kataloge/personen-liste.json` (Vorlage `kind:30000`, `d=personen`, `p`-Tags nur nach Einverständnis), `Hub-Entwicklung/kataloge/teilen-<community>.json` (Vorlagen `kind:16` mit `a`-, `k`-, `p`- und `h`-Tag für Communities mit wenig geteiltem Material, zur Entscheidung durch Jörg und die Redaktion). Die Bedarfsliste `Hub-Entwicklung/2026-11-07-etappe-4-bedarf-team.md` liegt bereits neben diesem Plan.

**Interfaces:**
- Consumes: die Konvention aus Task 1 (`h`-Tag und Reposts als Katalog, `d=katalog`/`katalog-<thema>` als Kuratierung), aus Task 5 (`d=personen`), die Schlüsselliste, die Relay-Bestände (Befund oben), das Repost-Format aus dem edufeed-Wiki „Sharing and reading community content“ (`kind:16`, `a`-Tag mit Relay-Hinweis, `k`, `p`, ein `h` je Community, `content` leer).
- Produces:
  - `Website/navigation.yaml`: `katalog: [qualitaet, oer-und-oep, tagungen, <sechs bis zehn Beitrags-Slugs mit Bezug zu Qualität, Metadaten, Lizenz, Kataloge>]`; mdparser `sync navigation` publiziert daraus `kind:30004` mit `d=katalog` und `a`-Tags auf `30023` des Schaufenster-Schlüssels (die Titel-Tabelle in mdparser kennt nur Menü und Fußzeile; bis zur Ergänzung zeigt der Hub `d` als Titel). Das ist die Kuratierungsschicht des Schaufensters, das keine Community hat.
  - `tools/listen/veroeffentlichen.ts`: `deno run --env-file=<pfad außerhalb des Repos> --allow-env --allow-net --allow-read=<vorlage> tools/listen/veroeffentlichen.ts <vorlage.json> <ENV_VARIABLE> [--dry-run]`; liest die Vorlage, setzt `created_at`, signiert mit dem Schlüssel aus der genannten Variablen (`npm:nostr-tools@2` `finalizeEvent`), sendet an `wss://relay.edufeed.org`, `wss://relay-rpi.edufeed.org`, `wss://amb-relay.edufeed.org` und protokolliert je Relay `OK`/`Grund`; gibt nie einen Schlüsselwert aus; `--dry-run` zeigt nur das unsignierte Event. Die Env-Datei (`~/.config/nachweis/listen.env`, Rechte 600) hält je Schlüssel eine Variable (`NSEC_RPI_VIRTUELL`, `NSEC_RELILAB`, `NSEC_RELIGLOBAL`, `NSEC_ALPIKA_GS`, `NSEC_FOERBICO`); ihr Pfad steht in der README, ihr Inhalt nirgends.
  - `personen-liste.json`: `{ "kind": 30000, "tags": [["d","personen"],["title","Personen im Hub"]], "content": "" }`; `p`-Tags trägt Jörg nach Einverständnis ein (zuerst die hauptamtlichen Teams, Spec 5a); signiert mit `NSEC_FOERBICO` oder `NSEC_RPI_VIRTUELL` (beide gelten in Task 5).
  - `teilen-<community>.json`: je Vorlage ein Repost `{ "kind": 16, "tags": [["a","30142:<hex>:<d>","wss://amb-relay.edufeed.org"],["k","30142"],["p","<hex>"],["h","<community-hex>"]], "content": "" }` für zwei bis drei offen lizenzierte Materialien aus dem Materialpool, die zur Community passen (ALPIKA Grundschule: Grundschul-Material; reliGlobal: Globales Lernen; rpi-virtuell: neu angelegte Materialien); signiert mit dem Community-Schlüssel, der nach der edufeed-Regel immer teilen darf. Welche Materialien, entscheidet Jörg mit der Redaktion; die Vorlagen sind Vorschläge.
  - `Hub-Entwicklung/kataloge/README.md`: was Grundschicht und Kuratierung sind, wie das Team Inhalte teilt (edufeed-App: „In Community teilen“), wie eine Kuratierungsliste entsteht (edufeed-App: Listen › Neue Liste › Kuratierungsliste, `d` = `katalog`), wie Entfernen funktioniert (Menü „Aus der Community entfernen“, nur mit dem Community-Schlüssel wirksam im Hub), und dass Bunker-Links und `nsec` nie ins Repo gehören.

- [ ] **Step 1: Skript, README und Vorlagen schreiben** (keine Namen, keine Schlüssel außer `npub`/Hex); `deno check tools/listen/veroeffentlichen.ts`.
- [ ] **Step 2: Prüfen** · Run: `cd ~/repositories/FOERBICO_und_rpi-virtuell && mkdir -p /tmp/claude-501/kat && cp Hub-Entwicklung/kataloge/README.md tools/listen/README.md Hub-Entwicklung/2026-11-07-etappe-4-bedarf-team.md /tmp/claude-501/kat/ && python3 -I tools/nachweis/check.py erschliessung /tmp/claude-501/kat && python3 -I -c "import json,glob; [json.load(open(f)) for f in glob.glob('Hub-Entwicklung/kataloge/*.json')]; print('json ok')" && deno run --allow-read=Hub-Entwicklung/kataloge tools/listen/veroeffentlichen.ts Hub-Entwicklung/kataloge/personen-liste.json NSEC_FOERBICO --dry-run` · Expected: „ohne Befund“, `json ok`, das unsignierte Event ohne Fehler.
- [ ] **Step 3: Gate**: Jörg legt die Env-Datei an, liest Vorlagen und Repost-Vorschläge gegen, nennt die npubs für die Personen-Liste; dann je Vorlage ein Lauf des Skripts (eigener Aufruf je Schlüssel, nie in Schleife, Pause zwischen den Läufen wegen der Adresssperre der Relays); Commit auf `kataloge-und-personen`, Merge nach `main` durch Jörg, `sync navigation` für die FOERBICO-Liste (Lauf von Hand mit lokalem Schlüssel, wie bei Menü und Fußzeile). Danach zeigen `#kooperieren/personen` „live · n Personen“ und `#community?c=oercommunity&zu=katalog` „1 Listen“ ohne Codeänderung.

```bash
cd ~/repositories/FOERBICO_und_rpi-virtuell && git checkout -b kataloge-und-personen main && git add Website/navigation.yaml tools/listen Hub-Entwicklung/kataloge && git commit -m "Inhaltsstrang Etappe 4: FOERBICO-Katalog in navigation.yaml, Veröffentlichungsskript für Listen und Reposts, Vorlagen für Personen-Liste und beispielhaftes Teilen"
```

### Task 8: Abschluss der Etappe (vorbereitet, Veröffentlichung nur durch Jörg)

**Files:** `~/.config/poutnik/protokolle/issue-kommentare-2026-12-07/`: `00-uebersicht.md` und vier Kommentar-Entwürfe `01-kommentar-sammlung.md`, `02-kommentar-katalog.md`, `05-kommentar-fortbildungskalender.md`, `06-kommentar-personen.md` (Form wie Runde 6: `ZIEL:`/`ID:` in voller Länge aus den `.fertig.json`, Leerzeile, Text „Umgesetzt in PR {{pr:<branch>}} (main {{main}}): <Entscheidung in einem Satz>. Ausprobieren: https://hub.rpi-virtuell.net/#<route>. Offen bleibt: <ein Satz>.“; der Katalog-Kommentar nennt ehrlich, was je Community geteilt ist und dass es noch keine Kuratierungsliste gibt). FOERBICO-Repo: `Hub-Entwicklung/2026-12-07-etappe-4-uebergabe.md` (Branch-Stapel mit SHAs, Merge-Ablauf, Gates, Hashes nach dem Merge, Schnappschuss-Hinweis), Spec-Fahrplan vierte Zeile „Erledigt am <Datum>: …“, Kommentare auf den Nachweis-Issues (Nummern in `Orga/nachweis-hub/ergebnis.json`: `04-ap-4-5` → #882 für 4.5, `05-ap-4-6` → #883 für 4.6, `09-ap-6-3` → #887 für 4.9, `13-ap-9-5` → #891 und `14-ap-2-4` → #892 für 4.10) über `forgejo-api comment` (eigener Aufruf, nicht mit Commit kombiniert, Token aus `~/.config/forgejo/token.txt`), Commit der Dateien.

- [ ] **Step 1: Entwürfe schreiben und prüfen** · Run: `python3 -I tools/nachweis/check.py gitworkshop ~/.config/poutnik/protokolle/issue-kommentare-2026-12-07` · Expected: Exit 0.
- [ ] **Step 2: Gate**: Jörg pusht die PRs (`deno task push … --as poutnik`), mergt, pusht `main`, setzt `{{pr:…}}` und `{{main}}` (Skript aus der Etappe-2-Übergabe), liest die Kommentare, gibt frei.
- [ ] **Step 3: Veröffentlichen** (nach Freigabe) · Run: je Datei `zsh tools/poutnik/skripte/pub-comment.sh <datei>` in der Reihenfolge 01, 02, 05, 06; `cd tools/poutnik && deno task threads --repo reli-hub --since 1` · Expected: vier Kommentare von Poutník mit heutigem Datum.
- [ ] **Step 4: Buchführung** · Spec-Fahrplan, Forgejo-Kommentare, Commit und Push im FOERBICO-Repo wie am 04.11.; Prüfung `python3 -I tools/nachweis/check.py erschliessung <ordner mit den neuen Dateien>` · Expected: ohne Befund.
- [ ] **Step 5: Schnappschuss vor der Tagung**: Wird der Stapel vor dem 16.11. gemergt, läuft `deno task schnappschuss` auf einem frischen Branch `pr/schnappschuss-2026-11-16` nach dem Muster der Etappe-3-Übergabe, mit den Quellen aus Task 4; sonst bleibt die dort beschriebene Erneuerung mit den relilab-Quellen.

## Selbstprüfung gegen die Spec

- 4.5 Sammlung: Filter (Task 2), Abonnieren (Task 2, Stufe A als Nostr-Filter, Stufe B Liste deaktiviert), Einbetten mit zwei Wegen (Task 2; der Shortcode-Parameter `community` liest dieselbe `h`-Logik wie der Hub), Teilen (Task 2), Leiste als Widget ist Etappe 2. Gedeckt.
- 4.6 Kataloge: Katalog-Seite je Community mit Stand (Task 3), geteilte Inhalte als Grundschicht ohne Lieferpflicht (Task 1, 3), Kuratierungslisten als zweite Schicht (Task 1, 3, 7), Materialpool als Katalog der Instanz rpi-virtuell (Task 3), Redaktionsoberfläche ist Stufe B (ADR, Etappe 5). Gedeckt; die Zusage „redaktionelle Aufbereitung“ erfüllt heute das Teilen in der App, die Liste kommt dazu.
- 4.9 Kalender: alle Quellen (Task 4 Quellenliste plus `h`), zwei Logiken als Taxonomie (Task 4), rpi-virtuell als Einstieg zu den Instituten (Task 4 Umbau `rvOpen`), Konsole (Task 4). Gedeckt; ptz-Termine brauchen Schlüssel oder `h` (Bedarf).
- 4.10 Personen: Personen-Ansicht (Task 5), echte Profile (Task 5 plus Team), Profil-Ansicht echt (Task 5 als `#person`, `#profil` bleibt Persona bis zur Anmeldung, bewusst), Folgen ist Rückfall nach Spec 8, Mastodon-Hinweis (Task 5 Satz). Gedeckt.
- 5a: Katalog FOERBICO über `navigation.yaml` (Task 7), Kataloge der vier Communities aus dem Geteilten plus optionale Listen (Task 7 README), Personen-Liste und Profile (Task 7, Bedarf), Termine ALPIKA (Bedarf). Gedeckt.
- 7: vier Issues bekommen je einen Kommentar (Task 8); ADR nötig: ja (Task 6).
- 8: Fahrplanzeile „bis 07.12.“ (Task 8). Gedeckt.
