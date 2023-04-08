# [BACK](../index.html)
# Inhaltsangabe
- [Methoden](#methoden)
	- [3-2-1 Regel](#3-2-1-regel)
- [Backup Strategien](#backup-strategien)
	- [Fifo](#fifo)
	- [Generationenprinzip](#generationenprinzip)
	- [Tuerme von Hanoi](#tuerme-von-hanoi)

# Definition
Datensicherung bezeichnet Kopieren von Daten um sie ggf wiederherstellen zu können. Elementare Maßnahme zur Datensicherheit

Vollbackup: Alles wird gesichert

Differenziell: Differenz zum letzten Voll-Backup

Inkrementell: Änderungen seit dem letzten Backup (inkrementell, diff, voll); ganze Kette muss vorhanden sein um alle Daten herstellen zu können

[TOP](#)
# Methoden
## 3-2-1 Regel
3 Backupkopien, 2 versch Datenträger (Platte, CD), 1 Kopie an einem separaten Ort (im falle elementarer Schäden)

[TOP](#)
# Backup Strategien
## Fifo
einfachste Backupstrategie. Wird 2. Datenträger langsam voll wird der erste Datenträger überschrieben

## Generationenprinzip 
*Großvater-Vater-Sohn*
Relativ veraltetse Prizip und relativ Plattenintensiv. Allerdings auch sehr sicher, da bis zu einem Jahr immer zurückgegangen werden kann. Vor allem nützlich bei RansomAngriff

4 Söhne (S1-S4) / Woche -> inkrementelle Backups

4 Väter (V1-V4) /Monat -> 1x/Woche vollBackup für die Woche

12 Großväter (G1-G12) / Jahr-> Vollbackup, gesichert für ein Jahr

## Tuerme von Hanoi
guter Kompromiss zwischen Speicher und Datensicherung. Nach dem Rätselspiel. Backupwiederherstellung die 1, 2, 4, 8 oder 16 Tage alt sind braucht aber nur 6 Bänder

1A,2B,3A,4C,5A,6B,7A,8D,9A,10B,11A,12C,13A,14B,15A,16E

01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16
--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--
A |  |A |  | A|  | A|  |A |  |A |  |A |  | A|
  |B |  |  |  | B|  |  |  |B |  |  |  |B |  |
  |  |  |C |  |  |  |  |  |  |  | C|  |  |  |
  |  |  |  |  |  |  |D |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |E
 


