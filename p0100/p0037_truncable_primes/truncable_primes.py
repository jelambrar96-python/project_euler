import itertools

from tqdm import tqdm


primes = [3]


def isPrime(num):

    if num == 2:
        return True
    elif num == 1 or num % 2 == 0:
        return False
    
    lastPrime = primes[-1]
    if num < lastPrime:
        if num in primes:
            return True

    for item in primes:
        if num % item == 0:
            return False
        if item * item > num:
            break
        
    for i in range(lastPrime + 2, num//3, 2):
        iPrime = True
        for item in primes:
            if i % item == 0:
                iPrime = False
                break
            if item * item > i:
                break
        if iPrime:
            primes.append(i)
            if num % i == 0:
                return False
        
        if i * i > num:
            break

    return True



def isTruncableLeft(i):
    d = 10
    while d < i:
        num = i % d
        if not isPrime(num):
            return False
        d *= 10
    return True



def isTruncableRight(i):
    while i > 0:
        if not isPrime(i):
            return False
        i //= 10
    return True



def truncablePrimes(N):

    countTruncablePrimes = 0
    truncablePrimesList = []
    for i in itertools.count(11, 2):
        
        if not isPrime(i):
            continue

        if isTruncableLeft(i) and isTruncableRight(i):
            countTruncablePrimes += 1
            truncablePrimesList.append(i)
            if countTruncablePrimes == N:
                break

    return truncablePrimesList



if __name__ == '__main__':
    N =11
    truncablePrimesList = truncablePrimes(N)
    print(truncablePrimesList)
    print(sum(truncablePrimesList))

