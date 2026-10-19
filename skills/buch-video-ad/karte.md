---
titel: /buch-video-ad
kurz: Ein Formular ausfüllen, Claude Code baut daraus eine fertige Amazon-Videoanzeige für ein Buch. Motion Graphics mit Remotion, zwei Hook-Varianten für den A/B-Test, ohne Ton verständlich, nichts erfunden.
autor: Fabian Gless
seit: 2026-10-19
stand: 2026-10-19
braucht: Claude Code, Internet; bun und ffmpeg installiert Claude bei Bedarf mit
---

## Was es tut

Amazon spielt Videoanzeigen meist stumm ab, und die ersten anderthalb Sekunden entscheiden. Ein Motion-Graphics-Video nach Agenturart kostet Geld oder Tage in After Effects. Der Skill macht daraus einen Nachmittag in Claude Code.

Du füllst Teil A des Prompts aus: Buch, Zielgruppe, echte Belege (Sterne, Rang, Zitate), Format, Stil. Claude recherchiert die aktuellen Amazon-Ads-Vorgaben für den Anzeigentyp, schlägt drei Hooks vor, zeigt dir den Szenenplan als Tabelle und wartet auf dein Okay. Dann baut es das Video mit Remotion: Cover als 3D-Buch, Kinetic Type, Stempel und Sticker für Belege, Schlusskarte mit Handlungsaufforderung. Vor dem finalen Render prüft es sich selbst über einen Kontaktbogen mit markierter Randzone und zeigt dir die Vorschau. Ergebnis: je Hook und Format eine MP4 plus eine README mit Quellen und offenen Punkten.

Am 19. Oktober 2026 so für „Die Kraft deines Zyklus" gebaut: 26 Sekunden, 1920×1080, zwei Hooks, ein Nachmittag.

## Key Benefits

- **Nichts erfinden.** Bewertungen, Ränge, Zitate und Zahlen kommen nur aus deinem Formular. Fehlt etwas, bleibt es weg. Jede Zahl im Video trägt eine Quellenzeile.
- **A/B-Test eingebaut.** Zwei Hooks, derselbe Rest. Der Test zeigt sauber, welcher Einstieg zieht.
- **Eine Datei steuert alles.** Texte, Timing, Szenen stehen in `src/script.ts`. Ein Satz geändert, neu gerendert, fertig. Optionale Szenen haben einen Schalter, falls Amazon eine Szene ablehnt.
- **Zwei Freigaben, kein Blindflug.** Vor dem Bauen den Szenenplan, vor dem Render die Vorschau. Audio erst nach dem ersten Okay, weil es Credits kostet.
- **Eine Bühne, alle Formate.** 16:9, 1:1 und 9:16 aus demselben Layout, mit sicherer Zone für Plattform-UI.

## Im Paket

- `SKILL.md`: der Einstieg. Sammelt Teil A ein (aus Datei, aus dem Projekt oder im Interview) und hält die Reihenfolge von Teil B ein.
- `prompt.md`: Fabians Prompt in voller Länge. Teil A ist das Formular, Teil B der Auftrag an Claude mit Grundsätzen, sechs Schritten und Prüfliste. Funktioniert auch ohne Skill: ausfüllen, komplett in Claude Code kopieren.

## Einbindung

Ordner entpacken, in Claude Code den Pfad einsetzen und diesen Prompt schicken:

```
Ich habe den Ordner "buch-video-ad" aus dem Zip nach <PFAD> entpackt.
Lies zuerst SKILL.md und prompt.md. Dann installiere den Skill in dieses
Projekt: beide Dateien nach .claude/skills/buch-video-ad/, unverändert.

Sag mir danach, wie ich ihn starte: /buch-video-ad in einem Projekt, in
dem Cover und Klappentext des Buchs liegen, oder mit einer ausgefüllten
Kopie von Teil A aus prompt.md.
```

## Hinweise

- Das Remotion-Projekt gehört in einen eigenen leeren Ordner, nicht ins Textrepo: `node_modules` und Renderdateien sind groß.
- Die ausführlichen Amazon-Ads-Richtlinien sind nur eingeloggt lesbar. Was Claude per Web-Recherche nicht belegen kann, steht als offener Punkt in der README; ob Expertenzitate oder Sterne im Video erlaubt sind, prüfst du selbst im Ads-Konto.
- Bauen und Schalten sind zwei Entscheidungen. Läuft am Buch gerade ein anderer Test (Klappentext, Preis), lieber warten, sonst ist der Effekt nicht lesbar.
- Voice-over über ElevenLabs ist optional. Der API-Key gehört in eine `.env`, nie in den Prompt.
- Allgemeine Fassung für Apps, Kurse, Produkte und Dienstleistungen: `/video-ad` auf dieser Seite. Diese Karte ist die Buchfassung mit Klappentext, Cover als 3D-Buch und Amazon-Ads-Regeln.
