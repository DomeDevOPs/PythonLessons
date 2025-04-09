
# Wir starten mit der Summe 0
summe = 0

# Wir fragen den Benutzer nach der ersten Zahl
zahl = int(input("Bitte gib eine Zahl ein (0 zum Beenden): "))

# Solange die Zahl nicht 0 ist, machen wir weiter
while zahl != 0:
    # Wir rechnen die Zahl zur Summe dazu
    summe = summe + zahl

    # Wir fragen nach der nächsten Zahl
    zahl = int(input("Bitte gib eine weitere Zahl ein (0 zum Beenden): "))

# Wenn der Benutzer 0 eingibt, sind wir fertig
# Jetzt zeigen wir das Ergebnis
print("Die Summe aller Zahlen ist:", summe)

