---
titel: /explanation-builder
kurz: Baut per Interview deinen eigenen Explanation-Skill. Danach erklärt Claude jedes Thema aus deinem Alltag als Seite mit Diagrammen, Bildern und einem kurzen Erklärvideo mit Stimme.
autor: Fabian Gless
seit: 2026-11-18
stand: 2026-11-18
braucht: Claude Code, optional ein API-Key für Stimme (ElevenLabs, OpenAI oder Gemini) und für Bilder (OpenAI oder Gemini)
---

## Was es tut

Du beschreibst Themen, Leser und Anlässe, und der Skill baut dir daraus einen eigenen Skill namens `Explanation`. Den rufst du danach für jedes Thema auf, das du dir schnell verständlich machen willst.

Jede erzeugte Erklärung ist grafisch zuerst: mindestens ein Diagramm, dazu Bilder, wenn eine Bild-API vorhanden ist, und ein kurzes Motion-Graphics-Video im Browser mit Sprecherstimme. Text erklärt, was das Diagramm zeigt, nicht umgekehrt.

Der Builder prüft vorher, welche Werkzeuge da sind (Artifact, Bild-API, Stimme), zeigt dir das Ergebnis und hilft beim Einrichten der Keys. Keys trägst du selbst in `~/.claude/.env` ein. Der Skill liest sie nie aus und schreibt sie nie in Dateien.

## Key Benefits

- **Dein eigener Skill.** Themen, Leser, Abschnitte und Stil kommen aus einem Interview, nicht aus einer Vorlage.
- **Nichts voraussetzen.** Jeder Fachbegriff wird beim ersten Auftreten erklärt.
- **Ohne Stimme nutzbar.** Fehlt ein Voice-Key, laufen die Videos stumm mit Untertiteln, statt eine Systemstimme zu ersetzen.
- **Sicher neu bauen.** Ein bestehender Explanation-Skill wird vor dem Überschreiben gesichert.

## Im Paket

- `SKILL.md`: der Builder mit Ablauf (Werkzeug-Check, Interview, Einrichtung, Schreiben).
- `References/`: Interview-Leitfaden, Werkzeug-Check, Blueprint für den erzeugten Skill, Seiten- und Video-Vorlagen, Anleitungen für Stimme und Bilder.

## Einbindung

```
Installiere den Skill explanation-builder aus diesem Repo in meinen Claude-Code-Skills-Ordner (~/.claude/skills/explanation-builder/). Danach starte den Builder mit „erklär-skill bauen“.
```

## Hinweise

- Der erzeugte Skill landet in `~/.claude/skills/Explanation/`. Der Builder selbst bleibt getrennt, damit Claude nicht zwei Skills mit gleichem Namen lädt.
- Stimme und Bilder kosten pro Nutzung. Die Kontingente der Anbieter gelten.
