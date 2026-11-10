# Hub als Nachweis, Etappe 5a: Beziehungsgefüge, Mitmachen, Zuschnitt, Anmeldung. Umsetzungsplan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bis 07.12.2026 zeigt der reli_hub das Netzwerk als Beziehungsgefüge: eine Ansicht „Ökosystem“ mit vier Reihen (Personen, Events, Communities, Materialien), deren Kanten aus den Events selbst kommen, eine live gelesene Communities-Liste mit Partnerkacheln (Zeilen 4.1, 4.7); einen öffentlichen Raum „Mitmachen“ mit Aktivitätsprotokoll als dauerhafter Relay-Subscription und Kommentaren nach NIP-22 (4.19, Stufe B); das relilab-Schaufenster als Labor mit der Trias Materialien, Menschen, Mitmachen (4.11); den Zuschnitt des ganzen Hubs auf eine Community über `?c=<npub>` mit einer Seite „Eigene Instanz“ (4.17); und die Anmeldung per NIP-07, die Folgen, Beitreten, Zusagen, Gefällt mir und das Speichern einer Sammlung als Nostr-Liste freischaltet (Stufe B der Zeilen 4.5, 4.10, 4.19). Vorbild für die Herangehensweise ist der Nachbau `docs/community-hub.html` im FOERBICO-Repo (08.11.2026); dessen Muster werden in den reli_hub übernommen, nicht daneben gestellt. Die übrigen Zeilen der Fahrplanstufe „bis 23.12.“ (4.4 Veröffentlichen, 4.8 Servicepoint, 4.16, 4.18 Klickweg, Erschließungs-Layer) folgen in Plan 5b.

**Architecture:** Eine HTML-Datei ohne Build (`index.html`, 4401 Zeilen, drei Inline-Skripte); alles Neue kommt ins Anwendungsskript und nutzt die Datenschicht (`hubFetch`, `datenstand`, ADR-0006), die Inhalte-Bausteine (ADR-0007) und die Community-Inhalte aus Etappe 4 (`coLaden`, `coEintraege`, `eintraegeAufloesen`, `eintragKarte`, `kalLaden`, `peLaden`, `profilAus`, ADR-0008). Neu sind vier Bausteine, die der Nachbau vorgezeichnet hat: ein **Beziehungsgefüge** (`bzBauen`: Entitäten `p:`, `c:`, `m:`, `e:` und ungerichtete Kanten aus Autorschaft, `h`-Tag, Reposts, Mitgliedschaften, Zusagen `kind:31925`, Reaktionen `kind:7`), eine **dauerhafte Subscription** (`hubAbonnieren`, eine je Relay, `since` jetzt, Wiederverbinden) nur für das Protokoll, der **Zuschnitt** (`HUB_C` aus `?c=`) als Datenfilter über alle Ansichten statt eines JSON-Kontextprofils, und die **Anmeldung** (`window.nostr`, NIP-07) mit einem einzigen Sendeweg (`hubSenden`). Drei Relays, Schnappschuss als Rückfall, Farbsystem und Konsolen-Struktur des reli_hub bleiben; was der Nachbau anders macht (purplepag.es, eigenes Design, leer ohne Netz), wird nicht übernommen. Jedes Issue wird ein PR-Branch `pr/<name>`, gestapelt, weil alle `index.html` ändern.

**Tech Stack:** HTML/CSS/JavaScript ohne Framework, WebSocket zu Nostr-Relays (NIP-01; Kinds 0, 1, 3, 7, 16, 1111, 10222, 30000, 30004, 30023, 30142, 31922, 31923, 31925; NIP-07 `window.nostr`; NIP-19; NIP-22 Kommentare; NIP-50 `search`), Deno 2 für Tests und Schnappschuss, ngit 3.0.4 (Konten `poutnik` und `joerg`, Amber), Wrapper `tools/poutnik`, Prüfwerkzeug `tools/nachweis/check.py`.

**Spec:** `docs/superpowers/specs/2026-11-02-hub-nachweis-gesamtkonzeption-design.md` (Abschnitte 3, 4.1, 4.5 B, 4.7, 4.10 B, 4.11, 4.17, 4.19, 5a, 7 Issues 7/11/14/16, 8 Fahrplan fünfte Zeile, 9, 10). Vorbild der Herangehensweise: `docs/community-hub.html` (Commit 51ba154; Funktionen `abfrage`, `abonnieren`, `senden`, `neuBauen`, `verbinde`, `sichtbar`, `punkte`, `karte`, `minis`, `reiheZeichnen`, `aktivitaetBauen`, `anmelden`, `signierenUndSenden`, `aktion`, `suchen`; dort nachlesen, hier übernehmen, nicht importieren). Vorige Pläne und Übergaben: `docs/superpowers/plans/2026-11-07-hub-etappe-4-sammlung-kataloge.md`, `Hub-Entwicklung/2026-12-07-etappe-4-uebergabe.md`. Community-Logik von edufeed: Wiki-Artikel „Sharing and reading community content in edufeed“ (`kind:30818`, `d=edufeed-community-content-sharing`, Edufeed-Schlüssel `bdc21f93…`): Community = `kind:10222`, Mitgliedschaft = `kind:30000 d=communities` mit `p`-Tags, Inhalt mit `h`-Tag oder `kind:16`-Repost, Entfernen-Label `kind:1985`. Kommentare: `~/repositories/oer-community/docs/entscheidungen/0041-kommentare-aus-dem-vertrauenskreis.md` und `docs/superpowers/specs/2026-10-08-kommentare-design.md` (Branch `feat/kommentare`, ungemergt; NIP-22 `kind:1111` mit `E`/`K`/`P` und `e`/`k`/`p`). Schlüsselliste: `Hub-Entwicklung/communities-schluessel.md`. Issue-Texte: `~/.config/poutnik/protokolle/issue-kommentare-2026-11-04/` (`07-oekosystem-karte.md`, `11-eigene-instanz.md`, `14-oeffentlicher-raum.md`, `16-relilab-schaufenster.md`; nevent-Links in den `.fertig.json`).

**Issue-Kurz-IDs** (erste acht Hex-Zeichen der Event-ID): 07 Ökosystem-Karte `e6875f0b`, 11 eigene Instanz `93b36056`, 14 öffentlicher Raum `bfa727b9`, 16 relilab-Schaufenster `6bc628db`; Stufe B von 01 Sammlung `b68eaaa5` und 06 Personen `693c69cc`. Stand 09.11.2026: alle offen, ohne Antwort des Teams.

**Befund vom 09.11.2026 (Sondierung von `relay.edufeed.org`, Grundlage der Entscheidungen unten):**

- Kommentare `kind:1111`: die 150 neuesten sind Fremdverkehr (Antworten auf `kind:1`, `1618`, `1068`), keiner zeigt auf ein Material, einen Termin oder einen Beitrag des Hubs. Der Raum „Mitmachen“ startet deshalb mit einem ehrlichen Leerzustand und liest nur Kommentare mit `K` in `30142`, `30023`, `31922`, `31923` sowie kurze Beiträge `kind:1` mit `h`-Tag auf die Hub-Communities.
- Communities `kind:10222`: 27 auf den beiden Relays, 21 mit Profil (Schlüsselliste vom 04.11.); die Communities-Ansicht des Prototyps zeigt 21 eingebettete Einträge, davon mehrere ohne Schlüssel (relimentar, narrt, Münchner Reli Room, relilab-Untergruppen). Live gibt es weniger, dafür echte; Einträge ohne Schlüssel werden Partnerkacheln (Spec 4.7).
- Der Nachbau `docs/community-hub.html` liest Mitgliedschaften (`kind:30000`, 300), Reposts (`kind:16` mit `#h`), Zusagen (`kind:31925`), Reaktionen (`kind:7` mit `#k`) und baut daraus ein Gefüge; live zeigt er auf jeder Karte die Zahl der Communities oder Mitglieder und beim Anklicken die verbundenen Einträge. Er hält eine Subscription je Relay für das Protokoll offen; die Adresssperre der Relays zählt schnelle Anfragen, keine offenen Verbindungen (Erfahrung seit 23.09.2026).
- Prüf-Label `kind:1985` mit `l=geprueft`: keines (Stufe B von 4.13 bleibt sichtbar als Lücke, kein Gegenstand dieser Etappe).

**Folgepläne (nicht Teil dieses Plans):** 5b bis 23.12. (4.4 Veröffentlichen, 4.8 Servicepoint, 4.16 Fußzeile, 4.18 Klickweg, Abschnitt 5 Erschließungs-Layer, NIP-50-Suche im Materialpool), Etappe 6 Januar (Feinschliff, Probelauf, eingefrorene Kopie).

## Global Constraints

- Launch-Stack ist der HTML-Prototyp: eine Datei `index.html`, kein Build, kein Framework, keine externen Abhängigkeiten außer Google Fonts (Spec 3). Kein Svelte, kein Stack-Wechsel, kein Import aus `docs/community-hub.html`; übernommen wird das Muster, nicht die Datei.
- Relays, von denen der Hub liest und an die er sendet: `wss://relay.edufeed.org`, `wss://relay-rpi.edufeed.org`, `wss://amb-relay.edufeed.org`. Nie `wss://groups.edufeed.org`, nie `wss://purplepag.es` oder andere fremde Relays (Abweichung vom Nachbau). Je Ansicht ein `REQ` pro Relay über `hubFetch`, höchstens eine abhängige Nachfrage; Listen, Labels, Profile, Reaktionen und Zusagen nur mit `authors`, `#h`, `#a` oder `#k` aus festen Mengen, nie global. Ausnahme: das Aktivitätsprotokoll hält **eine** dauerhafte Subscription je Relay (`hubAbonnieren`), `since` = Startzeit, Wiederverbinden höchstens fünfmal mit wachsender Pause; eine zweite Subscription desselben Namens schließt die erste.
- Jede Ansicht zeigt sichtbar „live · …“, „Stand vom <Datum>“ oder „Nachbau · …“ über `datenstand(viewId, zustand, info)`; nichts wird als echt ausgegeben, was nicht vom Relay kam; keine Antwort heißt „Die Relays antworten gerade nicht“, nicht „noch nichts“. Die Communities-Liste behält den eingebetteten Stand als Rückfall (`CY`, Stand vom 26.10.2026); das Beziehungsgefüge zeigt ohne Antwort die Einträge aus den Schnappschüssen (`RT_RAW`, `OC_RAW`, `MP`, `CY`) ohne Kanten und sagt es.
- Inhalte vom Relay sind fremder Text: Namen, `about`, Titel, Kommentare mit `esc()`; `href`/`src` nur über `sichereUrl()` oder Hub-Hash-Routen; Schlüssel nur über `istHex64()`; `a`-Tags nur nach Muster `^\d+:[0-9a-f]{64}:.+$`, `e`-Tags nur 64-Hex; Kommentar-Inhalte werden als Text gezeigt, nie als Markdown oder HTML.
- Anmeldung nur über `window.nostr` (NIP-07) oder „nur ansehen“ mit npub; der Hub fragt nie nach einem `nsec`, speichert keinen Schlüssel und sendet nichts ohne Klick auf genau den Knopf, der es sagt (Folgen, Beitreten, Zusagen, Gefällt mir, Sammlung speichern). Vor jedem Schreiben in eine Liste (`kind:3`, `kind:30000`, `kind:30004`) wird die aktuelle Liste frisch vom Relay geholt und ergänzt, nie blind ersetzt. Jedes gesendete Event zeigt im Toast, wie viele Relays es angenommen haben.
- Mitgliedschaft allein zeigt niemanden in der Personen-Ansicht (Einverständnis-Regel aus Etappe 4 bleibt); im Beziehungsgefüge erscheinen Personen nur mit Profil (`kind:0` mit Namen) und nur, wenn sie mindestens eine Kante haben; wer sich anmeldet, sieht sich selbst.
- Keine Rollenprüfung (das Gruppen-Relay wird nie gelesen); Kanten aus `h`-Tags gelten „wie geteilt, ohne Rollenprüfung“, Entfernen-Label zählen nur vom Community-Schlüssel (ADR-0008).
- Farbsystem nach ADR-0001: Bereichsfarben nur in `:root`; neue Farben als Fläche plus Textfarbe mit mindestens 4,5:1; keine Hex-Bereichsfarbe im Anwendungsskript; Fokus sichtbar; einspaltig bei 375 px. Ökosystem und Mitmachen tragen die Farbe „kooperieren“, Anmeldung die Farbe „hub“.
- Die vier Hub-Ergänzungen je Instanz bleiben (ADR-0002 Punkte 2 bis 4); Porträts unter © werden nicht übernommen; Profilbilder nur aus `kind:0` `picture` der Person oder Community.
- Konsolen-Struktur bleibt (fünf Funktionen, zwölf Aktionen, keine neue Knospe); `hub.home` führt künftig ins Ökosystem; `later()` bleibt nur in `standardAktion`. Die Leiste bleibt das Widget aus Etappe 2; der Zuschnitt erscheint dort als abwählbare Markierung, nicht als neuer Eintrag.
- Keine Arbeitspakete, Meilensteine, AP-/M-Nummern, Förderkennzeichen, kein Projektträger, kein Zwischenbericht in Code, Docs, ADRs, Commits, PR-Texten, Issue-Kommentaren. Prüfung: `deno task test` und `python3 -I tools/nachweis/check.py gitworkshop <ordner>` über jeden Entwurfsordner vor der Veröffentlichung.
- Keine Vornamen von Partnern in Dateien, Commits oder Kommentaren; Rollen („der UX-Gast“, „die Redaktion“, „der Leit-Maintainer“), Handles, Pubkey-Präfixe. Erlaubt: „Jörg Lohrer“, „Jens Dechow“. Namen aus Events werden angezeigt, nicht in den Code geschrieben.
- Keine privaten Schlüssel, `nsec`, Bunker-Links oder Tokens in Dateien oder im Gespräch; nur `npub` und Hex-Pubkeys.
- Hub-Texte auf Deutsch in Du-Ansprache; neue Texte nennen den Hub nicht beim Namen (Faden „Selbstverständnis“ offen); Fußzeilen und `document.title` neuer Ansichten wie in Etappe 4 („ein Vorhaben von FOERBICO · Prototyp“).
- Commits auf PR-Branches mit Author `Poutník <poutnik@users.noreply.edufeed.org>`; Branch `pr/<name>` ab dem Kopf des vorigen Branches (gestapelt), der erste ab `main` (`2ea71041`); Push nur über `cd ~/repositories/FOERBICO_und_rpi-virtuell/tools/poutnik && deno task push pr/<name> --as poutnik --cwd ~/repositories/reli-hub`, nie `git push origin`. `deno.lock` im Klon nie committen; Dateiserver für Browserprüfungen außerhalb des Repos starten (`cd /tmp && deno run --allow-net --allow-read jsr:@std/http/file-server ~/repositories/reli-hub`). Browserprüfungen mit Anmeldung brauchen eine NIP-07-Erweiterung; ohne sie wird der Pfad „nur ansehen“ geprüft und das im Bericht gesagt.
- Merge und Push von `main` nur durch Jörg (Ablauf unten). Nichts wird veröffentlicht, gepusht oder kommentiert ohne sein Ja. Im FOERBICO-Checkout nie Branch wechseln, nie stash oder reset; Inhaltsstrang-Dateien werden nur angelegt, der Commit ist Jörgs Gate.
- Tests dieser Etappe liegen in `tests/beziehungen.test.ts` (Tasks 1, 2, 3, 4) und `tests/zuschnitt-anmeldung.test.ts` (Tasks 5, 6, 7); die 65 Tests der Vorgänger bleiben grün. Zwei bestehende Zusicherungen ändern sich bewusst: `navigation.test.ts` prüft `html.includes('id="v-communities" data-stand="stand:26.10.2026 · Texte teils Beispiel"')` (Task 2 ersetzt sie durch die neue Startzeile) und `id="v-relilab" data-stand="stand:26.10.2026"` (Task 4). Prüfbefehl in jedem Task: `cd ~/repositories/reli-hub && deno task test`.
- Schnittregel der Tests: Funktionen des Anwendungsskripts beginnen mit zwei Leerzeichen (`  function name(…) {`) und enden mit `\n  }`; innere Zeilen sind tiefer eingerückt. Funktionen, die ein Test mit `new Function` baut (`bzBauen`, `bzNachbarn`, `bzPunkte`, `pkEintrag`, `zuschnittAus`, `listeErgaenzen`, `sammlungListe`), rufen außer `esc`, `sichereUrl`, `istHex64`, `tagWert`, `tagWerte` und den im Test mitgeschnittenen Blöcken (`aTagLesen`, `repostZiel`, `kurzHash`) nichts aus dem Skript auf.
- Rückfallreihenfolge dieser Etappe (Spec 8): Gerät der 07.12. in Gefahr, fällt zuerst in Task 6 das Speichern einer Sammlung als Liste weg (Folgen, Beitreten, Zusagen, Gefällt mir bleiben), dann in Task 4 die Spalte „Menschen“ (Kriterien, Materialien, Mitmachen bleiben), dann in Task 5 die Vorschau auf der Seite „Eigene Instanz“ (Zuschnitt und Schnipsel bleiben). Nicht verhandelbar: Task 1 (Gefüge), Task 2 (Ökosystem und Communities live), Task 3 (Protokoll und Mitmachen), Task 6 (Anmeldung mit mindestens Beitreten und Gefällt mir), weil sie die Zeilen 4.1, 4.7, 4.19 und die Stufe B tragen.

