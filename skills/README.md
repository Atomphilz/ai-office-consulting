# Skills für Claude Code

Seite: https://ai-office-consulting.de/skills/ (unverlinkt, `noindex`, nur für Leute mit dem Link).

## Einen Skill hinzufügen

1. Ordner `skills/<name>/` anlegen, Name klein und ohne Leerzeichen, z. B. `zwischenstand`.
2. Hinein: alles, was jemand zum Installieren braucht. `SKILL.md`, Hooks, Skripte, ein `settings-hooks.json` mit den Hook-Einträgen, falls der Skill Hooks hat.
3. Eine `karte.md` dazu, nach dem Muster in `zwischenstand/karte.md`:

   ```
   ---
   titel: /name
   kurz: Ein Satz, was der Skill tut.
   autor: Vorname Nachname
   seit: JJJJ-MM-TT
   stand: JJJJ-MM-TT
   braucht: Claude Code, …
   ---

   ## Was es tut
   ## Key Benefits
   ## Im Paket
   ## Einbindung      ← ein Codeblock mit dem Prompt, den man in Claude Code schickt
   ## Hinweise
   ```

   Markdown reicht: Absätze, `- ` Listen, Codeblöcke, `Code`, **fett**, Links. Abschnitte, die leer bleiben, weglassen.

4. Bauen: `python3 skills/bauen.py` aus dem Repo-Wurzelverzeichnis. Schreibt `skills/index.html` und `skills/<name>.zip` neu. Beides mit einchecken.
5. Branch, Commit, Pull Request. Nach dem Merge ist die Seite in etwa einer Minute live.

Tipp: Claude Code kann die `karte.md` aus einer `SKILL.md` vorschreiben. Prompt: „Lies `skills/zwischenstand/karte.md` als Muster und schreib eine `karte.md` für den Skill in `<Ordner>`. Den Einbindungs-Prompt so, dass ein fremder Claude Code den Skill ohne Rückfrage installiert."

## Was nicht hinein gehört

Zugangsdaten, Kundendaten, Pfade mit echten Namen Dritter. Das Repo ist öffentlich.
