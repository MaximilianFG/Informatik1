hobby_a = {"Fotografieren", "Anime", "PI Auswendig lernen", "Kochen"}
hobby_b = {"Apnoetauchen", "Fotografieren", "Reisen", "Kochen"}

print(f"Person A hat diese Hobbies: {hobby_a}")
print(f"Person B hat diese Hobbies: {hobby_b}")

print(f"\n\nGemeinsame: {hobby_a & hobby_b}")
print(f"Nur Person A: {hobby_a - hobby_b}")
print(f"Nur Person B: {hobby_b - hobby_a}")
