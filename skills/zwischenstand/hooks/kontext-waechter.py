#!/usr/bin/env python3
"""Kontext-Wächter — UserPromptSubmit-Hook.

Liest aus dem Session-Transkript den letzten API-Call und rechnet die
Kontextgröße aus (input + cache_creation + cache_read). Über der Schwelle
hängt er an Philipps Nachricht einen Hinweis an, den nur Claude sieht.

Schwellen (Arbeitsannahme 12. Sept 2026, Prüfung beim nächsten /level-up):
  HINWEIS  100.000 Token  — Zwischenstand einplanen
  MELDUNG  140.000 Token  — Zwischenstand jetzt, vor der nächsten Aufgabe

Pausen-Regel (14. Sept 2026, nach Nates Caching-Video, knowledge/nate/…tokens):
  Liegt der letzte API-Call länger als 60 Minuten zurück, ist der Prompt-Cache
  kalt (TTL im Abo: eine Stunde), und der nächste Call zahlt den gesamten
  Kontext neu. Ab PAUSE_MIN Minuten und PAUSE_CTX Token kommt deshalb ein
  eigener Hinweis, unabhängig von den Größenschwellen.

Abwesenheitstimer (16. Sept 2026, Arbeitsannahme, Prüfung beim /level-up 18.9.):
  Ab PAUSE_CTX Token bekommt jeder Zug die Anweisung, am Ende einen Wakeup auf
  TIMER_S Sekunden zu planen (ScheduleWakeup, Prompt beginnt mit TIMER_MARKER).
  Feuert der Wakeup und der letzte Call liegt TIMER_MIN Minuten zurück, war
  Philipp weg: Claude schreibt den Zwischenstand, solange der Cache noch warm
  ist. Danach liegt .claude/uebergabe-aktiv.md.

Sperre (16. Sept 2026):
  Liegt eine Übergabe und der letzte Call ist PAUSE_MIN Minuten her, ist die
  Session kalt und die Übergabe vollständig. Der Hook blockt dann Philipps
  Nachricht (sie wird nicht gesendet, kostet keinen Token) und sagt ihm /clear.
  Slash-Befehle werden nie geblockt.

Still, wenn: kein Transkript, noch kein API-Call, oder eine Übergabe schon
geschrieben und noch nicht verbraucht ist (und die Session nicht kalt ist).
"""
import json, os, sys
from datetime import datetime, timezone

HINWEIS = 100_000
MELDUNG = 140_000
PAUSE_MIN = 60       # Minuten seit dem letzten API-Call, ab denen der Cache kalt ist
PAUSE_CTX = 40_000   # darunter kostet der Neuaufbau weniger als eine Übergabe
TIMER_S = 3000       # Wakeup nach 50 Minuten: zehn Minuten Luft bis zur kalten Stunde
TIMER_MIN = 45       # feuert der Wakeup und der letzte Call ist so alt, war Philipp weg
TIMER_MARKER = "[Abwesenheitstimer]"
TIMER_AN = False     # 16. Sept 2026 abends abgeschaltet: VS Code zeigt Text vor einem
                     # abschließenden ScheduleWakeup nur als Zusammenfassung, Antworten
                     # gingen dreimal verloren. Sperre und Schwellen bleiben.
TAIL_BYTES = 400_000  # nur das Ende des Transkripts lesen; Dateien werden mehrere MB groß


def letzter_call(pfad):
    """(Kontextgröße, Minuten seit dem letzten API-Call). (0, None) wenn nichts da."""
    try:
        size = os.path.getsize(pfad)
        with open(pfad, "rb") as fh:
            fh.seek(max(0, size - TAIL_BYTES))
            zeilen = fh.read().decode("utf-8", "replace").splitlines()
    except OSError:
        return 0, None
    for zeile in reversed(zeilen):
        try:
            d = json.loads(zeile)
        except ValueError:
            continue
        if d.get("type") != "assistant":
            continue
        u = (d.get("message") or {}).get("usage") or {}
        if not u:
            continue
        ctx = (u.get("input_tokens", 0)
               + u.get("cache_creation_input_tokens", 0)
               + u.get("cache_read_input_tokens", 0))
        minuten = None
        ts = d.get("timestamp")
        if ts:
            try:
                dann = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                minuten = (datetime.now(timezone.utc) - dann).total_seconds() / 60
            except ValueError:
                pass
        return ctx, minuten
    return 0, None


def kontext(text):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit",
                                             "additionalContext": text}}))


