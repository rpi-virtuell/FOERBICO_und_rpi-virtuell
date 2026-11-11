// Poutník-Werkzeug: threads | push | doctor | dm. Issues, Kommentare und PRs schreibt ngit (Spec 4.8);
// nur private Nachrichten (NIP-17) signiert dm selbst, über einen eigenen Amber-Bunker.
const HILFE = `Poutník – Werkzeug neben ngit

  deno task threads [--since <Tage>] [--repo <id>] [--json]   Wo stehen meine Fäden?
  deno task push <branch> --as poutnik|joerg [--cwd <klon>]   Push mit Branch-/Signer-Prüfung
  deno task doctor                                            Einrichtung prüfen
  deno task dm send <npub> (--text "…"|--file <pfad>) [--send]   DM als Poutník (ohne --send: Probelauf)
  deno task dm inbox [--since <Tage>]                         DMs an Poutník lesen
`;

const befehle: Record<string, () => Promise<(argv: string[]) => Promise<number>>> = {
  push: async () => (await import('./src/push.ts')).cmdPush,
  threads: async () => (await import('./src/threads.ts')).cmdThreads,
  doctor: async () => (await import('./src/doctor.ts')).cmdDoctor,
  dm: async () => (await import('./src/dm.ts')).cmdDm,
};

async function main(argv: string[]): Promise<number> {
  const [cmd, ...rest] = argv;
  const lade = befehle[cmd ?? ''];
  if (!lade) {
    console.error(HILFE);
    return 2;
  }
  const fn = await lade();
  return fn(rest);
}

if (import.meta.main) Deno.exit(await main(Deno.args));
