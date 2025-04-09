int = 20             # Ganze Zahl
float = 20.1         # Fliesskomma Zahl
#string = "a" oder "hallo du"  # Zeichenfolge oder einzelne Zeichen, auch Literale genannt
Bool = True,  False
################################################################################
name = "Hugo"        # Variable mit dem Wert Hugo
Waehrung = "Euro"    # Variable mit dem Wert Euro

################################################################################
_age = 30

#################################################################################
wert = 10
mein_variable = "Hallo"
#de = python

#################################################################################
x = 10

def aendere_x():
    x = 5


print(x)
aendere_x()          # Aufruf / Funktionsaufruf
print(x)

##################################################################################
x = 10

def aendere_x():
    global x                  #Aufruf auf die globale Variable (hier x = 10) aus der Funktion heraus
    x = 5
    print(x)

print(x)
aendere_x()
print(x)
####################################################################################
aufgabe 5:

input()
###################################################################################
input("wie heisst du?")
###################################################################################
input("wie alt bist du?")
###################################################################################
name = input("wie heisst du?")  # so speichert man den namen in der variablen Name

#Ausgabe dann über den print() befehl--->

print("mein name lautet",name)
#####################################################################################
