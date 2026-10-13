#!/usr/bin/env python3
"""Baut skills/index.html und ein Zip je Skill aus den Ordnern unter skills/.

Aufruf aus dem Repo-Wurzelverzeichnis oder aus skills/:
    python3 skills/bauen.py

Jeder Skill ist ein Ordner skills/<name>/ mit einer karte.md (Kopf mit
titel/kurz/autor/seit/stand/braucht, dann Abschnitte "Was es tut",
"Key Benefits", "Im Paket", "Einbindung", "Hinweise") und den Dateien, die
jemand zum Installieren braucht. Das Zip enthält den ganzen Ordner ohne
karte.md und ohne __pycache__. Nur Standardbibliothek, kein pip.
"""
import html
import os
import re
import sys
import zipfile
from datetime import date

HIER = os.path.dirname(os.path.abspath(__file__))
REPO = "https://github.com/Atomphilz/ai-office-consulting/tree/main/skills"


# ---------- karte.md lesen ----------

def karte_lesen(pfad):
    with open(pfad, encoding="utf-8") as fh:
        text = fh.read()
    kopf, body = {}, text
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if m:
        for zeile in m.group(1).splitlines():
            if ":" in zeile:
                k, v = zeile.split(":", 1)
                kopf[k.strip()] = v.strip()
        body = m.group(2)
    abschnitte, aktuell, puffer = {}, None, []
    for zeile in body.splitlines():
        if zeile.startswith("## "):
            if aktuell:
                abschnitte[aktuell] = "\n".join(puffer).strip()
            aktuell, puffer = zeile[3:].strip(), []
        else:
            puffer.append(zeile)
    if aktuell:
        abschnitte[aktuell] = "\n".join(puffer).strip()
    return kopf, abschnitte


# ---------- kleines Markdown ----------

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    return s


def md(text):
    """Absätze, Listen, Codeblöcke. Mehr braucht eine Karte nicht."""
    out, zeilen, i = [], text.splitlines(), 0
    while i < len(zeilen):
        z = zeilen[i]
        if z.startswith("```"):
            j = i + 1
            while j < len(zeilen) and not zeilen[j].startswith("```"):
                j += 1
            code = html.escape("\n".join(zeilen[i + 1:j]), quote=False)
            out.append(f'<div class="code"><button class="kopieren" type="button">Kopieren</button>'
                       f'<pre><code>{code}</code></pre></div>')
            i = j + 1
            continue
        if z.startswith("- "):
            j = i
            punkte = []
            while j < len(zeilen) and zeilen[j].startswith("- "):
                punkte.append(f"<li>{inline(zeilen[j][2:])}</li>")
                j += 1
            out.append("<ul>" + "".join(punkte) + "</ul>")
            i = j
            continue
        if z.strip() == "":
            i += 1
            continue
        j = i
        absatz = []
        while j < len(zeilen) and zeilen[j].strip() and not zeilen[j].startswith(("- ", "```")):
            absatz.append(zeilen[j])
            j += 1
        out.append(f"<p>{inline(' '.join(absatz))}</p>")
        i = j
    return "\n".join(out)


# ---------- Zip ----------

def zip_bauen(ordner, name):
    ziel = os.path.join(HIER, f"{name}.zip")
    with zipfile.ZipFile(ziel, "w", zipfile.ZIP_DEFLATED) as z:
        for wurzel, dirs, dateien in os.walk(ordner):
            dirs[:] = [d for d in dirs if d != "__pycache__" and not d.startswith(".")]
            for d in sorted(dateien):
                if d in ("karte.md", ".DS_Store"):
                    continue
                voll = os.path.join(wurzel, d)
                z.write(voll, os.path.join(name, os.path.relpath(voll, ordner)))
    return os.path.getsize(ziel)


# ---------- Seite ----------

