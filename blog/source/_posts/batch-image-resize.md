---
title: "Alle Fotos und Bilder in eimen Verzeichnis verkleinern"
date: 2020-03-18
author: Tom
categories:
- ["coding"]
tags:
---

**Stichworte: imagemagick convert batch image resize**

Ständig kommt's wieder vor: Von irgendwoher hat man eine Menge 20MB große Fotos, und möchte die gern auf eine Bildergalerie-Webseite ins Internet stellen.
Dazu sollen die Bilddateien aber um ein Zehnfaches kleiner sein.

Das geht mit folgendem Befehl:

```
find . -iname \*.jpg -exec convert -verbose -quality 80 -resize 1600\> "{}" "../resized/{}" \;
```

So geschehen mit den Fotos vom Open Data Day Münster 2020: 
http://codeformuenster.org/opendataday/2020/gallery/
