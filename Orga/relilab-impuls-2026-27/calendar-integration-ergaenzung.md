## 2.6 Community assignment before attributes

A calendar event rarely belongs to one institution alone. The `relilab Impuls` series
is run jointly by institutes in Baden, the Palatinate and the Saarland; a single session
may have one host, a speaker from a second institute and participants registering through
four different systems.

Do **not** model these relationships as tags. They belong in the community graph, where
they can be curated, signed and revoked independently of the event:

- **Institutions and series are communities** (kind `10222`). Name, logo and description
  live in the community's kind `0` and are maintained once.
- **Content joins a community** through an `["h", "<community-pubkey>"]` tag on the event
  itself, or through a kind `16` repost carrying that tag. The older kind `30222` targeted
  publication is legacy: readers still honour it, nothing writes it any more.
- **Who may publish** is decided at read time against the community's roster, per content
  section. A moderated community declares `["access", "members"]` or
  `["access", "role", "<role>"]`; a client drops events whose author is not currently
  allowed. Removing a publisher therefore removes their events from the community view
  without deleting anything.

This is what makes a migration path possible. A crawler and a curated publisher can be
members of the same community at the same time; when the curated events are complete,
dropping the crawler from the roster retires its events from the community view in one
step, while they remain on the relays.

See `communikey` for the normative tag grammar.

## 2.7 Registration

Section 2.1 states that registration details belong in the description text. That holds
for a single organiser. It breaks as soon as a course is offered jointly, because each
participating state has its own registration system and accreditation:

```
["registrationRequired", "true"]
["registrationUrl", "https://evewa.bildung-rp.de/workflow?id=0&va_id=4153", "DE-RP", "Anmeldung Rheinland-Pfalz (eVEWA)"]
["registrationUrl", "https://bildungsportal.ekiba.de/", "DE-BW", "Anmeldung Baden (Ekiba-Bildungsportal)"]
["registrationUrl", "https://www.rpz-igb.de/", "DE-SL", "Anmeldung Saarland (RPZ St. Ingbert)"]
["registrationUrl", "https://relilab.org/relilab-impuls/", "", "Alle übrigen Länder"]
["registrationDeadline", "1808949540"]
```

| Position | Meaning |
| --- | --- |
| 1 | Registration URL |
| 2 | `eligibleRegion` as ISO 3166-2, empty = everywhere |
| 3 | Human-readable label |

A client renders the entry matching its own region and falls back to the unrestricted one.
`registrationDeadline` is a Unix timestamp; both eVEWA and the Ekiba portal carry it today,
and it is the one field where an error is silently fatal — a deadline after the event
turns registration off without anyone noticing.

Registration stays where it is. The description becomes shared, the enrolment systems
remain untouched.

## 2.8 People

Section 2.4 covers `organizer` and `attendee`. Teaching events additionally need the
person who actually delivers the session, and that person frequently belongs to a
different institution than the organiser:

```
["p", "<organizer pubkey hex>", "wss://relay.edufeed.org", "organizer"]
["p", "<speaker pubkey hex>", "wss://relay.edufeed.org", "performer"]
["p", "<coordinator pubkey hex>", "wss://relay.edufeed.org", "contributor"]
```

Roles are taken from schema.org: `organizer`, `performer` (the speaker), `contributor`
(coordination, moderation), `contactPoint`.

Most speakers have no key yet. Rather than leaving them out — which is how a name ends up
retyped, and misspelled, in every downstream system — record them in the AMB flattened
form alongside, and add the `p` tag once a key exists:

```
["performer:name", "Juliane Kleibert"]
["performer:type", "Person"]
["performer:affiliation:name", "RPI Karlsruhe"]
```

The `p` tag is authoritative where present; the flattened form is what NIP-52 clients
without key resolution can display.

## 2.9 External identifiers

`d` should be a stable slug chosen by the publisher, not a source URL. Source systems
change URLs, several systems hold the same course under different URLs, and two different
courses may share a title — an institute's own event and the joint session on the same
subject.

Carry every external key as an identifier instead, using the schema.org `PropertyValue`
pair flattened:

```
["identifier:propertyID", "eVEWA"]
["identifier:value", "27EA890004"]
["identifier:propertyID", "Kufer"]
["identifier:value", "26PTZ-118"]
```

This is what lets a consumer recognise that an export from an enrolment system and a
curated event describe the same session, and that a similarly titled event does not.
In practice these numbers already circulate as the de-facto shared reference — printed in
flyers, quoted in image credits — they just have no field to live in.

## 2.10 Event status

An event that is cancelled must stay visible and say so. NIP-09 deletion is wrong here:
it removes the event instead of marking it, and participants who registered would simply
see it disappear.

```
["eventStatus", "https://schema.org/EventScheduled"]
```

Values are taken exactly from schema.org: `EventScheduled`, `EventCancelled`,
`EventPostponed`, `EventRescheduled`, `EventMovedOnline`. Absent means `EventScheduled`.

## 2.11 Image licence

`image` carries a URL only. In an open data space an image without a licence cannot be
redistributed — consumers must either drop it or risk passing on material they have no
right to. This is not hypothetical: image credits in this field routinely read
"generated with AI and Canva" or "CC0 via iStock", neither of which permits redistribution.

```
["image", "https://blossom.edufeed.org/<sha256>.webp"]
["image:license:id", "https://creativecommons.org/licenses/by/4.0/"]
["image:creator:name", "Olav Richter"]
["image:description", "Alt text describing what is shown"]
["image:ai", "generated"]
```

`image:ai` takes `generated` or `modified`, following the EU AI Office icons for
labelling AI-generated content; see `license-events-nope`. Note that an AI label does not
replace the licence: prompting a model does not clear the rights to stock material used
as input.

Convention: **a client shows a community's fallback motif when `image:license:id` is
absent.** This turns rights clearance into something visible rather than something
enforced — an image appears on every downstream site once its licence is declared.

Where the file is hosted on Blossom, the `x` hash additionally links the event to its
kind `1063` licence attestation, so the licence travels with the bytes.

## 2.12 Educational level and audience

`educationalLevel` as used in 2.5 describes the type of the event
(`level_C` = Fortbildung/professional development) and stays as it is.

What it must not also carry is the school level the content is *about* — a teacher
training session on primary school material is `level_C` as an event and primary school
by subject. Overloading one field makes both unusable for filtering. Use `about` for the
subject level, and the KIM vocabulary "Intended End User Role" for the audience:

```
["educationalLevel:id", "https://w3id.org/kim/educationalLevel/level_C"]
["educationalLevel:prefLabel:de", "Fortbildung"]
["about:id", "https://w3id.org/kim/educationalLevel/level_2"]
["about:prefLabel:de", "Sekundarstufe I"]
["audience:id", "http://purl.org/dcx/lrmi-vocabs/intendedEndUserRole/teacher"]
["audience:prefLabel:de", "Lehrende"]
```

Source systems describe their audiences in free text and no two agree — "Lehrerinnen und
Lehrer", "Lehrkräfte, Pfarrer:innen, Diakon:innen", plus school types as a separate axis.
A controlled vocabulary is what makes them comparable across institutions.

## 2.13 Series and multi-session courses

Two different things are easily confused:

- **A series** — which sessions belong to `relilab Impuls 2026/27` — is community
  membership, not a calendar. Model it with `h` tags (2.6). Membership can then be
  asserted and revoked by each partner independently, which matters when the partners
  disagree about what belongs to the series.
- **A multi-session course** — one enrolment, several dates — is a genuine calendar:
  kind `31924` with `a` references to each session's `31923`.

