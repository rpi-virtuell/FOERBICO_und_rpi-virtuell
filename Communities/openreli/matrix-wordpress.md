# Matrix Chat Widget – Dokumentation

**Projekt:** Öffentliche Leseanzeige eines Matrix-Raums auf einer WordPress-Seite  
**Homeserver:** `matrix.rpi-virtuell.de`  
**Element-Client:** `element.rpi-virtuell.de`  
**Raum-ID:** `!NQPmoqtLSjGzdtLaXO:rpi-virtuell.de`  
**Stand:** März 2026

---

## Kontext und Problemlage

Ziel war es, einen öffentlichen Matrix-Raum als Leseanzeige (kein Login für Besucher:innen erforderlich) in eine WordPress-Seite einzubetten. Dabei wurden folgende Wege geprüft und verworfen:

**Matrix Public Archive / Matrix Viewer** – wurde eingestellt.

**matrix-live (live.hello-matrix.net)** – funktioniert nur mit Homeservern, die Guest Access aktiviert haben.

**Guest Access** – auf `matrix.rpi-virtuell.de` nicht aktiviert; auf `matrix.org` seit Januar 2025 abgeschaltet.

**Element Web als iFrame** – `app.element.io` und die meisten selbst gehosteten Instanzen setzen `X-Frame-Options: DENY` und können nicht eingebettet werden.

**Gewählte Lösung:** Ein eigenständiges HTML/JS-Widget, das direkt die Matrix Client-Server API abfragt. Voraussetzung ist ein dedizierter Bot-Account mit Lesezugriff, dessen Token fest im Widget hinterlegt ist. Das ist unkritisch, da der Token nur Lesezugriff auf einen öffentlichen Raum hat.

---

## Voraussetzungen

### 1. Raum auf „world_readable" setzen

In Element: **Raumeinstellungen → Sicherheit & Datenschutz → „Wer kann den Verlauf lesen?" → „Jeder"**

Ohne diese Einstellung antwortet die API mit HTTP 403.

### 2. Bot-Account anlegen und Token holen

Einen dedizierten Account (z. B. `@openrelibot:rpi-virtuell.de`) anlegen und einmalig per API einloggen:

```bash
curl -X POST https://matrix.rpi-virtuell.de/_matrix/client/v3/login \
  -H "Content-Type: application/json" \
  -d '{"type":"m.login.password","user":"openrelibot","password":"PASSWORT"}'
```

Die Antwort enthält `access_token` – dieser wird im Widget als `TOKEN` eingetragen.

> **Hinweis:** Da der Token in einem Chatprotokoll sichtbar war, sollte er bei nächster Gelegenheit rotiert werden (siehe Abschnitt Token-Rotation).

---

## Einbindung in WordPress

Gutenberg-Editor → Block **„Benutzerdefiniertes HTML"** → vollständigen Widget-Code einfügen → Speichern.

Kein Plugin erforderlich. Der Code ist vollständig eigenständig (kein externes CDN, keine Abhängigkeiten).

---

## Vollständiger Code

