---
titel: /day-close + /day-open
kurz: Ein Tagesritual in zwei ungleichen Hälften. Abends fünf Minuten planen, morgens sechzig Sekunden vorlesen. Ein Einmal-Interview legt fest, was abgefragt und geprüft wird.
autor: Philipp Konrad
seit: 2026-08-17
stand: 2026-10-13
braucht: Claude Code, ein Git-Repo als Projekt; optional ein Kalender-CLI
---

## Was es tut

Wer mehrere Bereiche alleine fährt, hat meist keinen Tagesplan: Aufgaben kommen in Ankunftsreihenfolge dran oder werden vertagt, bis sie vergessen sind. Das Paar ist die Gegenmaßnahme, als Ritual, nicht als Automation.

**`/day-close`, abends, ~5 Minuten.** Fragt, was heute wirklich passiert ist, fängt ein, was sonst nirgends steht (Bargeld, Zusagen am Telefon, was einem noch im Kopf sitzt), schlägt zwei bis drei Fokus-Kandidaten für morgen vor, und man wählt. Schreibt den Rückblick in die heutige Tagesdatei und den Plan für morgen in eine neue. Legt Kalenderblöcke an, wenn ein Kalender-Werkzeug konfiguriert ist.

**`/day-open`, morgens, 60 Sekunden.** Liest den Plan vor, prüft die konfigurierten Quellen (Kalender, Postfach, Logs) und meldet nur, was den Plan bricht. Fehlt der Abend, schreibt es selbst einen kalten Brief und erwähnt die Lücke nie.

**`/day-setup`, einmal.** Sieben Fragen, gebündelt: wer bist du, welche Bereiche, was abends erfassen, was morgens prüfen, welche Werkzeuge, welche Spannungen beim Planen benennen, was nie ins Ritual gehört. Schreibt `references/tagesritual.md`, lesbar und per Hand änderbar. Die beiden Tagesskills kennen keinen Namen, keinen Bereich, kein Werkzeug; alles Persönliche steht in dieser Datei.

## Key Benefits

- **Überlebt schlechte Tage.** Die Teilung ist absichtlich ungleich: eine schwere und eine triviale Hälfte. Zwei schwere tägliche Rituale sterben nach einer Woche.
- **Fängt, was kein System sieht.** Bargeld, Telefonzusagen, Chat-Versprechen existieren nur im Kopf, bis sie abends in die Tagesdatei kommen.
- **Kein Tadel, kein Zählen.** Ein ausgelassener Abend wird nicht erwähnt. Der Morgen stellt die Kette einfach wieder her.
- **Spannungen werden benannt, nicht wegdiskutiert.** Wenn zwei Dinge um dieselben Stunden konkurrieren, sagt der Abend laut, was das andere verliert, statt einen Plan zu zeigen, in dem alles passt.
- **Drift wird sichtbar.** Jede Tagesdatei trägt Plan und ehrlichen Rückblick. Eine Woche nebeneinander gelesen zeigt, was wirklich passiert.
- **Inhalt ist deiner, Mechanik ist fest.** Was gefragt wird, steht in einer Datei, die du änderst. Wie das Ritual läuft, steht in den Skills und bleibt.

## Im Paket

- `day-setup/SKILL.md`: das Einmal-Interview, schreibt `references/tagesritual.md`.
- `day-close/SKILL.md`: der Abend. Vier Schritte: Rückblick, Einfangen, Morgen entscheiden, schreiben und blocken.
- `day-open/SKILL.md`: der Morgen. Zwei Pfade: Plan vorhanden, oder kalter Brief.
- `daily-template.md`: die Vorlage der Tagesdatei, von beiden Skills benutzt, mit Platzhaltern aus der Konfiguration.

## Einbindung

Ordner entpacken, in Claude Code den Pfad einsetzen und diesen Prompt schicken:

```
Ich habe den Ordner "tagesritual" aus dem Zip nach <PFAD> entpackt.
Lies zuerst day-setup/SKILL.md, day-close/SKILL.md, day-open/SKILL.md
und daily-template.md. Dann installiere das Paket in dieses Projekt:

1. die drei Skill-Ordner nach .claude/skills/day-setup/, .claude/skills/day-close/
   und .claude/skills/day-open/ (je die SKILL.md)
2. daily-template.md nach references/daily-template.md
3. die Ordner references/ und daily/ anlegen, falls es sie nicht gibt

Ändere an den Skills und der Vorlage nichts: sie enthalten keine Namen,
Bereiche oder Werkzeuge, das kommt alles aus references/tagesritual.md,
die /day-setup gleich mit mir schreibt. Starte danach /day-setup und
führe das Interview mit mir.

Am Ende sag mir, wie es weitergeht: heute Abend /day-close, morgen früh
/day-open.
```

## Hinweise

- Ohne Kalender-Werkzeug lebt der Plan nur in der Tagesdatei; `/day-close` legt dann keine Blöcke an und erwähnt den Kalender nicht.
- Die Skills sind englisch geschrieben, das Interview und die Konfiguration deutsch. Die Sprache des Gesprächs und der Tagesdatei legt `/day-setup` fest.
- Die Datumswerte im Kopf der Skills kommen aus `date -v+1d` (macOS). Unter Linux `date -d '+1 day'` einsetzen.
- Die Konfigurationsdatei ist Markdown mit festen Überschriften. Inhalt frei ändern, Überschriften nicht umbenennen: die Skills suchen sie wörtlich.
