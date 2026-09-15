"""Giesst die Ergebnisse eines Laufs in Markdown.

Beantwortet genau eine Frage: Was ist in diesem Lauf passiert?

Adressat ist die Redaktion, nicht die Entwicklung — deshalb Deutsch, deshalb
Datei und Zeile statt Stacktrace, und deshalb steht bei jedem Fehler, was zu tun
ist.

Tut ausdruecklich NICHT: entscheiden, publizieren, den Exit-Code bestimmen.
Der Exit-Code gehoert zu `publish`, hier wird nur berichtet.
"""

from models import Outcome, PostResult, Severity

HABLA = "https://habla.news/a/"
YAKIHONNE = "https://yakihonne.com/article/"


def render_summary(results: list[PostResult]) -> str:
    """Die Job-Summary: erst was blockiert, dann die Zahlen, dann die Einzelheiten."""
    if not results:
        return "## Nostr-Sync\n\nKeine Beitraege zu bearbeiten.\n"

    nach_ausgang = {
        ausgang: [r for r in results if r.outcome is ausgang] for ausgang in Outcome
    }

    teile = ["## Nostr-Sync\n"]
    teile += _caution(nach_ausgang[Outcome.FAILED])
    teile += _silent_noop_warning(results, nach_ausgang)
    teile += _counts(nach_ausgang)
    teile += _failures(nach_ausgang[Outcome.FAILED])
    teile += _warnings(results)
    teile += _published(nach_ausgang[Outcome.PUBLISHED])
    teile += _skipped(nach_ausgang[Outcome.SKIPPED])
    return "\n".join(teile)


def _caution(failed: list[PostResult]) -> list[str]:
    if not failed:
        return []
    return [
        "> [!CAUTION]",
        f"> **{len(failed)} Beitrag(e) wurden nicht publiziert.** Einzelheiten unten.",
        "",
    ]


def _silent_noop_warning(results: list[PostResult], nach_ausgang: dict) -> list[str]:
    """Der Fall, der frueher gruen durchlief, ohne dass etwas ankam."""
    if nach_ausgang[Outcome.PUBLISHED] or nach_ausgang[Outcome.UNCHANGED]:
        return []
    return [
        "> [!WARNING]",
        f"> **{len(results)} Beitrag(e) angesehen, aber nichts publiziert und nichts bestaetigt.**",
        "> Auf den Relays hat sich nichts geaendert. Gruende unten.",
        "",
    ]


def _counts(nach_ausgang: dict) -> list[str]:
    zeilen = ["| Ausgang | Anzahl |", "|---|---|"]
    zeilen += [f"| {a.value} | {len(r)} |" for a, r in nach_ausgang.items()]
    return zeilen + [""]


def _failures(failed: list[PostResult]) -> list[str]:
    if not failed:
        return []
    zeilen = ["### Nicht publiziert", ""]
    for result in failed:
        zeilen.append(f"**{result.path}**")
        if result.reason:
            zeilen.append(f"- {result.reason}")
        zeilen += [f"- {zeile}" for f in result.findings for zeile in _finding_lines(f)]
        zeilen.append("")
    return zeilen


def _finding_lines(finding) -> list[str]:
    zeilen = [f"{finding.origin}: {finding.message}"]
    if finding.lines:
        zeilen.append("  Zeilen: " + ", ".join(str(n) for n in finding.lines))
    if finding.found:
        zeilen.append("  Gefunden: " + ", ".join(finding.found))
    if finding.rule:
        zeilen.append(f"  Regel: {finding.rule}")
    if finding.fix:
        zeilen.append(f"  Fix: {finding.fix}")
    return zeilen


def _warnings(results: list[PostResult]) -> list[str]:
    mit_warnung = [
        (r, [f for f in r.findings if f.severity is Severity.WARNING]) for r in results
    ]
    mit_warnung = [(r, f) for r, f in mit_warnung if f]
    if not mit_warnung:
        return []

    zeilen = [
        "> [!WARNING]",
        f"> **{len(mit_warnung)} Beitrag(e) mit Hinweisen zur Datenqualitaet.** Publiziert wurde trotzdem.",
        "",
        "### Zur Nacharbeit",
        "",
    ]
    for result, findings in mit_warnung:
        zeilen.append(f"**{result.path}**")
        zeilen += [f"- {f.origin}: {f.message}" for f in findings]
        zeilen.append("")
    return zeilen


def _published(published: list[PostResult]) -> list[str]:
    if not published:
        return []
    zeilen = ["### Publiziert", ""]
    for result in published:
        zeilen.append(f"**`{result.slug}`**" + _links(result))
        zeilen += _changes(result)
        zeilen.append("")
    return zeilen


def _links(result: PostResult) -> str:
    if not result.naddr:
        return ""
    return (f" — [Habla]({HABLA}{result.naddr}) · "
            f"[Yakihonne]({YAKIHONNE}{result.naddr}) · `{result.naddr}`")


def _changes(result: PostResult) -> list[str]:
    """Zeigt, was sich gegenueber dem Relay aendern wuerde.

    Ohne das laesst sich die Cutover-Vorgabe „jede Abweichung einzeln pruefen"
    nur mit einem eigenen Skript erfuellen — also gar nicht.
    """
    if result.existing is None:
        return ["- neu auf dem Relay (bisher kein Event zu diesem Slug)"]
    if result.article is None:
        return []

    neu, bisher = result.article["tags"], result.existing["tags"]
    zeilen = []
    for a, b in zip(neu, bisher):
        if a != b:
            zeilen.append(f"- `{a[0]}`: neu {a[1:]} · bisher {b[1:]}")
    if len(neu) != len(bisher):
        zeilen.append(f"- Tag-Anzahl: neu {len(neu)} · bisher {len(bisher)}")
    if result.article.get("content") != result.existing.get("content"):
        zeilen.append("- der Fliesstext hat sich geaendert")
    return zeilen or ["- nur `created_at` — inhaltlich gleich"]


def _skipped(skipped: list[PostResult]) -> list[str]:
    if not skipped:
        return []
    zeilen = ["### Uebersprungen", ""]
    zeilen += [f"- `{r.path}` — {r.reason}" for r in skipped]
    return zeilen + [""]
