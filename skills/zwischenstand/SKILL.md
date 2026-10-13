---
name: zwischenstand
description: Zieht einen Zwischenstand der laufenden Session als Übergabedatei und bereitet den Wechsel in eine frische Session vor. Wird vom Kontext-Wächter ausgelöst (Hinweis ab 100k Token, Meldung ab 140k), kann aber jederzeit laufen. Trigger auf "/zwischenstand", "zieh einen Zwischenstand", "Übergabe schreiben", "Session wird zu groß", "mach einen Cut".
---

## Was dieser Skill tut

Beendet eine Session, bevor sie sich aufbläht, ohne dass etwas verloren geht.
Er schreibt eine Übergabedatei im Format, das Philipp seit dem 9. September
2026 per Hand nutzt, legt einen Zeiger für die nächste Session ab und sagt
Philipp, dass er `/clear` tippen soll. Der `SessionStart`-Hook lädt die
Übergabe dann automatisch in die frische Session.

Warum nicht `/compact`: Die Zusammenfassung dort liegt nirgends und ist nicht
lesbar. Die Datei liegt in `references/`, in Git, und ist auch für `/day-close`
brauchbar. Wer beides will, macht erst den Zwischenstand, dann `/clear`.

**Schreibt direkt, ohne Entwurf.** Entschieden 12. Sept 2026: Die Datei liegt in
Git und ist umkehrbar; ein Bestätigungsschritt bei vollem Kontext kostet genau
das, was gespart werden soll.

## Weitere Auslöser, unabhängig von der Größe

Ergänzt 14. Sept 2026 nach Nates Caching-Video
(`knowledge/nate/2026-09-14-nate-save-you-millions-of-claude-tokens/auswertung.md`).
Der Prompt-Cache lebt im Abo eine Stunde und hängt am Anfang des Kontexts.
Alles, was den Anfang ändert oder die Stunde überschreitet, zahlt den gesamten
Kontext neu. Deshalb Zwischenstand auch dann, wenn die Session noch unter 100k
liegt:

- **Pause über 60 Minuten und neue Aufgabe.** Der Wächter meldet die kalte
  Pause ab 40k Kontext. Geht es mit derselben Aufgabe weiter, darf die Session
  bleiben. Fängt etwas anderes an: Zwischenstand, `/clear`.
- **Modellwechsel.** `/model` bricht den Cache vollständig, jedes Modell hat
  seinen eigenen. Wer Opus für eine Aufgabe will: erst Zwischenstand, dann
  `/clear`, dann `/model`. Nie `/model` in einer laufenden Session über 40k.
- **Kalte Session.** Der Wächter sperrt eine Session, deren Übergabe liegt und
  deren letzter Call über 60 Minuten her ist: jede Nachricht außer Slash-
  Befehlen wird mit dem Hinweis auf `/clear` abgewiesen, kostet nichts. Der
  Abwesenheitstimer lief nur am 16. Sept 2026 und ist abgeschaltet (Log
  16. Sept). Hintergrundaufgaben über 40k enden mit einer Übergabe (CLAUDE.md).
- **Extra-Usage.** Meldet Claude Code, dass das Wochenlimit erreicht ist und
  Extra-Usage greift, fällt die Cache-Lebensdauer auf fünf Minuten. Große
  Sessions dann sofort beenden und bis zum Reset nur in kleinen arbeiten.

## Ablauf

1. **Laufenden Werkzeugschritt abschließen.** Nichts halb fertig lassen: ein
   begonnener Dry-Run, ein halb geschriebenes Dokument, ein offener Mailentwurf
   wird erst zu Ende gebracht oder ausdrücklich als „abgebrochen bei …" notiert.

2. **Datei schreiben:** `references/zwischenstand-<YYYY-MM-DD>-<slug>.md`.
   Slug = zwei, drei Wörter zum Thema der Session, klein, mit Bindestrich
   (`velamed-benedikt`, `altes-macbook`, `listing-pt`). Gibt es an dem Tag schon
   eine Datei zum selben Thema, wird sie **fortgeschrieben**, nicht dupliziert.
   Ziel: **unter 5.000 Token**, etwa 200 Zeilen. Lieber Tabelle als Prosa.

