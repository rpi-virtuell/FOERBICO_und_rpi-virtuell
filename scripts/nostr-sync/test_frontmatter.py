from textwrap import dedent

import pytest

from frontmatter import NoFrontmatter, parse_post


def test_hugo_block_does_not_leak_into_common_metadata():
    raw = dedent("""\
        ---
        # commonMetadata
        name: AMB-Titel
        # staticSiteGenerator
        title: Hugo-Titel
        ---
        Fließtext
        """)

    post = parse_post(raw)

    assert post.metadata["name"] == "AMB-Titel"
    assert "title" not in post.metadata


def test_without_markers_the_whole_frontmatter_is_common_metadata():
    """Realfall 2026-03-03-OER-erstellen: Frontmatter ganz ohne Block-Marker."""
    raw = dedent("""\
        ---
        name: Titel ohne Marker
        license: https://creativecommons.org/licenses/by/4.0/
        ---
        Fließtext
        """)

    post = parse_post(raw)

    assert post.metadata["name"] == "Titel ohne Marker"
    assert post.metadata["license"].endswith("/by/4.0/")


def test_unquoted_date_becomes_a_string():
    """YAML liest `2026-08-12` als Datumsobjekt.

    Ungebremst stuende im published_at-Tag spaeter `2026-08-12 00:00:00` statt
    `2026-08-12` — NIP-01 verlangt Strings als Tag-Werte.
    """
    raw = dedent("""\
        ---
        # commonMetadata
        datePublished: 2026-08-12
        ---
        Fließtext
        """)

    post = parse_post(raw)

    assert post.metadata["datePublished"] == "2026-08-12"


def test_numbers_in_lists_become_strings():
    """`keywords: [2026]` ergaebe sonst einen numerischen Tag-Wert."""
    raw = dedent("""\
        ---
        # commonMetadata
        keywords:
          - 2026
          - Bibel
        ---
        Fließtext
        """)

    post = parse_post(raw)

    assert post.metadata["keywords"] == ["2026", "Bibel"]


def test_booleans_are_left_alone_for_the_checks_to_report():
    """`no` liest YAML als False — `str(False)` waere „False" und damit stiller Unsinn.

    Datum und Zahl lassen sich verlustfrei in einen String ueberfuehren, ein Bool
    nicht: Die Absicht war vermutlich das Wort. Deshalb bleibt der Wert, wie er ist,
    und error_checks meldet ihn mit Feldnamen — statt hier etwas zu erfinden.
    """
    raw = dedent("""\
        ---
        # commonMetadata
        modification: no
        ---
        Fließtext
        """)

    post = parse_post(raw)

    assert post.metadata["modification"] is False


def test_body_is_returned_unchanged():
    raw = dedent("""\
        ---
        # commonMetadata
        name: Titel
        ---
        Erster Absatz.

        ![Bild](foto.jpg)
        """)

    post = parse_post(raw)

    assert post.content == "Erster Absatz.\n\n![Bild](foto.jpg)\n"


def test_images_block_is_read_separately():
    """Der `# bilder`-Marker ist YAML-Kommentar, der Schluessel darunter heisst `bilder`."""
    raw = dedent("""\
        ---
        # commonMetadata
        name: Titel
        # bilder  (Konvention: bildattribution.md)
        bilder:
          foto.jpg:
            alt: Ein Foto
            licenceUrl: https://creativecommons.org/licenses/by/4.0/
        ---
        Fließtext
        """)

    post = parse_post(raw)

    assert post.images["foto.jpg"]["alt"] == "Ein Foto"
    assert "bilder" not in post.metadata


def test_without_images_block_the_mapping_is_empty():
    raw = dedent("""\
        ---
        # commonMetadata
        name: Titel
        ---
        Fließtext
        """)

    post = parse_post(raw)

    assert post.images == {}


def test_empty_file_raises_a_named_error():
    """Realfall: Website/content/de/posts/2026-01-27-pilgern-im-ru/index.md ist 0 Byte.

    Ein Absturz mit AttributeError waere hier wertlos — der Aufrufer muss den
    Beitrag als Befund melden koennen, mit Dateinamen.
    """
    with pytest.raises(NoFrontmatter):
        parse_post("")


def test_file_without_delimiters_raises_the_same_error():
    with pytest.raises(NoFrontmatter):
        parse_post("Nur Fließtext, keine drei Striche.\n")


def test_parsed_post_knows_where_the_body_starts_in_the_file():
    """Damit Befunde Zeilennummern melden koennen, die im Editor stimmen."""
    raw = dedent("""\
        ---
        # commonMetadata
        name: Titel
        ---
        Erste Textzeile
        """)

    post = parse_post(raw)

    assert post.content_line == 5
