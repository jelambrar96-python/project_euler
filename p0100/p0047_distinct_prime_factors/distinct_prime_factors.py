import itertools
from more_itertools import factor



def distinctPrimeFactors(n):
    for i in itertools.count(1):
        valid = True
        for j in range(i, i + n):
            if len(set(factor(j))) != n:
                valid = False
                break
        if valid:
            return i


if __name__ == '__main__':
    print(distinctPrimeFactors(4))