---
title: "Retro-Spiele-Konsole selbstgemacht"
date: 2023-10-03
author: Tom
categories:
- ["media"]
- ["electronics"]
tags:
---

# Retro-Games sind in!

Vor ein paar Jahren kam der Trend auf, alte Spielkonsolen (wie z.B. die erste Playstation oder das Super Nintento) als Mini-Spielkonsolen mit ein paar eingebauten Spielen wieder auferstehen zu lassen und zu Preisen ab 100€ zu verkaufen.

Derzeit gibt's anscheinend noch einen neuen Trend: USB-Sticks aus China mit vertrauenerweckenden Namen wie "4k Game Stick" oder "Retro Konsole Spielkonsole Plug and Play". Was man da bekommt ist: "Game Stick mit 2 Gamepad, 40000+ Spielen, 40+ Emulatoren, 4K HDMI Output, Englische Version, Drahtlose Videospielkonsole für TV Computer Projektor".

Vierzigtausend Spiele für 70€? Die Amazon-Bewertungen geben 3,4 Sterne, das ist nicht wirklich gut, aber auch nicht komplett schlecht. Der USB-Stick wird wohl schnell heiß, stürzt gern mal ab und die Joysticks sind schlecht. Für den Preis ist das wohl auch nicht anders machbar.

Aber das Geld kann man sich sparen! Wer noch einen Raspberry Pi und alte Gamepads oder Joysticks herumfliegen hat, kann sich sowas auch selbst installieren.

## Hardware-Auswahl

Ich habe z.B. einen ODroid und einen Raspberry 4, die gerade nicht verwendet werden.

Der ODroid ist ein kleiner System-on-a-Chip "SoC"-Einplatinencomputer ähnlich dem Raspberry Pi.

Die Version "ODroid XU4" kann neben MicroSD-Karten auch embedded Multi-Media Cards (eMMC) verwenden, die etwas schneller sind. Die eMMC-Karten sind ähnlich klein wie MicroSD-Karten und über einen abgefahrenen Konnektor kann man sie flexibel wechseln.

## ODroid vs. Raspberry Pi
Bei einer Neuanschaffung gibt's inzwischen wohl nur noch wenig Gründe, einen ODroid zu verwenden, zumal der einen Lüfter hat, der zwischendurch nervig sein kann. Ein Raspberry Pi 4 ist eine gleichwertige oder sogar bessere Wahl. Einerseits wegen eingebautem WLAN und Bluetooth und andererseits wegen der weltweiten Verbreitung und der großen Nutzer-Community.

Feature-Vergleich:

| Feature  | ODroidXU4  | RaspberryPi4 |
| -------- | ------- | ------------|
| Bluetooth  | nein    | ja |
| WLAN     | nein  | ja |
| Speicher   | 2GB   | 2GB-8GB |
| Boot | eMMC-Modul oder SD-Karte | SD-Karte |
| Prozessor | SoC Samsung Exynos 5422 | SoC Broadcom BCM2711 Quadcore |
| Kerne | 4 x Cortex-A15 2 GHz, 4 x Cortex-A7 1,5 GHz |  Cortex-A72 (ARM v8) 64 bit 1,5 GHz |
| Video | 1x HDMI 1.4a (1080p) | 2x Micro-HDMI (4K) |
| Audio Ausgang | kein extra Ausgang | Mini-Klinke |


## Auswahl einer Spiele-Emulations-Oberfläche

Der Clou des ganzen ist aber nicht die Hardware, sondern die Software. Es gibt sehr gut Open-Source-Projekte, die vorkonfigurierte Emulatoren und eine hübsche und benutzerfreundliche Oberfläche bieten.

### Spoiler: RecalBox vs. RetroPie?
* 😀 RecalBox "**just works**": Roms reinkopieren, *gamelist.txt* erstellen, fertig. Man muss sich um sonst nichts kümmern, der Rest funktioniert einfach. Und die wichtigen Dinge kann man direkt aus dem Emulationstation-Menü einstellen.

* 😡 RetroPie dagegen ist **super viel Arbeit**, um es vernünftig zu konfigurieren. Es gibt einige Probleme, nachdem man die Roms reinkopiert hat.. Emulatoren laufen nicht, weil Bios-Dateien fehlen, aber man bekommt nicht heraus welche fehlen. Auch ansonsten scheinen die Emulatoren bei RecalBox deutlich besser vorkonfiguriert zu sein. Und die ganzen komfortablen RecalBox-Einstellungen über das Emulationstation-Menü fehlen ebenfalls, statt dessen muss man seitenweise Dokumentations-Wikis wälzen.

<!-- more -->

### Recalbox
Auf meinem ODroid XU4 läuft **Recalbox**, eine All-in-one Retrospiele-Oberfläche mit eingebautem GUI, automatischer Joystick-Erkennung und allen möglichen vorkonfigurierten Emulatoren:
https://www.recalbox.com/

Das scheint aktuell neben **RetroPie** die State-of-the-Art-Lösung für Emulations-Frontends zu sein.

### Unterschiede Recalbox / RetroPie
Bei RecalBox ist gegenüber RetroPie angeblich der Vorteil, dass angeschlossene Controller besser erkannt werden und dass man seltener zur Tastatur greifen muss. Das ist praktisch, wenn man öfter mal unterschiedliche Gamepads anschließen möchte.
RetroPie ist im Gegenzug wohl besser konfigurierbar.

