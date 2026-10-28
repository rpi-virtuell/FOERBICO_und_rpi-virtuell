# Poutník: Issues, Kommentare und Code direkt aus dem Gespräch nach gitworkshop

Stand: 26.10.2026. Entstanden im Brainstorming mit Jörg Lohrer. Dieses Dokument beschreibt,
was gebaut wird und warum; die Umsetzungsschritte folgen in einem eigenen Plan.

## 1. Absicht und Hintergrund

Zwei Projekte überlagern sich zunehmend:

- **FOERBICO und rpi-virtuell** (gefördertes Projekt des Comenius-Instituts). Koordination und
  Nachweisführung laufen über Issues auf Forgejo (git.rpi-virtuell.de), ein offenes und ein
  geschlossenes Repo, mit Meilensteinen je Arbeitspaket.
- **edufeed-app** (edufeed-Team, Lead-Maintainer `laoc42`). Seit 02.09.2026 laufen alle Issues
  als NIP-34-Events auf Nostr und werden auf gitworkshop.dev angezeigt. Der Agent des
  edufeed-Teams, **Antiope**, schreibt dort einen großen Teil der Issues und Kommentare und setzt
  die Status. Die Zusammenarbeit mit edufeed findet dort statt, nicht auf Forgejo.

Bisher entstanden Entwürfe für edufeed-Issues in diesem Repo als Markdown und wurden von Hand in
die Weboberfläche von gitworkshop übertragen. Rückmeldungen dort (Antworten, Status) waren hier
nicht sichtbar; sie werden auf gitworkshop in der Regel innerhalb weniger Tage gegeben.

**Ziel:** Ein Entwurf entsteht im Gespräch mit Claude, wird von Jörg freigegeben und landet
direkt auf gitworkshop, als Issue oder Kommentar, veröffentlicht von der Agenten-Identität
**Poutník**, die wie Antiope nur auf Nostr existiert. Jörg kann jederzeit fragen, wo seine
Fäden gerade stehen, und bekommt eine Antwort aus beiden Welten (gelesen wird auch Forgejo).
Es gibt keinen dritten Ort, nichts wird doppelt gepflegt.

## 2. Ziele, Nicht-Ziele, Anti-Ziele

**Ziele**

1. Issues und Kommentare auf gitworkshop (NIP-34) aus dem Gespräch heraus veröffentlichen.
2. Eine eigene Agenten-Identität **Poutník** mit eigenem Nostr-Schlüssel, die klar vom Menschen
   Jörg unterscheidbar ist, und bei der Jörg jeden Text vorher freigibt. Poutník existiert
   **nur auf Nostr**, genau wie Antiope.
3. Eine Live-Abfrage „Wo stehen meine Fäden?“, die Issues und Kommentare von Jörg und Poutník
   auf Nostr holt, dazu lesend Jörgs Forgejo-Fäden, und alles nach letzter Aktivität sortiert
   zeigt.
4. Ein fester Ablauf, den auch spätere Claude-Sitzungen kennen (Skill im Repo).
5. **Code-Beiträge zu reli-hub**: Poutník arbeitet am Prototyp mit, reicht Änderungen als
   Pull Request über Nostr ein (wie Antiope bei edufeed-app), und Jörg mergt sie als Maintainer
   mit seinem Schlüssel. Jeder Commit zeigt, wer ihn geschrieben hat.

**Nicht-Ziele**

- Kein Spiegeln fremder Issues (des edufeed-Teams) in dieses Repo oder nach Forgejo.
- Keine Synchronisation zwischen Forgejo und gitworkshop in irgendeine Richtung.
- Kein Dauerbetrieb, kein Server, kein Polling: Poutník handelt nur, wenn Jörg mit Claude
  arbeitet. Kommt evtl. in späterem Stadium
- Keine Patches (kind 1617) und kein eigener Nostr-Client für Issues, Kommentare, Status oder
  PRs: das alles macht `ngit`. Fällt ngit bei einem PR auf Patches zurück (kein GRASP-06-Dienst
  erreichbar), bricht der Ablauf ab und meldet es, statt 1617-Events zu senden.