## Was der Hub ohne Beiträge des Teams zeigt (gekennzeichneter Rückfall)

| Zeile | Ohne Zutun des Teams | Kennzeichnung | Sobald das Team liefert |
|---|---|---|---|
| 4.1 Ökosystem | vier Reihen mit echten Kanten aus den vorhandenen Events (Mitgliedschaften, Reposts, Termine, Materialien); Zusagen und Reaktionen, soweit auf den Relays | `live · <n> Einträge · <k> Kanten · ohne Rollenprüfung` | mehr Kanten, sobald Personen zusagen, reagieren, teilen |
| 4.7 Communities | alle `kind:10222` mit Profil live; Einträge ohne Schlüssel als Partnerkachel | `live · <n> Communities · <m> Partner ohne Schlüssel` | Partner mit Schlüssel wechseln von der Kachel in die Liste (Entscheidung Jörg zu 4.7) |
| 4.19 Mitmachen | Protokoll der Aktivitäten live; Kommentare: keine (Leerzustand mit Einladung in die edufeed-App) | `live · <n> Aktivitäten · 0 Kommentare` | Kommentare erscheinen, sobald in der App jemand kommentiert |
| 4.11 relilab | Kriterien, Materialien und Beiträge mit relilab-Bezug, Labortermine; Menschen = Autorinnen und Autoren dieser Inhalte mit Profil | `live · …` | nichts zu liefern |
| 4.17 Zuschnitt | `?c=<npub>` wirkt auf alle Ansichten; „Eigene Instanz“ mit Vorschau und Schnipseln | – | Kooperationsvereinbarung und Bedarfsseite (Inhaltsstrang, Plan 5b) |
| Stufe B | Anmeldung per NIP-07, Aktionen senden an die drei Relays | Toast „angenommen von <n> Relays“ | nichts zu liefern |

## Review Focus

1. Ein `kind:30000`-Event mit `d=communities`, dessen `p`-Tags fremde oder kaputte Schlüssel tragen, ein Repost mit `e`-Ziel auf ein unbekanntes Event, eine Zusage mit `status=declined`, eine Reaktion mit `content='-'`: `bzBauen` legt keine Kante an, verwirft nichts Gültiges und stürzt nicht (Task 1, Test `bzBauen: Kanten nur aus gültigen Bezügen`).
2. Profilname, `about`, Kommentarinhalt oder Community-Name mit HTML oder `</script>`: alle Texte gehen durch `esc()`, Kommentare werden nie als Markdown gerendert, Bilder nur über `sichereUrl()` (Task 2 Test `ozKarte: maskiert`, Task 3 Test `pkEintrag: Kommentar als Text`).
3. Relays antworten nicht, Subscription bricht ab: Ökosystem zeigt die Schnappschuss-Einträge ohne Kanten mit „Stand vom …“, das Protokoll sagt „keine Live-Verbindung“ und versucht höchstens fünfmal neu; nichts springt auf „live“ (Task 2 Test `Ökosystem: drei Zustände`, Task 3 Test `hubAbonnieren: Wiederverbinden begrenzt`).
4. Anmeldung ohne Erweiterung, Signieren abgebrochen, kein Relay nimmt das Event an, Liste auf dem Relay neuer als die geladene: der Hub sagt es im Toast, sendet nichts Halbes, ersetzt keine Liste ohne frisches Holen (Task 6 Tests `listeErgaenzen: ergänzt, ersetzt nie` und `Aktionen: nur mit Signer`).
5. Relay-Last auf der Tagung: ein Rundgang Start → Ökosystem → Mitmachen → relilab → Eigene Instanz → Anmelden öffnet je Relay höchstens eine Verbindung je Ansicht plus die eine Protokoll-Subscription; `bzLaden` ist eine Abfrage, die übrigen Reihen kommen aus den Caches der Etappe 4 (Task 1 Test `bzLaden: ein REQ, feste Mengen`, Task 3 Test `hubAbonnieren: eine je Relay`).

---

## Merge-Ablauf (gilt für jeden Task, wird dort nur referenziert)

Vorbereitung vor dem ersten Push: `cd ~/repositories/reli-hub && git checkout main && git -c nostr.signer=joerg fetch origin main && git log --oneline main..origin/main` (leer heißt: `main` unverändert, sonst `git merge --ff-only origin/main` und den Stapel rebasen).

PR öffnen (nach Jörgs Ja zum Diff): `cd ~/repositories/FOERBICO_und_rpi-virtuell/tools/poutnik && deno task push pr/<name> --as poutnik --cwd ~/repositories/reli-hub` (ausgecheckt muss der Branch sein). Erwartet: `posting proposal as PR event`, kein Patch-Rückfall. PR-Beschreibung: Issue mit Kurz-ID und gitworkshop-Link, Entscheidung in zwei Sätzen, Prüfbefehl `deno task test`.

Mergen (Jörg): `cd ~/repositories/reli-hub && git checkout pr/<name> && ngit --signer joerg pr merge --offline`, nach allen Merges einmal `cd ~/repositories/FOERBICO_und_rpi-virtuell/tools/poutnik && deno task push main --as joerg --cwd ~/repositories/reli-hub` (Amber) und `cd ~/repositories/reli-hub && git push forgejo main`. Erwartet: gitworkshop zeigt die PRs als erledigt, `curl -s https://hub.rpi-virtuell.net/ | grep -c bzBauen` ist größer als 0 (Auslieferung bis 30 Minuten).

Wie in den Etappen 3 und 4: Bringt die Gesamt-Review eine Fix-Welle, kommt sie als `pr/nacharbeit-etappe-5a` auf den Stapel, und der Stapel wird in einer Sitzung vollständig gemergt.

---

### Task 1: Beziehungsgefüge: Entitäten und Kanten aus den Events (Querschnitt für Issues 07, 14, 16, 11)

**Files:** Modify `index.html` (Anwendungsskript, direkt nach dem Block „Community-Inhalte und Listen (ADR-0008)“: neuer Block „Beziehungsgefüge (ADR-0009)“), Create `tests/beziehungen.test.ts`, Modify `docs/daten.md` (Abschnitt „Beziehungsgefüge“). Branch `pr/beziehungen` ab `main` (`2ea71041`).

**Interfaces:**
- Consumes: `hubFetch`, `istHex64`, `tagWert`, `tagWerte`, `aTagLesen`, `repostZiel`, `CO_SCHLUESSEL`, `KAL_HEX`, `mpLaden`/`mpDaten` (Feld `ev`), `ocLaden`/`ocDaten` (`seiten`, `beitraege`, `termine`), `coLaden`/`coDaten` (`direkt`, `reposts`), `kalLaden`/`kalDaten` (rohe Events), `peLaden`/`peDaten` (`liste`, `profile`), `profilAus`.
- Produces:
  - `function bzLaden()` → `Promise<{ antwort: boolean, mitgliedschaften: ev[], communities: ev[], profile: ev[], zusagen: ev[], reaktionen: ev[] }>`, einmal je Sitzung (`bzDaten`; leere Antwort nicht gehalten): **ein** `hubFetch('beziehungen', [{ kinds: [30000], '#d': ['communities'], limit: 300 }, { kinds: [10222], limit: 60 }, { kinds: [0], authors: <Hex aller CO_SCHLUESSEL plus der Autoren der 10222 aus der Schlüsselliste, höchstens 60>, limit: 60 }, { kinds: [31925], limit: 200 }, { kinds: [7], '#k': ['30142', '30023', '31922', '31923'], limit: 200 }], { relays: ['wss://relay.edufeed.org', 'wss://relay-rpi.edufeed.org'] })`; `antwort` = mindestens ein Event. Die Community-Profile werden hier geholt, weil `peLaden` nur die Personen der Personen-Liste kennt; `profile` sind rohe `kind:0`-Events (Auswertung über `profilAus`).
  - `function bzQuellen()` → `{ materialien: ev[], beitraege: ev[], termine: ev[], reposts: ev[], mitgliedschaften: ev[], zusagen: ev[], reaktionen: ev[], personenListe: string[], communities: string[] }`: sammelt aus den Caches (`mpDaten` → `ev`, `ocDaten.beitraege` und `seiten`, `kalDaten`, jedes `coDaten`-Ergebnis → `direkt` und `reposts`, `bzDaten`, `peDaten.liste` → `p`-Tags) ohne Netz; fehlende Caches ergeben leere Listen.
  - `function bzBauen(q)` → `{ ents: Map<id, ent>, kanten: Map<id, Set<id>> }`, rein (keine Netz-, kein DOM-Zugriff): Entitäten `p:<hex>` (`{ id, typ: 'person', pk }`), `c:<hex>` (`{ id, typ: 'community', pk }`), `m:<kind>:<pk>:<d>` (`{ id, typ: 'material', ev, pk }` für `30142` und `30023`), `e:<kind>:<pk>:<d>` (`{ id, typ: 'event', ev, pk, start, ende }` für `31922`, `31923`; `31922` mit Tagesgrenzen); Schlüssel aus `q.communities` sind immer Communities, auch wenn sie Inhalte veröffentlichen. Kanten (ungerichtet, `bzVerbinde(kanten, a, b)`): Inhalt ↔ Autor; Inhalt ↔ jede Community aus `h`-Tags; Termin ↔ jede Person aus `p`-Tags; Mitgliedschaft (`30000 d=communities`) ↔ jede Community aus `p`-Tags; Repost ↔ Ziel über `repostZiel` (nur wenn das Ziel als Entität vorliegt) mit allen `h`-Communities; Zusage `31925` mit `status` `accepted` oder `tentative` ↔ Autor; Reaktion `7` mit `content !== '-'` ↔ Autor; Ziel von Zusage und Reaktion über den ersten `a`-Tag (`aTagLesen`) oder den ersten `e`-Tag, der auf ein adressierbares Event in `q` zeigt. Ungültige Schlüssel (`!istHex64`) erzeugen weder Entität noch Kante. Je adressierbarer Adresse gilt das neueste `created_at`.
  - `function bzNachbarn(kanten, ents, id, typ)` → `ent[]` der Nachbarn vom Typ `typ` (oder alle bei `typ = null`).
  - `function bzPunkte(ents, kanten, id, ich)` → Zahl nach dem Muster des Nachbaus: Person = 3 je Community + min(5, Materialien) + min(4, Termine) + 2 bei Profilbild + 100 wenn `id === 'p:' + ich`; Community = Zahl der Personen; Inhalt = 0.
  - `function bzZeit(ev)` → `{ start, ende, ganz }` (für `31922` aus `YYYY-MM-DD`, für `31923` aus Sekunden).
  - Profile: `bzProfil(hex)` → `profilAus`-Objekt aus `peDaten.profile`, `bzDaten.profile` oder `null`; Namen von Communities zuerst aus dem Profil, sonst aus `CO_SCHLUESSEL`/`CY`, sonst gekürzter npub.