STYLE = """
:root {
  color-scheme: dark;
  --bg: #0e1012; --surface: #15181b; --surface-2: #1b1f23; --text: #e8e8e4; --muted: #a4a8ac;
  --accent: #9ccfbf; --accent-ink: #0b1512; --rule: #272b30; --rule-strong: #3a4046;
  --shadow: 0 1px 0 rgba(255,255,255,.03) inset, 0 10px 30px rgba(0,0,0,.25);
  --radius: 14px; --max: 68rem; --prose: 42rem; --gutter: 16px;
}
@media (prefers-color-scheme: light) {
  :root {
    color-scheme: light;
    --bg: #f6f6f3; --surface: #ffffff; --surface-2: #f0f0ec; --text: #17191b; --muted: #5b6168;
    --accent: #1f6b5a; --accent-ink: #ffffff; --rule: #e2e2dc; --rule-strong: #c9c9c2;
    --shadow: 0 1px 2px rgba(0,0,0,.04), 0 10px 30px rgba(20,30,25,.06);
  }
}
*, *::before, *::after { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; scroll-behavior: smooth; scroll-padding-top: 76px; }
body { margin: 0; background: var(--bg); color: var(--text);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 1.0625rem; line-height: 1.65; -webkit-font-smoothing: antialiased; overflow-x: hidden; }
.wrap { max-width: var(--max); margin: 0 auto; padding: 0 var(--gutter); }
h1, h2, h3 { margin: 0; line-height: 1.2; letter-spacing: -0.015em; }
p { margin: 0 0 1rem; }
ul { margin: 0 0 1rem; padding-left: 1.2rem; }
li { margin-bottom: .4rem; }
strong { font-weight: 600; }
a { color: var(--accent); text-decoration: underline; text-underline-offset: 3px; text-decoration-thickness: 1px; }
a:hover { text-decoration-thickness: 2px; }
code { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: .92em;
  background: var(--surface-2); padding: 1px 5px; border-radius: 5px; }
:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; border-radius: 4px; }
.skip { position: absolute; left: -999px; top: 8px; background: var(--accent); color: var(--accent-ink); padding: 8px 12px; border-radius: 6px; z-index: 100; }
.skip:focus { left: 8px; }

.kopf { position: sticky; top: 0; z-index: 10; background: var(--bg);
  background: color-mix(in srgb, var(--bg) 85%, transparent);
  -webkit-backdrop-filter: blur(12px); backdrop-filter: blur(12px); border-bottom: 1px solid var(--rule); }
.kopf .wrap { display: flex; align-items: center; justify-content: space-between; gap: 16px; min-height: 60px; }
.marke { display: inline-flex; align-items: center; gap: 10px; color: var(--text); text-decoration: none; font-weight: 600; letter-spacing: -0.01em; min-height: 44px; }
.marke svg { width: 30px; height: 30px; flex: none; }
.nav { display: flex; gap: 4px; align-items: center; }
.nav a { color: var(--muted); text-decoration: none; padding: 10px 12px; border-radius: 8px; font-size: 0.95rem; line-height: 1; min-height: 44px; display: inline-flex; align-items: center; }
.nav a:hover { color: var(--text); background: var(--surface-2); }

.seite { padding: 64px 0 72px; }
.seite h1 { font-size: clamp(1.8rem, 1.3rem + 2vw, 2.6rem); font-weight: 700; letter-spacing: -0.025em; margin-bottom: 0.75rem; }
.seite .einstieg { color: var(--muted); font-size: 1.1rem; max-width: var(--prose); margin-bottom: 2.5rem; }

.inhalt { list-style: none; margin: 0 0 2.5rem; padding: 0; display: flex; flex-wrap: wrap; gap: 8px; }
.inhalt a { display: inline-flex; align-items: center; min-height: 40px; padding: 6px 14px; border: 1px solid var(--rule-strong);
  border-radius: 999px; text-decoration: none; color: var(--text); font-weight: 500; font-size: .95rem; }
.inhalt a:hover { border-color: var(--accent); }

.skill { background: var(--surface); border: 1px solid var(--rule); border-radius: var(--radius); box-shadow: var(--shadow);
  padding: 28px 28px 24px; margin-bottom: 24px; }
.skill-kopf { display: flex; flex-wrap: wrap; align-items: baseline; justify-content: space-between; gap: 8px 16px; margin-bottom: .5rem; }
.skill h2 { font-size: clamp(1.4rem, 1.1rem + 1vw, 1.8rem); font-weight: 650; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; color: var(--accent); }
.meta { color: var(--muted); font-size: .92rem; }
.meta span + span::before { content: " · "; }
.kurz { font-size: 1.1rem; font-weight: 500; max-width: var(--prose); margin-bottom: 1.25rem; }
.aktionen { display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 1.5rem; }
.btn { display: inline-flex; align-items: center; justify-content: center; gap: 8px; min-height: 44px; padding: 10px 18px;
  border-radius: 10px; font-weight: 600; font-size: .98rem; line-height: 1.2; text-decoration: none; border: 1px solid transparent;
  transition: transform .15s ease, border-color .15s ease; cursor: pointer; font-family: inherit; }
.btn-primary { background: var(--accent); color: var(--accent-ink); }
.btn-secondary { background: var(--surface); color: var(--text); border-color: var(--rule-strong); }
.btn:hover { transform: translateY(-1px); text-decoration: none; }
.btn-secondary:hover { border-color: var(--accent); }
.btn svg { width: 18px; height: 18px; flex: none; }

.spalten { display: grid; grid-template-columns: 1fr 1fr; gap: 24px 32px; }
.block h3 { font-size: 1rem; font-weight: 650; margin-bottom: .6rem; }
.block h3::before { content: ""; display: block; width: 28px; height: 3px; background: var(--accent); border-radius: 2px; margin-bottom: 10px; }
.block p:last-child, .block ul:last-child { margin-bottom: 0; }
.block.breit { grid-column: 1 / -1; }
.code { position: relative; margin: 0 0 1rem; }
.code pre { margin: 0; padding: 18px 18px 18px; background: var(--bg); border: 1px solid var(--rule); border-radius: 10px;
  overflow-x: auto; font-size: .9rem; line-height: 1.5; white-space: pre-wrap; word-break: break-word; }
.code pre code { background: none; padding: 0; font-size: inherit; }
.kopieren { position: absolute; top: 10px; right: 10px; min-height: 32px; padding: 4px 12px; border-radius: 8px; font-size: .85rem;
  font-weight: 600; background: var(--surface-2); color: var(--text); border: 1px solid var(--rule-strong); cursor: pointer; font-family: inherit; }
.kopieren:hover { border-color: var(--accent); }
.kopieren.ok { background: var(--accent); color: var(--accent-ink); border-color: var(--accent); }

.fuss { border-top: 1px solid var(--rule); padding: 28px 0 40px; color: var(--muted); font-size: 0.9rem; }
.fuss .wrap { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 8px 24px; }

@media (max-width: 860px) {
  .spalten { grid-template-columns: 1fr; }
  .seite { padding: 48px 0 56px; }
  .skill { padding: 20px 18px 18px; }
}
@media (max-width: 600px) {
  body { font-size: 1rem; }
  .aktionen .btn { flex: 1 1 100%; }
}
@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } .btn { transition: none; } }
"""

