from collections import Counter
from more_itertools import sieve, is_prime




def findPrimePermuttions():

    PRIMES_ARRAY = tuple(item for item in sieve(10_000) if item > 1000)

    for i, iprime in enumerate(PRIMES_ARRAY):
        
        if iprime == 1487:
            continue
        
        setIprime = Counter(str(iprime))
        
        for __, jprime in enumerate(PRIMES_ARRAY[i + 1:]):
            setJprime = Counter(str(jprime))
            if setJprime != setIprime:
                continue
            
            diff = jprime - iprime
            kprime = jprime + diff

            if kprime > 9999:
                continue
            if not is_prime(kprime):
                continue

            setKprime = Counter(str(kprime))
            if setIprime != setKprime:
                continue
            
            return (iprime, jprime, kprime)
            

if __name__ == '__main__':
    print(findPrimePermuttions()) # (2969, 6299, 9629) # 296962999629