- [ ] **Step 1: Tests schreiben** (`tests/beziehungen.test.ts`, Kopf wie `tests/sammlung.test.ts`: `s`, `block`, `fn`, `bau` mit `esc`, `sichereUrl`, `istHex64`, `tagWert`, `tagWerte`)

```ts
Deno.test('Beziehungsgefüge: Signaturen, Abfrage, Doku', async () => {
  for (const f of ['bzLaden()', 'bzQuellen()', 'bzBauen(q)', 'bzVerbinde(kanten, a, b)', 'bzNachbarn(kanten, ents, id, typ)', 'bzPunkte(ents, kanten, id, ich)', 'bzZeit(ev)', 'bzProfil(hex)']) assert(s.includes('function ' + f), f);
  const l = fn('bzLaden');
  assert(/hubFetch\('beziehungen', \[/.test(l) && /kinds: \[30000\], '#d': \['communities'\], limit: 300/.test(l) && /kinds: \[10222\], limit: 60/.test(l) && /kinds: \[31925\], limit: 200/.test(l) && /kinds: \[7\], '#k': \['30142', '30023', '31922', '31923'\]/.test(l), 'fünf Filter in einem Aufruf');
  assert(/relay-rpi\.edufeed\.org/.test(l) && !/amb-relay/.test(l) && !/purplepag/.test(html) && !/groups\.edufeed\.org/.test(html), 'Relays');
  assert((l.match(/hubFetch\(/g) || []).length === 1, 'ein REQ');
  const d = await Deno.readTextFile(new URL('../docs/daten.md', import.meta.url));
  assert(/bzBauen/.test(d) && /31925/.test(d) && /ohne Rollenprüfung/.test(d), 'docs/daten.md');
});

Deno.test('bzBauen: Kanten nur aus gültigen Bezügen', () => {
  const bz = bau('bzBauen', fn('aTagLesen') + fn('repostZiel') + fn('bzVerbinde') + fn('bzZeit'));
  const A = 'aa'.repeat(32), B = 'bb'.repeat(32), C = 'cc'.repeat(32), ID = 'dd'.repeat(32);
  const mat = { id: ID, kind: 30142, pubkey: A, created_at: 10, tags: [['d', 'm1'], ['h', C]] };
  const term = { id: 'ee'.repeat(32), kind: 31923, pubkey: A, created_at: 11, tags: [['d', 't1'], ['start', '1800000000'], ['p', B]] };
  const q = { materialien: [mat], beitraege: [], termine: [term], reposts: [{ kind: 16, pubkey: B, created_at: 12, tags: [['a', `30142:${A}:m1`], ['h', C]] }, { kind: 16, pubkey: B, created_at: 13, tags: [['e', 'ff'.repeat(32)]] }],
    mitgliedschaften: [{ kind: 30000, pubkey: B, created_at: 14, tags: [['d', 'communities'], ['p', C], ['p', 'kaputt']] }],
    zusagen: [{ kind: 31925, pubkey: B, created_at: 15, tags: [['a', `31923:${A}:t1`], ['status', 'declined']] }, { kind: 31925, pubkey: B, created_at: 16, tags: [['a', `31923:${A}:t1`], ['status', 'accepted']] }],
    reaktionen: [{ kind: 7, pubkey: B, created_at: 17, content: '-', tags: [['e', ID]] }, { kind: 7, pubkey: B, created_at: 18, content: '+', tags: [['e', ID]] }],
    personenListe: [], communities: [C] };
  const { ents, kanten } = bz(q);
  assert(ents.has('p:' + A) && ents.has('p:' + B) && ents.has('c:' + C) && ents.has(`m:30142:${A}:m1`) && ents.has(`e:31923:${A}:t1`), 'Entitäten');
  assert(!ents.has('p:kaputt') && !ents.has('c:kaputt'), 'kaputter Schlüssel ergibt nichts');
  const n = (id: string) => [...(kanten.get(id) || [])].sort();
  assertEquals(n(`m:30142:${A}:m1`), ['c:' + C, 'p:' + A, 'p:' + B].sort(), 'Material: Autor, h-Community, Repost-Community bleibt C, Reaktion B');
  assertEquals(n(`e:31923:${A}:t1`), ['p:' + A, 'p:' + B].sort(), 'Termin: Autor, p-Tag, Zusage (declined zählt nicht)');
  assert(n('c:' + C).includes('p:' + B), 'Mitgliedschaft');
  assertEquals(ents.get(`e:31923:${A}:t1`).start, 1800000000);
});

Deno.test('bzNachbarn und bzPunkte', () => {
  const nb = bau('bzNachbarn'), pt = bau('bzPunkte');
  const ents = new Map([['p:a', { id: 'p:a', typ: 'person', pk: 'a' }], ['c:b', { id: 'c:b', typ: 'community', pk: 'b' }], ['m:x', { id: 'm:x', typ: 'material', pk: 'a' }]]);
  const kanten = new Map([['p:a', new Set(['c:b', 'm:x'])], ['c:b', new Set(['p:a'])], ['m:x', new Set(['p:a'])]]);
  assertEquals(nb(kanten, ents, 'p:a', 'community').map((e: any) => e.id), ['c:b']);
  assertEquals(nb(kanten, ents, 'p:a', null).length, 2);
  assertEquals(pt(ents, kanten, 'p:a', null), 4); assertEquals(pt(ents, kanten, 'p:a', 'a'), 104); assertEquals(pt(ents, kanten, 'c:b', null), 1); assertEquals(pt(ents, kanten, 'm:x', null), 0);
});
```

- [ ] **Step 2: Fehlschlag sehen** · Run: `deno task test` · Expected: drei FAIL in `beziehungen.test.ts`, 65 PASS.

- [ ] **Step 3: Block „Beziehungsgefüge (ADR-0009)“ schreiben** (acht Funktionen, `bzDaten`-Halter); `docs/daten.md`: Abschnitt „Beziehungsgefüge“ (Quellen aus den Caches, der eine Filter, Kantenregeln als Tabelle, „ohne Rollenprüfung“, Grenze: Zusagen und Reaktionen nur die neuesten 200).

- [ ] **Step 4: Tests laufen lassen** · Expected: grün (68).

- [ ] **Step 5: Committen, PR** (`pr/beziehungen`)

```bash
git add index.html tests/beziehungen.test.ts docs/daten.md && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "Beziehungsgefüge: Entitäten und Kanten aus Autorschaft, Communities, Reposts, Mitgliedschaften, Zusagen und Reaktionen; eine Abfrage für Mitgliedschaften, Communities, Zusagen, Reaktionen"
```

### Task 2: Ökosystem als Explorer mit vier Reihen; Communities-Liste live mit Partnerkacheln (Issue 07 `e6875f0b`, Spec 4.1, 4.7)

**Files:** Modify `index.html` (neue Ansicht `<div class="view" id="v-oekosystem" data-stand="nachbau:Gefüge laden">` nach `v-communities`; Anwendungsskript: `ozOpen(qs)`, `ozRender()`, `ozReihe(i)`, `ozKarte(id)`, `ozSichtbar(ent)`, `ozWaehlen(id)`; Communities: `cyLaden()`, `cyAus(ev, profil)`, `cyRender()` liest live; `EX['hub.home'].go = ['Zum Ökosystem', '#oekosystem']`; `route()`: `oekosystem`; Partnerkacheln der Startseite: `PARTNERS` ohne Schlüssel bekommen `kind: 'partner'`; CSS `.oz-*`), Modify `tests/beziehungen.test.ts`, `tests/navigation.test.ts` (Startzeile `v-communities`), `docs/daten.md`, `docs/navigation.md`. Branch `pr/oekosystem` ab `pr/beziehungen`.

**Interfaces:**
- Consumes: `bzLaden`, `bzQuellen`, `bzBauen`, `bzNachbarn`, `bzPunkte`, `bzProfil`, `mpLaden`, `ocLaden`, `coLaden` (für die fünf `CO_SCHLUESSEL`), `kalLaden`, `peLaden`, `eintragKarte`, `datenstand`, `go`, `esc`, `sichereUrl`, `bech32`, `CY`, `PARTNERS`, `cyCards`, `HUB_C` (ab Task 5; bis dahin `null`).
- Produces:
  - Route `#oekosystem?wahl=<id>&reihen=person,event,community,material` (Reihenfolge der vier Reihen, Standard wie angegeben; `wahl` = Entitäts-ID aus Task 1, maskiert mit `encodeURIComponent`).
  - `function ozOpen(qs)`: liest `wahl` und `reihen`; zeigt sofort die Schnappschuss-Einträge (Materialien `MP`, Termine `RT_RAW`, Beiträge `OC_RAW`, Communities `CY`) ohne Kanten mit `Stand vom <jüngstes Schnappschuss-Datum>`; ruft `Promise.all([mpLaden(), ocLaden(), kalLaden(), peLaden(), bzLaden(), ...CO_SCHLUESSEL.map(k => coLaden(k.hex))])`, baut mit `bzBauen(bzQuellen())`, hält `{ ents, kanten }` in `ozGefuege`, rendert; mit Antwort `live · <n> Einträge · <k> Kanten · ohne Rollenprüfung`, ohne Antwort von `bzLaden` bleibt der Stand und der Hinweis „Verbindungen können gerade nicht geladen werden“. Lauf-Zähler gegen späte Antworten.
  - `function ozSichtbar(ent)` → boolean: Person nur mit Profilname und mindestens einer Kante (oder angemeldet als diese Person); Community immer; Termin nur, wenn `ende` oder `start` nicht älter als ein Tag; Material `30023` nur mit Community-Bezug (eigene oder Autor-Kante zu einer Community) oder Autor in der Personen-Liste; bei gesetztem `HUB_C` nur Einträge mit Kante zu `c:HUB_C` oder Autor mit dieser Kante.
  - `function ozReihe(i)`: Reihe `i` mit Kopf (Titel, Lupe mit Filterfeld, Hinweiszeile), Fokuskarte und Spur; ohne Auswahl die Liste nach `bzPunkte` (Personen, Communities) beziehungsweise Community-Bezug zuerst, dann Datum (Termine aufsteigend, Materialien absteigend), höchstens 80 je Reihe; mit Auswahl `ozWahl` die Nachbarn vom Typ der Reihe und Hinweis „<n> verbunden mit „<Name>““ oder „Keine Verbindung zu „<Name>““; Tauschknöpfe zwischen den Reihen schreiben `reihen` in die Route.
  - `function ozKarte(id)` → HTML: Form je Typ (Person rund, Community Sechseck, Termin und Material rechteckig mit leichter Drehung wie im Nachbau), Bild (`sichereUrl` aus Profil oder `image`-Tag, Platzhalter mit Initialen in einer Farbe aus `kurzHash(id)`), Pille (Person: „<n> Communities“ oder „Das bist du“; Community: „<n> Mitglieder“; Termin: Datum; Material: `learningResourceType:prefLabel:de` oder „Beitrag“), Name, Untertitel (`about`, `summary`, `description`, je 90 Zeichen), Minis (bis fünf verbundene Personen/Communities, „+n“), `data-wahl`, `aria-pressed`.
  - Auswahlzeile über den Reihen (`#ozAuswahl`): Typ, Name, Links „Bei edufeed ansehen ›“ (`https://edufeed.org/c/<npub>` für Communities, `#person?p=<npub>` für Personen, `#materialpool?d=…&p=…` für Materialien, `e.u` für Termine), ab Task 6 die Aktionsknöpfe; Knopf ✕ hebt die Auswahl auf; Escape ebenso.
  - Communities live: `function cyLaden()` → einmal je Sitzung aus `bzDaten.communities` (`kind:10222`) und `bzDaten.profile`; `function cyAus(ev, profil)` → `{ id: <Hex-Präfix 8>, hex, n: profil.name || 'Community ' + kurz, ab: Initialen, col: C.kooperieren, ty: 'netz', bio: profil.about (gekürzt 90), back: profil.about, m: <Zahl der Mitglieder aus dem Gefüge>, bild: sichereUrl(profil.picture), live: true }`; bekannte Schlüssel (`CO_SCHLUESSEL`, Schlüsselliste) behalten ihre `CY`-Kennung (`id`), damit `#community?c=<id>` weiter gilt (Zuordnung `CY_HEX` = Map `hex → id` für die Einträge, deren npub bekannt ist: rpi-virtuell, relilab, religlobal, alpika-gs, konfi `npub1jt62ef…`, frieden `npub1vsnck0…`, kuru `npub10dxgwe…`, agdm `npub1dnyvcx…`, kph `npub1vkn99j…`, rpi `npub1wak8hl…`, oercommunity = Schaufenster-Schlüssel ohne 10222, bleibt eingebettet); RpiCommunity `npub1gc2zfp…` wird ausgeblendet (Entscheidung 04.11.). `cyRender()` zeigt die Live-Einträge, dahinter die eingebetteten Einträge ohne Schlüssel als **Partnerkacheln** (Klasse `cy-partner`, Hinweis „Partner ohne eigenen Schlüssel im Datenraum“, kein Folgen-Knopf, kein Raum-Knopf, Link auf die Webseite, falls `PARTNERS` eine kennt); Stand-Zeile `live · <n> Communities · <m> Partner ohne Schlüssel`, ohne Antwort `Stand vom 26.10.2026 · Texte teils Beispiel`. Das HTML-Attribut von `v-communities` wird `data-stand="stand:26.10.2026 · Texte teils Beispiel"` belassen (Test in `navigation.test.ts` bleibt gültig).
  - Startseite: `PARTNERS`-Kacheln ohne `href` tragen das Wort „Partner“ und führen zu `#communities`; `EX['hub.home'].go` zeigt ins Ökosystem; `docs/navigation.md`: Zeile „Ökosystem | Home | `hub.home` | `#oekosystem` | – | reli_hub | gebaut“ ersetzt die Zeile Start/Home-Ziel `#partner`.

