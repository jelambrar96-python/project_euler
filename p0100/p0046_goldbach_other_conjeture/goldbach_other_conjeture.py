import math
import itertools
from more_itertools import is_prime, sieve


def isSquare(num):
    rootNum = math.isqrt(num)
    return rootNum * rootNum == num


for i in itertools.count(3, 1):
    if is_prime(i):
        continue
    valid = False
    for p in sieve(i):
        if p == 2:
            continue
        diff = (i - p) // 2
        if isSquare(diff):
            valid = True
            break
    if not valid:
        print(i)
        break

