#!/usr/bin/env python3
"""Übergabe laden — SessionStart-Hook (Matcher: clear, startup).

Liegt .claude/uebergabe-aktiv.md (vom Skill /zwischenstand geschrieben),
gibt der Hook die verlinkte Zwischenstand-Datei komplett aus, damit die
frische Session mit dem Stand beginnt statt mit Nichts. Danach wird der
Zeiger gelöscht; die Zwischenstand-Datei selbst bleibt in references/.

Zeiger älter als 7 Tage werden ignoriert und aufgeräumt — dann war es keine
Übergabe mehr, sondern ein Rest. (Bis 16.9.2026: 24 h. Seit der Abwesenheitstimer
Übergaben schreibt, während Philipp weg ist, muss ein Wochenende hineinpassen.)
"""
import json, os, sys, time

MAX_ALTER_S = 7 * 24 * 3600  # seit 16.9.2026: der Abwesenheitstimer schreibt Übergaben auch übers Wochenende


def main():
    try:
        ein = json.load(sys.stdin)
    except ValueError:
        ein = {}
    projekt = os.environ.get("CLAUDE_PROJECT_DIR") or ein.get("cwd") or "."
    zeiger = os.path.join(projekt, ".claude", "uebergabe-aktiv.md")
    if not os.path.exists(zeiger):
        return
    alter = time.time() - os.path.getmtime(zeiger)
    with open(zeiger, encoding="utf-8") as fh:
        kopf = fh.read().strip()
    if alter > MAX_ALTER_S:
        os.remove(zeiger)
        return
    # erste Zeile des Zeigers ist der Pfad zur Zwischenstand-Datei, relativ zum Projekt
    pfad = kopf.splitlines()[0].strip()
    voll = os.path.join(projekt, pfad)
    try:
        with open(voll, encoding="utf-8") as fh:
            inhalt = fh.read()
    except OSError:
        os.remove(zeiger)
        return
    os.remove(zeiger)
    print(f"[Übergabe] Die vorherige Session hat einen Zwischenstand hinterlassen "
          f"(`{pfad}`, vor {int(alter // 60)} Min). Er folgt vollständig. Arbeite von hier weiter, "
          f"lies die Datei nicht noch einmal, und beginne mit dem Ein-Satz-Ziel darin.\n")
    print(kopf.split("\n", 1)[1].strip() if "\n" in kopf else "")
    print("\n---\n")
    print(inhalt)


if __name__ == "__main__":
    main()
