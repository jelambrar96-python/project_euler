from math import factorial

import numpy as np


def combinatoricSelectionBruteForce(num, minValue):
    values = []
    for n in range(1, num + 1):
        for r in range(1, n + 1):
            perm = factorial(n) // (factorial(r) * factorial(n - r))
            if perm > minValue:
                values.append(perm)
    return values


def combinatoricSelection(num, minValue):
    factorials = [1] * (num + 1) # start with f0 to fnum
    for i in range(1, num + 1):
        factorials[i] = factorials[i - 1] * i 
    values = []
    for n in range(1, num + 1):
        for r in range(1, n + 1):
            perm = factorials[n] // (factorials[r] * factorials[n - r]) 
            if perm > minValue:
                values.append(perm)
    return values


def pascalMatrix(num, minValue):
    matrix = np.zeros((num + 1, num + 1), dtype=np.uint64)
    matrix[:, 0] = 1
    for i in range(1, num + 1):
        matrix[i, 1:i + 1] = matrix[i - 1, 0:i] + matrix[i - 1, 1:i + 1] 
    print(matrix[0:10, 0:10])
    return np.sum(np.where(matrix > minValue, 1, 0))
        

def pascalArray(num, minValue):
    array = np.zeros((num + 1,), dtype=np.uint64)
    counter = 0
    for n in range(1, num + 1, 1):
        array[n - 1] = 1
        for r in range(num - 1, 0, -1):
            array[r] = array[r] + array[r - 1]
            if array[r] > minValue:
                counter += 1
                array[r] = minValue
    return counter


if __name__ == '__main__':
    N = 100
    MAXIMUN = 1_000_000
    # print(len(combinatoricSelectionBruteForce(N, MAXIMUN)))
    # print(len(combinatoricSelection(N, MAXIMUN)))
    # print(pascalMatrix(N, MAXIMUN))
    print(pascalArray(N, MAXIMUN))