- [ ] **Step 1: Tests ergänzen**

```ts
Deno.test('Ökosystem: Ansicht, Route, drei Zustände, Karten maskiert', () => {
  assert(/id="v-oekosystem" data-stand="nachbau:/.test(html), 'Ansicht mit Stand-Zeile');
  assert(/'oekosystem'/.test(block(/function route\(\)[\s\S]*?window\.scrollTo/)) && /ozOpen\(/.test(s), 'Route');
  const o = fn('ozOpen');
  assert(/bzLaden\(\)/.test(o) && /bzBauen\(bzQuellen\(\)\)/.test(o) && /Stand vom/.test(o) && /ohne Rollenprüfung/.test(o) && /können gerade nicht geladen werden/.test(o), 'Zustände');
  const k = fn('ozKarte');
  assert(/esc\(/.test(k) && /sichereUrl\(/.test(k) && /kurzHash\(/.test(k) && /aria-pressed/.test(k) && /Das bist du/.test(k), 'Karte');
  assert(/function ozSichtbar\(ent\)/.test(s) && /HUB_C/.test(fn('ozSichtbar')), 'Sichtbarkeit kennt den Zuschnitt');
  assert(/'hub\.home': \{[^}]*#oekosystem/.test(s), 'Konsole: Home führt ins Ökosystem');
});

Deno.test('Communities live: cyAus, Partnerkacheln, RpiCommunity ausgeblendet', () => {
  const ca = bau('cyAus', "const C = { kooperieren: '#000' }; const kurzHash = () => 'abcd1234';");
  const ev = { kind: 10222, pubkey: 'ab'.repeat(32), created_at: 1, tags: [['r', 'wss://relay.edufeed.org']] };
  const c = ca(ev, { name: '<b>Kreis</b>', about: 'x'.repeat(200), picture: 'javascript:x' });
  assertEquals(c.hex, 'ab'.repeat(32)); assertEquals(c.n, '<b>Kreis</b>'); assert(c.bio.length <= 92 && c.bild === '' && c.live === true);
  const cy = fn('cyRender');
  assert(/cy-partner/.test(cy) && /Partner ohne eigenen Schlüssel/.test(cy), 'Partnerkacheln');
  assert(/npub1gc2zfp/.test(s) && /ausgeblendet|RpiCommunity/.test(block(/const CY_HEX[\s\S]*?\n  \]\)?;/) + fn('cyLaden')), 'RpiCommunity ausgeblendet');
  assert(html.includes('id="v-communities" data-stand="stand:26.10.2026 · Texte teils Beispiel"'), 'Startwert bleibt');
});
```

- [ ] **Step 2: Fehlschlag sehen** · Expected: zwei FAIL, 68 PASS.

- [ ] **Step 3: Ansicht, Funktionen, Communities live, Partnerkacheln, Konsole, CSS (`.oz-reihe`, `.oz-karte` mit `--oz-hell`/`--oz-text` in `:root`, Formen über `border-radius` und `clip-path`, Fokus sichtbar, einspaltig bei 375 px), Doku schreiben**; `docs/daten.md`: Verbraucher „Ökosystem“ und „Communities (live)“; `docs/navigation.md` nachführen.

- [ ] **Step 4: Tests laufen lassen** · Expected: grün (70).

- [ ] **Step 5: Im Browser prüfen**: `#oekosystem` zeigt erst „Stand vom …“, dann „live · n Einträge · k Kanten · ohne Rollenprüfung“; Klick auf reliGlobal zeigt in den drei anderen Reihen die verbundenen Materialien, Termine, Personen; Tausch der Reihen schreibt die Route; `#communities` zeigt live Communities mit Mitgliederzahl, dahinter Partnerkacheln; RpiCommunity fehlt; offline: Schnappschuss ohne Kanten; Netzwerk: eine Verbindung je Relay für `beziehungen`, die übrigen Daten aus den Caches; 375 px: Reihen untereinander.

- [ ] **Step 6: Committen, PR** (`pr/oekosystem`)

```bash
git add index.html tests/beziehungen.test.ts tests/navigation.test.ts docs/daten.md docs/navigation.md && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "Ökosystem: Explorer mit vier Reihen aus dem Beziehungsgefüge; Communities live vom Relay mit Partnerkacheln"
```

### Task 3: Aktivitätsprotokoll als Subscription und öffentlicher Raum „Mitmachen“ (Issue 14 `bfa727b9`, Spec 4.19)

**Files:** Modify `index.html` (Datenschicht: `hubAbonnieren(name, filters, opts)`, `hubAbbestellen(name)`; neuer Block „Mitmachen (ADR-0009)“: `pkLaden()`, `pkEintrag(ev, gefuege)`, `pkRender()`; neue Ansicht `<div class="view" id="v-mitmachen" data-stand="nachbau:Protokoll verbinden">`; Protokoll-Streifen auch im Ökosystem (`#ozProtokoll`); `route()`: `mitmachen`; Konsole: `kooperieren` Erklärkarte bekommt den Satz mit Link; CSS `.pk-*`), Modify `tests/beziehungen.test.ts`, `tests/datenschicht.test.ts` (ein Test für `hubAbonnieren`), `docs/daten.md`, `docs/navigation.md`. Branch `pr/mitmachen` ab `pr/oekosystem`.

**Interfaces:**
- Consumes: `hubFetch`, `RELAYS`, `MAX_CONN` (die Subscription zählt nicht gegen die Warteschlange von `hubFetch`, hält aber nie mehr als eine Verbindung je Relay), `bzBauen`/`ozGefuege`, `bzProfil`, `repostZiel`, `aTagLesen`, `CO_SCHLUESSEL`, `eintragKarte`, `datenstand`, `esc`, `sichereUrl`, `bech32`, `HUB_C`.
- Produces:
  - `function hubAbonnieren(name, filters, opts)` → `{ schliessen() }`: öffnet je Relay aus `opts.relays` (Standard: `relay.edufeed.org`, `relay-rpi.edufeed.org`) eine WebSocket-Verbindung mit `REQ` und `filters` plus `since: Math.floor(Date.now()/1000)`; `opts.beiEvent(ev)` je `EVENT`, `opts.beiStatus(n)` mit der Zahl verbundener Relays; bei `close` Wiederverbinden nach `4000 * (versuch + 1)` ms, höchstens fünf Versuche je Relay; `hubAbonnieren` mit demselben `name` schließt die vorige Subscription (Halter `hubAbos` Map). `hubAbbestellen(name)` schließt und löscht.
  - `const PK_KINDS = [30142, 30023, 31922, 31923, 31925, 7, 16, 30000, 1111, 1]`.
  - `function pkLaden()` → `Promise<{ antwort, kommentare: ev[], beitraege: ev[] }>`, einmal je Sitzung: `hubFetch('mitmachen', [{ kinds: [1111], '#K': ['30142', '30023', '31922', '31923'], limit: 100 }, { kinds: [1], '#h': CO_SCHLUESSEL.map(k => k.hex), limit: 100 }], { relays: [die zwei Relays] })`.
  - `function pkEintrag(ev, gefuege)` → `{ id, zeit, bezug: string[], html } | null`: Satz je Kind nach dem Muster des Nachbaus („hat ‹Termin› angelegt“, „hat [Material] veröffentlicht“, „hat den Beitrag [..] geschrieben“, „hat ‹..› im Kalender gespeichert“ / „kommt vielleicht zu ‹..›“ / „hat ‹..› abgesagt“, „hat [..] geliked“ / „abgelehnt“ / „mit <Zeichen> markiert“, „hat [..] in {Community} geteilt“, „ist {Community} beigetreten“, Kommentar `1111`: „hat zu [..] geschrieben: „<Text, 160 Zeichen>““, Beitrag `1`: „schreibt in {Community}: „<Text>““); `bezug` = alle verlinkten Entitäts-IDs plus der Autor; Ziel über `a`- oder `e`-Tag wie in `bzBauen`; Events ohne auflösbares Ziel ergeben `null` (außer eigene Inhalte und Beiträge `kind:1`); Namen über `bzProfil`, sonst gekürzter npub; alle Texte über `esc`, Kommentar- und Beitragsinhalt als Text (nie `mdSeite`), Links nur als Hub-Routen (`data-wahl` ins Ökosystem oder `#materialpool?d=…`, `#person?p=…`, `#community?c=…`).
  - `function pkRender()`: Ansicht `#mitmachen?c=<id>`: Kopf „Mitmachen“ mit Satz „Was im Ökosystem gerade passiert: Kommentare, Zusagen, Reaktionen, Geteiltes. Lesen geht ohne Anmeldung, Schreiben mit Schlüssel in der edufeed-App.“; Filter nach Community (Auswahl aus `CO_SCHLUESSEL` plus live gefundene Communities, Vorbelegung `HUB_C`); zwei Spalten: links das Protokoll (neueste 80, relative Zeit, neue Einträge mit Klasse `neu`), rechts „Gespräche“: Kommentare gruppiert nach Ziel (Karte des Ziels über `eintragKarte`, darunter die Kommentare als Text mit Autor und Zeit) und kurze Beiträge mit Community-Bezug; Leerzustand „Noch kein Gespräch zu Materialien, Terminen oder Beiträgen des Ökosystems. Der erste Kommentar entsteht in der edufeed-App.“ mit Link `https://edufeed.org`; Stand-Zeile `live · <n> Aktivitäten · <k> Kommentare · Protokoll verbunden mit <r> von 2 Relays`, ohne Antwort `Nachbau · Relays nicht erreichbar`, ohne Subscription-Verbindung Zusatz „· keine Live-Verbindung“. Das Protokoll speist sich aus `pkEintrag` über alle Events in `bzQuellen()` plus `pkLaden` plus den Live-Events; Live-Events werden gesammelt (`pkNeu`), nach 600 ms gebündelt in `bzQuellen` nachgetragen (`bzDaten` und `coDaten` werden nicht verändert; die Live-Events liegen in `pkLive`), das Gefüge wird neu gebaut und Ökosystem wie Mitmachen gezeichnet.
  - Ökosystem (Task 2) bekommt den Streifen `#ozProtokoll` mit den neuesten acht Protokollzeilen und Link „Alle im Raum Mitmachen ›“.
  - relilab: `#relilab?tab=mitmachen` zeigt denselben Raum mit `c=relilab` (Task 4 baut den Tab, hier nur die Funktion `pkRender(root, c)` mit Wurzel-Parameter).
  - Konsole: `EX['kooperieren'].p2`/`go2` wie bei `finden.material`: Satz „Was gerade besprochen wird, steht im Raum Mitmachen.“ mit Link `#mitmachen`. `docs/navigation.md`: Zeile „Mitmachen | – | – (Erklärkarte kooperieren) | `#mitmachen` | – | kooperieren | gebaut“.

- [ ] **Step 1: Tests ergänzen** (`tests/datenschicht.test.ts` für `hubAbonnieren` nach dem Muster der dortigen Verhaltenstests mit einem WebSocket-Stub; `tests/beziehungen.test.ts` für `pkEintrag` und die Ansicht)

