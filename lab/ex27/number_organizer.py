from tools.toolbox import input

n1 = int(input("Bitte gib die erste Zahl an: "))

n2 = int(input("Bitte gib die zweite Zahl an: "))

n3 = int(input("Bitte gib die dritte Zahl an: "))

if n1 <= n2:
    if n1 <= n3:
        print(f"{n1} , {n2} , {n3}")

    else:
        print(f"{n3} , {n1} , {n3}")

elif n2 <= n3:
    if n3 <= n1:
        print(f"{n2} , {n3} , {n1}")

    else:
        print(f"{n2} , {n1} , {n3}")

else:
    if n1 <= n2:
        print(f"{n3} , {n1} , {n2}")

    else:
        print(f"{n3} , {n2} , {n1}")
