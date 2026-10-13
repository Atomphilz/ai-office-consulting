---
name: day-setup
disable-model-invocation: true
description: Richtet das Tagesritual ein, einmalig. Ein Interview in höchstens sieben Fragen schreibt references/tagesritual.md, die Konfigurationsdatei, aus der /day-close und /day-open alles Persönliche lesen (Bereiche, Abendfragen, Morgenquellen, Werkzeuge, Spannungen, Ausschlüsse). Läuft erneut, um einzelne Abschnitte zu ändern. Trigger auf "/day-setup", "Tagesritual einrichten", "day-open einrichten", "richte das Tagesritual ein".
---

## Was dieser Skill tut

Schreibt `references/tagesritual.md`, die eine Datei, aus der `/day-close`
(abends, ~5 Minuten) und `/day-open` (morgens, 60 Sekunden) alles holen, was
den Nutzer betrifft. Die beiden Skills selbst kennen keinen Namen, keinen
Bereich, kein Werkzeug. Was in ihnen steht, ist Mechanik; was hier entsteht,
ist Inhalt.

Die Datei ist lesbares Markdown und darf jederzeit per Hand geändert werden.
Dieser Skill ist nur der bequeme Weg, sie beim ersten Mal zu füllen, und der
sichere Weg, sie später abschnittsweise zu ändern.

## Was fest ist, und warum

Die Mechanik der beiden Skills ist **nicht konfigurierbar**, und dieser Skill
fragt nicht danach:

- **Abends schwer, morgens trivial.** Der Abend denkt, der Morgen liest vor.
  Die ungleiche Teilung ist Absicht: eine schwere und eine triviale Hälfte,
  damit die triviale schlechte Tage überlebt. Zwei schwere tägliche Rituale
  sterben.
- **Der Morgen meldet nur, was den Plan bricht.** Kein Postfach-Dump, keine
  zweite Planungsrunde.
- **Ein ausgelassener Abend wird nie erwähnt.** Der Morgen degradiert dann zu
  einem kalten Brief und schreibt die Tagesdatei selbst.
- **Der Abend schlägt den Fokus vor, der Nutzer wählt.**
- **Jede Tagesdatei trägt Plan und ehrlichen Rückblick**, eine Datei pro Tag.
- **Kalenderblöcke nur, wenn ein Kalenderwerkzeug konfiguriert ist.** Sonst
  lebt der Plan nur in der Tagesdatei.
- **Kein Zug endet mit einem Tool-Aufruf, wenn der Text davor für den Nutzer
  ist.**

Das steht am Ende der Datei unter `## Nicht konfigurierbar`, damit der Leser
es weiß, bevor er versucht, es zu ändern.

## Ablauf

### Schritt 1 — Bestand prüfen

Prüfen, ob `references/tagesritual.md` existiert.

- **Existiert nicht:** kurz sagen, was gleich passiert (ein Interview, höchstens
  sieben Fragen, am Ende eine Datei), dann Schritt 2.
- **Existiert:** die Datei lesen und in höchstens acht Zeilen zusammenfassen
  (Name, Bereiche mit Priorität, was abends gefragt wird, was morgens geprüft
  wird, Werkzeuge, Spannungen, Ausschlüsse). Dann eine Frage:
  *„Ganz neu schreiben, oder einzelne Abschnitte ändern? Welche?"* Bei
  einzelnen Abschnitten nur die zugehörigen Fragen aus Schritt 2 stellen, der
  Rest der Datei bleibt wörtlich stehen. Vor dem Überschreiben die alte Fassung
  nach `archives/tagesritual-<YYYY-MM-DD-HHMM>.md` kopieren.

### Schritt 2 — Das Interview (höchstens sieben Fragen)

Fragen, die nicht voneinander abhängen, **gebündelt** stellen, nicht eine nach
der anderen. Jede Frage erlaubt *„weiß nicht"* und bekommt dann den genannten
Standard. Bei jeder Antwort nachhaken, bis sie konkret genug ist, dass ein
Skill damit arbeiten kann, aber nichts erfinden: was der Nutzer nicht sagt,
steht nicht in der Datei.

**Bündel A — wer und was (Fragen 1–2)**