```ts
// tests/datenschicht.test.ts
Deno.test('hubAbonnieren: eine Verbindung je Relay, since gesetzt, Wiederverbinden begrenzt, gleicher Name ersetzt', async () => {
  const offen: any[] = [];
  class WS { url: string; onopen: any; onmessage: any; onclose: any; onerror: any; sent: string[] = []; closed = false;
    constructor(u: string) { this.url = u; offen.push(this); setTimeout(() => this.onopen && this.onopen(), 0); }
    send(m: string) { this.sent.push(m); } close() { this.closed = true; setTimeout(() => this.onclose && this.onclose(), 0); } }
  const src = block(/  const hubAbos = new Map\(\);[\s\S]*?  function hubAbbestellen\(name\) \{[\s\S]*?\n  \}/);
  const api = new Function('WebSocket', 'setTimeout', src + '; return { hubAbonnieren, hubAbbestellen, hubAbos };')(WS, (f: any, ms: number) => setTimeout(f, Math.min(ms, 5)));
  const status: number[] = [];
  api.hubAbonnieren('t', [{ kinds: [7] }], { relays: ['wss://a', 'wss://b'], beiEvent: () => {}, beiStatus: (n: number) => status.push(n) });
  await new Promise(r => setTimeout(r, 20));
  assertEquals(offen.length, 2); assert(offen.every(w => /"since":\d{10}/.test(w.sent[0])), 'since gesetzt'); assertEquals(status.at(-1), 2);
  api.hubAbonnieren('t', [{ kinds: [7] }], { relays: ['wss://a'], beiEvent: () => {}, beiStatus: () => {} });
  await new Promise(r => setTimeout(r, 20));
  assert(offen[0].closed && offen[1].closed, 'gleicher Name schließt die vorige');
  for (let i = 0; i < 8; i++) { offen.at(-1).close(); await new Promise(r => setTimeout(r, 30)); }
  assert(offen.length <= 3 + 5, 'höchstens fünf Wiederverbindungen');
  api.hubAbbestellen('t'); assertEquals(api.hubAbos.size, 0);
});

// tests/beziehungen.test.ts
Deno.test('pkEintrag: Sätze je Kind, Kommentar als Text, ohne Ziel null', () => {
  const pe = bau('pkEintrag', fn('aTagLesen') + fn('repostZiel') + "const bzProfil = () => null; const bech32 = () => 'npub1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'; const CO_SCHLUESSEL = [];");
  const A = 'aa'.repeat(32), C = 'cc'.repeat(32);
  const ents = new Map([[`m:30142:${A}:m1`, { id: `m:30142:${A}:m1`, typ: 'material', ev: { kind: 30142, pubkey: A, tags: [['d', 'm1'], ['name', 'Gen 1 <b>']] }, pk: A }], ['c:' + C, { id: 'c:' + C, typ: 'community', pk: C }]]);
  const g = { ents, kanten: new Map() };
  const k = pe({ id: 'k1', kind: 1111, pubkey: A, created_at: 5, content: '<script>x</script> gut', tags: [['K', '30142'], ['A', `30142:${A}:m1`], ['a', `30142:${A}:m1`]] }, g);
  assert(k && /hat zu/.test(k.html) && /&lt;script&gt;/.test(k.html) && !/<script/.test(k.html) && /Gen 1 &lt;b&gt;/.test(k.html), 'Kommentar maskiert');
  assertEquals(pe({ id: 'k2', kind: 7, pubkey: A, created_at: 6, content: '+', tags: [['e', 'ff'.repeat(32)]] }, g), null, 'ohne Ziel null');
  const r = pe({ id: 'k3', kind: 16, pubkey: A, created_at: 7, tags: [['a', `30142:${A}:m1`], ['h', C]] }, g);
  assert(r && /geteilt/.test(r.html) && r.bezug.includes('c:' + C) && r.bezug.includes('p:' + A), 'Repost mit Community');
});

Deno.test('Mitmachen: Ansicht, Abfrage, Zustände, Protokoll im Ökosystem', () => {
  assert(/id="v-mitmachen" data-stand="nachbau:/.test(html) && /'mitmachen'/.test(block(/function route\(\)[\s\S]*?window\.scrollTo/)), 'Ansicht und Route');
  const l = fn('pkLaden');
  assert(/hubFetch\('mitmachen', \[\{ kinds: \[1111\], '#K': \['30142', '30023', '31922', '31923'\], limit: 100 \}, \{ kinds: \[1\], '#h': CO_SCHLUESSEL\.map/.test(l), 'zwei Filter, feste Mengen');
  const r = fn('pkRender');
  assert(/Noch kein Gespräch/.test(r) && /antworten gerade nicht|Relays nicht erreichbar/.test(r) && /keine Live-Verbindung/.test(r) && /Protokoll verbunden mit/.test(r), 'Zustände');
  assert(/hubAbonnieren\('protokoll', \[\{ kinds: PK_KINDS/.test(s) && /id="ozProtokoll"/.test(html), 'Subscription und Streifen');
  assert(!/mdSeite\(/.test(r) && !/mdSeite\(/.test(fn('pkEintrag')), 'Kommentare nie als Markdown');
});
```

- [ ] **Step 2: Fehlschlag sehen** · Expected: drei FAIL (zwei in `beziehungen`, einer in `datenschicht`), 70 PASS.

- [ ] **Step 3: Datenschicht-Erweiterung, Block „Mitmachen“, Ansicht, Streifen im Ökosystem, Konsolen-Satz, CSS (`.pk-liste`, `.pk-neu` mit Hervorhebung in `--c-koop`-Hellton), Doku schreiben**; `docs/daten.md`: Abschnitt „Subscription für das Protokoll“ (Regeln: eine je Relay, `since`, fünf Versuche, nie für Listen oder Inhalte) und Verbraucher „Mitmachen“; `docs/navigation.md` nachführen.

- [ ] **Step 4: Tests laufen lassen** · Expected: grün (73).

- [ ] **Step 5: Im Browser prüfen**: `#mitmachen` zeigt das Protokoll mit relativen Zeiten und „Protokoll verbunden mit 2 von 2 Relays“; „Gespräche“ zeigt den Leerzustand (Stand 09.11.); Community-Filter reduziert; ein neu in der App geteiltes Material erscheint innerhalb von Sekunden als „neu“ (wenn möglich während der Prüfung einmal in der App teilen, sonst im Bericht sagen); Netzwerk: zwei dauerhafte WebSockets, sonst keine neuen Abfragen; Verlassen der Ansicht lässt die Subscription laufen (sie gilt für die Sitzung), Neuladen baut sie neu auf.

- [ ] **Step 6: Committen, PR** (`pr/mitmachen`)

```bash
git add index.html tests/beziehungen.test.ts tests/datenschicht.test.ts docs/daten.md docs/navigation.md && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "Mitmachen: Aktivitätsprotokoll als Subscription je Relay, Kommentare nach NIP-22 und Beiträge mit Community-Bezug, Raum mit Filter nach Community"
```

### Task 4: relilab als Labor: Kriterien, Materialien, Menschen, Mitmachen (Issue 16 `6bc628db`, Spec 4.11)

**Files:** Modify `index.html` (Ansicht `v-relilab`: Abschnitt `data-rlsec="home"` neu aufgebaut, neuer Abschnitt `data-rlsec="mitmachen"`, Navigation der Instanz um „Mitmachen“ ergänzt; Anwendungsskript: `rlLaden()`, `rlHome()`, `rlShow(qs)` kennt `tab=mitmachen`; `RT_RAW`-Kalender der Startseite bleibt; die Instagram-Kacheln und die Attrappen-Suche der rechten Spalte entfallen; CSS `.rl-trias`), Modify `tests/beziehungen.test.ts`, `tests/navigation.test.ts` (Startzeile `v-relilab`), `docs/daten.md`, `docs/konstruktion.md` (Instanz relilab). Branch `pr/relilab-labor` ab `pr/mitmachen`.

**Interfaces:**
- Consumes: `coLaden(RL_HEX)`, `coEintraege`, `eintraegeAufloesen`, `eintragKarte`, `kalLaden`, `terminLogik`, `evToTermin`, `bzProfil`, `profilAus`, `hubFetch`, `pkRender(root, c)`, `datenstand`, `RL_HEX`, `CY`.
- Produces:
  - `const RL_KRITERIEN = ['offen ohne Anmeldung', 'kostenfrei', 'online', 'kurzer Impuls, dann Werkstatt', 'Unfertiges darf vorgestellt werden', 'Ergebnisse unter freier Lizenz', 'bundesland- und religionsübergreifend']` (aus Issue 16).
  - `function rlLaden()` → `Promise<{ antwort, materialien: eintrag[], beitraege: eintrag[], termine: termin[], menschen: profil[] }>`, einmal je Sitzung: `coLaden(RL_HEX)` → `coEintraege` → `eintraegeAufloesen` (Materialien `30142`, Beiträge `30023`); Termine aus `kalLaden()` mit `terminLogik(ev) === 'labor'`, bevorstehend, höchstens 6; Menschen = die Autoren der Materialien und Beiträge mit relilab-Bezug (ohne die Community-Schlüssel), höchstens 40 Schlüssel, Profile aus `bzProfil`, fehlende mit **einer** Abfrage `hubFetch('relilab:menschen', [{ kinds: [0], authors: [<fehlende, höchstens 40>] }])`; nur Profile mit Namen, Bots ausgelassen; wer in der Personen-Liste steht, zuerst.
  - `function rlHome(daten)`: Kopf „relilab · ein Labor“ mit `RL_KRITERIEN` als Pillenreihe und dem Satz „Was hier entsteht, ist unfertig und frei: Praxisentwürfe und Unterrichtsversuche stehen gleichrangig neben Produkten der Institute.“; drei Spalten **Materialien** (neueste 6 über `eintragKarte`, Link „Alle im Katalog ›“ nach `#community?c=relilab&zu=katalog`), **Menschen** (Profilkarten mit Bild oder Initiale, Name, `about`, Link `#person?p=<npub>`, Satz „Wer hier steht, hat im Labor veröffentlicht oder geteilt.“), **Mitmachen** (nächste 6 Labortermine, Link „Alle Labortermine ›“ nach `#finden/fortbildungen?logik=labor`, Knopf „Zum Raum Mitmachen ›“ nach `#relilab?tab=mitmachen`); der bestehende Monatskalender des Nachbaus bleibt unter den Spalten. Stand-Zeile `v-relilab`: `live · <m> Materialien · <p> Menschen · <t> Labortermine` (Startwert `data-stand="stand:…"` auf den Schnappschuss-Stand, gesetzt beim Laden wie bei `v-fortbildungen`); ohne Antwort bleibt der Stand.
  - Abschnitt `data-rlsec="mitmachen"`: `pkRender(root, 'relilab')` im relilab-Rahmen (Community-Filter fest auf relilab, nicht änderbar, Hinweis „Zuschnitt: relilab“).
  - `rlShow(qs)`: `tab=mitmachen` zeigt den Abschnitt; Konsole-Kontext `relilab`: `kooperieren.communities` bleibt, `kooperieren.personen` führt zu `#relilab` mit Scroll auf die Spalte Menschen; `finden.fortbildungen` bleibt bei den Laborterminen.
  - `docs/konstruktion.md`: Absatz „Instanz relilab“ nennt die Trias; `docs/daten.md`: Verbraucher „relilab“.

- [ ] **Step 1: Tests ergänzen**

```ts
Deno.test('relilab als Labor: Kriterien, Trias, Menschen nur mit Profil', () => {
  const k = block(/const RL_KRITERIEN = \[[\s\S]*?\];/);
  assert(k.includes('offen ohne Anmeldung') && k.includes('Ergebnisse unter freier Lizenz') && (k.match(/'/g) || []).length === 14, 'sieben Kriterien');
  const l = fn('rlLaden');
  assert(/coLaden\(RL_HEX\)/.test(l) && /terminLogik\(/.test(l) && /hubFetch\('relilab:menschen', \[\{ kinds: \[0\], authors:/.test(l) && (l.match(/hubFetch\(/g) || []).length === 1 && /\.bot/.test(l), 'Quellen und eine Nachfrage');
  const h = fn('rlHome');
  assert(/Materialien/.test(h) && /Menschen/.test(h) && /Mitmachen/.test(h) && /#person\?p=/.test(h) && /zu=katalog/.test(h) && /logik=labor/.test(h) && /esc\(/.test(h), 'drei Spalten mit Links');
  assert(/data-rlsec="mitmachen"/.test(html) && /pkRender\(/.test(fn('rlShow')), 'Raum im relilab-Rahmen');
  assert(!/Auf Instagram folgen/.test(html) && !/data-todo="Suche"/.test(html), 'Attrappen entfernt');
  assert(/id="v-relilab" data-stand="stand:/.test(html), 'Startwert bleibt ein Stand');
});
```

- [ ] **Step 2: Fehlschlag sehen** · Expected: ein FAIL, 73 PASS.

- [ ] **Step 3: Abschnitte, Funktionen, Navigation der Instanz, CSS, Doku schreiben**; `navigation.test.ts` an den neuen Startwert anpassen, falls die Zusicherung das Datum wörtlich prüft.

