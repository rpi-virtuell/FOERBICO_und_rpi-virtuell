"""Pruefungen, die nur melden.

Beantwortet genau eine Frage: Wo widerspricht ein Beitrag unseren eigenen
Konventionen, ohne dass ein Event dadurch ungueltig wuerde?

Nichts hier blockiert das Publizieren. Es geht um das Gegenteil des bisherigen
Verhaltens: Was heute stillschweigend verlorengeht — Schlagworte im falschen
Block, Bilder ohne aufloesbare URL, unbekannte Felder —, soll sichtbar werden.
Protokollverstoesse liegen dagegen in error_checks und blockieren.

Tut ausdruecklich NICHT: Daten reparieren, Events bauen, Dateien lesen. Die
Uebernahme der Schlagworte ist Ausbaustufe 2 und eine redaktionelle Entscheidung.
"""

from urllib.parse import urlparse

from models import CommonMetadata, Finding, Severity
from references import MARKDOWN_IMAGE, hash_from_url

KEYWORD_ORIGIN = "FOERBICO-Konvention (schlagworte.yaml)"
KEYWORD_RULE = (
    "schlagworte.yaml: „Nur diese Schreibweisen verwenden – in `keywords` "
    "(commonMetadata) und identisch in `tags` (staticSiteGenerator)."
)

# Das einzige Feld, aus dem `t`-Tags entstehen. Alle anderen sind Ablageorte,
# die der Sync nur liest, um Abweichungen zu melden.
PUBLISHED_FIELD = "commonMetadata.keywords"


def check_keywords(metadata: dict, site_generator: dict) -> list[Finding]:
    """Meldet Schlagworte, die nicht dort stehen, wo sie publiziert werden.

    Der Sync **aendert daran nichts**: `t`-Tags entstehen weiterhin allein aus
    `commonMetadata.keywords`. Gemessen ueber 96 Beitraege verteilen sich die
    Faelle auf 22 konsistente, 60 nur woanders, 1 abweichenden, 15 ohne.
    """
    publiziert = _as_texts(metadata.get("keywords"))
    andere = {
        "commonMetadata.tags": _as_texts(metadata.get("tags")),
        "staticSiteGenerator.keywords": _as_texts(site_generator.get("keywords")),
        "staticSiteGenerator.tags": _as_texts(site_generator.get("tags")),
    }
    gefuellt = {feld: werte for feld, werte in andere.items() if werte}
    if not gefuellt:
        return []
    if not publiziert:
        return [_nicht_publiziert(gefuellt)]
    return _divergenz(publiziert, gefuellt)


def _nicht_publiziert(gefuellt: dict[str, list[str]]) -> Finding:
    """Fall B: Schlagworte sind da, aber nicht im publizierten Feld."""
    felder = ", ".join(f"`{feld}`" for feld in gefuellt)
    werte = sorted({wort for liste in gefuellt.values() for wort in liste})
    return Finding(
        severity=Severity.WARNING,
        origin=KEYWORD_ORIGIN,
        message=(
            f"Schlagworte stehen nur in {felder}, `{PUBLISHED_FIELD}` ist leer — "
            "sie erreichen Nostr nicht"
        ),
        rule=KEYWORD_RULE,
        fix=f"Die Schlagworte zusaetzlich nach `{PUBLISHED_FIELD}` uebernehmen.",
        found=werte,
    )


def _divergenz(publiziert: list[str], gefuellt: dict[str, list[str]]) -> list[Finding]:
    """Fall C: Beide Seiten sind gefuellt, sagen aber Unterschiedliches."""
    andere = {wort for liste in gefuellt.values() for wort in liste}
    nur_publiziert = sorted(set(publiziert) - andere)
    nur_andere = sorted(andere - set(publiziert))
    if not nur_publiziert and not nur_andere:
        return []

    felder = ", ".join(f"`{feld}`" for feld in gefuellt)
    unterschiede = []
    if nur_publiziert:
        unterschiede.append(f"nur in `{PUBLISHED_FIELD}`: {', '.join(nur_publiziert)}")
    if nur_andere:
        unterschiede.append(f"nur in {felder}: {', '.join(nur_andere)}")

    return [Finding(
        severity=Severity.WARNING,
        origin=KEYWORD_ORIGIN,
        message=(
            f"Schlagwort-Felder weichen voneinander ab — publiziert wird allein "
            f"`{PUBLISHED_FIELD}`"
        ),
        rule=KEYWORD_RULE,
        fix="Beide Felder auf denselben Stand bringen.",
        found=unterschiede,
    )]


