from tools.toolbox import input

total = 0.0
number_count = float(input("Wie viele Zahlen möchtest du eingeben? "))
x = number_count

while number_count > 0:
    numbers = float(input(f"Bitte gib die {number_count:.0f}. positive Zahl ein: "))
    total += numbers
    number_count -= 1

mean = total / x
print(f"Der Durchschnitt der eingegebenen Zahlen ist: {mean}")
