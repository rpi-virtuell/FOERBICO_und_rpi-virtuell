#!/usr/bin/env python3
"""Setzt in den Fassungen unter Orga/issue-ueberarbeitung/ Hyperlinks auf Issues,
Pull Requests, Meilensteine, Dateien im Repo und Nachbar-Repos.
Aufruf: python3 verlinken.py <datei.md> [...]   (schreibt die Dateien um)"""
import os, re, sys

FORGE = 'https://git.rpi-virtuell.de/Comenius-Institut/'
OFFEN = FORGE + 'FOERBICO_und_rpi-virtuell'
GESCHL = FORGE + 'FOERBICO_und_rpi-virtuell-geschlossen'
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

# Forgejo-Meilenstein-IDs (offenes Repo | geschlossenes Repo), Schlüssel = AP-Kurzform
MEILENSTEINE = {
    'AP 1-1 + 1-2': (5, 204), 'AP 1-1': (5, 204), 'AP 1-3 + AP 1-4': (6, 205), 'AP 1-2': (6, 205),
    'AP 2-1': (82, 167), 'AP 2-2': (84, 169), 'AP 2-3': (85, 170), 'AP 2-4': (121, 206),
    'AP 3-1': (9, 164), 'AP 3-2 + 3-3': (83, 182), 'AP 3': (7, 196),
    'AP 4-1': (80, 166), 'AP 4-2': (88, 173), 'AP 4-3 + 4-4': (90, 175), 'AP 4-5': (99, 183),
    'AP 4-6': (115, 200), 'AP 4-7': (101, 185),
    'AP 5-1': (89, 174), 'AP 5-2': (97, 181),
    'AP 6-1': (91, 176), 'AP 6-2': (94, 180), 'AP 6-3': (100, 184), 'AP 6-4': (14, 197),
    'AP 7-1': (86, 171), 'AP 7-2': (92, 177), 'AP 7-3': (102, 187), 'AP 7-4': (107, 191), 'AP 7-5': (105, 190),
    'AP 8-1': (116, 201), 'AP 8-2': (93, 178), 'AP 8-3': (108, 192), 'AP 8-4': (103, 188),
    'AP 8-5': (109, 195), 'AP 8-6': (13, 193),
    'AP 9-1': (87, 172), 'AP 9-2': (8, 198), 'AP 9-3': (4, 165), 'AP 9-4': (118, 202), 'AP 9-5': (16, 203),
    'AP 10-1': (95, 179), 'AP 10-2': (110, 194),
    'AP 11-1': (10, 168), 'AP 11-2': (104, 186), 'AP 11-3': (106, 189), 'AP 11-4': (120, 199),
}

# Dateien anderer Repos, die in den Texten vorkommen
FREMD = {
    'docs/STATUS.md': FORGE + 'oer-community/src/branch/main/docs/STATUS.md',
    'docs/entscheidungen/': FORGE + 'oer-community/src/branch/main/docs/entscheidungen/',
    'docs/redaktion-longform.md': FORGE + 'oer-community/src/branch/main/docs/redaktion-longform.md',
    'redaktion-longform.md': FORGE + 'oer-community/src/branch/main/docs/redaktion-longform.md',
    'docs/designsystem.md': FORGE + 'oer-community/src/branch/main/docs/designsystem.md',
    'docs/betrieb.md': FORGE + 'oer-community/src/branch/main/docs/betrieb.md',
    'docs/redaktionskreis.md': FORGE + 'oer-community/src/branch/main/docs/redaktionskreis.md',
    'mdparser/docs/SETUP-GUIDE.md': FORGE + 'mdparser/src/branch/main/docs/SETUP-GUIDE.md',
    'core/bilder.ts': FORGE + 'mdparser/src/branch/main/sync/core/bilder.ts',
    'Comenius-Institut/oer-community': FORGE + 'oer-community',
    'Comenius-Institut/foerbico-editor': FORGE + 'foerbico-editor',
    'Comenius-Institut/mdparser': FORGE + 'mdparser',
    'Comenius-Institut/FOERBICO_und_rpi-virtuell-geschlossen': GESCHL,
    'Comenius-Institut/FOERBICO_und_rpi-virtuell': OFFEN,
    'rpi-Orga': FORGE + 'rpi-Orga',
    'nostr-oer-client': FORGE + 'nostr-oer-client',
    'FOERBICO-metadata-form': FORGE + 'FOERBICO-metadata-form',
    'image-rights-html-generator': FORGE + 'image-rights-html-generator',
    'MD2WordPress': FORGE + 'MD2WordPress',
    'wp-md-rest-import': FORGE + 'wp-md-rest-import',
}

