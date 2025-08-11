import itertools
import math


def isPentagonal(number):
    s = int(round(math.sqrt(1 + 8 * number)))
    return s**2 == (1 + 8 * number) and (s - 1) % 2 == 0


def isTriangular(number):
    s = int(round(math.sqrt(1 + 24 * number)))
    return s**2 == (1 + 24 * number) and (1 + s) % 6 == 0


def tphBruteForce():
    for k in itertools.count(144, 1):
        hk = 2 * (2 * k - 1)
        if isPentagonal(hk) and isTriangular(hk):
            return k


if __name__ == '__main__':
    k = tphBruteForce()
    print(k)
    print(k * (2 * k - 1))
