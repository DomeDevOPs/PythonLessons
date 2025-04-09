###aufgabenblatt Teil 3
#aufgaben 1 bis 7

#gerade zahlen von 1-20 ausgeben
#
for i in range(10):

    if i%2 == 0:
        print(i)

# jeder zweite schritt
for i in range(0,20,2):   # range; start; stop; schritt
    print(i)

# zählt solange wie i kleiner ist als der stop!

# jeder 5 schritt
for i in range(5,25,5):   # range; start; stop; schritt
    print(i) # zählt solange wie i kleiner ist als der stop

#sternenmuster

for i in range(1,6,1):
    print("*****")

#ausgabe rückwärts

for zahl in range (10, 0, -1):
    print(zahl)


