#!/usr/bin/env python3
"""Postet die freigegebenen Issues auf Forgejo. Aufruf: post_issues.py [--dry]"""
import json, os, sys, urllib.request, urllib.error

DRY = '--dry' in sys.argv
T = open(os.path.expanduser('~/.config/forgejo/token.txt')).read().strip()
H = {'Authorization': 'token ' + T, 'Content-Type': 'application/json'}
API = 'https://git.rpi-virtuell.de/api/v1/repos/Comenius-Institut/'
OPEN = 'FOERBICO_und_rpi-virtuell'
CLOSED = 'FOERBICO_und_rpi-virtuell-geschlossen'
OPEN_URL = 'https://git.rpi-virtuell.de/Comenius-Institut/FOERBICO_und_rpi-virtuell/issues/'


def call(method, url, body=None):
    if DRY:
        print(f'  [dry] {method} {url}' + (f' ({len(json.dumps(body))} Bytes)' if body else ''))
        return {'number': 0}
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body is not None else None,
                                 headers=H, method=method)
    try:
        return json.load(urllib.request.urlopen(req))
    except urllib.error.HTTPError as e:
        print('FEHLER', e.code, e.read().decode()[:400]); raise


def create(repo, title, body, milestone, labels, close=False):
    j = call('POST', f'{API}{repo}/issues', {'title': title, 'body': body, 'milestone': milestone, 'labels': labels})
    n = j['number']
    if close:
        call('PATCH', f'{API}{repo}/issues/{n}', {'state': 'closed'})
    print(f'{"geschlossen" if close else "offen     "}  {repo.split("_")[-1][:12]:12} #{n}  {title[:80]}')
    return n


def patch_body(repo, n, body):
    call('PATCH', f'{API}{repo}/issues/{n}', {'body': body})


# ---------------------------------------------------------------- offen
OPEN_ISSUES = {}

OPEN_ISSUES['A'] = dict(milestone=88, labels=[321, 122, 178],
    title='Bildnachweise als Standard: `# bilder`-Block, Konvention bildattribution.md, kind:1063',
    body='''Seit dem 07.09.2026 trägt jeder oer.community-Beitrag seine Bildnachweise als dritten markierten Block im Frontmatter von `index.md`. Dieses Issue hält fest, was entschieden ist, und sammelt die nächsten Schritte. Beantwortet #191.

**Stand 16.09.2026**

- Konvention: `Orga/oer-community-webseite-orga/wissensgrundlagen/bildattribution.md`. Felder `alt`, `imageUrl`, `title`, `sourceUrl`, `author`, `authorUrl`, `licence`, `licenceUrl`, `modification`, `ai`; Reihenfolge normativ. Caption-Zeile direkt unter dem Bild: `[title](sourceUrl), [author](authorUrl), [licence](licenceUrl), KI-Kennzeichnung, modification`.
- Der `# bilder`-Block ist Eingabe zum Prägen. Wahrheit ist der Lizenznachweis `kind:1063` auf dem Relay, adressiert über den SHA-256 des Bildes (x-Tag). Die Abbildungstabelle Block → 1063-Tags steht in der Konvention.
- Bilder liegen als Blossom-Hash-URL (`https://blossom.edufeed.org/<sha256>.<ext>`) in `commonMetadata.image`, `cover.image` (`relative: false`) und im Fließtext. `felder.yaml` beschreibt Zielform und lokale Übergangsform.
- KI-Kennzeichnung: `ai: generated | modified` nach dem edufeed-Wiki vom 10.09.2026 (EU-AI-Office-Icons), in der Caption als „KI-generiert“ oder „KI-verändert“ hinter der Lizenz. In allen vier Werkzeugen (mdparser/sync, md2blossom, foerbico-editor, oer-community) am selben Tag umgesetzt.
- Lizenzregeln: Eigene Fotos folgen der Footer-Regel (CC BY FOERBICO, `sourceUrl` = der Beitrag). Fremde Werke tragen Urheber:in, Quelle und deren Lizenz. Was nicht frei lizenziert werden darf, bekommt keinen CC-Eintrag.
- Präzedenzfall Logos (16.09., hello-world): geschützte Logos von Institutionen bekommen `licence: ©` mit `licenceUrl` auf das UrhG, `author` ist die Institution. Als Regel 9 in `bildattribution.md` festgeschrieben.
- Präzedenzfall KI-Bilder (16.09., KI-im-RU): rein KI-generierte Bilder erhalten `CC0 1.0` statt CC BY, weil ohne persönliche geistige Schöpfung (§ 2 UrhG) kein Recht einzuräumen ist. Der Text bleibt CC BY 4.0.

**Commits (Auswahl)**: 240ba8e, 3056ca9, fbc94d2, 3efa594, 9770638; mdparser 820f0d1, 56892f9, 01a4efa.

**Offen**

- [ ] Präzedenzfall CC0 für KI-Bilder in `bildattribution.md` festschreiben.
- [ ] `content-lint` soll YAML-Gültigkeit und Blossom-Form vor dem Merge prüfen (Entscheidung 09.09.: ersetzt den Regression-Wächter). Zwei Build-Brüche in einer Woche zeigen den Bedarf.
- [ ] Konvention und FOERBICO-Zusatzfelder in die AMB-NIP-Diskussion einbringen (#794).
''')

