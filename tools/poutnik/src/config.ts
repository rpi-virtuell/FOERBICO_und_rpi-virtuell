// Konfiguration: Repos, Identitäten, Forgejo (config.json) und Umgebungsdatei (~/.config/poutnik/env).
// Relays, die beim Lesen gemieden werden (IP-Sperre bei vielen Subscriptions, siehe Spec 3 und 4.4).
const READ_BLOCKLIST = ['groups.edufeed.org'];
const MAX_READ_RELAYS = 3;

export type RepoConfig = {
  id: string;
  owner: string;
  coordinate: string;
  relays: string[];
  readRelays: string[];
  maintainers: string[];
  web: string;
};

export type Identity = { alias: 'joerg' | 'poutnik'; pubkey: string };

export type Config = {
  repos: Record<string, RepoConfig>;
  identities: Identity[];
  forgejo: { base: string; repos: string[]; login: string };
};

type RawRepo = Omit<RepoConfig, 'coordinate' | 'readRelays'>;
type RawConfig = { repos: Record<string, RawRepo>; identities: Identity[]; forgejo: Config['forgejo'] };

const DEFAULT_CONFIG = new URL('../config.json', import.meta.url);

export function loadConfig(path: string | URL = DEFAULT_CONFIG): Config {
  const raw = JSON.parse(Deno.readTextFileSync(path)) as RawConfig;
  const repos: Record<string, RepoConfig> = {};
  for (const [key, r] of Object.entries(raw.repos)) {
    repos[key] = {
      ...r,
      coordinate: `30617:${r.owner}:${r.id}`,
      readRelays: r.relays.filter((u) => !READ_BLOCKLIST.some((b) => u.includes(b))).slice(0, MAX_READ_RELAYS),
    };
  }
  return { repos, identities: raw.identities, forgejo: raw.forgejo };
}

export function defaultEnvPath(): string {
  const home = Deno.env.get('HOME') ?? '';
  return `${home}/.config/poutnik/env`;
}

/** Liest KEY=WERT-Zeilen; Kommentare (#) und Leerzeilen werden übersprungen, Anführungszeichen entfernt. */
export function loadEnv(path: string = defaultEnvPath()): Record<string, string> {
  const out: Record<string, string> = {};
  let text: string;
  try {
    text = Deno.readTextFileSync(path);
  } catch {
    return out;
  }
  for (const line of text.split('\n')) {
    const t = line.trim();
    if (!t || t.startsWith('#')) continue;
    const i = t.indexOf('=');
    if (i < 0) continue;
    const key = t.slice(0, i).trim();
    let val = t.slice(i + 1).trim();
    if ((val.startsWith('"') && val.endsWith('"')) || (val.startsWith("'") && val.endsWith("'"))) val = val.slice(1, -1);
    out[key] = val;
  }
  return out;
}
