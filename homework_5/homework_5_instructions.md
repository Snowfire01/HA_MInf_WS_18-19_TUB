
# TU BERLIN | Einführung in die Medieninformatik | WS 2018/19 | Hausaufgabe 5

## Aufgabe 1 - Dezibelrechner
Schreiben Sie einen Dezibelrechner, der zwei dB-Werte addiert und die Summe der beiden Werte zurückgibt! Beachten Sie, dass Dezibel Werte logarithmisch sind und daher nicht direkt addiert werden können, sondern vor der Addition entsprechend umgerechnet werden müssen!

 - Eingabegrößen: zwei Dezibelwerte
 - Ausgabe: Die Summe der beiden Dezibelwerte

Verwenden Sie eine Logarithmusfunktion und runden Sie das Ergebnis auf zwei Nachkommastellen! Die Eingabe soll nach einer textuellen Aufforderung geschehen. Die Ausgabe soll die beiden Eingabewerte, sowie das Ergebnis als Satz darstellen.

Bsp.: 

>     Wie viel Dezibel hat der erste Summand? → 90
>     Wie viel Dezibel hat der zweite Summand? → 96
>     Die Summe aus 90.00 dB und 96.00 dB ist 96.97 dB
>     
## Aufgabe 2 - Tiefpassfilter
Beantworten Sie folgende Frage als Kommentar in dem abzugebendem Code: *"Vor der Digitalisierung wird ein Tiefpassfilter auf das Signal angewendet, der Frequenzen filtert, die höher als die halbe Abtastfrequenz sind. Welchen Sinn hat das? Erwähnen Sie dabei den Namen der entsprechenden Gesetzmäßigkeit und den des Effekts, den Sie damit verhindern (1-3 Sätze)."*

## Aufgabe 3 - WAV-Schmalbandfilter
Schreiben Sie einen Frequenzfilter für eine .wav-Datei in Python, der nur auf das Frequenzspektrum eines alten Analogtelefons zurückgreift (Schmalband). Der Filter soll alle Frequenzen unter 300 Hz und über 3.4 kHz filtern. Nach der Filterung soll das Resultat als Plot (immer mit korrekter Achsenbeschriftung!) dargestellt werden.

**Als Ressource zum Testen können Sie [speech_clean] benutzen.**

