

# TU BERLIN | Einführung in die Medieninformatik | WS 2018/19 | Hausaufgabe 9

## Einleitung

Sie haben sich in den letzten Übungen mit verschiedenen Farbräumen beschäftigt. Hier haben Sie gelernt, dass ein Bild aus einzelnen Pixeln besteht. Weiterhin haben Sie geübt, ein Bild einzulesen und es auf verschiedenen Farbebenen darzustellen und zu manipulieren.

![Abbildung 1: Schema - Farbräume](https://artsdocbox.com/docs-images/72/66627938/images/4-1.jpg)

In dieser Hausaufgabe sollen Sie ein Bild einlesen und einen Farbfilter erstellen. Wir haben den Filter den Namen ColorSplash gegeben. Desweiteren soll der Filter vier unterschiedliche Modi besitzen. Die Funktion des Filters soll abschließend mittels eines Bild-Plots überprüft werden. Dafür müssen Sie in jupyter code schreiben. Bitte kommentieren Sie den Code angemessen! 
Benötigt werden:

 - Hostskript für die Bildbearbeitung
 - Funktion in separater Datei für den Farbfilter

## Aufgabe 1 - Hostskript erstellen

Erstellen Sie ein Host-Skript mit jupyter! Hier soll der Name der Bild-Datei eingegeben werden und die Funktionen zur Farbfilterung aufgerufen werden. Desweiteren soll im Host-Skript der Filtermodus bestimmt werden. Dies kann über eine Nutzerabfrage passieren oder festgelegt werden. Denken Sie daran, die externen Funktionen, entsprechend zu importieren! 
Abschließend soll im Host-Skript der Befehl stehen, der das gefilterte Bild anzeigt. Es soll kein Subplot erstellt werden, sondern es soll nur das Bild angezeigt werden, welches gerade erstellt/- gefiltert wurde. Das Ergebnis der vier Filter-Modi soll (beispielhaft) wie folgt aussehen:

![Abbildung 2: Orginales Bild und YCbCr-Farbmodell ==> Mod’1.Quadrant’, Mod’2.Quadrant’, Mod’3.Quadrant’, Mod’4.Quadrant’; ©Album-Cover AHAB - The Boats of the Glen Carrig](https://github.com/Snowfire01/HA_MInf_WS_18-19_TUB/blob/master/resources/homework_9_result_example.png?raw=true)

## Aufgabe 2 - ColorSplash-Filter

Der ColorSplash-Filter ist ein Bildfilter, der nur bestimmte Farbkomponenten zulässt und alle anderen Farbwerte aus dem Bild entfernt (Siehe Abb. 2). Um dies zu erreichen müssen zuerst die Helligkeitswerte von den Farbwerten getrennt werden. Dies sollte bereits in der Hausaufgabe Nr. 8 selbst nachvollzogen werden. Für diese Aufgabe können Sie ihre eigene Farbraum-Transformation verwenden oder die mitgelieferte Funktionalität (`var = bild.convert(’YCbCr’)`).

## Wichtige Hinweise
Der Farbfilter soll vier Modi haben:

 1. es sollen nur Farben im Bild zugelassen werden, die **im ersten Quadranten des YCbCr-Farbmodells** enthalten sind
 2. es sollen nur Farben im Bild zugelassen werden, die **im zweiten Quadranten des YCbCr-Farbmodells** enthalten sind
 3. es sollen nur Farben im Bild zugelassen werden, die **im dritten Quadranten des YCbCr-Farbmodells** enthalten sind
 4. es sollen nur Farben im Bild zugelassen werden, die **im vierten Quadranten des YCbCr-Farbmodells** enthalten sind

Erinnern Sie sich bitte an die Aufgabe zum Schmalbandfilter (Hausaufgabe 5). Dort haben wir unerwünschte Frequenzen auf 0 gesetzt. 
Um nun unerwünschte Farbwerte zu entfernen, müssen die entsprechenden Werte aus der Matrix neutralisiert werden. Dies erreicht man nicht, indem man sie auf 0 setzt, wie bei Audiofrequenzen, sondern indem man sie auf den Mittelwert der entsprechenden Achsen des YCbCr-Farbraums setzt.
Sehen Sie sich dafür das Farbraummodell für YCbCr an und welche Werte die Kanäle (bei 8 bit) annehmen können.
