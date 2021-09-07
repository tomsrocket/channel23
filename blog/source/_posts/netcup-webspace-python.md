---
title: "Python auf Netcup Webspace"
date: 2021-09-07
author: Tom
categories:
- ["coding"]

---

Auf Netcup ab "Webhosting 4000" kann man Python Anwendungen laufen lassen.
Wie das funktioniert ist aber leider bei Netcup nicht so gut dokumentiert (Stand 09/2021).

**Funktionsweise**
Im Prinzip ist es so, dass man die benötigten Python-Pakete auf seinem lokalen System per Virtual Environment erzeugen und dann aus dem "venv"-Ordner auf den Server hochladen muss.
Daher sollte man erst herausfinden welche Python-Version auf netcup läuft. Das steht im Customer-Service-Center. Bei mir war das Python 3.5.3. Wenn man nämlich mit einer anderen Python Version (z.B. 3.8) erstellte Pakete hochlädt, dann bekommt man mit hoher Wahrscheinlichkeit Syntax errors.

Der Rest funktioniert auf dem Sesrver über phusion passenger und man kann dann sogar Python-Anwendungen zum laufen bringen, die das Web-Framework "django" benötigen .. sofern sie keine aktuelle Django-Version nutzen. Ab der bereits recht alten Version "Django 3.0" braucht man Pyhton 3.6. Das vom Server unterstützte, quasi ur-alte Python 3.5 war für unser Projekt leider der Showstopper.
Falls man mit Python 3.5 zufrieden ist, dann folgt eine Anleitung, wie man es auf Netcup Webhosting ab 4000 ans Laufen bekommt.

<!-- more -->

## Vorbereitung des Servers
Eine sehr gute Anleitung findet man unter:
https://saschaszott.github.io/2021/02/14/netcup-python-webhosting.html

Dort fehlt nur das Detail mit der alten Python Version, was ich im Folgenden beschreibe.

Man sollte also zunächst so vorgehen wie in der ^ verlinkten Doku von Sascha Szott gezeigt.
Das funktioniert nicht nur für flask, sondern auch für andere Python web frameworks wie django.
Dazu muss man nur entsprechend eine andere "passenger_wsgi.py" anlegen. Beispieldateien findet man auf phusionpassenger.com. Für Django z.B. ist es hier beschrieben: https://www.phusionpassenger.com/library/deploy/wsgi_spec.html

# Lokale Installation der Pakete
Lokal zunächst die gleiche Python Version installieren wie auf dem Netcup Webspace.
Hier steht, wie man Python 3.5 so installieren kann, dass nicht die Standardinstalltion von Python kaputt macht, sondern so dass Python3.5 zusätzlich mit dem Befehl "python3.5" nutzbar ist: https://tecadmin.net/install-python-3-5-on-ubuntu/

Dann kann man die von der gewünschten Anwendung benötigten Python-Pakete lokal installieren:

```bash
  # Venv mit python 3.5 erstellen
  python3.5 -m venv venv
  source venv/bin/activate # Virtual environment starten

  pip --version # checke die pip version. Müsste 3.5 sein.
  pip install -r requirements.txt
  deactiavte # Virtual environment wieder verlassen
```

Die requirements.txt sollte die benötigen Abhängigkeiten enthalten.

Nun muss man nur noch die Paket-Verzeichnisse aus dem lokalen venv-Ordner auf den Server SCPen und dann läuft das:

```bash
  # Dann kann man die benötigten Pakete hochladen, z.B. mit:
  scp -r flask itsdangerous jinja2 markupsafe werkzeug user@server.tld:/flask-app
```
