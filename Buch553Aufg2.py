##schreibe ein programm,dass nach eingabe zweier gleitkommazahlen,die kleinste zahl ausgibt

# Benutzer nach zwei Gleitkommazahlen fragen
zahl1 = float(input("Bitte geben Sie die erste Gleitkommazahl ein: "))
zahl2 = float(input("Bitte geben Sie die zweite Gleitkommazahl ein: "))
#________________________________________________________________________________
# Kleinste Zahl bestimmen und ausgeben
#kleinste_zahl = zahl1 if zahl1 < zahl2 else zahl2

#print(f"Die kleinste Zahl ist: {kleinste_zahl}")
#_________________________________________________________________________________


#####################
def zahlen_sortieren(zahl1,zahl2):
    if zahl1 < zahl2:
        print(f"Die kleinste Zahl ist: {zahl1}")

    else:
        print(f"Die kleinste Zahl ist: {zahl2}")

zahlen_sortieren(zahl1,zahl2)                          ####Aufruf d. Funktion

#___________________________________________________________________________________
def kleinste_zahl():
    zahl1 = int(input("Geben Sie die erste Zahl ein: "))
    zahl2 = int(input("Geben Sie die zweite Zahl ein: "))
    if zahl1 < zahl2:
        print(f"Die kleinste Zahl ist: {zahl1}")
    else:
        print(f"Die kleinste Zahl ist: {zahl2}")

kleinste_zahl()

zahl1 = int(input("Geben Sie die erste Zahl ein: "))
zahl2 = int(input("Geben Sie die zweite Zahl ein: "))
if zahl1 < zahl2:
        print(f"Die kleinste Zahl ist: {zahl1}")
else:
        print(f"Die kleinste Zahl ist: {zahl2}")