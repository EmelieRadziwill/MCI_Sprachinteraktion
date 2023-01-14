# Präsentation Stichpunkte
## Aufgabenstellung
### Thema
Unser Praktikum beschäftigt sich mit der individualisierten Interaktion zwischen Mensch und Computer am Beispiel eines Sprachassistenten ausgelegt auf ältere Menschen und deren Bedürfnisse.

### Ziele
Dementsprechend ist das Ziel die Entwicklung eines für die Zielgruppe älterer Menschen anwendbaren Adaptionskonzepts für Sprachinteraktion basierend auf der Konfiguration von Feature-Modellen und der Konfigurationsauswahl durch ein Recommender-System.

## Lösungsidee
Die Umsetzung unterteilt sich in vier Teilschritte:

Analyse der Zielgruppe: Sammeln und Auswerten von Demografischen Daten sowie Studien. Erstellung eines User Model sowie Personas.

Design eines Feature-Model: Anforderungsanalyse anhand des User-Model, sowie Publikationen über verwandte Arbeiten.

Entwicklung eines Recommender-System: KNN-Algorithmus entwicklen, auf den Personas basierend Traingsdaten erstelllen und damit das System anlernen

Exemplarische Anwendung (Prototyp): beispielhafte Darstellung mithilfe eines Sprachskills (durch Voreinstellungen individualisiert)

## Aktueller Stand
### Analyse der Zielgruppe
22% der Bevölkerung in Deutschland ist über 65. Durch die Größe der Zielgruppe entsteht eine Vielfalt in den Charackteristiken. 

So unterscheiden sich Senioren nicht nur in vermeintlich offensichtlichen Punkten wie der Wohnsituation, dem Familienstand, Gesundheit, und der Höhe des Einkommen. Sondern ebenfalls in Punkten wie den technischen Vorkenntnissen die sie mitbringen, ihren Altagsgewohnheiten und ihrem allgemeinen Bildungsstand. 

Auch ist zu berücksichtigen, das einige Merkmale einen Einfluss auf andere Merkmale haben. Beispielsweise beeinflussen Bildungsstand und Einkommen, das Gesundheitsempfinden.

Auch steigt die Anzahl der Senioren bei den Gasthöhrern an Hochschulen. Wintersemester 2004/2005 bei 22% Senioren unter Gasthörern und Wintersemester 2014/2015 42%. Dadurch zeigt sich, das zumindest ein Teil wissbegierig und offen für neue Informationen ist.

Auch Gesundheitlich enorme Unterschiede. Ob kognitiv, snsorisch oder physisch, jeder Senior definiert sich über andere Einschränkungen, welche berücksichtigt werden müssen, um ihm seinen Alltag so leicht wie möglich zu gestalten. 
Besonders häufig vertreten sind Seh- und Hörschwächen, eingeschränkte Beweglichkeiten und eine verminderte Anpassungsfähigkeit

Dazu wurden Personas anhand von Studien und Demografischen Daten Entwickelt. Zwei Beispiele hier: Neugierde und Starsinn veranschaulicht

### Design eines Feature-Model
Unterteilung in drei Gruppen: Stimme, Spracheigenschaften und Kommunikationsstil.

Stimme soll möglichst gut verständlich und subjektiv angenehm sein. Unterscheidung von Geschlecht, Tonlage, Stimmart und Lautstärke. Je nach Präferenzen des Nutzers. Systeme werden ehr angenommen, wenn der Nutzer sie als Angenehm empfindet. Häufig werden männliche tiefe Stimmen bevorzugt, jedoch auch identifizierung wichtig je nach Charakter. 

Spracheigenschaft definiert die Sprechweise, ob Pause zwischen den Sätzen für besseres Folgen der Konversation nötig sind, die allgemeine Sprechgeschwindigkeit oder die länge der Sätze. Sowie die zusätzliche möglichkeit den Ausdruck zu vereinfachen um die Komplexität möglicher Antworten zu verringern. Je nach dem wie geistig Fit die Nutzer sind kann dies das Sprachverständnis fördern

Kommunikationsstil fokussiert sich auf Sprache und Umgang zwischen VA und Nutzer, beispielsweise welche Anredeform bevorzugt wird, oder ob sich das System nur auf die Aufgaben beschränken soll oder sozialer agiert. Ebenfalls die möglichkeit zu Alternativen Keywords (Wake up, Abfragen von funktionen) um nicht mit den Sprachgewohnheiten des Nutzers zu brechen. 

### Entwicklung eines Recommender-System
basierend auf dem Recommender-System von vorherigen Praktikum

"gefüttert" mit Trainingssätzen --> Personas/Forschungsergebnisse(Analyse Zielgruppe)

nach Initialfragestellungen gibt Recommender basierend auf KNN eine für ihn sinvolle Konfiguration aus

Nutzer kann beliebige Einstellungen übernehmen

seperate Funktion überprüft Validität der Konfiguration (Featuremodell)


### Herausforderungen
Zielgruppe: Wo nimmt man daten her und was ist davon dann wichtig? Wenig vorerfahrung

Feature Model: Welche Features sind überhaupt umsetzbar und was ist Skill und was Feature? 

Recommender System: Wie mache ich aus einer Persona eine Konfiguration, wie setzt man an?

Teamarbeit: Austritt eines Teammitglied, umverteilung der Aufgaben. Aufgaben analyse, unterschiedliche Interpretationen und Kommunikationsschwierigkeiten.

Zeitmanagement: Abschätzung des Arbeitsaufwands und planen der Sprints

## Zeitplan und nächste Schritte

Ab dem 10.11.2022: Einarbeitung in frühere Arbeiten und Analyse der Zielgruppe. 
Ab dem 15.12.2022: Feature Modell anfangen und Analyse der Anforderungen für das Recommender Systen
Ab dem 05.01.2023: Personas erstellen, weitere Ausarbeitung des Feature Modell sowie beginn des Recommender System

Die weiter geplanten Schritte sind die fertigstellung des Recommender Systems, die implementierung des Skills zum proof of concept und das ausarbeiten der Dokumentation

## Demo

## Fragen für die Diskussion

Rücksichtahme auf Dialekte?
Welche Skilld sind sinnvoll für Senioren?
Möglicher Ausbau des Konzeptes zu einem Helfersystem, was für Funktionen?
Bessere Annahme von VAs durch Senioren, wie?