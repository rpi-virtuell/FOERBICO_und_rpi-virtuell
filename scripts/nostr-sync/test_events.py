from events import build_amb, build_article, build_attestation, tags_equal
from models import CommonMetadata

PUBKEY = "5a12b41ec15b466321e88c371be2dc47d9193f9c8bba4ab09fc50045bd35aedf"
AMB_RELAY = "wss://amb-relay.edufeed.org/"
HASH = "d1e936d2add304adb02dd816588f9f22ea480bc2199bbb0b79e105f123a7c4ae"
BLOSSOM = "https://blossom.edufeed.org"

BASIS = {
    "id": "https://oer.community/ein-beitrag",
    "name": "Ein Beitrag",
    "description": "Eine Zusammenfassung.",
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "creator": [{"givenName": "Gina", "familyName": "Buchwald-Chassée"}],
    "inLanguage": ["de"],
    "datePublished": "2026-08-12",
}


def artikel(**extra):
    meta = CommonMetadata.model_validate(BASIS | extra)
    return build_article(meta, extra.pop("_content", ""), PUBKEY, AMB_RELAY)


def tags(event, name):
    return [t for t in event["tags"] if t[0] == name]


def test_the_basic_tags_come_in_the_documented_order():
    event = artikel()

    assert event["kind"] == 30023
    assert [t[0] for t in event["tags"]] == ["d", "title", "summary", "published_at", "inLanguage"]


def test_the_slug_becomes_the_d_tag():
    assert tags(artikel(), "d") == [["d", "ein-beitrag"]]


def test_the_summary_carries_the_language_as_third_value():
    assert tags(artikel(), "summary") == [["summary", "Eine Zusammenfassung.", "de"]]


def test_published_at_is_epoch_seconds_as_a_string():
    """Live nachgeprueft: 2026-08-12 ergibt 1786492800."""
    assert tags(artikel(), "published_at") == [["published_at", "1786492800"]]


def test_the_content_is_the_markdown_body_unchanged():
    event = artikel(_content="## Die Problematik\n\nEin Absatz.\n")

    assert event["content"] == "## Die Problematik\n\nEin Absatz.\n"


def test_keywords_become_t_tags_unchanged():
    """Ohne Kleinschreibung — anders als md2blossom, wie mdparser es haelt."""
    event = artikel(keywords=["Metadaten", "Vernetzung"])

    assert tags(event, "t") == [["t", "Metadaten"], ["t", "Vernetzung"]]


def test_a_learning_resource_points_at_its_amb_event():
    event = artikel(type="LearningResource")

    assert tags(event, "a") == [
        ["a", f"30142:{PUBKEY}:ein-beitrag", AMB_RELAY, "amb-metadata"]
    ]


def test_without_learning_resource_there_is_no_cross_reference():
    assert tags(artikel(), "a") == []


def test_the_cover_hash_follows_its_image_tag_directly():
    """Die Konvention ist positionsabhaengig: Das erste x IST der Cover-Hash."""
    event = artikel(image=f"{BLOSSOM}/{HASH}.jpg")

    namen = [t[0] for t in event["tags"]]
    assert namen[namen.index("image") + 1] == "x"
    assert tags(event, "x") == [["x", HASH]]


def test_an_image_without_a_hash_gets_no_x_tag():
    """Realfall: 64 der 80 Cover zeigen auf oer.community."""
    event = artikel(image="https://oer.community/Herausforderung-Bildung.jpg")

    assert tags(event, "image") == [["image", "https://oer.community/Herausforderung-Bildung.jpg"]]
    assert tags(event, "x") == []


CONTENT_RELAY = "wss://relay-rpi.edufeed.org/"


def amb(**extra):
    meta = CommonMetadata.model_validate(BASIS | {"type": "LearningResource"} | extra)
    return build_amb(meta, PUBKEY, CONTENT_RELAY)


def test_amb_starts_with_the_documented_four_tags():
    event = amb()

    assert event["kind"] == 30142
    assert [t[0] for t in event["tags"]][:4] == ["d", "type", "name", "description"]


def test_amb_content_repeats_the_description():
    assert amb()["content"] == "Eine Zusammenfassung."


def test_a_creator_with_affiliation_expands_into_its_tag_set():
    event = amb(creator=[{
        "givenName": "Gina", "familyName": "Buchwald-Chassée", "type": "Person",
        "affiliation": {"name": "Comenius-Institut", "id": "https://ror.org/025e8aw85"},
    }])

    namen = [t for t in event["tags"] if t[0].startswith("creator")]
    assert namen == [
        ["creator:name", "Gina Buchwald-Chassée"],
        ["creator:type", "Person"],
        ["creator:affiliation:name", "Comenius-Institut"],
        ["creator:affiliation:id", "https://ror.org/025e8aw85"],
    ]


def test_an_affiliation_without_ror_id_gets_no_id_tag():
    """Realfall Jannik Streek / B310 Digital GmbH — das Feld ist optional."""
    event = amb(creator=[{
        "givenName": "Jannik", "familyName": "Streek", "type": "Person",
        "affiliation": {"name": "B310 Digital GmbH"},
    }])

    assert tags(event, "creator:affiliation:id") == []


def test_amb_keeps_every_language_not_just_the_first():
    """Anders als im 30023, wo nur inLanguage[0] landet."""
    event = amb(inLanguage=["de", "en"])

    assert tags(event, "inLanguage") == [["inLanguage", "de"], ["inLanguage", "en"]]