OPEN_ISSUES['B'] = dict(milestone=118, labels=[178, 254],
    title='Bildmigration der oer.community-Beiträge auf Blossom',
    body='''Alle Bilder der oer.community-Beiträge sollen mit Lizenznachweis auf Blossom liegen. Arbeitsliste mit fertigen Blockvorschlägen je Beitrag: `Orga/oer-community-webseite-orga/bildmigration.md`. Der Hub zeigt Cover ohne Nachweis seit 15.09. mit „Lizenz ungeklärt“ (ADR-0032); Bilder von `oer.community` gelten als unaufgelöst (ADR-0030). Damit ist die Migration sichtbar die Redaktionsliste des Hubs. Konvention: #{A}.

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
''')

OPEN_ISSUES['C'] = dict(milestone=8, labels=[321, 122, 213],
    title='Nostr-Sync: stille Fehlschläge behoben, Backfill, Bilder, Seiten und Listen in der CI',
    body='''Die Pipeline `.github/workflows/nostr-sync.yml` (GitHub-Mirror → `mdparser/sync` → Relays) publiziert Inhalte aus `Website/content/` als `kind:30023` und `kind:30142`. Statusbericht 02.–15.09.2026.

**Befund 02.09.**: Die Pipeline lief seit Monaten fast leer, ohne dass es sichtbar war. `keywords` war Pflichtfeld; 74 von 93 Dateien hatten keins und wurden übersprungen. Läufe waren grün, obwohl nichts publiziert wurde.

**Behoben und ausgebaut**

- `keywords` empfohlen statt Pflicht (78 statt 18 Dateien publizierbar). Job-Summary nennt publizierte, übersprungene und fehlgeschlagene Posts; ein Abbruch vor dem Publish-Step erscheint als Warnung (424cbe5, bd82037).
- Backfill `--force-all` am 02.09.: 81 publiziert, 13 übersprungen, 1 fehlgeschlagen (2025-07-07-oer-rel-paed, 131 KB, über der NIP-46-Grenze von 65535 Bytes für die verschlüsselte Signieranfrage; Protokollgrenze, der Post bleibt nur auf der Hugo-Site).
- 07.09.: `x`-Tags aus den Blossom-URLs (Cover zuerst, je Fließtextbild eins, kein `imeta`).
- 09.09.: Bilderschritt in `publish` (`core/bilder.ts`): Blob-Upload nach Blossom, wenn die Datei im Ordner liegt; Lizenznachweis aus dem `# bilder`-Block prägen, wenn auf dem Relay keiner oder ein abweichender liegt. Nichts davon blockiert das 30023, Git ist die Wahrheit.
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
''')