```html
<!-- 
  Matrix Chat Widget für rpi-virtuell.de
  Mit Thread- und Reply-Unterstützung (eingerückt + ausklappbar)
  Bearbeitete Nachrichten werden dedupliziert und mit "(bearbeitet)" markiert.

  VORAUSSETZUNG: Raumeinstellungen → Sicherheit → "Verlauf: Jeder" (world_readable)
  EINBINDUNG: Gutenberg-Block "Benutzerdefiniertes HTML"
-->

<div id="matrix-widget-wrapper">
  <div id="matrix-chat-header">
    <div id="matrix-header-left">
      <div id="matrix-room-avatar" class="matrix-room-avatar-placeholder"></div>
      <span id="matrix-room-name">Chat wird geladen…</span>
    </div>
    <span id="matrix-status" class="matrix-dot loading"></span>
  </div>
  <div id="matrix-messages"></div>
  <div id="matrix-chat-footer">
    <a href="https://element.rpi-virtuell.de/#/room/!NQPmoqtLSjGzdtLaXO:rpi-virtuell.de"
       target="_blank" rel="noopener">
      ✏️ Mitschreiben in Element
    </a>
  </div>
</div>

<style>
#matrix-widget-wrapper {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  overflow: hidden;
  max-width: 700px;
  margin: 1em 0;
  background: #fff;
}
#matrix-chat-header {
  background: #0dbd8b;
  color: white;
  padding: 10px 16px;
  font-weight: 600;
  font-size: 0.95em;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
#matrix-header-left {
  display: flex;
  align-items: center;
  gap: 10px;
}
.matrix-room-avatar-placeholder {
  width: 36px; height: 36px;
  border-radius: 8px;
  background: rgba(255,255,255,0.25);
  flex-shrink: 0;
}
#matrix-room-avatar img {
  width: 36px; height: 36px;
  border-radius: 8px;
  object-fit: cover;
  display: block;
}
.matrix-dot {
  width: 10px; height: 10px;
  border-radius: 50%;
  display: inline-block;
  flex-shrink: 0;
}
.matrix-dot.loading { background: #fff8; animation: pulse 1s infinite; }
.matrix-dot.ok      { background: #4caf50; }
.matrix-dot.error   { background: #f44336; }
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.4} }

#matrix-messages {
  height: 420px;
  overflow-y: auto;
  padding: 12px 16px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  background: #fafafa;
}

/* ── Nachricht (Top-Level) ─────────────────────────── */
.matrix-msg {
  display: flex;
  gap: 10px;
  align-items: flex-start;
  animation: fadeIn .2s ease;
}
@keyframes fadeIn { from{opacity:0;transform:translateY(4px)} to{opacity:1;transform:none} }

.matrix-avatar {
  width: 36px; height: 36px;
  border-radius: 50%;
  color: white;
  font-size: 0.8em;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  text-transform: uppercase;
  overflow: hidden;
}
.matrix-avatar img {
  width: 36px; height: 36px;
  object-fit: cover;
  border-radius: 50%;
  display: block;
}
.matrix-bubble {
  background: white;
  border: 1px solid #e8e8e8;
  border-radius: 0 10px 10px 10px;
  padding: 6px 10px;
  max-width: 85%;
  flex: 1;
  min-width: 0;
}
.matrix-sender {
  font-size: 0.75em;
  font-weight: 600;
  color: #0dbd8b;
  margin-bottom: 2px;
}
.matrix-text {
  font-size: 0.9em;
  color: #333;
  line-height: 1.4;
  word-break: break-word;
}
.matrix-time {
  font-size: 0.7em;
  color: #aaa;
  margin-top: 2px;
}
.matrix-edited {
  font-style: italic;
  color: #bbb;
}

/* ── Klassische Reply-Vorschau (zitierter Text) ────── */
.matrix-reply-preview {
  font-size: 0.78em;
  color: #888;
  border-left: 3px solid #0dbd8b;
  padding: 2px 6px;
  margin-bottom: 4px;
  border-radius: 0 4px 4px 0;
  background: #f0faf6;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* ── Thread-Toggle-Button ──────────────────────────── */
.matrix-thread-toggle {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  margin-top: 5px;
  font-size: 0.75em;
  color: #0dbd8b;
  cursor: pointer;
  user-select: none;
  background: none;
  border: none;
  padding: 0;
  font-family: inherit;
}
.matrix-thread-toggle:hover { text-decoration: underline; }
.matrix-thread-toggle .arrow { display: inline-block; transition: transform .2s; }
.matrix-thread-toggle.open .arrow { transform: rotate(90deg); }

/* ── Thread-Container (eingerückte Replies) ────────── */
.matrix-thread {
  display: none;
  margin-top: 4px;
  margin-left: 46px; /* avatar-breite + gap */
  border-left: 2px solid #d0f0e6;
  padding-left: 10px;
  gap: 4px;
  flex-direction: column;
}
.matrix-thread.open { display: flex; }

/* Thread-Replies: kleinere Avatare */
.matrix-thread .matrix-msg { gap: 7px; }
.matrix-thread .matrix-avatar {
  width: 26px; height: 26px;
  font-size: 0.7em;
}
.matrix-thread .matrix-avatar img { width: 26px; height: 26px; }
.matrix-thread .matrix-bubble {
  border-radius: 0 8px 8px 8px;
  padding: 4px 8px;
}
.matrix-thread .matrix-sender { font-size: 0.72em; }
.matrix-thread .matrix-text   { font-size: 0.85em; }
.matrix-thread .matrix-time   { font-size: 0.68em; }

/* ── Eingerückte klassische Reply (kein Thread) ────── */
.matrix-reply-indent {
  margin-left: 46px;
  border-left: 2px solid #e0e0e0;
  padding-left: 10px;
}
.matrix-reply-indent .matrix-avatar { width: 26px; height: 26px; font-size: 0.7em; }
.matrix-reply-indent .matrix-avatar img { width: 26px; height: 26px; }

/* ── Footer ────────────────────────────────────────── */
#matrix-chat-footer {
  padding: 8px 16px;
  background: #f5f5f5;
  border-top: 1px solid #e0e0e0;
  font-size: 0.82em;
  text-align: right;
}
#matrix-chat-footer a { color: #0dbd8b; text-decoration: none; }
#matrix-chat-footer a:hover { text-decoration: underline; }
.matrix-error-msg {
  color: #888;
  font-size: 0.85em;
  text-align: center;
  padding: 20px;
}
</style>

<script>
(function() {
  const HOMESERVER   = 'https://matrix.rpi-virtuell.de';
  const ROOM_ID      = '!NQPmoqtLSjGzdtLaXO:rpi-virtuell.de';
  const LIMIT        = 40;
  const POLL_SEC     = 30;
  const TOKEN        = 'syt_b3BlbnJlbGlib3Q_SdFwxHEkUplXymuZJcPD_1Vvd2k';
  const HEADERS      = { 'Authorization': 'Bearer ' + TOKEN };

  const messagesEl   = document.getElementById('matrix-messages');
  const statusEl     = document.getElementById('matrix-status');
  const nameEl       = document.getElementById('matrix-room-name');
  const roomAvatarEl = document.getElementById('matrix-room-avatar');
  const avatarCache  = {};

  // ── Hilfsfunktionen ──────────────────────────────────────────

  const COLORS = ['#0dbd8b','#5c56f5','#e06c75','#d19a66','#61afef','#56b6c2','#c678dd'];
  function colorFor(sender) {
    let h = 0;
    for (let c of sender) h = (h * 31 + c.charCodeAt(0)) & 0xffffffff;
    return COLORS[Math.abs(h) % COLORS.length];
  }
  function localpart(mxid) {
    const m = mxid.match(/^@([^:]+):/);
    return m ? m[1] : mxid;
  }
  function formatTime(ts) {
    return new Date(ts).toLocaleTimeString('de-DE', {hour:'2-digit', minute:'2-digit'});
  }
  function escapeHtml(str) {
    return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  }
  function mxcToHttp(mxc) {
    if (!mxc || !mxc.startsWith('mxc://')) return null;
    return HOMESERVER + '/_matrix/media/v3/download/' + mxc.slice(6);
  }

  // ── Raum-Metadaten ───────────────────────────────────────────

  async function fetchRoomAvatar() {
    try {
      const res = await fetch(HOMESERVER + '/_matrix/client/v3/rooms/' + encodeURIComponent(ROOM_ID) + '/state/m.room.avatar/', { headers: HEADERS });
      if (res.ok) {
        const data = await res.json();
        const http = mxcToHttp(data.url);
        if (http) roomAvatarEl.innerHTML = '<img src="' + http + '" alt="Raumlogo">';
      }
    } catch(_) {}
  }

  async function fetchRoomName() {
    try {
      const res = await fetch(HOMESERVER + '/_matrix/client/v3/rooms/' + encodeURIComponent(ROOM_ID) + '/state/m.room.name/', { headers: HEADERS });
      if (res.ok) {
        const data = await res.json();
        if (data.name) nameEl.textContent = data.name;
      }
    } catch(_) {}
  }

  // ── Benutzer-Avatare ─────────────────────────────────────────

  async function getUserAvatarUrl(mxid) {
    if (mxid in avatarCache) return avatarCache[mxid];
    try {
      const res = await fetch(HOMESERVER + '/_matrix/client/v3/profile/' + encodeURIComponent(mxid) + '/avatar_url', { headers: HEADERS });
      if (res.ok) {
        const data = await res.json();
        const http = mxcToHttp(data.avatar_url);
        avatarCache[mxid] = http;
        return http;
      }
    } catch(_) {}
    avatarCache[mxid] = null;
    return null;
  }

  // ── DOM-Hilfsfunktion: Nachrichtenzeile bauen ─────────────────

  function buildMsgEl(e, small) {
    const sender    = localpart(e.sender);
    const initials  = escapeHtml(sender.slice(0, 2));
    const color     = colorFor(e.sender);
    const avatarUrl = avatarCache[e.sender];
    const size      = small ? 26 : 36;

    const avatarInner = avatarUrl
      ? '<img src="' + avatarUrl + '" alt="' + initials + '" width="' + size + '" height="' + size + '" onerror="this.parentElement.style.background=\'' + color + '\';this.outerHTML=\'' + initials + '\'">'
      : initials;
    const avatarStyle = avatarUrl ? '' : 'background:' + color + ';';

    // Reply-Vorschau: zitierter Text aus m.in_reply_to
    // Element bettet Zitat als "> Text\n\nAntwort" in den body ein
    let replyPreview = '';
    const rel = e.content && e.content['m.relates_to'];
    const isReply = rel && rel['m.in_reply_to'] && (!rel.rel_type || rel.rel_type !== 'm.thread');
    if (isReply) {
      const body = e.content.body || '';
      const parts = body.split('\n\n');
      if (parts.length > 1) {
        const quoted = parts.slice(0, -1).join(' ').replace(/^>?\s*/gm, '').trim();
        if (quoted) {
          replyPreview = '<div class="matrix-reply-preview">' + escapeHtml(quoted.slice(0, 80)) + '</div>';
        }
      }
    }

    // Nachrichtentext: bei Replies nur den Teil nach dem Zitat
    let displayBody = e.content.body || '';
    if (isReply) {
      const parts = displayBody.split('\n\n');
      if (parts.length > 1) displayBody = parts[parts.length - 1];
    }

    const div = document.createElement('div');
    div.className = 'matrix-msg';
    div.setAttribute('data-event-id', e.event_id);
    div.innerHTML =
      '<div class="matrix-avatar" style="' + avatarStyle + '">' + avatarInner + '</div>' +
      '<div class="matrix-bubble">' +
        replyPreview +
        '<div class="matrix-sender">' + escapeHtml(sender) + '</div>' +
        '<div class="matrix-text">'   + escapeHtml(displayBody) + '</div>' +
        '<div class="matrix-time">'   + formatTime(e.origin_server_ts) +
          (e._edited ? ' <span class="matrix-edited">(bearbeitet)</span>' : '') +
        '</div>' +
      '</div>';
    return div;
  }

  // ── Rendering ────────────────────────────────────────────────

  async function renderMessages(events) {
    messagesEl.innerHTML = '';

    // ── Edit-Deduplizierung ─────────────────────────────────────
    // m.replace-Events (rel_type: "m.replace") enthalten den neuen Text in
    // content['m.new_content']. Pro Original-ID wird das neueste Replace-Event
    // ermittelt, dessen Inhalt dann das Original überschreibt. Die Replace-Events
    // selbst werden aus der Anzeigeliste herausgefiltert.
    const latestEdit = {};
    events.forEach(function(e) {
      if (e.type !== 'm.room.message') return;
      const rel = e.content && e.content['m.relates_to'];
      if (rel && rel.rel_type === 'm.replace' && rel.event_id) {
        const orig = rel.event_id;
        if (!latestEdit[orig] || e.origin_server_ts > latestEdit[orig].origin_server_ts) {
          latestEdit[orig] = e;
        }
      }
    });

    const patchedEvents = events
      .filter(function(e) {
        if (e.type !== 'm.room.message') return false;
        const rel = e.content && e.content['m.relates_to'];
        if (rel && rel.rel_type === 'm.replace') return false;
        return true;
      })
      .map(function(e) {
        const edit = latestEdit[e.event_id];
        if (!edit) return e;
        const newContent = edit.content['m.new_content'] || {};
        return Object.assign({}, e, {
          content: Object.assign({}, newContent, { '_edited': true }),
          _edited: true
        });
      });

    const msgs = patchedEvents.slice(-LIMIT);

    if (!msgs.length) {
      messagesEl.innerHTML = '<p class="matrix-error-msg">Noch keine Nachrichten.</p>';
      return;
    }

    // Avatare parallel vorladen
    const senders = [...new Set(msgs.map(function(e) { return e.sender; }))];
    await Promise.all(senders.map(getUserAvatarUrl));

    // Nachrichten aufteilen: Top-Level vs. Thread-Kinder
    const byId     = {};
    const threads  = {};
    const topLevel = [];

    msgs.forEach(function(e) { byId[e.event_id] = e; });

    msgs.forEach(function(e) {
      const rel = e.content && e.content['m.relates_to'];
      if (rel && rel.rel_type === 'm.thread' && rel.event_id) {
        const rootId = rel.event_id;
        if (!threads[rootId]) threads[rootId] = [];
        threads[rootId].push(e);
      } else {
        topLevel.push(e);
      }
    });

    // Top-Level rendern
    topLevel.forEach(function(e) {
      const wrapper = document.createElement('div');
      const rel = e.content && e.content['m.relates_to'];
      const isClassicReply = rel && rel['m.in_reply_to'] && (!rel.rel_type || rel.rel_type !== 'm.thread');
      if (isClassicReply) wrapper.className = 'matrix-reply-indent';

      wrapper.appendChild(buildMsgEl(e, isClassicReply));

      const children = threads[e.event_id];
      if (children && children.length > 0) {
        const toggle = document.createElement('button');
        toggle.className = 'matrix-thread-toggle';
        toggle.innerHTML = '<span class="arrow">▶</span> ' + children.length +
          ' Antwort' + (children.length > 1 ? 'en' : '') + ' im Thread';

        const threadEl = document.createElement('div');
        threadEl.className = 'matrix-thread';
        children.forEach(function(child) { threadEl.appendChild(buildMsgEl(child, true)); });

        toggle.addEventListener('click', function() {
          const open = threadEl.classList.toggle('open');
          toggle.classList.toggle('open', open);
          toggle.querySelector('.arrow').textContent = open ? '▼' : '▶';
        });

        const bubble = wrapper.querySelector('.matrix-bubble');
        if (bubble) bubble.appendChild(toggle);
        wrapper.appendChild(threadEl);
      }

      messagesEl.appendChild(wrapper);
    });

    // Thread-Kinder deren Root außerhalb des Ladefensters liegt
    msgs.forEach(function(e) {
      const rel = e.content && e.content['m.relates_to'];
      if (rel && rel.rel_type === 'm.thread' && rel.event_id && !byId[rel.event_id]) {
        const wrap = document.createElement('div');
        wrap.className = 'matrix-reply-indent';
        wrap.appendChild(buildMsgEl(e, true));
        messagesEl.appendChild(wrap);
      }
    });

    messagesEl.scrollTop = messagesEl.scrollHeight;
  }

  // ── Nachrichten laden ─────────────────────────────────────────

  async function fetchMessages() {
    try {
      const url = HOMESERVER + '/_matrix/client/v3/rooms/' + encodeURIComponent(ROOM_ID) +
        '/messages?dir=b&limit=' + (LIMIT * 3);
      const res = await fetch(url, { headers: HEADERS });

      if (res.status === 403) {
        messagesEl.innerHTML = '<p class="matrix-error-msg">Raum nicht öffentlich lesbar.<br>' +
          'Element: Raumeinstellungen → Sicherheit → Verlauf: Jeder</p>';
        statusEl.className = 'matrix-dot error';
        return;
      }
      if (!res.ok) throw new Error(res.status);

      const data = await res.json();
      await renderMessages((data.chunk || []).reverse());
      statusEl.className = 'matrix-dot ok';
    } catch(err) {
      statusEl.className = 'matrix-dot error';
      if (!messagesEl.querySelector('.matrix-error-msg')) {
        messagesEl.innerHTML = '<p class="matrix-error-msg">Verbindung fehlgeschlagen (' + err.message + ')</p>';
      }
    }
  }

  fetchRoomName();
  fetchRoomAvatar();
  fetchMessages();
  setInterval(fetchMessages, POLL_SEC * 1000);
})();
</script>
```

