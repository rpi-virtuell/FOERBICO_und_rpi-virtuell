from references import extract_slug, hash_from_url, image_references

HASH = "d1e936d2add304adb02dd816588f9f22ea480bc2199bbb0b79e105f123a7c4ae"


def test_slug_is_the_path_without_the_outer_slashes():
    assert extract_slug("https://oer.community/just-calling-it-open") == "just-calling-it-open"


def test_slug_keeps_inner_slashes():
    """Regel aus mdparser: der ganze Pfad, nicht nur das letzte Segment.

    Vier Beitraege haben mehrsegmentige ids. Nur das letzte Segment zu nehmen
    wuerde dort ein anderes Event adressieren.
    """
    assert extract_slug("https://oer.community/en/our-team") == "en/our-team"


def test_slug_ignores_a_trailing_slash():
    assert extract_slug("https://oer.community/ki-und-religionspaedagogik/") == "ki-und-religionspaedagogik"


def test_hash_from_a_blossom_url_with_extension():
    assert hash_from_url(f"https://blossom.edufeed.org/{HASH}.jpg") == HASH


def test_hash_from_a_blossom_url_without_extension():
    assert hash_from_url(f"https://blossom.edufeed.org/{HASH}") == HASH


def test_hash_is_lowercased():
    assert hash_from_url(f"https://blossom.edufeed.org/{HASH.upper()}.JPEG") == HASH


def test_url_without_hash_has_none():
    """Realfall: 64 der 80 Cover zeigen auf oer.community statt auf Blossom."""
    assert hash_from_url("https://oer.community/Herausforderung-Bildung.jpg") is None


def test_relative_path_has_none():
    """Realfall: 197 Fliesstextbilder sind relative Pfade.

    Ein geratener Hash waere schlimmer als keiner — deshalb None statt Versuch.
    """
    assert hash_from_url("OER-im-Blick-2.jpg") is None


HASH_2 = "16eff3ca18abe00ad8c3fe08750ee0433bc524d5a4d974237fd7eb7054b9a6e7"
BLOSSOM = "https://blossom.edufeed.org"


def test_cover_comes_first():
    """Die Konvention haengt an der Position: Das erste x IST der Cover-Hash.

    edufeeds ArticleView und der Hub lesen es so — es gibt kein Label dafuer.
    """
    refs = image_references(f"{BLOSSOM}/{HASH}.jpg", f"![Zweites]({BLOSSOM}/{HASH_2}.png)")

    assert [r.hash for r in refs] == [HASH, HASH_2]


def test_inline_images_keep_their_order():
    content = f"![a]({BLOSSOM}/{HASH_2}.png)\n\n![b]({BLOSSOM}/{HASH}.jpg)"

    refs = image_references(None, content)

    assert [r.hash for r in refs] == [HASH_2, HASH]


def test_the_same_image_is_listed_once():
    """Zeigt der Text das Cover erneut, gibt es trotzdem nur ein x."""
    refs = image_references(f"{BLOSSOM}/{HASH}.jpg", f"![Schrein]({BLOSSOM}/{HASH}.jpg)")

    assert [r.hash for r in refs] == [HASH]


def test_images_without_a_hash_are_skipped():
    """Realfall: relative Pfade und fremde Hosts — 197 bzw. 64 Stueck."""
    content = "![a](OER-im-Blick-2.jpg) ![b](https://open-educational-resources.de/foto.png)"

    refs = image_references("https://oer.community/cover.jpg", content)

    assert refs == []


def test_a_title_in_the_markdown_link_does_not_break_the_match():
    refs = image_references(None, f'![alt]({BLOSSOM}/{HASH}.jpg "Ein Titel")')

    assert [r.hash for r in refs] == [HASH]
