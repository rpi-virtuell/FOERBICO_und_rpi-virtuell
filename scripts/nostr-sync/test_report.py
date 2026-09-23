from models import Finding, Outcome, PostResult, Severity
from report import progress_line, render_brief, render_summary


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


# --- Punkt 3: Fortschritt waehrend des Laufs -------------------------------

def test_the_progress_line_shows_label_path_and_slug():
    """Ohne Fortschritt schweigt der Lauf minutenlang — man sieht nicht, ob er haengt."""
    zeile = progress_line(ergebnis(
        Outcome.UNCHANGED, path="Website/content/de/posts/OER-Werkstatt/index.md",
        slug="oer-werkstatt",
    ))

    assert zeile.startswith("unveraendert")
    assert "Website/content/de/posts/OER-Werkstatt/index.md" in zeile
    assert zeile.endswith("oer-werkstatt")


def test_a_progress_line_without_a_slug_shows_only_the_path():
    """Uebersprungene Beitraege haben keinen Slug — dort darf nicht „None" stehen."""
    zeile = progress_line(ergebnis(Outcome.SKIPPED, path="Website/content/de/impressum/index.md"))

    assert "None" not in zeile
    assert zeile.endswith("index.md")


def test_all_progress_labels_have_the_same_width():
    """Sonst ist die Spalte im Log nicht lesbar."""
    zeilen = [progress_line(ergebnis(ausgang, path="X", slug="s")) for ausgang in Outcome]

    assert len({zeile.index("X") for zeile in zeilen}) == 1


# --- Punkt 4: der knappe Bericht -------------------------------------------

def fehlschlag(**kwargs):
    befund = Finding(
        severity=Severity.ERROR, origin="NIP-23", message="HTML im content",
        rule='NIP-23 — "MUST NOT support adding HTML to Markdown"',
        fix="Tag entfernen; fuer einen Absatz eine Leerzeile setzen.",
        lines=[70, 92], found=["<br>"],
    )
    return ergebnis(Outcome.FAILED, slug="kaputt", findings=[befund], **kwargs)


def test_the_brief_report_counts_and_names_every_error():
    text = render_brief([fehlschlag(), ergebnis(Outcome.PUBLISHED, slug="gut")])

    assert "[!CAUTION]" in text
    assert "| fehlgeschlagen | 1 |" in text
    for stelle in ("HTML im content", "70, 92", "MUST NOT", "Leerzeile"):
        assert stelle in text, stelle


def test_the_brief_report_leaves_out_published_and_unchanged_posts():
    text = render_brief([
        ergebnis(Outcome.PUBLISHED, slug="publizierter-slug", naddr="naddr1xyz"),
        ergebnis(Outcome.UNCHANGED, slug="unveraenderter-slug"),
    ])

    assert "publizierter-slug" not in text
    assert "unveraenderter-slug" not in text
    assert "naddr1xyz" not in text and "habla" not in text


def test_the_brief_report_mentions_warnings_only_as_a_number():
    text = render_brief([
        ergebnis(Outcome.UNCHANGED, slug="a", findings=[warnung("Schlagworte fehlen")]),
        ergebnis(Outcome.UNCHANGED, path="posts/zwei/index.md", slug="b",
                 findings=[warnung("Schlagworte fehlen")]),
    ])

    assert "2 Hinweis" in text
    assert "--log" in text
    assert "Schlagworte gehoeren nach" not in text, "die Regel gehoert nicht in den knappen Bericht"
    assert "Publiziert wurde trotzdem" not in text, "gilt fuer fehlgeschlagene Beitraege nicht"


def test_the_brief_report_shows_only_the_errors_of_a_failed_post():
    """publish.py haengt einem blockierten Beitrag auch seine Warnungen an.

    Alle auszugeben brachte den knappen Bericht bei vier blockierten Beitraegen
    zurueck auf ~90 Zeilen.
    """
    kaputt = fehlschlag()
    kaputt.findings.append(warnung("Schlagworte erreichen Nostr nicht"))

    text = render_brief([kaputt])

    assert "HTML im content" in text
    assert "Schlagworte erreichen Nostr nicht" not in text


def test_the_brief_report_stays_short_without_errors():
    """Messbare Obergrenze statt Gefuehl."""
    viele = [
        ergebnis(Outcome.UNCHANGED, path=f"posts/{i}/index.md", slug=str(i),
                 findings=[warnung("irgendein Hinweis")])
        for i in range(90)
    ]

    assert len(render_brief(viele).splitlines()) < 15


def test_the_brief_report_keeps_the_nothing_published_warning():
    """„Kein stiller Erfolg" gilt auch im knappen Bericht."""
    text = render_brief([ergebnis(Outcome.SKIPPED, reason="Pflichtfelder fehlen")])

    assert "[!WARNING]" in text


def test_the_brief_report_names_an_empty_run():
    assert "Keine Beitraege" in render_brief([])


def test_the_brief_report_puts_the_numbers_before_the_details():
    """Ein Zaehler hinter 30 Zeilen Fehlertext ist keine Uebersicht."""
    kaputt = fehlschlag()
    kaputt.findings.append(warnung("ein Hinweis"))

    text = render_brief([kaputt])

    assert text.index("Hinweis(e) zur Datenqualitaet") < text.index("### Nicht publiziert")


# --- Punkt 7: der Probelauf muss sofort ins Auge fallen --------------------

