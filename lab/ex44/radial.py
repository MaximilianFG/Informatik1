def radial_math(r):
    print(f"Radius {r}")
    print()
    print(f"Duchmesser ist {(2 * r):.2f}")
    print()
    print(f"Der Umfang ist ca. {(2 * 3.141592654 * r):.2f}")
    print()
    print(f"Der Flächeninhalt ist ca {(3.141592654 * r**2):.2f}")
    print()
    print(f"Volumen von der Kugel ist ca. {(4 / 3 * 3.141592654 * r**3):.2f}")
    print("------------------------------------------")
    print()


for p in range(1, 21):
    radial_math(p)