---

## Technische Dokumentation

### Architektur

Das Widget ist eine einzelne, vollständig eigenständige HTML-Datei ohne externe Abhängigkeiten. Es kommuniziert direkt mit der Matrix Client-Server API (v3) des Homeservers per `fetch()`.

```
Browser → fetch() → matrix.rpi-virtuell.de/_matrix/client/v3/...
                  → /_matrix/media/v3/download/... (Bilder)
```

### Verwendete API-Endpunkte

| Endpunkt | Zweck |
|---|---|
| `GET /rooms/{roomId}/state/m.room.name/` | Raumname laden |
| `GET /rooms/{roomId}/state/m.room.avatar/` | Raumlogo laden (mxc-URL) |
| `GET /rooms/{roomId}/messages?dir=b&limit=N` | Letzte Nachrichten abrufen |
| `GET /profile/{userId}/avatar_url` | Benutzer-Avatar laden (mxc-URL) |
| `GET /_matrix/media/v3/download/{server}/{id}` | Mediendatei (Bild) abrufen |

Alle Requests senden den `Authorization: Bearer {TOKEN}` Header, da der Homeserver auch für world-readable Räume Authentifizierung verlangt (HTTP 401 ohne Token).

### Konfigurationsparameter

```javascript
const HOMESERVER = 'https://matrix.rpi-virtuell.de'; // Matrix-Homeserver
const ROOM_ID    = '!NQPmoqtLSjGzdtLaXO:rpi-virtuell.de'; // Raum-ID
const LIMIT      = 40;   // Anzahl angezeigter Top-Level-Nachrichten
const POLL_SEC   = 30;   // Polling-Intervall in Sekunden
const TOKEN      = '...'; // Access Token des Bot-Accounts
```

