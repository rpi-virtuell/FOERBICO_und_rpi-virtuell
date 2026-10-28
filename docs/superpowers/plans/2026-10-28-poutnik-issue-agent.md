# Poutník Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Issues, Kommentare, Status und Pull Requests aus dem Claude-Gespräch heraus nach gitworkshop (edufeed-app, reli-hub) veröffentlichen, mit der Agenten-Identität Poutník und Jörgs Freigabe, plus eine Live-Abfrage „Wo stehen meine Fäden?“ über gitworkshop und Forgejo.

**Architecture:** `ngit` (v3.0.4) macht alles Schreibende auf Nostr mit zwei Konto-Aliasen `poutnik` und `joerg` (beide als Amber-Bunker). Ein kleines Deno-Werkzeug `tools/poutnik/` liefert, was ngit nicht kann: `threads` (Fäden aus ngit-JSON, Relay-Kommentaren und Forgejo-API), `push` (Wrapper, der Branch und Signer bindet) und `doctor` (Einrichtungsprüfung). Ein Skill in `.claude/skills/poutnik/` legt den Gesprächsablauf fest. Ein einmaliges Setup-Skript ergänzt Poutníks Profil.

**Tech Stack:** Deno 2 (TypeScript, `Deno.test`, `jsr:@std/assert`), `npm:applesauce-signers@^2` + `npm:applesauce-relay@^2` (nur für das Setup-Skript und Relay-Lesen, wie `Website/scripts/blossom-bunker.ts`), `ngit` 3.0.4 (Release-Binary darwin-universal), Forgejo REST API v1, Amber (NIP-46).

**Spec:** `docs/superpowers/specs/2026-10-26-poutnik-issue-agent-design.md`

## Global Constraints

- Kein Schlüssel und kein Bunker-Link im Repo, in Commits oder in Ausgaben. Geheimnisse nur in `~/.config/poutnik/env` (chmod 600) und im macOS-Schlüsselbund (ngit `--secret-storage auto`).
- Poutník-Pubkey hex `6a90adda7da538994ee435d0ee03edde050d806ece4b4a8aa1fb45f04df54777` (npub `npub1d2g2mkna55ufjnhyxhgwuqldmczsmqrwee954z4pldzlqn04gamstvkeev`); Jörg-Pubkey hex beginnt `4fa5d1c413e2b45e10d40bf3562ab701a5331206e359c90baae0e99bfd6c6e41`; Prototyp-Urheber (Jens Dechow) hex `f0a250fda57445e71fca119fdd6179ac3d915f043bb4594856e79a733145a00f`.
- Repo-Koordinaten: `30617:1c5ff3caacd842c01dca8f378231b16617516d214da75c7aeabbe9e1efe9c0f6:edufeed-app` und `…:reli-hub`; Repo-Relays `wss://relay.ngit.dev`, `wss://gitnostr.com`, `wss://ngit.danconwaydev.com`, `wss://groups.edufeed.org`. **Lesend nie `groups.edufeed.org` abfragen** (IP-Sperre), höchstens 3 Relays parallel, eine Subscription je Relay und Abfrage.
- Branch-Regel: `pr/*` wird nur mit Signer `poutnik` gepusht, `main` nur mit `joerg`; alles andere lehnt der Wrapper ab. Kein direkter `git push` ohne Wrapper.
- Keine Patches (kind 1617): meldet ngit beim Push einen Patch-Rückfall, Abbruch mit Fehlermeldung.
- Kein Schreiben nach Forgejo oder GitHub. Forgejo nur lesend mit Token aus `~/.config/forgejo/token.txt`.
- Probeläufe nur im Test-Repo `poutnik-test` (unter Jörgs Schlüssel), nie in edufeed-app oder reli-hub.
- Alle Texte, Befehle, Tests und Kommentare auf Deutsch; Code-Bezeichner Englisch.
- Abweichung von Spec 4.2, erzwungen durch ngit: `ngit issue create|comment` kann kein zusätzliches `p`-Tag auf Jörg setzen. Jörgs Benachrichtigung über Poutníks Beiträge läuft deshalb über `threads` (Poutníks Fäden sind immer enthalten), nicht über gitworkshop-Mentions. Die Spec ist entsprechend ergänzt.
- Jeder Task endet mit einem Commit in diesem Repo (Branch `poutnik`), außer den rein manuellen Einrichtungs-Tasks, die ihre Prüfausgabe dokumentieren.

## Review Focus

