---
title: "Dual Boot mit Windows, Linux (Ubuntu), Ruhezustand (Hibernate) und gemeinsamer Partition"
date: 2010-10-08
author: Tom
categories:
- ["allgemein"]
tags:

---
Ok. Manchmal nervt's mich wie kompliziert Betriebssyteme sein können.
Wenn man ein Dual-Boot-System mit Windows und Linux hat (z.B. Windows 7 und Ubuntu) und beide laufen auf getrennten Festplatten, und man möchte die Systeme nicht immer komplett herunterfahren, 
sondern im Ruhezustand beenden (Ruhezustand = "Hibernate" => Speicherabbild wird auf Festplatte gespeichert) und quasi beim Booten will man immer nur zwischen dem Linux- oder dem Windows- Ruhezustand wechseln, dann ist das solange kein Problem wie man keine *gemeinsame Partition* verwendet. 

<!-- more --> 
<h3>Gemeinsame Partition mit FAT-32</h3>
Sobald man eine gemeinsame Partition hat, ist die Kacke am dampfen. 
Ich habe für die shared Partition extra FAT32 gewählt, weil ich dachte, "altes und simples Dateisystem, da kann nicht viel schiefgehen".
Aber Pustekuchen, Windows speichert im Hibernate-Abbild irgendwelche Dateisystem-Cache-Strukturen.
Wenn man also unter Linux Dateien auf die FAT32 Partition speichert, und dann Windows bootet, dann sind die Dateien plötzlich verschwunden. 

Probier mal folgendes aus: 
Man beende Windows indem man es in den Ruhezustand ("Hibernate") fährt.
Dann starte den Rechner neu. Im Dual Boot Menü (bei mir: Grub) wähle nun Ubuntu Linux aus und fahre es hoch. 
(Ob das Linux auch im Ruhezustand war oder nicht, ist egal)
Schreibe Dateien auf eine FAT32-Partition die im Windows gemountet ist. 
Beende Linux, fahre Windows aus dem Ruhezustand hoch: Schwupps, die Dateien sind weg. 

Das Problem wurde schon 2005 im Ubuntu Forum geschildert: 
<a href="http://ubuntuforums.org/showthread.php?p=171082">http://ubuntuforums.org/showthread.php?p=171082</a>
Aber irgendwie keine gescheite Lösung.. :-p

<h3>Gemeinsame Partition mit NTFS</h3>
Man kann statt FAT32 auch einfach NTFS nutzen, dann tritt das Problem angeblich nicht so oft auf, wenn man Glück hat sogar garnicht. 
Das trügt aber, denn das Problem bleibt das gleiche! Windows hat irgendwelche Inodes im Cache und es kann unter ungünstigen Umständen sogar passieren, dass das NTFS Dateisystem komplett kaputtgeht.
Näheres dazu hier: 
<a href="http://superuser.com/questions/39532/hibernating-and-booting-into-another-os-will-my-filesystems-be-corrupted">http://superuser.com/questions/39532/hibernating-and-booting-into-another-os-will-my-filesystems-be-corrupted</a>


Dieses Problem hat ausser mir anscheinend kaum jemand. 
Und anscheinend muss einem total klar sein dass das alles nicht funktioniert. Mir war's nicht. 


<h3>Die Lösung</h3>

<strong>Ansatz 1: Fremd-Tool</strong>
Ich fand ein Tool namens "hiberfix", das man unter Windows als Service installieren kann.
Das ist aber in der neusten Version von 2005, und läuft nicht unter Windows 7.

<strong>Ansatz 2: "Festplatte auswerfen"</strong>
Ich dachte mir, "unter Linux kann man die Platte doch einfach un-mounten, dann wird alles draufgeschrieben und bingo, 
wieso sollte man das nicht unter Windows machen".
Tatsächlich geht das. 
Und zwar mit dem Tool "diskpart", das wird bei Windows mitgeliefert und das kann man über die Kommandozeile cmd.exe oder die Powershell benutzen:


<strong>Partition abmelden (dismount.txt)</strong>
Bei mir ist der Laufwerksbuchstabe der shared partition "E:/"

<code>diskpart
list disk
select disk 0
select volume e
(Er sagt jetzt "Volume X ist jetzt das gewählte volume." Den Wert von X merken!)
remove letter=e
</code>
=> Bingo, Partition ist abgemeldet!


<strong>Partition anmelden (mount.txt)</strong>

<code>diskpart
list disk
select disk 0
select volume X 
(Statt X den o.g. Wert einsetzen. Bei mir X=2)
assign letter=e</code>

=> Partition back online!


Die beiden Skripte kann man sich dann als Batch-Dateien anlegen: 
<em>before_hibernate.bat</em>
<code>diskpart /s dismount.txt </code>

<em>after_startup.bat</em>
<code>diskpart /s mount.txt </code>


Eine umfangreiche und sehr detaillierte Übersicht über die Funktionen von diskpart gibt es hier: 
<a href="http://technet.microsoft.com/de-de/library/cc766465%28WS.10%29.aspx">http://technet.microsoft.com/de-de/library/cc766465%28WS.10%29.aspx</a>
