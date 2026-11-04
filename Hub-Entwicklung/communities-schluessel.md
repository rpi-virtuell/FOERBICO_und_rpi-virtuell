# Community-Schlüssel: Bestand, Aktivität und offene Fragen

Stand: 04.11.2026. Erhoben von den Relays `relay-rpi.edufeed.org` und `relay.edufeed.org`
(Community-Definitionen `kind:10222`, Profile `kind:0`, Mitgliedschaften `kind:30000` mit
`d=communities`, Beiträge über den `h`-Tag, eigene Veröffentlichungen je Schlüssel) sowie aus
dem NIP-05-Verzeichnis `edufeed.org/.well-known/nostr.json` (40 Namen) und den Repositories.
Enthalten sind nur öffentliche Schlüssel (npub). Private Schlüssel, Bunker-Links und
Zugangsdaten gehören nicht in dieses Repository.

Grenzen der Zahlen: Die Relays liefern je Abfrage höchstens einige hundert Events, die
Mitglieder- und Beitragszahlen sind deshalb Untergrenzen. „Beiträge" zählt Events mit `h`-Tag
auf den Community-Schlüssel (Reposts `kind:16`, Termine, Artikel, Kommentare). „Eigene" zählt
Events, die der Schlüssel selbst signiert hat. Wer einen Schlüssel hält, ist aus dem Relay nicht
ablesbar und steht in Abschnitt 5 als Frage.

## 1. Ergebnis in drei Sätzen

Es gibt 28 Communities (`kind:10222`) auf den beiden Relays, davon 21 mit eigenem Profil und
Namen. Die vier für die Kataloge vorgesehenen Communities rpi-virtuell, relilab, reliGlobal und
ALPIKA Grundschule haben alle bereits einen Schlüssel und eine Community; die Annahme im Plan
(relilab und ALPIKA Grundschule fehlen) ist überholt. Keine einzige Community hat bisher eine
Katalog-Liste (`kind:30004`); die einzigen Listen im Projektumfeld sind Hauptmenü und Fußzeile
des FOERBICO-Schlüssels.

## 2. Communities für die Hub-Kataloge (Spec 4.6, 5a)

| Community | Instanz | npub | Community seit | Mitglieder | Beiträge (letzter) | Eigene Events | Katalog-Liste |
|---|---|---|---|---|---|---|---|
| rpi-virtuell | rpi-virtuell (Materialpool, Fortbildungskalender, News) | `npub14esenw6rt4c2pmxwvyey4jqw0sjdahetq6qvh5lffxp7w4thg63ql480z2` | 15.09.2026 | 35 | 48 (27.10.2026) | 3 (2 Termine, 1 Artikel) | fehlt |
| relilab | relilab (Labor-Instanz) | `npub1fpcxaz2wvjl90gjs60x37ny2pa5u4yqfx7fklz73rgfjnnfujl3sr2fxgk` | 17.09.2026 | 26 | 831, davon 748 Termine, 61 Artikel (19.10.2026) | 103 (102 Termine) | fehlt |
| reliGlobal | eigene Community, NIP-05 `religlobal@edufeed.org` | `npub12atlgghwe2qwkps9sgm9z4je825hskh47ef7kc28zzgn5tztgtyqyveeqs` | 15.10.2026 | 4 | 13 (27.10.2026) | 8 (4 Materialien, 4 Termine) | fehlt |
| ALPIKA Grundschule | eigene Community, NIP-05 `alpika-grundschule@edufeed.org` | `npub10gyagq3eev0vcnqks69gewz22kvpe2989c5zua88huarjwwl04dqdzrmzr` | 11.09.2026 | 6 | 9 (24.09.2026) | 2 | fehlt |
| FOERBICO (oer.community) | Schaufenster oer.community | `npub1tgftg8kptdrxxg0g3sm3hckuglv3j0uu3way4vylc5qyt0f44m0s3gun6e` | keine Community (nur Profil) | – | – | 103 Artikel und Seiten, 409 Bildlizenzen, 2 Listen (Hauptmenü, Fußzeile), 2 Materialien | nur Menü und Fußzeile |

