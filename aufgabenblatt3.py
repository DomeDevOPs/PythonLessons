###aufgabenblatt Teil 3
#aufgaben 8 bis 10

namen = ["Anna", "Max", "Tom", "Lisa"]
print(namen)

namen.append("Maria")
print("nach append",namen)

namen.remove("Tom")
print("nach remove",namen)

print("length:",len(namen))

#aufgaben 9

zahlen = [5, 3, 8, 1, 2]
zahlen.sort()
print("aufsteigend",zahlen)

zahlen = [5, 3, 8, 1, 2]
zahlen.sort()
print("aufsteigend",zahlen)
zahlen.sort(reverse=True)
print("absteigend" ,zahlen)
zahlen.reverse()
print("reverse" ,zahlen)

#aufgabe 10
zahlen = [1,2,3,4,5]
print(zahlen)
zahlen.insert(len(zahlen), 6)
print("append 6", zahlen)
zahlen.insert(0, 0)
print("insert 0", zahlen)

zahlencount = zahlen.count(3)
print("die 3 kommt", zahlencount, "oft vor")

#aufgabe 11

liste =  [10,20,30,40,50]
for zahl in liste:  # Inhalt von Zahl wird mit Inhalt von liste ersetzt
    print(zahl)

#aufgabe 12

summe = 0
liste =  [10,20,30,40,50]
for zahl in liste:
    summe += zahl  # Inhalt von Zahl wird mit Inhalt von liste ersetzt
    print(zahl)

summe = 0
liste =  [10,20,30,40,50]
for zahl in liste:
    summe += zahl  # Inhalt von Zahl wird mit Inhalt von liste ersetzt
    print("partiale summe", summe)
print("totale summe", summe)

#aufgabe 13
h = "hallo"
for i in h:
    print(i)  # druckt auch eine Reihe aus( erst h, dann a usw) es bleibt eine \n
              # schleife hallo ist eine auflistung kein wort für die schleife

#aufgabe 14
liste = [17,2,14,6,9]
for wert in liste:
    if wert > 10:
        print("aus der liste:",liste, "größer als 10:", wert)

#aufgabe 15
liste = [17,2,14,6,9]
for i in liste:
    print("index:", liste.index(i), "| wert aus index",i)

#aufgabe 16
liste = [10,20,30,40,50]
for index, wert in enumerate(liste):
    print(f"index {index},wert {wert}")











