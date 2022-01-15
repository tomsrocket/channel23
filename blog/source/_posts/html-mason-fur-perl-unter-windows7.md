---
title: "HTML::Mason für Perl unter Windows7 "
date: 2012-03-02
author: Tom
categories:
- ["coding"]
tags:
---
Mason ist ein Webframework für Perl. Wenn man auf die verrückte Idee kommt, Webseiten mit Perl bauen zu wollen, dann benötigt man sowas.

Um das auf Windows 7 zum Laufen zu bekommen habe ich so ziemlich alles ausprobiert (XAMPP, zangweb, strawberry perl + irgendeine WAMPP distro) aber funktioniert hat es nur mit <a href="http://www.indigostar.com/indigoampp.php">indigoampp</a>.

Eine genauere Anleitung dazu folgt in diesem Blogpost.

<!-- more -->

Also:

* Indigoampp runterladen und installieren nach c:\indigoampp
* Mason installieren mit

	```
	cmd.exe
	cd indigoampp\perl-5.12.1\bin
	ipm

	# gestartet wird Indigo Package Manager (<em>IPM</em>),
	# ein Extra-Windows-Tool für IndigoPerl

	$ install HTML::Mason
	```

	.... wird installiert, irgendwann gibt es Fehler weil HTML::Entities nicht gefunden werden kann.

	```
	$ search entities
	```
	.... es werden ein paar module aufgelistet die HTML-Entities-irgendwas heissen. Eins davon installieren, dann:
	```
	$ install HTML::Mason -force
	```
	....diesmal sollte es klappen mit der Installation.

* Apache config anpassen:

	```
	<Directory "C:/indigoampp/apache-2.2.15/htdocs/perl">
	<IfModule mod_perl.c>
		SetHandler perl-script
		PerlHandler  HTML::Mason::ApacheHandler
		allow from all
	</IfModule&gt;&lt;/Directory>
	```

	Den anderen Bereich, der SetHandler perl-script benutzt einfach auskommentieren.

Bingo! Jetzt kann man unter http://localhost/perl/ Beliebige Skripte ablegen, die von HTML::Mason geparst werden.