- Kein Code-Weg für edufeed-app. Dort schreibt Poutník nur Issues und Kommentare.
- Kein Schreiben nach Forgejo oder GitHub. Poutník hat dort kein Konto und bekommt keines.
  Forgejo-Issues und -Kommentare entstehen weiter wie bisher unter Jörgs Konto (Weboberfläche
  oder das Skript `post_issues.py` im Branch `issue-ueberarbeitung`). Forgejo wird vom Werkzeug
  nur **gelesen** (für die Fäden-Abfrage).

**Anti-Ziele** (das wäre ein Fehlschlag, auch wenn es technisch läuft)

- Ein dritter Arbeitsort entsteht: Markdown-Dateien im Repo, die neben Forgejo und gitworkshop
  gepflegt werden müssen. Entwürfe sind flüchtig und leben nur im Gespräch (und ggf. im
  Scratchpad), bis sie veröffentlicht sind.
- Jörg muss etwas zweimal pflegen oder findet nicht, wo der aktuelle Arbeitsstrang ist.
- Unklar, ob ein Text von Jörg oder von Poutník stammt.
- FOERBICO-Meilensteine und edufeed-app-Entwicklung werden so verbucht, dass Doppelförderung
  im Raum steht (siehe Abschnitt 6).
- Ein Schlüssel liegt im Repo, in einer Umgebungsvariable im Repo oder im Verlauf.

## 3. Rahmenbedingungen (erkundet am 26.10.2026)

**edufeed-app auf Nostr**

- Repo-Koordinate: `30617:1c5ff3caacd842c01dca8f378231b16617516d214da75c7aeabbe9e1efe9c0f6:edufeed-app`
- Repo-Relays laut Ankündigung: `wss://relay.ngit.dev`, `wss://gitnostr.com`,
  `wss://ngit.danconwaydev.com`, `wss://groups.edufeed.org`. Letzteres sperrt bei vielen
  Subscriptions von einer IP („blocked: already 2000 subscriptions from this IP“); es wird
  beim Lesen nicht gebraucht, beim Schreiben nur als eines von vieren.
- Maintainer (werden auf Issues mit `p` markiert): `1c5ff3ca…` (laoc42, Lead),
  `28d7ca9c…` (Antiope, antiope@edufeed.org), `df1a6a03…` (ohne Profil).
- Unter demselben Schlüssel liegen weitere Repos (amb-mcp, index-profile-app,
  edufeed-agent-connect, nope-relay, pyramid-edufeed u. a.). Das Werkzeug muss daher das Ziel-Repo
  über seinen `d`-Tag wählen können, mit `edufeed-app` als Voreinstellung. mdparser liegt
  **nicht** auf Nostr (GitHub edufeed-org/mdparser); mdparser-Issues bleiben Handarbeit.