### Nachrichten-Typen und Darstellung

Das Widget unterscheidet vier Typen von Events anhand des `m.relates_to`-Feldes:

**Normale Nachricht** – kein `m.relates_to` → wird auf Top-Level gerendert.

**Bearbeitete Nachricht** (`rel_type: "m.replace"`) → wird nicht als separate Nachricht angezeigt. Stattdessen überschreibt das neueste Replace-Event den Inhalt der Originalnachricht. In der Zeitzeile erscheint kursiv *(bearbeitet)*.

**Klassische Reply** (`m.in_reply_to`, kein `rel_type: m.thread`) → wird um 46 px eingerückt dargestellt, mit grauer linker Borderlinie und einer grünen Zitiervorschau des Originaltexts. Element bettet den zitierten Text als `> Zitat\n\nAntwort` in den `body` ein – das Widget extrahiert dieses Muster per `split('\n\n')`.

**Thread-Reply** (`rel_type: "m.thread"`, `event_id` = Root-Event-ID) → wird unter der Root-Nachricht gesammelt und erst nach Klick auf den Toggle-Button sichtbar. Der aufgeklappte Thread-Container hat eine grüne linke Borderlinie und kleinere Avatare (26 px statt 36 px).

### Rendering-Pipeline

```
fetchMessages()
  → API: /messages?dir=b&limit=120
  → events.reverse()                  // chronologisch sortieren
  → Edit-Deduplizierung:
      latestEdit{} sammeln (m.replace)
      Replace-Events herausfiltern
      Originale mit m.new_content patchen + _edited:true
  → patchedEvents.slice(-40)          // letzte 40 behalten
  → getUserAvatarUrl() parallel       // Avatare vorladen
  → Sortierung: byId{}, threads{}, topLevel[]
  → topLevel.forEach → buildMsgEl()
      → threads[e.event_id] → Toggle + threadEl
  → Orphan-Thread-Kinder anhängen
```

