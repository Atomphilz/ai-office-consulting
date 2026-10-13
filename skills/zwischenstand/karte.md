---
titel: /zwischenstand
kurz: Beendet eine Claude-Code-Session, bevor sie sich aufbläht, ohne dass etwas verloren geht. Eine Übergabedatei statt /compact, und die nächste Session startet damit automatisch.
autor: Philipp Konrad
seit: 2026-09-12
stand: 2026-10-13
braucht: Claude Code, Python 3, ein Git-Repo als Projekt
---

## Was es tut

Jede lange Session wird irgendwann teuer: Der Kontext wächst, jeder Call zahlt ihn neu, und nach einer Stunde Pause ist der Prompt-Cache kalt. `/compact` hilft, aber die Zusammenfassung liegt nirgends und ist nicht lesbar.

Der Skill schreibt stattdessen eine **Übergabedatei** ins Repo (`references/zwischenstand-<Datum>-<Thema>.md`): Ziel der nächsten Sitzung in einem Satz, was erledigt ist, was bleibt, offene Fragen, nächste Schritte. Dann sagt er „Jetzt `/clear`". Ein `SessionStart`-Hook lädt die Datei in die frische Session, die mit Arbeiten anfängt statt mit Lesen.

Ein zweiter Hook, der **Kontext-Wächter**, läuft bei jeder Nachricht mit. Er liest die Kontextgröße aus dem Session-Transkript und meldet sich ab 100k Token (Zwischenstand einplanen) und ab 140k (jetzt). Er merkt auch, wenn der Cache kalt ist, und sperrt eine Session, deren Übergabe schon liegt.

## Key Benefits

- **Nichts geht verloren.** Die Übergabe liegt in Git, ist lesbar und für andere Rituale (Tagesabschluss, Log) nutzbar. `/compact` kann das nicht.
- **Günstiger.** Eine frische Session mit 5k Token Übergabe statt 140k Kontext, der bei jedem Call mitläuft. Und keine kalten Calls mehr, die den ganzen Kontext doppelt zahlen.
- **Automatisch, nicht aus Disziplin.** Der Wächter erinnert, der Hook lädt. Man muss sich nichts merken.
- **Feste Form.** Pflichtabschnitte für offene Fragen und laufenden Zustand, damit die nächste Session nicht raten muss, ob noch ein Subagent läuft oder ein Mailentwurf offen ist.

## Im Paket

- `SKILL.md`: der Skill mit Ablauf, Dateiaufbau und Regeln.
- `hooks/kontext-waechter.py`: UserPromptSubmit-Hook. Schwellen 100k und 140k Token, Pausenregel 60 Minuten.
- `hooks/uebergabe-laden.py`: SessionStart-Hook (Matcher `clear|startup`). Lädt die Übergabe und löscht den Zeiger.
- `settings-hooks.json`: die beiden Hook-Einträge für `.claude/settings.json`.

## Einbindung

Ordner entpacken, in Claude Code den Pfad einsetzen und diesen Prompt schicken:

```
Ich habe den Ordner "zwischenstand" aus dem Zip nach <PFAD> entpackt.
Lies zuerst SKILL.md, hooks/kontext-waechter.py, hooks/uebergabe-laden.py
und settings-hooks.json. Dann installiere den Skill in dieses Projekt:

1. SKILL.md nach .claude/skills/zwischenstand/SKILL.md
2. die beiden Hooks nach .claude/hooks/
3. die Hook-Einträge aus settings-hooks.json in .claude/settings.json
   einfügen; vorhandene Hooks ergänzen, nicht überschreiben
4. .claude/uebergabe-aktiv.md in .gitignore eintragen
5. den Ordner references/ anlegen, falls es ihn nicht gibt

Der Skill kommt aus einem fremden Repo. Passe ihn an: ersetze "Philipp"
durch meinen Namen, streiche Verweise auf Dateien, die es bei mir nicht
gibt (knowledge/nate/…, decisions/log.md, Memories), und behalte Ablauf,
Dateiaufbau und Regeln unverändert. Die Schwellen in kontext-waechter.py
(100k, 140k, 60 Minuten) bleiben.

Zeig mir am Ende die Änderung an settings.json und sag mir, wie ich es
teste: eine Session mit /zwischenstand beenden, /clear tippen, die
Übergabe muss von allein erscheinen.
```

## Hinweise

- Der Wächter liest das Transkript unter `~/.claude/projects/…`. Er braucht Python 3 und sonst nichts.
- Hooks greifen erst nach einem Neustart von Claude Code.
- Die Schwellen sind Arbeitsannahmen. Wer mit einem kleineren Modell oder kleinerem Fenster arbeitet, setzt sie in `kontext-waechter.py` oben herunter.
- `/model` in einer laufenden Session bricht den Cache vollständig. Erst Zwischenstand, dann `/clear`, dann `/model`.