- **reli-hub** (`30617:1c5ff3ca…:reli-hub`, gitworkshop.dev/laoc.xyz/relay.ngit.dev/reli-hub) ist
  das zweite feste Ziel, angelegt am 27.10.2026 vom Lead-Maintainer (ein Commit, nur README), mit
  denselben vier Relays wie edufeed-app. Maintainer laut Ankündigung: `1c5ff3ca…` (laoc42, Lead),
  `1bf3806b…`, `3c35fc4a…` und **Jörg** (`4fa5d1c4…`). Jörg darf dort
  also Status auf fremde Issues setzen und Code direkt pushen; Poutník ist kein Maintainer.
  Dort entsteht der Prototyp des reli-hubs, zuerst als Weiterarbeit am HTML-Entwurf (Prototyp 5),
  später mit dem Svelte-Stack darauf. Es löst den Neustart aus
  `git.rpi-virtuell.de/Comenius-Institut/hub` ab; die dortigen Issues (#1–#10) werden nicht
  übernommen, sondern bei Bedarf neu gestellt. Maintainer und Relays prüft das Werkzeug beim
  Start aus der Ankündigung (wie bei edufeed-app).
- Issue-Format (Vorlage: `src/lib/helpers/issue-report.js` in edufeed-app):
  kind 1621, Tags `a` (Koordinate, Relay-Hint), `p` je Maintainer (mit Relay-Hint),
  `subject`, `t` je Label, `alt` („Git issue: <subject>“), Inhalt Markdown.
- Kommentar-Format (so wie Antiope es schreibt): kind 1111 nach NIP-22 mit `E`, `K`=1621, `P`
  (Wurzel) und `e`, `k`, `p` (Elternteil), jeweils mit Relay-Hint; bei Antworten auf
  Kommentare zeigt die Kleinbuchstaben-Gruppe auf den Kommentar. Kommentare tragen **kein**
  `a`-Tag auf das Repo; sie sind nur über `#E`/`#e` mit Issue-IDs zu finden.
- Status: kind 1630 (offen), 1631 (erledigt), 1632 (geschlossen), 1633 (Entwurf) mit `e`-Tag
  root; der jüngste Status von Autor oder Maintainer gilt.
- Jörg postet dort bislang mit seinem **Privatschlüssel** `4fa5d1c4…`
  (joerglohrer@joerg-lohrer.de), nicht mit dem FOERBICO-Schlüssel `5a12b41e…`.

**Forgejo (git.rpi-virtuell.de)**

- Offenes Repo `Comenius-Institut/FOERBICO_und_rpi-virtuell`, geschlossenes Repo
  `Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen`.
- API-Token von Jörg in `~/.config/forgejo/token.txt` (nur lesen, nie ausgeben).
- Meilenstein- und Label-IDs sind bekannt (Gedächtnisnotiz forgejo-issues-workflow).
- Was ins geschlossene Repo gehört: Personennamen, persönliche Kommunikation, Secrets.

**Signieren**

- Amber (NIP-46-Bunker) ist der gewünschte Weg: unabhängig vom Browser, mit der Möglichkeit
  der dauerhaften Freigabe. Die Website-Pipeline nutzt das bereits
  (`Website/scripts/blossom-bunker.ts`, `NostrConnectSigner` aus applesauce, feste
  Client-Identität über `CLIENT_SECRET_HEX`, damit Amber nicht bei jedem Lauf fragt).
- `nak` ist auf diesem Rechner kaputt (alle Verbindungen laufen in den Timeout, auch HTTP);
  `ngit`, `n34`, `cargo` sind nicht installiert. Deno ist vorhanden, WebSocket-Abfragen damit
  funktionieren.

**ngit (geprüft am 28.10.2026, Doku ngit.dev, Version 3.0.4 mit macOS-Universal-Binary)**

- `ngit issue create|list|view --comments|comment|close|resolved|reopen|label` und
  `ngit pr list|view|checkout|comment|merge|close|reopen`, alle mit `--json`, `--repo` und
  `--signer <alias|npub>`. Für `git push` wählt `git -c nostr.signer=<alias> push …` den
  Signer. Mehrere Konten pro Rechner über Aliase (`ngit account login --alias …`, auch mit
  Bunker-URL); `ngit account whoami` zeigt sie. Damit entfällt ein eigener Nostr-Client für
  Issues, Kommentare, Status und PRs.
- `ngit pr merge <id>` erzeugt lokal einen No-ff-Merge-Commit und pusht nicht; erst
  `git push origin main` veröffentlicht und markiert den PR als angewendet.
- GRASP-06 (PR-Hosting): Ein Contributor ohne Maintainer-Recht pusht seine PR-Objekte auf
  einen GRASP-Dienst unter `/prs/<eigene npub>/<repo-id>.git`, Ref `refs/nostr/<event-id>`; das
  1618-Event trägt den `clone`-Tag dorthin. Kein Fork, keine Maintainer-Rechte nötig.
  gitnostr.com unterstützt GRASP-06 ausdrücklich. Der Dienst darf nach Größe oder Spam-Regeln
  ablehnen; der Prototyp 5 hat 264 KB.

## 4. Entscheidungen

### 4.1 Zwei Identitäten, zwei Freigabestufen

| | Jörg (Privatschlüssel `4fa5d1c4…`) | Poutník (neuer Schlüssel) |
|---|---|---|
| Wann | Jörg will selbst sprechen und sagt das ausdrücklich | Regelfall für alles, was Claude entwirft |
| Freigabe im Gespräch | ja, Text wird vorher gegengelesen | ja, Text wird vorher gegengelesen |
| Freigabe in Amber | **je Event** am Handy (Einzelfreigabe) | **dauerhaft** (keine Nachfrage) |
| Forgejo | wie bisher, außerhalb dieses Werkzeugs | nicht vorhanden |

Damit ist technisch garantiert: Unter Jörgs Namen erscheint nichts, was er nicht persönlich am
Handy bestätigt hat. Und alles, was Poutník schreibt, ist als Poutník erkennbar.

### 4.2 Poutník als Nostr-Identität

- Der Schlüssel existiert bereits: Jörg hat Poutník am 26.10.2026 in edufeed angelegt.
  `npub1d2g2mkna55ufjnhyxhgwuqldmczsmqrwee954z4pldzlqn04gamstvkeev`
  (hex `6a90adda7da538994ee435d0ee03edde050d806ece4b4a8aa1fb45f04df54777`). Er muss in Amber
  liegen; das Werkzeug kennt nur den Bunker-Link, der Schlüssel steht nie im Repo.
- Profil (kind 0) heute: `name` „Poutník“, Bild auf blossom.edufeed.org, `about` leer, kein
  `bot`-Feld. Die Einrichtung ergänzt (ohne das Bild zu verlieren): `display_name` „Poutník“,
  `about` mit zwei Sätzen (der Pilger aus Comenius' „Labyrinth der Welt und Paradies des
  Herzens“; Agent von Jörg Lohrer; jeder Beitrag ist von Jörg freigegeben), `bot: true`
  (NIP-24; Antiope hat am 09.10.2026 ein Issue für ein Bot-Abzeichen in edufeed angelegt).
  NIP-05-Adresse vorerst keine.
- Relay-Liste (kind 10002) heute: relay.damus.io, nos.lol, relay.edufeed.org. Die Einrichtung
  ergänzt die vier Repo-Relays, damit Antworten an Poutník dort ankommen, wo gitworkshop sie
  sucht.
- Jedes Issue und jeder Kommentar von Poutník sollte Jörg per `p`-Tag markieren. Nachtrag
  28.10.2026: ngit bietet dafür keine Option; Jörg sieht Poutníks Fäden stattdessen immer in
  der Abfrage aus 4.4, die Poutníks Beiträge als Jörgs Seite behandelt.
- Ein Kommentar von Poutník endet nicht mit einer Signaturzeile; die Identität reicht.

### 4.3 Ablauf im Gespräch

1. Jörg beschreibt das Anliegen. Claude entwirft Titel, Text, Labels und schlägt Ziel-Repo
   und Identität vor (edufeed-app als Poutník ist der Regelfall; Jörg als Identität nur auf
   Wunsch). Gehört das Anliegen nach Forgejo, sagt Claude das und entwirft den Text zum
   Einfügen dort, veröffentlicht aber nicht.
2. Der Entwurf wird im Gespräch gezeigt. Keine Datei, kein Commit. Bei längeren Texten darf
   ein Scratchpad-Zwischenstand genutzt werden, der nach dem Veröffentlichen keine Bedeutung
   mehr hat.
3. Jörg gibt frei („veröffentlichen“), gegebenenfalls mit Korrekturen.
4. Claude ruft `ngit --signer poutnik issue create` (bzw. `issue comment`) mit `--json` auf,
   ngit signiert über Amber, veröffentlicht an die Repo-Relays und gibt die Event-ID zurück.
   Claude nennt Jörg den gitworkshop-Link (nevent).
5. Antworten auf ein bestehendes Issue laufen genauso, mit dem Issue (nevent oder
   gitworkshop-URL) als Bezug.

Wenn eine Veröffentlichung scheitert (Bunker antwortet nicht, Relays lehnen ab), bleibt der
Entwurf im Gespräch und wird nicht wiederholt, ohne dass Jörg es sieht.

### 4.4 „Wo stehen meine Fäden?“

Eine Abfrage, keine Datei. Das Werkzeug holt:

- auf Nostr: alle Issues (1621) von Jörg und Poutník in den edufeed-Repos (edufeed-app, reli-hub
  und weitere), dazu alle Kommentare
  (1111) und Status (1630–1633) zu diesen Issue-IDs; außerdem Kommentare von Jörg und Poutník
  auf fremden Issues (per `authors`), und zu diesen die Wurzel-Issues;
- auf Forgejo (nur lesend, mit Jörgs Token): offene Issues beider Repos mit Aktivität im
  Zeitfenster, mit letztem Kommentar.

Ausgabe: eine Liste nach letzter Aktivität, je Faden eine Zeile: Datum, Plattform, Titel,
Status, wer zuletzt was getan hat (Kurzfassung), Link. Dazu eine Hervorhebung „wartet auf dich“
für Fäden, bei denen die letzte Aktivität von jemand anderem stammt. Claude fasst das im
Gespräch zusammen; die Rohliste kann Jörg sehen, wenn er will.

Die Abfrage schont `groups.edufeed.org` (nicht abfragen) und hält die Zahl paralleler
Subscriptions klein (Gedächtnisnotiz edufeed-IP-Sperre).

**Zeitfenster (Entscheidung Claude, nach Reviewer-Rückfrage):** Jörg hat fast alle
Forgejo-Issues selbst angelegt; „alles“ wäre dort die komplette offene Liste. Deshalb zeigt
`threads` standardmäßig nur Fäden mit Aktivität in den letzten 30 Tagen (`--since` änderbar),
auf beiden Plattformen gleich. Auf Forgejo wird die Issue-Liste beider Repos nach `updated`
absteigend geholt und nur für Issues im Zeitfenster der letzte Kommentar nachgeladen; einen
Filter „von mir kommentiert“ bietet die API nicht, er wird deshalb nicht nachgebaut. Poutníks
Beiträge zählen bei „wartet auf dich“ zu Jörgs Seite.

### 4.5 Status setzen (eigene Issues, oder als Maintainer)

Das Werkzeug darf Status-Events (1631 erledigt, 1632 geschlossen, 1630 wieder offen)
schreiben, aber nur mit einer Identität, deren Status NIP-34 anerkennt: der Autor des Issues
oder ein Maintainer des Repos laut Ankündigung. Für Poutník heißt das: nur eigene Issues. Für
Jörg: eigene Issues überall, und in reli-hub alle Issues (dort ist er Maintainer). Das Werkzeug
prüft das vor dem Signieren und lehnt sonst ab (ngit setzt dieselbe Regel durch:
`issue close|resolved|reopen` nur für Autor oder Maintainer). Grund: Jörg kann so eigene erledigte Fäden selbst
schließen, und der Probelauf (4.7) lässt sich sauber aufräumen.

### 4.6 Code-Weg für reli-hub

**Werkzeug:** `ngit` (Dan Conways CLI mit `git-remote-nostr`), installiert über das
Release-Binary von gitworkshop.dev/ngit oder den Ein-Zeilen-Installer, nicht über cargo. Ein
lokaler Klon von reli-hub mit `origin = nostr://laoc.xyz/reli-hub` liegt unter
`~/repositories/reli-hub` (außerhalb dieses Repos). Der Prototyp wird dort als einzelne
HTML-Datei ohne Build weiterentwickelt; das edufeed-Team kennt dieses Muster (edufeed-app
CLAUDE.md: alle Arbeit auf `pr/<slug>`-Branches, Merge über Nostr-PRs).

**Zwei Rollen, zwei Schlüssel, wie bei Issues:**

| Schritt | Identität | Signatur |
|---|---|---|
| Branch `pr/<slug>` anlegen, Commits (Autor „Poutník“) | Poutník | git-Author Poutník |
| Branch pushen = PR öffnen (kind 1618 von ngit erzeugt) | Poutník | Amber, Dauerfreigabe |
| Review: Diff im Gespräch oder auf gitworkshop | Jörg | – |
| Merge nach `main` und Push | Jörg (Maintainer) | Amber, Einzelfreigabe am Handy |

Damit ist auch beim Code technisch garantiert: Auf `main` landet nichts ohne Jörgs Bestätigung
am Handy, und im Verlauf ist an Autor und PR-Event sichtbar, was von Poutník und was von Jörg
stammt. Ein Beitrag, den Jörg selbst schreibt, wird mit seinem git-Author und seinem Schlüssel
gepusht; dann entfällt der PR.

**Ablauf im Gespräch:** Jörg beschreibt die Änderung am Prototyp. Claude arbeitet im Klon auf
einem `pr/`-Branch, zeigt Diff und, wo sinnvoll, die Seite im Browser. Jörg gibt frei. Poutník
pusht den Branch (PR entsteht). Jörg entscheidet, ob er sofort mergt (Claude führt Merge und
Push aus, Amber fragt am Handy) oder den PR erst auf gitworkshop ansieht. Kommentare zum PR
laufen über denselben Kommentar-Weg wie bei Issues (NIP-22 auf das 1618-Event).

**Zwei ngit-Identitäten auf einem Rechner:** ngit kennt Konto-Aliase. Beide Bunker-Links
werden als `poutnik` und `joerg` angemeldet; kein Konto ist Standard. Jeder Push nennt den
Signer ausdrücklich: `git -c nostr.signer=poutnik push -u origin pr/<slug>` bzw.
`git -c nostr.signer=joerg push origin main`. Ein kleines Wrapper-Skript (`tools/poutnik/`)
kapselt beide Aufrufe und lehnt ab, wenn Branch und Signer nicht zusammenpassen (`pr/` nur
poutnik, `main` nur joerg). Ohne Wrapper direkt gepusht wird nicht.

**Poutník ist kein Maintainer, und das reicht:** Nach GRASP-06 landen Poutníks PR-Objekte
unter `/prs/<Poutník-npub>/reli-hub.git` auf einem GRASP-Dienst (gitnostr.com oder
relay.ngit.dev), das PR-Event verweist per `clone`-Tag dorthin, und Jörg holt den Branch mit
`ngit pr checkout <id>`. Kein Fork, keine Maintainer-Rechte für Poutník.

**Freigabe am Handy, konkret:** Beim Push nach `main` signiert ngit das Repo-State-Event
(kind 30618) und je GRASP-Ziel ein HTTP-Auth-Event (kind 27235). Jörgs Bunker-Link in Amber
bekommt Dauerfreigabe für 27235 und Einzelfreigabe für 30618 und für Status-Events
(1630–1633). So ist es ein Tipp am Handy pro Merge, nicht fünf bis zehn, und trotzdem landet
nichts auf `main` ohne Jörgs Bestätigung. Für Issues und Kommentare (1621, 1111) gilt
Einzelfreigabe wie in 4.1.

**Startinhalt:** siehe Abschnitt 8 (Prototyp 5 als `index.html`, erster PR von Poutník).

### 4.7 Probelauf ohne Spuren in den edufeed-Repos

Kein Test-Issue und kein Test-PR in den edufeed-Repos: Antiope greift neue Issues innerhalb
weniger Tage auf. Stattdessen legt **Jörg** einmalig ein kleines Test-Repo auf Nostr an
(`ngit init` mit seinem Schlüssel, `d` = `poutnik-test`, GRASP-Server relay.ngit.dev und
gitnostr.com, Maintainer nur Jörg). Damit haben beide Identitäten im Probelauf genau die
Rollen, die sie in reli-hub haben: Poutník ist Nicht-Maintainer, Jörg ist Maintainer.

Der Probelauf prüft nacheinander: Poutník legt ein Issue an und kommentiert; Jörg
kommentiert; Poutník schließt sein Issue; Jörg öffnet es wieder (Maintainer); Poutník pusht
einen `pr/`-Branch (GRASP-06-Pfad unter Poutníks npub, PR-Event erscheint auf gitworkshop);
Jörg holt ihn mit `ngit pr checkout`, mergt mit `ngit pr merge` und pusht `main` (ein Tipp in
Amber); der PR gilt als angewendet. Zum Schluss wird das Issue geschlossen; das Test-Repo
bleibt für spätere Probeläufe.

### 4.8 Technischer Ort und Konfiguration

- **ngit** erledigt alles, was auf Nostr geschrieben oder gelesen wird: Issues, Kommentare,
  Status, PRs, Merge, Push. Installiert aus dem Release-Binary (`darwin-universal`, Hash im
  Installer), nicht über cargo. Beide Konten als Aliase `poutnik` und `joerg` über ihre
  Bunker-Links; die Bunker-Geheimnisse legt ngit im macOS-Schlüsselbund ab, nicht im Repo.
- **Ein Deno-Werkzeug `tools/poutnik/`** im Repo für das, was ngit nicht kann:
  `threads` (4.4: liest `ngit issue list --json` und `ngit pr list --json` je Repo, dazu
  Kommentare über die Relays per `#E`, und die Forgejo-API; sortiert und markiert „wartet auf
  dich“), der Push-Wrapper aus 4.6 (Branch-/Signer-Prüfung), und ein Aufräum-/Prüfbefehl
  `doctor` (sind beide Konten angemeldet, antworten Bunker, stimmen Relays und Maintainer der
  Repo-Ankündigungen mit der Konfigdatei überein). Es nutzt für Relay-Abfragen dieselben
  Bibliotheken wie `blossom-bunker.ts`, signiert aber selbst nichts.
- Konfiguration außerhalb des Repos in `~/.config/poutnik/env` (chmod 600): Pubkeys beider
  Identitäten, Forgejo-Token-Pfad; Relays und Maintainer je Repo in einer kleinen Konfigdatei
  im Werkzeug, beim Start gegen die Ankündigung (kind 30617) geprüft.
- Ein Skill im Repo (`.claude/skills/poutnik/SKILL.md`) beschreibt die Abläufe aus 4.3, 4.4
  und 4.6 mit den konkreten ngit-Aufrufen und die Regeln aus Abschnitt 6, damit jede
  Claude-Sitzung sie gleich anwendet.
- Tests: Sortierung und „wartet auf dich“ von `threads` sowie die Branch-/Signer-Prüfung des
  Wrappers als Unit-Tests ohne Netz; der Probelauf aus 4.7 gegen die echten Relays.

## 5. Kommentare: Zuordnung und Benachrichtigung

- Poutník antwortet auf gitworkshop als Kommentar unter dem Issue (NIP-22). Ein Kommentar auf
  einen Kommentar bleibt dem Wurzel-Issue zugeordnet (`E`) und zeigt mit `e` auf den
  Elternkommentar.
- Jörg wird auf jedem Poutník-Event mit `p` markiert; Maintainer werden auf Issues mit `p`
  markiert, auf Kommentaren nur der Elternautor und der Wurzelautor (so wie Antiope es tut).
- Auf Forgejo schreibt Poutník nicht.

## 6. Getrennte Projektdoku

Regel, die Claude beim Entwerfen und Veröffentlichen anwendet:

- **Forgejo (FOERBICO)** dokumentiert FOERBICO-Leistungen: Anforderungen, Tests, Konzepte,
  Inhalte, Nachweise je Arbeitspaket. Wo edufeed-app etwas umgesetzt hat, steht ein Verweis auf
  das gitworkshop-Issue als **externe Umsetzung**, nicht als eigene Leistung.
- **gitworkshop (edufeed-app)** beschreibt das Produktanliegen aus Nutzersicht. Keine
  Arbeitspakete, Meilensteine, Fördernummern oder Berichtsbezüge.
- Nichts wird von einer Seite auf die andere kopiert. Synergie wird durch Verweise sichtbar,
  nicht durch doppelte Verbuchung.
- Im Zweifel fragt Claude, bevor es veröffentlicht.

## 7. Was dem Builder überlassen bleibt

- Genaue Befehlsnamen und Parameter des Deno-Werkzeugs, Fehlerbehandlung, Ausgabeformat.
- Wie gemeinsame Relay-Teile aus `blossom-bunker.ts` herausgelöst werden (nur Lesen).
- git-Author-E-Mail für Poutník (Vorschlag: `poutnik@users.noreply.edufeed.org` oder
  npub-basiert), `--no-ff` beim Merge, Verweis in `docs/relihub-prototypen.json` auf die
  reli-hub-Fassung.
- Wie der Skill die Entwurfs-Vorlagen (Issue, Kommentar) formuliert.
- Wie die erste Einrichtung dokumentiert wird (Poutníks Schlüssel in Amber, zwei
  Bunker-Links holen, Profil und Relay-Liste ergänzen, Test-Repo ankündigen, ngit installieren
  und beide Konten verbinden, reli-hub klonen).
- Wie der PR-Probelauf aussieht (ein `pr/`-Branch im Test-Repo aus 4.7, nicht in reli-hub).

## 8. Offene Fragen an Jörg

Keine mehr.

Entschieden am 28.10.2026 (Urheberschaft des Import-Commits): Der Urheber des Prototyps 5,
Jens Dechow (Nostr-Kennung `npub17z39pld9w3z7w872zx0a6cte4s7ezhcy8w69jjzku7d8xv295q8s6dmu40`),
stellt ihn dem Projekt zum Start zur Verfügung und ist mit dem öffentlichen Repo und der
Namensnennung einverstanden; er kann später als Maintainer dazukommen. Festlegung (Claude):
git-Author des Import-Commits ist Jörg Lohrer (er bringt den Entwurf ein), Committer Poutník
(er pusht den PR), der Commit-Text und die README nennen den Urheber mit seiner Kennung. Kein
Co-Authored-By-Trailer (keine E-Mail für das Feld); der Hinweis im Text reicht.

Entschieden am 28.10.2026 (nach dem zweiten Reviewer-Durchlauf, Entscheidungen Claude):
Poutník braucht keine Maintainer-Rechte und keinen Fork, GRASP-06 hostet seine PR-Objekte
unter seiner npub; Jörgs Einzelfreigabe gilt für Repo-State (30618), Status und Issues, die
Auth-Events (27235) sind dauerhaft freigegeben; das Test-Repo liegt unter Jörgs Schlüssel,
damit die Rollen im Probelauf echt sind; ngit ersetzt den eigenen Nostr-Client.

Entschieden am 28.10.2026: Startinhalt für reli-hub ist der Prototyp 5
(`docs/relihub-prototyp_5.html` aus diesem Repo, 264 KB) als `index.html`, dazu die
Konstruktionsbeschreibung als `docs/konstruktion.md`; das ist der erste PR von Poutník. Die
Kopie in diesem Repo bleibt als Archiv für die Werkstatt-Seite (GitHub Pages) liegen. Das
Svelte-Repo `Comenius-Institut/hub` (Stufe 1) wird nicht gelöscht, sondern geparkt, bis der
Svelte-Stack wieder dran ist. Code-Beiträge gehören von Anfang an dazu (4.6).

Entschieden am 26.10.2026: Poutník existiert nur auf Nostr; kein Forgejo-Konto,
kein GitHub-Zugang (mdparser-Issues bleiben Handarbeit). Der Schlüssel ist der heute in
edufeed angelegte (siehe 4.2), Bild vorhanden, NIP-05 vorerst keine. Jörgs Privatschlüssel
liegt bereits in Amber; für das Werkzeug wird dort nur ein zweiter Bunker-Link mit
Einzelfreigabe erzeugt. Zu prüfen bei der Einrichtung: ob Poutníks Schlüssel schon in Amber
ist oder erst importiert werden muss.
