"""Beschreibt, wie die Daten aussehen duerfen.

Beantwortet genau eine Frage: Ist dieses Frontmatter wohlgeformt?

Tut ausdruecklich NICHT: Dateien lesen, Events bauen, Protokollregeln pruefen
(das ist NIP-Sache und liegt in error_checks).

Die Feldnamen entsprechen bewusst **woertlich** dem YAML im Frontmatter
(`givenName`, `datePublished`, `inLanguage`) statt der sonst ueblichen
Python-Schreibweise mit Unterstrichen. Dieses Modell ist der Spiegel eines
fremden Dokumentformats — wer es gegen das AMB-Schema oder eine index.md
vergleicht, soll dieselben Woerter sehen und nicht uebersetzen muessen.
"""

from pydantic import BaseModel, ConfigDict, Field, field_validator


class Affiliation(BaseModel):
    model_config = ConfigDict(extra="allow")

    name: str
    id: str | None = None
    type: str | None = None


class Creator(BaseModel):
    model_config = ConfigDict(extra="allow")

    givenName: str
    familyName: str
    type: str | None = None
    affiliation: Affiliation | None = None


class CommonMetadata(BaseModel):
    """Der `# commonMetadata`-Block einer index.md.

    Unbekannte Felder sind erlaubt und werden aufbewahrt: Ein Zusatzfeld
    beschaedigt kein Event, es wird nur nicht in Tags uebersetzt. Gemeldet
    werden sie trotzdem — `unknown_fields()` liefert die Namen dafuer.
    """

    model_config = ConfigDict(extra="allow")

    # Pflicht (nach mdparser/sync/core/validation.ts)
    id: str
    name: str
    description: str
    license: str
    creator: list[Creator]
    inLanguage: list[str]
    datePublished: str

    # Optional
    type: str | None = None
    about: list[str] = Field(default_factory=list)
    keywords: list[str] = Field(default_factory=list)
    image: str | None = None
    learningResourceType: list[str] = Field(default_factory=list)
    educationalLevel: list[str] = Field(default_factory=list)
    creativeWorkStatus: str | None = None

    @field_validator("inLanguage", mode="before")
    @classmethod
    def _single_language_becomes_list(cls, value):
        """`inLanguage: de` (19 Beitraege) als einelementige Liste lesen.

        mdparser nimmt dort `inLanguage[0]` und indiziert damit den String: Auf dem
        Relay steht bei diesen Beitraegen `["inLanguage", "d"]` — der Buchstabe
        statt der Sprache. Das Lesen als Liste repariert die Events beim naechsten
        Lauf.

        Bewusst nur hier: `about`, `keywords`, `learningResourceType`,
        `educationalLevel` und `creator` sind in allen 95 Beitraegen echte Listen.
        """
        if isinstance(value, str):
            return [value]
        return value

    def unknown_fields(self) -> list[str]:
        """Feldnamen, die das Schema nicht kennt — Eingabe fuer warning_checks."""
        return sorted(self.model_extra or {})
