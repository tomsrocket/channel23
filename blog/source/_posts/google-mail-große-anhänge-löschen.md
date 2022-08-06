---
title: "Google Konto Speicherplatz aufräumen - Große Gmail Mails löschen"
date: 2022-07-28
author: Tom
categories:
- ["allgemein"]
tags:
- ["spam"]
---

Wenn man ein Google (Mail-)Konto einige Jahre lang verwendet, dann ist es unweigerlich irgendwann soweit: Der Google Speicherplatz ist voll. Die Speicherplatz-Übersicht ("Google Konto verwalten"->"Speicher") zeigt es schnell: Das sind nicht nur Fotos und der Google Drive Speicherplatz, sondern auch Gmail belegt sehr viel Platz.

Mein Googlemail Postfach z.B. belegt in etwa 7GB. Da sind sicherlich sehr viele Emails drin, aber Emails allein, d.h. Text und (auf Mailversand optimierte) Bilder -- selbst wenn es sehr sehr viele sind -- belegen so schnell keine 7GB. Da sind ganz bestimmt viele große Attachments dabei, die ich nicht mehr benötige.
Zumal ich eigentlich alle Attachments, die wichtig sind, eh immer herunterlade.

Also könnte sicher einiges an Speicher gespart werden durch löschen alter Mails mit großen Anhängen. Außerdem, wer guckt nochmal in Mails, die älter als 10 Jahre sind.
Zur Sicherheit kann man ja vorher ein Backup anlegen.

## Schritt 1: Backup aller Emails

Gut, dass man seine gesamten Google-Emails herunterladen kann. Wie das geht, steht hier:
https://www.theverge.com/21324801/gmail-download-data-back-up-save-email

Ab damit auf eine Backup-Festplatte im Schrank. Danach kann man dann Attachments in Gmail löschen, und SOLLTE doch was wichtiges dabei gewesen sein, dann hab ich ein lokales Backup der Mails auf der Festplatte im Schrank.

Wie man an einzelne Mails und Dateien aus der MBOX-Backupdatei wieder herankommt (mit Thunderbird) wird z.B. hier beschrieben:
https://www.howtogeek.com/709718/how-to-open-an-mbox-file-in-mozilla-thunderbird/

## Schritt 2: Große, alte Mails löschen
Die Suchfunktion von Googlemail kann so einiges. Man kann über das "Regler"-Symbol am rechten Rand des Suchfeldes die "Suchoptionen anzeigen"-Funktion öffnen, mit der man sehr spezielle Suchfilter durchführen kann.

Das gleiche geht aber auch durch Eingeben bestimmter Begriffe in das Suchfeld:

1. Mails finden mit großen Attachments
    ```
    has:attachment larger:10M
    ```

2. Alte Mails finden (bis 31.12.2014)
    ```
    before:2015/01/01
    ```

Zusammen ergibt das:

```
has:attachment larger:1M before:2015/01/01
```

Ab damit ins Suchfeld, Suche ausführen und schon werden die Treffen angezeigt. Man kann sich durchklicken und kontrollieren, ob das soweit passt.

Mit dem Kästchen "Auswählen" oben links kann man die ersten 50 angezeigten Mails nun auswählen. Wir wollen aber nicht nur 50, sondern alle löschen.

Damit alle gefundenen Mails ausgewählt werden, klicken auf *"Alle Konversationen auswählen, die mit dieser Suche übereinstimmen"*.

Nun auf das Mülleimer-Symbol klicken und die Cloud wird von (m)einer Datenlast befreit. Ist auch gut für's Klima, weil im Endeffekt weniger Festplatten in der Cloud laufen müssen.

