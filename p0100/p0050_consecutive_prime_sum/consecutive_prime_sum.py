import itertools
from more_itertools import sieve, is_prime
from tqdm import tqdm


def findBiggestConsecutivePrimeSum(N):

    primes = tuple(sieve(N))
    nprimes = len(primes)

    maxChain = 21
    maxPrime = 953
    maxJ = None
    for i in tqdm(range(nprimes, maxChain, -1)):
        for j in range(nprimes - i + 1):
            sumPrime = sum(primes[j: j + i])
            if sumPrime >= N:
                break
            if is_prime(sumPrime):
                if i > maxChain:
                    return sumPrime, i, j
    return maxPrime, maxChain, maxJ


if __name__ == '__main__':

    N = 1_000_000
    print(findBiggestConsecutivePrimeSum(N))