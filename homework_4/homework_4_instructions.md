# TU BERLIN | Einführung in die Medieninformatik | WS 2018/19 | Hausaufgabe 4

## Aufgabe 1 - WAV Dateigröße berechnen

### 1.1  Programmcode schreiben
Schreiben Sie einen Rechner der unter Verwendung von Auflösung, Abtastrate, der Anzahl der Kanäle und der Spieldauer die Mindestdateigröße einer unkomprimierten .wav-Datei berechnet!

 - Eingabegrößen: Auflösung, Abtastrate, Anzahl Kanäle & Spieldauer
 - Ausgabe: Dateigröße in MiB

Verwenden Sie die Befehle input() und print() um ein Dialogsystem zu entwickeln! Jede der vier Eingabevariablen soll in einer separaten Eingabeaufforderung erfragt werden.

Bsp.: 

>     Wie hoch ist die Abtastrate (in Hz)? → 44100 
>     Wie hoch ist die Bitrate (in kbit/s)? → 320

All diese Inputs sollen nun verwendet werden um die zu erwartende Dateigröße einer .wav-Datei zu errechnen. Das Ergebnis soll in Mebibyte (https://en.wikipedia.org/wiki/Mebibyte) angegeben und auf drei Nachkommastellen gerundet werden.

**Als Ressource zum Testen können Sie [speech_clean] benutzen.**

### 1.2 Textaufgabe
Weshalb ist eine tatsächliche Datei auf Ihrem Computer immer ein wenig größer als die von den hier betrachteten Parametern abhängige Dateigröße? Schreiben Sie die Antwort als Kommentar in den Code!

## Aufgabe 2 - Morse-Encoder

Übersetzen Sie einen natürlichsprachlichen Satz in Morsecode. Verwenden Sie `.` für “kurz”, `-` für “lang” und `/` für ein “Leerzeichen”. Es müssen nur alle 26 Buchstaben betrachtet werden, die Behandlung von Sonderzeichen und Ziffern ist nicht notwendig; diese Zeichen sollen ignoriert werden. Der zu kodierende Satz soll wie in Aufgabe 1 durch eine Kommandozeilenabfrage eingegeben und als übersetzter Zeichenstring auf der Konsole ausgegeben werden.

 - Eingabe: Ein natürlichsprachlicher Satz
 - Ausgabe: Eine Morsecode-Zeichenkette

