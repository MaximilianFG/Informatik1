from tools.toolbox import input

ALCOHOL_DENSITY = 0.8  # g/ml

mass_person = float(input("Wie viel wiegt die Person in kg? "))
drink_volume_ml = float(input("Wie viel ml Alkohol wurde getrunken? "))
alcohol_percentage = float(input("Wie viel Prozent Alkohol hat das Getränk? "))

type_of_person = input("Ist die Person männlich, weiblich oder ein Kind? (m/w/k) ")

if type_of_person == "m":
    distribution_ratio = 0.7
elif type_of_person == "w":
    distribution_ratio = 0.6
elif type_of_person == "k":
    distribution_ratio = 0.8

alcohol_mass = drink_volume_ml * (alcohol_percentage / 100) * ALCOHOL_DENSITY

blood_alcohol_concentration = alcohol_mass / (mass_person * distribution_ratio)

print(
    f"Die Blutalkoholkonzentration beträgt {blood_alcohol_concentration:.4f} g/kg (Ca. {blood_alcohol_concentration:.2f} Promille)."
)
