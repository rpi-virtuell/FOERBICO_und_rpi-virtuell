# Einrichtung: ngit, Amber und die beiden Konten

Einmalig auf Jörgs Rechner. Nichts davon landet im Repo. Spec: `docs/superpowers/specs/2026-10-26-poutnik-issue-agent-design.md`, Abschnitte 4.1, 4.2, 4.6, 4.8.

## a) ngit 3.0.4 installieren

Release-Binary `darwin-universal` aus dem Installer-Manifest (`https://ngit.dev/install.sh`, Zeile `darwin-universal|<url>|<sha256>|…`). Entweder der Ein-Zeilen-Installer:

```bash
curl -Ls https://ngit.dev/install.sh | bash
```

oder von Hand: Archiv laden, `shasum -a 256` gegen den Hash aus dem Manifest prüfen, `ngit` und `git-remote-nostr` nach `~/.local/bin` (muss im PATH liegen) entpacken.

Prüfung:

```bash
ngit --version && which git-remote-nostr
```

Erwartet: `ngit 3.0.4` und ein Pfad für `git-remote-nostr`.

## b) Zwei Bunker-Verbindungen in Amber

Amber → Anwendungen → neue Verbindung („Bunker-Link“), zweimal:

| Verbindung | Schlüssel | Berechtigungen |
|---|---|---|
| **poutnik** | Poutník (`npub1d2g2mkna55ufjnhyxhgwuqldmczsmqrwee954z4pldzlqn04gamstvkeev`) | alles **dauerhaft** freigeben (sign event, alle Kinds; nip04/nip44 nicht nötig) |
| **joerg** | Jörgs Privatschlüssel (`4fa5d1c4…`) | **dauerhaft** nur kind 27235 (HTTP Auth, NIP-98); **jedes Mal fragen** bei 1621, 1111, 1630, 1631, 1632, 1633, 30618 |

Falls Poutníks Schlüssel noch nicht in Amber liegt: dort zuerst importieren (nsec aus der edufeed-Registrierung).

Die beiden `bunker://…`-Links kopieren. Sie enthalten ein Geheimnis: nicht in Dateien im Repo, nicht in den Chat.

## c) Konten in ngit anmelden

```bash
ngit account login --bunker-url "bunker://…poutnik…" --alias poutnik --offline
ngit account login --bunker-url "bunker://…joerg…" --alias joerg --offline
ngit account logout
```

`logout` ohne `--forget` entfernt nur das aktive Standardkonto; die beiden Aliase bleiben gespeichert (Geheimnis im macOS-Schlüsselbund, `--secret-storage auto`). So pusht nie ein Konto „aus Versehen“, jeder Aufruf nennt `--signer` bzw. `-c nostr.signer=`.

## d) Prüfung

```bash
ngit account whoami --json
```

Erwartet: beide Aliase mit ihren npubs, kein aktives Standardkonto.

## e) Umgebungsdatei

```bash
mkdir -p ~/.config/poutnik && touch ~/.config/poutnik/env && chmod 600 ~/.config/poutnik/env
```

Inhalt (Werte einsetzen):

```
POUTNIK_PUBKEY_HEX=6a90adda7da538994ee435d0ee03edde050d806ece4b4a8aa1fb45f04df54777
JOERG_PUBKEY_HEX=4fa5d1c413e2b45e10d40bf3562ab701a5331206e359c90baae0e99bfd6c6e41
POUTNIK_BUNKER_URL=bunker://…poutnik…
POUTNIK_CLIENT_SECRET_HEX=<einmalig: openssl rand -hex 32>
FORGEJO_TOKEN_FILE=/Users/joerglohrer/.config/forgejo/token.txt
```

`POUTNIK_BUNKER_URL` und `POUTNIK_CLIENT_SECRET_HEX` braucht nur das Setup-Skript `setup/profile.ts` (Profil ergänzen); ngit nutzt den Schlüsselbund.

Abschließend: `cd tools/poutnik && deno task doctor` (ab Task 7) muss alle Checks grün zeigen.
