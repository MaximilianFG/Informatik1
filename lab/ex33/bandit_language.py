from tools.toolbox import input

CONSONANTS = "bcdfghjklmnpqrstvwxyz"
index_of_text = 0
finished_text = ""
options = int(input("Möchtest du in Räubersprache übersetzten (1) oder zurück(2)? "))
if options == 1:
    text_input = input("Bitte gib den Klartext der übersetzt werden soll an: ")
    finished_text = text_input.lower()
    for letter in text_input:
        index_of_text += 1
        if letter.lower() in CONSONANTS:
            finished_text.insert(index_of_text, "o")
            finished_text.insert(index_of_text, letter.lower())

    print(f"Übersetzung in Räubersprache: {finished_text}")
