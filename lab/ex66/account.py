class account:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit(self, amount):
        self.balance += abs(amount)
        return True

    def withdraw(self, amount):
        if abs(amount) > self.balance:
            print("Nicht genug Geld auf dem Konto")
            return False
        else:
            self.balance -= abs(amount)
            return True

    def get_balance(self):
        return self.balance


my_account = account(500)

my_account.deposit(100)
print(my_account.get_balance())
my_account.withdraw(300)
print(my_account.get_balance())
