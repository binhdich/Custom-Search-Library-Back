# Overview

Dieses Projekt soll die Möglichkeit für jeden bieten, seine ganz eigene individuelle Suchbibliothek zu erstellen.

# Purpose

Anwendungsbeispiel: Man schreibt seine Bachelorarbeit und hat unzählig viele verschiedene Text- und Informationsquellen. Von eingescannten Seiten aus Büchern bis hin zu gegoogelten Websites. Ab einem bestimmten Punkt verliert man den Überblick. Dann kann es schonmal sehr schwer fallen sich zu erinnern, in welchem Dokument sich eine bestimmte Textstelle oder Information befand. Dieses Custom Search Engine Projekt könnte Abbhilfe schaffen. Es ist eine Webapplikation, welches ermöglicht digitale Textdokumente inklusive Zuordnungsreferenz, sprich eigener Name für das Dokumente oder URL oder whatever man möchte, in einer Datenbank zu speichern. Zusätzlich ist die Möglichkeit geboten, diese Datenbank blitzschnell nach Keywords, Passagen etc zu durchsuchen. Dabei wird eine sortierte Liste an Dokumenten ausgegeben, auf diese die Suchanfrage am ehesten passt. 

## Wie erfolgt die Suche so schnell?

Dokumente werden nicht einfach so als Ganzes in der Datenbank abgespeichert. Vielmehr werden sie indexiert. In diesem Kontext bedeutet das, dass der gesamte Text auf jedes einzelne Wort aufgesplittert wird und dann anschließend werden die Wörter zusammen mit der Referenz und der Anzahl ihres Vorkommens innerhalb des Dokumentes abgespeichert. Somit werden bei der Suchanfrage keine gesamten Volltexte durchgeschaut sondern noch einzelnen Wörtern. Anschließend wird geschaut, wo sie vorkommen und wie oft.

## Nach welchen Kriterien werden die Suchergebnisse sortiert?

Um die Relevanz zu bestimmen wird ein Mix aus Häufigkeit der einzelnen Keywords aus der Suchanfrage in den einzelnen Dokumenten(ja man kann nach ganzen Sätzen/Textstellen etc suchen) und die Vollständigkeit der Suchanfrage je Dokument genommen. Heißt allein weil ein Wort aus der Suchanfrage sehr oft in einem Dokument vorhanden ist, bedeutet das nicht automatisch, dass dieses ganz oben erscheint. 

## Auf welcher Datenbanktechnologie basiert das Ganze?

Es wird aktuell auf eine NoSql Cloudlösung von Microsoft Azure zurückgegriffen. Diese bietet die ideale Flexibilität und Skalierbarkeit für das Projekt.

## Wie kann hier noch weiter zu beigetragen werden?

Aktuell beschränkt sich das Projekt auf Websites als Dokumente. Sprich die Webanwendung bietet derzeit nur die Möglichkeit URLs anzugeben, um Webinhalte zu indexieren. Auch wäre eine Nutzerverwaltung eventuell sinnvoll. Im Moment kann jeder so viele Indices erstellen wie er möchte (solange der Speicherplatz hierfür ausreicht) Die Suchanfragen beziehen sich pro Index. Man kann selbst eingeben wie der Index heißen soll und entsprechend welchen Index man durchsuchen möchte. Die Option Einträge zu löschen gibt es bisher auch nur manuell. Ebenfalls fehlt die Frontend Anzeige für die Suchergebnisse. Aktuell existiert hierfür noch keine visuelle Ausgabe.
![image](https://user-images.githubusercontent.com/90770330/177101751-594a99c0-5e4b-4bc1-a7a7-74c7809c5eb8.png)


# Zur Einrichtung:

Bitte vorher die requirements.txt Datei einsehen und die aufgeführten requirements installieren. 

## Die Klassen:

### dbConnector 
- stellt die Verbindung zur Datenbank her. Die hierfür benötigten Zugriffsdaten lassen sich im eigenen <a href="https://portal.azure.com/#home">Azure Portal</a>  einsehen. Verwendet wird CosmosDB 

### controller 
- bildet die Schnittstelle zum Frontend

### parser 
- hier werden Dokumente für zum Indexieren aufbereitet

### index 
- umfasst die Index-Funktion für Dokumente

### search 
- beinhaltet die Suchfunktion inklusive Ranking Algorithmus

