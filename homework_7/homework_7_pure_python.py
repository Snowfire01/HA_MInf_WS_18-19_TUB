import math

##################### 7.1 #####################

signalPressure = int(input("Please enter the signal sound pressure in pascal: "))
noisePressure = int(input("Please enter the noise sound pressure in pascal: "))

signalPressureLevel = 20 * math.log10(signalPressure/(2*math.pow(10,-5)))
noisePressureLevel = 20 * math.log10(noisePressure/(2*math.pow(10,-5)))

signalNoiseRatio = signalPressureLevel-noisePressureLevel

# Mit dem Oldenburger Satztest kann man näherungsweise bestimmen, wie viel Rauschen in einem Audiosignal enthalten sein 
# darf, damit man Sprache noch verstehen kann. Dazu werden Proband*innen mit verschiedenen SNRs konfrontiert und müssen
# jeweils angeben, was sie verstanden haben. Sind es mehr als 50% des Satzes, dann gilt der Test als bestanden und der
# Anteil des Rauschens wird erhöht. Aus einigen Tests (typischerweise 30-50) lässt sich somit ein Ergebnis mit möglichst
# geringer Varianz erzielen, das eine Schwelle für das SNR angibt, ab der der Proband weniger als 50% der Sprache verstehen
# kann. Verschiedene Quellen sind sich uneinig, wo genau der Wert für Menschen ohne Hörschädigung liegt, da das schwer
# exakt festzustellen ist. Er bewegt sich jedoch vermutlich im Bereich von -6 bis -7.1 oder knapp darum herum. Für dieses
# Programm wird der Einfachheit halber der Wert -6 angenommen.
speechComprehensible = signalNoiseRatio > -6

print(f"The signal-noise-ratio (rounded to 2 decimal places) is {round(signalNoiseRatio,2)} dB.")
print(f"That means if your signal were speech, it would probably", 
      "still" if speechComprehensible else "not", "be comprehensible.")
      
      
##################### 7.2 #####################

# Signalleistung = SL, Rauschleistung = RL
#-----------------------------------------------------------
# SNR = 10 * log10(SL/RL)
# 6.2 = 10 * log10(SL/RL)
# 0.62 = log10(SL/RL)
# 10^(0.62) = SL/RL
# 10^(0.62) * RL = SL
#-----------------------------------------------------------
# The ratio is 1 : 10^(0.62), or with a rounded value for the power approximately 1 : 4.168