from tools.toolbox import input

starting_money = float(input("Anlagesumme: (EUR) "))
interest_percent = float(input("Zinssatz: (in %) "))
time_lenght = int(input("Laufzeit: (Jahre) "))
total_money = starting_money
t = 0

while time_lenght > 0:
    time_lenght -= 1
    t += 1
    total_money = total_money * (interest_percent / 100 + 1)
    print(f"Nach Jahr {t}: {total_money:16,.2f}")
