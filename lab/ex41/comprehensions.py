list_a = [a**2 for a in range(1, 21)]
print(f"Square Numbers: {list_a}")

list_b = [b for b in [3, 8, 15, 22, 29, 36, 43, 50] if b % 5 == 0]
print(f"Durch 5 Teilbar: {list_b}")

list_c = [c.upper() for c in ["python", "media", "technology", "comprehension"]]
print(f"Großbuchstaben: {list_c}")

list_de = [(d, e) for d in [1, 2, 3] for e in [4, 5, 6]]
print(f"Paare: {list_de}")

list_f = [
    f for f in ["apple", "banana", "cherry", "date", "fig", "grape"] if len(f) == 5
]
print(f"5 Buchstaben: {list_f}")

list_g = [round((g * (9 / 5) + 32), 1) for g in [0, 10, 20, 30, 37.8]]
print(f"Fahrenheit: {list_g}")

list_h = [h[::-1] for h in ["media", "technology", "python"]]
print(f"Umgedreht: {list_h}")
