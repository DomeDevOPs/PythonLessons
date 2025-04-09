artikel = "Laptop"
preis = 999.99
menge = 3
gesamtpreis = preis * menge

print("Artikel: {}\nPreis: {:.2f} €\nMenge: {}\nGesamtpreis: {:.2f} €".format(artikel, preis, menge, gesamtpreis))


#####andere Variante
artikel = input("gib artikel an")
preis =  float(input("gib preis an"))
menge = int(input("(gib menge an"))

print(f"Artikel: {artikel}")
print(f"preis: {preis}")
print(f"menge: {menge}")
print(f"gesamtpreis: {gesamtpreis}")