MARKE = ('<svg viewBox="0 0 64 64" aria-hidden="true" focusable="false"><rect width="64" height="64" rx="14" fill="var(--surface-2)"/>'
         '<rect x="2" y="2" width="60" height="60" rx="12" fill="none" stroke="var(--accent)" stroke-width="2.5"/>'
         '<text x="32" y="42" text-anchor="middle" font-family="-apple-system,BlinkMacSystemFont,\'Segoe UI\',Roboto,Helvetica,Arial,sans-serif" '
         'font-size="28" font-weight="700" fill="var(--accent)">PK</text></svg>')

ICON_ZIP = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>')
ICON_GH = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 .5a12 12 0 0 0-3.8 23.4c.6.1.8-.3.8-.6v-2.2c-3.3.7-4-1.4-4-1.4-.6-1.4-1.4-1.8-1.4-1.8-1.1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1.1 1.9 2.8 1.3 3.5 1 .1-.8.4-1.3.8-1.6-2.7-.3-5.5-1.3-5.5-5.9 0-1.3.5-2.4 1.2-3.2-.1-.3-.5-1.5.1-3.2 0 0 1-.3 3.3 1.2a11.5 11.5 0 0 1 6 0c2.3-1.5 3.3-1.2 3.3-1.2.7 1.7.3 2.9.1 3.2.8.8 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6A12 12 0 0 0 12 .5z"/></svg>')


def block(titel, text, breit=False):
    if not text:
        return ""
    klasse = "block breit" if breit else "block"
    return f'<div class="{klasse}"><h3>{html.escape(titel)}</h3>{md(text)}</div>'


