"""Prueft, was die Veroeffentlichung eines Beitrags blockiert.

Beantwortet genau eine Frage: Verletzt dieser Beitrag eine fremde Spezifikation
(NIP-01, NIP-23, NIP-94) so, dass er nicht publiziert werden darf?

Warum blockierend: kind:30023 und kind:30142 sind ersetzbar. Ein fehlerhaftes
Event loescht die funktionierende Vorversion auf dem Relay. Nicht publizieren ist
dann besser als publizieren.

Tut ausdruecklich NICHT: eigene Konventionen pruefen (das ist warning_checks),
Events bauen, publizieren.
"""

import re

from models import Finding, Severity

# Tag-artige Muster: `<br>`, `</br>`, `<div class="x">`. Bewusst grob — im
# Fliesstext eines Blogbeitrags gibt es keinen legitimen Grund fuer spitze
# Klammern um einen Bezeichner.
HTML_TAG = re.compile(r"</?[a-zA-Z][a-zA-Z0-9]*(?:\s[^>]*)?/?>")

CODE_FENCE = "```"


def check_html(content: str, first_line: int = 1) -> list[Finding]:
    """NIP-23 verbietet HTML im Markdown — das gilt auch fuer ein einzelnes `<br>`.

    `first_line` ist die Dateizeile, in der `content` beginnt. Ohne sie meldet der
    Befund Zeilennummern des Fliesstexts, die im Editor ins Leere zeigen.
    """
    lines: list[int] = []
    found: list[str] = []
    for number, line in _lines_outside_code_blocks(content, first_line):
        tags = HTML_TAG.findall(line)
        if not tags:
            continue
        lines.append(number)
        found.extend(tag for tag in tags if tag not in found)

    if not lines:
        return []

    return [
        Finding(
            severity=Severity.ERROR,
            origin="NIP-23",
            message="HTML im content",
            rule='NIP-23 — "MUST NOT support adding HTML to Markdown"',
            fix="Tag entfernen; fuer einen Absatz eine Leerzeile setzen.",
            lines=lines,
            found=found,
        )
    ]


def _lines_outside_code_blocks(content: str, first_line: int):
    """Zeilennummer und Text, Codebloecke ausgelassen.

    In einem Codeblock ist HTML gezeigter Inhalt, kein Formatierungsversuch.
    """
    inside = False
    for number, line in enumerate(content.split("\n"), start=first_line):
        if line.lstrip().startswith(CODE_FENCE):
            inside = not inside
            continue
        if not inside:
            yield number, line


# Satzende. Die deutschen Schlusszeichen muessen mit rein — Deutsch schliesst mit
# “ (U+201C), nicht mit ”. Fehlt U+201C hier, meldet der Check zwei
# vollstaendige Zitatfragen auf eigenen Zeilen als harten Umbruch und blockiert
# damit einen korrekten Beitrag (gesehen an 2025-10-06-Reformation).
SENTENCE_END = re.compile(r"[.!?:;»«“”’\"')\]]\s*$")

# Zeilen, die einen eigenen Block eroeffnen — dort ist ein Umbruch Struktur.
BLOCK_START = ("#", "-", "*", ">", "|", "!", "[", "```")
NUMBERED = re.compile(r"^\s*\d+[.)]\s")

# Eine Zeile setzt den Satz fort, wenn sie klein oder mit oeffnendem Zitat beginnt.
CONTINUES_SENTENCE = re.compile(r"^[a-zäöüß„«\"]")


def check_hard_line_breaks(content: str, first_line: int = 1) -> list[Finding]:
    """NIP-23 verbietet, Absaetze hart umzubrechen.

    Erkannt wird nur der eindeutige Fall: Eine Zeile endet **mitten im Satz** und
    die naechste setzt ihn fort. Bewusst **kein** Laengenkriterium — „drei Zeilen
    zwischen 60 und 90 Zeichen" meldet absichtlich zeilenweise gesetzten Text
    falsch, und ein Fehlalarm haelt hier eine korrekte Veroeffentlichung auf.
    """
    lines = list(_lines_outside_code_blocks(content, first_line))
    hits = [
        number
        for (number, line), (_, following) in zip(lines, lines[1:])
        if _breaks_mid_sentence(line, following)
    ]
    if not hits:
        return []

    return [
        Finding(
            severity=Severity.ERROR,
            origin="NIP-23",
            message="harte Absatzumbrueche im content",
            rule='NIP-23 — "MUST NOT hard line-break paragraphs of text"',
            fix="Absatz in eine durchgehende Zeile schreiben; Umbrueche macht der Client.",
            lines=hits,
        )
    ]


def _breaks_mid_sentence(line: str, following: str) -> bool:
    """Endet `line` mitten im Satz und setzt `following` ihn fort?"""
    if not line.strip() or not following.strip():
        return False
    if line.startswith(BLOCK_START) or following.startswith(BLOCK_START):
        return False
    if NUMBERED.match(line) or NUMBERED.match(following):
        return False
    if line.endswith("  "):
        return False
    if SENTENCE_END.search(line):
        return False
    return bool(CONTINUES_SENTENCE.match(following))
