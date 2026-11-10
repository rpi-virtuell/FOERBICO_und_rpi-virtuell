# Übergabe Hub-Netzwerk und Mitmachen (Etappe 5a): Branch-Stapel, Merge-Ablauf, offene Schritte

Stand 10.11.2026: Die acht Branches sind lokal fertig (90 Tests grün); der achte, `pr/nacharbeit-etappe-5a`, trägt die Fix-Welle der Gesamt-Review. PRs am 10.11.2026 als Poutník auf gitworkshop (je 4 bis 5 von 7 Relays). Noch nichts gemergt oder kommentiert; die PR-Spalte bleibt „–“, bis Jörg die Branches als Poutník gepusht hat. Jeder Branch sitzt auf dem Kopf des vorigen, ein PR zeigt nach dem Merge der Vorgänger nur seinen eigenen Diff. Basis ist `main` `2ea71041`. Zahl = Issue der Kommentarentwürfe.

## 1. Branch-Stapel in Reihenfolge

| Nr. | Branch | Kopf-Commit | Was er tut | Issue | PR |
|---|---|---|---|---|---|
| 1 | `pr/beziehungen` | `ea512e0e` | Beziehungsgefüge: Entitäten und Kanten aus Autorschaft, Communities, Reposts, Mitgliedschaften, Zusagen und Reaktionen; eine Abfrage dafür | 07 | [PR](https://gitworkshop.dev/nevent1qqsp0l8ps3mttjtw4u6ekdndsujacw33yyqg3px8gce8pwgmx5du62cpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mhnk3332) |
| 2 | `pr/oekosystem` | `b2019edf` | Ökosystem: Explorer mit vier Reihen, Communities live vom Relay, Partnerkacheln, Profilabfrage | 07 | [PR](https://gitworkshop.dev/nevent1qqszwzx0c7lt0c3wgp5gp4sses3rsjnnr62vd05r5fl7e3n7pgrjtgqpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mhpjv59r) |
| 3 | `pr/mitmachen` | `7bddf110` | Mitmachen: Aktivitätsprotokoll als Subscription je Relay, Kommentare nach NIP-22, Beiträge, Filter nach Community | 14 | [PR](https://gitworkshop.dev/nevent1qqs84z2xa3uqyh0me8w72dej6437l3zw0ysqyeht8khea40377ak7rgpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mhnswpnr) |
| 4 | `pr/relilab-labor` | `a4389765` | relilab als Labor: Kriterien, Trias Materialien, Menschen, Mitmachen | 16 | [PR](https://gitworkshop.dev/nevent1qqsp8zf27lfmex76yhyhknm4l0cph44w9qwf89eqr0jvemjfd8wa4xspz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mhwa8ptq) |
| 5 | `pr/zuschnitt` | `01f159e8` | Zuschnitt auf eine Community über `?c=<npub>`, Seite „Eigene Instanz“ mit Vorschau, Link, Kontextprofil, Shortcode | 11 | [PR](https://gitworkshop.dev/nevent1qqsp2fdjtddzdnhegazkpzcy4gqvjv3swgce87n6rfq60dmuptvvj4cpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mhp6aph0) |
| 6 | `pr/anmeldung` | `556cbe33` | Anmeldung per NIP-07 oder „nur ansehen“; Folgen, Beitreten, Zusagen, Gefällt mir, Sammlung als Liste über einen Sendeweg | 01b, 06b | [PR](https://gitworkshop.dev/nevent1qqsgp3frj2a8nfg798vymr3wh7qgw2n4mhqu5nwgmqvqffauyyd9lrspz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mhhlyzkd) |
| 7 | `pr/doku-etappe-5a` | `82949834` | ADR-0009, README und Konstruktionsbeschreibung nachgeführt | – | [PR](https://gitworkshop.dev/nevent1qqsv7n3qzv5n34pqrldfty9lj7y7wm87qzyk8kdqaeyasfgu9lmh7cgpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mhdhu8xa) |
| 8 | `pr/nacharbeit-etappe-5a` | `041a147b` (sieben Commits ab `82949834`) | Fix-Welle der Gesamt-Review (siehe Abschnitt 4) | alle | [PR](https://gitworkshop.dev/nevent1qqsyytllqe8ea5dkfv5guz7dz5m4skgh738jljuctjf5k73a9hmj05gpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzq65s4hd8mffcn98wgdwsacp7mhs9pkqxanjtf292r7697pxl23mhetlljr) |

Die Kurz-SHAs 1 bis 7 stammen aus `git -C ~/repositories/reli-hub log --oneline main..pr/doku-etappe-5a` (Stand 10.11.2026), dort stehen auch die Zwischen-Commits (`374a0708`, `e75a09b4`, `f513f5c2`, `7d577608`, `0d9b1d13`).

**Bedingung:** Die Nacharbeit (Branch 8) behebt Befunde aus den Branches 1 bis 6. Den Stapel deshalb in einer Sitzung vollständig mergen und erst danach `main` pushen, wie in Etappe 3 und 4; einzelne frühere PRs ohne Branch 8 nicht ausliefern.

## 2. Merge-Ablauf (Jörg, der Reihe nach)

Der Ablauf steht im Plan `docs/superpowers/plans/2026-11-09-hub-etappe-5a-netzwerk-mitmachen.md` im Abschnitt „Merge-Ablauf“ und gilt unverändert; hier nur die Reihenfolge der Schritte.

1. Vorbereitung: `cd ~/repositories/reli-hub && git checkout main && git -c nostr.signer=joerg fetch origin main && git log --oneline main..origin/main`. Leere Ausgabe heißt: `main` unverändert; sonst `git merge --ff-only origin/main`, den Stapel rebasen, `deno task test`.
2. Je Branch als Poutník pushen: `cd ~/repositories/FOERBICO_und_rpi-virtuell/tools/poutnik && deno task push pr/<name> --as poutnik --cwd ~/repositories/reli-hub` (Branch ausgecheckt). PR-Beschreibung: Issue mit Kurz-ID und gitworkshop-Link, Entscheidung in zwei Sätzen, Prüfbefehl `deno task test`.
3. Je Branch mergen: `cd ~/repositories/reli-hub && git checkout pr/<name> && ngit --signer joerg pr merge --offline`, in der Reihenfolge der Tabelle (1 bis 8).
4. Danach einmal `main` pushen: `deno task push main --as joerg --cwd ~/repositories/reli-hub` im Wrapper-Ordner, dann `cd ~/repositories/reli-hub && git push forgejo main`. Prüfung: `curl -s https://hub.rpi-virtuell.net/ | grep -c bzBauen` größer als 0 (Auslieferung bis 30 Minuten).
5. Merge-Commits je Branch hier nachtragen: [nachtragen].

## 3. Gates für Jörg

1. Diff je Branch lesen, dann Push als Poutník (Schritt 2).
2. Mergen und `main` pushen (Schritte 3 und 4).
3. In den Kommentar-Entwürfen `{{pr:<branch>}}` und `{{main}}` ersetzen; Entwürfe in `~/.config/poutnik/protokolle/issue-kommentare-2026-12-07b/` (siehe `00-uebersicht.md`), lesen, freigeben.
4. Veröffentlichen: je Datei `zsh tools/poutnik/skripte/pub-comment.sh <datei>` in der Reihenfolge 07, 14, 16, 11, 01b, 06b, danach `cd tools/poutnik && deno task threads --repo reli-hub --since 1` (sechs Kommentare von Poutník).
5. Buchführung im FOERBICO-Repo: Spec-Fahrplan, Forgejo-Kommentare auf #879, #882, #884, #888, #889, #891, #893 (je ein eigener Aufruf), Commit der neuen Dateien; vorher `python3 -I tools/nachweis/check.py erschliessung <Ordner mit den neuen Dateien>`.
6. Nach dem Merge einmal Schnappschuss auf frischem Branch (`deno task schnappschuss`), damit der Rückfall den Stand der Tagung trägt.

## 4. Rulings und offene Punkte

### Rulings (aus dem Protokoll der Umsetzung, in der Reihenfolge ihres Auftretens)

Jede Zeile nennt die Entscheidung und, was sie kostet, falls sie falsch war.

- HUB_C wird schon in Task 1 als `let HUB_C = null` angelegt (Task 5 füllt es), damit T2/T3 es lesen können · sonst ReferenceError zwischen den Branches · Kosten falls falsch: eine Zeile zieht um.
- Task 5 heißt im Kopf des Plans teils pr/eigene-instanz; verbindlich ist pr/zuschnitt aus dem Task-Text · Kosten: Branchname.
- kind:0-Abfrage in bzLaden nimmt CO_SCHLUESSEL plus KAL_HEX (10222-Autoren vorab unbekannt); weitere Community-Profile holt cyLaden in Task 2 · Kosten falls falsch: Communities außerhalb der Schlüsselliste ohne Namen im Gefüge bis Task 2.
- bzLaden bekommt genau eine abhängige Profil-Nachfrage (kind:0, authors = Mitglieder/Zusagende/Reagierende ohne Profil, höchstens 150), weil die Reihe „Menschen“ sonst fast leer ist (Plan-Lücke; Constraint erlaubt eine abhängige Nachfrage) · Kosten falls falsch: eine Abfrage mehr je Sitzung, Test „ein REQ“ wird zu „höchstens zwei“.
- ICH schon jetzt als const ICH = { hex: null, kann: false } (Form aus Task 6) · Kosten: keine.
- „Partner“ nur für Einträge ohne Schlüssel, nicht für alle ohne href · Kosten: keine.
- CY_HEX enthält CampusCom (hat Schlüssel), navigation.test.ts-Zusicherung zu v-communities bleibt, da der Brief das Attribut stehen lässt · Kosten: keine.
- Spalte „Menschen“ im relilab lässt auch die Kalender-Quellen (KAL_HEX) weg, weil dort ein Termin-Bot ohne bot:true und Organisationsprofile erschienen · Kosten falls falsch: eine echte Person, die zugleich Kalenderquelle ist, fehlt in der Spalte.
- navigation.test.ts hatte keine v-relilab-Zusicherung; nichts zu ersetzen (Plan-Text irrte) · Kosten: keine.
- Folgen (kind:3) fragt immer per confirm mit Datum und Zahl der gefundenen Liste und warnt vor Verlust anderswo gepflegter Follows, statt Folgen ganz zu streichen · Spec 4.10 B verlangt Folgen; Kosten falls falsch: wer trotz Warnung bestätigt, kann Follows verlieren, die nur auf fremden Relays liegen. Für Jörg sichtbar machen.
- Reviewer-Minor 3 (Verhaltenstests für die Listenregeln) und 7 (Reaktion ohne e-Tag nicht senden) in dieselbe Fix-Runde gezogen, weil sie die Schreibregeln absichern · Kosten: keine.
- Task 8 bekommt keine Subagenten-Review; die Abnahme ist laut Plan Jörgs Gegenlesen (Step 3 Gate), die mechanischen Prüfungen (Namen, Projektsprache) sind gelaufen · Kosten falls falsch: inhaltliche Schwächen fallen erst beim Gegenlesen auf.
- Important 1 · Listen werden nur geschrieben, wenn jedes befragte Relay mit EOSE geantwortet hat; sonst „Nicht alle Relays haben geantwortet; nichts gesendet.“; 30004 fragt bei fehlender Liste · Kosten falls falsch: bei einem ausgefallenen Relay geht gar kein Listen-Schreiben, dafür kein Datenverlust.
- Important 3 · die fünf community:<hex>-Abfragen werden zu einer Abfrage gefaltet (gleicher coDaten-Cache); relilab-Kette bleibt, wird dokumentiert; ADR/daten.md korrigieren. Weitergehendes (ein Socket je Ansicht) → Plan 5b · Kosten falls falsch: Kaltstart Ökosystem bleibt bei rund 10 Verbindungen je Relay; Lesefreigabe für die Tagungs-IP bleibt nötig.
- Important 4 · Community-Entitäten nur für Schlüssel aus q.communities (Hub-Schlüssel plus 10222-Autoren); weicht vom Plan-Wortlaut „jede Community aus p-Tags“ ab, folgt Review Focus 1 · Kosten: Communities ohne 10222 auf den zwei Relays fehlen im Gefüge.
- Important 5 · im Live-Modus Beitreten-Knopf statt Attrappe, keine Persona-Vorbelegung · Kosten: keine.
- Folgen über kind:3 bleibt mit Rückfrage (Spec 4.10 B); Alternative Follow-Set kind:30000 mit eigenem d als Entscheidung an Jörg · Kosten falls falsch: siehe Task 6.
- Minors in die Welle: created_at = max(now, alt+1); npub-Prüfsumme in zuschnittAus; wiederhergestellte Sitzung ohne Erweiterung → kann=false; Etikett „Zur eigenen Sammlung“ sagt „öffentliche Liste“; Hinweis Doku zu 10222-limit. Übrige deferred minors bleiben nach dem Merge (Liste oben).

### Offene Punkte

- **Sendeweg nie gegen echte Relays geprüft.** Der Hub sendet nur auf Klick, aber kein Lauf ging bisher an echte Relays. Vor der Vorführung ist ein Handlauf mit einem Testschlüssel nötig: Beitreten, Gefällt mir, Sammlung speichern (im Netzwerk-Tab: ein frisches REQ, dann drei EVENT-Sockets). Ohne NIP-07-Erweiterung wurde nur der Pfad „nur ansehen“ geprüft.
- **Partner ohne Schlüssel.** Die Entscheidung steht aus, siehe `Hub-Entwicklung/2026-11-09-partner-ohne-schluessel.md`; bis dahin bleiben diese Partner Kacheln ohne Folgen- und Raum-Knopf.
- **Platzhalter in den zwei Inhaltsseiten.** `Website/content/de/kooperationsvereinbarung/index.md` und `Website/content/de/bedarfe-technik/index.md` tragen Platzhalter „[von der Redaktion zu ergänzen: …]“; beide Seiten sind untracked und warten auf das Gegenlesen.
- **Lesefreigabe für die Tagungsadresse.** Die Relays und Blossom sperren nach rund 20 schnellen Abfragen je Adresse. Ein kalter Start des Ökosystems öffnet rund zehn Verbindungen je Relay (Ruling zu Important 3), deshalb bleibt die Ausnahme für die Tagungs-IP nötig; ein Socket je Ansicht ist Sache von Plan 5b.
- **Schnappschuss nach dem Merge.** Einmal `deno task schnappschuss` auf frischem Branch, committen, nach dem Ablauf oben ausliefern; `deno.lock` nie committen.
- **Folgen: `kind:3` mit Rückfrage oder Follow-Set?** Folgen schreibt heute die Follow-Liste und fragt immer. Die verlustfreie Alternative wäre ein Follow-Set (`kind:30000` mit eigenem `d`), falls die Spec 4.10 B nicht auf `kind:3` besteht. Entscheidung bei Jörg.
- **Zurückgestellte kleine Befunde** (nach dem Merge; Einzelheiten in `.superpowers/sdd/2026-11-09-hub-etappe-5a-netzwerk-mitmachen/progress.md` im Klon): Termine mit `end`-Tag einen Tag zu lang, doppelter Helfer „neueste je Adresse“, bekannte Einträge ohne 10222 fallen aus der Live-Liste, Fokusverlust beim Neuzeichnen von Protokoll und Eigene-Instanz-Seite, Spalte „Menschen“ zeigt höchstens acht Karten, Nachzügler-Wortlaute in der Doku.

## Nachtrag 10.11.2026: Gesamt-Review und Nacharbeit

Die Gesamt-Review fand fünf wichtige Punkte, keinen kritischen. Die Nacharbeit (`pr/nacharbeit-etappe-5a`, Kopf `041a147b`) hat alle behoben, die Nachprüfung bestätigt das. Entscheidungen dabei:

- Listen (Folgen, Beitreten, Sammlung) werden nur geschrieben, wenn alle drei Relays die frische Abfrage vollständig beantwortet haben. Sonst sagt der Hub „Nicht alle Relays haben geantwortet; nichts gesendet.“ Preis: Fällt ein Relay aus, geht kein Listen-Schreiben.
- Das Protokoll nimmt nur noch auf, was im Hub eine Zeile oder Verbindung ergibt, höchstens 500 Events.
- Die fünf Community-Abfragen laufen als eine gebündelte. Ein Kaltstart des Ökosystems öffnet zehn Verbindungen zum Haupt-Relay statt vierzehn. Die Lesefreigabe für die Tagungsadresse bleibt nötig.
- Communities im Gefüge entstehen nur aus bekannten Schlüsseln und Community-Konten, nicht aus beliebigen Tags.
- Die Live-Liste der Communities zeigt den echten Knopf „Beitreten“ statt der Attrappe.

Nach dem Merge zu beheben (bewusst zurückgestellt): kein Rückfall, falls ein Relay die gebündelte Abfrage ablehnt (am 10.11. nehmen beide sie an); eine spät ladende Signer-Erweiterung lässt die Sitzung bis zur Neuanmeldung im Nur-ansehen-Zustand; ein Massenimport fremder Materialien zeichnet das Ökosystem weiter im Takt neu; dazu die kleinen Punkte aus den Einzel-Reviews (Ledger im reli-hub-Klon unter `.superpowers/sdd/2026-11-09-hub-etappe-5a-netzwerk-mitmachen/progress.md`, bis zum Merge).

Vom Controller am 10.11. im Browser geprüft: Kaltstart des Ökosystems mit leerem Zwischenspeicher, Stand „live · 802 Einträge · 1758 Kanten“, alle fünf Community-Inhalte geladen, keine Konsolenfehler. Nicht geprüft: jedes Senden an echte Relays.

## Nachtrag 10.11.2026 abends: gemergt, `main` auf Nostr, Forgejo offen

Merge-Commits (als joerg, `ngit pr merge --offline`): beziehungen `1b3bba51`, oekosystem `0933c3b9`, mitmachen `93291d3f`, relilab-labor `069ed24f`, zuschnitt `efcc42dd`, anmeldung `36a45f7e`, doku-etappe-5a `14a97679`, nacharbeit-etappe-5a `68525694`. Auf `main` laufen 90 Tests grün. `main` `68525694` ist als joerg nach Nostr gepusht (acht Statusmeldungen „gemergt“). `{{main}}` in den Kommentar-Entwürfen ist `68525694`.

Der Push nach Forgejo wurde abgelehnt: Dort liegen seit 09.11.2026 zwei Commits, die es auf Nostr nicht gibt (`51c5c58c` „Deployment auf neue Art“ und der Merge `90c3b22f` des Forgejo-PR 12). Sie fügen `.woodpecker.yml` hinzu (Auslieferung per CI bei jedem Push auf `main`) und löschen das `Dockerfile`. Der Merge mit `main` wäre konfliktfrei. Entscheidung offen: Forgejo-Stand in `main` aufnehmen und beide Seiten pushen, oder zuerst mit dem Betrieb klären. Bis dahin liefert der Server den Stand der Etappe 4 aus.

## Nachtrag 10.11.2026, 14:10 Uhr: zusammengeführt und ausgeliefert

Der Forgejo-Stand (`.woodpecker.yml`, `Dockerfile` entfällt) ist mit Jörgs Ja in `main` gemergt: `a1a1d836`, 90 Tests grün. `main` liegt auf Nostr und auf Forgejo. Die neue CI hat sofort ausgeliefert: `https://hub.rpi-virtuell.net/#oekosystem` zeigt „live · 802 Einträge · 1758 Kanten · ohne Rollenprüfung“, ohne Konsolenfehler. `{{main}}` in den Kommentar-Entwürfen ist jetzt `a1a1d836`. Lehre: vor jedem Forgejo-Push `git fetch forgejo main` und `git log main..forgejo/main` prüfen. Nachzuziehen: `docs/betrieb.md` im Hub beschreibt noch den alten Weg mit Dockerfile.

Offen bleiben: Handlauf des Sendens mit Testschlüssel (jetzt gegen die Live-Seite möglich), die sechs Kommentare, Spec-Fahrplan und Forgejo-Kommentare, Partnerentscheidung, Platzhalter der zwei Inhaltsseiten, Lesefreigabe für die Tagungsadresse, Schnappschuss, Folgeliste oder Follow-Set.

### Zurückgestellte kleine Befunde (aus dem Ledger übernommen; Berichte und Reviews liegen noch im reli-hub-Klon unter `.superpowers/sdd/2026-11-09-hub-etappe-5a-netzwerk-mitmachen/`, git-ignoriert)

- Task 1: minor (deferred): bzZeit 31922 mit end-Tag einen Tag zu lang (NIP-52 end exklusiv), kein Test
- Task 1: minor (deferred): bzQuellen und lauf.fertig/kalFertig ohne Test
- Task 1: minor (deferred): Helfer „neueste je Adresse“ doppelt in bzLaden und bzBauen
- Task 2: minor (deferred): cyRender lässt bekannte Einträge ohne Live-10222 ganz weg (kein eingebetteter Rückfall je Eintrag)
- Task 2: minor (deferred): PARTNER_MIT_SCHLUESSEL als Namensliste statt Feld kind:'partner'
- Task 2: minor (deferred): Tests nur Quelltext-Regexe für ozSichtbar, cyRender-Aufteilung
- Task 2: minor (deferred): unbekannte wahl-Id bleibt in Route; ozStandDatum mit festen Daten; bzProfil linear je Karte; Zähler „n verbunden“ vor dem Filter
- Task 2: minor (deferred): leerer Block { … } in cyLaden; Profil-Obergrenze 150 teilt sich mit Community-Konten (Menschen 120)
- Task 3: minor (deferred, für die Nacharbeit vorgemerkt): Subscription {kinds: PK_KINDS} ohne #h nimmt fremde kind-1/kind-7 auf, pkLive wächst unbegrenzt und löst alle 600 ms Neubau aus (plan-mandatiert; Fix: fremde kind 1 verwerfen, pkLive kappen)
- Task 3: minor (deferred): Ladeliste in pkAnstossen und ozOpen doppelt (gemeinsames quellenLaden)
- Task 3: minor (deferred): pkAktualisieren zeichnet #pkRoot ganz neu, Fokus geht verloren; „neu“-Markierung verblasst nicht ohne Neuzeichnen
- Task 3: minor (deferred): Tests hubAbonnieren nur Obergrenze; pkEintrag nur drei Zweige; explain() verliert Link, wenn go2[0] nicht in p2
- Task 4: minor (deferred): Spalte Menschen zeigt höchstens 8 Karten, Stand-Zeile zählt alle (bis 40)
- Task 4: minor (deferred): href="" möglich, falls evToTermin keine URL liefert; Kriterien-Test zählt Apostrophe; Personenkarten stapeln ≤560px
- Task 5: minor (deferred, für die Nacharbeit vorgemerkt): zuschnittAus prüft npub nur per Regex ohne Prüfsumme (Tippfehler ergibt stillen Zuschnitt auf fremden Schlüssel); Test fehlt
- Task 5: minor (deferred): eiRender baut nach cyLaden alles neu, Eingabe in #eiNpub geht verloren; „in Vorbereitung“ liest ocDaten ohne Laden; globales const B32 tot; Name doppelt maskiert; Leiste-✕ verliert Fokus; Tests nur Zeichenketten
- Task 6: minor (deferred): akZeichnen auf #person ruft prOpen neu (Ladezustand, ggf. neue Abfrage); „Gefällt dir“/„Zugesagt“ kennen ältere eigene Events nicht; crRender-Schlüsselsuche inline; kein confirm bei fehlender Sammlungs-Liste
- Task 6: minor (deferred): Platzhalter-ichDaten kann #profil kurz als „nicht erreichbar“ zeigen; RSVP/Like ohne gemerktes Event tut still nichts
- Task 7: minor (deferred): docs/daten.md:313 nennt den Dialog noch „#anmelden“; „eine Profilabfrage“ ohne „höchstens“ in konstruktion.md:135 und ADR Folgen; kein RED-Lauf für den Doku-Test
- Fix-Welle: parked · kein Rückfall, wenn ein Relay das gebündelte REQ ablehnt · Ruling: real, aber heute nicht ausgelöst (Controller-Browserlauf: beide Relays nehmen das Bündel an, alle fünf Caches gefüllt); nach dem Merge beheben (leere Teile nicht cachen, auf Einzelabfragen zurückfallen) · Kosten falls falsch: lehnt ein Relay künftig viele Filter ab, zeigt das Ökosystem „live“ ohne Community-Inhalte.
- Fix-Welle: parked · wiederhergestellte Sitzung schreibt kann:false dauerhaft, wenn die Erweiterung spät lädt · Ruling: real, harmlos (neu anmelden hilft), nach dem Merge · Kosten: Person bleibt bis zur Neuanmeldung im Nur-ansehen-Zustand.
- Fix-Welle: parked · bzMass vergleicht nur Zahlen; Massenimport fremder 30142 zeichnet weiter alle 600 ms neu (gekappt, pausiert bei Fokus) · Ruling: real, nach dem Merge · Kosten: unruhige Ökosystem-Ansicht während eines Imports.

## Nachtrag 10.11.2026, 14:30 Uhr: Kommentare veröffentlicht

Die sechs Kommentare der Runde 8 (Issues 07, 14, 16, 11 sowie Stufe B von 01 und 06) sind mit Jörgs Ja als Poutník auf gitworkshop veröffentlicht, je 4 bis 5 von 7 Relays; Kennungen in `~/.config/poutnik/protokolle/issue-kommentare-2026-12-07b/00-uebersicht.md`. Vor der Veröffentlichung an den Live-Stand angepasst: Verweis auf die Nacharbeit, „rund zehn Verbindungen zum Haupt-Relay“, die zwei Inhaltsseiten als „in Vorbereitung“. Offen bleiben: Spec-Fahrplan, Kommentare auf den Nachweis-Issues in Forgejo, Handlauf des Sendens, Commit der Dateien in diesem Repo.

## Nachtrag 10.11.2026, 14:20 Uhr: Buchführung

Spec-Fahrplan (Zeile „bis 23.12.2026“) um „Teil 5a erledigt am 10.11.2026“ ergänzt. Sieben Kommentare auf den Nachweis-Issues in Forgejo: #879 (14646), #884 (14647), #888 (14648), #889 (14649), #893 (14650), #882 (14651), #891 (14652). Commit dieser Datei, des Plans, der Spec und der Partner-Vorlage auf `main`; die zwei Inhaltsseiten unter `Website/content/de/` bleiben bis zu Jörgs Gegenlesen untracked, weil ein Commit dort die Pipeline auslöst.
