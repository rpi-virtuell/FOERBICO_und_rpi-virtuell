// Signiert unsignierte Event-Vorlagen (JSON-Objekt oder Array von Objekten) mit einem
// Schlüssel aus einer Umgebungsvariablen und sendet sie an die drei edufeed-Relays.
// Aufruf: deno run --env-file=<Pfad> --allow-env --allow-net --allow-read=<Vorlage> \
//   tools/listen/veroeffentlichen.ts <vorlage.json> <ENV_VARIABLE> [--dry-run]
// Gibt nie einen Schlüsselwert aus.
import { finalizeEvent, nip19 } from "npm:nostr-tools@2";

const RELAYS = [
  "wss://relay.edufeed.org",
  "wss://relay-rpi.edufeed.org",
  "wss://amb-relay.edufeed.org",
];
const TIMEOUT_MS = 15_000;
const PAUSE_MS = 3_000;

function fehler(msg: string): never {
  console.error(`Fehler: ${msg}`);
  Deno.exit(1);
}

function leseSchluessel(variable: string): Uint8Array {
  const wert = Deno.env.get(variable);
  if (!wert) {
    fehler(
      `Umgebungsvariable ${variable} fehlt oder ist leer (Env-Datei mit --env-file angeben).`,
    );
  }
  const w = wert.trim();
  if (w.startsWith("nsec1")) {
    try {
      const d = nip19.decode(w);
      if (d.type !== "nsec") throw new Error("kein nsec");
      return d.data as Uint8Array;
    } catch {
      fehler(`Wert in ${variable} ist kein gültiger nsec.`);
    }
  }
  if (/^[0-9a-fA-F]{64}$/.test(w)) {
    return Uint8Array.from(w.match(/../g)!.map((h) => parseInt(h, 16)));
  }
  fehler(`Wert in ${variable} ist weder nsec1… noch 64-stelliges Hex.`);
}

function senden(relay: string, ev: { id: string }): Promise<string> {
  return new Promise((resolve) => {
    let fertig = false;
    let ws: WebSocket | undefined;
    const ende = (s: string) => {
      if (fertig) return;
      fertig = true;
      clearTimeout(t);
      try {
        ws?.close();
      } catch { /* ignorieren */ }
      resolve(s);
    };
    const t = setTimeout(() => ende("Grund: Zeitüberschreitung (15 s)"), TIMEOUT_MS);
    try {
      ws = new WebSocket(relay);
    } catch {
      return ende("Grund: Verbindung nicht möglich");
    }
    ws.onopen = () => ws!.send(JSON.stringify(["EVENT", ev]));
    ws.onerror = () => ende("Grund: Verbindungsfehler");
    ws.onclose = () => ende("Grund: Verbindung geschlossen ohne OK");
    ws.onmessage = (m) => {
      try {
        const d = JSON.parse(m.data as string);
        if (d[0] === "OK" && d[1] === ev.id) {
          ende(d[2] ? "OK" : `Grund: ${d[3] ?? "abgelehnt"}`);
        }
      } catch { /* ignorieren */ }
    };
  });
}

const args = Deno.args.filter((a) => !a.startsWith("--"));
const dry = Deno.args.includes("--dry-run");
if (args.length !== 2) {
  fehler("Aufruf: veroeffentlichen.ts <vorlage.json> <ENV_VARIABLE> [--dry-run]");
}
const [datei, variable] = args;

let roh: unknown;
try {
  roh = JSON.parse(await Deno.readTextFile(datei));
} catch (e) {
  fehler(`Vorlage nicht lesbar: ${(e as Error).message}`);
}
type Vorlage = { kind: number; tags: string[][]; content: string };

function pruefe(v: unknown, pos: number): Vorlage {
  const f = (m: string): never => fehler(`${datei}, Vorlage ${pos}: ${m}`);
  if (typeof v !== "object" || v === null || Array.isArray(v)) f("kein Objekt");
  const o = v as Record<string, unknown>;
  if (!Number.isInteger(o.kind)) f("kind fehlt oder ist keine ganze Zahl");
  if (!Array.isArray(o.tags)) f("tags fehlt");
  const tags = o.tags as unknown[];
  tags.forEach((t, i) => {
    if (!Array.isArray(t) || !t.every((x) => typeof x === "string")) {
      f(`tags[${i}] ist kein Array aus Strings`);
    }
  });
  if (o.content !== undefined && typeof o.content !== "string") f("content ist kein String");
  return { kind: o.kind as number, tags: tags as string[][], content: (o.content as string) ?? "" };
}

const eintraege: unknown[] = Array.isArray(roh) ? roh : [roh];
if (eintraege.length === 0) {
  fehler(`${datei}: keine Events enthalten (leeres Array: erst Materialien eintragen).`);
}
const vorlagen = eintraege.map((v, i) => pruefe(v, i + 1));

if (dry) {
  for (const v of vorlagen) {
    console.log(
      JSON.stringify({ ...v, created_at: Math.floor(Date.now() / 1000) }, null, 2),
    );
  }
  console.log("(Trockenlauf: nichts signiert, nichts gesendet)");
  Deno.exit(0);
}

const sk = leseSchluessel(variable);
let erster = true;
for (const v of vorlagen) {
  if (!erster) await new Promise((r) => setTimeout(r, PAUSE_MS));
  erster = false;
  const ev = finalizeEvent(
    {
      kind: v.kind,
      tags: v.tags,
      content: v.content,
      created_at: Math.floor(Date.now() / 1000),
    },
    sk,
  );
  console.log(`Event ${ev.id} (kind ${ev.kind})`);
  for (const r of RELAYS) {
    console.log(`  ${r}: ${await senden(r, ev)}`);
  }
}