- [ ] **Step 4: Tests laufen lassen** · Expected: grün (74).

- [ ] **Step 5: Im Browser prüfen**: `#relilab` zeigt Kriterien, drei Spalten mit echten Inhalten (Stand 09.11.: 16 Materialien, 61 Beiträge, 47 Labortermine), Menschen mit Profilen; `#relilab?tab=mitmachen` zeigt den Raum im relilab-Rahmen; `#relilab?tab=termine` unverändert; offline bleibt der Stand; 375 px: Spalten untereinander.

- [ ] **Step 6: Committen, PR** (`pr/relilab-labor`)

```bash
git add index.html tests/beziehungen.test.ts tests/navigation.test.ts docs/daten.md docs/konstruktion.md && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "relilab als Labor: Kriterien, Trias Materialien, Menschen, Mitmachen aus den Community-Inhalten, Raum Mitmachen im Labor-Zuschnitt"
```

### Task 5: Zuschnitt auf eine Community über `?c=<npub>` und Seite „Eigene Instanz“ (Issue 11 `93b36056`, Spec 4.17)

**Files:** Modify `index.html` (Anwendungsskript: Block „Zuschnitt (ADR-0009)“ mit `HUB_C`, `zuschnittAus(search)`, `zuschnittSetzen(hex)`, `zuschnittName()`; `leseHash`/`go`: Suchparameter `c` bleibt beim Routenwechsel erhalten; Leiste: Markierung „Zuschnitt: <Name> ✕“ über `RelihubLeiste.setItems` (Eintrag `kind: 'zuschnitt'` vor den Instanzen) und Attribut `label`; Konsole: `registerContext` je Kontext bekommt `params: { c }` für `finden.material`, `finden.fortbildungen`, `kooperieren.communities`; Ansichten: `saOpen` (Vorbelegung `c`), `kaOpen` (Filter auf Quelle und `h` der Community), `crOpen` (Standard-Community bei `#community` ohne `c`), `ozSichtbar`, `pkRender`, `peRender` (Schnitt Personen-Liste mit Mitgliedern); neue Ansicht `<div class="view" id="v-eigene-instanz" data-stand="nachbau:Vorschau">` mit `eiOpen(qs)`, `eiRender()`; `kontextprofilAus(f)` bekommt das Feld `c`; `route()`: `eigene-instanz`; CSS `.ei-*`), Create `tests/zuschnitt-anmeldung.test.ts`, Modify `docs/leiste.md`, `docs/navigation.md`, `docs/daten.md`. Branch `pr/zuschnitt` ab `pr/relilab-labor`.

**Interfaces:**
- Consumes: `npubToHex`, `istHex64`, `bech32`, `CO_SCHLUESSEL`, `CY`, `CY_HEX`, `cyLaden`, `bzProfil`, `RelihubLeiste.setItems`, `leisteItems`, `kontextprofilAus`, `shortcodeAus`, `speicher`, `sessionStorage`, `esc`, `sichereUrl`, `datenstand`.
- Produces:
  - `let HUB_C = null` (Hex oder `null`): `function zuschnittAus(search)` → Hex oder `null` aus `new URLSearchParams(search).get('c')` (npub oder 64-Hex, sonst `null`); beim Start aus `location.search`, sonst aus `sessionStorage` `relihub-c`; `function zuschnittSetzen(hex)` schreibt `HUB_C`, `sessionStorage`, den Suchparameter `c` (`history.replaceState`), setzt die Leiste neu und ruft `route()`; `zuschnittSetzen(null)` hebt auf. `function zuschnittName()` → Name aus `bzProfil`, `CO_SCHLUESSEL`, `CY` oder gekürzter npub.
  - Wirkung je Ansicht (jeweils als Vorbelegung, die die Person ändern kann, außer im Ökosystem und im Raum Mitmachen, wo der Zuschnitt den Rahmen setzt): Sammlung `c` = Community mit `CY`-Kennung, falls bekannt; Kalender zeigt Termine der Community (`#h` oder Absender) zuerst und bietet den Chip „nur <Name>“; Katalog öffnet die Community; Personen zeigt von der Personen-Liste nur, wer Mitglied der Community ist (Kante im Gefüge), Satz „Zuschnitt: <Name>“; Ökosystem und Mitmachen filtern wie in Task 2 und 3; Startseite zeigt die Kachel der Community oben und den Satz „Dieser Hub ist auf <Name> zugeschnitten.“ mit Aufheben-Link. Communities ohne `CY`-Kennung (nur Hex) funktionieren über `#community?c=<npub>` (Task 2 `cyAus` liefert `id` = Hex-Präfix; `crOpen` akzeptiert npub und Hex).
  - Leiste: erster Eintrag `{ id: 'zuschnitt', label: 'Zuschnitt: <Name>', short: '<Name>', href: '#eigene-instanz', kind: 'zuschnitt' }` nur bei gesetztem `HUB_C`; das Widget zeigt `kind: 'zuschnitt'` mit Ring-Symbol wie Communities (`docs/leiste.md` nachführen: dritter `kind`). Das Panel „Leiste anpassen“ bekommt den Knopf „Zuschnitt aufheben“.
  - `#eigene-instanz?c=<npub>`: Kopf „Eigene Instanz“ mit Satz „Schneide den Hub auf deine Community zu, prüfe die Vorschau und nimm den Schnipsel mit auf deine Seite.“; Auswahl der Community (`CO_SCHLUESSEL` plus live gefundene aus `cyLaden`, Suchfeld für npub); **Vorschau**: eine zweite `<relihub-steuerkonsole context="vorschau-<hex>">` und `<relihub-leiste>` im Rahmen (`.ei-vorschau`), mit `params` auf die Community; **Schnipsel** (je mit Kopierknopf): (1) der Link `https://hub.rpi-virtuell.net/?c=<npub>#start`, (2) das Kontextprofil `kontextprofilAus({ c, … })` als JSON mit Satz „für die Steuerkonsole als eigenständiges Skript (`config-src`); das Skript folgt“, (3) der WordPress-Shortcode `shortcodeAus({ c })` mit Satz zu den Plugins amb-nostr, longform-nostr, nostr-calendar, (4) der Hinweis auf den White-Label-Betrieb der edufeed-App („Umgebungsvariablen, siehe edufeed-Dokumentation“, Link `https://git.edufeed.org/edufeed/edufeed-app`); **Vereinbarung**: Kachel „Kooperationsvereinbarung“ mit Link `#oercommunity/kooperationsvereinbarung` (Seite vom Schaufenster-Schlüssel, bis dahin „in Vorbereitung“ über `spielregelLink`-Muster) und Kachel „Technische Bedarfe“ mit Link `#oercommunity/bedarfe-technik` (ebenso); Stand-Zeile `Nachbau · Vorschau` (die Seite zeigt keine Relay-Daten außer den Namen).
  - `docs/navigation.md`: Zeile „Eigene Instanz | – | – (Leiste: Zuschnitt) | `#eigene-instanz` | Zuschnitt | kooperieren | gebaut“; `docs/daten.md`: Abschnitt „Zuschnitt“ (Quelle des `c`, Wirkung je Ansicht als Tabelle).

- [ ] **Step 1: Tests schreiben** (`tests/zuschnitt-anmeldung.test.ts`, Kopf wie `tests/sammlung.test.ts`)

```ts
Deno.test('zuschnittAus: npub, Hex, Unsinn', () => {
  const za = bau('zuschnittAus', fn('npubToHex'));
  assertEquals(za('?c=npub14esenw6rt4c2pmxwvyey4jqw0sjdahetq6qvh5lffxp7w4thg63ql480z2'), 'ae6199bb435d70a0ecce61324ac80e7c24dedf2b0680cbd3e94983e7557746a2');
  assertEquals(za('?c=' + 'ab'.repeat(32)), 'ab'.repeat(32)); assertEquals(za('?c=kaputt'), null); assertEquals(za(''), null);
});

Deno.test('Zuschnitt: Leiste, Ansichten, eigene Instanz', () => {
  assert(/let HUB_C = null/.test(s) && /function zuschnittSetzen\(hex\)/.test(s) && /relihub-c/.test(fn('zuschnittSetzen')), 'Zustand und Speicher');
  assert(/kind: 'zuschnitt'/.test(fn('leisteItems')) && /Zuschnitt aufheben/.test(html), 'Leiste');
  for (const f of ['saOpen', 'kaOpen', 'crOpen', 'peRender', 'pkRender']) assert(/HUB_C/.test(fn(f)), f + ' kennt den Zuschnitt');
  assert(/id="v-eigene-instanz" data-stand="nachbau:/.test(html) && /'eigene-instanz'/.test(block(/function route\(\)[\s\S]*?window\.scrollTo/)), 'Ansicht und Route');
  const e = fn('eiRender');
  assert(/kontextprofilAus\(/.test(e) && /shortcodeAus\(/.test(e) && /config-src/.test(e) && /\?c=/.test(e) && /kooperationsvereinbarung/.test(e) && /bedarfe-technik/.test(e) && /relihub-steuerkonsole/.test(e) && /relihub-leiste/.test(e), 'Vorschau und Schnipsel');
  assert(/"c"/.test(fn('kontextprofilAus')) || /c:/.test(fn('kontextprofilAus')), 'Kontextprofil trägt den Zuschnitt');
  const d = Deno.readTextFileSync(new URL('../docs/leiste.md', import.meta.url));
  assert(/zuschnitt/.test(d), 'docs/leiste.md');
});
```

- [ ] **Step 2: Fehlschlag sehen** · Expected: zwei FAIL in `zuschnitt-anmeldung.test.ts`, 74 PASS.

- [ ] **Step 3: Block, Leiste, Konsolen-Parameter, Wirkung je Ansicht, Seite „Eigene Instanz“ mit Vorschau und Schnipseln, CSS, Doku schreiben.** Die Vorschau-Konsole registriert ihren Kontext mit `RelihubSteuerkonsole.registerContext('vorschau-' + hex, { actions: { 'finden.material': { params: { c } }, … }, handler: d => standardAktion(d, 'Vorschau') })`.

- [ ] **Step 4: Tests laufen lassen** · Expected: grün (76).

- [ ] **Step 5: Im Browser prüfen**: `/?c=npub12atlg…#start` (reliGlobal) zeigt die Markierung in der Leiste, `#finden/sammlung` vorbelegt, `#finden/fortbildungen` mit Chip, `#oekosystem` nur Verbundenes, `#kooperieren/personen` mit Satz; Aufheben entfernt alles; `#eigene-instanz?c=…` zeigt Vorschau und vier Schnipsel, Kopieren meldet per Toast; nach Neuladen bleibt der Zuschnitt (sessionStorage); 375 px: Vorschau untereinander.

- [ ] **Step 6: Committen, PR** (`pr/zuschnitt`)

```bash
git add index.html tests/zuschnitt-anmeldung.test.ts docs/leiste.md docs/navigation.md docs/daten.md && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "Zuschnitt auf eine Community über ?c=<npub> in Leiste, Konsole und allen Ansichten; Seite Eigene Instanz mit Vorschau, Link, Kontextprofil, Shortcode, Vereinbarung"
```

### Task 6: Anmeldung per NIP-07 und Aktionen: Folgen, Beitreten, Zusagen, Gefällt mir, Sammlung speichern (Stufe B der Issues 01 `b68eaaa5`, 06 `693c69cc`, 14 `bfa727b9`; Spec 4.5 B, 4.10 B, 4.19)

**Files:** Modify `index.html` (Block „Anmeldung (NIP-07, ADR-0009)“: `ICH`, `anmelden()`, `nurAnsehen(npub)`, `abmelden()`, `hubSenden(ev)`, `signierenUndSenden(vorlage, erfolg)`, `listeErgaenzen(alt, kind, d, tag)`, `sammlungListe(f, eintraege)`, `aktion(was, ziel)`; Dialog `#anmelden` (Knopf „Mit Schlüssel anmelden“, Erklärung NIP-07, Feld „nur ansehen“ mit npub, Link „Konto bei edufeed anlegen“); Kopfzeilen: „Anmelden“/„Mein Profil“ führen zum Dialog beziehungsweise `#profil`; `#profil` zeigt bei angemeldeter Person `prRender(ICH.hex)` mit Zusatz „Das bist du“, eigene Communities (Kanten), eigene Veröffentlichungen, sonst die Persona mit dem Satz aus Etappe 4; Aktionsknöpfe: Personen-Karten und `#person` „Folgen“, Community-Raum „Beitreten“, Termine im Kalender und in der Auswahlzeile des Ökosystems „Zusagen“/„Vielleicht“, Material-Detail und Ökosystem „Gefällt mir“, Sammlung „Als Nostr-Liste speichern“, Material-Detail „Zur eigenen Sammlung“ (statt Toast); `LOGGED` wird aus `ICH.hex` abgeleitet; CSS `.an-*`), Modify `tests/zuschnitt-anmeldung.test.ts`, `tests/inhalte.test.ts` (Zusicherung zu `lizenzAktionen`: Aktion 3 bei `offen` geht, bei Anmeldung sendet sie, sonst Hinweis), `docs/daten.md`, `docs/navigation.md` (Zeilen Profil, Anmelden). Branch `pr/anmeldung` ab `pr/zuschnitt`.

