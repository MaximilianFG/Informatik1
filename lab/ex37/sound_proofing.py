PRICE_PER_SQM = 108.99
ROOM_LENGTH = 8
ROOM_WIDTH = 6

headline = "      " + "  ".join(f"{length:>6}m" for length in range(1, ROOM_LENGTH + 1))
print(headline)

for width in range(1, ROOM_WIDTH + 1):
    row = []
    for length in range(1, ROOM_LENGTH + 1):
        price = width * length * PRICE_PER_SQM
        row.append(f"{price:8.2f}")
    print(f"{width:>2}m  " + " ".join(row))
