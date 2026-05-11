from tools.toolbox import input

password = str(input("Bitte geben Sie ihr Passwort ein: "))

if password[:3] == "123":
    print(password[:3])


def isPasswordValid(password: str):
    if len(password) < 8 or len(password) > 20:
        return False
    elif len(password) % 2 != 0:
        return False
    elif password == "password":
        return False
    elif password[:3] == "123":
        return False
    elif "***" in password:
        return False
    elif password[1] == "#":
        return False
    elif "?" not in password:
        return False
    elif password.lower() == "password":
        return False
    elif password.isupper() or password.islower():
        return False
    elif "a" or "e" or "i" or "o" or "u" not in password:
        return False
    elif list(password.lower()) == list(password.lower()).reverse:
        return False
    else:
        return True


if isPasswordValid(password):
    print("Sehr Weise Wahl")
else:
    print("Weise Wahl aber nicht genug")
