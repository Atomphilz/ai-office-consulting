---
name: video-ad
description: Baut ein Motion-Graphics-Video als Anzeige für ein Produkt, Buch, Kurs, eine App oder Dienstleistung, mit Remotion, bis zur fertigen MP4. Trigger auf "/video-ad", "Videoanzeige bauen", "Motion-Ad", "Werbevideo für", "Sponsored Brands Video", "Reel für mein Produkt", "Video Ad". Fragt die Angaben zum Angebot ab, zeigt Szenenplan und Hook-Ideen zur Freigabe, baut dann, prüft sich selbst per Kontaktbogen und rendert.
---

## Was dieser Skill tut

Aus einem Angebot, seinem Hero-Visual (Cover, Produktfoto, Screenshot, Logo)
und echten Belegen entsteht ein 6–30-Sekunden-Video für eine Anzeigenplattform:
ohne Ton verständlich, das Visual mit Körper statt flach, zwei Hook-Varianten
mit gleichem Rest für den A/B-Test. Technik: Remotion (React), `bun`,
`ffmpeg`. Das Vorgehen steht vollständig in `prompt.md` neben dieser Datei;
der Skill ist nur der Einstieg und hält die Reihenfolge ein.

## Ablauf

1. **Lies `prompt.md`** in diesem Ordner, vollständig. Teil A ist das Formular,
   Teil B der Auftrag. Beides gilt wörtlich.
2. **Angaben einsammeln (Teil A).** Drei Wege, in dieser Reihenfolge prüfen:
   - Der Nutzer hat eine ausgefüllte Kopie von Teil A mitgegeben oder einen
     Pfad genannt: lesen, fertig.
   - Im Projekt liegen Beschreibung, Visual, Bewertungen, Landingpage-Text
     oder eine Positionierung: daraus vorbefüllen, dem Nutzer die Tabelle
     zeigen und nur die Lücken fragen.
   - Sonst Teil A als Interview, gebündelt in höchstens vier Fragenblöcken
     (Angebot, Zielgruppe, Belege, Plattform und Stil). Unbekanntes bleibt
     leer, nichts raten.
3. **Teil B ausführen**, Schritt 0 bis 6. Die beiden Pausen sind Pflicht:
   Freigabe des Szenenplans vor dem Bauen (Schritt 3), Freigabe der Vorschau
   vor dem finalen Render (Schritt 5). Audio erst nach der ersten Freigabe,
   es kostet Credits.
4. **Projekt außerhalb des Textrepos anlegen**, in einem eigenen leeren
   Ordner (Remotion zieht `node_modules` und Renderdateien im hohen
   Megabyte-Bereich). Den Pfad am Anfang nennen.
5. **Ergebnis** wie in Teil B: je Hook und Format eine MP4 unter `export/`,
   dazu eine `README.md` mit Quellen, Plattformregeln und offenen Punkten.
   Nichts wird hochgeladen; das macht der Nutzer im Anzeigenkonto selbst.

## Regeln, die über Teil B hinaus gelten

- **Ein Schalter je optionaler Szene** in `src/script.ts` (z. B.
  `OPTIONS.includeQuote`). Lehnt die Plattform eine Szene in der Moderation
  ab, wird sie ausgeschaltet und neu gerendert, statt das Skript umzubauen.
- **Bauen und Schalten sind zwei Entscheidungen.** Der Skill liefert die Datei.
  Ob und wann die Anzeige läuft, hängt davon ab, was sonst gerade am Angebot
  getestet wird (Preis, Text, andere Kampagnen). Am Ende einen Satz dazu
  sagen, nicht zum Upload drängen.
- **Richtlinienfragen ehrlich beantworten.** Manche Plattformrichtlinien sind
  nur eingeloggt lesbar. Was die Web-Recherche nicht belegt, als offen in die
  README schreiben, nicht als geklärt.
