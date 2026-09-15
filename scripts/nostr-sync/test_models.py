import pytest
from pydantic import ValidationError

from models import CommonMetadata

VOLLSTAENDIG = {
    "id": "https://oer.community/just-calling-it-open-is-not-enough",
    "name": "Just calling it Open is not enough",
    "description": "OER sind offen lizenzierte Bildungsmaterialien.",
    "license": "https://creativecommons.org/licenses/by/4.0/deed.de",
    "creator": [
        {
            "givenName": "Gina",
            "familyName": "Buchwald-Chassée",
            "type": "Person",
            "affiliation": {"name": "Comenius-Institut", "id": "https://ror.org/025e8aw85"},
        }
    ],
    "inLanguage": ["de"],
    "datePublished": "2026-08-12",
}


def test_complete_metadata_becomes_a_typed_model():
    meta = CommonMetadata.model_validate(VOLLSTAENDIG)

    assert meta.name == "Just calling it Open is not enough"
    assert meta.creator[0].familyName == "Buchwald-Chassée"
    assert meta.creator[0].affiliation.id == "https://ror.org/025e8aw85"


def test_missing_required_field_is_rejected():
    """Pflichtfelder nach mdparser/sync/core/validation.ts."""
    ohne_lizenz = {k: v for k, v in VOLLSTAENDIG.items() if k != "license"}

    with pytest.raises(ValidationError) as fehler:
        CommonMetadata.model_validate(ohne_lizenz)

    assert "license" in str(fehler.value)


def test_unknown_field_is_kept_and_nameable():
    """Realfall Save_the_Date: `url` steht im AMB-Block.

    Entscheidung: kein Fehler, aber meldbar — warning_checks braucht die Namen.
    """
    mit_fremdfeld = VOLLSTAENDIG | {"url": "save-the-date", "@type": "Article"}

    meta = CommonMetadata.model_validate(mit_fremdfeld)

    assert set(meta.unknown_fields()) == {"url", "@type"}


def test_inlanguage_as_plain_string_becomes_a_one_item_list():
    """Realfall in 19 Beitraegen: `inLanguage: de` statt `inLanguage: [de]`.

    mdparser indiziert den String mit `[0]` und publiziert deshalb live den Tag
    `["inLanguage", "d"]` — den Buchstaben, nicht die Sprache. Wir lesen den
    Skalar als einelementige Liste und reparieren die Events damit.
    """
    meta = CommonMetadata.model_validate(VOLLSTAENDIG | {"inLanguage": "de"})

    assert meta.inLanguage == ["de"]


def test_only_inlanguage_is_coerced_not_the_other_list_fields():
    """Waechter fuer den engen Zuschnitt: Nur inLanguage kommt real als Skalar vor."""
    with pytest.raises(ValidationError):
        CommonMetadata.model_validate(VOLLSTAENDIG | {"about": "https://w3id.org/kim/x"})