1. **Amber nicht erreichbar** (Handy aus, kein Netz): ngit hängt bei „signing event … with remote signer“. Erwartung: `doctor` meldet den Bunker als nicht erreichbar, der Skill sagt, dass Jörg Amber öffnen muss; kein stiller Hänger über Minuten. → Test in Task 7 (`doctor` mit Timeout).
2. **Relay-Drosselung** (`CLOSED … blocked`, Timeout): `threads` darf nicht leer „alles erledigt“ melden. Erwartung: Fäden aus den erreichbaren Quellen plus Warnung je ausgefallener Quelle. → Test in Task 5 (`mergeThreads` mit `warnings`).
3. **Patch-Rückfall beim PR-Push** (kein GRASP-06-Dienst): Erwartung: Abbruch vor dem Senden, Meldung, nichts auf Nostr. → Test in Task 6 (Wrapper erkennt Ausgabe „patch“).
4. **Umlaute und lange Titel** in `--subject`/`--body` und in der Fäden-Ausgabe: Erwartung: unverändert übernommen, keine kaputten Zeichen, Titel gekürzt nur in der Tabellenspalte. → Test in Task 5 (`formatThreadLine` mit „Lizenzpille fehlt … (`/calendar/event/<naddr>`)“).
5. **Forgejo-Token fehlt oder abgelaufen** (401): Erwartung: Nostr-Fäden werden trotzdem gezeigt, Forgejo-Teil mit klarer Warnung. → Test in Task 4 (`fetchForgejoThreads` wirft `ForgejoAuthError`, Task 5 fängt ihn als Warnung).

---

## Dateistruktur

```
tools/poutnik/
  deno.json              # tasks: threads, push, doctor, test; imports
  config.json            # Repos (coordinate, d, relays, maintainers), Identitäten (pubkeys, aliases)
  main.ts                # CLI-Dispatch: threads | push | doctor
  src/config.ts          # loadConfig(): Config; loadEnv(): Env (aus ~/.config/poutnik/env)
  src/relays.ts          # queryRelays(relays, filter, opts): Promise<{events, warnings}>
  src/ngit.ts            # runNgit(args): Promise<unknown>; listIssues(repo, signer); listPrs(repo, signer)
  src/forgejo.ts         # fetchForgejoThreads(since, token): Promise<Thread[]>
  src/threads.ts         # Thread-Typ, mergeThreads(), formatThreadLine(), waitingOnMe()
  src/push.ts            # checkPush(branch, signer): Decision; runPush(...)
  src/doctor.ts          # runDoctor(): Report
  src/*.test.ts          # Unit-Tests ohne Netz
  setup/profile.ts       # Einmalig: Poutníks kind 0 ergänzen (bot:true, about), kind 10002 erweitern
  setup/EINRICHTUNG.md   # Schritte für Jörg (Amber, ngit, Konten, Test-Repo)
.claude/skills/poutnik/SKILL.md
```

Jedes Modul exportiert reine Funktionen, die Netz und Prozesse über injizierbare Parameter bekommen (`run`, `fetch`), damit die Tests ohne Netz laufen.

---

### Task 1: Werkzeuggerüst, Konfiguration, Relay-Lesen

**Files:**
- Create: `tools/poutnik/deno.json`, `tools/poutnik/config.json`, `tools/poutnik/main.ts`, `tools/poutnik/src/config.ts`, `tools/poutnik/src/relays.ts`
- Test: `tools/poutnik/src/config.test.ts`, `tools/poutnik/src/relays.test.ts`

**Interfaces:**
- Produces: `type RepoConfig = { id: string; owner: string; coordinate: string; relays: string[]; readRelays: string[]; maintainers: string[]; web: string }`, `type Identity = { alias: 'joerg'|'poutnik'; pubkey: string }`, `type Config = { repos: Record<string, RepoConfig>; identities: Identity[]; forgejo: { base: string; repos: string[] } }`, `loadConfig(path = <neben main.ts>): Config`, `loadEnv(path = '~/.config/poutnik/env'): Record<string,string>`, `queryRelays(relays: string[], filter: object, opts?: { timeoutMs?: number; max?: number }): Promise<{ events: NostrEvent[]; warnings: string[] }>` (dedupliziert nach id, pro Relay eine Subscription, `readRelays` ohne groups.edufeed.org).

- [ ] **Step 1: Failing tests schreiben**

`config.test.ts`: `loadConfig()` liefert `repos['edufeed-app'].coordinate === '30617:1c5ff3caacd842c01dca8f378231b16617516d214da75c7aeabbe9e1efe9c0f6:edufeed-app'`, `repos['reli-hub'].maintainers` enthält Jörgs hex, `readRelays` enthält kein `groups.edufeed.org`, `identities` hat genau `joerg` und `poutnik` mit 64-stelligen hex-Pubkeys. `loadEnv()` mit einer Temp-Datei `A=1\n#k\nB="x y"` liefert `{A:'1', B:'x y'}`.

