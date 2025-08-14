
from math import prod
from itertools import product
from functools import reduce


def sumDigits(num):
    suma = 0
    while num > 0:
        suma += (num % 10)
        num //= 10
    return suma


def maxSumDigits(N):    
    return reduce(max, (sumDigits(prod([a] * b)) for a,b in product(range(1, N), range(1, N)))) 


if __name__ == '__main__':
    print(maxSumDigits(100))