# Veröffentlichen von Listen und Reposts

`veroeffentlichen.ts` liest eine unsignierte Event-Vorlage (ein JSON-Objekt oder ein Array), setzt `created_at`, signiert mit einem Schlüssel aus einer Umgebungsvariablen und sendet an `wss://relay.edufeed.org`, `wss://relay-rpi.edufeed.org` und `wss://amb-relay.edufeed.org`. Je Relay erscheint `OK` oder `Grund: …`, dazu die Event-Id. Schlüsselwerte werden nie ausgegeben.

## Schlüssel

Die Env-Datei liegt außerhalb des Repos: `~/.config/nachweis/listen.env`, Rechte 600. Sie enthält je Schlüssel eine Variable:

`NSEC_RPI_VIRTUELL`, `NSEC_RELILAB`, `NSEC_RELIGLOBAL`, `NSEC_ALPIKA_GS`, `NSEC_FOERBICO`

Erlaubt sind `nsec1…` oder 64-stelliges Hex. Der Inhalt der Datei steht nirgends im Repository.

## Aufruf

```bash
deno run --env-file=$HOME/.config/nachweis/listen.env --allow-env --allow-net \
  --allow-read=Hub-Entwicklung/kataloge \
  tools/listen/veroeffentlichen.ts Hub-Entwicklung/kataloge/personen-liste.json NSEC_FOERBICO
```

Trockenlauf (kein Schlüssel nötig, es wird nichts signiert oder gesendet): `--dry-run` anhängen. `--allow-env`, `--allow-net` und `--env-file` entfallen, `--allow-read` bleibt:

```bash
deno run --allow-read=Hub-Entwicklung/kataloge \
  tools/listen/veroeffentlichen.ts Hub-Entwicklung/kataloge/personen-liste.json NSEC_FOERBICO --dry-run
```

Die Vorlage wird vor jeder Verwendung geprüft (`kind` ganze Zahl, `tags` Array aus String-Arrays, `content` String); Fehler nennen Datei und Position.

## Regeln

- Ein Aufruf je Vorlage und Schlüssel, nie in einer Schleife. Bei Arrays wartet das Skript 3 s zwischen den Events.
- Zwischen zwei Läufen einige Minuten Pause: Die Relays sperren Adressen nach etwa 20 schnellen Anfragen.
- Vorher immer `--dry-run` und die Vorlage gegenlesen.
