from models import CommonMetadata, Severity
from warning_checks import check_images, check_keywords, check_unknown_fields

PFLICHT = {
    "id": "https://oer.community/ein-beitrag",
    "name": "Ein Beitrag",
    "description": "Eine Zusammenfassung.",
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "creator": [{"givenName": "Gina", "familyName": "Buchwald-Chassée"}],
    "inLanguage": ["de"],
    "datePublished": "2026-08-12",
}

BLOSSOM = "https://blossom.edufeed.org/" + "a" * 64 + ".jpg"


# --- Schlagworte -----------------------------------------------------------

def test_keywords_only_in_the_hugo_block_are_reported():
    """Fall B, 60 Beitraege: vorhanden, aber sie erreichen Nostr nicht."""
    befunde = check_keywords({}, {"tags": ["Metadaten", "OER"]})

    assert len(befunde) == 1
    assert befunde[0].severity is Severity.WARNING
    assert "schlagworte.yaml" in befunde[0].origin
    assert "staticSiteGenerator.tags" in befunde[0].message
    assert befunde[0].found == ["Metadaten", "OER"]


def test_keywords_in_common_metadata_tags_are_also_reported():
    """Fall B, andere Auspraegung: richtiger Block, falsches Feld (2 Beitraege)."""
    befunde = check_keywords({"tags": ["OER"]}, {})

    assert len(befunde) == 1
    assert "commonMetadata.tags" in befunde[0].message


def test_consistent_keywords_are_not_reported():
    """Fall A, 22 Beitraege: genau so ist es gemeint."""
    assert check_keywords({"keywords": ["OER"]}, {"tags": ["OER"]}) == []


def test_a_post_without_any_keywords_is_not_reported():
    """Fall D, 15 Beitraege: es gibt nichts zu uebertragen."""
    assert check_keywords({}, {}) == []


def test_keywords_only_in_common_metadata_are_not_reported():
    """Der Hugo-Block ist kein Pflichtfeld — nur das publizierte Feld zaehlt."""
    assert check_keywords({"keywords": ["OER"]}, {}) == []


def test_diverging_keyword_fields_are_reported_in_both_directions():
    """Fall C, 1 Beitrag: teils publiziert, teils nicht — beide Seiten nennen."""
    befunde = check_keywords(
        {"keywords": ["OER", "Nur-AMB"]}, {"tags": ["OER", "Nur-Hugo"]}
    )

    assert len(befunde) == 1
    assert "weichen" in befunde[0].message
    gefunden = " ".join(befunde[0].found)
    assert "Nur-AMB" in gefunden and "Nur-Hugo" in gefunden


def test_only_the_order_differing_is_not_a_divergence():
    assert check_keywords({"keywords": ["B", "A"]}, {"tags": ["A", "B"]}) == []


# --- Bilder ----------------------------------------------------------------

def test_relative_image_paths_are_reported_with_their_lines():
    """197 Stueck — auf der Website richtig, im Nostr-Client kaputt."""
    content = "Ein Absatz.\n\n![Erstes](bild.jpg)\n\nText\n\n![Zweites](unter/zwei.png)\n"

    befunde = check_images(None, content, first_line=10)

    assert len(befunde) == 1
    assert "relative" in befunde[0].message
    assert befunde[0].found == ["bild.jpg", "unter/zwei.png"]
    assert befunde[0].lines == [12, 16]


def test_an_absolute_url_without_a_hash_is_reported_separately():
    """64 Cover — auflösbar, aber ohne Lizenznachweis."""
    befunde = check_images("https://oer.community/titel.jpg", "")

    assert len(befunde) == 1
    assert "Lizenznachweis" in befunde[0].message
    assert befunde[0].found == ["https://oer.community/titel.jpg"]


def test_a_blossom_hash_url_is_not_reported():
    """Der Regelfall — dafuer ist der Bilderschritt da."""
    assert check_images(BLOSSOM, f"![Bild]({BLOSSOM})") == []


def test_both_kinds_of_image_problems_are_reported_apart():
    befunde = check_images("https://oer.community/titel.jpg", "![Bild](relativ.jpg)")

    assert len(befunde) == 2


def test_the_same_url_twice_is_reported_once():
    befunde = check_images(None, "![A](bild.jpg)\n\n![B](bild.jpg)")

    assert befunde[0].found == ["bild.jpg"]


def test_a_post_without_images_is_not_reported():
    assert check_images(None, "Nur Text.") == []


# --- Unbekannte Felder -----------------------------------------------------

def test_unknown_frontmatter_fields_are_named():
    """Sie beschaedigen kein Event — sie werden nur in keinen Tag uebersetzt.

    Die JSON-LD-Schluessel `@context` und `@type` zaehlen nicht dazu, siehe
    test_models.py::test_jsonld_keys_are_known_fields.
    """
    metadata = CommonMetadata(**PFLICHT, **{"cover": "bild.jpg", "sonstiges": "x"})

    befunde = check_unknown_fields(metadata)

    assert len(befunde) == 1
    assert befunde[0].severity is Severity.WARNING
    assert befunde[0].found == ["cover", "sonstiges"]


def test_a_clean_frontmatter_has_no_unknown_fields():
    assert check_unknown_fields(CommonMetadata(**PFLICHT)) == []


def test_counts_are_worded_in_german_singular():
    """Die Meldungen liest die Redaktion — „1 unbekannte Felder" nicht."""
    ein_bild = check_images("https://oer.community/titel.jpg", "![Bild](relativ.jpg)")
    ein_feld = check_unknown_fields(CommonMetadata(**PFLICHT, **{"cover": "bild.jpg"}))

    assert "1 relativer Bildpfad" in ein_bild[0].message
    assert "1 Bild ohne Blossom-Hash" in ein_bild[1].message
    assert "1 unbekanntes Feld" in ein_feld[0].message