`relays.test.ts`: `queryRelays` mit einem injizierten `WebSocket`-Fake (Parameter `opts.socketFactory`), der auf REQ zwei EVENTs (eine id doppelt) und EOSE schickt, liefert 1 Event; ein zweiter Fake, der `["CLOSED","x","blocked"]` schickt, liefert `warnings` mit dem Relay-Namen und `blocked`.

- [ ] **Step 2: Tests laufen lassen, Fehlschlag prüfen**

Run: `cd tools/poutnik && deno test --allow-read --allow-env src/`
Expected: FAIL, Module nicht gefunden.

- [ ] **Step 3: `config.json`, `config.ts`, `relays.ts`, `deno.json`, `main.ts` anlegen**

`config.json` mit beiden Repos (Werte aus Global Constraints; `web` = gitworkshop-URL), `poutnik-test` wird in Task 8 ergänzt. `relays.ts` nach dem Muster des Scratchpad-Skripts aus dem Brainstorming: `WebSocket`, REQ mit zufälliger Sub-ID, Sammeln bis EOSE oder Timeout (Default 15 s), `CLOSED`/`NOTICE` als Warnung. `deno.json`: `"tasks": {"threads": "deno run -A main.ts threads", "push": "deno run -A main.ts push", "doctor": "deno run -A main.ts doctor", "test": "deno test --allow-read --allow-env src/"}`. `main.ts` kennt die drei Befehle und gibt bei unbekanntem Befehl die Hilfe aus (Exit 2).

- [ ] **Step 4: Tests laufen lassen**

Run: `cd tools/poutnik && deno task test`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git checkout -b poutnik
git add tools/poutnik && git commit -m "poutnik: Werkzeuggerüst, Konfiguration und Relay-Lesen"
```

---

### Task 2: ngit installieren und beide Konten anmelden (manuell, mit Prüfung)

**Files:**
- Create: `tools/poutnik/setup/EINRICHTUNG.md`

**Interfaces:**
- Produces: ngit-Aliase `poutnik` und `joerg`, sichtbar in `ngit account whoami --json`; Datei `~/.config/poutnik/env` mit `POUTNIK_PUBKEY_HEX`, `JOERG_PUBKEY_HEX`, `POUTNIK_BUNKER_URL` und `POUTNIK_CLIENT_SECRET_HEX` (beide nur für Task 3; Client-Secret einmalig mit `openssl rand -hex 32` erzeugt), `FORGEJO_TOKEN_FILE=~/.config/forgejo/token.txt`.

- [ ] **Step 1: `EINRICHTUNG.md` schreiben**

Abschnitte, jeweils mit dem Befehl und der erwarteten Ausgabe: (a) ngit installieren: Release `ngit-v3.0.4-universal-apple-darwin.tar.gz` aus dem Installer-Manifest (`curl -Ls https://ngit.dev/install.sh | bash` oder Download + SHA-256-Vergleich mit dem Hash aus dem Manifest), danach `ngit --version` → `3.0.4`, `git-remote-nostr` im PATH. (b) In Amber zwei Bunker-Verbindungen anlegen: für Poutník mit Dauerfreigabe aller Kinds; für Jörg mit Dauerfreigabe nur für kind 27235 (HTTP Auth) und Einzelfreigabe für 1621, 1111, 1630–1633, 30618. (c) Konten anmelden: `ngit account login --bunker-url "<poutnik>" --alias poutnik --offline` und `ngit account login --bunker-url "<joerg>" --alias joerg --offline`, danach `ngit account logout` ohne `--forget`, damit kein Konto Standard ist. (d) `ngit account whoami --json` → beide Aliase mit ihren npubs. (e) `~/.config/poutnik/env` anlegen, `chmod 600`.

- [ ] **Step 2: Jörg führt (a)–(e) aus; Prüfung**

Run: `ngit --version && ngit account whoami --json`
Expected: `3.0.4`; JSON nennt `poutnik` → `npub1d2g2…` und `joerg` → `npub1…` (Jörgs), kein aktives Standardkonto.

- [ ] **Step 3: Commit**

```bash
git add tools/poutnik/setup/EINRICHTUNG.md && git commit -m "poutnik: Einrichtungsanleitung für ngit und beide Konten"
```

---

### Task 3: Poutníks Profil und Relay-Liste ergänzen (Setup-Skript)

**Files:**
- Create: `tools/poutnik/setup/profile.ts`
- Test: `tools/poutnik/setup/profile.test.ts`