def _as_texts(value) -> list[str]:
    """Schlagworte als Textliste — leere Eintraege bleiben sichtbar.

    Ein leeres Listenelement kommt real vor. Es stillschweigend zu entfernen
    waere genau das Verhalten, gegen das dieses Modul antritt.
    """
    if not isinstance(value, list):
        return []
    return [str(wort) if wort is not None else "(leerer Eintrag)" for wort in value]


def _plural(anzahl: int, einzahl: str, mehrzahl: str) -> str:
    """Deutsche Zahlform — die Meldungen liest die Redaktion, nicht die CI."""
    return f"{anzahl} {einzahl if anzahl == 1 else mehrzahl}"


def check_images(cover_url: str | None, content: str, first_line: int = 1) -> list[Finding]:
    """Meldet Bilder, zu denen es auf Nostr weder Blob noch Nachweis gibt.

    Zwei getrennte Befunde, weil die Folgen verschieden schwer wiegen: Ein
    relativer Pfad ist im Nostr-Client **kaputt** (die Datei liegt nur im
    Hugo-Page-Bundle), eine absolute URL ohne Hash ist auflösbar, aber ohne
    Lizenznachweis.
    """
    relativ: dict[str, int | None] = {}
    ohne_hash: dict[str, int | None] = {}

    for url, zeile in _image_urls(cover_url, content, first_line):
        if hash_from_url(url) is not None:
            continue
        ziel = ohne_hash if _is_absolute(url) else relativ
        ziel.setdefault(url, zeile)

    befunde = []
    if relativ:
        befunde.append(_bild_warnung(
            relativ,
            _plural(len(relativ), "relativer Bildpfad", "relative Bildpfade")
            + " — im Nostr-Event nicht aufloesbar",
            rule="Ein relativer Pfad zeigt ins Hugo-Page-Bundle. Nostr-Clients "
                 "kennen es nicht — dort bleibt das Bild leer.",
            fix="Die Bilder nach Blossom ueberfuehren (siehe bildmigration.md), "
                "dann verweist der Beitrag auf eine Hash-URL.",
        ))
    if ohne_hash:
        befunde.append(_bild_warnung(
            ohne_hash,
            _plural(len(ohne_hash), "Bild ohne Blossom-Hash", "Bilder ohne Blossom-Hash")
            + " — kein Lizenznachweis moeglich",
            rule="Ein kind:1063 wird ueber den SHA-256 des Bildes gefunden. Ohne "
                 "Hash in der URL gibt es nichts, woran er haengen koennte.",
            fix="Die Bilder nach Blossom ueberfuehren, damit ein kind:1063 entstehen kann.",
        ))
    return befunde


def _image_urls(cover_url: str | None, content: str, first_line: int):
    """Alle Bild-URLs des Beitrags mit ihrer Dateizeile.

    Das Cover steht im Frontmatter und hat deshalb keine Zeile im Fliesstext.
    """
    if cover_url:
        yield cover_url, None
    for versatz, zeile in enumerate(content.splitlines()):
        for treffer in MARKDOWN_IMAGE.finditer(zeile):
            yield treffer.group(2), first_line + versatz


def _is_absolute(url: str) -> bool:
    parsed = urlparse(url)
    return bool(parsed.scheme and parsed.netloc)


def _bild_warnung(
    gefunden: dict[str, int | None], message: str, *, rule: str, fix: str
) -> Finding:
    return Finding(
        severity=Severity.WARNING,
        origin="FOERBICO-Konvention (bildattribution.md)",
        message=message,
        rule=rule,
        fix=fix,
        lines=sorted(zeile for zeile in gefunden.values() if zeile is not None),
        found=list(gefunden),
    )


def check_unknown_fields(metadata: CommonMetadata) -> list[Finding]:
    """Meldet Frontmatter-Felder, die das AMB-Schema nicht kennt.

    Sie beschaedigen kein Event — sie werden nur in keinen Tag uebersetzt. Genau
    deshalb faellt es sonst niemandem auf.
    """
    unbekannt = metadata.unknown_fields()
    if not unbekannt:
        return []
    return [Finding(
        severity=Severity.WARNING,
        origin="AMB-Schema",
        message=(
            _plural(len(unbekannt), "unbekanntes Feld", "unbekannte Felder")
            + " im `# commonMetadata`-Block — ohne Wirkung auf die Events"
        ),
        rule="Bekannt sind die Felder aus models.py:CommonMetadata.",
        fix="Feldnamen pruefen (Tippfehler?) oder in den `# staticSiteGenerator`-Block "
            "verschieben, wenn sie nur Hugo betreffen.",
        found=unbekannt,
    )]