Folgerung für die Spec: In 4.6 und 5a steht „eigene Community-Schlüssel (werden angelegt)".
Richtig ist: Die Schlüssel bestehen und liegen beim Projektteam, anzulegen sind nur die Katalog-Listen. Für FOERBICO ist zu
entscheiden, ob der Schaufenster-Schlüssel eine Community (`kind:10222`) bekommt oder ob der
Katalog FOERBICO als reine Liste vom Profil-Schlüssel ausgeliefert wird (Spec 5a sieht Letzteres vor).

## 3. Weitere Communities im religionsbezogenen Umfeld

Alle mit Schlüssel und Community vorhanden; Kandidaten für Partnerkacheln und für die Ökosystem-Karte.

| Community | npub | seit | Mitglieder | Beiträge (letzter) | Eigene Events | Anmerkung |
|---|---|---|---|---|---|---|
| KuRU und Schuldek.de | `npub10dxgwerwfmjsyu9lq97pxdu4q0w3efycykhv3a9j2ut7y5l4xhkqyclpt8` | 12.10.2026 | 2 | 0 | 0 | Schuldekane-Büros und Referat 2.1 der Landeskirche Württemberg; ohne Aktivität |
| Friedenspädagogik | `npub1vsnck0crdcjdczggrlp7ng7tn6fawpdauts2wdwetsnh8s7dkcqsumc7zj` | 17.07.2026 | 8 | 9 (14.10.2026) | 8 Materialien (Konfi) | evangelischer Bildungsbereich, vermutlich die EKD-Fachstelle Friedensbildung aus dem Zwischenbericht |
| Konfiarbeit EKD | `npub1jt62efpmw02uuj58fqzgss2nxe2wvsjx48x6etvdrpa4prtp8l2s0zld3w` | 19.10.2026 | 3 | 4 (19.10.2026) | 1 Material | ALPIKA-AG Konfiarbeit, erprobt edufeed EKD-weit |
| Religionspädagogisches Institut von EKKW und EKHN | `npub1wak8hljj3szpe5g3fmak6jqspvhyn4867flrq8anlq7xfg5xjn6qtmtpsw` | 22.09.2026 | 14 | 11 (18.09.2026) | 22 Materialien | eigenes Institut mit Materialbestand |
| KPH Wien/NÖ, Zentrum Fortbildung Religion | `npub1vkn99j7kufchmgcly98lg9uexfste9epxe6jhgdt20wn4adzrvpqxhac4w` | 15.10.2026 | 22 | 22 (29.09.2026) | 18 (16 Materialien) | NIP-05 `fortbildung_religion@edufeed.org`; Österreich |
| Pilgern in der Grundschule | `npub10zn9rxfqx0fyk96gw3m5y5zlxu8t2l3epr8f4avvtw4hxxmzlhpq8cmnme` | 03.09.2026 | 1 | 0 | 1 Material | Themen-Community |
| Open Theology Hub | `npub1w5ah5an2k64yc34s0wgdk554xvcturruk0qg9prpaw02agrjhs9s0pj5jc` | 15.07.2026 | 9 | 1 (15.07.2026) | 0 | Lehrende und Forschende, OER und OEP in der Theologie |
| RpiCommunity | `npub1gc2zfp85vqe57snsevxn4u9emsq7t4l283r2p83al0s0yzujaljq466thz` | 28.10.2025 | 1 | 0 | 0 | Vorläufer von rpi-virtuell, wird stillgelegt (Entscheidung 04.11.2026); im Hub ausblenden |

## 4. Communities und Funktionsschlüssel des Ökosystems

Nicht religionsbezogen oder keine Community, aber für Ökosystem-Karte, Kalender und Nachweise relevant.

