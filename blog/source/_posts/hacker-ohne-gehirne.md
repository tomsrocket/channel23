---
title: "Häcker ohne Gehirne"
date: 2007-05-03
author: Tom
categories:
- ["various"]
tags:
---
*LOL** ich raff's nich mehr.. was geht hier eigentlich ab. Ich wollt mir bloss mal die Zugriffsstatistiken vom <a href="http://www.wohnzimmer-ev.de" title="Homepage Wohnzimmer e.V." target="_blank">wohnzimmer-ev.de</a> angucken.. Seh ich da, dass die meisten nachverfolgbaren Hits von irgendsoner polnischen Hackerseite kommen. (700 hits/monat) .. Ok - Schock überwunden, Apache Logfile reingeschaut, gehen alle Zugriffe von der Hackerseite bloss auf eine olle Pfeilchen-Icon-Gif-Grafik aus dem Wohnzimmer-e.V.-Forum.  ("arrow.gif")

OK.. Im Hackerforum nachgeschaut, und tatsächlich, irgendjemand hat allen ernstes eine Icon-Grafik vom wohnzimmer-ev-server über &lt;img src="http://wohnzimmer-ev.de/bla/forum/arrow.gif"&gt; eingebunden.. Was hat der denn geraucht, warum macht der das? Jedenfalls, gut dass es REWRITE_COND gibt ;-) Gleich mal die arrow.gif per .htaccess weitergeleitet, sofern der referer von dieser komischen Url kommt..

vorher:   <a href="/blog/wp-content/uploads/2007/05/hackerssvorher.jpg" title="Hackerforum mit unserer Grafik"><img src="/blog/wp-content/uploads/2007/05/hackerssvorherVorschaubild.jpg" alt="Hackerforum mit unserer Grafik" /></a>    nachher:   <a href="/blog/wp-content/uploads/2007/05/hackerssnachher.jpg" title="Hackerforum mit umgeleiteter Grafik"><img src="/blog/wp-content/uploads/2007/05/hackerssnachherVorschaubild.jpg" alt="Hackerforum mit umgeleiteter Grafik" /></a>

Der Kack-Hut war mir aber dann doch zu krass, nich dass die Jungs noch sauer werden und auf dumme Gedanken kommen. Hab das inzwischen gegen Schäuble ausgetauscht.. :-)  Siehe http://foros.hackerss.com/index.php?showtopic=927&amp;hl=Soft

Mal gucken ob das so bleibt.. Oder ob die jetzt den Wohnzimmer-e.V.-Server plattmachen :-p