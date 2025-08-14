import itertools

from more_itertools import is_prime
import numpy as np


def spiralIterativeGenerator(M):

    spiralMatrix = None
    minispiral = np.array([[1]], dtype=np.uint32)

    if M == 1:
        yield  minispiral
    
    for N in itertools.count(3, 2):

        spiralMatrix = np.empty((N,N), dtype=np.uint32)
        spiralMatrix[1:N - 1, 1:N - 1] = minispiral

        initSpiral = (N - 2) * (N - 2) + 1
        spiralMatrix[1:N, N - 1] = np.arange(initSpiral, initSpiral + N - 1)
        
        initSpiral += (N - 1)
        spiralMatrix[N - 1, 0:N - 1] = np.arange(initSpiral, initSpiral + N - 1)[::-1]

        initSpiral += (N - 1)
        spiralMatrix[0:N - 1, 0] = np.arange(initSpiral, initSpiral + N - 1)[::-1]

        initSpiral += (N - 1)
        spiralMatrix[0, 1: N] = np.arange(initSpiral, initSpiral + N - 1)

        minispiral = spiralMatrix

        if M <= N:
            yield spiralMatrix



def diagonalsElementGenerator(N):
    currentValue = 1
    elements = [currentValue]
    if N == 1:
        yield elements
    currentDelta = 2
    for i in itertools.count(3, 2):
        for j in range(4):
            currentValue += currentDelta
            elements.append(currentValue)
        currentDelta += 2
        if N <= i:
            yield elements


def diagonalsElementCounterGenerator(N):
    primesCounter = 0
    noPrimesCounter = 1
    if N == 1:
        yield primesCounter, noPrimesCounter
    currentDelta = 2
    currentValue = 1
    for i in itertools.count(3, 2):
        for __ in range(4):
            currentValue += currentDelta
            if is_prime(currentValue):
                primesCounter += 1
            else:
                noPrimesCounter += 1
        currentDelta += 2
        if N <= i:
            yield primesCounter, noPrimesCounter



def findSpiralPrimesLength(ratio):
    N = 7
    for i, (primeCounter, noPrimeCounter) in  zip(itertools.count(N, 2), diagonalsElementCounterGenerator(N)):
        currentRatio = primeCounter / (primeCounter + noPrimeCounter)
        if currentRatio < ratio:
            return i, currentRatio        


if __name__ == '__main__':
    print(findSpiralPrimesLength(0.10))