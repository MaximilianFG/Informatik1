from tools.toolbox import input

age = int(input("Bitte gib das Alter der Person an: "))
distance = int(input("Bitte gib die Reisedistanz in Kilometern an: "))
travel_day_index = int(
    input("Bitte gib den Reisetag an (0 = Montag, ... 6 = Sonntag): ")
)
reservation = input("Gibt es eine Platzreservierung oder nicht? (ja/nein) ")

travel_day = {
    "Montag",
    "Dienstag",
    "Mittwoch",
    "Donnerstag",
    "Freitag",
    "Samstag",
    "Sonntag",
}

PRICE_PER_KM = 0.10
# Dienstag +5 EUR
# Samstag und Sonntag - 10 EUR
PRICE_RESERVATION = 2.00
PRICE_UNDER_21_MODIFICATION = 0.7

MINIMAL_PRICE = 3.00
MAXIMAL_PRICE = 49.99

total_price = distance * PRICE_PER_KM

if travel_day_index == 1:
    total_price += 5

elif travel_day_index == 5 or travel_day_index == 6:
    total_price -= 10

if reservation == "ja":
    total_price += PRICE_RESERVATION

if age < 21:
    total_price = total_price * PRICE_UNDER_21_MODIFICATION

if total_price < 3:
    total_price = 3

elif total_price > 49.99:
    total_price = 49.99


print(f"Ihr Endpreis beträgt: {total_price:0.2f} EUR")