**Interfaces:**
- Consumes: `loadEnv`, `queryRelays`, `Config` (Task 1); `NostrConnectSigner` wie in `Website/scripts/blossom-bunker.ts`.
- Produces: `buildProfile(current: Record<string,unknown>): Record<string,unknown>` (behält `picture`, setzt `name` „Poutník“, `display_name` „Poutník“, `bot: true`, `about` = fester Zwei-Satz-Text aus Spec 4.2), `buildRelayList(current: string[][], repoRelays: string[]): string[][]` (vereinigt `r`-Tags, keine Duplikate, bestehende Einträge zuerst).

- [ ] **Step 1: Failing tests schreiben**

`buildProfile({name:'Poutník', picture:'https://blossom.edufeed.org/32e4….png', about:''})` → `picture` unverändert, `bot === true`, `about` beginnt mit „Der Pilger aus Comenius'“. `buildRelayList([['r','wss://relay.damus.io/'],['r','wss://nos.lol/'],['r','wss://relay.edufeed.org/']], repoRelays)` → 7 Einträge, Reihenfolge: die drei alten zuerst, dann die vier Repo-Relays, kein Duplikat bei nochmaligem Aufruf.

- [ ] **Step 2: Fehlschlag prüfen** — Run: `deno test -A setup/` → FAIL.

- [ ] **Step 3: `profile.ts` implementieren**

Ablauf: aktuelles kind 0 und 10002 von `relay.edufeed.org`, `relay-rpi.edufeed.org`, `relay.ngit.dev` lesen (`queryRelays`), Vorschau beider neuen Events auf stdout, Bestätigung per `--yes` oder Rückfrage, Signieren mit `NostrConnectSigner` aus `POUTNIK_BUNKER_URL` + `POUTNIK_CLIENT_SECRET_HEX` (Muster blossom-bunker.ts, feste Client-Identität), Veröffentlichen an die drei edufeed-Relays plus die drei lesbaren Repo-Relays, mindestens 2 OKs. Exit 1, wenn das gelesene kind 0 kein `picture` hat (Schutz gegen leere Überschreibung).

- [ ] **Step 4: Tests laufen lassen** — Run: `deno test -A setup/` → PASS.

- [ ] **Step 5: Einmal ausführen und prüfen**

Run: `deno run -A setup/profile.ts --yes`, danach `deno run -A main.ts doctor` (Task 7) oder vorerst eine Relay-Abfrage: kind 0 von Poutník enthält `"bot":true`, kind 10002 enthält `relay.ngit.dev`.

- [ ] **Step 6: Commit** — `git add tools/poutnik/setup && git commit -m "poutnik: Profil und Relay-Liste per Setup-Skript ergänzen"`

---

### Task 4: Forgejo-Fäden lesen

**Files:**
- Create: `tools/poutnik/src/forgejo.ts`, `tools/poutnik/src/threads.ts` (nur der `Thread`-Typ in diesem Task)
- Test: `tools/poutnik/src/forgejo.test.ts`

**Interfaces:**
- Produces: `type Thread = { source: 'nostr'|'forgejo'; repo: string; kind: 'issue'|'pr'; id: string; title: string; status: 'open'|'resolved'|'closed'|'draft'; createdBy: string; lastActivityAt: number; lastActor: string; lastAction: string; url: string }`, `class ForgejoAuthError extends Error`, `fetchForgejoThreads(opts: { base: string; repos: string[]; token: string; since: Date; fetchFn?: typeof fetch }): Promise<Thread[]>`.

- [ ] **Step 1: Failing tests schreiben**

Mit `fetchFn`-Fake: (a) `GET /api/v1/repos/<repo>/issues?state=open&sort=updated&type=issues&since=<iso>&limit=50` liefert 2 Issues, davon eines mit `updated_at` vor `since` → nur 1 Thread; `lastActor` kommt aus dem letzten Kommentar (`GET /repos/<repo>/issues/<n>/comments` letzter Eintrag), ohne Kommentare aus dem Issue-Autor; `url` = `html_url`. (b) Antwort 401 → wirft `ForgejoAuthError`. (c) Pagination: Header `X-Total-Count` > limit → zweite Seite wird geholt.

- [ ] **Step 2: Fehlschlag prüfen** — Run: `deno task test` → FAIL.

- [ ] **Step 3: `forgejo.ts` implementieren** — Token als `Authorization: token <t>`; `lastAction` = „Kommentar“ bzw. „angelegt“; `createdBy`/`lastActor` = Forgejo-Login.

- [ ] **Step 4: Tests laufen lassen** — Run: `deno task test` → PASS.

- [ ] **Step 5: Commit** — `git add tools/poutnik/src && git commit -m "poutnik: Forgejo-Fäden lesen"`

---

### Task 5: Nostr-Fäden über ngit und Relays, Zusammenführen, `threads`-Befehl

