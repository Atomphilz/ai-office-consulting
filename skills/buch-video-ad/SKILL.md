---
name: buch-video-ad
description: Baut ein Motion-Graphics-Video als Amazon-Anzeige für ein Buch, mit Remotion, bis zur fertigen MP4. Trigger auf "/buch-video-ad", "Videoanzeige fürs Buch", "Sponsored Brands Video", "Motion-Ad", "Amazon Video Ad bauen", "Buchvideo". Fragt die Angaben zum Buch ab, zeigt Szenenplan und Hook-Ideen zur Freigabe, baut dann, prüft sich selbst per Kontaktbogen und rendert.
---

## Was dieser Skill tut

Aus einem Buch, seinem Cover und echten Belegen entsteht ein 15–30-Sekunden-
Video für Amazon Ads: ohne Ton verständlich, Cover als 3D-Buch, zwei Hook-
Varianten mit gleichem Rest für den A/B-Test. Technik: Remotion (React),
`bun`, `ffmpeg`. Das Vorgehen steht vollständig in `prompt.md` neben dieser
Datei; der Skill ist nur der Einstieg und hält die Reihenfolge ein.

## Ablauf

1. **Lies `prompt.md`** in diesem Ordner, vollständig. Teil A ist das Formular,
   Teil B der Auftrag. Beides gilt wörtlich.
2. **Angaben einsammeln (Teil A).** Drei Wege, in dieser Reihenfolge prüfen:
   - Der Nutzer hat eine ausgefüllte Kopie von Teil A mitgegeben oder einen
     Pfad genannt: lesen, fertig.
   - Im Projekt liegen Klappentext, Cover, Rezensionen oder eine
     Positionierung: daraus vorbefüllen, dem Nutzer die Tabelle zeigen und nur
     die Lücken fragen.
   - Sonst Teil A als Interview, gebündelt in höchstens vier Fragenblöcken
     (Buch, Zielgruppe, Belege, Format und Stil). Unbekanntes bleibt leer,
     nichts raten.
3. **Teil B ausführen**, Schritt 0 bis 6. Die beiden Pausen sind Pflicht:
   Freigabe des Szenenplans vor dem Bauen (Schritt 3), Freigabe der Vorschau
   vor dem finalen Render (Schritt 5). Audio erst nach der ersten Freigabe,
   es kostet Credits.
4. **Projekt außerhalb des Textrepos anlegen**, in einem eigenen leeren
   Ordner (Remotion zieht `node_modules` und Renderdateien im hohen
   Megabyte-Bereich). Den Pfad am Anfang nennen.
5. **Ergebnis** wie in Teil B: je Hook und Format eine MP4 unter `export/`,
   dazu eine `README.md` mit Quellen, Amazon-Regeln und offenen Punkten.
   Nichts wird hochgeladen; das macht der Nutzer im Ads-Konto selbst.

## Regeln, die über Teil B hinaus gelten

- **Ein Schalter je optionaler Szene** in `src/script.ts` (z. B.
  `OPTIONS.includeExpertQuote`). Lehnt Amazon eine Szene in der Moderation ab,
  wird sie ausgeschaltet und neu gerendert, statt das Skript umzubauen.
- **Bauen und Schalten sind zwei Entscheidungen.** Der Skill liefert die Datei.
  Ob und wann die Anzeige läuft, hängt davon ab, was sonst gerade am Buch
  getestet wird (Klappentext, Preis, Sponsored-Products-Anzeigen). Am Ende
  einen Satz dazu sagen, nicht zum Upload drängen.
- **Richtlinienfragen ehrlich beantworten.** Die ausführlichen Amazon-Ads-
  Richtlinien sind nur eingeloggt lesbar. Was die Web-Recherche nicht belegt,
  als offen in die README schreiben, nicht als geklärt.
