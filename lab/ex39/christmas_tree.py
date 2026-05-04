import random

from tools.toolbox import input

height = int(input("Höhe: "))
width = 2 * height - 1

for y in range(1, height + 1):
    stars = "*" * (2 * y - 1)
    new_line = ""
    for letter in stars:
        if letter == "*" and random.random() < 0.15:
            new_line += "0"
        else:
            new_line += letter
    print(new_line.center(width))

print("|".center(width))
print("=" * width)