OPEN_ISSUES['D'] = dict(milestone=90, labels=[122, 321, 178],
    title='Redaktionswerkzeuge: md2blossom, blossom-bunker, foerbico-editor',
    body='''Drei Werkzeuge, ein Ziel: Ein Beitrag mit Bildern kommt ohne lokalen Nostr-Key nach Git; alles, was den FOERBICO-Key braucht, macht die CI nach dem Merge (#{C}).

**`Website/scripts/md2blossom.mjs`** (Node, seit 04.09., Tests `npm test`): hasht Bilder im Beitragsordner, ersetzt relative Pfade durch Blossom-URLs, schreibt Caption nach Konvention und `image`/`cover` um, legt unsignierte 30023/1063-Vorlagen und ein AMB-JSON ab. Bilder ohne Blockeintrag: `TODO:LICENSE`, Exit 2, Blockvorlage wird gedruckt. Kein Upload, keine Signatur.

**`Website/scripts/blossom-bunker.ts`** (Deno, seit 09.09.): `upload` (BUD-01, Hash geprüft) und `publish` (1063 signieren) über den NIP-46-Bunker, nur für Sonderfälle seit dem CI-Bilderschritt.

**foerbico-editor** (SvelteKit, statisch, Repo `Comenius-Institut/foerbico-editor`, seit 07.09.): Formular für einen Beitrag mit den drei Blöcken nach `felder.yaml` und `bildattribution.md`. Ausgang: Branch `beitrag/<kürzel>`, Commit, Pull Request unter dem eigenen Forgejo-Konto (persönliches Token). Bilder werden im Browser gehasht; liegt zum Hash ein 1063 auf `relay-rpi.edufeed.org`, werden die Angaben übernommen. Bestehende Beiträge lassen sich laden und migrieren. Am 09.09. wurde der Nostr-Entwurfsweg zugunsten des Git-Wegs entfernt. Woodpecker-Pipeline seit 08.09.

**Offen**

- [ ] Editor: Schriften lokal; Kürzel-Änderung legt neuen Ordner an; Bilddateien überleben ein Neuladen nicht; keine Bildverkleinerung.
- [ ] Wer aus dem Team testet den Editor an einem echten Beitrag? Die beiden Build-Brüche kamen aus dem Forgejo-Webeditor; der foerbico-editor schreibt gültiges YAML.
- [ ] Produktive Adresse des Editors festlegen und in `bildmigration.md` nennen.
''')

OPEN_ISSUES['E1'] = dict(milestone=99, labels=[255, 321, 122],
    title='Hub: Artikel-Detailansicht mit Lizenznachweis, Demonstrator „Beitrag live“ (02.–10.09.)',
    body='''Repo `Comenius-Institut/oer-community` (bis 15.09. `community-hub`; `docs/STATUS.md` als Logbuch, Entscheidungen als ADR mit Index unter `docs/entscheidungen/`). Erster Abschnitt 02.–10.09.: ein Beitrag mit nachgewiesener Bildlizenz als OER-Client-Durchstich. Fortsetzung: #{E2}.

**Erreicht**

- Artikelseite liest `kind:30023` von den Relays und zu jedem Bild den `kind:1063` über den Hash. Prüfkette in fünf Schritten gibt den Abbruchgrund zurück; „nicht erreichbar“ und „hat nichts“ werden unterschieden (ADR-0013/0022).
- Entwickleransicht `…/json`: Beitrag und Nachweis nebeneinander mit lieferndem Relay und Prüfschritten (ADR-0017).
- Bildlizenz wie edufeed, Attribution nach eigener Konvention: Bild immer ausgeliefert, Lizenzstand daran; Alt-Text aus dem `alt`-Tag (ADR-0022). Fließtextbilder mit Hash-URL aufgelöst, hashlose entfernt (ADR-0023/0015). KI-Marke aus dem `ai`-Tag (ADR-0025).
- Designsystem in der Detailansicht: lokale Schriften, Kontrastwerte als Test (ADR-0018, später durch ADR-0031 ersetzt).
- Redaktionsmodell ADR-0021 (Entwürfe unter Redaktions-Keys, Freigabe per NIP-32-Label, FOERBICO-Key nur durch `sync adopt`), Status offen; `docs/redaktion-longform.md`.
- Auslieferung rootlos, Dienst auf 127.0.0.1; Woodpecker-Pipeline seit 09.09.
- Demonstrator `docs/beitrag-live.html` in diesem Repo (07.09.): eine HTML-Datei ohne Build, Beitrag mit Nachweisen live vom Relay, `?d=<slug>`.

**Offen**

- [ ] ADR-0024 (Vorrang des eigenen Keys bei konkurrierenden Nachweisen) umsetzen.
- [ ] ADR-0021 im Team bestätigen; Nachtrag zu Entwürfen (30024) liegt ungespeichert vor.
- [ ] Prüfwerkzeug für die Redaktion: Welche Beiträge tragen Bilder ohne Nachweis? Seit ADR-0032 im Blog sichtbar, eine Liste fehlt.
''')

