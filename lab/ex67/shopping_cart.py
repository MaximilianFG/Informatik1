class Item:
    def __init__(self, name: str, price: float, amount: int = 1):
        self.name = name
        self.price = price
        self.amount = amount


class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self, item: Item):
        self.cart.append(item)

    def show_items(self):
        if not self.cart:
            print("Leerer Warenkorb")
        else:
            for item in self.cart:
                print(f"{item.name} Anzahl: {item.amount} Einzelpreis: {item.price}")
            print(f"Insgesamter Preis: {self.get_total_price()}")

    def get_total_price(self):
        total_price = 0
        for item in self.cart:
            total_price += item.price * item.amount
        return total_price


cart = ShoppingCart()

item1 = Item("Schoko", 5.99, 2)
item2 = Item("Stift", 3.99)

cart.add_item(item1)
cart.add_item(item2)

cart.show_items()
