---
title: Wie schreibt man gute Prompts für KI-Bildgeneratoren?
date: 2023-05-14
author: Tom
categories:
- ["open"]
---

Ich habe das Gefühl, Input-Texte für KI-Bildgeneratoren zu schreiben ist ähnliche Magie wie Suchmaschinenoptimierung..
Hier ein paar Tipps aus dem Internet, um etwas Struktur in KI-Prompts zu bekommen. Folgendes empfiehlt der NightCafe-Newsletter:

Baue den Prompt folgendermaßen auf:

1. Hauptinhalt
2. Zweites Thema
3. Nennung von Künstlernamen / Stil-Beschreibung
4. Fotografische Details bzw. künstlerische Anregungen
5. Spezifische Farben (optional)

Beispiel:
```
A cow passing through (main subject)
an abandoned atztec city (secondary subject),
by Samuel Palmer and Gustave Dore  (artist names / styles),
8k resolution, a masterpiece, 35mm, hyperrealistic, hyper maximalist (photography/artistic prompts),
crimson, pink (colors).
```

Prompt-Beispiele inklusive visuelle Vorschau der generierten Styles gibt es hier:
* https://github.com/Dalabad/stable-diffusion-prompt-templates

## Weitere Tipps für KI-Prompts
* Die Reihenfolge im Prompt spielt eine Rolle, daher das Hauptthema bzw. wichtigste Schlagworte an erste Stelle setzen.
* Beschreibende Adjektive einbauen. Vermeiden, dass die Eingabeaufforderung mit widersprüchlichen Wörtern überfüllt wird.
* Ein Trick ist manchmal, Wörter oder Details mehrmals zu wiederholen, wie z.B. Feuer, Rauch, beleuchtet usw.
* Statt nur "Colorful" zu nennen, kann man eine bestimmten Farbpalette aufzählen: "Colorful, mostly reds, purples, blues and black".

Bereich "Photography"
* Bestimmte Begriffe wirken als Modifikatoren, z.B. „Bokeh“ sorgt für Tiefe und „Panorama“ ist wie ein Weitwinkelobjektiv.
* Da funktioniert auch "telephoto", "fisheye lens" oder "time-lapse".
* Wenn eine Kreation zu "verrauscht" ist, sorgen "cel-shaded" oder "polished" mit einer geringen Gewichtung für eine gute Bereinigung

Thema "Negative prompt"
* Einige Bildgeneratoren bieten die Möglichkeit, "negative prompts" anzugeben, also Stichworte die nicht auf das Bild zutreffen sollen.
Sowas kann man z.B. nutzen, falls Figuren deformiert sind.
Beispiel:
    ```
    Negative prompt: Ugly, Morbid, Extra fingers, Poorly drawn hands, Mutation, Blurry, Extra limbs, Gross proportions, Missing arms, Mutated hands, Long neck, Duplicate, Mutilated, Mutilated hands, Poorly drawn face, Deformed, Bad anatomy, Cloned face, Malformed limbs, Missing legs, Too many fingers
    ```

Trotzdem macht die KI nie so wirklich das was ich will.. 😄