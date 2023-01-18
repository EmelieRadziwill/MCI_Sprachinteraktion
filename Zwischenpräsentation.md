# Präsentation Stichpunkte
## Einleitung (Emelie)
### Inhalt (Eric?, Max?)
## Aufgabenstellung
### Thema (Eric)
Unser Praktikum beschäftigt sich mit der individualisierten Interaktion zwischen Mensch und Computer am Beispiel eines Sprachassistenten ausgelegt auf ältere Menschen und deren Bedürfnisse.

Bevölkerungsanteil von Senioren in DeutschesLand steigt stetig Anfang 2000 noch bei 17%, 2020 22%, VA durch Hand und Augenfreie Kommunikation besonders gut geeignet um einen Begleiter im Alltag zu bieten. Ob einfachen Zugang zum Internet, unterstützen der täglichen Aufgaben oder sozialen Support. Je nach Skill ist dieser vielseitig einsetzbar. Doch was muss ein entsprechender Sprachassistent mitbringen?

individualisierten Interaktion zwischen Mensch und Computer
ausgelegt auf ältere Menschen und deren Bedürfnisse

Bevölkerungsanteil von Senioren in DeutschesLand
Sprachassistenten bieten eine augenfreie Kommunikation mit Systemen die den Alltag erleichtern

einfacher Zugang zum Internet, Unterstützung bei täglichen Aufgaben, sozialer Support oder einfach nur die Erinnerung an Termine 

### Ziele (Max)
Dementsprechend ist das Ziel die Entwicklung eines für die Zielgruppe älterer Menschen anwendbaren Adaptionskonzepts für Sprachinteraktion basierend auf der Konfiguration von Feature-Modellen und der Konfigurationsauswahl durch ein Recommender-System.

## Lösungsidee (Max)
Die Umsetzung unterteilt sich in vier Teilschritte:

Analyse der Zielgruppe: Sammeln und Auswerten von Demografischen Daten sowie Studien. Erstellung eines User Model sowie Personas.

Design eines Feature-Model: Anforderungsanalyse anhand des User-Model, sowie Publikationen über verwandte Arbeiten(Sprachassistent).

Entwicklung eines Recommender-System: KNN-Algorithmus entwicklen, auf den Personas basierend Traingsdaten erstelllen und damit das System anlernen

Exemplarische Anwendung (Prototyp): beispielhafte Darstellung mithilfe eines Sprachskills (durch Voreinstellungen individualisiert)

## Aktueller Stand
### Analyse der Zielgruppe (Emelie)
Zur Analyse der Zielgruppe wurden verschiedene demografische Daten und Studien gesammelt und ausgewertet. Das Resultat war eindeutig uneindeutig, mit anderen Worten: Senioren sind keine homogene Gruppe. 

22% der Bevölkerung in Deutschland ist über 65, bei 83 Millionen Menschen sind das etwas über 18 Millionen. Durch die Größe der Zielgruppe entsteht entsprechend eine Vielfalt in den Charackteristiken. 

Neben den offensichtlichen Punkten wie Geschlecht und Alter, variieren vor allem das Einkommen (Wie viel steht monatlich zur Verfügung und woher kommt es?), der Bildungsstand (gemessen an Abschlüssen), die Wohnsituation (Haushaltsgröße oder Heim) und der Familienstand (verheiratet, ledig/verwitwet). 

Ebenfalls korrelieren einige der Faktoren, beispielsweise tendieren Einkommensstärkere Senioren, oder solche mit höherem Bildungsgrad, dazu sich länger gesundheitlich Fit zu fühlen, was sich wiederum auf das Allgemeinbefinden positiv auswirkt.

Etwas, das die gesammte Zielgruppe betrifft, ist der umgangssprachliche Altersstarrsinn, mit zunehmendem Alter verringert sich die Aufnahme- und Anpassungsfähigkeit, sowie die geistige flexibilität. Aud die natürliche Neugierde und den Wissenddrang hat dies jedoch keinen Einfluss. So stieg beispielsweise die Anzahl der Senioren unter den Gasthöhrern an Hochschulen. Wintersemester 2004/2005 lag diese noch bie bei 22%, Wintersemester schon bei 2014/2015 42%. 

Auch Gesundheitlich gibt es enorme Unterschiede. Ob kognitiv, snsorisch oder physisch, jeder Senior definiert sich über andere Einschränkungen in anderen Ausmaßen, welche berücksichtigt werden müssen, um ihm seinen Alltag so leicht wie möglich zu gestalten. 
Besonders häufig vertreten sind Seh- und Hörschwächen, eingeschränkte Beweglichkeiten und Vergesslichkeit auf. 

Zur besseren Veranschaulichkeit, wurde Personas entwickelt, zwei sind hier vorgestellt. Diese sind nach Charaktertypen gestaltet und angelehnt an eine Studie, welche die Reaktionen von älteren Menschen auf Sprachassistenten untersuchte. 

