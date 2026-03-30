y = 2026
t = 121
Weekday = y + (y - 1) // 4 - (y - 1) // 100 + (y - 1) // 400 + t

index = int(Weekday) % 7
wochentage = [
    "Samstag",
    "Sonntag",
    "Montag",
    "Dienstag",
    "Mittwoch",
    "Donnerstag",
    "Freitag",
]
print(f"Der Wochentag für das gewählte Datum ist {wochentage[index]}")
