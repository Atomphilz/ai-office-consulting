# Prompt: Motion-Graphics-Video als Anzeige für ein Produkt oder Angebot

> **So benutzt du das:** Füll Teil A aus (alles in `[eckigen Klammern]` ersetzen, Unbekanntes leer lassen oder „weiß nicht" schreiben). Dann den kompletten Text — Teil A + Teil B — in Claude Code kopieren, am besten in einem neuen, leeren Ordner. Claude baut das Video dort mit Remotion (React-basiertes Video-Framework) und rendert eine fertige MP4.
>
> Funktioniert für alles, was ein Bild und eine Aussage hat: ein Buch, eine App, ein Online-Kurs, eine Dienstleistung, ein physisches Produkt, eine Veranstaltung. Die Beispiele in den Klammern sind nur Beispiele.
>
> Voraussetzungen auf dem Rechner: Claude Code, Internet. `bun` und `ffmpeg` installiert Claude bei Bedarf mit dir zusammen.

---

## TEIL A — Deine Angaben

### Das Angebot
- **Name:** [Produkt-, Buch-, Kurs- oder Angebotsname]
- **Zusatz / Untertitel / Claim:** [oder leer]
- **Absender:** [Autor, Marke, Firma oder Person, so wie es auf dem Visual steht]
- **Art / Kategorie:** [z. B. Thriller, Ratgeber Finanzen, Produktivitäts-App, Yoga-Onlinekurs, Steuerberatung, Küchenmesser]
- **Worum geht's in einem Satz:** [Ein Satz, so wie du ihn einem Fremden erzählen würdest]
- **Längere Beschreibung:** [Klappentext, Produktbeschreibung, Landingpage-Text reinkopieren]
- **Hero-Visual (die eine Datei, die das Angebot zeigt):** [Pfad, z. B. ~/Desktop/cover.jpg oder ~/Desktop/produkt.png — Buchcover, Produktfoto mit freigestelltem Hintergrund, App-Screenshot, Logo; möglichst hochauflösend, ideal ≥ 1600 px Höhe]
- **Weitere Bilder:** [optional: Innenseiten, Screenshots, Detailfotos, Vorher/Nachher — Pfade]
- **Varianten / Formate:** [z. B. Taschenbuch / E-Book / Hörbuch — oder: Basis / Pro — oder leer]
- **Preis:** [z. B. 14,99 € — oder leer, wenn der Preis nicht ins Video soll]
- **Wohin führt der Klick:** [Amazon-Produktseite / App Store / Landingpage / Terminbuchung — URL, falls vorhanden]

### Zielgruppe
- **Wer soll das kaufen oder nutzen:** [z. B. Frauen 35–55, die skandinavische Krimis mögen / Selbstständige, die ihre Steuern selbst machen / Teams von 5–20 Leuten ohne eigene IT]
- **Vergleichbares, das die Zielgruppe schon kennt („für Fans von …", „wie X, nur …"):** [2–3 Titel, Marken oder Produkte]
- **Das Problem oder der Wunsch, den das Angebot anspricht:** [z. B. „will abends abschalten und nicht wissen, wer der Täter ist" / „hat Angst vor der Steuererklärung" / „verliert jeden Montag eine Stunde mit Zusammensuchen"]

### Belege (nur echte, überprüfbare Dinge — nichts davon erfinden lassen)
- **Bewertungen:** [z. B. 4,6 Sterne bei 212 Bewertungen auf Amazon / 4,8 im App Store / 37 Google-Rezensionen — oder leer]
- **Ränge, Auszeichnungen, Zahlen zum Erfolg:** [z. B. „#1 in Kategorie X am 03.10.2026", „Testsieger bei …", „1.200 Kunden seit 2023" — oder leer]
- **Zitate von Kunden / Presse / bekannten Personen:** [Zitat + Quelle — oder leer]
- **Zahlen aus dem Angebot selbst, die neugierig machen:** [z. B. „7 Methoden", „in 30 Tagen", „spart 3 Stunden pro Woche" mit Quelle — oder leer]
- **Starke Sätze oder kurze Zitate aus dem Angebot:** [1–5 Sätze aus dem Buch, dem Kurs, der Website, die Lust machen]

### Video-Format (bitte vorher im Anzeigenkonto nachsehen, wo die Anzeige laufen soll)
- **Plattform und Anzeigentyp:** [z. B. Amazon Sponsored Brands Video / Meta Reels / YouTube Bumper / LinkedIn Video Ad / Website-Header / weiß nicht]
- **Seitenverhältnis + Auflösung:** [z. B. 16:9 = 1920×1080 / 1:1 = 1080×1080 / 9:16 = 1080×1920 / weiß nicht]
- **Länge:** [z. B. 6 s / 15 s / 20 s / 30 s]
- **Mehrere Formate gleichzeitig?** [ja: welche / nein]

### Ton & Stil
- **Stimmung des Videos:** [z. B. düster und spannend / warm und humorvoll / klar und sachlich / schnell und laut]
- **Farben:** [aus dem Hero-Visual übernehmen / Markenfarben: … / eigene Farben: …]
- **Schriftart:** [wie auf dem Visual / Markenschrift: … / egal]
- **Sprecherstimme (Voice-over)?** [nein, nur Text + Musik / ja, mit ElevenLabs-Account — Stimme: männlich/weiblich, Alter, Stil]
- **ElevenLabs-API-Key vorhanden?** [ja / nein — den Key NICHT hier reinschreiben, Claude fragt danach und legt ihn in eine `.env`-Datei]
- **Musik:** [eigene Datei: Pfad / Claude soll etwas Lizenzfreies vorschlagen / keine Musik]
- **Was auf keinen Fall ins Video soll:** [z. B. Spoiler, bestimmte Wörter, Gesichter, Preise, Wettbewerbernamen]

### Sprache
- **Sprache der Anzeige:** [Deutsch / Englisch / …]
- **Markt / Region:** [z. B. amazon.de / DACH / USA]

---

## TEIL B — Der Auftrag an Claude

Du bist Motion Designer und Performance-Marketer in einer Person. Baue aus den Angaben in Teil A ein Motion-Graphics-Video als Anzeige für dieses Angebot. Ziel ist ein Video, das im Feed oder auf der Plattform aus Teil A in der ersten Sekunde auffällt, **ohne Ton** verständlich ist und Leute zum Klick bringt. Technisch baust du es mit **Remotion** (React) und renderst eine fertige MP4.

### Grundsätze

1. **Eine Datei steuert alles.** Lege `src/script.ts` an. Darin stehen pro Szene: Headline-Text, optionaler Voice-over-Text, Fußnote/Quelle und welches Grafik-Element die Szene zeigt. Szenen-Timing, Audio und Render leiten sich daraus ab. Wer einen Satz ändert, ändert nur diese Datei. Optionale Szenen (z. B. ein Zitat, eine Bewertung) bekommen einen Schalter, damit sie ohne Umbau ausgeblendet werden können.
2. **Stumm verständlich.** Die meisten Plattformen spielen Videos ohne Ton ab. Die Bildschirmtexte tragen die Aussage, der Ton ist Bonus.
3. **Nichts erfinden.** Bewertungen, Ränge, Zitate und Zahlen kommen nur aus Teil A. Fehlt etwas, bleibt es weg — du formulierst keine Ersatz-Belege und keine „über 1.000 begeisterte Kunden", die nirgends stehen. Jede Zahl im Video bekommt eine kleine Quellenzeile.
4. **Das Hero-Visual ist der Star.** Es muss mehrfach groß und gut lesbar im Bild sein — mindestens im Einstieg oder spätestens nach 3 Sekunden und auf der Schlusskarte. Gib ihm Körper, statt es flach zu zeigen: ein Buch als 3D-Buch mit leichter Drehung, Schatten und Lichtkante; ein Produkt freigestellt mit Schatten und Parallaxe; eine App als Gerät mit Rahmen; ein Logo mit Tiefe oder Reveal.

### Schritt 0 — Format und Regeln klären

- Prüfe die **aktuellen Vorgaben der Plattform** für den Anzeigentyp aus Teil A (Web-Recherche auf der offiziellen Seite, z. B. Amazon Ads, Meta Business Help, Google Ads, LinkedIn Marketing Solutions): erlaubte Seitenverhältnisse, Auflösung, Länge, Dateigröße, Bildrate, Ton-Vorgaben, Regeln für Text im Bild, ob Bewertungen/Zitate/Preise/Handlungsaufforderungen erlaubt sind, ob Schwarzbilder am Anfang/Ende verboten sind. Fasse die Regeln, die für dieses Video gelten, in 5–10 Punkten zusammen und nenne die Quelle. Was du nicht belegen kannst (manche Richtlinien sind nur eingeloggt lesbar), markierst du als offen.
- Steht beim Format „weiß nicht", schlag auf Basis der Recherche ein Format vor und begründe es in einem Satz.
- Fehlen in Teil A Angaben, die du wirklich brauchst (z. B. das Hero-Visual), frag gezielt nach. Alles andere: sinnvoll annehmen und die Annahme nennen.

### Schritt 1 — Konzept: drei Hook-Ideen

Die ersten 1,5 Sekunden entscheiden. Schlag **drei unterschiedliche Hooks** vor, z. B.:

- **Frage/Problem-Hook:** spricht den Wunsch oder das Problem der Zielgruppe direkt an.
- **Zitat-Hook:** der stärkste Satz aus dem Angebot, Wort für Wort eingeblendet.
- **Beleg-Hook:** Bewertung, Rang oder Pressezitat groß im Bild (nur wenn in Teil A vorhanden).
- **„Wie X, nur …"-Hook:** wenn Vergleichbares angegeben ist.
- **Vorher/Nachher-Hook:** wenn das Angebot einen sichtbaren Unterschied macht.

Regeln für den Hook: **Frame 0 zeigt schon Inhalt** (dient als Vorschaubild, kein leerer Start, kein Schwarzbild), die Kernaussage ist in unter 1,5 Sekunden lesbar.

Danach der Aufbau (für 15–30 s, kürzer = weniger Szenen; bei 6 s nur Hook und Schlusskarte):

1. **Hook** (0–3 s)
2. **Versprechen / Prämisse** — worum es geht, was man bekommt (ein Satz, Hero-Visual im Bild)
3. **1–3 Beweis- oder Neugier-Szenen** — Zitat, Bewertung, Zahl, „wie X, nur …", Blick hinein (Innenseiten, Screenshots, Details). Jede Szene hat einen visuellen „Punch" (Stempel, Sticker, Zähler, Sterne, die nacheinander aufploppen).
4. **Schlusskarte** — Hero-Visual groß, Name, Absender, Variante/Preis falls erlaubt und angegeben, eine klare Handlungsaufforderung, die den Plattformregeln aus Schritt 0 entspricht. Mindestens 2 Sekunden stehen lassen.

**Gleicher Body, nur der Hook wechselt:** Baue das Video so, dass zwei Hook-Varianten denselben Rest teilen. Dann zeigt ein A/B-Test sauber, welcher Hook besser zieht.

### Schritt 2 — Skript-Regeln

- **Headlines:** max. 2 Zeilen, kurze Zeilen (bei großer Schrift ca. 15–18 Zeichen pro Zeile). Lieber ein kürzeres Wort als drei Zeilen.
- **Ein Gedanke pro Szene.** Jede Szene muss ca. 1,5–2 Sekunden ruhig lesbar sein, bevor sie wechselt.
- **Voice-over (falls gewünscht):** Wortbudget ca. 2,5 Wörter pro Sekunde abzüglich Übergängen — bei 30 s also höchstens ca. 65–70 Wörter, bei 15 s ca. 30. Zahlen im Sprechtext als Wörter ausschreiben („zweihundertzwölf"), sonst liest die KI-Stimme sie falsch. Ist der Text zu lang: kürzen, nicht die Sprechgeschwindigkeit hochdrehen.
- **Keine Spoiler, keine Wettbewerber-Namen ohne Freigabe**, nichts aus „Was auf keinen Fall ins Video soll".

### Schritt 3 — PAUSE: Freigabe

Zeig mir vor dem Bauen eine kompakte Tabelle: Szene · Dauer · Bildschirmtext · Voice-over · Grafik-Element · Quelle der Aussage. Dazu die drei Hook-Ideen mit deiner Empfehlung. **Warte auf meine Freigabe**, bevor du Audio erzeugst (kostet Credits) oder renderst.

### Schritt 4 — Bauen (Remotion)

- Projekt mit `bun` anlegen (nicht npm), in einem eigenen leeren Ordner außerhalb von Text- oder Dokumentrepos (`node_modules` und Renderdateien sind groß). Remotion in aktueller stabiler Version, Versionen pinnen.
- **Animation nur über `useCurrentFrame()` + `interpolate`/`spring` mit `extrapolateLeft/Right: "clamp"`.** CSS-`transition`/`animation` funktionieren in Remotion nicht, weil Frame für Frame gerendert wird.
- **Eine Bühne, mehrere Formate:** Layoute alle Szenen in einer festen Bühne und skaliere sie pro Format in die sichere Zone. Keine Pixel-Korrekturen pro Format von Hand.
- **Sichere Zone:** Text und Hero-Visual mit genug Abstand zum Rand (mindestens ca. 5–6 % rundherum, bei 9:16 deutlich mehr oben und unten, weil dort Plattform-UI liegt). Nichts Wichtiges darf angeschnitten werden.
- **Typografie:** Kinetic Type — Wörter einzeln per Masken-Reveal einblenden, Schlüsselwörter in Akzentfarbe mit gezeichneter Unterstreichung. Markiere Highlights im Skript pro Wort (`*Wort*`), nie über mehrere Wörter, sonst landet ein Sternchen im Video.
- **Farben aus dem Hero-Visual ableiten** (falls keine Markenfarben angegeben): eine Hintergrundfarbe, eine Textfarbe, **eine** Akzentfarbe. Die Akzentfarbe als Fläche nur einmal (z. B. für den Button auf der Schlusskarte), sonst nur für Text und Konturen.
- **Rhythmus:** harte Schnitte unter einem kurzen Wipe (schräge Farbflächen, die genau im Schnitt-Frame voll decken), dezente Hintergrundbewegung (treibende Formen, Partikel, eine Textur passend zum Angebot: Papier für ein Buch, Raster für Software, Stoff oder Holz für ein Produkt), ein kleiner Fortschrittsbalken oder Zähler hält Leute bis zum Ende.
- **Sound (falls Ton gewünscht):** Musikbett leise (ca. 15–20 % Lautstärke) mit Fade-in/-out; SFX für Wipes (Whoosh), Einblendungen (Pop), Punches (Impact/Stempel), passende Geräusche zum Angebot (Seitenumblättern, Klick, Verschluss). Voice-over pro Szene als eigener Clip, Stille am Anfang und Ende per ffmpeg trimmen, **Szenenlänge = gemessene Sprechdauer + kurzer Puffer**. Bei ElevenLabs: max. 4 Anfragen parallel, mit Retry.
- **Kein Schwarzbild** am Anfang oder Ende.

### Schritt 5 — Vorschau und Selbstkontrolle

- Rendere zuerst eine **Vorschau in halber Auflösung** (geht schnell).
- Zieh per ffmpeg ca. 24 gleichmäßig verteilte Frames als **Kontaktbogen** (ein PNG-Raster mit Frame-Nummern) und lege ein halbtransparentes **rotes Overlay über die unsichere Randzone**. Schau dir jeden Bogen selbst an und prüfe:
  - [ ] Nichts Wichtiges im roten Bereich, nichts angeschnitten
  - [ ] Kein Text läuft über Kanten oder in andere Elemente
  - [ ] Keine sichtbaren Sternchen oder Steuerzeichen, Unterstreichungen erscheinen erst mit ihrem Wort
  - [ ] Frame 0 zeigt Inhalt, Hook in < 1,5 s lesbar
  - [ ] Hero-Visual groß und scharf, Name lesbar
  - [ ] Jede Zahl/jede Bewertung hat eine Quelle und steht so in Teil A
  - [ ] Akzentfarbe als Fläche nur einmal
  - [ ] Ohne Ton verständlich
- Fehler fixen, neu prüfen. Erst wenn alles grün ist: **zeig mir die Vorschau** und warte auf mein OK.

### Schritt 6 — Finaler Render

- Volle Auflösung, H.264, 30 fps (oder was die Plattform verlangt), AAC 48 kHz.
- Ton per ffmpeg auf ca. −14 LUFS normalisieren (Bildspur per Stream-Copy übernehmen), falls die Plattform nichts anderes vorgibt.
- Prüfe mit `ffprobe`: Auflösung, Länge, Bildrate, Dateigröße innerhalb der Plattformgrenzen. Melde die Werte.

### Ergebnis

- `export/<name>-<hook>-<format>.mp4` — je Hook-Variante und Format eine Datei.
- `README.md` mit: Hook-Varianten und welche du empfiehlst, Quellen jeder Aussage im Video, Plattformregeln aus Schritt 0 mit Link und offenen Punkten, Vorschlag für Anzeigen-Headline und Begleittext (im Rahmen der Zeichengrenzen der Plattform), was ich selbst noch prüfen muss.
- Du lädst nichts hoch. Das mache ich selbst.
