# Etappe 4 des Hubs: Was das Team vor der Fachtagung (17./18.11.2026) liefern kann

Stand 05.11.2026. Die Etappe 4 (Plan `docs/superpowers/plans/2026-11-07-hub-etappe-4-sammlung-kataloge.md`) baut Sammlung, Kataloge, Fortbildungskalender und Personen in den Hub. Kataloge sind schon jetzt echt, weil der Hub zeigt, was die Communities geteilt haben; die Personen-Ansicht zeigt ohne Liste die Teamseite als Schnappschuss. Was unten steht, macht die Etappe vor der Tagung runder. Keine Schlüssel, Bunker-Links oder Zugangsdaten in diese Datei; die Schlüssel liegen beim Team (siehe `Hub-Entwicklung/communities-schluessel.md`).

## 1. Kataloge: in die Communities teilen, Listen nur zur Kuratierung (Spec 4.6, Frist 21./23.12., gern vor dem 17.11.)

Der Katalog einer Community ist im Hub, was mit ihr geteilt wurde: Material, Beiträge und Termine mit `h`-Tag auf den Community-Schlüssel, Vorhandenes als Repost (edufeed-App: „In Community teilen“). Das gibt es heute schon; niemand muss dafür eine Liste anlegen. Eine Kuratierungsliste `kind:30004` (`d = katalog`, weitere `katalog-<thema>`) ist die zweite Schicht „Vom Redaktionskreis zusammengestellt“ und kann später kommen.

| Community | Heute geteilt (05.11.2026) | Was vor der Tagung hilft |
|---|---|---|
| rpi-virtuell | 26 Materialien, 2 Beiträge, 8 Termine (keiner bevorstehend) | neu angelegte Materialien beim Veröffentlichen in die Community teilen; ein, zwei bevorstehende Fortbildungen teilen |
| relilab | 16 Materialien, 61 Artikel, 386 Termine (47 bevorstehend) | nichts Dringendes; optional eine Kuratierungsliste mit den laufenden Serien und wichtigsten Lernbausteinen |
| reliGlobal | 5 Materialien, 1 Beitrag, 4 Termine (alle bevorstehend) | zwei, drei weitere Materialien zum Globalen Lernen teilen |
| ALPIKA Grundschule | 4 Materialien, 4 Termine (keiner bevorstehend) | erste Grundschul-Materialien mit dem Grundschul-Vokabular teilen, einen Termin eintragen |
| FOERBICO (Schaufenster) | eigene Seiten und Beiträge, keine Community | Kuratierungsliste `katalog` über `Website/navigation.yaml` und `mdparser sync navigation` (Jörg, Lauf von Hand) |

Grenzen, die der Hub sichtbar sagt: Er prüft keine Mitgliederrollen (das Gruppen-Relay wird nie gelesen) und lässt nur weg, was die Community mit ihrem eigenen Schlüssel über „Aus der Community entfernen“ markiert hat. Wer mit dem Community-Schlüssel teilt, ist immer zugelassen. Beispielhaftes Teilen kann auch ein Skript übernehmen (Plan Task 7): Jörg legt die Schlüssel in einer Env-Datei außerhalb des Repos ab und entscheidet mit der Redaktion, was geteilt wird.

Prüfung: `https://hub.rpi-virtuell.net/#community?c=<id>&zu=katalog` zeigt das Geteilte mit „zuletzt geteilt am <Datum>“; eine Liste erscheint darüber mit „Stand vom <Datum der Liste>“, ohne Codeänderung.

## 2. Personen-Liste anlegen und Profile pflegen (Spec 4.10, 5a, Frist 23.12., Teams gern vor dem 17.11.)