Das Ladefenster (`limit = LIMIT * 3 = 120`) ist größer als die angezeigten 40 Nachrichten, um sicherzustellen, dass zu den angezeigten Top-Level-Nachrichten auch ihre zugehörigen Edit- und Thread-Events im selben API-Response enthalten sind.

### mxc-URLs

Matrix speichert Mediendateien intern als `mxc://server/id`. Die Funktion `mxcToHttp()` konvertiert diese in reguläre HTTPS-URLs:

```
mxc://rpi-virtuell.de/AbcXyz
→ https://matrix.rpi-virtuell.de/_matrix/media/v3/download/rpi-virtuell.de/AbcXyz
```

### Avatar-Caching

Um bei jedem Polling-Zyklus unnötige API-Aufrufe zu vermeiden, werden User-Avatare in einem In-Memory-Objekt `avatarCache` gespeichert (`mxid → URL | null`). Pro Rendering-Durchlauf werden alle einzigartigen Absender parallel vorgeladen (`Promise.all`), bevor die Nachrichten gerendert werden.

### Fallback-Logik für Avatare

Ist kein Profilbild hinterlegt oder schlägt das Laden fehl (`onerror`), zeigt das Widget einen farbigen Kreis mit den ersten zwei Buchstaben des Localparts. Die Farbe wird deterministisch per Hash-Funktion aus der vollständigen MXID berechnet – dieselbe Person hat immer dieselbe Farbe.