### Lakka
Außerdem gibt es noch "**Lakka**", ein schlankes Frontend basierend auf RetroArch. Das habe ich noch nicht ausprobiert.

### MAME
Die Emulation von Arcade-Spielen via MAME ist wohl bei allen drei oben genannten Varianten nicht optimal, da dort veraltete MAME-Versionen verwendet werden. Bei Lakka besteht zudem das Problem, dass das dort verfolgte Konzept, dass jeder Emulator eine eigene "Core" darstellt, mit MAME nicht so gut harmoniert.
Mehr Infos dazu, wie man MAME auf einem Raspberry Pi einsetzen sollte, findet sich im MAME Subreddit:
https://www.reddit.com/r/MAME/

## Recalbox Einrichtung
Eine Installationsanleitung findet man hier:
https://wiki.recalbox.com/de/basic-usage/preparation-and-installation

Kurzfassung: Die Image-Datei der neusten RecalBox Version herunterladen und mit dem "Raspberry Pi Imager" auf die SD Karte installieren.
Das Image der aktuellen (10/2023) RecalBox "Version 9.1 - Pulstar" gibt's hier: https://www.recalbox.com/de/download/stable/odroid/odroidxu4/alternative/

## Spiele-ROMs

### Wie kann man Spiele hinzfügen?
Die SD-Karte in ein anderes System zu stecken, um Datein hinzuzufügen, das bringt nichts. Von der 32GB-SD-Karte sieht man dann nur die ca. 3GB große Boot-Partition.
Das liegt an dem zugrundeliegenden Batocera Linux, da ist die eigentliche Batocera-Partition in einem speziellen Format. Man kann nur ROMs hinzufügen wenn das Batocera-System hochgefahren ist. Dann entweder durch Anstecken eines USB-Sticks mit den ROMs oder über Netzwerk Share.

Über Netzwerk kann man ROMs auf den Share `\\RECALBOX\` in den passenden Ordner kopieren. Allerdings haben die Spiele dann keine Vorschau-Bilder.

### ROM Manager
Es gibt für die Emulatoren-Config bei Recalbox eine "gamelist.txt"-Datei, da muss man Sachen eintragen, damit die Spiele im Auswahlmenü hübsch aussehen. Das macht von Hand keinen Spaß. Daher empfiehlt sich, einen der extra dafür vorgesehenen ROM Manager zu nutzen:
* Skraper - https://www.skraper.net
* ARRM - http://jujuvincebros.fr/hard-soft/arrm-gamelist-roms-manager-scraper

Diese ROM Manager lesen die Daten von folgenden Spieledatenbanken ab:
* Screen Scraper - https://www.screenscraper.fr
* TheGamesDB - https://thegamesdb.net

Außerdem hat Recalbox einen eingebauten Scraper, der neue ROMs feststellen kann und dann die passenden Beschreibungen raussucht. Dieser eingebaute Scraper funktioniert bei mir leider nicht.

### Wo bekommt man Spiele-ROMs her

So ein China-Gerät mit 40.000 Spielen ist evtl. eine gute Quelle. Ansonsten findet man einiges auf Google. Sehr gute fertig zusammengestellte und vorkonfigurierte Image-Dateien findet man bei Arcadepunks.

## EmulationStation im Einsatz

### Tastenbelegung im Emulator

Wenn man den Controller konfiguriert, dann kann man eine Hotkey-Taste definieren. Sollte man keine freie Taste am Controller mehr übrig haben, wird empfohlenm, den "Select"-Button zu wählen. Mit der Hotkey-Taste kann man während des Spielens folgende Tastenkombinationen nutzen:

    Hotkey + Start = exit emulator
    Hotkey + R1    = save state
    Hotkey + L1    = load saved state
    Hotkey + Left  = decrease current saved state slot number
    Hotkey + Right = increase current saved state slot number
    Hotkey + X     = quick menu (with access to most of these other items)
    Hotkey + B     = reset game

### Joystick Probleme lösen

Joysticks erstmal am PC ausprobieren: https://wiki.ubuntuusers.de/joystick/

```bash
    # jstest installieren
    sudo apt-get install joystick

    # Joystick device rausfinden
    cat /proc/bus/input/devices

    # Joystick ausprobieren
    jstest /dev/input/js0
```

### Joystick Einstellungen in Recalbox resetten
Option 1\
Man kann über das Haupmenü einen Factory-Reset durchführen, dann vergisst das EmulationStation alle Einstellungen (also solche Einstellungen wie: Controller Settings, Overlays ausschalten, Menü-Musik auschalten, 2x bestätigen zum Spiele beenden, ..)

Option 2
* Erst **EmulationStation stoppen, damit es die config Dateien nicht wieder überschreibt** (macht es sonst beim beenden gern mal):
Also auf dem Device: Strg+Alt+F2 drücken für ein Terminalfenster (oder per SSH). Einloggen mit *root / recalboxroot*.
* Dann `es stop` eingeben um EmulationStation zu beenden.
* Nun über's Netzwerk die Config Datei anpassen:
In `\\RECALBOX\share\system\recalbox.conf` die Zeilen `emulationstation.padX=...` löschen.

## Pro-Version: Bartop-Gehäuse

Hier gibt's einen coolen holländischen Shop mit Bausätzen für Tabletop/Bartop Arcade-Gehäusen: https://arcade-expert.nl/Bartop-DHZ-Arcadekast-Bouwpakket
