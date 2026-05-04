from tools.toolbox import input
import random

number = round(random.random() * 100)

not_solved = True

while not_solved:
    guess = int(input("Dein Guess: "))

    if guess < number:
        print("Die Zahl ist höher, versuchs nochmal")
    elif guess > number:
        print("Die Zahl ist kleiner, versuchs nochmal")
    elif guess == number:
        not_solved = False

print(f"Prima du hast die Zahl {number} erraten!")