**Files:**
- Create: `tools/poutnik/src/ngit.ts`
- Modify: `tools/poutnik/src/threads.ts`, `tools/poutnik/main.ts`
- Test: `tools/poutnik/src/ngit.test.ts`, `tools/poutnik/src/threads.test.ts`, Fixtures `tools/poutnik/src/fixtures/ngit-issue-list.json`, `ngit-pr-list.json`

**Interfaces:**
- Consumes: `queryRelays`, `fetchForgejoThreads`, `Config`, `loadEnv`.
- Produces: `runNgit(args: string[], run?: (cmd: string[]) => Promise<{code:number; stdout:string; stderr:string}>): Promise<unknown>` (ruft `ngit … --json -d`, wirft bei Exit ≠ 0 mit stderr), `listIssues(repo: RepoConfig, run?): Promise<Thread[]>`, `listPrs(repo: RepoConfig, run?): Promise<Thread[]>`, `fetchComments(issueIds: string[], relays: string[]): Promise<NostrEvent[]>` (Filter `{kinds:[1111], '#E': ids}` in Blöcken zu 50 IDs), `mergeThreads(parts: { threads: Thread[]; warnings: string[] }[], me: string[]): { threads: Thread[]; warnings: string[] }` (sortiert `lastActivityAt` absteigend, `waitingOnMe = lastActor ∉ me`), `formatThreadLine(t: Thread, waiting: boolean): string`, `cmdThreads(argv: string[]): Promise<number>` mit `--since <Tage>` (Default 30), `--json`, `--repo <id>`.

- [ ] **Step 1: Fixtures erzeugen**

Run einmal mit echtem ngit (nach Task 2) in einem Klon von edufeed-app oder mit `--repo nostr://laoc.xyz/edufeed-app`: `ngit issue list --json -d --signer poutnik > src/fixtures/ngit-issue-list.json` und `ngit pr list --json -d --signer poutnik > src/fixtures/ngit-pr-list.json`. Die Fixtures auf je 5 Einträge kürzen; Feldnamen aus der echten Ausgabe übernehmen (die Doku nennt sie nicht).

- [ ] **Step 2: Failing tests schreiben**

`ngit.test.ts`: `listIssues` mit `run`-Fake, der das Fixture liefert, ergibt Threads mit `source:'nostr'`, `kind:'issue'`, `status` aus dem ngit-Statusfeld (`open|resolved|closed|draft`), `url` = `https://gitworkshop.dev/<nevent>` (nevent aus id + author + `relays[0]`, Encoder in `src/nip19.ts` oder `npm:nostr-tools` `nip19.neventEncode`); `runNgit` wirft bei `code:1` mit dem stderr-Text.
`threads.test.ts`: `mergeThreads` sortiert drei Threads nach `lastActivityAt`; `waitingOnMe` ist true, wenn `lastActor` weder Jörg noch Poutník (Pubkeys bzw. Forgejo-Login `joerglohrer`) ist; Warnungen beider Teile werden verkettet; `formatThreadLine` für den Titel „Lizenzpille fehlt auf der Kalender-Event-Seite (`/calendar/event/<naddr>`)“ enthält den Titel unverändert bis 60 Zeichen und dann „…“, Umlaute im Titel „Gästelink in Anrufen“ bleiben erhalten; ein Teil mit leerer Liste und Warnung „relay.ngit.dev: timeout“ führt nicht zu einem leeren Ergebnis, sondern zur Warnung in der Ausgabe.

- [ ] **Step 3: Fehlschlag prüfen** — Run: `deno task test` → FAIL.

- [ ] **Step 4: `ngit.ts`, `threads.ts`, `cmdThreads` implementieren**

`cmdThreads`: für jedes konfigurierte Repo `listIssues` + `listPrs` (Signer `poutnik`, Lese-Operation), auf Autoren Jörg/Poutník filtern **oder** Issues, auf denen einer von beiden kommentiert hat (Kommentare per `fetchComments` über die Issue-IDs der letzten `--since` Tage, `readRelays`, Blöcke zu 50), `lastActivityAt`/`lastActor` aus dem jüngsten Kommentar oder Status; Forgejo-Teil über `fetchForgejoThreads` mit `ForgejoAuthError` → Warnung. Ausgabe: Tabelle `Datum | Quelle | Repo | Titel | Status | zuletzt | Link`, Zeilen mit `waitingOnMe` mit vorangestelltem `→`, danach die Warnungen; `--json` gibt `{threads, warnings}` aus.

- [ ] **Step 5: Tests laufen lassen** — Run: `deno task test` → PASS.

