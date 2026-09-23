"""Giesst die Ergebnisse eines Laufs in Markdown.

Beantwortet genau eine Frage: Was ist in diesem Lauf passiert?

Adressat ist die Redaktion, nicht die Entwicklung — deshalb Deutsch, deshalb
Datei und Zeile statt Stacktrace, und deshalb steht bei jedem Fehler, was zu tun
ist.

Zwei Stufen, weil zwei Leserschaften: `render_brief` fuer einen CI-Lauf — nur
Zaehler und Probleme, damit ein Fehler nicht zwischen 90 Beitraegen untergeht.
`render_summary` fuer den Blick von Hand, mit allen Abschnitten. Welche Stufe,
entscheidet allein `--verbose`; die Umgebung entscheidet nie mit.

`progress_line` ist keine Stufe, sondern die laufende Ausgabe waehrend der
Arbeit: eine Zeile je fertigem Beitrag.

Tut ausdruecklich NICHT: entscheiden, publizieren, den Exit-Code bestimmen.
Der Exit-Code gehoert zu `publish`, hier wird nur berichtet.
"""

from models import Outcome, PostResult, Severity

HABLA = "https://habla.news/a/"
YAKIHONNE = "https://yakihonne.com/article/"


TITEL = "## Nostr-Sync"
PROBELAUF_TITEL = f"{TITEL} — PROBELAUF"
LEERER_LAUF = "\n\nKeine Beitraege zu bearbeiten.\n"


def progress_line(result: PostResult) -> str:
    """Eine Zeile je fertig bearbeitetem Beitrag: Ausgang, Pfad, Slug.

    Ohne sie schweigt ein Lauf ueber 96 Beitraege minutenlang, und niemand kann
    unterscheiden, ob er arbeitet oder haengt.

    Das Label ist auf 15 Zeichen gepolstert (`fehlgeschlagen` ist mit 14 der
    laengste Ausgang), damit Pfad und Slug eine lesbare Spalte bilden. Der Slug
    fehlt bei uebersprungenen Beitraegen — sie kamen nie so weit.

    Fehlgeschlagene und uebersprungene Beitraege tragen ihren Grund mit. Sonst
    ist er in der Kurzfassung **nirgends** zu finden: Den Abschnitt
    *Uebersprungen* gibt es dort nicht, und „16 uebersprungen" beantwortet nicht
    „warum ist mein Beitrag nicht auf Nostr". Bei fehlgeschlagenen macht der
    Grund ausserdem die Abbruchstelle selbsterklaerend.

    Publizierte tragen ihn nicht: Dort steht „dry-run — nichts gesendet", und
    das sagt schon die Kopfzeile des Berichts.
    """
    zeile = f"{result.outcome.value:<15}{result.path}"
    if result.slug:
        zeile += f"  {result.slug}"
    if result.reason and result.outcome in (Outcome.FAILED, Outcome.SKIPPED):
        zeile += f" — {result.reason}"
    return zeile


def render_brief(results: list[PostResult], *, dry_run: bool = False) -> str:
    """Die Kurzfassung fuer einen CI-Lauf: Zaehler, Probleme, sonst nichts.

    Bewusst weggelassen: publizierte und unveraenderte Beitraege, deren
    Adressen und Links, die geaenderten Tags und die Warnungen im Einzelnen.
    Gemessen waren das 498 Zeilen, in denen die vier blockierten Beitraege
    untergingen. Hier bleiben ~11 Zeilen, plus ~8 je blockiertem Beitrag — der
    Bericht waechst also nur im Umfang des Problems.

    Wer alles braucht: `--verbose` oder das Protokoll (`--log`).
    """
    if not results:
        return _titel(dry_run) + LEERER_LAUF

    nach_ausgang = _by_outcome(results)
    teile = _head(results, nach_ausgang, dry_run=dry_run)
    teile += _warning_count(results)
    teile += _failures(nach_ausgang[Outcome.FAILED], only_errors=True)
    return "\n".join(teile)


def _by_outcome(results: list[PostResult]) -> dict:
    return {ausgang: [r for r in results if r.outcome is ausgang] for ausgang in Outcome}


def _head(results: list[PostResult], nach_ausgang: dict, *, dry_run: bool) -> list[str]:
    """Was beide Stufen gemeinsam haben — und in derselben Reihenfolge.

    Gemeinsam, damit die Reihenfolge nicht zwischen den Stufen auseinanderlaeuft:
    Was blockiert, steht immer vor den Zahlen, und die Zahlen vor jeder
    Einzelheit. Der Probelauf-Hinweis steht noch davor — er deutet alles
    darunter um.
    """
    teile = [_titel(dry_run) + "\n"]
    teile += _dry_run_alert(dry_run)
    teile += _caution(nach_ausgang[Outcome.FAILED])
    teile += _silent_noop_warning(results, nach_ausgang)
    teile += _counts(nach_ausgang)
    return teile


def _warning_count(results: list[PostResult]) -> list[str]:
    """Die Warnungen als eine Zahl, mit dem Weg zu den Einzelheiten.

    Bewusst ohne den Satz „Publiziert wurde trotzdem" aus der ausfuehrlichen
    Stufe: Auch fehlgeschlagene Beitraege tragen ihre Konventionsbefunde, dort
    waere die Aussage falsch.
    """
    warnungen = [f for r in results for f in r.findings if f.severity is Severity.WARNING]
    if not warnungen:
        return []
    betroffen = {r.path for r in results if any(
        f.severity is Severity.WARNING for f in r.findings
    )}
    return [
        f"{len(warnungen)} Hinweis(e) zur Datenqualitaet, "
        f"{_beitraege(len(betroffen))} betroffen — vollstaendig mit `--verbose` "
        "oder im Protokoll (`--log`)",
        "",
    ]