OPEN_ISSUES['E2'] = dict(milestone=83, labels=[255, 321, 178],
    title='oer.community aus Nostr: Schaufenster live, Seiten, Feed, Zweisprachigkeit, Termine (14.–15.09.)',
    body='''Zweiter Abschnitt im Repo `Comenius-Institut/oer-community` (erster: #{E1}). Entscheidung ADR-0026: Das Vorhaben ist oer.community aus Nostr, FOERBICO statt relilab als Zuschnitt. Der eigentliche Community-Hub kommt später, auf den Erfahrungen dieses Schaufensters (Teambesprechung 15.09.).

**Erreicht, live unter `community-hub.rpi-virtuell.net` seit 14.09., 19:03 Uhr**

- Spiegel im Prozess statt Live-Abfrage (ADR-0028): lädt 87 Artikel in rund 2 Sekunden, Standdatei auf der Platte, Architekturtest verbietet Relay-Zugriff außerhalb des Spiegels. Adressen sind das `d` des Beitrags, `naddr` leitet weiter (ADR-0029).
- Seitenstruktur aus Nostr (ADR-0027): Seiten per Selbst-Label, Menü und Fußzeile als Kuratierungslisten `kind:30004`, Startseite als Seite mit `d = startseite`, Profil-`about` als Fußtext. Blog und Themen als Ansichten.
- FOERBICO-Designsystem (ADR-0031, `docs/designsystem.md`), Feed `application/rss+xml`, Sitemap, kanonische URLs auf `https://oer.community/…`.
- Lizenzpille (ADR-0032): Lizenzstand als Overlay auf jedem Bild, auch in der Übersicht; Cover ohne Nachweis erscheinen mit „Lizenz ungeklärt“. Bilder von `oer.community` gelten als unaufgelöst (ADR-0030).
- Zweisprachig DE/EN (ADR-0033, offen): `/en` als englische Startseite, Umschalter, `hreflang`, Übersetzungen als `a`-Tag mit Marker `translation`. Live geprüft am 15.09.
- Termine aus der Community (ADR-0034): Quelle je Inhaltsart, Artikel und Seiten vom FOERBICO-Key, Termine (`kind:31922/31923`) aus der Communikey-Community rpi-virtuell mit `h`-Tag und Redaktionskreis (`kind:30000`); Seite `/termine`, „Nächste Termine“ auf beiden Startseiten. Erster Termin: Abschlusstagung „Offen. Vernetzt. Zukunft.“ (2.–3. Februar 2027, Frankfurt).
- Repo am 15.09. in `oer-community` umbenannt (ADR-0011-Nachtrag). 422 Tests grün, `pnpm check` ohne Befund.

**Offen**

- [ ] ADR-0033 und ADR-0034 in der nächsten Besprechung bestätigen.
- [ ] Redaktion: Seitenbeschreibungen (abgeleitet), doppelte Überschrift auf der Startseite, Profil-`about`, Startseiten-Logos (relative Pfade, im Hub unsichtbar).
- [ ] Umschalttag oer.community → Hub festlegen (Cut-over-Bedingungen in `redaktion-longform.md`).
- [ ] Dunkelmodus, Logo bewusst offen gelassen.
- [ ] Betrieb nach Umbenennung: Server-Verzeichnis, Unit, DNS `oer-community.rpi-virtuell.net`, `.woodpecker.yml`, `docs/betrieb.md` (Details im geschlossenen Repo).
''')