def link(text, url):
    return f'[{text}]({url})'

def issue_links(s):
    # Verweise ins geschlossene Repo: "geschlossene(n) Repo #22", "geschlossenes Repo #132"
    s = re.sub(r'(geschlossene[nsm]?\s+Repos?\s+)#(\d+)',
               lambda m: m.group(1) + link('#' + m.group(2), f'{GESCHL}/issues/{m.group(2)}'), s)
    # Bereiche "#840–#847"
    s = re.sub(r'(?<![\w\[])#(\d+)–#(\d+)',
               lambda m: link('#' + m.group(1), f'{OFFEN}/issues/{m.group(1)}') + '–' +
                         link('#' + m.group(2), f'{OFFEN}/issues/{m.group(2)}'), s)
    # einzelne Issues/PRs, nicht in Überschriften-Rauten oder schon verlinkt
    s = re.sub(r'(?<![\w\[])#(\d{1,4})(?![\d\]])',
               lambda m: link('#' + m.group(1), f'{OFFEN}/issues/{m.group(1)}'), s)
    return s

def milestone_links(s):
    # nur die Kurzform in Tabellenzellen und nach "MS", "Meilenstein" verlinken, längste Schlüssel zuerst
    for key in sorted(MEILENSTEINE, key=len, reverse=True):
        oid, cid = MEILENSTEINE[key]
        pat = re.compile(r'(?<![\w\[])' + re.escape(key) + r'(?![\w-])')
        s = pat.sub(lambda m, k=key, o=oid: link(k, f'{OFFEN}/milestone/{o}'), s)
    return s

def file_links(s):
    def repl(m):
        p = m.group(1)
        if p in FREMD:
            return link(f'`{p}`', FREMD[p])
        cand = p.rstrip('/')
        if os.path.exists(os.path.join(REPO_ROOT, cand)):
            return link(f'`{p}`', f'{OFFEN}/src/branch/main/{p}')
        return m.group(0)
    # Backtick-Pfade mit Slash oder bekannter Endung
    return re.sub(r'(?<!\[)`([A-Za-z0-9_./\-äöüÄÖÜ ()%]+?)`', lambda m: repl(m) if ('/' in m.group(1) or m.group(1) in FREMD) else m.group(0), s)

def adr_links(s):
    return re.sub(r'(?<!\[)ADR-(\d{4})(?!\])', lambda m: link('ADR-' + m.group(1), FREMD['docs/entscheidungen/']), s)

def ms_table():
    rows = ['', '## Meilenstein-Links', '', '| AP | offenes Repo | geschlossenes Repo |', '|---|---|---|']
    seen = set()
    for key, (o, c) in MEILENSTEINE.items():
        if o in seen or key == 'AP 1-3 + AP 1-4':
            continue
        seen.add(o)
        rows.append(f'| {key} | [{o}]({OFFEN}/milestone/{o}) | [{c}]({GESCHL}/milestone/{c}) |')
    return '\n'.join(rows) + '\n'

def process(path):
    s = open(path, encoding='utf-8').read()
    kopf, sep, rest = s.partition('\n')
    rest = issue_links(rest)
    rest = milestone_links(rest)
    rest = file_links(rest)
    rest = adr_links(rest)
    if '## Meilenstein-Links' not in rest:
        rest += ms_table()
    open(path, 'w', encoding='utf-8').write(kopf + sep + rest)
    print('verlinkt:', os.path.basename(path), len(re.findall(r'\]\(https://', rest)), 'Links')

if __name__ == '__main__':
    for p in sys.argv[1:]:
        process(p)
