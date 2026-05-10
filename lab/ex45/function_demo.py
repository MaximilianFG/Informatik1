###a
def add(num1, num2):
    result_add = num1 + num2
    return result_add


print(f"Add 5 und 5. Erwartung 10. Ergebnis: {add(5, 5)}")


###b
def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


print(f"max 5 und 6, Erwartung 6. Ergebnis {max(5, 6)}")


###c
def max3(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            return num1
        else:
            return num3
    elif num2 > num3:
        return num2
    elif num3 > num2:
        return num3


print(f"max3 4,5,6 Erwartung: 6, Ergebnis {max3(4, 5, 6)}")


###d
def is_negative(num1):
    if num1 < 0:
        return True
    else:
        return False


print(f"is_negative mit -4, Erwartung True, Ergebnis: {is_negative(-4)}")


###e
def sum_series(n):
    if n == 1:
        return 1
    else:
        return n + sum_series(n - 1)


print(f"sum_series mit 3, Erwartung 6, Ergebnis: {sum_series(3)}")


###f
def count_words(text):
    counter = 1
    for letter in text:
        if letter == " ":
            counter += 1
    return counter


print(
    f"count_words mit 'Ich hab Hunger', Erwartung: 3, Ergebnis: {count_words('Ich Hab Hunger')}"
)


###g
def invert_color(R, G, B):
    return 255 - R, 255 - G, 255 - B


print(
    f"invert_color mit 255, 0, 100, Erwartung: 0,255,155, Ergebnis: {invert_color(255, 0, 100)}"
)


###h
def is_contained(x1, y1, x2, y2, xp, yp):
    if xp > x1 and xp < x2 and yp > y1 and yp < y2:
        return True
    else:
        return False


print(
    f"is_contained mit 0,0,4,4,2,2 Erwartung: True, Ergebnis {is_contained(0, 0, 4, 4, 2, 2)}"
)


###i
def is_contained(xk, yk, r, xp, yp):
    difference_x = abs(xk - xp)
    difference_y = abs(yk - yp)
    distance = (difference_x**2 + difference_y**2) ** 0.5
    if distance < r:
        return True
    else:
        return False


print(
    f"is_contained mit 2,2,2,1,1, Erwartung: True, Ergebnis {is_contained(2, 2, 2, 1, 1)}"
)


###j
def is_palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False


print(
    f"is_palindrome mit LAGERREGAL, Erwartung: True, Ergebnis: {is_palindrome('LAGERREGAL')}"
)


###k
def is_prime(num):
    for number in range(2, num):
        if num % number == 0:
            return False
    return True


print(f"is_prime mit 41, Erwartung: True, Ergebnis: {is_prime(41)}")


###l
def count_prime(n):
    prime_list = []
    for number in range(2, n):
        if is_prime(number):
            prime_list.append(number)
    return prime_list


print(
    f"count_primes mit 22, Erwartung: 2, 3 , 5, 7, 11, 13, 17, 19, Ergbenis: {count_prime(22)}"
)


###m
def ordered_numbers():
    previous = "1000"
    for num in range(1000, 10000):
       for d in str(num):
           

ordered_numbers()
