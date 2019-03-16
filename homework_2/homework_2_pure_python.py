import numpy as np

##################### 2.1 #####################

results = [];

for x in range(0,12):
    results.append(int(input("Ergebnis Prüfung %d: " % (x+1))))

print()

total = 0;

for result in results:
    if result >= 25:
        total += result

# Ausgehend davon, dass bei der Notenvergabe die Punkte immer abgerundet werden (was wir nicht wissen können, 
# das Prinzip ist aber gleich)
finalResult = int(total / (1200/15))

print("Final result: %d points" % finalResult)

# Negative Bonuspunkte kann es nicht geben
bonusPoints = int(finalResult - 5 if finalResult - 5 > 0 else 0)

print("That's %d bonus points!" % bonusPoints)


##################### 2.2 #####################

personen = np.matrix("100,175,210;90,160,150;200,50,100;120,0,310")
preise = np.matrix("0.0298;0.0390;0.0199")

ausgaben = np.dot(personen, preise)
print(ausgaben)