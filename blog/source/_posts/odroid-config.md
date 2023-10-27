---
title: "Retro-Spiele Emulator mit ODroid und RecalBox"
date: 2023-10-03
author: Tom
categories:
- ["media"]
- ["electronics"]
tags:
---
# Odroid mit Recalbox

Auf meinem ODroid XU4 läuft Recalbox, eine Linux Distro mit eingebautem GUI und allen möglichen Emulatoren und so weiter:
https://www.recalbox.com/

Das scheint aktuell neben RetroPie die State-of-the-Art-Lösung für Emulations-Frontends zu sein. Bei RecalBox ist gegenüber RetroPie angeblich der Vorteil, dass angeschlossene Controller besser erkannt werden. Das ist praktisch, wenn man mal dieses und mal jenes Gamepad anschließen möchte.

Eine Installationsanleitung findet man hier:
https://wiki.recalbox.com/de/basic-usage/preparation-and-installation

## Wie kann man Spiele hinzfügen?
Die SD-Karte in ein anderes System zu stecken, um Datein hinzuzufügen, das bringt nichts. Von der 32GB-SD-Karte sieht man dann nur die ca. 3GB große Boot-Partition.
Das liegt an dem zugrundeliegenden Batocera Linux, da ist die eigentliche Batocera-Partition in einem speziellen Format. Man kann nur ROMs hinzufügen wenn das Batocera-System hochgefahren ist. Dann entweder durch Anstecken eines USB-Sticks mit den ROMs oder über Netzwerk Share.

Über Netzwerk kann man ROMs auf den Share "RECALBOX" in den passenden Ordner kopieren. Allerdings haben die Spiele dann keine Bilder.

## ROM Manager
Es gibt für die Emulatoren-Config bei Recalbox wohl eine gamelist.txt, da muss man Sachen eintragen, damit die Spiele im Auswahlmenü hübsch aussehen. Das macht von Hand keinen Spaß. Daher empfiehlt sich, eins der extra dafür vorgesehenen ROM Manager zu nutzen:
* Skraper - https://www.skraper.net
* ARRM - http://jujuvincebros.fr/hard-soft/arrm-gamelist-roms-manager-scraper

Die lesen die Daten von folgenden Spieledatenbanken ab:
* Screen Scraper - https://www.screenscraper.fr
* TheGamesDB - https://thegamesdb.net

Außerdem hat Recalbox einen eingebauten Scraper, der neue ROMs feststellen kann und dann die passenden Beschreibungen raussucht. Dieser eingebaute Scraper funktioniert bei mir leider nicht.

Ein Nachteil beim ODroid ist, dass der Lüfter ganzschön Lärm machen kann, wenn Last auf dem System ist.

