// Relay-Lesen: eine Subscription je Relay, Sammeln bis EOSE oder Timeout, Deduplizierung nach id.
// Signiert nichts. Für Schreiben ist ngit zuständig (Spec 4.8).

export type NostrEvent = {
  id: string;
  kind: number;
  pubkey: string;
  created_at: number;
  tags: string[][];
  content: string;
  sig: string;
};

/** Minimale WebSocket-Oberfläche, damit Tests einen Fake einsetzen können. */
export type SocketLike = {
  onopen: (() => void) | null;
  onmessage: ((ev: { data: string }) => void) | null;
  onerror: ((e: unknown) => void) | null;
  onclose: (() => void) | null;
  send(data: string): void;
  close(): void;
};

export type SocketFactory = (url: string) => SocketLike;

export type QueryOptions = { timeoutMs?: number; socketFactory?: SocketFactory };

const defaultFactory: SocketFactory = (url) => new WebSocket(url) as unknown as SocketLike;

function queryOne(url: string, filter: object, opts: Required<QueryOptions>, sink: Map<string, NostrEvent>): Promise<string | null> {
  return new Promise((resolve) => {
    let done = false;
    let sock: SocketLike;
    const finish = (warning: string | null) => {
      if (done) return;
      done = true;
      clearTimeout(timer);
      try {
        sock.close();
      } catch { /* bereits zu */ }
      resolve(warning);
    };
    const timer = setTimeout(() => finish(`${url}: timeout nach ${opts.timeoutMs} ms`), opts.timeoutMs);
    try {
      sock = opts.socketFactory(url);
    } catch (e) {
      finish(`${url}: ${String(e)}`);
      return;
    }
    const subId = 'p' + Math.random().toString(36).slice(2, 10);
    sock.onopen = () => sock.send(JSON.stringify(['REQ', subId, filter]));
    sock.onmessage = (m) => {
      let msg: unknown[];
      try {
        msg = JSON.parse(m.data);
      } catch {
        return;
      }
      const [type, , payload] = msg as [string, string, unknown];
      if (type === 'EVENT') {
        const ev = payload as NostrEvent;
        if (ev?.id && !sink.has(ev.id)) sink.set(ev.id, ev);
      } else if (type === 'EOSE') {
        finish(null);
      } else if (type === 'CLOSED' || type === 'NOTICE') {
        finish(`${url}: ${type} ${String(msg[2] ?? msg[1] ?? '')}`.trim());
      }
    };
    sock.onerror = (e) => finish(`${url}: Fehler ${(e as { message?: string })?.message ?? ''}`.trim());
    sock.onclose = () => finish(done ? null : `${url}: Verbindung geschlossen`);
  });
}

/** Fragt alle Relays parallel ab (eine Subscription je Relay) und liefert Events ohne Duplikate plus Warnungen. */
export async function queryRelays(
  relays: string[],
  filter: object,
  opts: QueryOptions = {},
): Promise<{ events: NostrEvent[]; warnings: string[] }> {
  const full: Required<QueryOptions> = { timeoutMs: opts.timeoutMs ?? 15_000, socketFactory: opts.socketFactory ?? defaultFactory };
  const sink = new Map<string, NostrEvent>();
  const results = await Promise.all(relays.map((u) => queryOne(u, filter, full, sink)));
  return { events: [...sink.values()], warnings: results.filter((w): w is string => w !== null) };
}
