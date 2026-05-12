def isPrime2(n, f):
    print(n, f)
    if f == 1:
        return True
    elif n % f == 0:
        return False
    else:
        return isPrime2(n, f - 1)


def isPrime(n):
    return isPrime2(n, n - 1)


print(isPrime(12))
