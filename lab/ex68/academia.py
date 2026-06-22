from enum import Enum


class Role(Enum):
    PROFESSOR = "Professor"
    LECTURER = "Dozent"
    ASSISTANT = "Assistent"


class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    def introduce(self):
        print(f"{self.name}, {self.age}")

    def get_count():
        print(Person.count)


class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def introduce(self):
        print(f"{self.name}, {self.age} , {self.major}")


class Lecturer(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role

    def introduce(self):
        print(f"{self.name}, {self.age} , {self.role.value}")


# Test
people = [
    Person("Lena", 32),
    Student("Max", 21, "Prokrastination"),
    Lecturer("Dr. Fisher", 50, Role.LECTURER),
]

for p in people:
    p.introduce()
