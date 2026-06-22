from tools.toolbox import input


class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.availability = True

    def borrow(self):

        if self.availability:
            self.availability = False
            print(f"Sie haben das Buch {self.title} ausgeliehen.")
        else:
            print("Das Buch ist nicht verfügbar")

    def return_book(self):
        self.availability = True
        print(f"Sie haben das Buch {self.title} wieder zurückgebracht.")

    def info(self):
        status = "verfügbar" if self.availability else "ausgeliehen"

        return f"'{self.title}' von {self.author} — {status}"


class Library:
    def __init__(self):
        self.list = []

    def add_book(self, book: Book):

        self.list.append(book)

        print(f"'{book.title}' wurde der Bibliothek hinzugefügt")

    def search(self, title):
        for book in self.list:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, title):
        book = self.search(title)

        if book:
            book.borrow()

    def return_book(self, title):
        book = self.search(title)

        if book:
            book.return_book()

    def list_books(self):
        print("-- Bibliothek ----------")
        for book in self.list:
            print(book.info())


library = Library()

while True:
    action = str(
        input(
            "Wähle Aktion: [h] Hinzufügen [s] Suchen [a] Ausleihen [z] Zurückgeben [l] Liste anzeigen (RETURN zum beenden): "
        )
    )

    if action == "h":
        title = str(input("Der Titel des Buches: "))
        if title == "":
            print("Keine Eingabe, abgebrochen")
            continue
        author = str(input("Der Autor des Buches: "))
        if author == "":
            print("keine Eingabe, abgebrochen")
            continue

        library.add_book(Book(title, author))
    elif action == "s":
        title = str(input("Titel des gesuchten Buches: "))
        if title == "":
            print("Keine Eingabe, abgebrochen")
            continue

        book = library.search(title)

        if book:
            print(f"Gefunden. {book.info()}")
        else:
            print("Buch wurde nicht gefunden.")
    elif action == "a":
        title = str(input("Titel des gesuchten Buches: "))
        if title == "":
            print("Keine Eingabe, abgebrochen")
            continue

        library.borrow_book(title)

    elif action == "z":
        title = str(input("Titel des gesuchten Buches: "))
        if title == "":
            print("Keine Eingabe, abgebrochen")
            continue

        library.return_book(title)

    elif action == "l":
        library.list_books()

    elif action == "":
        print("Beendet")
        break

    else:
        print("Unbekannte Eingabe, versuche erneut")
