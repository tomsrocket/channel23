---
title: "Wikidata per SPARQL abfragen / Beispielqueries"
date: 2025-12-29
author: Tom
categories:
- ["coding", "open"]

---

Wikidata ist ein unfassbar große und gute Datenquelle für alle möglichen Themen, ähnlich zu dem was in der Wikipedia zu finden ist. Mit dem schönen Vorteil, dass man die gesamten Informationen aus Wikidata mit der Abfragesprache "SPARQL" abfragen und verknüpfen kann. 

Alle Wikidata-Abfragen können online mit dem Wikidata Query Service gestellt werden: https://query.wikidata.org

## Allgemeine Tipps
* Immer Strg+Space drücken zur Autovervollständigung
* Z.B. wenn man `wdt:` eingegeben hat, dann kann man danach ein Wort bzw einen Suchbegriff eingeben, und strg+Leertaste, dann werden objekt-IDs aufgelistet die zu dem Suchbegriff passen
* Immer den Labelservice einbinden: SERV tippen, dann strg+leerzeichen, dann das dritte autocomplete item auswählen
* Mit der Maus über Q- oder P-Nummern drüber fahren, dann kann man die items und properties beschrieben bekommen.
* Wikipedia Daten Abfragen - Hier steht beschrieben, wie die Daten in Wikidata überführt werden: https://www.mediawiki.org/wiki/Wikibase/Indexing/RDF_Dump_Format

Allgemeine Infos, die ich aus einem Talk von https://github.com/lucaswerkmeister @ 39C3 mitgeschrieben habe. Ohne Gewähr.
* Wie aktiv wird eigentlich an Wikidata gearbeitet? 38.000 aktive Bearbeiter im Monat 
* Sind die Daten aus Wikipedia auch in Wikidata? Jein, es gibt keinen systematischen Import, aber die Community macht da immer mal wieder Dinge mit Tools

SPARQL Query Abfragen Beispiele folgen nach dem Klick..
<!-- more -->

<!--more-->

# Beispielqueries

Wann hat Albert Einstein welche Titel erhalten?
```sparql
SELECT ?Wert ?WertLabel ?Zeit WHERE {
  wd:Q937 p:P166 [
    ps:P166 ?Wert;
    pq:P585 ?Zeit
  ].
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". }
}
```

Welche Eigentschaften hat ein Wikidata Objekt?
```sparql
SELECT ?Eigenschaft ?EigenschaftLabel ?Objekt ?ObjektLabel WHERE {
  wd:Q137186950 ?wdt ?Objekt.
  ?Eigenschaft wikibase:directClaim ?wdt
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". }
}
```

Wer hat Wikipedia gegründet?
```sparql
#title:Die Gründer von Wikipedia
SELECT ?Gründer ?GründerLabel WHERE {
  wd:Q52 wdt:P112 ?Gründer.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". }
}
```

Was haben die beiden Gründer noch zusammen gegründet?
```sparql
SELECT ?Gründer ?GründerLabel WHERE {
  ?Gründer wdt:P112 wd:Q181.
  ?Gründer wdt:P112 wd:Q185.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". }
}
```

Was hat je einer der beiden Gründer noch gegründet?
```sparql
SELECT ?Gründer ?GründerLabel WHERE {
 { ?Gründer wdt:P112 wd:Q181. } UNION
 { ?Gründer wdt:P112 wd:Q185. }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". }
}
```

Jetzt noch mit Datum
```sparql
SELECT ?Gründer ?GründerLabel ?Datum  WHERE {
 { ?Gründer wdt:P112 wd:Q181. } UNION
 { ?Gründer wdt:P112 wd:Q185. }
  
  ?Gründer wdt:P571 ?Datum.
  FILTER(?Datum <= "2001-01-01"^^xsd:dateTime )
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". }
}
```

Alle Vorfahren von Ludwig den XIV.
```sparql
SELECT ?Vorfahr ?VorfahrLabel ?dob WHERE {
  wd:Q7742 wdt:P22* ?Vorfahr.
  ?Vorfahr wdt:P569 ?dob.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". }
}
```

Alle Veranstaltungen die Teil einer Reihe sind vom CCC: 
```sparql
SELECT ?Event ?EventLabel ?Start WHERE {
  ?Event wdt:P580 ?Start.
  ?Event wdt:P179 ?Reihe. 
  ?Reihe wdt:P664 wd:Q124062965
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". }
}
```

Dynamische Abfrage über die Hierarchie
```sparql
SELECT DISTINCT ?Event ?EventLabel ?Start WHERE {
  ?Event wdt:P580 ?Start.
  ?Event wdt:P179?/wdt:P664/wdt:P749? wd:Q23138.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". }
}
ORDER BY ?Start
```

## Weitere Links 
* Tutorials: https://developer.wikimedia.org/use-content/tutorials/ ("Getting startet querying Wikidata")
* Artikel mit weiteren Beispielen: https://katharinabrunner.de/2022/06/useful-snippets-for-writing-sparql-queries/
