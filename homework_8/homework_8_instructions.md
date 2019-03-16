
# TU BERLIN | Einführung in die Medieninformatik | WS 2018/19 | Hausaufgabe 8

## Einleitung

In der Vorlesung haben Sie von verschiedenen Farbräumen gehört.

![Abbildung 1: Schema - Farbräume](https://artsdocbox.com/docs-images/72/66627938/images/4-1.jpg)

In dieser Hausaufgabe sollen Sie ein Bild einlesen und die Werte vom RGB-Farbraum in der YCbCr-Farbraum übertragen. Desweiteren sollen Sie die einzelnen Komponenten des YCbCr-Farbraums in einem subplot getrennt darstellen. Bitte kommentieren Sie den Code angemessen!
Benötigt werden:

 - Hostskript für die Bildbearbeitung
 - Funktion in separater Datei für die Berechnung RGB --> YCbCr
 - Funktion in separater Datei für die Berechnung YCbCr--> RGB

## Aufgabe 1 - Hostskript erstellen

Erstellen Sie ein Host-Skript mit jupyter! Hier soll die Bild-Datei eingelesen und die Funktionen zur Farbraumtransformation aufgerufen werden. Denke Sie daran, die externen Funktionen entsprechend zu importieren! Im Host-Skript soll weiterhin der subplot erstellt werden. Das Ergebniss soll wie folgt aussehen:

![Abbildung 2: Org. Bild, Y-Kanal, CB-Kanal, CR-Kanal](https://github.com/Snowfire01/HA_MInf_WS_18-19_TUB/blob/master/resources/homework_8_result_example.png?raw=true)

## Aufgabe 2 - RGB zu YCbCr

Schreiben Sie eine Funktion die aus den RGB-Werten des eingelesenen Bildes die entsprechenden YCbCr-Werte berechnet! Dafür muss die Funktion die RGB-Werte als Eingangsparameter bekommen. Speichern Sie die berechneten Werte unter Verwendung von aussagekräftigen Variablennamen ab! Benutzen Sie dafür **nicht** die mitgelieferten Transformation-Funktionen, sondern berechnen sie die YCBCR-Werte über die nachfolgende Formel:

    Y    /  16 \           /  65.481  128.553   24.966 \   / R \
    CB = | 128 | + 1/256 * | -37.945  -74.494  112.439 | * | G |
    CR   \ 128 /           \ 112.439  -18.285  -18.285 /   \ B /

## Aufgabe 3 - YCbCr zu RGB
Schreiben Sie eine zweite Funktion, die aus den YCbCr-Werten des Bildes wieder die entsprechenden RGB-Werte berechnet! Hierfür müssen der Funktion die YCbCr-Werte übergeben werden und die RGB-Werte sollen zurückgegeben werden. Benutzen Sie auch hier **nicht** die mitgelieferten Transformation-Funktionen, sondern berechnen sie die RGB-Werte über die nachfolgende Formel:

    R   / 1.000   0.000   1.400 \   /    Y   \
    G = | 1.000  -0.343  -0.711 | * | CB-128 |
    B   \ 1.000   1.765   0.000 /   \ CR-128 /

## Wichtige Hinweise
Es gilt vor jeder Berechnung zu beachten, dass die Bilder-Matrizen in „float“ und vor der Ausgabe auf dem Bildschirm wieder zurück in „uint8“ umgerechnet werden müssen! 

 - `value.astype(np.float)`
 - `value.astype(np.uint8)`

Weiterhin ist zu beachten, dass die einzelnen Layer (Y, CB, CR) nicht ohne weiteres zu plotten sind! Sie müssen für einen Plot auf einem Bildschirm erst wieder als RGB-Werte interpretiert, also umgerechnet werden. Dies erreicht man dadurch, dass die ungewünschten Kanäle, vor der Umrechnung zu RGB, auf den Mittelwert des entsprechenden Farbraums gesetzt werden. 

Die angebenen Formeln zeigen Vektoren und Matrizen und keine Beträge der Werte, o.ä. an! Es muss also Vektoren- und Matrizenrechnung durchführt werden.