| Name | npub | Art | Zahlen | Anmerkung |
|---|---|---|---|---|
| Edufeed | `npub1hhpplya3ut9h2cyvant6pgq2w7thnkfk0hyhnz7e7gflqmy4h3yqp2p4pk` | Community seit 09.09.2026 | 119 Mitglieder, 27 Beiträge | Dach-Community der Plattform; in der App als Vorschlag beim Anmelden hinterlegt |
| e-teaching.org | `npub1tsysvvfz87826nzmfdgfrgrj6vs52td5z9ngfv6fkxmj45mlllkqanx3nv` | Community seit 07.07.2026 | 12 Mitglieder, 163 Beiträge, 313 eigene (215 Termine, 76 Materialien) | aktivste Fremd-Community; Hochschule |
| CampusCom | `npub1deah5w4wj5ke43580cp4n33zx8433gevey5xv8lfxxzf8qwyl3ss06nnst` | Community seit 05.11.2025 | 14 Mitglieder, 16 Beiträge | Hochschul-Community |
| AG Didaktische Metadaten | `npub1dnyvcxlxnpvk5r0xt7r0ww5046l4pjnd22k3adjndzf3zgl3qshqhsk6et` | Community seit 20.10.2026 | 3 Mitglieder, 3 Beiträge | NIP-05 `metadaten@edufeed.org`; Anschluss an Metadatenprofil und Vokabulare |
| Freie Bildungsflotte | `npub16mfpfl38lnq2dywapuzdz54hehd87c0edundcssa7340pw630yhqvjwt3l` | Community seit 11.11.2025 | 19 Mitglieder, 8 Beiträge | Workshop-Identität |
| HackathOERn 2026 | `npub1lcvcmzvw452sd4jen7r3j0za60pzawach6nyyws0094ltz2ezr5qae6xhj` | Community seit 11.05.2026 | 8 Mitglieder, 1 Beitrag | Veranstaltungs-Community |
| LehrerInnenZimmer | `npub1mxs2uv44xxzlkksgzpg7zyh77ufzu8h5t6wq9rfxy468reyevsts93d0x2` | Community seit 12.05.2026 | 10 Mitglieder, 0 Beiträge | Relay `dev.edufeed.org`; im Termin-Chatbot-Konzept als Beispiel |
| CoHart, Geheimclub, Testprofil (11366bab…), Einzelprofile mit Community (laoc42, joerglohrer, a6f8e9a8…, 3f4db561…), Dr. Bob Struktur, AI und Nostr Relations Lab | – | Communities ohne Hub-Bezug | – | Test-, Workshop- und Einzelprofile; nicht in die Ökosystem-Karte aufnehmen |
| News-Redaktion rpi-virtuell | `npub12jguyxp6sdanpafe3mjelezm7dtlzuxqwc4qczdkr260azqqsstq05rr6j` | Funktionsschlüssel, kein Profil, keine Community | 4025 Beiträge (`kind:30023`) | Instanz rpi-virtuell, Kerndienst News; Profil (`kind:0`) fehlt |
| BiK-Terminimport | `npub12g780vegprsdangl7ypfhjqf7rytwuws5ka4wwd6trexcjea007qqlu3mw` | Funktionsschlüssel, kein Profil | 5500 Termine | bildung-kirchen.de; seit 21.01.2026 keine neuen Events |
| relilab-impuls | `npub1lde034983zllh2nhe48lt60q6p3a6lsxn0g90uemhg0906jsnzesh5vz8y` | Profil, keine Community | Termine der Fortbildungsreihe | Zuordnung zu relilab über `h`-Tag |
| relilab-Termine-Bot | `npub17mq54dad6ewkrnunzx5xs4t4c0edur99gz7ymhu3dam0pz034fpsxjqk3d` | Profil, keine Community | Absender der relilab.org-Termine | Zuordnung zu relilab über `h`-Tag |
| Comenius-Institut | `npub1nvw4g3twxcflygxszeemmgg22q6ue8fkhua22wpwnyfq8mjanm9s6vj992` | Profil, keine Community | 0 | Profilname derzeit „CI_JD"; Institutsschlüssel? |
| Johan Amos Comenius | `npub12j35qpeve33929kg64etvw9g9rzms4c8g5gnqta58yhjdc6wryfse3phmu` | Profil, keine Community | 139 Termine, 21 Materialien | Standard-Autor im WordPress-Kalender-Block (`nostr-calendar-block`); Zweck klären |
| VocabulOER | NIP-05 `vocabuloer@edufeed.org` | Profil | – | Vokabulare (w3id); Anschluss an Metadatenprofil |
| Poutník, Antiope | NIP-05 `poutnik@edufeed.org`, `antiope@edufeed.org` | Agentenprofile | – | Coding-Agenten, keine Communities |