def timer_planen():
    return (f"Beende diesen Zug mit ScheduleWakeup: delaySeconds {TIMER_S}, noop true, "
            f"prompt genau \"{TIMER_MARKER} Prüfung.\", reason \"Abwesenheitstimer\". "
            f"Nicht erwähnen, nicht erklären.")


def timer_zug(uebergabe, ctx, minuten, k):
    """Der Wakeup hat gefeuert. Entscheiden, was der Zug tut."""
    m = "unbekannt" if minuten is None else f"{int(minuten)}"
    if not TIMER_AN:
        # Alter Wakeup aus einer Session vor dem Abschalten: nicht neu planen.
        kontext(f"{TIMER_MARKER} Timer ist abgeschaltet. ScheduleWakeup stop, sonst nichts. "
                f"Sag Philipp in einem Satz, dass ein alter Wakeup gefeuert hat und jetzt gestoppt ist.")
    elif uebergabe:
        kontext(f"{TIMER_MARKER} Übergabe liegt schon. ScheduleWakeup stop, sonst nichts.")
    elif ctx < PAUSE_CTX:
        kontext(f"{TIMER_MARKER} Kontext bei {k}, unter 40k, nichts zu retten. ScheduleWakeup stop, sonst nichts.")
    elif minuten is not None and minuten >= TIMER_MIN:
        kontext(f"{TIMER_MARKER} {m} Minuten ohne Aktivität, Kontext bei {k}, Cache noch warm. "
                f"Läuft noch ein Subagent oder eine Hintergrundaufgabe von dir, nichts schreiben und "
                f"stattdessen: {timer_planen()} Sonst: führe jetzt den Skill /zwischenstand aus "
                f"(Ziel der nächsten Sitzung = die Aufgabe, an der diese Session gerade war), "
                f"danach ScheduleWakeup stop. Antwort an Philipp höchstens zwei Sätze.")
    else:
        kontext(f"{TIMER_MARKER} Philipp war aktiv, letzter Call vor {m} Minuten, Kontext {k}. "
                f"Nichts schreiben. {timer_planen()}")


def main():
    try:
        ein = json.load(sys.stdin)
    except ValueError:
        return
    projekt = os.environ.get("CLAUDE_PROJECT_DIR") or ein.get("cwd") or "."
    prompt = (ein.get("prompt") or "").strip()
    uebergabe = os.path.exists(os.path.join(projekt, ".claude", "uebergabe-aktiv.md"))
    ctx, minuten = letzter_call(ein.get("transcript_path", ""))
    k = f"{ctx // 1000}k"

    if prompt.startswith(TIMER_MARKER):
        timer_zug(uebergabe, ctx, minuten, k)
        return

    if uebergabe:
        if minuten is not None and minuten >= PAUSE_MIN and not prompt.startswith("/"):
            print(json.dumps({"decision": "block", "reason":
                f"[Kontext-Wächter] Session kalt: letzter Call vor {int(minuten)} Min, Kontext {k}. "
                f"Eine Übergabe liegt schon. Deine Nachricht wurde nicht gesendet. "
                f"Tipp /clear, die neue Session lädt die Übergabe automatisch."}))
        return  # Übergabe liegt, Philipp muss nur noch /clear tippen

    teile = []
    if ctx >= MELDUNG:
        teile.append(f"[Kontext-Wächter] Kontext bei {k} Token, Schwelle 140k überschritten. "
                     f"Schließe den laufenden Werkzeugschritt ab, dann führe den Skill /zwischenstand aus, "
                     f"bevor du die nächste Aufgabe beginnst. Sag Philipp am Ende: jetzt /clear.")
    elif ctx >= HINWEIS:
        teile.append(f"[Kontext-Wächter] Kontext bei {k} Token, über 100k. "
                     f"Plane einen /zwischenstand am nächsten natürlichen Haltepunkt ein und sag Philipp "
                     f"in einem Satz, dass die Session groß wird.")
    if minuten is not None and minuten >= PAUSE_MIN and ctx >= PAUSE_CTX:
        teile.append(f"[Kontext-Wächter] Letzter Call vor {int(minuten)} Minuten, der Prompt-Cache ist kalt: "
                     f"dieser Call zahlt die vollen {k} Token neu. Sag Philipp das in einem Satz. "
                     f"Wenn er eine andere Aufgabe anfängt als die vor der Pause, empfiehl /zwischenstand "
                     f"und /clear statt hier weiterzuarbeiten.")
    if TIMER_AN and ctx >= PAUSE_CTX:
        teile.append(f"{TIMER_MARKER} Kontext bei {k}. {timer_planen()}")
    if not teile:
        return
    kontext(" ".join(teile))


if __name__ == "__main__":
    main()