- **Personen-Liste:** eine Follow-Liste `kind:30000` mit `d = personen` unter dem Schaufenster-Schlüssel oder dem Community-Schlüssel rpi-virtuell (edufeed-App: Listen › Neue Liste › Follow-Liste). Die `p`-Tags sind das Einverständnis: zuerst die hauptamtlichen Teams, weitere Personen erst nach Rückfrage durch das Community-Management. Ohne Liste zeigt der Hub die Teamseite als Schnappschuss.
- **Profile (`kind:0`) der genannten Personen:** `name` oder `display_name`, `about` (ein bis zwei Sätze zu Rolle und Themen), `picture` (eigenes Bild mit Rechten; Porträts unter © werden nicht übernommen), `website`, `nip05` (`name@edufeed.org`). Profile mit `bot: true` werden ausgelassen.
- **Profile für Funktionsschlüssel:** News-Redaktion rpi-virtuell und BiK-Import haben kein Profil; ohne Profil erscheinen ihre Beiträge und Termine ohne Absendernamen. Ein `kind:0` mit `name` genügt.

## 3. Fortbildungskalender (Spec 4.9, laufend)

- Der Hub liest feste Quellen (relilab-Schlüssel, rpi-virtuell, reliGlobal, ALPIKA Grundschule, KPH Wien/NÖ, RPI EKKW/EKHN, KuRU, Konfiarbeit EKD, Friedenspädagogik, bildung-kirchen.de, Kalender-Schlüssel rpi-virtuell, FOERBICO) und zusätzlich Termine mit `h`-Tag auf eine Hub-Community. Termine anderer Absender erscheinen nur über den `h`-Tag.
- **ptz-Termine** liegen heute unter einem persönlichen Schlüssel und sind damit keine Quelle. Zwei Wege: eigener ptz-Schlüssel (dann in die Quellenliste) oder `h`-Tag auf rpi-virtuell beim Veröffentlichen.
- **ALPIKA-Termine** (Spec 5a): über den FOERBICO-Schlüssel oder den Schlüssel ALPIKA Grundschule eintragen; beide sind Quellen.
- **Merkmale für die zwei Logiken:** Der Hub erkennt `registrationUrl` (mit Anmeldung), `price` (`0` = kostenfrei), `location` (Zoom, Online, URL = online; Ortsangabe = Präsenz) und `t = relilab` oder Absender relilab (Labor). Wer Termine anlegt, trägt diese Felder ein, sonst steht „keine Angabe“.
- **bildung-kirchen.de:** seit 21.01.2026 keine neuen Termine; wenn der Import nicht wieder läuft, zeigt der Kalender dort nichts Aktuelles.

## 4. Betrieb vor der Tagung

- **Lesefreigabe der Relays für die Tagungs-IP** beim Relay-Betreiber erbitten (Spec 3); der Hub bündelt die Abfragen, aber viele Gäste hinter einem WLAN überschreiten die Schwelle.
- **Schnappschuss erneuern** (`deno task schnappschuss`) nach dem Merge der Kalender-Änderung, damit der Rückfall alle Quellen trägt.
- **edufeed-App-Route für Profile:** Der Hub verlinkt „Bei edufeed ansehen“ erst, wenn die Adresse eines Personenprofils in der App feststeht (für Communities ist es `edufeed.org/c/<npub>`).

## 5. Was der Hub bis dahin zeigt

| Zeile | Ohne Lieferung | Mit Lieferung |
|---|---|---|
| Sammlung | voll nutzbar (Filter über die Materialien der drei Relays) | Community-Filter greift auf die Katalog-Listen |
| Kataloge | das Geteilte je Community (bei zweien ohne bevorstehende Termine); rpi-virtuell zusätzlich mit Materialpool-Zähler; keine Kuratierungsliste | mehr Geteiltes, Kuratierungsliste mit Stand |
| Kalender | Termine der bekannten Quellen, Merkmale wo vorhanden | mehr Quellen, vollständige Merkmale |
| Personen | Teamseite als Schnappschuss mit Initialen | Karten aus den Profilen, Profilseite je Person |
