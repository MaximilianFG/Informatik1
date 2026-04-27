from tools.toolbox import input

decimal = int(input("Bitte gib eine Dezimalzahl ein: "))
if decimal == 0:
    hexadecimal = "0"
else:
    hex_digits = "0123456789ABCDEF"
    result = []
    while decimal > 0:
        remainder = decimal % 16
        result.append(hex_digits[remainder])
        decimal = decimal // 16
    hexadecimal = "".join(result[::-1])
print(f"Die hexadezimale Darstellung von {decimal} ist: {hexadecimal}")
