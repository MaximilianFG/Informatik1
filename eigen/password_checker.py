def checkPassword(password: str) -> bool:
    if len(password) <= 8:
        return False

    if not (
        "H" in password.upper() or "D" in password.upper() or "M" in password.upper()
    ):
        return False

    for index in range(len(password) - 1):
        if password[index] == password[index + 1]:
            return False

    if password.lower()[::-1] == password.lower():
        return False

    return True


print(checkPassword("Halloduda"))
print(checkPassword("Hallo"))
print(checkPassword("aabbccddee"))
print(checkPassword("Abcdefgha"))
