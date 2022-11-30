# MCI_Sprachinteraktion

## Zielstellung
### Kontext 
 Entlang der aktuell stark bearbeiteten Forschungsfelder der Künstlichen Intelligenz und
der natürlich-sprachlichen Interaktion entwickelt sich der Bereich der Robotik fernab von Indust-
rierobotern in schnellem Tempo weiter. Insbesondere die Bereiche der Sozialen Assistenzroboter
(SARs) und Mensch-Roboter-Interaktion bieten allerdings noch zahlreiche offene technische und
auch anwendungsbezogene Fragen.
Ein zunehmender Bedarf an SARs erschließt sich im Umfeld von Menschen mit Beeinträchtigun-
gen, Senioren sowie im Altenpflegebereich. SARs könnten hier eingesetzt werden, um die Selbstän-
digkeit und Selbstbestimmtheit der Nutzenden zu fördern. Gleichzeitig können solche Assistenz-
systeme dazu beitragen, den personell angespannten Pflegebereich zu entlasten.
Bisherige SARs verfügen noch nicht über einen breiten Funktionsumfang, um verschiedentliche
Anwendungsfälle abzudecken und die Entwicklung von Software für SARs ist mangels plattform-
übergreifender Lösungen teuer. Eine besondere Herausforderung ist außerdem die Umsetzung
einer gebrauchstauglichen Mensch-Roboter-Interaktion. Idealerweise wird diese benutzenden-
zentriert entwickelt und erlaubt eine automatische Adaption an die Anforderungen der Nutzenden,
den Anwendungskontext und sich dynamisch ändernde Faktoren.
Ein Ansatz zur Lösung der beschriebenen Probleme kann die Entwicklung einer gemeinsamen An-
wendungsarchitektur, basierend auf den Methoden aus der Softwarevariabilität, sein. Diese um-
schließt neben den implementierten Anwendungsfällen auch die Interaktion und ermöglicht daher
die erforderliche Adaptivität.

### Projektziel
 Bezogen auf den o. g. Kontext konzentriert sich die Aufgabe dieses Komplexprakti-
kums auf die Anwendung der Softwarevariabilität zur Umsetzung von individualisierbarer Inter-
aktion (automatisch, adaptiv). Zur weiteren Fokussierung beschränken wir uns zudem auf die In-
teraktion mittels nur einer Modalität: Sprachinteraktion (also über ein Voice User Interface, VUI).
Das Ziel beschreiben wir folgendermaßen: Entwicklung eines für die Zielgruppe älterer Menschen
anwendbaren Adaptionskonzepts für Sprachinteraktion basierend auf der Konfiguration von Fea-
ture-Modellen und der Konfigurationsauswahl durch ein Recommender-System.

Hieraus ergeben sich die folgenden Teilziele:

1. Vertraut machen mit den bestehenden Projektergebnissen: Die Ergebnisse dieses KP sol-
len Sprachinteraktion adaptierbar machen, sodass die Architektur eines Sprachassistenten
benötigt wird. Hierfür darf das KP zur Mycroft-Implementierung (wurde bereitgestellt) ver-
wendet werden oder aber auf Amazons Alexa (ggf. im Zusammenspiel mit RASA) zurückge-
griffen werden. Gleichzeitig soll die Adaptierbarkeit durch eine Konfiguration von Feature-
Modellen ermöglicht werden, welches durch ein Recommender-System ausgewählt wird.
Hierfür soll auf die Ergebnisse des KPs zum Deep-Learning-Ansatz (ebenfalls bereitgestellt)
zurückgegriffen werden.
2. Entwicklung eines Feature-Modells zur Abbildung von Sprachvarianten für einen Skill:
Mit dem Wissen über das benötigte Input-Feature-Modell sollte sich ein Feature-Modell ent-
werfen lassen, mit dem variable Sprachinteraktion dargestellt werden kann, die sich zur auto-
matisierten Konfiguration eignet. Die Entwicklung des Feature-Modells muss auf geeignete,
wissenschaftliche Weise erfolgen, also hauptsächlich basierend auf wissenschaftlicher Litera-
turarbeit. Dieser Teil ist in der Projektdokumentation nachvollziehbar darzustellen. Im Ergeb-
nis können zwei Modelle entstehen: Einerseits ein sog. Nutzermodell zur Beschreibung von
Nutzenden und andererseits ein Variabilitätsmodell zur Beschreibung der Sprachinteraktion.
3. Entwicklung geeigneter Trainingsdaten: Zur Lösung des sog. Kaltstartproblems werden
initiale Trainingsdaten für das Recommender-System benötigt. Hierfür gibt es unterschiedli-
che zulässige Vorgehensweisen. Ideal ist ein solches Vorgehen, bei dem im Ergebnis mög-
lichst viele plausible Daten gesammelt werden. Beispielsweise lassen sich geeignete Personas
recherchieren oder selbst erstellen, aus deren Perspektive jeweils mehrere geeignete Konfi-
gurationen entworfen werden. Die Personas selbst lassen sich mittels des Nutzermodells be-
schreiben (sog. Nutzerprofil).
4. Exemplarische Anwendung der Daten mittels des Recommenders sowie eines Sprach-
assistenten: Die bestehenden KP-Projekte dienen als Grundlage, das entworfene Modell und
die vorbereiteten Trainingsdaten auszutesten und zu demonstrieren. Hierfür muss ein sog.
Skill für den Sprachassistenten entwickelt werden, der in der Interaktion mit dem Nutzenden
auf eine vorgeschlagene Konfiguration zurückgreifen wird. Damit ein Vorschlag passend für
den Nutzenden unterbreitet werden kann, muss das System die Berücksichtigung von Nut-
zerprofilen unterstützen.


Beachten Sie bitte auch die folgenden Punkte zur Bearbeitung des Projekts:
* Arbeiten Sie sich gründlich in die Materie ein.
    * Wie sind Feature-Modelle aufgebaut und wie funktioniert die Konfiguration des-
sen?
    * Wie funktioniert Deep-Learning und wie könnte es eingesetzt werden, um ein
Recommender-System für die Konfiguration von Feature-Modellen zu entwickeln?
    * Wie programmiert man einen Skill für Sprachassistenten (VUI und Logik als Ba-
ckend)?
* Planen Sie Ihre Vorgehensweise gründlich und wenden Sie Methoden des Softwaremana-
gements (Projektmanagement für Softwareprojekte) an.
* Achten Sie auf gleichmäßige Verteilung der Arbeitsaufgaben im Team. Verteilen Sie dazu
beispielsweise Rollen bzw. Verantwortlichkeiten.
* Nutzen Sie übliche Mittel der Zusammenarbeit, bspw. Versionierungswerkzeuge wie Git.
* „Erfinden Sie das Rad nicht neu“: Schauen Sie, inwiefern bestehende Lösungen und Me-
thoden genutzt werden können, um die Aufgabe zu lösen.
* Dokumentieren Sie Ihre Arbeit (Planung, Vorgehensweise, Lösungsansatz, Beschreibung
der Lösung, ggf. Bedienungshinweise und Installationsanweisungen)
* Bereiten Sie zum Abschluss eine Präsentation Ihrer Ergebnisse vor.
* Teil der Abgabe zum Projekt ist das Projektergebnis selbst, die schriftliche Dokumenta-
tion und die Projektpräsentation.