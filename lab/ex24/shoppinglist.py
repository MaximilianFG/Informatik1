cart = {"Apfel": 3, "Banenen": 5, "Milch": 2}
prices = {"Apfelpreis": 0.5, "Bananenpreis": 0.3, "Milchpreis": 1.2}

for item, quantity in cart.items():
    totalprice = (
        cart["Apfel"] * prices["Apfelpreis"]
        + cart["Banenen"] * prices["Bananenpreis"]
        + cart["Milch"] * prices["Milchpreis"]
    )


print(f"Der komplette Warenkorb kostet: {totalprice} EUR")
