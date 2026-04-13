from tools.toolbox import input

firstname = str(input("Vorname eingeben "))
lastname = str(input("Nachname eingeben "))
len(lastname)

print(f"Darf ich dich {firstname[0]}. {lastname[0]}. nennen?")
print(
    f'Dein Geheimname ist: "{lastname[len(lastname) - 1].upper() + lastname[-2::-1].lower()}{firstname[::-1].lower()}"'
)