3. **Zeiger ablegen:** `.claude/uebergabe-aktiv.md`. Erste Zeile: der Pfad der
   Datei relativ zum Projekt. Zweite Zeile: das Ein-Satz-Ziel. Sonst nichts.
   Der Zeiger ist gitignored und wird vom Hook nach dem Laden gelöscht.

4. **Philipp sagen, in zwei Sätzen:** wohin die Datei geschrieben wurde und was
   das Ziel der nächsten Sitzung ist. Letzter Satz wörtlich: **„Jetzt `/clear`."**
   Danach nichts mehr anfangen. Keine neue Aufgabe in dieser Session.

## Aufbau der Datei

```markdown
# Zwischenstand — <Datum>, <Tageszeit> — <Thema>

*Übergabedokument. Vorgänger: `<Datei>` oder „keiner". Entität: <E1–E6 oder P1–P4>.
**Ziel der nächsten Sitzung, ein Satz: …***

## Kurzfassung
| Frage | Antwort |   ← die drei bis sechs Fragen, die jemand nach dem Öffnen stellt

## Erledigt in dieser Session
Nummerierte Liste. Was gebaut, entschieden, verschickt wurde. Mit Dateipfaden.

## Befunde, die bleiben
Was gelernt wurde und über die Session hinaus gilt. Zahlen, Pfade, Zusagen.

## Offene Fragen an Philipp
Nur die, die die nächste Session blockieren. Gebündelt, nicht verstreut.
Pflichtabschnitt: wenn leer, steht hier „keine".

## Laufender Zustand
Hintergrundprozesse (Aufnahmemaschine, Subagenten, Monitor), offene Dry-Runs,
Gmail-Entwürfe, die noch nicht abgeschickt sind. Mit Kennung und wie man sie
beendet. Pflichtabschnitt: wenn leer, steht hier „keine".

## Nächste Schritte, in Reihenfolge
Der erste Schritt so konkret, dass die neue Session ihn ohne Rückfrage beginnt.
Wo etwas gebaut wurde: ein Prüfschritt dazu (Befehl oder Blick, erwartetes Ergebnis).

## Für `/day-close` heute Abend
Bargeld, Telefonzusagen, verschobene Blöcke, was ins Tagesblatt gehört.
```

Weglassen, was leer wäre, außer den zwei Pflichtabschnitten. Nicht hinein: das Drei-Jahres-Horizont-Dokument,
Dinge, die schon in `context/` oder `decisions/log.md` stehen. Was ins
Entscheidungslog gehört, wird **dort** eingetragen und in der Übergabe nur
verlinkt.

## Regeln

- **Ein Satz Ziel ist Pflicht.** Ohne ihn fängt die nächte Session mit Lesen an
  statt mit Arbeiten. Das hat sich am 12. Sept bewährt.
- **Entität nennen.** Sechs Sets an Geld und Gegenparteien; die nächste Session
  darf nicht raten müssen, wessen Konto gemeint ist.
- **Keine Bewertung des Verbrauchs.** Nicht „die Session war zu lang". Der
  Zwischenstand ist ein Werkzeug, kein Tadel. Siehe die Regel zu Ritualen in
  den Memories: besser, nicht perfekt.
- **Die ganze Session durchgehen**, nicht die letzten Schritte. Übergaben
  verlieren, was am Anfang entschieden wurde. Und **kein Dateisystem-Audit**:
  nichts per `git log` oder Suche neu entdecken, nur, was diese Session
  angefasst hat. Beides aus Nates `/session-handoff`, 14. Sept 2026.
- **Nichts erfinden.** Was nicht sicher ist, steht als „unklar", nicht als Fakt.
- **Wenn der Wächter mitten in einer Aufgabe meldet**, die ohne den vollen
  Kontext nicht fertig wird (langes Transkript prüfen, Verhandlungsanalyse),
  wird die Aufgabe zu Ende gebracht und der Zwischenstand direkt danach
  gezogen. Der Hinweis ist beratend, nicht blockierend.