- [ ] **Step 6: Echtlauf** — Run: `deno task threads --since 30`
Expected: Jörgs edufeed-app-Issues vom Oktober (z. B. „Verhältnis von 30023-Beitrag und 30142-AMB-Event festlegen“, offen, zuletzt laoc42 am 22.10.) erscheinen mit `→`; Forgejo-Issues des offenen Repos erscheinen; keine Abfrage an `groups.edufeed.org` (im `-v`-Log).

- [ ] **Step 7: Commit** — `git add tools/poutnik && git commit -m "poutnik: Fäden-Abfrage über ngit, Relays und Forgejo"`

---

### Task 6: Push-Wrapper

**Files:**
- Create: `tools/poutnik/src/push.ts`
- Modify: `tools/poutnik/main.ts`
- Test: `tools/poutnik/src/push.test.ts`

**Interfaces:**
- Produces: `type PushDecision = { ok: true; signer: 'poutnik'|'joerg'; args: string[] } | { ok: false; reason: string }`, `checkPush(branch: string, signer: string): PushDecision`, `detectPatchFallback(output: string): boolean`, `cmdPush(argv: string[], run?): Promise<number>` mit Aufruf `deno task push <branch> --as poutnik|joerg [--cwd <klon>]`.

- [ ] **Step 1: Failing tests schreiben**

`checkPush('pr/prototyp-5', 'poutnik')` → ok, `args` = `['git','-c','nostr.signer=poutnik','push','-u','origin','pr/prototyp-5']`; `checkPush('main','joerg')` → ok mit `push origin main`; `checkPush('pr/x','joerg')` → `ok:false`, reason enthält „pr/“ und „poutnik“; `checkPush('main','poutnik')` → `ok:false`; `checkPush('feature/x','joerg')` → `ok:false` (nur `pr/*` und `main`). `detectPatchFallback('… sending as patches (kind 1617) …')` → true; mit „pull request“ → false. `cmdPush` mit `run`-Fake, dessen stdout Patch-Rückfall enthält → Exit 1 und Meldung „Patch-Rückfall“, **kein** zweiter Aufruf.

- [ ] **Step 2: Fehlschlag prüfen** — Run: `deno task test` → FAIL.

- [ ] **Step 3: `push.ts` implementieren** — Vor dem Push `git rev-parse --abbrev-ref HEAD` muss gleich `branch` sein, sonst Abbruch; Ausgabe von git/ngit durchreichen; Patch-Erkennung auf stdout+stderr (Wörter `patch`, `1617`). Hinweis in der Ausgabe bei `joerg`: „Amber: Freigabe für Repo-State am Handy nötig“.

- [ ] **Step 4: Tests laufen lassen** — Run: `deno task test` → PASS.

- [ ] **Step 5: Commit** — `git add tools/poutnik && git commit -m "poutnik: Push-Wrapper bindet Branch an Signer"`

---

### Task 7: `doctor`

**Files:**
- Create: `tools/poutnik/src/doctor.ts`
- Modify: `tools/poutnik/main.ts`
- Test: `tools/poutnik/src/doctor.test.ts`

**Interfaces:**
- Consumes: `runNgit`, `queryRelays`, `loadConfig`, `loadEnv`.
- Produces: `type Check = { name: string; ok: boolean; detail: string }`, `runDoctor(deps: { run; query; env; config; timeoutMs?: number }): Promise<Check[]>`, `cmdDoctor(argv): Promise<number>` (Exit 1, wenn ein Check fehlschlägt).

- [ ] **Step 1: Failing tests schreiben**

Checks mit Fakes: (a) `ngit --version` ≠ `3.0.4` → Check „ngit“ nicht ok; (b) `ngit account whoami --json` ohne Alias `joerg` → nicht ok, detail nennt den fehlenden Alias; (c) Repo-Ankündigung (kind 30617 per `query`) mit Relays ≠ `config.json` → nicht ok, detail listet die Abweichung; Maintainer-Abweichung ebenso; (d) `env` ohne `FORGEJO_TOKEN_FILE` → nicht ok; (e) Bunker-Erreichbarkeit: `ngit --signer poutnik account whoami` (oder ein harmloser Signierlauf) mit `timeoutMs: 100` und `run`-Fake, der nie antwortet → Check „Amber (poutnik)“ nicht ok mit detail „keine Antwort in 0,1 s“, nicht hängend.

- [ ] **Step 2: Fehlschlag prüfen** — Run: `deno task test` → FAIL.

- [ ] **Step 3: `doctor.ts` implementieren** — Timeout über `Promise.race`; Ausgabe als Liste `✓/✗ name — detail`.

- [ ] **Step 4: Tests laufen lassen** — Run: `deno task test` → PASS.

- [ ] **Step 5: Echtlauf** — Run: `deno task doctor` → alle Checks ✓ (nach Task 2 und 3).

