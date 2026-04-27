from tools.toolbox import input

t = int(input("Wie warm ist es draussen?"))

if t >= 30:
    print("Bitte sonnencreme und Hut einpacken")

elif t >= 0:
    print("Bitte Regenschirm mitnehmen")

elif t >= -20:
    print("Handschuhe und warme klammotten")

else:
    print("Achtung eisbären")
