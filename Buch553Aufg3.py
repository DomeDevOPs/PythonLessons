
zahl1 = int(input("Geben sie 1. Zahl an: "))
zahl2 = int(input("Geben sie 2. Zahl an: "))
zahl3 = int(input("Geben sie 3. Zahl an: "))

if zahl1 > zahl2 and zahl1 > zahl3:
    print(f"{zahl1}=zahl1 ist die größte Zahl")
elif zahl2 > zahl1 and zahl2 > zahl3:
    print(f"{zahl2}=zahl2 ist die größte Zahl")
else:
    print(f"{zahl2}=zahl2 ist die größte Zahl")


