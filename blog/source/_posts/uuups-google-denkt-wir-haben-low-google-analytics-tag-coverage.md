---
title: "Uuups - Google denkt wir haben 'low Google Analytics tag coverage'?"
date: 2010-07-29
author: Tom
categories:
- ["allgemein"]
tags:
---
Da wollte mal jemand die tollen neuen "AdPlanner" Tools von Google ausprobieren, und hat festgestellt, dass dort eine Warnmeldung von Google aufgeführt ist: 
"blaa.com has low Google Analytics tag coverage"

Ich habe natürlich sofort die Suchergebnisse der Google-Suche nach "site:blaa.com" großflächig stichprobenartig durchsucht, aber keine sinifikanten Mengen an fehlenden Analytics-Tags gefunden. 
 
Einzig aufgefallen ist, dass Google offensichtlich vereinzelt AJAX-Fragmente die eigentlich in der Seite nachgeladen werden als alleinstehende Suchtrreffer indiziert hat, was suboptimal ist. Aber das schienen nicht viele zu sein.
Trotzdem nach einer Lösung gesucht, und neben rel="nofollow" an den entsprechenden Links auch einen HTTP-Header eingebaut den ich vorher noch nicht kannte, der aber wohl ähnlich funktionieren soll wie der &lt;META ROBOTS.. &gt;-Tag (nur dass ich keinen HTML &lt;HEAD&gt;-Bereich habe wo ich den META-Tag hinpacken könnte): 
<strong>header( 'X-Robots-Tag: noindex, nofollow', true);</strong>
Mehr dazu hier: <a href="http://yoast.com/x-robots-tag-play/">http://yoast.com/x-robots-tag-play/</a>

Vielleicht hilft das ja erstmal.. Ich werde zusätzlich noch ein Skript schreiben das unsere Seite crawlt und die Ergebnisse nach GA-Tags durchsucht. Aber nicht heute. ;-p