OPEN_ISSUES['F'] = dict(milestone=88, labels=[321],
    title='Abstimmung mit edufeed: x-Tags, ai-Tag, Blossom-Freischaltung, Lizenz-Relay',
    body='''Sammelissue für die Schnittstellen zu edufeed (Relays, Blossom, Wiki `license-events-nope`, edufeed-app). Bezug: #794, #{A}.

**Geklärt**

- 07.09.: Bild-Hashes als wiederholte `x`-Tags am 30023, kein `imeta`. Umgesetzt in mdparser und Hub.
- 10.09.: `ai`-Tag am 1063 (`generated | modified`, Wiki-Fassung 10.09.). Alle FOERBICO-Werkzeuge am selben Tag nachgezogen; die edufeed-app zeigt die Marke vor dem Lizenzkürzel, wir hinter dem Lizenz-Link.
- Lizenznachweise liegen auf `relay-rpi.edufeed.org` und `relay.edufeed.org`; Blossom `blossom.edufeed.org`; Upload mit dem FOERBICO-Key funktioniert (CI seit 09.09.).
- Termine kommen aus der Communikey-Community rpi-virtuell der edufeed-app (`kind:31922`, ADR-0034).
- `relay-rpi.edufeed.org` war am 03./07.09. vorübergehend nicht erreichbar (Platte voll), seither stabil.

**Offen**

- [ ] `PUT /mirror` (BUD-04) auf Blossom für `sync adopt`.
- [ ] Bunker-Modell für Redaktions-Keys (ADR-0021).
- [ ] Nimmt `relay.edufeed.org` dauerhaft 1063 an?
- [ ] Umschalttag oer.community → Hub gemeinsam festlegen.
- [ ] Konvention `bildattribution.md` und Zusatzfelder (`authorUrl`, `modification`) ins Wiki (#794).
''')

OPEN_ISSUES['G'] = dict(milestone=100, labels=[254, 178],
    title='Blogbeitrag „Künstliche Intelligenz im evangelischen Religionsunterricht“ (Wiederveröffentlichung als OER)',
    body='''Branch `add-blogpost-ki-ru-baden`, PR #838 (WIP). Beitrag von Olav Richter (RPI Karlsruhe), zuerst in den Badischen Pfarrvereinsblättern 7/2026, mit Genehmigung von Autor und Redaktion unter CC BY 4.0 wiederveröffentlicht. Rund 4.900 Wörter. Erster Beitrag eines ALPIKA-Instituts, der als OER auf oer.community nachnutzbar wird.

**Stand 16.09.2026**

- 11.09.: Text übernommen, Frontmatter nach `felder.yaml`, `isBasedOn` auf die Erstveröffentlichung (af370ee).
- 16.09.: Titelbild vom Autor (KI-generiert, 13.09.), `# bilder`-Block gefüllt, `ai: generated`. Lizenz des Bildes `CC0 1.0`, weil rein maschinell erzeugte Bilder keine persönliche geistige Schöpfung nach § 2 UrhG sind; der Text bleibt CC BY 4.0 (9770638). Erster Nachweis mit `ai: generated` im Bestand.
- 16.09.: md2blossom-Probelauf ohne `--write` läuft durch (Exit 0): ein Bild, ein Nachweis, Cover wird zur Blossom-URL `bb3dfcb3…jpg`, `commonMetadata.image` wird ergänzt, `cover.relative: false`. Mit `--write` schreibt md2blossom diese Fassung direkt in `index.md`; die Bilddatei bleibt im Ordner, damit die CI den Blob hochladen kann (#{C}).
- `creativeWorkStatus` noch `Draft`.

**Offen**

- [ ] Review gegen die Druckfassung (Fußnoten, Zitate).
- [ ] `md2blossom --write`, `creativeWorkStatus: Published`, PR #838 aus WIP nehmen, Merge. Die CI publiziert.
- [ ] Autor informieren; Beitrag über die ALPIKA-Kanäle streuen.
''')

