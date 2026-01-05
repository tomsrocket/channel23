---
title: "Linux auf einem Datenträger mit weniger als 8GB Speicher installieren"
date: 2026-01-02
author: Tom
categories:
- ["*nix"]
tags:
---

Es gibt einige Linux-Distributionen, die sind besonders für alte Computer mit wenig Rechenpower geeignet.
Eine der beliebtesten ist wohl Lubuntu, da dessen neue Desktopumgebung sehr performant und trotzdem ressourcenschonend ist. Die Mindestanforderung für eune Lubuntu-Installation ist allerdings 8GB Festplattenplatz. 

Wenn man wie ich eine Festplatte mit nur 7,2GB fest seinem Mini-PC verbaut hat, was tut man dann? Es fehlen nur 800MB! Das muss doch trotzdem gehen. 
..denkt man sich, aber wenn man den Lubuntu-Installer startet, bricht der sofort im zweiten Schritt ab, mit der Meldung "mindestens 8GB Festplatte erforderlich". 

Es gibt aber einen Trick. Zumindest aktuell, Stand Anfang 2026: Das Installationsprogramm von Lubuntu heißt "Calamares" und man kann die Configdateien davon bearbeiten. Dabei kann man einstellen, dass die Installationsvoraussetzung nicht 8GB Plattenplatz, sondern z.B. nur 6GB ist.

<!-- more -->

Schritt 1: Das Lubuntu System vom USB-Stick booten 
* Auf einem Beliebigen Rechner einen Bootfähigen Lubuntu USB Stick erstellen. Unter Ubuntu kann man dafür das Tool "USB-Abbildersteller" über das Startmenü nutzen. Die benötigte Lubuntu Iso kann man hier Downloaden: https://lubuntu.me/downloads/
* Dann den USB-Stick in den Ziel-Rechner stecken, also den Computer, der zu wenig Speicher hat.
* Falls der Rechner nicht direkt vom Stick bootet, dann erst das Bootmenü aktivieren (Bei einem IGEL-PC: *Entf*-Taste beim Boot drücken).
* Vom Lubuntu-USB-Stick booten und dann in der textbasierten Abfrage "Try or install Lubuntu" auswählen. 
* Lubuntu startet sich. Dann die Sprache auswählen, mit dem WLAN verbinden (optional) und "Tru Lubuntu" auswählen. 

Schritt 2: Installer modifizieren 

* Nachdem man im Desktop des Lubuntu-Systems gelandet ist, muss man folgendes ausführen: 
* Die Datei `/etc/calamares/modules/welcome.conf` (Pfad ggf. ähnlich) mit einem Texteditor öffnen. 
* In der Welcome.Conf-Datei steht in einer der ersten Zeilen sowas wie `space required: 8`. Die Ziffer nach belieben reduzieren, z.B. auf 6.
* Danach den Installer durch Klick auf das Desktop Icon starten. Nun schlägt der Speicher Check nicht mehr fehl und die Installation läuft weiter.
* Bei der Abfrage zum Installations-Umfang dann natürlich nicht "Full installation" wählen, sondern unbedingt das **minimale** System.
* Auch die Swap-Datei und das automatische Installieren von Updates nach der Installation sollte man erstmal deaktivieren, sonst bricht der Installer später ab mit Speicherplatz-Fehler.
* Der Install sollte nun erfolgreich durch laufen und man kann das System anschließend von der Festplatte booten.

## Nach der Lubuntu-Minimal-Installation weitere Software nachinstallieren

Wenn man sich nun denkt "Ich kann ja alles weitere ganz easy mit `apt` installieren".. Ja, das stimmt, aber bitte mit Vorsicht:

Wenn nur wenig, also unter 1 GB an freiem Festplattenplatz zur Verfügung steht, ist die Installation weiterer Software, z.B. eines Webbrowsers wie Firefox oder Chromium, leider sehr "gefährlich". Nutzt man z.B. `sudo apt install firefox` um Firefox zu installieren, dann steht zwar in der darauffolgenden Übersicht, dass nur 150 MB heruntergeladen, und zuätzliche 200 MB verbraucht werden.

