# Probelauf 28.10.2026 (Spec 4.7)

Test-Repo `poutnik-test` unter Jörgs Schlüssel, Maintainer nur Jörg; Poutník ist dort wie in reli-hub Nicht-Maintainer.
gitworkshop: https://gitworkshop.dev/npub1f7jar3qnu269uyx5p0e4v24hqxjnxysxudvujza2ur5ehltvdeqsly2fx9/relay.ngit.dev/poutnik-test

| Schritt | Identität | Ergebnis |
|---|---|---|
| `ngit init` (Ankündigung, main-Push) | joerg | ok, Status an 2/3 Relays (nos.lol fehlt, unkritisch) |
| Issue „Probelauf Issue“ anlegen | poutnik | ok, ohne Amber-Nachfrage (Dauerfreigabe) |
| Kommentar | poutnik | ok |
| Kommentar | joerg | ok, 1 Amber-Tipp |
| Issue schließen (eigenes) | poutnik | ok |
| Issue wieder öffnen (Maintainer) | joerg | ok, 1 Amber-Tipp |
| Zweites Issue anlegen | joerg | ok |
| Fremdes Issue schließen | poutnik | **abgelehnt** von ngit: „only the issue author or a repository member …“ |
| Branch `pr/probelauf`, Commit Author Poutník, `deno task push pr/probelauf --as poutnik` | poutnik | ok: Objekte als `refs/nostr/<event-id>` auf relay.ngit.dev und gitnostr.com (GRASP-06), PR-Event an 4/5 Relays, kein Patch-Rückfall |
| `ngit pr merge <id>` auf main | joerg | ok, No-ff-Merge-Commit lokal |
| `deno task push main --as joerg` | joerg | ok, 1 Amber-Tipp (kind 30618), Status „applied“ an 4/5 Relays |
| `deno task threads --repo poutnik-test` | – | PR resolved (Jörg: erledigt), beide Issues mit richtigem Stand und Akteur |
| Aufräumen: beide Issues schließen | poutnik / joerg | ok |

Event-IDs und Rohausgaben: `.superpowers/sdd/2026-10-28-poutnik-issue-agent/probelauf-log.txt` (nicht im Repo).

Erkenntnisse:
- `ngit issue list`/`pr list` zeigen nur offene Einträge und keine Zeitstempel; die Fäden-Abfrage liest deshalb direkt von den Relays.
- nos.lol lehnt Schreibzugriffe von hier regelmäßig ab; für die Repo-Relays ohne Bedeutung.
- Der Wrapper wertet einen `pr/`-Push nur dann als Erfolg, wenn ngit „proposal as PR event“/„Published N PR“ meldet; die Patch-Erkennung ist eng gefasst (`kind 1617`, „as patches“), damit Hex-IDs und Branch-Namen nicht anschlagen (Review I1). Sie läuft nach dem Push, kann also nichts verhindern, nur ehrlich melden („auf gitworkshop prüfen“).
- Offen (Review I3): Ein Negativ-Probelauf mit ausgeschaltetem Handy (Flugmodus) für `deno task push --timeout 30` und `doctor` steht noch aus; `doctor` prüft Amber nicht, nur die ngit-Konten.
- reli-hub, 28.10. ab 12:16: Jörgs `ngit repo accept` veröffentlicht; 15 s später neue Lead-Ankündigung von laoc42 nur mit laoc42 und `1bf3806b…` → Jörg nicht bestätigt, Push nach main abgewiesen („not a confirmed maintainer“). PR `pr/prototyp-5` bleibt offen, Merge-Commit 46ff367 lokal.