COMMENT_191 = '''Stand 16.09.2026: Beantwortet. Bildmetadaten stehen beitragsbezogen als `# bilder`-Block im Frontmatter (Konvention `Orga/oer-community-webseite-orga/wissensgrundlagen/bildattribution.md`), werden von der CI als `kind:1063` mit dem SHA-256 des Bildes publiziert und vom Hub live vom Relay gelesen. Details und offene Punkte in #{A}. Schema.org-Auszeichnung für Google Images ist damit nicht gemacht, wäre aber aus dem Block ableitbar. Ich schließe das Issue; der Rest läuft in #{A}.'''

# ---------------------------------------------------------------- geschlossen
CLOSED_ISSUES = {}

CLOSED_ISSUES['H'] = dict(milestone=184, labels=[334], close=True,
    title='Wiederveröffentlichung RPI Karlsruhe: Genehmigungen, Titelbild, Kontakt',
    body='''Dokumentation zum öffentlichen Issue {OPEN}{G} (Blogbeitrag „KI im evangelischen Religionsunterricht“, PR Comenius-Institut/FOERBICO_und_rpi-virtuell#838).

- Genehmigung zur Wiederveröffentlichung unter CC BY 4.0 liegt vor von Olav Richter (Autor, Studienleitung Medienpädagogik, RPI Karlsruhe) und von der Redaktion der Badischen Pfarrvereinsblätter (Dr. Kunath).
- 13.09.2026: Titelbild vom Autor geliefert (mit ChatGPT erzeugt), Lizenz CC0 1.0, `ai: generated`.
- Auf Wunsch des Autors wurde der Name der Redaktion aus dem öffentlichen Wiederveröffentlichungshinweis entfernt (Commit 9770638); die Genehmigung selbst ist hier dokumentiert.
- `authorUrl` im Bildnachweis zeigt auf rpi-baden.de.
- Nach Veröffentlichung: Link an Autor und Redaktion, Dank.

Geschlossen zur Dokumentation.
''')

CLOSED_ISSUES['I'] = dict(milestone=202, labels=[339], close=True,
    title='Bildmigration: Abstimmung im Team, zwei Build-Brüche, Midjourney-Konto',
    body='''Dokumentation zum öffentlichen Issue {OPEN}{B} (Bildmigration).

- Gina arbeitet im Forgejo-Webeditor auf Branch `add-bildlizenzen`: 10.09. zehn Beiträge (gemerged), 11.09. TikTok, 16.09. hello-world (offen).
- Zwei Hugo-Build-Brüche durch unquotierte `alt`-Texte mit „: “: 10.09. Canva („Ausweis: Canva-Lizenz“, fünf rote CI-Läufe), 16.09. hello-world („Das FOERBICO Team: Phillip, …“). Jörg hat beide repariert (3efa594) und den Abschnitt „Stolpersteine beim händischen Bearbeiten“ in `bildattribution.md` ergänzt. Das YAML ist die Fehlerquelle, nicht die Person. Für die Webeditor-Arbeit: vorher YAML-Prüfer oder gleich den foerbico-editor. Besser: `content-lint` in der Woodpecker-Pipeline, damit der PR rot wird und nicht die Website.
- OER-Fachtag-Orca.NRW: Cover liegt nur im Midjourney-Konto von Jörg. Download, dann `ai: generated`. Liste auf weitere Midjourney-URLs prüfen.
- Aufteilung der 70 offenen Beiträge im Team ist noch offen; läuft über das öffentliche Issue.

Geschlossen zur Dokumentation.
''')

