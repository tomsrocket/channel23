---
title: "Ein Arcade-Spielautomat für zu Hause"
date: 2023-10-10
author: Tom
categories:
- ["media"]
- ["electronics"]
tags:
---

![Retro Arcade Automat im Wohnzimmer](/images/bartop-arcade.jpg)

Ich wollte schon immer einen Spielautomaten zu Hause haben und habe mir daher in den 2000ern für günstig zwei kaputte TV-Ideal Arcade-Gehäuse gekauft. Bei beiden war der Monitor kaputt, ansonsten war alles intakt, original Spielplatinen und Jamma-Einsteck-Adapter inklusive. Ich hab dann einen PC und einen alten Röhrenmonitor eingebaut, das sah dann ungefähr so aus:
https://next-level.fun/die-wiederauferstehung-des-tv-ideal/

Eins der Gehäuse habe ich heute noch, inzwischen mit Flachbildschirm statt Röhre, und den alten PC durch einen Raspberry Pi 4 ersetzt. Dieser Blogartikel soll der Dokumentation der Hard- und Softwarekomponenten dienen.

<!-- more -->

## Eckdaten des Gehäuses

Allgemeine Infos:
* Gehäuse-Bezeichnung "TV-Ideal"
* Astausch-Monitor
  * 22 Zoll (55,88 cm) 16:10
  * Nicht optimal: Das Bild des Monitors ist breiter als die Aussparung der Frontscheibe. Aber die Bildschirm-Höhe passt, daher für Spiele im 4:3-Format ganz OK.
* Adapter zum Anschluss der Joysticks & Buttons:
  * IPAC mit PS/2 Anschluss
  * *Aktiver* PS/2 auf USB Adapter
    * Es gibt auch passive PS2-USB-Adapter, die funktionieren in diesem Fall nicht.
    * Die 2019er RetroPie-Version hatte das Problem: Nach einer Weile der Nichtbenutzung (vmlt. Energiesparmodus?) wurde das Keyboard, also die Controller nicht mehr erkannt. Scheint in RetroPie 4.8 behoben zu sein. Die Menüeinstellung für Energiesparmodus ist allerdings auch abgeschaltet.

Buttons pro Spieler:
* 4-Wege-Joystick
* 3 Buttons ("Aktion I" - "Aktion III")
* Start Knopf
* Coin Button (Gehäuseseite)

Und noch 1x Extra Button an der rechten Gehäuseseite weiter hinten. Die Coin- und Reset-Buttons an der Gehäuseseite habe ich selbst eingebaut, die sind nicht original.

# Controller bzw. Tatatur konfigurieren

## I-PAC 2 Legacy Version (PS/2 Anschluss)

Standard-Tastaturbelegung des IPAC:
(Das entspricht auch meiner Belegung)

