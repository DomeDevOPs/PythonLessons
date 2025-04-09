
# Wir starten mit dem Passwort
PW = "1234R"

# Wir fragen den Benutzer nach dem Passwort
PW_Eingabe = str(input("Bitte gib dein Passwort ein"))

# Solange das PW nicht richtig ist, fragen wir erneut nach der Eingabe
while PW_Eingabe != PW:

    # Wir fragen erneut nach Eingabe
    PW_Eingabe = input("Bitte gib dein Passwort ein: ")


# Wenn das richtige Passwort eingegeben wurde,geben wir folgendes aus
print("Danke für die Eingabe")
print(PW_Eingabe)