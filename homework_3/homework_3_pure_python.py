##################### 3.1 #####################

import math

def getEntropy(dictionary):
    retVal = 0

    for i in dictionary:
        xa = math.log2(1/dictionary[i])
        pa = dictionary[i]
        retVal += pa * xa
    
    return retVal

dict = {
    "dreieck": 0.2,
    "summe": 0.125,
    "omega": 0.2,
    "k": 0.345,
    "phi": 0.13
}

print(f"Die Entropie der Zeichen ist: {getEntropy(dict)}")


##################### 3.2 #####################

# Beim Huffman-Code sind keine Trennzeichen nötig, da kein kein Codewort mit dem Präfix eines anderen Codewortes 
# beginnen kann. Codiert man bspw. mit Nullen und Einsen, so enthält kein Codewort mehr als eine Null. Das Wort
# mit der höchsten Wahrscheinlichkeit besteht aus einer Null und dasjenige mit der geringsten Wahrscheinlichkeit
# besteht als einziges nur aus Einsen. Alle anderen beginnen mit Einsen und enden mit einer Null. Die Null markiert
# somit das Ende eines Codewortes. Das wahrscheinlichste Codewort erkennt man daran, dass es als einziges zulässt,
# dass zwei Nullen nacheinander stehen. Das unwahrscheinlichste Codewort erkennt man daran, dass die maximale Länge
# eines Codeworts mit der Anzahl an aufeinander folgenden Einsen überchritten wird, ohne, dass eine Null dazwischen
# stand. Somit kann man immer Wörter voneinander trennen, ohne gesonderte Trennzeichen einführen zu müssen.
# Der verwendete Codebaum muss zur Dekodierung deshalb vorliegen.


##################### 3.3 #####################

# 3.1:
# Menschliche Sprache hat einen maximalen Frequenzbereich zwischen 3.5kHz und 4 kHz. Das Abtasttheorem besagt, dass für eine
# genaue Rekonstruktion ein Signal mindestens mit dem doppelten seiner maximalen Frequenz abgetastet werden muss. 
# Bei einem Telefonat muss die Abtastrate also 2 * 4kHz (also 8 kHz) betragen. 

# 3.2:
# Da der Mensch Töne bis 20 kHz hört, muss nach dem Abtasttheorem zur perfekten Aufnahme von Musik die Abtastrate
# mindestens 40 kHz betragen (2 * 20kHz).
# Üblicherweise gibt es einen Tiefpassfilter, der weitere Störungen durch zu hohe Frequenzen vermeidet indem er sie dämpft.
# Da dies in der Praxis nicht immer ideal funktioniert, wird ein Übergangsbereich von 2.05 kHz bzw. 4 kHz ausgewiesen, der 
# bei der Berechnung der Abtastrate auf die maximale Hörfrequenz des Menschen angerechnet werden muss. Somit ergibt sich 
# die Abtastrate von 44.1 kHz aus der Rechnung (20kHz + 2.05kHz) * 2 und die Abtastrate von 48 kHz aus aus der Rechnung 
# (20kHz + 4kHz) * 2.