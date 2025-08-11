from itertools import permutations
from math import factorial
from tqdm import tqdm


SIEVE = [None, 2, 3, 5, 7, 11, 13, 17]
SET_DIGITS = set(range(10))


def getNumber(tuple):
    return sum(item * 10 ** i for i, item in enumerate(reversed(tuple)))


def isValid(tuple):
    for i in range(1, 8):
        n = getNumber(tuple[i: i + 3])
        if n % SIEVE[i] != 0:
            return False
    return True


def find_substring_div():
    valid = []
    with tqdm(total=factorial(9) * 9) as pbar:
        for i in range(1,10):
            tempSet = SET_DIGITS - {i}
            for originalPerm in permutations(tempSet, 9):
                pbar.update(1)
                perm = (i,) + originalPerm
                if isValid(perm):
                    valid.append(getNumber(perm))
    return valid


if __name__ == '__main__':
    print(sum(find_substring_div()))
