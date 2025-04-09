betrag_euro = float(input("Bitte gib den Euro-Betrag ein: "))
wechselkurs = 1.10  # Beispielsweise 1 EUR = 1.10 USD
betrag_usd = betrag_euro * wechselkurs
print(f"{betrag_euro} EUR sind {betrag_usd:.2f} USD.")