def test_a_dry_run_is_named_in_the_title_and_as_an_alert():
    """Sonst sieht ein Probelauf zeichengleich aus wie ein echter Lauf.

    „dry-run — nichts gesendet" stand bisher nur an den publizierten Beitraegen,
    also in dem Abschnitt, den die Kurzfassung streicht. Beide Laeufe melden
    „publiziert 19" — bei einem davon ist nichts passiert.
    """
    text = render_brief([ergebnis(Outcome.PUBLISHED, slug="x")], dry_run=True)

    assert "## Nostr-Sync — PROBELAUF" in text, "im Titel, fuer den Blick von oben"
    assert "[!IMPORTANT]" in text, "eigene Farbstufe, nicht dieselbe wie Fehler"
    assert "NICHTS gesendet" in text


def test_a_real_run_is_not_called_a_dry_run():
    text = render_brief([ergebnis(Outcome.PUBLISHED, slug="x")])

    assert "PROBELAUF" not in text
    assert "[!IMPORTANT]" not in text
    assert text.startswith("## Nostr-Sync\n")


def test_the_dry_run_alert_comes_before_the_errors():
    """Er deutet alles darunter um — auch die Zahl der publizierten Beitraege."""
    text = render_brief([fehlschlag()], dry_run=True)

    assert text.index("[!IMPORTANT]") < text.index("[!CAUTION]")


def test_both_report_levels_name_the_dry_run():
    """Sonst verhalten sich die Stufen unterschiedlich."""
    ergebnisse = [ergebnis(Outcome.PUBLISHED, slug="x")]

    for stufe in (render_brief, render_summary):
        assert "PROBELAUF" in stufe(ergebnisse, dry_run=True), stufe.__name__


def test_an_empty_dry_run_is_still_marked():
    assert "PROBELAUF" in render_brief([], dry_run=True)


def test_a_failed_post_carries_its_reason_in_the_progress_line():
    """Die Abbruchzeile muss an ihrer Stelle selbsterklaerend sein.

    Sonst steht im Log nur „fehlgeschlagen <pfad>", und das Warum findet man
    erst, wenn man zum Bericht scrollt. Uebersprungene Beitraege bleiben davon
    unberuehrt — das ist Punkt 8 und zurueckgestellt.
    """
    zeile = progress_line(ergebnis(
        Outcome.FAILED, slug="kaputt",
        reason="unerwarteter Abbruch: JSONDecodeError: Expecting value",
    ))

    assert "JSONDecodeError" in zeile


def test_a_published_post_does_not_repeat_its_reason():
    """Dort stand „dry-run — nichts gesendet" — das sagt schon die Kopfzeile."""
    zeile = progress_line(ergebnis(
        Outcome.PUBLISHED, slug="x", reason="dry-run — nichts gesendet",
    ))

    assert "dry-run" not in zeile


# --- Alle vier Abschnitte aufklappbar --------------------------------------

MENUE = "<details><summary>Betroffene Beiträge</summary>"


def vier_abschnitte() -> list:
    """Ein Ergebnissatz, der alle vier langen Abschnitte fuellt."""
    return [
        ergebnis(Outcome.PUBLISHED, slug="publizierter", naddr="naddr1abc"),
        ergebnis(Outcome.UNCHANGED, path="posts/zwei/index.md", slug="unveraenderter"),
        ergebnis(Outcome.SKIPPED, path="de/impressum/index.md",
                 reason="Pflichtfelder fehlen: creator, name"),
        ergebnis(Outcome.UNCHANGED, path="posts/drei/index.md", slug="mit-hinweis",
                 findings=[warnung("Schlagworte fehlen")]),
    ]


def test_all_four_long_sections_are_collapsible():
    """Publiziert und Uebersprungen klappten nicht auf — gerade die laengsten.

    Bei 54 publizierten Beitraegen mit je vier Zeilen sind das ~280 Zeilen, die
    den Bericht offen fuellen.
    """
    text = render_summary(vier_abschnitte())

    assert text.count(MENUE) == 4
    assert text.count("</details>") == 4


def test_the_content_of_every_section_survives_the_folding():
    """Zugeklappt heisst nicht weg."""
    text = render_summary(vier_abschnitte())

    for inhalt in ("publizierter", "unveraenderter", "mit-hinweis",
                   "de/impressum/index.md", "Pflichtfelder fehlen: creator, name"):
        assert inhalt in text, inhalt


def test_the_unchanged_section_no_longer_builds_a_sentence_around_the_count():
    """„1 Beitrag lagen bereits so auf dem Relay" war grammatisch falsch."""
    text = render_summary([ergebnis(Outcome.UNCHANGED, slug="x")])

    assert "lagen bereits" not in text
    assert MENUE in text


def test_the_brief_report_has_no_collapsible_sections():
    """Die Kurzfassung hat diese Abschnitte gar nicht — sie bleibt unberuehrt."""
    text = render_brief(vier_abschnitte())

    assert "<details>" not in text


# --- Punkt 8: warum ein Beitrag uebersprungen wurde ------------------------

def test_a_skipped_post_carries_its_reason_in_the_progress_line():
    """In der Kurzfassung steht nur „16 uebersprungen" — ohne jedes Warum.

    Der Abschnitt *Uebersprungen* gibt es dort nicht, und die Warnung „nichts
    publiziert" greift nicht, solange irgendetwas publiziert wurde. Ohne diese
    Zeile ist „warum ist mein Beitrag nicht auf Nostr" in der CI unbeantwortbar.
    """
    zeile = progress_line(ergebnis(
        Outcome.SKIPPED, path="Website/content/de/impressum/index.md",
        reason="Pflichtfelder fehlen oder haben den falschen Typ: creator, name",
    ))

    assert zeile.endswith("— Pflichtfelder fehlen oder haben den falschen Typ: creator, name")
    assert "None" not in zeile, "uebersprungene Beitraege haben keinen Slug"