CLOSED_ISSUES['J'] = dict(milestone=173, labels=[171, 334], close=False,
    title='Personen auf Fotos in Bildnachweisen: Klarnamen in alt und title',
    body='''Bezug: öffentliche Issues {OPEN}{A} (Konvention) und {OPEN}{B} (Migration). Datenschutz.

Mit der Migration werden `alt`- und `title`-Texte als `kind:1063` auf öffentliche Relays publiziert. Relay-Events lassen sich nachträglich kaum zurückholen. Aktuell mit Klarnamen:

- tagung-open-education (digiLL): Joana Kadir und Matthias Kostrzewa in `alt` und `title` (Eröffnung), Foto FOERBICO, bereits publiziert.
- oercamp-2026: Gina Buchwald-Chassée in `alt`, bereits publiziert.
- hello-world (Branch): „Das FOERBICO Team: Phillip, Jörg, Ludger, Laura und Gina“ in `alt`; eigenes Team, Vornamen.
- Weitere Beiträge der Arbeitsliste zeigen Veranstaltungsfotos.

**Grundsatz (16.09.2026)**: Fotos von unseren Veranstaltungen gelten als mit Einwilligung aufgenommen und stehen unter CC BY. Es werden keine Fotoerlaubnisse nachträglich eingeholt. Bereits publizierte Nachweise bleiben.

**Zu klären**

- [ ] Regel für neue Nachweise: Klarnamen in `alt`/`title` nur, wenn die Person öffentlich auftritt (Referent:in, Podium) oder zugestimmt hat; sonst Funktion statt Name („Eröffnung durch das digiLL-Team“). Öffentlich in `bildattribution.md`, ohne Beispielnamen.
- [ ] Widerspruch einer abgebildeten Person: Nachweis neu prägen (der jüngste gewinnt) und Löschanfrage (`kind:5`) an die Relays. Ablauf kurz dokumentieren.
- [ ] Redaktionsliste `kind:30000` und Profil enthalten Pubkeys und Namen des Redaktionskreises; Einverständnis der Mitglieder festhalten.
''')

CLOSED_ISSUES['K'] = dict(milestone=198, labels=[369, 171], close=False,
    title='Signatur-Infrastruktur: Amber-Bunker, Secrets, lokaler Key. Ziel: nsec im Bunker-Dienst',
    body='''Bezug: öffentliches Issue {OPEN}{C} (Nostr-Sync). Sicherheitsrelevant, deshalb hier.

**Zielbild**: Der FOERBICO-nsec liegt in einem Bunker-Dienst (NIP-46), nicht auf einem Handy und nicht als Klartext in einer `.env`. CI und Handläufe signieren ausschließlich über diesen Bunker. Wir wollen auf diese Lösung umstellen.

**Ist-Stand 16.09.2026**

- Bunker ist die Amber-App auf Jörgs privatem Handy. Fällt das Gerät aus oder ist offline, publiziert die CI nichts („Bunker connect timeout“); so im Juni und August 2026 (Ausfall über Wochen, erst am 02.09. sichtbar).
- Secrets (`BUNKER_URL`, `CLIENT_SECRET_HEX`, `AUTHOR_PUBKEY_HEX`) als GitHub-Repo-Secrets im Mirror `rpi-virtuell/FOERBICO_und_rpi-virtuell` und lokal in `mdparser/.env`; `blossom-bunker.ts` nutzt dieselbe Datei.
- Seit 14.09. (mdparser 451e6e4) erlaubt `AUTHOR_SECRET_HEX` in der lokalen `.env` `sync redaktion` und `sync navigation` ohne Bunker. Damit liegt der FOERBICO-Schlüssel im Klartext auf Jörgs Laptop. Die CI bleibt beim Bunker.
- Die CI läuft auf GitHub (Mirror), nicht auf der eigenen Forgejo/Woodpecker-Infrastruktur.

**Schritte**

- [ ] Bunker-Dienst aufsetzen (Server im Institut oder bei edufeed), nsec dort hinterlegen, Amber nur noch als Fallback oder abschalten.
- [ ] CI-Secrets auf den neuen Bunker umstellen (`BUNKER_URL`), `CLIENT_SECRET_HEX` behalten.
- [ ] Lokalen Klartext-Key (`AUTHOR_SECRET_HEX`) entfernen, sobald Menü und Redaktionsliste über die CI oder den Bunker laufen.
- [ ] Wer außer Jörg kann im Notfall neu pairen? Runbook (`mdparser/docs/SETUP-GUIDE.md`, Hürde 4) im Team bekannt machen.
- [ ] Redaktions-Keys nach ADR-0021: Verwahrung im selben Bunker-Modell, Verantwortliche.
- [ ] Umzug der Pipeline auf Woodpecker prüfen, damit Secrets im Haus bleiben.
- [ ] Benachrichtigung bei roten Läufen an mehr als eine Person.
''')

