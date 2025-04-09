jahr = int(input("gib jahr an)"))

if (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0):
    print(f"{jahr} ist ein schaltjahr")

else:
    print(f"{jahr} kein schaltkajr")


