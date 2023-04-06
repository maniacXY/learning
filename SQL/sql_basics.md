# [back](../index.html)

# Inhaltsangabe
- [Anomalien](#anomalien)
- [Kreuztabelle](#kreuztabelle)
- [Vergleich Excel-Datenbank](#vergleich-excel-datenbank)
- [Notes](#notes)

# Anomalien
- Löschanomalie: bei bewusstem Löschen eines Datensatzes gehen unbewusst Informationen eines anderen Datensatzes verloren
- Einfügeanomalie: führt zu Inkonsistenz bei nicht vollständiger Dateneingabe oder wenn ein Wert vergessen wird, wird gar nichts eingefügt
- Aktualisierungs-/Änderungsanomalie: Inkonsistenz der Daten wenn nicht atomar und an meheren Stellen verfügbar, somit ist nicht klar welcher Wert korrekt ist

# Kreuztabelle
Bei einer n:m-Beziehung wird eine Zwischentabelle erzeugt. 

Der Primary Key von der 1er Tabelle wird zum Foreign key der N Tabelle

# Vergleich Excel-Datenbank
		
		Excel			|		Datenbank
		---			|	----
excel ausgelegt für wenige Nutzer 	|	Datenbank für sehr viele Nutzer
keine referenzielle Integrität		|	referenzielle Integrität
					|	logging von Zugriffen
					|	feinere Benutzerverwaltung
					| 	rollbackfunction, Datenänderung erst bei commit
redundanz spielt keine Rolle		| 	redundanzen werden vermieden 
					| 	Datenbanken hat eigenes

# Notes
referenzielle Integrität: Ein FK-Wert kann nur eingetragen werden, wenn die zugehörige PK-Wert existiert

Kardinalität: n:m:1
Entity: Grundstück
