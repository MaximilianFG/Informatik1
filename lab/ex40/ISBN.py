from tools.toolbox import input

number = str(input("Bitte gib die 9-Stellige Nummer an: "))
isbn_total = 0
counter = 0

for x in number:
    counter += 1
    isbn_test = int(x) * (10 - counter + 1)
    isbn_total += isbn_test

check_number = 11 - (isbn_total % 11)
if check_number == 10:
    check_number = "X"

print(f"Prüfziffer ist: {check_number}")