Da wäre zum einen der sprunghafte und neugierige Typ, hier personifiziert als Giesela. Häufig hat dieser Personentyp schon erste Erfahrungen mit technischen Geräten gemacht und ist meist motiviert, sich damit auseinander zu setzen. Auch wenn es häufig am technischen Verständnis hakt.

Das genaue Gegenteil ist Herbert, dieser Typ ist ehr nachdenklich und primär skeptisch und ablehnent Gegenüber Technik. Vor allem die Akzeptanz ist ein Problem, auch wenn die Vorteile eines solchen Systems gesehen werden, gibt es nur wenig Vertrauen. 

### Design eines Feature-Model (Emelie)
Mittels der Nutzeranalyse, wurde ein Feature Modell konzipiert.

Unterteilung in drei Gruppen: Stimme, Spracheigenschaften und Kommunikationsstil.

Stimme soll möglichst gut verständlich und subjektiv angenehm sein. Unterscheidung von Geschlecht (männlich, weiblich), Tonlage (tief, mittel, hoch), Stimmart (natürlich, syntetisch) und Lautstärke (Skala 1-5 Repräsentativ). Je nach Präferenzen des Nutzers. Systeme werden ehr angenommen, wenn der Nutzer sie als Angenehm empfindet. Häufig werden männliche tiefe Stimmen bevorzugt, jedoch auch identifizierung wichtig je nach Charakter. 

Spracheigenschaft definiert die Sprechweise des VA, ob Pause zwischen den Sätzen, für besseres Folgen der Konversation, nötig sind, die allgemeine Sprechgeschwindigkeit (durchschnittlich, verlangsamt) oder die länge der Sätze potenziell verkürzt wird. Sowie die zusätzliche möglichkeit den Ausdruck zu vereinfachen um die Komplexität möglicher Antworten zu verringern. Je nach dem wie geistig Fit die Nutzer sind kann dies das Sprachverständnis fördern

Kommunikationsstil fokussiert sich auf Sprache und Umgang zwischen VA und Nutzer, beispielsweise welche Anredeform bevorzugt wird, oder ob sich das System nur auf die Aufgaben beschränken soll oder sozialer agiert. Ebenfalls die Möglichkeit zu alternativen Keywords (Wake up, Abfragen von Funktionen) um nicht mit den Sprachgewohnheiten des Nutzers zu brechen. 

### Entwicklung eines Recommender-System (Eric)

aufbauend auf dem Recommender-System von vorherigen Praktikum (nearest neighbour)

Prototyp zunächst in Python geschrieben(Forschungsergebnisse noch nicht implementiert)

sklearn für KNN benutzt

Datensätze vorerst vom Vorpraktikum (Testzwecke)

Trainingsdaten müssen Profile und Konfigurationen beinhalten um das Modell vom KNN zu trainieren

wird später "gefüttert" mit eigenen Trainingssätzen --> Personas/Forschungsergebnisse(Analyse Zielgruppe)

Erstellung/Auswahl eigener Profile

Vorschlag vom Recommender generieren

Nutzer kann beliebige Einstellungen übernehmen

### Herausforderungen (Max)
Zielgruppe: Wo nimmt man Daten her und was ist davon dann wichtig? Wenig vorerfahrung, Demografische Daten kaum findbar, Studien hatten meistens die gleiche Kernaussage.Neugier da, langfristig useless 

Feature Model: Welche Features sind überhaupt umsetzbar und was ist Skill und was Feature? 

Recommender System: Welche Eigenschaften der Personen sind auschlaggebend für die Konfiguration. Wie realistisch umsetzen. 

Teamarbeit: Austritt eines Teammitglied, umverteilung der Aufgaben. Aufgaben analyse, unterschiedliche Interpretationen und Kommunikationsschwierigkeiten.

Zeitmanagement: Abschätzung des Arbeitsaufwands und planen der Sprints

## Zeitplan und nächste Schritte(Max)

Ab dem 10.11.2022: Einarbeitung in frühere Arbeiten und Analyse der Zielgruppe. 
    - Recommender System und Mycroft Sprachassistent

Ab dem 15.12.2022: Feature Modell anfangen und Analyse der Anforderungen für das Recommender Systen
Ab dem 05.01.2023: Personas erstellen, weitere Ausarbeitung des Feature Modell sowie beginn des Recommender System

Die weiter geplanten Schritte sind die fertigstellung des Recommender Systems, die implementierung des Skills zum proof of concept und das ausarbeiten der Dokumentation

## Demo (Eric)

## Fragen für die Diskussion

Rücksichtahme auf Dialekte?
Welche Skilld sind sinnvoll für Senioren?
Möglicher Ausbau des Konzeptes zu einem Helfersystem, was für Funktionen?
Bessere Annahme von VAs durch Senioren, wie?