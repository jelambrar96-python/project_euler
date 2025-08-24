from itertools import product, combinations_with_replacement, permutations, chain, pairwise
from collections import deque
from math import sqrt, factorial
# from functools import map

from more_itertools import transpose
from tqdm import tqdm


def istriangle(num):
    s = int(round(sqrt(1 + 8 * num)))
    return s**2 == 1 + 8 * num and (1 + s) % 2 == 0

def issquare(num):
    s = int(round(sqrt(4 * num)))
    return s**2 == 4 * num and s % 2 == 0

def ispentagon(num):
    s = int(round(sqrt(1 + 24 * num)))
    return s**2 == 1 + 24 * num and (1 + s) % 6 == 0

def ishexagon(num):
    s = int(round(sqrt(1 + 8 * num)))
    return s**2 == 1 + 8 * num and (1 + s) % 2 == 0

def isheptagon(num):
    s = int(round(sqrt(1 + 40 * num)))
    return s**2 == 1 + 40 * num and (3 + s) % 10 == 0

def isoctagon(num):
    s = int(round(sqrt(1 + 12 * num)))
    return s**2 == 1 + 12 * num and (2 + s) % 2 == 0

def digitsToNum(digits):
    return sum(item * 10 ** i for i, item in enumerate(reversed(digits)))


def createSixCicle(perm, n):
    lenperm = len(perm)
    if lenperm != 2 * n:
        raise ValueError()
    numbers = []
    for i in range(0, lenperm, 2):
        digits = [perm[(i + j) % lenperm] for j in range(4)]
        numbers.append(digitsToNum(digits))
    return numbers


def createNumberCicle(pairs, n):
    lenpairs = len(pairs)
    if lenpairs != n:
        raise ValueError()
    numbers = [p1 * 100 + p2 for p1, p2 in pairwise(pairs)]
    numbers.append(pairs[-1] * 100 + pairs[0])
    return numbers


# functionList = [isoctagon, isheptagon, ishexagon, ispentagon, issquare, istriangle]
functionList = [istriangle, issquare, ispentagon, ishexagon, isheptagon, isoctagon]

setNumers = {1,2,3,4,5,6,7,8,9}
pairs = tuple(prd[0] * 10 + prd[1] for prd in product(setNumers, repeat=2))
print(pairs)

def findNumbers(ncicles):

    total_bar = factorial(len(pairs) + ncicles - 1) // (factorial(ncicles) * factorial(len(pairs) - 1))
    with tqdm(total=total_bar) as pbar:
        
        for combrep in combinations_with_replacement(pairs, r=ncicles):
            pbar.update(1)    
            for perm0 in permutations(combrep):
                # perm = tuple(chain(perm0))
                # perm = tuple(int(i) for i in chain(str(item) for item in perm0))
                # numbers = createSixCicle(perm, ncicles)
                numbers = createNumberCicle(perm0, ncicles)
                mat = []
                continueFlag = False
                for i, fnc in enumerate(functionList[:ncicles]):
                    flags = [fnc(item) for item in numbers]
                    if not any(flags):
                        continueFlag = True
                        break
                    mat.append(flags)
                
                if continueFlag:
                    continue 

                flag_cols = all(sum(row) for row in transpose(mat))
                if flag_cols:
                    print(perm0)
                    print(numbers)
                    for fnc in functionList[:ncicles]:
                        print(list(map(fnc, numbers)))
                    return numbers
    return None


nums = findNumbers(6) 
print(nums)
print(sum(nums))

