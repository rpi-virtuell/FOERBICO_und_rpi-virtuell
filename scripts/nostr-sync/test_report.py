from models import Finding, Outcome, PostResult, Severity
from report import render_summary


def ergebnis(outcome, **kwargs):
    return PostResult(path=kwargs.pop("path", "posts/ein-beitrag/index.md"), outcome=outcome, **kwargs)


def test_the_summary_counts_every_outcome():
    text = render_summary([
        ergebnis(Outcome.PUBLISHED, slug="a"),
        ergebnis(Outcome.PUBLISHED, slug="b"),
        ergebnis(Outcome.UNCHANGED, slug="c"),
        ergebnis(Outcome.SKIPPED, reason="Pflichtfelder fehlen"),
        ergebnis(Outcome.FAILED, slug="d", reason="Relay nicht abfragbar"),
    ])

    assert "| publiziert | 2 |" in text
    assert "| unveraendert | 1 |" in text
    assert "| uebersprungen | 1 |" in text
    assert "| fehlgeschlagen | 1 |" in text


def test_a_failure_shows_file_lines_rule_and_fix():
    """Die Meldung muss ohne Rueckfrage behebbar sein."""
    befund = Finding(
        severity=Severity.ERROR, origin="NIP-23", message="HTML im content",
        rule='NIP-23 — "MUST NOT support adding HTML to Markdown"',
        fix="Tag entfernen; fuer einen Absatz eine Leerzeile setzen.",
        lines=[70, 92], found=["<br>", "</br>"],
    )
    text = render_summary([
        ergebnis(Outcome.FAILED, path="posts/loewe/index.md", slug="loewe", findings=[befund])
    ])

    assert "posts/loewe/index.md" in text
    assert "70, 92" in text
    assert "MUST NOT" in text
    assert "Leerzeile" in text
    assert "<br>" in text


def test_failures_are_flagged_as_caution_at_the_top():
    text = render_summary([ergebnis(Outcome.FAILED, slug="x", reason="kaputt")])

    assert "[!CAUTION]" in text
    assert text.index("[!CAUTION]") < text.index("| publiziert |")


def test_warnings_get_their_own_visible_section():
    warnung = Finding(
        severity=Severity.WARNING, origin="FOERBICO-Konvention",
        message="Schlagworte erreichen Nostr nicht",
    )
    text = render_summary([ergebnis(Outcome.PUBLISHED, slug="x", findings=[warnung])])

    assert "[!WARNING]" in text
    assert "Schlagworte erreichen Nostr nicht" in text


def test_a_published_post_shows_its_address_for_looking_at():
    text = render_summary([
        ergebnis(Outcome.PUBLISHED, slug="ein-beitrag", naddr="naddr1qq3x5atnwskkx")
    ])

    assert "naddr1qq3x5atnwskkx" in text
    assert "habla.news/a/naddr1qq3x5atnwskkx" in text


def test_a_run_that_published_nothing_despite_candidates_is_called_out():
    """Der Fall, den die alte Loesung nur nachtraeglich meldete.

    Dateien lagen im Diff, publiziert wurde nichts — gruen durchgelaufen, auf
    Nostr kam nichts an.
    """
    text = render_summary([
        ergebnis(Outcome.SKIPPED, reason="Pflichtfelder fehlen"),
        ergebnis(Outcome.SKIPPED, reason="Pflichtfelder fehlen"),
    ])

    assert "nichts publiziert" in text


def test_an_empty_run_says_so_plainly():
    assert "Keine Beitraege" in render_summary([])