### XSS-Schutz

Alle aus der API stammenden Texte (Absendername, Nachrichtentext, Zitiervorschau) werden durch `escapeHtml()` bereinigt, bevor sie per `innerHTML` eingefügt werden. Bilder werden nur als `<img src="...">` eingebettet, nie als HTML aus dem Event-Content übernommen.

### Statusanzeige

Der kleine Punkt oben rechts im Header zeigt den Verbindungsstatus:

- 🟡 pulsierend – Ladevorgang
- 🟢 grün – letzter API-Aufruf erfolgreich
- 🔴 rot – Fehler (403 Forbidden oder Netzwerkfehler)

### Polling statt WebSocket

Das Widget verwendet Polling alle 30 Sekunden statt einer persistenten WebSocket-Verbindung (`/sync`). Begründung: WordPress-Seiten haben oft viele gleichzeitige Besucher:innen. Ein dauerhafter Sync-Kanal pro Seitenaufruf würde den Homeserver stark belasten. Polling ist hier ausreichend und deutlich ressourcenschonender.

---

## Anpassungsmöglichkeiten

**Höhe des Chat-Bereichs** – CSS: `#matrix-messages { height: 420px; }`

**Anzahl der Nachrichten** – `const LIMIT = 40;`

**Polling-Frequenz** – `const POLL_SEC = 30;` (nicht unter 10 setzen)

**Farbe des Headers** – `#matrix-chat-header { background: #0dbd8b; }` (Matrix-Grün)

**„Mitschreiben"-Link** – URL im `<a href="...">` im HTML-Teil anpassen

---

## Token-Rotation

Da der Token im Klartext im Code steht, sollte er bei Bedarf rotiert werden:

```bash
# Alten Token invalidieren
curl -X POST https://matrix.rpi-virtuell.de/_matrix/client/v3/logout \
  -H "Authorization: Bearer ALTERTOKEN"

# Neuen Token holen
curl -X POST https://matrix.rpi-virtuell.de/_matrix/client/v3/login \
  -H "Content-Type: application/json" \
  -d '{"type":"m.login.password","user":"openrelibot","password":"PASSWORT"}'
```

Neuen `access_token` im Code als `TOKEN` einsetzen und WordPress-Seite aktualisieren.
