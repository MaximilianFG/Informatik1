from tools.toolbox import input

CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def to_bandit_language(text):
    """Übersetzt einen Text in Räubersprache"""
    result = ""
    for letter in text:
        if letter.lower() in CONSONANTS:
            result += letter + "o" + letter.lower()
        else:
            result += letter
    return result


def from_bandit_language(text):
    """Übersetzt Räubersprache zurück in Klartext"""
    result = ""
    i = 0
    while i < len(text):
        if (
            i + 2 < len(text)
            and text[i].lower() in CONSONANTS
            and text[i + 1] == "o"
            and text[i + 2].lower() == text[i].lower()
        ):
            result += text[i]
            i += 3
        else:
            result += text[i]
            i += 1
    return result


options = int(input("Möchtest du in Räubersprache übersetzen (1) oder zurück (2)? "))

if options == 1:
    text_input = input("Bitte gib den Klartext ein der übersetzt werden soll: ")
    finished_text = to_bandit_language(text_input)
    print(f"Übersetzung in Räubersprache: {finished_text}")
elif options == 2:
    text_input = input("Bitte gib den Räubersprache-Text ein: ")
    finished_text = from_bandit_language(text_input)
    print(f"Übersetzung zurück in Klartext: {finished_text}")
