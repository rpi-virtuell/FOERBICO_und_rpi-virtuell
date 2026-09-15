from textwrap import dedent

from error_checks import check_hard_line_breaks, check_html
from models import Severity


def test_clean_markdown_has_no_findings():
    assert check_html("Ein Absatz.\n\nEin zweiter Absatz.\n") == []


def test_html_in_content_is_an_error():
    """NIP-23: *MUST NOT support adding HTML to Markdown*.

    Realfall 2026-02-04-loewe-von-juda: achtmal `<br>` bzw. `</br>` als
    Absatztrenner — publiziert und live.
    """
    findings = check_html("Erster Teil <br>Zweiter Teil\n")

    assert len(findings) == 1
    assert findings[0].severity is Severity.ERROR
    assert findings[0].origin == "NIP-23"


def test_the_finding_names_line_and_tag_so_it_can_be_fixed():
    content = dedent("""\
        Absatz eins.

        Absatz zwei <br>mit Umbruch.
        """)

    finding = check_html(content)[0]

    assert finding.lines == [3]
    assert "<br>" in finding.found


def test_html_inside_a_code_block_is_allowed():
    """Im Codeblock ist HTML legitimer Inhalt, kein Formatierungsversuch."""
    content = dedent("""\
        So sieht das aus:

        ```html
        <div class="beispiel">Text</div>
        ```
        """)

    assert check_html(content) == []


def test_every_offending_line_is_collected_into_one_finding():
    content = "<br>eins\nsauber\n<br>drei\n"

    findings = check_html(content)

    assert len(findings) == 1
    assert findings[0].lines == [1, 3]


def test_the_finding_carries_rule_and_fix_so_nobody_has_to_ask():
    """Die Spec verlangt eine Meldung, die ohne Rueckfrage behebbar ist."""
    finding = check_html("Text <br>mehr\n")[0]

    assert "MUST NOT" in finding.rule
    assert finding.fix


def test_line_numbers_can_be_shifted_to_match_the_file():
    """Ohne Versatz meldet der Check Zeile 3 statt Zeile 70 — im Editor wertlos.

    Der Aufrufer kennt die Zeile, in der der Fliesstext beginnt, und gibt sie mit.
    """
    finding = check_html("sauber\nsauber\nText <br>mehr\n", first_line=52)[0]

    assert finding.lines == [54]


def test_a_hard_wrapped_paragraph_is_an_error():
    """Realfall de/unser-team: ein Satz ueber vier Zeilen verteilt.

    NIP-23: *MUST NOT hard line-break paragraphs of text.*
    """
    content = dedent("""\
        Das Comenius-Institut, Evangelische Arbeitsstätte für Erziehungswissenschaft e.V.,
        fördert Bildung und Erziehung aus evangelischer Verantwortung.
        """)

    findings = check_hard_line_breaks(content)

    assert len(findings) == 1
    assert findings[0].severity is Severity.ERROR
    assert findings[0].origin == "NIP-23"


def test_lines_that_each_end_a_sentence_are_left_alone():
    """Realfall 2025-10-06-Reformation: absichtlich zeilenweise gesetzter Text."""
    content = dedent("""\
        Konkret im Unterricht:
        Schülerinnen und Schüler schreiben Posts aus Luthers Perspektive:
        Sie wählen Hashtags, Emojis und Bilder, die seine Emotionen transportieren.
        """)

    assert check_hard_line_breaks(content) == []


def test_the_german_closing_quote_counts_as_end_of_sentence():
    """Der Fallstrick aus der Spec: Deutsch schliesst mit \u201c (U+201C).

    Fehlt das Zeichen in der Satzende-Liste, meldet der Check zwei vollstaendige
    Zitatfragen als harten Umbruch — und blockiert einen korrekten Beitrag.
    """
    content = (
        "\u201eWie w\u00fcrde Luther heute seine Thesen posten?\u201c\n"
        "\u201eWelches Medium w\u00fcrde er w\u00e4hlen?\u201c\n"
    )

    assert check_hard_line_breaks(content) == []


def test_address_blocks_are_reported_too():
    """Realfall de/datenschutz — und das ist richtig so.

    Markdown verschmilzt aufeinanderfolgende Zeilen zu einem Absatz: Aus der
    Anschrift wird „Marco Tessendorf procado Consulting 10243 Berlin". Sie
    braucht eine Liste oder gewollte Umbrueche, sonst rendert sie falsch.
    Eine Ausnahme fuer Adresszeilen wurde verworfen: gemessen aendert sie die
    Menge betroffener Dateien nicht und unterdrueckt echte Treffer.
    """
    content = dedent("""\
        Marco Tessendorf
        procado Consulting, IT- & Medienservice
        """)

    assert len(check_hard_line_breaks(content)) == 1


def test_a_deliberate_markdown_break_is_left_alone():
    """Zwei Leerzeichen am Zeilenende sind ein gewollter Umbruch."""
    content = "Erste Zeile mit Absicht umbrochen  \nzweite Zeile.\n"

    assert check_hard_line_breaks(content) == []


def test_lists_and_headings_are_left_alone():
    content = dedent("""\
        ## Eine Überschrift
        - erster Punkt
        - zweiter Punkt
        """)

    assert check_hard_line_breaks(content) == []


def test_no_length_criterion_is_used():
    """Ein Laengenkriterium wuerde hier falsch melden: kurze Zeilen, klare Saetze."""
    content = "Kurz.\nAuch kurz.\nEbenfalls.\n"

    assert check_hard_line_breaks(content) == []