**Interfaces:**
- Consumes: `window.nostr` (NIP-07: `getPublicKey()`, `signEvent(ev)`), `RELAYS`, `hubFetch`, `istHex64`, `npubToHex`, `bech32`, `prRender`, `peLaden`, `bzBauen`/`ozGefuege`, `kurzHash`, `sammlungFilter`, `saF` (der aktuelle Filter) und die Trefferliste, die `saRender` berechnet (dafür in `let saTreffer = []` gehalten), `lizenzAktionen`, `toast`, `esc`, `datenstand`, `speicher`.
- Produces:
  - `const ICH = { hex: null, kann: false }` (`kann` = Signer vorhanden); `function anmelden()` → `Promise<void>`: ohne `window.nostr` Toast „Keine Nostr-Erweiterung gefunden (zum Beispiel nos2x oder Alby). Alternativ: nur ansehen mit npub.“; sonst `getPublicKey()`, `istHex64` prüfen, `ICH` setzen, `sessionStorage` `relihub-ich` (Hex und `kann`), Profil über `peLaden`/`hubFetch('ich:' + hex, [{ kinds: [0], authors: [hex], limit: 1 }, { kinds: [30000], authors: [hex], '#d': ['communities'], limit: 1 }, { kinds: [3], authors: [hex], limit: 1 }])` laden, Dialog schließen, `route()`; `function nurAnsehen(npub)`: wie oben mit `kann = false`; `function abmelden()`: `ICH` leeren, Speicher löschen, `route()`.
  - `function hubSenden(ev)` → `Promise<number>`: sendet `['EVENT', ev]` an alle drei `RELAYS`, wertet `['OK', id, true|false, grund]` aus, 8 s je Relay, liefert die Zahl der Relays, die angenommen haben; schließt jede Verbindung.
  - `function signierenUndSenden(vorlage, erfolg)` → `Promise<boolean>`: nur mit `ICH.kann` und `window.nostr`, sonst Toast „Zum Mitmachen bitte mit Schlüssel anmelden.“; `signEvent({ created_at: jetzt, content: '', …vorlage, pubkey: ICH.hex })`; bei 0 Relays Toast „Kein Relay hat das Ereignis angenommen.“; sonst Toast „<erfolg> (angenommen von <n> Relays)“ und das Event in die lokalen Quellen aufnehmen (`pkLive`), Gefüge neu bauen, Ansicht neu zeichnen; Abbruch → Toast „Signieren abgebrochen.“.
  - `function listeErgaenzen(alt, kind, d, tag)` → unsigniertes Event (rein): aus dem bisherigen Listen-Event `alt` (oder `null`) ein neues mit allen bisherigen Tags außer `d`, dem `d`-Tag (für `kind:3` keiner) und dem neuen `tag`, wenn er nicht schon enthalten ist; `content` bleibt; liefert `null`, wenn der Tag schon enthalten ist. Vor jedem Aufruf holt `aktion` die Liste frisch (`hubFetch` mit `authors: [ICH.hex]` und dem Kind, Zwischenspeicher umgangen über einen Namen mit Zeitstempel).
  - `function sammlungListe(f, eintraege)` → unsigniertes `kind:30004`: `d` = `'sammlung-' + kurzHash(JSON.stringify(f))`, `title` = „Sammlung: <Fach/Stufe/Lizenz/Begriffe, kurz>“, `description` aus dem Filter, `a`-Tags `30142:<pk>:<d>` der ersten 100 Treffer, Tag `['client', 'reli_hub']` entfällt (Hub nicht nennen: `['client', 'hub']`).
  - `function aktion(was, ziel)`: `folgen` (`kind:3`, `p`-Tag; frisch holen, `listeErgaenzen`, senden; Erfolg „Du folgst jetzt <Name>.“), `beitreten` (`kind:30000 d=communities`, `p`-Tag der Community; ohne bestehende Liste Rückfrage per `confirm`; Erfolg „<Name> beigetreten.“), `zusagen`/`vielleicht` (`kind:31925` mit `d` = `'rsvp-' + <Adresse>`, `a`, `e`, `p`, `status`), `gefaellt` (`kind:7`, `content: '+'`, `a`, `e`, `p`, `k`), `sammlungSpeichern` (`sammlungListe(saF, saTreffer)`), `zurSammlung` (`kind:30004 d=sammlung` der Person, `a`-Tag des Materials über `listeErgaenzen`). Ohne Anmeldung bleiben alle Knöpfe sichtbar, deaktiviert und mit dem Hinweis „braucht Anmeldung mit Schlüssel“; mit „nur ansehen“ ebenso. Schon Vorhandenes (Folge, Mitgliedschaft, Zusage) zeigt der Knopf als Zustand („Folgst du“, „Mitglied“, „Zugesagt“) und sendet nicht erneut.
  - `#profil` angemeldet: Kopf mit Profil (`prRender`-Bausteine), Abschnitte „Meine Communities“ (Kanten aus dem Gefüge, Link je Community), „Meine Veröffentlichungen“, „Meine Sammlungen“ (eigene `kind:30004` mit `d` `sammlung…`, eine Abfrage `authors: [ICH.hex]`), Knopf „Abmelden“; Stand-Zeile `live · angemeldet` oder `live · nur ansehen`. Nicht angemeldet: die Persona bleibt mit `Nachbau · Persona Luca Beispiel` und dem Satz aus Etappe 4 plus Knopf „Anmelden“.
  - `docs/navigation.md`: Zeilen „Profil | Mein Profil | `hub.profil` | `#profil` (angemeldet: eigenes Profil) | …“ und „Anmelden | Kopfzeile | – | Dialog `#anmelden` | – | reli_hub | gebaut“.

- [ ] **Step 1: Tests ergänzen**

```ts
Deno.test('listeErgaenzen: ergänzt, ersetzt nie, doppelt ergibt null', () => {
  const le = bau('listeErgaenzen');
  const alt = { kind: 30000, content: 'x', tags: [['d', 'communities'], ['p', 'aa'.repeat(32)], ['client', 'Edufeed']] };
  const neu = le(alt, 30000, 'communities', ['p', 'bb'.repeat(32)]);
  assertEquals(neu.kind, 30000); assertEquals(neu.content, 'x');
  assertEquals(neu.tags, [['d', 'communities'], ['p', 'aa'.repeat(32)], ['client', 'Edufeed'], ['p', 'bb'.repeat(32)]], 'alte Tags bleiben, d einmal, neuer Tag hinten');
  assertEquals(le(alt, 30000, 'communities', ['p', 'aa'.repeat(32)]), null, 'schon enthalten');
  const k3 = le(null, 3, null, ['p', 'cc'.repeat(32)]);
  assertEquals(k3.tags, [['p', 'cc'.repeat(32)]]); assert(!k3.tags.some((t: string[]) => t[0] === 'd'), 'kind 3 ohne d');
});

Deno.test('sammlungListe: d aus Filter, höchstens 100 Einträge, kein Hub-Name', () => {
  const sl = bau('sammlungListe', fn('kurzHash'));
  const f = { c: 'religlobal', fach: ['Ethik'], stufe: [], lizenz: 'offen', q: ['Frieden'] };
  const e = Array.from({ length: 120 }, (_, i) => ({ adr: `30142:${'ab'.repeat(32)}:m${i}`, kind: 30142 }));
  const ev = sl(f, e);
  assertEquals(ev.kind, 30004); assert(/^sammlung-[0-9a-f]{8}$/.test(ev.tags.find((t: string[]) => t[0] === 'd')[1]));
  assertEquals(ev.tags.filter((t: string[]) => t[0] === 'a').length, 100); assert(!JSON.stringify(ev).includes('reli_hub'));
  assertEquals(sl(f, e).tags.find((t: string[]) => t[0] === 'd')[1], ev.tags.find((t: string[]) => t[0] === 'd')[1], 'deterministisch');
});

Deno.test('Aktionen: nur mit Signer, frisch holen, Relays zählen, kein nsec', () => {
  assert(/const ICH = \{ hex: null, kann: false \}/.test(s) && /window\.nostr/.test(fn('anmelden')) && !/nsec/.test(s.replace(/nsec1…|kein nsec|nie nach einem nsec/g, '')), 'NIP-07, kein nsec im Skript');
  const a = fn('aktion');
  assert(/listeErgaenzen\(/.test(a) && /authors: \[ICH\.hex\]/.test(a) && /kinds: \[3\]/.test(a) && /kinds: \[30000\]/.test(a) && /kind: 31925/.test(a) && /kind: 7/.test(a) && /sammlungListe\(/.test(a), 'alle Aktionen über Listen-Ergänzung und Vorlagen');
  const su = fn('signierenUndSenden');
  assert(/ICH\.kann/.test(su) && /Signieren abgebrochen/.test(su) && /Kein Relay hat/.test(su) && /angenommen von/.test(su), 'Zustände');
  assert(/function hubSenden\(ev\)/.test(s) && /'OK'/.test(fn('hubSenden')) && /RELAYS/.test(fn('hubSenden')), 'Senden an die drei Relays mit OK');
  assert(/braucht Anmeldung mit Schlüssel/.test(s) && /id="anmelden"/.test(html), 'Hinweis und Dialog');
  assert(/Das bist du/.test(block(/if \(v === 'profil'\)[\s\S]*?\n    \}/) + s), 'eigenes Profil');
});
```

- [ ] **Step 2: Fehlschlag sehen** · Expected: drei FAIL, 76 PASS.

- [ ] **Step 3: Block, Dialog, Kopfzeilen, Aktionsknöpfe an den vier Stellen, `#profil` angemeldet, `lizenzAktionen`-Aktion 3, CSS, Doku schreiben**; `docs/daten.md`: Abschnitt „Anmeldung und Schreiben“ (NIP-07, nie `nsec`, Sendeweg, Listen-Regel, Zustände je Aktion).

- [ ] **Step 4: Tests laufen lassen** · Expected: grün (79).

- [ ] **Step 5: Im Browser prüfen** (mit NIP-07-Erweiterung, sonst „nur ansehen“ und das im Bericht sagen): Anmelden zeigt das eigene Profil mit Communities; Beitreten bei einer Community, der man noch nicht angehört, fragt bei fehlender Liste nach und meldet die Relays; Gefällt mir an einem Material erscheint im Protokoll; Zusagen an einem Termin; Sammlung speichern erzeugt eine Liste, die unter „Meine Sammlungen“ erscheint; ohne Anmeldung bleiben die Knöpfe deaktiviert mit Hinweis; Netzwerk: je Aktion drei Verbindungen zum Senden, davor eine zum frischen Holen.

- [ ] **Step 6: Committen, PR** (`pr/anmeldung`)

```bash
git add index.html tests/zuschnitt-anmeldung.test.ts tests/inhalte.test.ts docs/daten.md docs/navigation.md && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "Anmeldung per NIP-07 oder nur ansehen; Folgen, Beitreten, Zusagen, Gefällt mir und Sammlung als Liste über einen Sendeweg mit frisch geholten Listen; eigenes Profil statt Persona"
```

### Task 7: ADR-0009 „Beziehungsgefüge, Mitmachen, Zuschnitt, Anmeldung“ und Doku der Etappe

**Files:** Create `docs/adr/0009-beziehungsgefuege-mitmachen-anmeldung.md`, Modify `docs/adr/README.md` (Tabelle), `README.md` (ADR-Tabelle, Ansichten: Ökosystem, Mitmachen, Eigene Instanz, Anmeldung; Absatz „Daten“), `docs/konstruktion.md` (Abschnitt „Beziehungsgefüge, Mitmachen, Zuschnitt, Anmeldung (Etappe 5a)“ nach „Community-Inhalte und Listen (Etappe 4)“; Tabelle „Offene Stellen“: Zeilen „Anmeldung“, „Folgen“, „Abonnieren als Nostr-Liste“, „config-src“ streichen beziehungsweise auf den neuen Stand setzen; neue Zeilen „Schreiben von Kommentaren im Hub“ (Stufe C), „Konsole als eigenständiges Skript“ (Plan 5b)), `tests/zuschnitt-anmeldung.test.ts`. Branch `pr/doku-etappe-5a` ab `pr/anmeldung`.

