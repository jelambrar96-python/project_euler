from itertools import permutations
from more_itertools import is_prime

# SYMBOLS = range(1,10)

def biggestPandigitalPrime():
    biggestPrime = 0
    for digits in range(9, 0, -1):
        for perm in permutations(range(1, digits + 1), digits):
            number = sum( item * 10 ** i for i, item in enumerate(reversed(perm)))
            if not is_prime(number):
                continue
            if number > biggestPrime:
                biggestPrime = number

        if biggestPrime != 0:
            return biggestPrime
    return None


if __name__ == '__main__':
    print(biggestPandigitalPrime())