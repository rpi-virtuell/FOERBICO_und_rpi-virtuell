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


def test_a_dry_run_shows_which_tags_would_change():
    """Damit „jede Abweichung einzeln pruefen" mit dem Werkzeug selbst geht."""
    neu = {"kind": 30023, "tags": [["d", "x"], ["inLanguage", "de"]], "content": "Text"}
    live = {"kind": 30023, "tags": [["d", "x"], ["inLanguage", "d"]], "content": "Text"}

    text = render_summary([
        ergebnis(Outcome.PUBLISHED, slug="x", article=neu, existing=live)
    ])

    assert "inLanguage" in text
    assert '"de"' in text or "'de'" in text
    assert "neu" in text.lower() and "bisher" in text.lower()


def test_a_post_without_a_live_event_is_named_as_new():
    neu = {"kind": 30023, "tags": [["d", "x"]], "content": "Text"}

    text = render_summary([ergebnis(Outcome.PUBLISHED, slug="x", article=neu, existing=None)])

    assert "neu" in text.lower()


def warnung(message, rule="Schlagworte gehoeren nach `commonMetadata.keywords`.", **kwargs):
    return Finding(
        severity=Severity.WARNING, origin="FOERBICO-Konvention (schlagworte.yaml)",
        message=message, rule=rule, **kwargs
    )


def test_warnings_of_the_same_rule_are_counted_not_repeated():
    """Bei 60 betroffenen Beitraegen darf nicht 60-mal dieselbe Regel dastehen.

    Ein Zaehler, die Regel einmal, darunter die Pfade — je Pfad die eigene
    Meldung, weil sie das betroffene Feld bzw. die Anzahl nennt. Die
    vollstaendigen Befunde stehen im Log-Artefakt (`--log`).
    """
    ergebnisse = [
        ergebnis(Outcome.UNCHANGED, path=f"posts/{i}/index.md", slug=str(i),
                 findings=[warnung("Schlagworte erreichen Nostr nicht")])
        for i in range(60)
    ]

    text = render_summary(ergebnisse)

    assert "60 Beitraege" in text
    assert text.count("Schlagworte gehoeren nach `commonMetadata.keywords`.") == 1
    assert all(f"posts/{i}/index.md" in text for i in range(60))


def test_different_rules_stay_apart():
    """Sonst steht unter einem Fix die Nacharbeit fuer eine andere Regel."""
    text = render_summary([
        ergebnis(Outcome.UNCHANGED, slug="a", findings=[
            warnung("1 relativer Bildpfad", rule="Bilder brauchen eine Hash-URL."),
            warnung("Schlagworte erreichen Nostr nicht"),
        ]),
    ])

    assert "Bilder brauchen eine Hash-URL." in text
    assert "Schlagworte gehoeren nach `commonMetadata.keywords`." in text


def test_the_warning_section_names_rule_and_fix_once_per_group():
    text = render_summary([
        ergebnis(Outcome.UNCHANGED, slug="a", findings=[
            warnung("Schlagworte erreichen Nostr nicht", fix="Nach `keywords` uebernehmen.")
        ]),
        ergebnis(Outcome.UNCHANGED, path="posts/zwei/index.md", slug="b", findings=[
            warnung("Schlagworte erreichen Nostr nicht", fix="Nach `keywords` uebernehmen.")
        ]),
    ])

    assert text.count("Nach `keywords` uebernehmen.") == 1
    assert "2 Beitraege" in text


def test_unchanged_posts_are_listed_not_only_counted():
    """Sonst steht im Bericht nur eine Zahl, und das Log muesste die Frage beantworten."""
    text = render_summary([
        ergebnis(Outcome.UNCHANGED, path="posts/eins/index.md", slug="eins"),
        ergebnis(Outcome.UNCHANGED, path="posts/zwei/index.md", slug="zwei"),
    ])

    assert "eins" in text and "zwei" in text


def test_a_published_post_shows_how_many_relays_confirmed():
    """Gruen heisst „nachweislich publiziert" — die Zahl gehoert dazu."""
    text = render_summary([ergebnis(Outcome.PUBLISHED, slug="x", acks=2)])

    assert "2 Relay" in text


def test_a_dry_run_does_not_claim_confirmations():
    text = render_summary([
        ergebnis(Outcome.PUBLISHED, slug="x", acks=0, reason="dry-run — nichts gesendet")
    ])

    assert "0 Relay" not in text
    assert "dry-run" in text


def test_a_warning_carries_its_line_numbers_into_the_report():
    """Ohne Zeilennummer muss die Redaktion die Stelle selbst suchen."""
    befund = Finding(
        severity=Severity.WARNING, origin="FOERBICO-Konvention (bildattribution.md)",
        message="2 relative Bildpfade — im Nostr-Event nicht aufloesbar",
        rule="Bilder brauchen eine Hash-URL.", lines=[12, 16],
        found=["bild.jpg", "zwei.png"],
    )

    text = render_summary([ergebnis(Outcome.UNCHANGED, slug="x", findings=[befund])])

    assert "12, 16" in text
    assert "bild.jpg" in text


def test_only_the_differing_part_of_a_tag_is_shown():
    """Realfall Sprachreparatur: Der summary-Tag traegt 700 Zeichen Text und die
    Sprache als letztes Element. Beides auszugeben, um einen Buchstaben zu
    zeigen, macht den Bericht unlesbar.
    """
    lang = "L" * 700
    neu = {"kind": 30023, "tags": [["summary", lang, "de"]], "content": ""}
    alt = {"kind": 30023, "tags": [["summary", lang, "d"]], "content": ""}

    text = render_summary([ergebnis(Outcome.PUBLISHED, slug="x", article=neu, existing=alt)])

    assert "'de'" in text and "'d'" in text
    assert lang not in text, "der unveraenderte Teil gehoert nicht in den Bericht"


def test_a_completely_new_tag_value_is_shown_whole():
    neu = {"kind": 30023, "tags": [["title", "Neuer Titel"]], "content": ""}
    alt = {"kind": 30023, "tags": [["title", "Alter Titel"]], "content": ""}

    text = render_summary([ergebnis(Outcome.PUBLISHED, slug="x", article=neu, existing=alt)])

    assert "Neuer Titel" in text and "Alter Titel" in text
