import collections
import more_itertools

from tqdm import tqdm


N = 1_000_000
# N = 100

primes = set(more_itertools.sieve(N))
circular_primes = []

for p in tqdm(primes):
    if p < 10:
        circular_primes.append(p)
        continue
    
    strp = collections.deque(str(p))
    if any(int(item) % 2 == 0 for item in strp):
        continue

    len_strp = len(strp)
    isCircular = True
    for __ in range(1, len_strp):
        strp.rotate(1)
        new_prime = int("".join(strp))
        if not new_prime in primes:
            isCircular = False
            break
    
    if isCircular:
        circular_primes.append(p)


# print(sorted(list(circular_primes)))
print(len(circular_primes))
