line = []

print("Eröffnung, niemand in der Schlange")

line.append("A")
line.append("B")
line.append("C")
line.append("D")
print(f"\n\n A, B, C, D stellen sich an.\n Schlange jetzt: {line}")

del line[0]
print("\n\nErster bekommt Eis und geht")
print(f"Schlange jetzt: {line}")

line.append("E")
line.append("F")
line.append("G")
line.append("H")
print(f"\n\n E, F, G, H stellen sich an.\n Schlange jetzt: {line}")


line.remove("H")
print(f"\n\n H ist die Schlange zu lang und geht. \n Schlange jetzt: {line}")

line.remove("B")
line.remove("C")
print(f"\n\n B und C bekommen ein Eis und gehen \n Schlange jetzt: {line}")

line.insert(0, "M")
line.insert(0, "L")
line.insert(0, "K")
line.insert(0, "J")
print(f"\n\n J, K, L, M sind gut mit D und gehen nach vorn \n Schlange jetzt: {line}")

line.insert(1, line.pop(2))
print(f"\n\n 3. drängelt sich auf 2. vor \n Schlange jetzt: {line}")

print(f"\n\n Schlange wird nach verlangen umgedreht \n Schlange jetzt: {line[::-1]}")
line.reverse()

del line[0]
del line[1]
del line[2]
del line[3]

print(f"\n\n Die ersten 4 bekommen ein Eis \n Schlange jetzt: {line}")
print(f"\n\n Eisdiele zu \n  {line} haben kein Eis bekommen")