- [ ] **Step 6: Commit** — `git add tools/poutnik && git commit -m "poutnik: doctor prüft ngit, Konten, Bunker, Relays und Ankündigungen"`

---

### Task 8: Test-Repo anlegen und Probelauf (Spec 4.7)

**Files:**
- Modify: `tools/poutnik/config.json` (Repo `poutnik-test`), `tools/poutnik/setup/EINRICHTUNG.md` (Abschnitt Probelauf)
- Create: `tools/poutnik/setup/PROBELAUF.md` (Protokoll mit Event-IDs und Ergebnis)

**Interfaces:**
- Consumes: ngit-Aliase, `deno task push`, `deno task threads`.

- [ ] **Step 1: Test-Repo anlegen (Jörg, einmalig)**

Run in einem neuen leeren Ordner `~/repositories/poutnik-test` mit einem Commit (README):
`ngit --signer joerg init --identifier poutnik-test --name "Poutník Test" --description "Probeläufe für Poutník, kein Inhalt" -g relay.ngit.dev -g gitnostr.com --defaults`
Expected: Ankündigung unter Jörgs Schlüssel, `origin` = `nostr://…/poutnik-test`; Amber fragt einmal (30617) und einmal je Server-Auth, falls nicht dauerhaft freigegeben. `config.json` um `poutnik-test` ergänzen (owner Jörg, maintainers nur Jörg).

- [ ] **Step 2: Issue-Weg proben**

`ngit --signer poutnik issue create --repo nostr://<jörg-npub>/poutnik-test --subject "Probelauf Issue" --body "Testtext mit Umlauten: Gästelink, Lizenzpille" --label test -d --json` → Event-ID notieren; `ngit --signer poutnik issue comment <id> …`; `ngit --signer joerg issue comment <id> …` (Amber: 1 Tipp); `ngit --signer poutnik issue close <id>` (Autor darf); `ngit --signer joerg issue reopen <id>` (Maintainer darf). Gegenprobe: Jörg legt ein zweites Issue an, `ngit --signer poutnik issue close <zweite-id>` muss abgelehnt werden (weder Autor noch Maintainer). Alle Schritte in gitworkshop sichtbar.

- [ ] **Step 3: PR-Weg proben**

Im Klon: Branch `pr/probelauf` mit einem Commit (Author „Poutník <poutnik@users.noreply.edufeed.org>“); `deno task push pr/probelauf --as poutnik --cwd ~/repositories/poutnik-test` → PR erscheint auf gitworkshop, `clone`-Tag des 1618 zeigt auf `/prs/npub1d2g2…/poutnik-test.git`; `ngit --signer joerg pr checkout <id>`; `ngit --signer joerg pr merge <id>`; `deno task push main --as joerg --cwd ~/repositories/poutnik-test` (Amber: 1 Tipp für 30618); PR auf gitworkshop „applied/merged“.

- [ ] **Step 4: Fäden prüfen** — Run: `deno task threads --repo poutnik-test` → Issue und PR mit richtigem Status und `lastActor`.

- [ ] **Step 5: Protokoll und Commit** — Ergebnis mit IDs in `PROBELAUF.md`; `git add tools/poutnik && git commit -m "poutnik: Test-Repo und Probelauf dokumentiert"`

---

### Task 9: Skill für den Gesprächsablauf

**Files:**
- Create: `.claude/skills/poutnik/SKILL.md`

**Interfaces:**
- Consumes: alle Befehle aus Task 5–7, ngit-Aufrufe aus Task 8.

- [ ] **Step 1: SKILL.md schreiben**

Frontmatter `name: poutnik`, `description` (auslösen bei: Issue/Kommentar an edufeed-app oder reli-hub, „wo stehen meine Fäden“, PR für reli-hub, Poutník). Inhalt: (1) Rollenregel aus Spec 4.1 (Regelfall Poutník, Jörg nur auf Wunsch); (2) Ablauf Issue/Kommentar: Entwurf im Gespräch zeigen → Freigabe abwarten → `ngit --signer poutnik issue create|comment … -d --json` → nevent-Link nennen; Vorlagen für Issue (Titel, Problem, Erwartung, Beispiel-Events) und Kommentar; (3) Ablauf Fäden: `deno task threads`, Zusammenfassung mit „wartet auf dich“ zuerst; (4) Ablauf PR reli-hub: Klon `~/repositories/reli-hub`, `pr/<slug>` als Poutník, Diff zeigen, `deno task push pr/<slug> --as poutnik`, Merge nur nach Jörgs Ja: `ngit --signer joerg pr merge <id>` + `deno task push main --as joerg`; (5) Trennregel aus Spec Abschnitt 6 wörtlich; (6) Fehlerfälle: Amber nicht erreichbar → `deno task doctor`; Patch-Rückfall → abbrechen; Relay-Warnungen weitergeben. Keine Schlüssel, keine Bunker-Links im Skill.

