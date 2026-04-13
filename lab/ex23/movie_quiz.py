import random

from tools.toolbox import input

movies = {
    "Bullet Train": "Brad Pitt",
    "The Amazing Spiderman": "Andrew Garfield",
    "The Wolf of Wallstreet": "Leonardo DiCaprio",
    "Interstellar": "Matthew McConaughey",
    "The Dark Knight": "Christian Bale",
}
movie1, movie2 = random.sample(list(movies), 2)

print(f"Wer spielte in {movie1} die Hauptrolle, nicht in {movie2}")
guess = str(input("Dein Tipp: "))

if guess == movies[movie1] and guess != movies[movie2]:
    print("Richtig!")
