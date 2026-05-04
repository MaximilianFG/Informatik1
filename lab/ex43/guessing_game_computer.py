from tools.toolbox import input

print("Denke dir eine Zahl zwischen 1 und 100 aus.")
print("Der Computer wird sie erraten.")

low = 1
high = 100
not_solved = True

while not_solved:
    guess = (low + high) // 2
    response = (
        input(
            f"Ist die Zahl {guess}? Antworte mit 'h' für höher, 'k' für kleiner oder 'j' für ja: "
        )
        .strip()
        .lower()
    )

    if response == "h":
        low = guess + 1
    elif response == "k":
        high = guess - 1
    elif response == "j":
        not_solved = False
        print(f"Der Computer hat deine Zahl {guess} erraten!")
    else:
        print("Bitte gib 'h', 'k' oder 'j' ein.")

    if low > high and not_solved:
        print("Da stimmt etwas nicht. Bitte überprüfe deine Antworten.")
        break