def render_summary(results: list[PostResult], *, dry_run: bool = False) -> str:
    """Die ausfuehrliche Stufe: erst was blockiert, dann die Zahlen, dann alles."""
    if not results:
        return _titel(dry_run) + LEERER_LAUF

    nach_ausgang = _by_outcome(results)

    teile = _head(results, nach_ausgang, dry_run=dry_run)
    teile += _failures(nach_ausgang[Outcome.FAILED])
    teile += _warnings(results)
    teile += _published(nach_ausgang[Outcome.PUBLISHED])
    teile += _unchanged(nach_ausgang[Outcome.UNCHANGED])
    teile += _skipped(nach_ausgang[Outcome.SKIPPED])
    return "\n".join(teile)


def _titel(dry_run: bool) -> str:
    return PROBELAUF_TITEL if dry_run else TITEL


def _dry_run_alert(dry_run: bool) -> list[str]:
    """Kennzeichnet den Probelauf — an drei Stellen, nicht nur fett.

    Ohne ihn ist ein Probelauf von einem echten Lauf **nicht zu unterscheiden**:
    In der Kurzfassung gibt es den Abschnitt der publizierten Beitraege nicht,
    und nur dort stand „dry-run — nichts gesendet". Beide Laeufe melden
    „publiziert 19"; bei einem davon ist nichts passiert. Genau der stille
    Erfolg, den CLAUDE.md verbietet.

    `IMPORTANT` und nicht `WARNING` oder `CAUTION`: Die beiden sind belegt —
    rot heisst blockiert, gelb heisst Datenqualitaet. Ein Probelauf ist etwas
    Drittes und bekommt eine dritte Farbe.
    """
    if not dry_run:
        return []
    return [
        "> [!IMPORTANT]",
        "> **Probelauf (`--dry-run`): Es wurde NICHTS gesendet und NICHTS bestaetigt.**",
        "> Die Zahlen unten sagen, was ein echter Lauf tun wuerde.",
        "",
    ]


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


def _failures(failed: list[PostResult], *, only_errors: bool = False) -> list[str]:
    """Die blockierten Beitraege mit allem, was zum Beheben noetig ist.

    `only_errors` fuer die knappe Stufe: `publish.py` haengt einem blockierten
    Beitrag auch seine Konventionswarnungen an (damit die Redaktion beim Oeffnen
    der Datei alles auf einmal sieht). Alle auszugeben brachte den knappen
    Bericht bei vier blockierten Beitraegen zurueck auf ~90 Zeilen.
    """
    if not failed:
        return []
    zeilen = ["### Nicht publiziert", ""]
    for result in failed:
        befunde = [f for f in result.findings
                   if not only_errors or f.severity is Severity.ERROR]
        zeilen.append(f"**{result.path}**")
        if result.reason:
            zeilen.append(f"- {result.reason}")
        zeilen += [f"- {zeile}" for f in befunde for zeile in _finding_lines(f)]
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
    pfade = [f"- `{result.path}` — {finding.message}{_fundstelle(finding)}"
             for result, finding in eintraege]
    return zeilen + [""] + _aufklappbar(pfade)


def _fundstelle(finding) -> str:
    """Zeilen und Fundstellen an die Meldung — sonst bleibt das Suchen bei der Redaktion."""
    teile = []
    if finding.lines:
        teile.append("Zeilen " + ", ".join(str(n) for n in finding.lines))
    if finding.found:
        teile.append(", ".join(finding.found))
    return f" ({' · '.join(teile)})" if teile else ""


def _aufklappbar(zeilen: list[str]) -> list[str]:
    """Legt einen Abschnitt in ein aufklappbares Menue.

    Die langen Abschnitte — 54 publizierte, 25 unveraenderte, 16 uebersprungene —
    wuerden den Bericht sonst so fuellen, dass die blockierten Beitraege darin
    untergehen. Zugeklappt bleibt jede Zeile erhalten und ist einen Klick weit
    entfernt.

    Die Leerzeilen um den Inhalt sind Pflicht: Ohne sie rendert GitHub das
    Markdown innerhalb von `<details>` nicht.
    """
    return ["<details><summary>Betroffene Beiträge</summary>", "", *zeilen, "", "</details>", ""]


def _beitraege(anzahl: int) -> str:
    return f"{anzahl} Beitrag" if anzahl == 1 else f"{anzahl} Beitraege"


def _published(published: list[PostResult]) -> list[str]:
    if not published:
        return []
    eintraege = []
    for result in published:
        eintraege.append(f"**`{result.slug}`**" + _links(result))
        eintraege += _changes(result)
        if result.naddr:
            eintraege.append(f"- `{result.naddr}`")
        eintraege.append(f"- {_bestaetigungen(result)}")
        eintraege.append("")
    return ["### Publiziert", ""] + _aufklappbar(eintraege)


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
    eintraege = [f"- `{r.slug or r.path}`{_links(r)}" for r in unchanged]
    return ["### Unveraendert", ""] + _aufklappbar(eintraege)


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
    eintraege = [f"- `{r.path}` — {r.reason}" for r in skipped]
    return ["### Uebersprungen", ""] + _aufklappbar(eintraege)