```bash
 	KEY         CODE 	MIT SHIFT       Tom's Gehäuse Mapping
                        (hold 1P
                        start)
    COIN 1 	    5                       Button Gehäuse links
    COIN 2 	    6                       Bt. Geh.rechts vorne
    START 1 	1                       1P Start
    START 2 	2 	    ESC             2P Start

    # Player 1
    1 RIGHT 	R arr.  Tab             1P RIGHT
    1 LEFT 	    L arr.  Enter           1P LEFT
    1 UP 	    U arr. 	Key Below ESC   1P UP
    1 DOWN 	    D arr. 	P (pause)       1P DOWN
    1 SW 1 	    L-ctrl 	5 (Coin A)      1P Aktion I
    1 SW 2 	    L-alt                   1P Aktion II
    1 SW 3 	    space                   1P Aktion III
    1 SW 4 	    L-shift
    1 SW 5 	    Z
    1 SW 6 	    X
    1 SW 7 	    C
    1 SW 8 	    V                       Bt. Geh.rechts hinten
    1 A 	    P
    1 B 	    ENTER

    # Player 2
    2 RIGHT 	G                       2P RIGHT
    2 LEFT 	    D                       2P LEFT
    2 UP 	    R                       2P UP
    2 DOWN 	    F                       2P DOWN
    2 SW 1 	    A                       2P Aktion I
    2 SW 2 	    S                       2P Aktion II
    2 SW 3 	    Q                       2P Aktion III
    2 SW 4 	    W
    2 SW 5 	    I
    2 SW 6 	    K
    2 SW 7 	    J
    2 SW 8 	    L
    2 A 	    TAB
    2 B 	    ESC
```
(Quelle: https://www.arcadeworlduk.com/pages/IPAC-2-Code-Table.html)

## Passende Retropie Keyboard Config

Muss in diese Datei eingetragen werden: `\\RETROPIE\configs\all\retroarch.cfg`
```yaml
input_player1_a = "ctrl"
input_player1_b = "alt"
input_player1_x = "space"
input_player1_start = "num1"
input_player1_select = "num5"
input_player1_r = "w"
input_player1_left = "left"
input_player1_right = "right"
input_player1_up = "up"
input_player1_down = "down"
input_player1_y = "down"
input_player1_l = "up"

input_player2_a = "a"
input_player2_b = "s"
input_player2_x = "q"
input_player2_start = "num2"
input_player2_select = "num6"
input_player2_r = "w"
input_player2_left = "d"
input_player2_right = "g"
input_player2_up = "r"
input_player2_down = "f"
input_player2_y = "down"
input_player2_l = "up"
```

# Retropie Einstellungen

Die Config-Dateien liegen unter:
 * `/opt/retropie/configs/all` - wenn man die SD Karte in den Rechner steckt
 * `\\RETROPIE\configs\all\` - über Netzwerk-Share

## Bios Dateien

Im Gegensatz zu Recalbox hat Retropie keinen Menüpunkt, mit dem man fehlende Bios-Dateien auflisten kann. Daher stochert man da ziemlich im dunkeln.

## Audio Ausgabe konfigurieren
Der HDMI-Ausgang ist standardmäßig aktiv. Wenn man statt dessen den Klinkenausgang nutzen möchte, dann:
* (*Nicht* in Emulationstation auf "Sound Settings" gehen, das hilft nicht)
* Im Hauptmenü wo man Emulatoren auswählen kann
* **Retropie** öffnen
* **Audio** auswählen
* "Headphones"
* Es gibt noch eine Einstellung unter **raspi-config**
* Dann klappt's

## Weitere Emulatoren installieren

Immer erst den Emulator installieren wie im Folgenden beschrieben, dann wird das entsprechende roms-Verzeichnis angelegt. Danach erst die Roms reinkopieren.

**Schritte zur Installation:**
* Retopie-Hauptmenü öffnen
* **Retropie-Setup**
* "Manage Packages"
* "Manage Optional Packages"
* Eine Liste wird angezeigt
  * Die roten sind nicht für die aktuelle Plattform (RaspberryPi) verfügbar
  * Namen, die mit "**lr-**" starten, basieren auf Libretro (RetroArch). Wenn beides zur Auswahl steht, dann im Internet gucken, welcher besser ist (s.u.)
* Emulator auswählen
* "Install from binary"

**Konkrete Emulatoren nachinstallieren:**
* C64
  * C64-Emulator "Vice" z.B. gibts als `lr-vice` und als `vice`.  Der lr-vice hat das bessere Interface für Betrieb ohne angeschlossene Tastatur ("keyboardless"), weil er so eine praktische Tastatureinblendung auf "Coin 1" (Button am Gehäuse links) hat.
* Amiga
  * Es gibt mehrere zur Auswahl.. Ich habe mal Amiberry genommen, weil der angeblich für Arcade Gehäuse am besten ist. Alle Infos unter: https://retropie.org.uk/docs/Amiga/ - aber ich bin damit nicht sehr weit gekommen. Erst liefen die Roms nicht (nur schwarzer Bildschirm), dann mussten die Joysticks neu konfiguriert werden.. Das war Grund für mich, auf eine vorkonfigurierte Distribution zu wechseln.

## Sonstige EmulationStation Einstellungen
* Game List Settings -> Automatic Game Lists
  * Favorites
  * Last Played
* Damit beim Starten von Spielen das graue Fenster nicht erscheint ("Runcommand")
  * Retropie -> Run Command Configuration