**Interfaces:**
- Consumes: Entscheidungen der Tasks 1 bis 6; `docs/community-hub.html` als genanntes Vorbild.
- Produces: ADR-0009 nach der Vorlage (Status: angenommen · <Datum> · Entscheidung der Maintainer · Bezug: Issues `e6875f0b…`, `93b36056…`, `bfa727b9…`, `6bc628db…`, Stufe B von `b68eaaa5…` und `693c69cc…` (gitworkshop); Vorbild: der Nachbau des Figma-Entwurfs im FOERBICO-Repo, 08.11.2026), Entscheidung in sechs Punkten: (1) Das Ökosystem ist ein Beziehungsgefüge aus den Events selbst (Kantenregeln als Liste), gelesen mit einer Abfrage für Mitgliedschaften, Communities, Zusagen und Reaktionen, die übrigen Reihen aus den Caches; Personen nur mit Profil und Kante; ohne Rollenprüfung; (2) Communities live aus `kind:10222` und `kind:0`, Partner ohne Schlüssel als Kacheln; (3) das Aktivitätsprotokoll hält eine dauerhafte Subscription je Relay (die einzige im Hub), Kommentare und Beiträge werden gelesen, nicht geschrieben (Schreiben in der edufeed-App; im Hub Stufe C); (4) der Zuschnitt auf eine Community kommt aus `?c=<npub>` und wirkt als Datenfilter auf alle Ansichten, Leiste und Konsole; das JSON-Kontextprofil bleibt als Export für fremde Seiten; (5) die Anmeldung läuft nur über NIP-07 oder „nur ansehen“; der Hub kennt keinen `nsec`; jede Aktion ist ein eigener Klick, Listen werden frisch geholt und ergänzt; (6) das relilab zeigt die Trias aus den Community-Inhalten; Menschen sind, wer dort veröffentlicht oder geteilt hat. Verworfen: das Gefüge aus einer globalen Abfrage bauen (Fremdverkehr, Relay-Grenze); fremde Relays für Profile (`purplepag.es` im Nachbau: Drei-Relay-Regel); NIP-46-Bunker im Hub (Schlüsselhaltung im Browser-Tab); Kommentare im Hub schreiben (die App hat den Editor, der Hub die Übersicht); den Nachbau als zweite Seite betreiben (ein Hub, ein Gefüge). Folgen: Plan 5b baut Klickweg und Erschließungs-Layer auf das Gefüge und den Zuschnitt; die Konsole als eigenständiges Skript liest denselben `?c=`-Zuschnitt.

- [ ] **Step 1: Test ergänzen**

```ts
Deno.test('ADR-0009 und README nennen die Etappe', async () => {
  const adr = await Deno.readTextFile(new URL('../docs/adr/0009-beziehungsgefuege-mitmachen-anmeldung.md', import.meta.url));
  assert(/^# ADR-0009/.test(adr) && /## Status/.test(adr) && /## Entscheidung/.test(adr) && /e6875f0b/.test(adr) && /bfa727b9/.test(adr) && /NIP-07/.test(adr) && /\?c=/.test(adr) && /ohne Rollenprüfung|Mitgliederrollen/.test(adr) && /purplepag/.test(adr));
  assert(!/Arbeitspaket|Meilenstein|Förderkennzeichen|Projektträger|Zwischenbericht/.test(adr), 'Projektsprache');
  const r = await Deno.readTextFile(new URL('../README.md', import.meta.url));
  assert(/0009-beziehungsgefuege-mitmachen-anmeldung/.test(r) && /Ökosystem/.test(r) && /Mitmachen/.test(r) && /Anmeldung|anmelden/.test(r), 'README');
});
```

- [ ] **Step 2: Fehlschlag sehen** · Expected: ein FAIL, 79 PASS.
- [ ] **Step 3: ADR, README, Konstruktionsbeschreibung, ADR-Tabelle schreiben** (prüfen: `python3 -I ~/repositories/FOERBICO_und_rpi-virtuell/tools/nachweis/check.py gitworkshop docs`: nur „kopf“-Zeilen).
- [ ] **Step 4: Tests laufen lassen** · Expected: grün (80).
- [ ] **Step 5: Committen, PR** (`pr/doku-etappe-5a`)

```bash
git add docs/adr/0009-beziehungsgefuege-mitmachen-anmeldung.md docs/adr/README.md README.md docs/konstruktion.md tests/zuschnitt-anmeldung.test.ts && git commit --author="Poutník <poutnik@users.noreply.edufeed.org>" -m "ADR-0009: Beziehungsgefüge, Mitmachen, Zuschnitt, Anmeldung; README und Konstruktion nachgeführt"
```

### Task 8: Inhaltsstrang 5a: Kooperationsvereinbarung, technische Bedarfe, Partnerentscheidung (Spec 4.17, 4.7, 5a; nur Dateien im FOERBICO-Repo)

**Files (FOERBICO-Repo, keine Commits, kein Branchwechsel):** Create `Website/content/de/kooperationsvereinbarung/index.md` und `Website/content/de/bedarfe-technik/index.md` (Seitenformat wie `Website/content/de/qualitaet/index.md`, `creativeWorkStatus: Draft`, `url` = `kooperationsvereinbarung` beziehungsweise `bedarfe-technik`, das sind die `d`-Namen aus Task 5), Create `Hub-Entwicklung/2026-11-09-partner-ohne-schluessel.md` (Entscheidungsvorlage zu 4.7).

**Interfaces:**
- Consumes: Spec 4.17 (Vereinbarung technisch und als Arbeitsbündnis; Bedarfserhebung aus den Fäden auf gitworkshop, den Rückmeldungen der Zwischenfazit-Tagung und Beobachtungen), 4.7 (Partner: rpp-katholisch, Konfessionskundliches Institut, relimentar und die Einträge ohne Schlüssel in `CY`), `Hub-Entwicklung/communities-schluessel.md` Fragen 5 und 6, die Issues 11 und 07, ADR-0009.
- Produces:
  - Seite „Kooperationsvereinbarung“ (500 bis 900 Wörter): ein Satz, worum es geht; Teil A technisch (welche Daten hinein: Material, Termine, Beiträge mit `h`-Tag oder Repost; welche hinaus: Schnipsel, Shortcode, Zuschnitt-Link; Relay, Schlüsselhaltung, Entfernen); Teil B Arbeitsbündnis (Ansprechpersonen als Rollen, Kanäle, Mitverantwortung für Inhalte und Moderation, Dauer, Ausstieg); Checkliste „Bevor eine Instanz startet“; Lizenzzeile CC BY 4.0. Keine Namen von Personen, Rollen statt Vornamen, keine Projektsprache.
  - Seite „Technische Bedarfe“ (400 bis 700 Wörter): was Communities gebraucht haben (aus den Fäden auf gitworkshop, dem Konsens vom 03.11. und der Hub-Erkundung; ohne Personennamen), was der Hub darauf antwortet (Leiste als Widget, Zuschnitt, Plugins, White-Label), was offen bleibt; Verweis auf die Konsultation als mögliche Ergänzung im Januar.
  - `Hub-Entwicklung/2026-11-09-partner-ohne-schluessel.md`: Tabelle der `CY`-Einträge ohne Schlüssel (relimentar, narrt, Münchner Reli Room, relilab NRW, #relilab Impulse, relilab|BRU, relilab|Junior, relilab|interreligiös, Makerspace, relilab.Schulseelsorge, CampusCom hat einen Schlüssel) und der Partner aus 4.7 mit je zwei Optionen (Schlüssel anlegen und von wem gehalten; Partnerkachel mit Link) und einer Empfehlung; Entscheidung ist Jörgs Gate und fließt als Liste in `PARTNERS` (Task 2) beziehungsweise in neue Community-Schlüssel ein.

- [ ] **Step 1: Drei Dateien schreiben.**
- [ ] **Step 2: Prüfen** · Run: `cd ~/repositories/FOERBICO_und_rpi-virtuell && mkdir -p /tmp/claude-501/e5a && cp Website/content/de/kooperationsvereinbarung/index.md /tmp/claude-501/e5a/kooperationsvereinbarung.md && cp Website/content/de/bedarfe-technik/index.md /tmp/claude-501/e5a/bedarfe-technik.md && cp Hub-Entwicklung/2026-11-09-partner-ohne-schluessel.md /tmp/claude-501/e5a/ && python3 -I tools/nachweis/check.py gitworkshop /tmp/claude-501/e5a; python3 -I tools/nachweis/check.py erschliessung /tmp/claude-501/e5a` · Expected: Namensprüfung „ohne Befund“; die gitworkshop-Prüfung meldet nur „kopf: TITEL/ZIEL fehlt“, keine Projektsprache.
- [ ] **Step 3: Gate**: Jörg liest gegen, entscheidet die Partnerliste, committet die Seiten auf einen Branch und mergt; die Pipeline veröffentlicht; `#eigene-instanz` zeigt die Kacheln dann als „Lesen ›“ statt „in Vorbereitung“ ohne Codeänderung.

### Task 9: Abschluss der Etappe (vorbereitet, Veröffentlichung nur durch Jörg)

**Files:** `~/.config/poutnik/protokolle/issue-kommentare-2026-12-07b/`: `00-uebersicht.md` und Kommentar-Entwürfe `07-kommentar-oekosystem.md`, `11-kommentar-eigene-instanz.md`, `14-kommentar-mitmachen.md`, `16-kommentar-relilab.md`, `01b-kommentar-sammlung-liste.md` (Stufe B zu Issue 01), `06b-kommentar-personen-folgen.md` (Stufe B zu Issue 06) (Form wie Runde 7: `ZIEL:`/`ID:` in voller Länge, Leerzeile, Text „Umgesetzt in PR {{pr:<branch>}} (main {{main}}): <Entscheidung in einem Satz>. Ausprobieren: https://hub.rpi-virtuell.net/#<route>. Offen bleibt: <ein Satz>.“; der Ökosystem-Kommentar nennt den Nachbau im FOERBICO-Repo als Vorbild und verlinkt ihn über GitHub Pages). FOERBICO-Repo: `Hub-Entwicklung/2026-12-07-etappe-5a-uebergabe.md` (Branch-Stapel mit SHAs, Merge-Ablauf, Gates, Hashes, Schranken: Partnerentscheidung, Seiten des Inhaltsstrangs, NIP-07-Erweiterung für Vorführungen, Lesefreigabe), Spec-Fahrplan fünfte Zeile „bis 23.12.“ um „Teil 5a erledigt am <Datum>: …“ ergänzen, Kommentare auf den Nachweis-Issues (Nummern in `Orga/nachweis-hub/ergebnis.json`: `01-ap-3-2-3-3` → #879 für 4.1, `06-ap-4-7` → #884 für 4.7, `10-ap-9-1` → #888 für 4.17, `11-ap-9-2` → #889 für 4.11, `15-ap-3` → #893 für 4.19, `04-ap-4-5` → #882 und `13-ap-9-5` → #891 für die Stufe B) über `forgejo-api comment` (eigener Aufruf), Commit der Dateien.

- [ ] **Step 1: Entwürfe schreiben und prüfen** · Run: `python3 -I tools/nachweis/check.py gitworkshop ~/.config/poutnik/protokolle/issue-kommentare-2026-12-07b` · Expected: Exit 0.
- [ ] **Step 2: Gate**: Jörg pusht die PRs, mergt, pusht `main`, setzt `{{pr:…}}` und `{{main}}`, liest die Kommentare, gibt frei.
- [ ] **Step 3: Veröffentlichen** (nach Freigabe) · Run: je Datei `zsh tools/poutnik/skripte/pub-comment.sh <datei>` in der Reihenfolge 07, 14, 16, 11, 01b, 06b; `cd tools/poutnik && deno task threads --repo reli-hub --since 1` · Expected: sechs Kommentare von Poutník mit heutigem Datum.
- [ ] **Step 4: Buchführung** · Spec-Fahrplan, Forgejo-Kommentare, Commit und Push im FOERBICO-Repo wie am 05.11.; Prüfung `python3 -I tools/nachweis/check.py erschliessung <ordner mit den neuen Dateien>` · Expected: ohne Befund.
- [ ] **Step 5: Schnappschuss**: Nach dem Merge einmal `deno task schnappschuss` auf einem frischen Branch (je Gruppe, Hinweis bei Grenze), damit der Rückfall den Stand der Tagung trägt.

## Selbstprüfung gegen die Spec

- 4.1 Netzwerk sichtbar: Communities-Liste live (Task 2, Stufe A), Karte der Verbindungen als Explorer mit Kanten aus Mitgliedschaft, Teilen, Zusagen, Reaktionen (Tasks 1, 2, Stufe B); Folgen als Kante fehlt bewusst (kind:3 der Personen wird nicht global gelesen; eigene Folgen nach Anmeldung in Task 6). Gedeckt, Lücke benannt.
- 4.7 Weitere Communities: Liste live mit Status (Mitglied/folge ich erst nach Anmeldung, Task 6), Partner ohne Schlüssel als Kacheln (Task 2), Entscheidung über Schlüssel (Task 8, Gate). Gedeckt.
- 4.11 Kerndienste: relilab als Labor mit Trias (Task 4); rpi-virtuell war Etappe 2; relidesk bleibt Nachbau (Stufe C). Gedeckt für Stufe A.
- 4.17 Technische Bedarfe: Zuschnitt und Seite „Eigene Instanz“ mit Vorschau, Schnipseln, White-Label- und Plugin-Hinweis (Task 5), Vereinbarung und Bedarfsseite (Task 8), Leiste als Widget aus Etappe 2; die Konsole als eigenständiges Skript bleibt Plan 5b. Gedeckt.
- 4.19 Öffentlicher Raum: Lesen und Filtern von Kommentaren und Beiträgen, Protokoll live, relilab-Zuschnitt (Tasks 3, 4), Schreiben in der App, Reaktionen und Zusagen im Hub (Task 6). Gedeckt für Stufe B.
- 4.5 B Abonnieren als Nostr-Liste und 4.10 B Folgen: Task 6. Gedeckt.
- 5a Inhaltsstrang: Kooperationsvereinbarung, Bedarfe (Task 8). Gedeckt.
- 7: sechs Kommentare (Task 9); neues ADR (Task 7). Gedeckt.
- 8: Fahrplanzeile „bis 23.12.“ Teil 5a (Task 9); Plan 5b trägt 4.4, 4.8, 4.16, 4.18 und Abschnitt 5.
