---
title: "Landkarte aller münsteraner Spielplätze 2020"
date: 2020-01-10
author: Tom
categories:
- ["allgemein"]
tags:
---

# Spielplätze in Münster


<a href="//plot.ly/~tomsrocket/1/"><img src="//www.channel23.de/spielplaetze-in-muenster/spielplatzkarte-preview.jpg" alt="Spielplatzstandorte" /></a>

*Wo sind die Spielplätze in Münster?*

Ich habe mal im Jahr 2012 eine Karte mit allen Spielplätzen in Münster gebaut, weil es so etwas noch nicht gab.
Meine Karte von damals funktioniert leider inzwischen nicht mehr, vermutlich weil sich bei Google Maps irgend etwas geändert hat.

ABER wir sind im 20. Jahrhundert, da braucht man keine Spielplatzkarte mehr selbst bauen, denn es gibt fertige Angebote: 

## Spielplatzkarte #1 - Umrisse 
<a href="//geo.stadt-muenster.de/webgis/application/Umweltkataster?visiblelayers=598/6191">Diese Karte vom Katasteramt Münster zeigt von allen Spielplätzen die exakten Umrisse.</a> Und ich hätte fast behauptet, diese Karte ist perfekt, aber leider gibt es hier keine weiteren Informationen zu den Spielplätzen, z.B. welche Spielgeräte gibt es dort, oder zumindest welche Altersklassen sind die Zielgruppen des Spielplatzes.

## Spielplatzkarte #2 - Punkte mit Details
<a href="//geo7.stadt-muenster.de/webgis/map/?wmsurl=https%3A//www.stadt-muenster.de/ows/mapserv706/odspielplserv&wmslayer=spielplaetze&titel=Spielpl%C3%A4tze"> Ebenfalls vom Katasteramt eine Karte mit allen Spielplätzen.</a> Hier werden statt der exakten Umrisse aber Punkte auf der Karte angezeigt. Der Vorteil ist: Wenn man auf einen Punkt klickt, bekommt man weitere Informationen zum entsprechenden Spielplatz angezeigt. Z.B. Altersklasse, Größe in Quadratmeter, und ob ein Ballspielplatz dabei ist. Dazu gibt es folgende Kategorien: 



    Altersklasse
    A - Spielplatz für alle Altersklassen mit zentraler Versorgungsfunktion
    B/C - Kleinkinder/schulpfl. Kinder/Jugendliche => Versorgung eines Wohnbereiches
    C - Spielplatz für Kleinkinder

    Ball
    0 - kein Ballspielplatz
    1 - separater Ballspielplatz
    2 - Spielplatz mit integriertem Ballspielplatz

## Spielplatzkarte #3 - Fancy
Ich wollte diese Informationen gern alle "gleichzeitig" in der Karte sehen können. Moderne Darstellungsmöglicheiten bieten da ja so einiges. Man kann über die Größe und Farbe der Punkte zusätzliche Informationen kodieren, nämlich z.B. Altersklasse und Größe. Glücklicherweise hat die Stadt Münster ein Open-Data-Portal auf dem man die Spielplatz-Standorddaten herunterladen kann. Außerdem gibt es komfortable Online-Tools, um Daten zu visualisieren, z.B. Plotly. In Kombination sieht das dann so aus:

<a href="//plot.ly/~tomsrocket/1/">Visuell aufbereitete Darstellung aller Münsteraner Spielplätze</a>


Man kann mit einer solchen Karte gucken, wieviele Spielplätze in der näheren Umgebung seiner Wohnung liegen, bzw. in der Nähe der Traumwohnung wenn man auf Wohnungssuche ist. Ein weiterer Anwendungsfall ist z.B. ein langeweiliges Wochenende, an dem man nicht weiß, was man unternehmen soll: Ein Ausflug zu einem "neuen" Spielplatz geht immer. 
Die Spielplatz-Koordinaten stammen aus der OpenData-Initiative 2011 und wurden von der Stadt Münster zur Verfügung gestellt. 

**Das Open Data Portal der Stadt Münster**

Wer sich selbst eine solche visuelle Darstellung bauen möchte, findet die notwendigen Daten auf dem Open-Data-Portal der Stadt Münster:  
<a href="//opendata.stadt-muenster.de/dataset/kinderspielpl%C3%A4tze">Datensatz mit allen Spielplatz-Standorten und weiteren Informationen, leider aber *nicht* mit einer detaillierten Liste aller Spielgeräte</a>