## 5. Fragen an die Projektleitung und Antworten

Beantwortet am 04.11.2026 (Fragen 1 bis 3), die übrigen offen.

1. **Wer hält welchen Schlüssel?** Antwort: Die Schlüssel für rpi-virtuell, relilab, reliGlobal,
   ALPIKA Grundschule, Friedenspädagogik und Konfiarbeit EKD liegen beim Projektteam
   (Comenius-Institut und edufeed); das Team kann mit allen signieren. Die Katalog-Listen
   (Frist 21./23.12.2026) können damit intern angelegt werden. Offen bleibt die Haltung der Schlüssel
   von KuRU, RPI EKKW/EKHN und KPH Wien.
2. **Materialpool:** Antwort: Die Materialpool-Ressourcen (`kind:30142`) wurden zunächst importiert
   und dann wieder gelöscht. Sie werden qualitätskriteriengeleitet und größtenteils von Hand neu
   angelegt. Folge für den Katalog rpi-virtuell: Er kann nur so viele Einträge zeigen, wie bis zum
   21.12.2026 neu angelegt sind; die Liste wächst mit der Redaktionsarbeit. Die wenigen Materialien
   auf `relay-rpi.edufeed.org` (Schlüssel „Johan Amos Comenius" und joerglohrer) sind kein Bestand.
3. **RpiCommunity (28.10.2025):** Antwort: Vorläufer von rpi-virtuell, wird stillgelegt. Im Hub
   nicht anzeigen.
4. **Profile nachrüsten:** News-Redaktion und BiK-Import haben kein Profil (`kind:0`). Ohne Profil
   erscheinen 4025 Beiträge und 5500 Termine im Hub ohne Absendernamen.
5. **Weitere Partner mit eigenem Schlüssel:** rpp-katholisch, Konfessionskundliches Institut und
   relimentar aus dem Zwischenbericht 2025 haben keinen Schlüssel auf den Relays. Partnerkachel mit
   Link (Spec 4.7) oder Schlüssel anbieten?
6. **FOERBICO als Community:** Soll der Schaufenster-Schlüssel eine Community (`kind:10222`)
   bekommen, damit Beiträge und Kommentare ihm per `h`-Tag zugeordnet werden können?

## 6. Was der Prototyp daraus übernimmt

Der Prototyp (`index.html`, Liste `CY`) führt Communities ohne Schlüssel als Schnappschuss. Mit
ADR-0006 (Live-Daten) ersetzt die Abfrage `{"kinds":[10222]}` auf `relay.edufeed.org` diese Liste;
Namen und Bilder kommen aus `kind:0`, Mitgliedschaften aus `kind:30000` (`d=communities`),
Beiträge aus `#h`. Die Zuordnung Community zu Instanz (Abschnitt 2) bleibt Konfiguration im Hub-Code.

Rohdaten der Erhebung liegen nicht im Repository; die Abfrage ist mit einem WebSocket-Skript
(REQ bis EOSE, 25 s Zeitgrenze je Relay) wiederholbar. `nak req` hängt auf diesen Relays nach dem
EOSE und ist für Bestandsabfragen ungeeignet.