1. **Wer bist du, wie sprechen wir, in welcher Sprache?** Name, du oder Sie,
   Sprache im Gespräch und in der Tagesdatei. Dazu, in einem Satz: *welchen
   Schmerz soll das Ritual angreifen?* (Standard: „kein Tagesplan, Dinge
   werden in Ankunftsreihenfolge erledigt".)
2. **Welche Bereiche gibt es, und was hat gerade Priorität?** Jeder Bereich
   mit Kurzname (so, wie er in Kalenderblöcken stehen soll), einem Einzeiler
   und seiner aktuellen Priorität oder „ruht". Wenn die Ziele irgendwo
   aufgeschrieben sind, nur den Pfad nehmen, keine Kopie. (Standard: ein
   Bereich „Arbeit", keine Prioritätenquelle.)

**Bündel B — abends und morgens (Fragen 3–4)**

3. **Was soll abends erfasst werden, das sonst nirgends steht?** Beispiele
   zum Anstoßen, nicht als Vorgabe: Geld, das in keinem System auftaucht;
   Zusagen am Telefon oder in Chats, die der Skill nicht sieht; ein täglicher
   Schritt nach außen, der gezählt werden soll. Daraus werden die Abendfragen
   in ihrem Wortlaut und, wo nötig, feste Zeilen in der Tagesdatei. (Standard:
   nur die beiden festen Fragen „Was ist heute passiert?" und „Hast du jemandem
   etwas versprochen?", keine Zusatzzeilen.)
4. **Was soll morgens geprüft werden, und womit?** Kalender, Postfach, Logs
   von Hintergrundläufen; für jede Quelle das Werkzeug oder den Befehl, und
   die Regel, was davon gemeldet wird. Für das Postfach: wann eine Mail in den
   Morgenbrief darf. (Standard: nur der Kalender, wenn es einen gibt; sonst
   nichts.)

**Bündel C — Werkzeuge und Grenzen (Fragen 5–7)**

5. **Wo liegt die Tagesdatei, und gibt es ein Kalenderwerkzeug?** Ordner der
   Tagesdatei; Kalender lesen und schreiben, mit Befehl, Kalender-ID und
   Zeitzone, oder „kein Kalender". Dazu: gilt für Schreibbefehle eine
   Dry-run- oder Bestätigungsregel? (Standard: `daily/`, kein Kalender.
   Ohne Kalender legt `/day-close` keine Blöcke an.)
6. **Welche Spannungen sollen beim Planen benannt werden?** Zwei Dinge, die
   um dieselben Stunden konkurrieren; ein Puffer, der fehlt; ein Thema, das
   nie als Trade-off verkauft werden darf. Je eine Zeile. (Standard: keine.)
7. **Was gehört nie ins Tagesritual?** Dokumente, die der Morgen nicht lesen
   soll; Bereiche, die geschlossen sind und nicht eingeplant werden. (Standard:
   nichts.)

Nicht mehr als diese sieben. Wer mehr will, ändert die Datei per Hand.

### Schritt 3 — Datei schreiben

`references/tagesritual.md` schreiben, mit genau diesen Überschriften in dieser
Reihenfolge; die Skills suchen sie wörtlich:

```
## Kopf
## Bereiche
## Abends erfassen        (Unterabschnitte: Vorher lesen · Die Fragen · Zeilen in der Tagesdatei · Terminquellen für Schritt 3)
## Morgens prüfen         (Unterabschnitt: Mail-Filter)
## Werkzeuge
## Spannungen
## Nie im Tagesritual
## Nicht konfigurierbar
```

Im Kopf der Datei: Datum des Interviews, der Hinweis „per Hand änderbar;
`/day-setup` erneut ausführen überschreibt nach Rückfrage" und die Tabelle,
welche Überschrift von welchem Skill gelesen wird. Unter `## Nicht
konfigurierbar` die Liste aus „Was fest ist" oben, wörtlich. Unter `## Abends
erfassen` → *Zeilen in der Tagesdatei* steht, welche Zeilen zusätzlich in den
Plan-Teil (unter `## Focus`) und in den Abend-Teil (zwischen `**What
happened:**` und `**Promised to someone:**`) der Tagesdatei kommen; bei
„keine" steht dort „keine". Den Ordner der Tagesdatei anlegen, falls er fehlt.

Eine bestehende Datei nie stillschweigend überschreiben: Schritt 1 hat
gefragt, und die Sicherung liegt in `archives/`.

### Schritt 4 — Zeigen und schließen

Die fertige Datei im Chat zeigen, ganz. Dann drei Zeilen, nicht mehr:

```
Tagesritual eingerichtet: references/tagesritual.md (per Hand änderbar).
Heute Abend: /day-close.   Morgen früh: /day-open.
Die Mechanik ist fest, der Inhalt ist deiner. Abschnitt ändern: /day-setup oder direkt in der Datei.
```

Kein Zug endet mit einem Tool-Aufruf, wenn der Text davor für den Nutzer ist:
erst schreiben, dann sprechen.

## Regeln

- **Sieben Fragen sind die Obergrenze.** Keine achte im Gespräch.
- **Nichts erfinden.** Standardwerte sind die genannten, sonst steht „keine".
- **Nicht die Mechanik verhandeln.** Wer sie ändern will, ändert die Skills.
- **Idempotent.** Erneut laufen ändert nur die gewählten Abschnitte und sichert
  die alte Fassung.
- **Vorlage nicht anfassen.** `references/daily-template.md` ist generisch und
  wird aus der Konfiguration gefüllt; dieser Skill schreibt sie nicht.
