---
title: "Internetradio mit Fritzbox Mediaserver einrichten"
date: 2022-01-02
author: Tom
categories:
- ["music"]
tags:
- ["party"]
---

![Denon CEOL Piccolo - wenn's mal wieder länger dauert](/images/denon-musikanlage-ceol-piccolo.jpg)

Wir besitzen ein DENON CEOL Piccolo ("N4") Wireless-Musiksystem mit WLAN und Bluetooth. Diese praktische Musikanlage steht bei uns in der Küche und wir nutzen sie schon lange, um Internetradio-Streams damit zu hören. Die Hardware ist top: Das Gerät ist hübsch, klein, weiß und hat guten Sound.

Aaaaber die Software ist grottig. Und wie bekommt man neue Radio-Sender einprogrammiert, seit es beim voreingestellten Radioanbieter "vTuner" nur noch dieses Abo-Modell gibt? Da hilft der Mediaserver der Fritzbox.

<!-- more -->

## Warum die DENON Anlage so schlecht ist

Zunächst ein Rant wegen der DENON CEOL Piccolo Stereoanlagen-Software. Also wenn man die Musikanlage einschaltet, dann benötigt sie ca. 2 Minuten, bis sie mit "hochfahren" fertig ist (keine Ahnung was das Teil da tut), dann erst fängt die Musik an zu spielen. Sofern sie überhaupt aktuell auf einen Sender eingestellt ist. Alle paar Stunden geht nämlich in unregelmäßigen Abständen der Stream aus, und die Anlage wechselt in den "Sender auswählen"-Modus, so dass man erstmal mit der Fernbedinung blöd rumklicken muss um wieder einen Sender anzuschalten. Macht man das nicht, geht sie von alleine aus. Früher dachte ich, das läge an unserem schlechten WLAN, aber inzwischen haben wir unser WLAN so dermaßen aufgerüstet, dass es daran definitiv nicht liegen kann. Das passiert auch bei egal welchem Sender, an den Sendern liegt's also auch nicht.

Und überhaupt, Spotify Connect soll die Anlage wohl können -> Vergiss es! Wenn man das nutzt, muss man an der Musikanlage danach einen Hard-Reset durchführen, das hab ich schon 2x machen müssen, die zeigt dann nur noch eine Fehlermeldung bei jedem Start. Und Bluetooth-Verbindung? Dauert ebenfalls ewig, bis die Verbindung aufgebaut wird, und funktioniert in 50% der Fälle nicht, dann muss man erst das Handy neustarten. (Und das liegt nicht am Handy sondern tritt NUR bei der DENON Musikanlage auf.. ich nutze noch andere Bluetoothboxen, die klappen immer und mit sofortigem Connect..)

Zu guter letzt darf man seit einiger Zeit keine neuen Internetradio-Sender mehr einprogrammieren, sondern man muss dafür erst ein jährliches Abo bei vTuner abschließen. Sorry, aber was stimmt mit DENON nicht.. Für so einen schlecht funktionierenden Service bezahl' ich doch nicht auch noch Abogebühren. Wenn ich mir nochmal ein Medienabspielgerät mit Internetanschluss kaufe, dann auf KEINEN FALL von DENON. Was mit Software, das können die einfach nicht.

## Fritzbox als Radiostationsliste nutzen

Genug Gemecker. Dieser Blog-Artikel soll sich um das Einprogrammieren neuer Internetradio-Sender drehen, ohne auf das Vtuner-Abo-Modell wechseln zu müssen. Mit einer Fritzbox geht das nämlich sehr gut: Da ist ein Mediaserver eingebaut, in den man die Internetsender konfigurieren kann, und dann lassen sie sich auch über die alte DENON Musikanlage abspielen, genau so komfortabel wie die dort sonst nur mit Abo auswählbaren Sender. Man muss dazu auf dem Denon Gerät beid der Senderauswahl über das Menü "Mediaserver" gehen, statt über "Internetradio".

**Problem:** Bei Änderungen an den Radiosendern in der Fritzbox (z.B. wenn man neue Sender eingetragen hat) ändert sich die Senderliste der Musikanlage nicht.

**Lösung:** Den Mediaserver der Fritzbox umbenennen, das hilft nicht. Man muss die Fritzbox neu starten (Menüpunkt "Sicherung" und dann den Reiter "Neustart"). Also wenn man z.B. neue Radiosender auf der Fritzbox hinterlegt hat, dann gibt die FritzBox im Netzwerk über DLNA immer noch fröhlich weiter eine alte Senderliste aus, die nicht der Senderliste entspricht, die im Admin-Interface der Fritzbox angezeigt wird! Erst wenn man sie neustartet, wird die neue Senderliste auch für andere Geräte im Netzwerk sichtbar.

## Gute Musiksender

Die bekannteren Sender (Sunshine live, Delta Radio, Alternative.FM, Flux.Fm, etc) haben teilweise recht nervige Werbung. Ist natürlich OK, die müssen ja Geld verdienen, aber an manchen Tagen habe ich keine Lust auf 10-Minuten-Pro-Stunde-In-Your-Face-Baumarkt-Werbung.
Daher habe ich die Streams der "Senderfamilien" Radio Record, Digitally Imported und Got Radio als Alternative entdeckt. Got Radio wirbt damit, dass nur 5 Minuten Werbung pro Stunde laufen, und die Werbung ist auch bei weitem nicht so aufgedreht und stressig wie "normale" Radiowerbung.

Got Radio ist aber erstmal die einzige meiner Lieblings-Radiostationen, die ich auf die Denon Anlage bekommen habe.

**Probleme:**
* Radio Record spielt seine Streams nur AAC+ codiert, was die Denon Anlage nicht versteht. Lösung: Noch keine
* Digitally Imported kann man kostenlos nur im Browser hören. Stream-Urls für Internetradio-Hardware gibt es nur im Premium-Modell für 48€/Jahr. Das lohnt sich vermutlich, aber dafür konnte ich mich noch nicht durchringen, das ist ja teurer als ein Playstation Plus Abo, und so oft höre ich nun auch wieder nicht in der Küche.. Lösung: Für einige Digitally Imported Sender findet man Stream-Urls in Radio-Stream-Suchmaschinen wie radio-browser.info.

**Senderlisten**

Alle Stream URLs von Sunshine Live:\
http://stream.sunshine-live.de/

Webseite mit ca. 30.000 Stream-URLs:\
https://www.radio-browser.info/ => Man findet dort auch vereinzelt DI.FM Urls, die vermutlich von DI.FM-Premium-Usern eingetragen wurden, und da eigentlich nicht rein gehören, aber funktioniert natürlich trotzdem..
Wenn man einen Sender dort findet, kann man in die Fritzbox die auto-generierte PLS-Datei von radio-browser.info eintragen, was den Vorteil hat, dass vielleicht jemand eine neue Stream-Url einträgt, wenn die alte Url mal nicht mehr funktioniert:
https://de1.api.radio-browser.info/pls/url/{UUID}

Alle Stream URLs von Radio Record (RU):\
https://docs.juniper.bot/en/misc/radio-stations/ => Die Links taugen aber leider nichts, weil das Audioformat (AAC+) von vielen Geräten nicht unterstützt wird, darunter die DENON CEOL Piccolo und mein Philips Fernseher.


## Meine komplette Internetradio-Senderliste

Als Reminder an mich selbst, falls ich wieder die Mediaserver-Soft- oder Hardware wechsele, ohne die Radiosender-Liste zu speichern..

| Sender | Stream Url |
|---|---|
| Byte.FM	| http://www.byte.fm/stream/bytefm.m3u |
| Flux.FM	| https://www.surfmusik.de/m3u/fluxfm-100-6,4326.m3u |
| Radio Q | https://de1.api.radio-browser.info/pls/url/fb59f331-eaba-45c1-a1b2-bf1183481ad9 |
| Alternative.FM	| http://www.alternativefm.de/afm_128.m3u |
| Sunshine Live |	https://sunshinelive.hoerradar.de/sunshinelive-live-mp3-hq |
| Sunshine Live Classics | https://sunshinelive.hoerradar.de/sunshinelive-classics-mp3-hq |
| Sunshine Live Chillout | https://sunsl.streamabc.net/sunsl-chillout-mp3-192-3900120 |
| Guitar Genius - Got Radio |  http://pureplay.cdnstream1.com/6018_128.mp3 |
| Piano Perfect - Got Radio | https://pureplay.cdnstream1.com/6017_128.mp3 |
| 90s Alternative - Got Radio | https://pureplay.cdnstream1.com/6039_128.mp3 |
| Alternative - Got Radio | https://pureplay.cdnstream1.com/6033_128.mp3 |
| Hardbase.FM | https://listen.hardbase.fm/tunein-mp3 |
| DrumAndBass.FM | http://radio.drumandbass.fm/listen192.m3u |
| Alternative - Delta Radio | https://delta.hoerradar.de/deltaradio-alternative-mp3-hq |
| Surf Rock Radio | https://de1.api.radio-browser.info/pls/url/81001fc1-72fd-483c-91f7-8475bdc8bbc4 |
| Liquid DNB | https://de1.api.radio-browser.info/pls/url/2ce32b92-2822-43a3-a0e0-5f3e56b64411 |
| Digital Impulse - Trance | https://de1.api.radio-browser.info/pls/url/96206a82-0601-11e8-ae97-52543be04c81 |

## Diese Sender habe ich leider aussortiert..

..weil nicht untertütztes Format AAC+ oder nur per Premium verfügbar. Aber trotzdem super Sender:

| Sender | Stream Url |
|---|---|
| Liquid Funk - Radio Record | https://radiorecord.hostingradio.ru/liquidfunk96.aacp |
| Summer Dance - Radio Record | https://radiorecord.hostingradio.ru/summerparty96.aacp |
| Chill House - Radio Record | https://radiorecord.hostingradio.ru/chillhouse96.aacp |
| Liquid Funk - Radio Record | https://radiorecord.hostingradio.ru/liquidfunk96.aacp |
| Trance - Digitally Imported | Webplayer => https://www.di.fm/trance und  https://www.di.fm/classictrance |
| Liquid DNB - Digitally Imported | Webplayer => https://www.di.fm/liquiddnb und https://www.di.fm/drumandbass |
