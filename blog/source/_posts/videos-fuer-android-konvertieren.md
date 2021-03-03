---
title: "Video für Whatsapp / Android konvertieren"
date: 2020-04-18
author: Tom
categories:
- ["*nix"]
tags:
- ["video"]
---

Aufgabe: Wir wollen ein kleines Video für Oma's Geburtstag drehen.
Ziel: Das Ergebnis soll auf dem Handy in Whatsapp funktionieren.

Nach einigen Sessions hatten wir folgendes Ausgangsmaterial: 

* Mit Handy gefilmte kurze Videos: Handy per USB-Kabel an den Rechner anschließen und schon können sie herüberkopiert werden.
* Stopmotion Videos vom IPad: Die IPad Videos kann man bequem über "ICloud" auf den Rechner bekommen: Auf dem IPad in die ICloud speichern, und dann am Rechner über icloud.com herunterladen.

Wie bekommt man die nun zu einem einzigen Videofilm zusammengesetzt?

Ich wollte gern Ubuntu nutzen, und entschied mich für das Videoschnittprogramm "Pitivi", denn es hat nicht so viele Abhängigkeiten und ist leicht über den Standard Ubuntu Softwareinstaller zu installieren.

Eins der Videos war leider kopfüber gefilmt, das liess sich aber relativ einfach um 180° drehen, dazu kann man in Pitivi einen Filter nutzen. Komisch war nur die Drehungs-Einstellung: man muss eine total krumme Kommazahl eingeben, um 180° zu erreichen.

Funktionierte also alles ganz gut, nur ein Problem blieb: Als Ergebnis kommt immer ein MP4 heraus, das auf unseren Android Handys nicht funkionert. Andere Exportformate in Pitivi klappten leider nicht (Diverse Fehlermeldungen auf der Konsole) und ich hatte keine Lust das Setup zu debuggen. 
(Insofern kann ich jetzt auch das Gemecker über Videoschnitt mit Linux verstehen..)

Ich hab dann eine halbe Stunde recherchiert, bis ich endlich eine Möglichkeit fand, das Video so zu konvertieren, dass es in Whatsapp angezeigt wird: 

    ffmpeg -i omi2020.mp4 -vcodec mpeg4 -acodec aac -strict -2 -ac 1 -ar 16000 -r 13 -ab 32000  output4.mp4

Nur so gehts. Allerdings ist das Video danach nur noch 2MB groß und ist so krass komprimiert, dass es echt grottenschlechte Qualität hat..!
Beim nächsten mal muss ich das Videoqualitätsproblem noch lösen.