def skill_html(name, kopf, ab, zip_kb):
    titel = html.escape(kopf.get("titel", "/" + name))
    meta = []
    if kopf.get("autor"):
        meta.append(f"<span>{html.escape(kopf['autor'])}</span>")
    if kopf.get("stand"):
        meta.append(f"<span>Stand {html.escape(kopf['stand'])}</span>")
    if kopf.get("braucht"):
        meta.append(f"<span>Braucht: {html.escape(kopf['braucht'])}</span>")
    return f"""
<article class="skill" id="{html.escape(name)}">
  <div class="skill-kopf">
    <h2>{titel}</h2>
    <p class="meta">{''.join(meta)}</p>
  </div>
  <p class="kurz">{inline(kopf.get('kurz', ''))}</p>
  <div class="aktionen">
    <a class="btn btn-primary" href="{html.escape(name)}.zip" download>{ICON_ZIP}Zip laden ({zip_kb} KB)</a>
    <a class="btn btn-secondary" href="{REPO}/{html.escape(name)}">{ICON_GH}Dateien auf GitHub</a>
  </div>
  <div class="spalten">
    {block("Was es tut", ab.get("Was es tut"))}
    {block("Key Benefits", ab.get("Key Benefits"))}
    {block("Im Paket", ab.get("Im Paket"))}
    {block("Hinweise", ab.get("Hinweise"))}
    {block("Einbindung in den eigenen Claude Code", ab.get("Einbindung"), breit=True)}
  </div>
</article>"""


def seite(skills):
    inhalt = "".join(f'<li><a href="#{html.escape(n)}">{html.escape(k.get("titel", "/" + n))}</a></li>'
                     for n, k, _, _ in skills)
    karten = "".join(skill_html(n, k, ab, kb) for n, k, ab, kb in skills)
    heute = date.today().isoformat()
    return f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Skills für Claude Code – Philipp Konrad</title>
<meta name="description" content="Skills und Hooks für Claude Code, mit Beschreibung, Nutzen und einem Prompt zur Einbindung ins eigene Projekt.">
<meta name="robots" content="noindex, nofollow">
<meta name="color-scheme" content="dark light">
<meta name="theme-color" content="#0e1012" media="(prefers-color-scheme: dark)">
<meta name="theme-color" content="#f6f6f3" media="(prefers-color-scheme: light)">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<style>{STYLE}</style>
</head>
<body>
<a class="skip" href="#inhalt">Zum Inhalt</a>
<header class="kopf">
  <div class="wrap">
    <a class="marke" href="/" aria-label="Philipp Konrad, zur Startseite">{MARKE}<span>Philipp Konrad</span></a>
    <nav class="nav" aria-label="Zurück"><a href="/">Zur Startseite</a></nav>
  </div>
</header>
<main id="inhalt" class="seite">
  <div class="wrap">
    <h1>Skills für Claude Code</h1>
    <p class="einstieg">Was sich im Alltag mit Claude Code bewährt hat, zum Mitnehmen. Jede Karte: was der Skill tut, warum er sich lohnt, was im Paket ist, und ein Prompt, mit dem Claude ihn im eigenen Projekt installiert und anpasst. Unverlinkt, nur für Leute mit dem Link.</p>
    <ul class="inhalt" aria-label="Skills auf dieser Seite">{inhalt}</ul>
    {karten}
  </div>
</main>
<footer class="fuss">
  <div class="wrap">
    <span>Philipp Konrad · 2026 · Stand {heute}</span>
    <span><a href="/impressum.html">Impressum</a> · <a href="/datenschutz.html">Datenschutz</a></span>
  </div>
</footer>
<script>
document.querySelectorAll('.kopieren').forEach(function (b) {{
  b.addEventListener('click', function () {{
    var t = b.parentNode.querySelector('code').textContent;
    navigator.clipboard.writeText(t).then(function () {{
      b.textContent = 'Kopiert'; b.classList.add('ok');
      setTimeout(function () {{ b.textContent = 'Kopieren'; b.classList.remove('ok'); }}, 1800);
    }});
  }});
}});
</script>
</body>
</html>
"""


def main():
    skills = []
    for name in sorted(os.listdir(HIER)):
        ordner = os.path.join(HIER, name)
        karte = os.path.join(ordner, "karte.md")
        if not os.path.isdir(ordner) or not os.path.exists(karte):
            continue
        kopf, ab = karte_lesen(karte)
        groesse = zip_bauen(ordner, name)
        skills.append((name, kopf, ab, max(1, round(groesse / 1024))))
        print(f"{name}: {kopf.get('titel', '')}, Zip {groesse} Bytes")
    if not skills:
        sys.exit("keine Skills gefunden (Ordner mit karte.md)")
    with open(os.path.join(HIER, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(seite(skills))
    print(f"index.html geschrieben, {len(skills)} Skill(s)")


if __name__ == "__main__":
    main()