- [ ] **Step 2: Prüfen** — Eine frische Claude-Sitzung mit `/poutnik` und der Bitte „Entwirf ein Issue für reli-hub: README beschreibt den Prototyp“ muss den Entwurf zeigen und **vor** dem ngit-Aufruf auf Freigabe warten.

- [ ] **Step 3: Commit** — `git add .claude/skills/poutnik && git commit -m "poutnik: Skill für Issues, Fäden und PRs"`

---

### Task 10: Erster PR: Prototyp 5 nach reli-hub

**Files:**
- Create (in `~/repositories/reli-hub`, außerhalb dieses Repos): `index.html`, `docs/konstruktion.md`, `README.md`
- Modify: `docs/relihub-prototypen.json` (dieses Repo): Feld `relihub` mit der gitworkshop-URL des Repos

**Interfaces:**
- Consumes: Skill (Task 9), Push-Wrapper, ngit-Aliase.

- [ ] **Step 1: Klonen** — `git clone nostr://laoc.xyz/reli-hub ~/repositories/reli-hub` (ngit-Remote-Helfer); `git log` zeigt `d4dce37 Initial commit`.

- [ ] **Step 2: Branch und Inhalt** — `git checkout -b pr/prototyp-5`; `index.html` = Kopie von `docs/relihub-prototyp_5.html` (Byte-gleich, `shasum -a 256` beider Dateien identisch); `docs/konstruktion.md` = Kopie von `docs/relihub-prototyp_5.md`; `README.md`: Titel „reli_hub“, drei Absätze: was der Prototyp ist (eine HTML-Datei ohne Build), Herkunft „Entwurf: Jens Dechow (`npub17z39pld9w3z7w872zx0a6cte4s7ezhcy8w69jjzku7d8xv295q8s6dmu40`), geschenkt zum Start des reli-hub, Oktober 2026“, Hinweis auf `docs/konstruktion.md`. Lizenz: wie dieses Repo (CC BY 4.0 für Inhalte), in der README nennen.

- [ ] **Step 3: Commit** — Author Jörg, Committer Poutník:
`GIT_COMMITTER_NAME=Poutník GIT_COMMITTER_EMAIL=poutnik@users.noreply.edufeed.org git commit --author="Jörg Lohrer <lohrer@comenius.de>" -m "Prototyp 5 des Prototyp-Urhebers Dechow als Startpunkt" -m "Entwurf des Prototyp-Urhebers Dechow (npub17z39…), geschenkt zum Start des reli-hub. Konstruktionsbeschreibung rekonstruiert von Jörg Lohrer."`

- [ ] **Step 4: PR öffnen** — `deno task push pr/prototyp-5 --as poutnik --cwd ~/repositories/reli-hub`; Expected: PR auf gitworkshop.dev/laoc.xyz/relay.ngit.dev/reli-hub, Autor Poutník, 264 KB angenommen (sonst: Review Focus 3, Abbruch und Rücksprache mit laoc42 über die Größenregel des GRASP-Dienstes).

- [ ] **Step 5: Jörg mergt** — nach Jörgs Ja im Gespräch: `ngit --signer joerg pr merge <id>` im Klon auf `main`, `deno task push main --as joerg --cwd ~/repositories/reli-hub` (Amber: 1 Tipp). Expected: `main` auf gitworkshop zeigt `index.html`, PR „merged“.

- [ ] **Step 6: Verweis und Commit hier** — `docs/relihub-prototypen.json`: `"relihub": "https://gitworkshop.dev/laoc.xyz/relay.ngit.dev/reli-hub"`; `git commit -m "Prototypen-Verzeichnis: Verweis auf reli-hub (gitworkshop)"`.

---

### Task 11: Abschluss: Gedächtnis, Branch zusammenführen

**Files:**
- Modify: `~/.claude/projects/…/memory/gitworkshop-edufeed-app.md` (Poutník eingerichtet, Aliase, Test-Repo, Stand), `MEMORY.md`

- [ ] **Step 1: Gedächtnisnotiz ergänzen** — Datum, dass ngit 3.0.4 mit Aliasen `poutnik`/`joerg` läuft, Test-Repo `poutnik-test` unter Jörg, erster PR gemergt (Datum, Commit).
- [ ] **Step 2: Gesamtlauf** — `cd tools/poutnik && deno task test && deno task doctor` → PASS / alle ✓.
- [ ] **Step 3: Branch `poutnik` nach `main` mergen** (Forgejo-PR oder lokal, wie Jörg es möchte) und pushen.
