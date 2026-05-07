# Wissensgrundlagen für oer.community

Dieses Verzeichnis enthält die **gemeinsamen Wissensgrundlagen** für die oer.community-Content-Pipeline. Sie sind die kanonische Quelle für alle Inhalts- und Metadaten-Entscheidungen und werden von mehreren unabhängigen Tools gelesen.

## Was hier liegt

| Datei | Zweck | Konsumenten |
|---|---|---|
| `felder.yaml` | Schema und Regeln für YAML-Frontmatter (Pflicht-/Optionalfelder, erlaubte Werte, Standardwerte, Ableitungslogik) | `comenius-yaml-mcp`, `content-lint`, `mdparser`, der `YAML-FRONTMATTER-ASSISTENT-PROMPT.md` |
| `personen.yaml` | Verzeichnis bekannter Autor:innen und ihrer Affiliations (mit ORCID, ROR, Standardangaben für `creator`-Feld) | `comenius-yaml-mcp`, LLM-Helferlein, manuelle Redaktion |
| `schlagworte.yaml` | Kanonische Schreibweisen aller Schlagworte (verhindert Synonyme und Tippfehler) | `comenius-yaml-mcp`, `content-lint` (Validierung), LLM-Helferlein |
| `schlagwort-glossar.md` | Menschenlesbare Beschreibung der Schlagworte mit Definitionen und Verwendungshinweisen | Mensch, LLM-Prompts |

## Prinzip

Jede Wissensgrundlage existiert in zwei deckungsgleichen Formen:

1. **Maschinenlesbar** (`*.yaml`) — Single Source of Truth, von Tools direkt geparst.
2. **Menschenlesbar** (`*.md`) — für Autor:innen, Reviewer und LLM-Prompts ohne MCP-Setup.

Mittelfristig sollen die menschenlesbaren Pendants aus den YAMLs **generiert** werden, sodass kein Drift entsteht. Aktuell werden sie von Hand gepflegt; ein Konsistenz-Test (im oercommunity-Hub) ist geplant.

## Wer liest die Wissensgrundlagen, wie?

- **`comenius-yaml-mcp`** liest die YAMLs über HTTP von einem stabilen Endpunkt (siehe dort `src/forgejo.ts`). Aktuell wird der Pfad auf den GitHub-Mirror `rpi-virtuell/FOERBICO_und_rpi-virtuell` umgestellt, um Anubis zu umgehen.
- **`content-lint`** soll perspektivisch seine Validierungsregeln aus `felder.yaml` ziehen statt sie hardcoded zu pflegen.
- **`mdparser/sync`** soll für sein YAML→Event-Mapping ebenfalls auf `felder.yaml` zurückgreifen.
- **LLM-Helferlein** (Claude, ChatGPT, lokale Modelle) konsumieren den menschenlesbaren `YAML-FRONTMATTER-ASSISTENT-PROMPT.md` (eine Etage höher) und die `*.md`-Dateien hier.

## Erweiterung

Neue Wissensgrundlagen (z.B. Lizenzen, Zielgruppen, Affiliations) finden hier ihre Heimat ohne Umordnung. Konvention:

- Maschinenlesbar als `<thema>.yaml`
- Menschenlesbar als `<thema>.md`
- Beide gleich benannt, damit klar ist welches Pendant zu welchem gehört
- Konsumenten und Pflichtfelder im Header der YAML-Datei dokumentieren

## Restrukturierung 2026-04-08

Bis zum 8. April 2026 lagen `felder.yaml`, `personen.yaml` und `schlagworte.yaml` unter `comenius-yaml-mcp/data/` — ein irreführender Pfad, der sie als Eigentum eines einzelnen Tools darstellte. Sie sind in dieses tool-neutrale Verzeichnis umgezogen. Der `schlagwort-glossar-oer-community.md` ist mitumgezogen und in `schlagwort-glossar.md` umbenannt.

Begründung und Migrationsschritte: siehe ADR
`oercommunity/docs/decisions/2026-04-08-restructure-wissensgrundlagen.md`
im Orchestrierungs-Hub.