Diese Info von `apt`  ist aber leider komplett gelogen, denn während der Installation werden weit über 1 GB an Paketen heruntergeladen und verbleiben auch auf der Festplatte. Das liegt anscheinend daran, dass es sich bei Chromium und Firefox derzeit um *Snap*-Pakete handelt, für die erst `snapd` installiert wird, und das wiederum installiert (zumindest bei meinem Mini-PC) mesa-Treiber, gnome- und core-Pakete, die teils 400-800 MB groß sind. 

**Achtung bei snap Paketen**\
Daher der Tipp: Sobald bei einem `apt install` Befehl in der Liste der zu installierenden Pakete **snapd** steht, sollte man die Installation lieber nicht ausführen. Vor dem Herunterladen bzw dem darauffolgenden Entpacken wird durch Snap anscheinend nicht geprüft, ob genügend Platz auf der Festplatte frei ist, so dass mit kritischen Fehlern abgebrochen wird, sobald der Plattenspeicher voll ist. Das System kann danach irreparabel zerstört sein, da die halb installierten Pakete nicht mehr ohne weiteres gelöscht werden können.

**Pakete lieber als DEB installieren**\
Viele Pakete kann man stattdessen als DEB Pakete installieren. Dann belegen sie *wirklich* nur wenige Megabytes. Die ".deb"-Dateien kann man entweder direkt von den jeweiligen Webseiten herunterladen, oder man kann zusätzliche Softwarequellen hinzufügen und die gewünschte Software per APT installieren, dann erhält man auch regelmäßige Updates. 
Wie das z.B. für **Firefox** geht, steht hier beschrieben: https://www.omgubuntu.co.uk/2022/04/how-to-install-firefox-deb-apt-ubuntu-22-04

## Vorsicht bei Paket-Updates
Die Updates aller Pakete über das Softwarecenter oder mit `sudo apt update && sudo apt upgrade` sollte man vorsichtig ausführen. Ich habe mir dabei einigen Ärger eingehandelt, weil währenddessen die Festplatte voll wurde.

## Befehle um Festplattenplatz aufzuräumen

Apt
```bash
# Auflisten aller apt Pakete und deren Größe
dpkg-query -W -f='${Installed-Size;8}  ${Package}\n' | sort -n

sudo apt remove papiros-icon-theme # Einzelne Pakete löschen, z.B.
sudo apt autoremove # unnötige Pakete entfernen (150MB)
sudo apt clean # Apt Cache leeren (800MB)
```

Snap
```bash
# Auflisten aller snap Pakete und deren Größe
du -hcs /var/lib/snapd/snaps/* 

# Snap Paket deinstalliern
sudo snap remove gtk-common-themes 

# Nach dem entfernen der Snap Pakete den Speicher freigeben
rm -rf /var/lib/snapd/cache/*
sudo apt purge snapd
```

## Automatisch Internetbrowser beim Systemstart im Vollbild öffnen

Ich möchte den Computer nutzen, um nach dem Start automatisch ein Dashboard auf einem per HDMI angeschlossenen Bildschirm anzuzeigen. Bei dem Dashboard handelt es sich um eine Internetseite, die verschiedene Daten zusammenträgt und darstellt, z.B. Wettervorhersage, Stundpläne, TODO-Listen, etc. (Quellcode hier: https://github.com/tomsrocket/family-dashboard )

Das System soll also direkt in den Firefox booten. Das geht so: 

Datei im Homeverzeichnis erstellen: `startup.sh`
```
#!/bin/bash 

# Warte auf WLAN
sleep 5
sleep 5

# Öffne Browser im Vollbild
firefox -kiosk https://webseite.tld/seitenurl
```

Dann die Datei mit `chmod 755 startup.sh` ausführbar machen.

Damit sie nach dem Start automatisch ausgeführt wird, kann man sie über den Einstellungen-Dialog von Linux in der Autostart-Liste hinterlegen.

Bei Lubuntu ist das hier: `Einstellungen` -> `LXQt-Systemeinstellungen` -> `Sitzungskonfiguration` -> `Autostart`

Bei Ubuntu geht es stattdessen über die Programm-Suche der Taskleiste und dann eingeben: `Startprogramme`

Über die `hinzufügen`-Funktion die neu erstellte Shell-Datei `startup.sh` auswählen und einen Namen vergeben, fertig! Beim Neustart öffnet der Computer dann immer automatisch die Internetseite im Firefox Browser.
