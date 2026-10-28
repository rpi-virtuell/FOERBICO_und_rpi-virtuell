// Poutník-Werkzeug: threads | push | doctor. Alles Schreibende auf Nostr macht ngit (Spec 4.8).
const HILFE = `Poutník – Werkzeug neben ngit

  deno task threads [--since <Tage>] [--repo <id>] [--json]   Wo stehen meine Fäden?
  deno task push <branch> --as poutnik|joerg [--cwd <klon>]   Push mit Branch-/Signer-Prüfung
  deno task doctor                                            Einrichtung prüfen
`;

const befehle: Record<string, () => Promise<(argv: string[]) => Promise<number>>> = {
  push: async () => (await import('./src/push.ts')).cmdPush,
  threads: async () => (await import('./src/threads.ts')).cmdThreads,
  doctor: async () => (await import('./src/doctor.ts')).cmdDoctor,
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
