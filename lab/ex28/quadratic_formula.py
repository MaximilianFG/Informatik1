from tools.toolbox import input

a = int(input("Bitte gib a an: "))
b = int(input("Bitte gib b an: "))
c = int(input("Bitte gib c an: "))

if b**2 - 4 * a * c < 0:
    print("Es gibt keine Lösung")

elif b**2 - 4 * a * c > 0:
    x1 = (-b + (b**2 - 4 * a * c) ** 0.5) / 2 * a
    x2 = (-b - (b**2 - 4 * a * c) ** 0.5) / 2 * a
    print(f"Hat zwei Lösungen: x1 = {x1} , x2 = {x2}")

else:
    x1 = (-b) / 2 * a
    print(f"Hat eine Lösung: x = {x1}")
