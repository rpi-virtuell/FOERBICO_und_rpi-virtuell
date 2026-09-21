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
    teile += _unchanged(nach_ausgang[Outcome.UNCHANGED])
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
    """Die Datenqualitaets-Hinweise, nach Regel gebuendelt.

    Nach Regel und nicht nach Beitrag, weil dieselbe Konvention 60 Beitraege
    betrifft: eine Liste je Beitrag wuerde alles andere aus der Summary
    draengen. Die vollstaendigen Befunde stehen im Log-Artefakt (`--log`).
    """
    gruppen = _by_rule(results)
    if not gruppen:
        return []

    betroffen = {r.path for eintraege in gruppen.values() for r, _ in eintraege}
    zeilen = [
        "> [!WARNING]",
        f"> **{_beitraege(len(betroffen))} mit Hinweisen zur Datenqualitaet.** "
        "Publiziert wurde trotzdem.",
        "",
        "### Zur Nacharbeit",
        "",
    ]
    for (origin, rule, fix), eintraege in gruppen.items():
        zeilen += _warning_group(origin, rule, fix, eintraege)
    return zeilen


def _by_rule(results: list[PostResult]) -> dict:
    """Warnungen nach Herkunft, Regel und Fix — alles, was eine Nacharbeit ausmacht.

    Der Fix gehoert in den Schluessel: Fehlende und abweichende Schlagworte
    verletzen dieselbe Regel, sind aber verschieden zu beheben.
    """
    gruppen: dict = {}
    for result in results:
        for finding in result.findings:
            if finding.severity is not Severity.WARNING:
                continue
            schluessel = (finding.origin, finding.rule, finding.fix)
            gruppen.setdefault(schluessel, []).append((result, finding))
    return gruppen


def _warning_group(origin: str, rule: str, fix: str, eintraege: list) -> list[str]:
    betroffen = {result.path for result, _ in eintraege}
    zeilen = [f"**{_beitraege(len(betroffen))}** — {origin}"]
    if rule:
        zeilen.append(f"- Regel: {rule}")
    if fix:
        zeilen.append(f"- Fix: {fix}")
    zeilen += ["", "<details><summary>Betroffene Beitraege</summary>", ""]
    for result, finding in eintraege:
        zeilen.append(f"- `{result.path}` — {finding.message}{_fundstelle(finding)}")
    return zeilen + ["", "</details>", ""]


def _fundstelle(finding) -> str:
    """Zeilen und Fundstellen an die Meldung — sonst bleibt das Suchen bei der Redaktion."""
    teile = []
    if finding.lines:
        teile.append("Zeilen " + ", ".join(str(n) for n in finding.lines))
    if finding.found:
        teile.append(", ".join(finding.found))
    return f" ({' · '.join(teile)})" if teile else ""


def _beitraege(anzahl: int) -> str:
    return f"{anzahl} Beitrag" if anzahl == 1 else f"{anzahl} Beitraege"


def _published(published: list[PostResult]) -> list[str]:
    if not published:
        return []
    zeilen = ["### Publiziert", ""]
    for result in published:
        zeilen.append(f"**`{result.slug}`**" + _links(result))
        zeilen += _changes(result)
        if result.naddr:
            zeilen.append(f"- `{result.naddr}`")
        zeilen.append(f"- {_bestaetigungen(result)}")
        zeilen.append("")
    return zeilen


def _bestaetigungen(result: PostResult) -> str:
    """Was das Relay bestaetigt hat — oder warum nichts zu bestaetigen war.

    Ohne diese Zeile heisst „publiziert" nur „wir haben es versucht". Im Dry-Run
    steht hier der Grund statt einer Null, denn 0 Bestaetigungen saehen aus wie
    ein Fehlschlag.
    """
    if result.acks:
        return f"{result.acks} Relay-Bestaetigung(en)"
    return result.reason or "keine Bestaetigung"


def _unchanged(unchanged: list[PostResult]) -> list[str]:
    """Die unveraenderten beim Namen nennen, nicht nur zaehlen.

    „59 unveraendert" ist keine Aussage darueber, *welche* — und genau das ist
    beim Abnehmen eines Laufs die Frage. Eingeklappt, damit es den Bericht nicht
    dominiert.
    """
    if not unchanged:
        return []
    zeilen = [
        "### Unveraendert", "",
        f"<details><summary>{_beitraege(len(unchanged))} lagen bereits so auf dem Relay</summary>",
        "",
    ]
    zeilen += [f"- `{r.slug or r.path}`{_links(r)}" for r in unchanged]
    return zeilen + ["", "</details>", ""]


def _links(result: PostResult) -> str:
    if not result.naddr:
        return ""
    return f" — [Habla]({HABLA}{result.naddr}) · [Yakihonne]({YAKIHONNE}{result.naddr})"


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
            zeilen.append(f"- `{a[0]}`: {_tag_unterschied(a, b)}")
    if len(neu) != len(bisher):
        zeilen.append(f"- Tag-Anzahl: neu {len(neu)} · bisher {len(bisher)}")
    if result.article.get("content") != result.existing.get("content"):
        zeilen.append("- der Fliesstext hat sich geaendert")
    return zeilen or ["- nur `created_at` — inhaltlich gleich"]


def _tag_unterschied(neu: list, bisher: list) -> str:
    """Nur die Stellen, an denen sich zwei Tags unterscheiden.

    Der `summary`-Tag traegt 700 Zeichen Text und die Sprache als letztes
    Element. Beides auszugeben, um einen Buchstaben zu zeigen, verdeckt genau
    die Aenderung, die gemeldet werden soll. Das vollstaendige Event steht im
    Log-Artefakt (`--log`).
    """
    if len(neu) != len(bisher):
        return f"neu {neu[1:]} · bisher {bisher[1:]}"

    teile = []
    for stelle, (a, b) in enumerate(zip(neu, bisher)):
        if a != b:
            teile.append(f"Wert {stelle}: neu {a!r} · bisher {b!r}")
    return " · ".join(teile)


def _skipped(skipped: list[PostResult]) -> list[str]:
    if not skipped:
        return []
    zeilen = ["### Uebersprungen", ""]
    zeilen += [f"- `{r.path}` — {r.reason}" for r in skipped]
    return zeilen + [""]
