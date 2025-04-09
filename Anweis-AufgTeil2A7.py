name = input("Bitte gib deinen Namen ein: ")
alter = int(input("Bitte gib dein Alter ein: "))

aktuelles_jahr = 2023  # oder du könntest das Jahr mithilfe von datetime erhalten
jahr_100 = aktuelles_jahr + (100 - alter)
print(f"{name}, du wirst im Jahr {jahr_100} 100 Jahre alt.")
