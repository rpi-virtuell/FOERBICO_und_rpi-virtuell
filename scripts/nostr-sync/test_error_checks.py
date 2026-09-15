from textwrap import dedent

from error_checks import check_html
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
