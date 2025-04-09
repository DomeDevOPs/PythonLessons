
input("Hallo. Bitte wählen Sie eine Option: Weiter mit der Eingabetaste ") #begruessung
print("Bitte wählen Sie eine dieser Optionen: A für die Addition, S für die Subtraktion,\n M für Multiplikation,D für Division,0 für Ergebnis und Beenden ") #optionen

auswahl = str(input("A,S,M,D oder 0: ")) # auswahl
zahl = 25

summe = 0

if auswahl == "A":
    print("Ok. Addition. Gib deine erste Zahl ein:",zahl)
elif auswahl == "S":
    print("Ok.Subtraktion. Gib deine erste Zahl ein:",zahl)
elif auswahl == "M":
    print("Ok. Subtraktion. Gib deine erste Zahl ein:", zahl)
elif auswahl == "D":
    print("Ok. Division. Gib deine erste Zahl ein:", zahl)
elif auswahl != "0":
    print("Die Summe aller Zahlen ist:", summe, "Bis bald!")



# Solange die Zahl nicht 0 ist, machen wir weiter
# while zahl != 0:
#     # Wir rechnen die Zahl zur Summe dazu
#     summe = summe + zahl
#
#     # Wir fragen nach der nächsten Zahl
#     zahl = int(input("Bitte gib eine weitere Zahl ein (0 zum Beenden): "))

# Wenn der Benutzer 0 eingibt, sind wir fertig
# Jetzt zeigen wir das Ergebnis
#print("Die Summe aller Zahlen ist:", summe)


#####andere Variante
#x = int(input("eingabe zahl 1"))
# = int(input("eingabe zahl 2"))

#summe = x + y
#rint(summe)