CLOSED_ISSUES['M'] = dict(milestone=182, labels=[369], close=False,
    title='Betrieb oer-community: Server, Unit, DNS, Umschalttag',
    body='''Bezug: öffentliches Issue {OPEN}{E2} (oer.community aus Nostr).

Ergebnisse der Besprechung am 15.09.2026 (Jörg, Gina, Ludger): Quelle je Inhaltsart (Artikel, Seiten, Listen, Profil vom FOERBICO-Key; Termine aus der Community rpi-virtuell), Umbenennung des Repos in oer-community, der eigentliche Community-Hub kommt später.

**Aufgaben Ludger**

- [x] Server-Verzeichnis und systemd-Unit von `community-hub` auf `oer-community` umbenennen; `deploy-app.sh` anpassen.
- [x] DNS `oer-community.rpi-virtuell.net` anlegen.
- [ ] Woodpecker Repo 13: prüfen, ob Webhook und Clone nach der Umbenennung greifen.
- [ ] `COMMUNITY_PUBKEY` nicht setzen (rpi-virtuell ist Standard; ein gesetzter leerer Wert schaltet den Kalender ab).

**Aufgaben Jörg**

- [ ] `.woodpecker.yml` und `docs/betrieb.md` auf den neuen Namen nachziehen.

**Offen im Team**

- [ ] Umschalttag oer.community → Hub: Entscheidung mit Steffen und Ludger, Cut-over-Bedingungen aus `redaktion-longform.md`.
- [ ] ADR-0033, ADR-0034 und der Nachtrag zu ADR-0021 (Entwürfe als 30024) in der nächsten Runde bestätigen.
''')


def main():
    print('=== offenes Repo ===')
    nums = {}
    for k, it in OPEN_ISSUES.items():
        nums[k] = create(OPEN, it['title'], it['body'], it['milestone'], it['labels'])
    # Querverweise nachtragen
    for k, it in OPEN_ISSUES.items():
        if '#{' in it['body']:
            patch_body(OPEN, nums[k], it['body'].format(**nums))
    # #191 beantworten und schließen
    call('POST', f'{API}{OPEN}/issues/191/comments', {'body': COMMENT_191.format(**nums)})
    call('PATCH', f'{API}{OPEN}/issues/191', {'state': 'closed'})
    print('#191 kommentiert und geschlossen')

    print('=== geschlossenes Repo ===')
    cnums = {}
    for k, it in CLOSED_ISSUES.items():
        body = it['body'].replace('{OPEN}', OPEN_URL).format(**nums)
        cnums[k] = create(CLOSED, it['title'], body, it['milestone'], it['labels'], close=it['close'])
    json.dump({'offen': nums, 'geschlossen': cnums}, open(os.path.join(os.path.dirname(__file__), 'issue-nummern.json'), 'w'), indent=1)
    print('Nummern:', nums, cnums)


if __name__ == '__main__':
    main()
