# Prompt: Motion-Graphics-Video für eine Amazon-Buchanzeige

> **So benutzt du das:** Füll Teil A aus (alles in `[eckigen Klammern]` ersetzen, Unbekanntes leer lassen oder „weiß nicht" schreiben). Dann den kompletten Text — Teil A + Teil B — in Claude Code kopieren, am besten in einem neuen, leeren Ordner. Claude baut das Video dort mit Remotion (React-basiertes Video-Framework) und rendert eine fertige MP4.
>
> Voraussetzungen auf dem Rechner: Claude Code, Internet. `bun` und `ffmpeg` installiert Claude bei Bedarf mit dir zusammen.

---

## TEIL A — Deine Angaben

### Das Buch
- **Titel:** [Titel]
- **Untertitel:** [Untertitel oder leer]
- **Autor:** [Name, wie er auf dem Cover steht]
- **Genre / Kategorie:** [z. B. Thriller, Ratgeber Finanzen, Fantasy, Biografie]
- **Worum geht's in einem Satz:** [Ein Satz, so wie du ihn einem Fremden erzählen würdest]
- **Klappentext:** [Klappentext reinkopieren]
- **Cover-Datei:** [Pfad zur Datei, z. B. ~/Desktop/cover.jpg — möglichst hochauflösend, ideal ≥ 1600 px Höhe]
- **Formate:** [Taschenbuch / E-Book / Hörbuch / Kindle Unlimited — was gibt es?]
- **Preis:** [z. B. 14,99 € Taschenbuch, 4,99 € E-Book — oder leer, wenn der Preis nicht ins Video soll]
- **Seitenzahl:** [optional]

### Zielgruppe
- **Wer soll das Buch lesen:** [z. B. Frauen 35–55, die skandinavische Krimis mögen / Selbstständige, die ihre Steuern selbst machen]
- **Vergleichbare Bücher / Autoren („für Fans von …"):** [2–3 Titel oder Autoren]
- **Das Problem oder der Wunsch des Lesers, den das Buch anspricht:** [z. B. „will abends abschalten und nicht wissen, wer der Täter ist" / „hat Angst vor der Steuererklärung"]

### Belege (nur echte, überprüfbare Dinge — nichts davon erfinden lassen)
- **Bewertung auf Amazon:** [z. B. 4,6 Sterne bei 212 Bewertungen — oder leer]
- **Bestseller-Rang / Auszeichnungen:** [z. B. „#1 in Kategorie X am 03.10.2026" — oder leer]
- **Zitate von Rezensenten / Presse / bekannten Personen:** [Zitat + Quelle — oder leer]
- **Zahlen aus dem Buch, die neugierig machen:** [z. B. „7 Methoden", „in 30 Tagen", eine überraschende Statistik mit Quelle — oder leer]
- **Starke Sätze oder kurze Zitate aus dem Buch selbst:** [1–5 Sätze, die Lust aufs Lesen machen]

### Video-Format (bitte vorher im Amazon-Ads-Konto nachsehen, wo die Anzeige laufen soll)
- **Anzeigentyp:** [z. B. Sponsored Brands Video / Sponsored Display Video / Streaming-TV / weiß nicht]
- **Seitenverhältnis + Auflösung:** [z. B. 16:9 = 1920×1080 / 1:1 = 1080×1080 / 9:16 = 1080×1920 / weiß nicht]
- **Länge:** [z. B. 15 s / 20 s / 30 s]
- **Mehrere Formate gleichzeitig?** [ja: welche / nein]

### Ton & Stil
- **Stimmung des Videos:** [z. B. düster und spannend / warm und humorvoll / klar und sachlich]
- **Farben:** [aus dem Cover übernehmen / eigene Farben: …]
- **Schriftart:** [wie auf dem Cover / egal / bestimmte Schrift: …]
- **Sprecherstimme (Voice-over)?** [nein, nur Text + Musik / ja, mit ElevenLabs-Account — Stimme: männlich/weiblich, Alter, Stil]
- **ElevenLabs-API-Key vorhanden?** [ja / nein — den Key NICHT hier reinschreiben, Claude fragt danach und legt ihn in eine `.env`-Datei]
- **Musik:** [eigene Datei: Pfad / Claude soll etwas Lizenzfreies vorschlagen / keine Musik]
- **Was auf keinen Fall ins Video soll:** [z. B. Spoiler, bestimmte Wörter, Gesichter]

### Sprache
- **Sprache der Anzeige:** [Deutsch / Englisch / …]
- **Markt:** [amazon.de / amazon.com / …]

---

## TEIL B — Der Auftrag an Claude

Du bist Motion Designer und Performance-Marketer in einer Person. Baue aus den Angaben in Teil A ein Motion-Graphics-Video als Amazon-Anzeige für dieses Buch. Ziel ist ein Video, das im Amazon-Umfeld in der ersten Sekunde auffällt, **ohne Ton** verständlich ist und Leser zum Klick auf das Buch bringt. Technisch baust du es mit **Remotion** (React) und renderst eine fertige MP4.

### Grundsätze

1. **Eine Datei steuert alles.** Lege `src/script.ts` an. Darin stehen pro Szene: Headline-Text, optionaler Voice-over-Text, Fußnote/Quelle und welches Grafik-Element die Szene zeigt. Szenen-Timing, Audio und Render leiten sich daraus ab. Wer einen Satz ändert, ändert nur diese Datei.
2. **Stumm verständlich.** Amazon spielt Videos meist ohne Ton ab. Die Bildschirmtexte tragen die Aussage, der Ton ist Bonus.
3. **Nichts erfinden.** Bewertungen, Ränge, Zitate und Zahlen kommen nur aus Teil A. Fehlt etwas, bleibt es weg — du formulierst keine Ersatz-Belege und keine „über 1.000 begeisterte Leser", die nirgends stehen. Jede Zahl im Video bekommt eine kleine Quellenzeile.
4. **Das Cover ist der Star.** Das Buchcover muss mehrfach groß und gut lesbar im Bild sein — mindestens im Einstieg oder spätestens nach 3 Sekunden und auf der Schlusskarte. Animiere es als 3D-Buch (leichte Drehung, Schatten, Lichtkante), nicht als flaches Bild.

### Schritt 0 — Format und Regeln klären

- Prüfe die **aktuellen Amazon-Ads-Vorgaben** für den Anzeigentyp aus Teil A (Web-Recherche auf der offiziellen Amazon-Ads-Seite): erlaubte Seitenverhältnisse, Auflösung, Länge, Dateigröße, Bildrate, Ton-Vorgaben, Regeln für Text im Bild, ob Sternebewertungen/Rezensionszitate/Preise/Handlungsaufforderungen erlaubt sind, ob Schwarzbilder am Anfang/Ende verboten sind. Fasse die Regeln, die für dieses Video gelten, in 5–10 Punkten zusammen und nenne die Quelle.
- Steht beim Format „weiß nicht", schlag auf Basis der Recherche ein Format vor und begründe es in einem Satz.
- Fehlen in Teil A Angaben, die du wirklich brauchst (z. B. Cover-Datei), frag gezielt nach. Alles andere: sinnvoll annehmen und die Annahme nennen.

### Schritt 1 — Konzept: drei Hook-Ideen

Die ersten 1,5 Sekunden entscheiden. Schlag **drei unterschiedliche Hooks** vor, z. B.:

- **Frage/Problem-Hook:** spricht den Wunsch oder das Problem des Lesers direkt an.
- **Zitat-Hook:** der stärkste Satz aus dem Buch, Wort für Wort eingeblendet.
- **Beleg-Hook:** Bewertung, Rang oder Pressezitat groß im Bild (nur wenn in Teil A vorhanden).
- **„Für Fans von …"-Hook:** wenn vergleichbare Titel angegeben sind.

Regeln für den Hook: **Frame 0 zeigt schon Inhalt** (dient als Vorschaubild, kein leerer Start, kein Schwarzbild), die Kernaussage ist in unter 1,5 Sekunden lesbar.

Danach der Aufbau (für 15–30 s, kürzer = weniger Szenen):

1. **Hook** (0–3 s)
2. **Versprechen / Prämisse** — worum es geht, was der Leser bekommt (ein Satz, Cover im Bild)
3. **1–3 Beweis- oder Neugier-Szenen** — Zitat, Bewertung, Zahl aus dem Buch, „Für Fans von …", Inhaltsversprechen. Jede Szene hat einen visuellen „Punch" (Stempel, Sticker, Zähler, Sterne, die nacheinander aufploppen).
4. **Schlusskarte** — Cover groß, Titel, Autor, Format/Preis falls erlaubt und angegeben, eine klare Handlungsaufforderung, die den Amazon-Regeln aus Schritt 0 entspricht. Mindestens 2 Sekunden stehen lassen.

**Gleicher Body, nur der Hook wechselt:** Baue das Video so, dass zwei Hook-Varianten denselben Rest teilen. Dann zeigt ein A/B-Test sauber, welcher Hook besser zieht.

### Schritt 2 — Skript-Regeln

- **Headlines:** max. 2 Zeilen, kurze Zeilen (bei großer Schrift ca. 15–18 Zeichen pro Zeile). Lieber ein kürzeres Wort als drei Zeilen.
- **Ein Gedanke pro Szene.** Jede Szene muss ca. 1,5–2 Sekunden ruhig lesbar sein, bevor sie wechselt.
- **Voice-over (falls gewünscht):** Wortbudget ca. 2,5 Wörter pro Sekunde abzüglich Übergängen — bei 30 s also höchstens ca. 65–70 Wörter, bei 15 s ca. 30. Zahlen im Sprechtext als Wörter ausschreiben („zweihundertzwölf"), sonst liest die KI-Stimme sie falsch. Ist der Text zu lang: kürzen, nicht die Sprechgeschwindigkeit hochdrehen.
- **Keine Spoiler**, nichts aus „Was auf keinen Fall ins Video soll".

### Schritt 3 — PAUSE: Freigabe

Zeig mir vor dem Bauen eine kompakte Tabelle: Szene · Dauer · Bildschirmtext · Voice-over · Grafik-Element · Quelle der Aussage. Dazu die drei Hook-Ideen mit deiner Empfehlung. **Warte auf meine Freigabe**, bevor du Audio erzeugst (kostet Credits) oder renderst.

### Schritt 4 — Bauen (Remotion)

- Projekt mit `bun` anlegen (nicht npm). Remotion in aktueller stabiler Version, Versionen pinnen.
- **Animation nur über `useCurrentFrame()` + `interpolate`/`spring` mit `extrapolateLeft/Right: "clamp"`.** CSS-`transition`/`animation` funktionieren in Remotion nicht, weil Frame für Frame gerendert wird.
- **Eine Bühne, mehrere Formate:** Layoute alle Szenen in einer festen Bühne und skaliere sie pro Format in die sichere Zone. Keine Pixel-Korrekturen pro Format von Hand.
- **Sichere Zone:** Text und Cover mit genug Abstand zum Rand (mindestens ca. 5–6 % rundherum, bei 9:16 deutlich mehr oben und unten, weil dort Plattform-UI liegt). Nichts Wichtiges darf angeschnitten werden.
- **Typografie:** Kinetic Type — Wörter einzeln per Masken-Reveal einblenden, Schlüsselwörter in Akzentfarbe mit gezeichneter Unterstreichung. Markiere Highlights im Skript pro Wort (`*Wort*`), nie über mehrere Wörter, sonst landet ein Sternchen im Video.
- **Farben aus dem Cover ableiten** (falls nicht anders angegeben): eine Hintergrundfarbe, eine Textfarbe, **eine** Akzentfarbe. Die Akzentfarbe als Fläche nur einmal (z. B. für den Button auf der Schlusskarte), sonst nur für Text und Konturen.
- **Rhythmus:** harte Schnitte unter einem kurzen Wipe (schräge Farbflächen, die genau im Schnitt-Frame voll decken), dezente Hintergrundbewegung (treibende Formen, Partikel, Papier-/Seiten-Textur passend zum Genre), ein kleiner Fortschrittsbalken oder Kapitel-Zähler hält Leute bis zum Ende.
- **Sound (falls Ton gewünscht):** Musikbett leise (ca. 15–20 % Lautstärke) mit Fade-in/-out; SFX für Wipes (Whoosh), Einblendungen (Pop), Punches (Impact/Stempel), Seitenumblättern für das Buch. Voice-over pro Szene als eigener Clip, Stille am Anfang und Ende per ffmpeg trimmen, **Szenenlänge = gemessene Sprechdauer + kurzer Puffer**. Bei ElevenLabs: max. 4 Anfragen parallel, mit Retry.
- **Kein Schwarzbild** am Anfang oder Ende.

### Schritt 5 — Vorschau und Selbstkontrolle

- Rendere zuerst eine **Vorschau in halber Auflösung** (geht schnell).
- Zieh per ffmpeg ca. 24 gleichmäßig verteilte Frames als **Kontaktbogen** (ein PNG-Raster mit Frame-Nummern) und lege ein halbtransparentes **rotes Overlay über die unsichere Randzone**. Schau dir jeden Bogen selbst an und prüfe:
  - [ ] Nichts Wichtiges im roten Bereich, nichts angeschnitten
  - [ ] Kein Text läuft über Kanten oder in andere Elemente
  - [ ] Keine sichtbaren Sternchen oder Steuerzeichen, Unterstreichungen erscheinen erst mit ihrem Wort
  - [ ] Frame 0 zeigt Inhalt, Hook in < 1,5 s lesbar
  - [ ] Cover groß und scharf, Titel lesbar
  - [ ] Jede Zahl/jede Bewertung hat eine Quelle und steht so in Teil A
  - [ ] Akzentfarbe als Fläche nur einmal
  - [ ] Ohne Ton verständlich
- Fehler fixen, neu prüfen. Erst wenn alles grün ist: **zeig mir die Vorschau** und warte auf mein OK.

### Schritt 6 — Finaler Render

- Volle Auflösung, H.264, 30 fps (oder was die Amazon-Vorgaben verlangen), AAC 48 kHz.
- Ton per ffmpeg auf ca. −14 LUFS normalisieren (Bildspur per Stream-Copy übernehmen), falls Amazon nichts anderes vorgibt.
- Prüfe mit `ffprobe`: Auflösung, Länge, Bildrate, Dateigröße innerhalb der Amazon-Grenzen. Melde die Werte.

### Ergebnis

- `export/<buchtitel>-<hook>-<format>.mp4` — je Hook-Variante und Format eine Datei.
- `README.md` mit: Hook-Varianten und welche du empfiehlst, Quellen jeder Aussage im Video, Amazon-Regeln aus Schritt 0 mit Link, Vorschlag für Anzeigen-Headline (im Rahmen der Amazon-Zeichengrenzen), offene Punkte, die ich selbst prüfen muss.
- Du lädst nichts zu Amazon hoch. Das mache ich selbst.
