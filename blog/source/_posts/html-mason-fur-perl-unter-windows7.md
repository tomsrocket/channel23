---
title: "HTML::Mason für Perl unter Windows7 "
date: 2012-03-02
author: Tom
categories:
- ["coding"]
tags:
---
Ich hab so ziemlich alles ausprobiert (XAMPP, zangweb, strawberry perl + irgendeine WAMPP distro) aber funktioniert hat es nur mit <a href="http://www.indigostar.com/indigoampp.php">indigoampp</a>.

Also:
<ol>
	<li>Indigoampp runterladen und installieren nach c:\indigoampp</li>
	<li>Mason installieren mit
<code>
cmd.exe
cd indigoampp\perl-5.12.1\bin
ipm&nbsp;

# gestartet wird Indigo Package Manager (<em>IPM</em>), ein Extra-Windows-Tool für IndigoPerl

$ install HTML::Mason
.... wird installiert, irgendwann gibt es Fehler weil HTML::Entities nicht gefunden werden kann.
$ search entities
.... es werden ein paar module aufgelistet die HTML-Entities-irgendwas heissen. Eins davon installieren, dann:

</code><code>$ install HTML::Mason -force
....diesmal sollte es klappen mit der Installation.
</code></li>
	<li>Apache config anpassen:
<code>&lt;Directory "C:/indigoampp/apache-2.2.15/htdocs/perl"&gt;
&lt;IfModule mod_perl.c&gt;
SetHandler perl-script
PerlHandler  HTML::Mason::ApacheHandler
allow from all
&lt;/IfModule&gt;&lt;/Directory&gt;</code></li>
</ol>
Den anderen Bereich, der SetHandler perl-script benutzt einfach auskommentieren.

Bingo! Jetzt kann man unter http:://localhost/perl/ Beliebige Skripte ablegen, die von HTML::Mason geparst werden.