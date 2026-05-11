def brutto(netto):
    return netto * 1.19


def netto(brutto):
    return brutto * (1 - 0.19)


def brightness(red, green, blue):
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue


def daysInMonth(month, year):
    daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and year % 4 == 0:
        return 29
    else:
        return daysPerMonth[month]