def test_amb_points_back_at_the_article():
    assert tags(amb(), "a") == [
        ["a", f"30023:{PUBKEY}:ein-beitrag", CONTENT_RELAY, "content"]
    ]


def test_amb_uses_the_kim_id_suffix_for_vocabulary_fields():
    event = amb(
        about=["https://w3id.org/kim/hochschulfaechersystematik/n0"],
        learningResourceType=["https://w3id.org/kim/hcrt/text"],
        educationalLevel=["https://w3id.org/kim/educationalLevel/level_A"],
    )

    assert tags(event, "about:id") == [["about:id", "https://w3id.org/kim/hochschulfaechersystematik/n0"]]
    assert tags(event, "learningResourceType:id") == [["learningResourceType:id", "https://w3id.org/kim/hcrt/text"]]
    assert tags(event, "educationalLevel:id") == [["educationalLevel:id", "https://w3id.org/kim/educationalLevel/level_A"]]


def test_amb_writes_the_date_as_given_not_as_timestamp():
    """Anders als published_at im 30023 — dort Epochensekunden, hier das Datum."""
    assert tags(amb(), "datePublished") == [["datePublished", "2026-08-12"]]


# Der Eintrag aus dem `# bilder`-Block, Feldnamen nach bildattribution.md
EINTRAG = {
    "title": "Erster OER-Brownbag der OE_COM-Projekte",
    "alt": "Screenshot mit den teilnehmenden OE_COM-Projektpartnern.",
    "author": "FOERBICO",
    "authorUrl": "https://oer.community",
    "licenceUrl": "https://creativecommons.org/licenses/by/4.0/",
    "sourceUrl": "https://oer.community/oer-brownbag",
}


def test_the_attestation_reproduces_the_live_tag_order():
    """Vorlage ist ein echtes Live-Event; die Reihenfolge ist Pflicht.

    kind:1063 ist nicht ersetzbar. Weicht die Tag-Folge von md2blossom ab,
    publizieren sich beide Werkzeuge wechselseitig ueber.
    """
    event = build_attestation(
        url=f"{BLOSSOM}/{HASH}.jpg", image_hash=HASH,
        entry=EINTRAG, mime="image/jpeg", size=99545,
    )

    assert event["kind"] == 1063
    assert event["content"] == ""
    assert [t[0] for t in event["tags"]] == [
        "url", "x", "m", "size", "title", "license", "credit", "alt", "source", "authorUrl",
    ]


def test_missing_optional_fields_become_empty_strings_not_missing_tags():
    """title, license, credit und alt stehen immer da — so haelt es md2blossom."""
    event = build_attestation(
        url=f"{BLOSSOM}/{HASH}.jpg", image_hash=HASH,
        entry={"licenceUrl": "https://creativecommons.org/licenses/by/4.0/"},
        mime="image/jpeg",
    )

    paare = {t[0]: t[1] for t in event["tags"]}
    assert paare["title"] == ""
    assert paare["credit"] == ""
    assert "size" not in paare


def test_alt_falls_back_to_the_title():
    event = build_attestation(
        url=f"{BLOSSOM}/{HASH}.jpg", image_hash=HASH,
        entry={"title": "Ein Titel", "licenceUrl": "https://x"}, mime="image/jpeg",
    )

    assert ["alt", "Ein Titel"] in event["tags"]


def test_only_the_two_documented_ai_values_produce_a_tag():
    """edufeed-Wiki: generated | modified. Alles andere ist „nicht deklariert"."""
    gueltig = build_attestation(
        url=f"{BLOSSOM}/{HASH}.jpg", image_hash=HASH,
        entry=EINTRAG | {"ai": "generated"}, mime="image/jpeg",
    )
    unsinn = build_attestation(
        url=f"{BLOSSOM}/{HASH}.jpg", image_hash=HASH,
        entry=EINTRAG | {"ai": "vielleicht"}, mime="image/jpeg",
    )

    assert ["ai", "generated"] in gueltig["tags"]
    assert [t for t in unsinn["tags"] if t[0] == "ai"] == []


def test_the_ai_tag_comes_last():
    event = build_attestation(
        url=f"{BLOSSOM}/{HASH}.jpg", image_hash=HASH,
        entry=EINTRAG | {"ai": "modified", "pubkey": "a" * 64}, mime="image/jpeg",
    )

    assert event["tags"][-1] == ["ai", "modified"]


def test_two_events_with_the_same_tags_count_as_equal():
    """Grundlage der Idempotenz: created_at, id, sig und pubkey zaehlen nicht."""
    a = {"kind": 30023, "tags": [["d", "x"]], "content": "Text"}
    b = {"kind": 30023, "tags": [["d", "x"]], "content": "Text",
         "created_at": 1789, "id": "abc", "sig": "def", "pubkey": "a" * 64}

    assert tags_equal(a, b)


def test_a_different_tag_value_makes_them_unequal():
    a = {"kind": 30023, "tags": [["d", "x"]], "content": "Text"}
    b = {"kind": 30023, "tags": [["d", "y"]], "content": "Text"}

    assert not tags_equal(a, b)


def test_a_different_content_makes_them_unequal():
    a = {"kind": 30023, "tags": [["d", "x"]], "content": "Text"}
    b = {"kind": 30023, "tags": [["d", "x"]], "content": "Anderer Text"}

    assert not tags_equal(a, b)
