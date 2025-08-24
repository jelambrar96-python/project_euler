import more_itertools



LIMIT = 129977413 # < 2 ** 32

print("computing primes table...")
primes = tuple(more_itertools.sieve(LIMIT))
print("done")


def findPrimes(arrayin, ind, k):

    if len(arrayin) == k:
        return arrayin
    
    for i in range(ind, len(primes) - k + len(arrayin)):

        p = primes[i]
        flag = all(
            more_itertools.is_prime(int(str(p) + str(j))) \
                and more_itertools.is_prime(int(str(j) + str(p)))
                for j in arrayin
        )
        if not flag:
            continue
        result = findPrimes(arrayin + [p], i + 1, k)
        if result is not None:
            return result
    
    return None


def findLowestSumPrimes(arrayin, ind, k, limitsum):
    if len(arrayin) == k:
        return arrayin 
    
    currenSum = sum(arrayin, 0)
    maxNum = limitsum - currenSum

    bestResult = None
    lowestSum = limitsum

    for i in range(ind, len(primes) - k + len(arrayin)):

        p = primes[i]
        if p > maxNum:
            break
        flag = all(
            more_itertools.is_prime(int(str(p) + str(j))) \
                and more_itertools.is_prime(int(str(j) + str(p)))
                for j in arrayin
        )
        if not flag:
            continue
        result = findPrimes(arrayin + [p], i + 1, k)
        if result is not None:
            sumResult = sum(result, 0)
            if  sumResult < lowestSum:
                lowestSum = sumResult
                bestResult = result
    
    return bestResult




primes5 = findPrimes([3, 7, 109, 673, 129976621], 0, 5)
sumPrimes = sum(primes5)
print(primes5, sumPrimes)

primesResult = findLowestSumPrimes([], 0, 5, sumPrimes)

print(primesResult, sum(primesResult, 0))
