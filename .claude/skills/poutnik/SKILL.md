---
name: poutnik
description: Issues, Kommentare, Status und Pull Requests für die edufeed-Repos auf Nostr (edufeed-app, reli-hub auf gitworkshop.dev) aus dem Gespräch heraus veröffentlichen, als Agenten-Identität Poutník oder auf Wunsch als Jörg, und die Frage „Wo stehen meine Fäden?“ über gitworkshop und Forgejo beantworten. Auslösen bei: Issue oder Kommentar für edufeed-app oder reli-hub, Antwort an das edufeed-Team, PR oder Code für reli-hub, Poutník, Fäden, Arbeitsstrang, „was ist offen“.
---

# Poutník: Arbeiten mit gitworkshop und reli-hub

Spec: `docs/superpowers/specs/2026-10-26-poutnik-issue-agent-design.md`. Werkzeug: `tools/poutnik/` (Deno) neben `ngit` 3.0.4 mit den Konto-Aliasen `poutnik` und `joerg` (beide Amber-Bunker). Keine Schlüssel, keine Bunker-Links in Dateien oder im Gespräch.

## 1. Rollen

- **Poutník** ist der Regelfall für alles, was Claude entwirft: Issues, Kommentare, PRs. Signer `poutnik` (Amber: Dauerfreigabe).
- **Jörg** nur, wenn er ausdrücklich selbst sprechen will. Signer `joerg` (Amber: Einzelfreigabe am Handy, ein Tipp pro Event).
- Repos: `edufeed-app` (Issues, Kommentare) und `reli-hub` (Issues, Kommentare, Code). Poutník ist nirgends Maintainer. Ob Jörg in reli-hub bestätigter Maintainer ist, zeigt `deno task doctor` (Ankündigung) bzw. `ngit repo` im Klon; Seit 28.10.2026 ist Jörg dort bestätigter Co-Maintainer (gegenseitige Ankündigungen mit laoc42). Fällt das weg (Lead-Ankündigung ohne Jörg), wird ein Push nach `main` abgewiesen; dann muss der Lead-Maintainer ihn erneut eintragen (`ngit repo edit --add-maintainer <npub>`) und Jörg `ngit --signer joerg repo accept -d` ausführen. Der PR bleibt derweil offen für das edufeed-Team.
- Forgejo (git.rpi-virtuell.de) wird nur gelesen. Issues und Kommentare dort entstehen wie bisher unter Jörgs Konto, nicht über Poutník.

## 2. Issue oder Kommentar veröffentlichen

1. Entwurf im Gespräch zeigen: Titel, Text (Markdown), Labels, Ziel-Repo, Identität. Keine Datei, kein Commit.
2. **Auf Jörgs Freigabe warten** („veröffentlichen“). Ohne Freigabe nichts senden.
3. Veröffentlichen:

```bash
cd tools/poutnik
ngit --signer poutnik issue create --repo nostr://laoc.xyz/edufeed-app --subject "<Titel>" --body "<Text>" --label <label> -d --json
ngit --signer poutnik issue comment --repo nostr://laoc.xyz/edufeed-app <nevent|id> --body "<Text>" -d --json
ngit --signer poutnik pr comment --repo nostr://laoc.xyz/reli-hub <nevent|id> --body "<Text>" -d --json
```

   `--repo` akzeptiert `nostr://laoc.xyz/<repo>`; für reli-hub entsprechend. Bei `--as jörg` den Signer `joerg` nehmen und Jörg sagen, dass Amber am Handy fragt.
4. Den gitworkshop-Link nennen: `https://gitworkshop.dev/<nevent>` (nevent aus der JSON-Ausgabe).
5. Status nur für eigene Issues (Poutník) bzw. als Maintainer (Jörg in reli-hub): `ngit --signer <alias> issue close|resolved|reopen <id>`.

**Vorlage Issue:** Titel in einer Zeile; Absätze „Beobachtung“ (was passiert, mit Route/URL), „Erwartung“, „Beispiel“ (Event-IDs, naddr, Screenshots als Blossom-Link), „Vorschlag“ (optional). Deutsch, Nutzersicht, keine Arbeitspakete oder Meilensteine (Abschnitt 5).

**Vorlage Kommentar:** Bezug in einem Satz, dann Inhalt, ggf. Rückfrage. Keine Signaturzeile.

## 3. „Wo stehen meine Fäden?“

```bash
cd tools/poutnik && deno task threads --since 30        # oder --repo reli-hub, --json
```

Zusammenfassen: zuerst die Zeilen mit `→` (wartet auf Jörg), dann der Rest, Warnungen am Ende weitergeben. Link je Faden nennen. Poutníks Beiträge zählen als Jörgs Seite.

## 4. Code für reli-hub (Pull Request)

Klon: `~/repositories/reli-hub` (`git clone nostr://laoc.xyz/reli-hub`). Alle Arbeit auf `pr/<slug>` ab `main`.

1. Branch anlegen, Änderung umsetzen, Commits mit Author **Poutník** (`Poutník <poutnik@users.noreply.edufeed.org>`). Beiträge des Prototyp-Urhebers oder Jörgs mit deren Author.
2. Diff zeigen (und die Seite im Browser, wenn sinnvoll). **Auf Jörgs Freigabe warten.**
3. PR öffnen (nur über den Wrapper, nie `git push` direkt):

```bash
cd tools/poutnik && deno task push pr/<slug> --as poutnik --cwd ~/repositories/reli-hub
```

   Der Wrapper bricht bei Patch-Rückfall (kind 1617) ab. Dann nicht wiederholen, sondern Jörg melden.
4. Merge nur nach Jörgs Ja. Jörg kann den PR vorher auf gitworkshop ansehen.

```bash
cd ~/repositories/reli-hub && git checkout main && git -c nostr.signer=joerg fetch origin && git merge --ff-only origin/main && ngit --signer joerg pr merge <id>
cd tools/poutnik && deno task push main --as joerg --cwd ~/repositories/reli-hub      # Amber fragt am Handy (kind 30618)
```

## 5. Getrennte Projektdoku (immer anwenden)

- Forgejo (FOERBICO) dokumentiert FOERBICO-Leistungen: Anforderungen, Tests, Konzepte, Inhalte, Nachweise je Arbeitspaket. Wo edufeed-app etwas umgesetzt hat, steht ein Verweis auf das gitworkshop-Issue als externe Umsetzung, nicht als eigene Leistung.
- gitworkshop (edufeed-app, reli-hub) beschreibt das Produktanliegen aus Nutzersicht. Keine Arbeitspakete, Meilensteine, Fördernummern oder Berichtsbezüge.
- Nichts wird von einer Seite auf die andere kopiert. Synergie wird durch Verweise sichtbar, nicht durch doppelte Verbuchung. Im Zweifel vor dem Veröffentlichen fragen.

## 6. Fehlerfälle

- ngit hängt bei „signing event … with remote signer“: Amber am Handy nicht erreichbar. `deno task push` bricht nach `--timeout` (Standard 180 s) ab; `deno task doctor` prüft Konten und Ankündigungen, aber nicht Amber selbst. Jörg bitten, Amber zu öffnen, dann den Stand auf gitworkshop prüfen, bevor etwas wiederholt wird.
- `threads` meldet Warnungen (Timeout, blocked): Ergebnis trotzdem zeigen, Warnung nennen. `groups.edufeed.org` wird nie lesend abgefragt.
- Patch-Rückfall beim Push: abbrechen, melden (Spec: keine kind 1617).
- Probeläufe nur im Test-Repo `poutnik-test` (unter Jörgs Schlüssel), nie in edufeed-app oder reli-hub.
