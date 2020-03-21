---
title: "Data Science Meetup Münster - Julia"
date: 2020-03-12
author: Tom
categories:
- ["coding"]
tags:
---

Beim Datascience Meetup Münster am 12.3.2020 hat Mirko Bunse von der TU Dortmund die Programmiersprache Julia vorgestellt.
Das Treffen fand statt im DigitalHub Münster.
<!-- more -->


## Julia

Meine Notizen zu den Folien: 
* Dynamische Sprachen (Python, R ..) vs. statisch getypte Sprache (C++, Java ..)
* Julia liegt quasi im Raum dazwischen. 
* Hat eine Just in time (JIT) Kompilierung. 
* Unterstützt optional Typisierung.
* Man kann z.B. erstmal einen Prototypen ohne Typisierung bauen, und dann zum Beschleunigen später Typen hinzufügen.
* Julia gibts seit 2012
* Parallelisierung ist möglich, und teilweise schon eingebaut.
* Hat eine interaktive shell, dort integriert ist eine Bash shell und eine Paketverwaltung
* Wenn man die shell nutzt, um seine Programme auszuführen, dann funktioniert auch die just-in-time-Kompilierung
* Tab completion funktioniert auch mit utf8 zeichen, wenn man die wie bei LateX eingibt
* Objektorientierte features sind nicht so ausgereift, dafür gibt es "Multiple dispatch", mit dem man viel machen kann
* "jump" Julia for Mathematical Programming => Beliebtes Paket, für Optmierung z.B.
* Parallele Ausführung kann man über eine Konfigurationsdatei steuern (welche Knoten gibt es, wer ist der Masterprozess, etc..)
* Das macht das Paket "distributed" das ist in der Standardinstallation mit drin
* Die Verbreitung ist nicht sehr groß
* Es gibt viele Pakete, aber nicht so viele wie bei Python. Es gibt aber ein Python-binding und man kann Python Pakete benutzen.

Beispiele für Typen

    x = 1
    typeof(x) # Int64
    
    x = "1"
    typeof(x) # String

    function printtype(x)
        println (typeof(x))
    end

    # Mit typen

    printtype_int(x::Integer) = println("Some integer, typeof(x))

    printtype_int(1) # geht
    printtype_ing("1") # wirf teinen Fehler

Beispiele für Loops

    for i in [1,2,3] # regulärer loop
        println(i)
    end

    foreach(println, 1:3) # functional style

    println.(1:3) # dot syntax

Details findet man in den Folien von Mirko: 
https://github.com/mirkobunse/julia-knn-tutorial/blob/master/julia-introduction.pdf

In diesem Repository sind auch die Übungsaufgaben, die wir nach dem kurzen Intro-Vortreag gemacht haben:
https://github.com/mirkobunse/julia-knn-tutorial
