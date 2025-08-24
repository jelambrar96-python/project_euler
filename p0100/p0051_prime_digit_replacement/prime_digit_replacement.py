import itertools
from more_itertools import is_prime


def generateNumber(shell, digitsFalse, digitTrue):
    # numberDigitFalse = len(digitsFalse)
    indDigitFalse = 0
    digitNumber = [0] * len(shell)
    for i, item in enumerate(shell):
        if item:
            digitNumber[i] = digitTrue
        else:
            digitNumber[i] = digitsFalse[indDigitFalse]
            indDigitFalse += 1
    return sum(item * 10 ** i for i, item in enumerate(reversed(digitNumber)))


def numberFinder(shell, minPrimes):
    numDigits = len(shell)
    minNumber = 10 ** (numDigits - 1)
    sumFalse = len([item for item in shell if not item])
    for prd in itertools.product(range(10), repeat=sumFalse):
        if not shell[0] and prd[0] == 0:
            continue
        if not shell[-1] and prd[-1] in (0, 2, 4, 6, 8):
            continue
        counter = 0
        for i in range(10):
            if (10 - i) < (minPrimes - counter):
                break
            number = generateNumber(shell, prd, i)
            if number < minNumber:
                continue
            if is_prime(number):
                counter += 1
        if counter >= minPrimes:
            # return generateNumber(shell, prd, 0)
            return [ generateNumber(shell, prd, i) for i in range(10) if is_prime(generateNumber(shell, prd, i)) ]

    return None


BOOLEAN_TABLE = {True, False} 


def findSmallestPrimeDigitReplacement(minValue):

    print("for 2 digits...")
    for perm in itertools.permutations(BOOLEAN_TABLE):
        result = numberFinder(perm, minPrimes=minValue)
        if result is not None:
            return result

    # numero de cifras
    for i in itertools.count(3,1):
        print(f"for {i} digits...")
        maxDigitsChange = i - 2
        for comb in itertools.combinations_with_replacement(BOOLEAN_TABLE, maxDigitsChange):
            for perm in itertools.permutations(comb + (True, False), i):
                result = numberFinder(perm, minPrimes=minValue)
                if result is not None:
                    return result                

    return None


if __name__ == '__main__':
    print(findSmallestPrimeDigitReplacement(8))




