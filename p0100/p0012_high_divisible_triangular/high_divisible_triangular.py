from math import prod
# from functools import lru_cache
import itertools


class PrimeGenerator:

    primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    def __init__(self):
        self.candidate = 1
        self.flag = True

    def sieve(self):
        if self.flag:
            self.flag = False
            return 2

        self.candidate += 2
        if self.candidate <= PrimeGenerator.primes[-1]:
            if self.candidate in PrimeGenerator.primes:
                return self.candidate

        # print()
        while True:
            is_prime = not any(self.candidate % p == 0 for p in PrimeGenerator.primes if p * p <= self.candidate)
            if is_prime:
                PrimeGenerator.primes.append(self.candidate)
                return self.candidate 
            self.candidate += 2
            # print(".", end="")

    def reset(self):
        self.candidate = 1
        self.flag = True



def primesFactor(n):
    """
    Generate the prime factors of a number n.
    
    :param n: The number to factor.
    :return: A list of prime factors of n.
    """
    pg = PrimeGenerator()
    pg.reset()
    factors = []
    while n > 1:
        prime = pg.sieve()
        count = 0
        while n % prime == 0:
            count += 1
            n //= prime
        if count > 0:
            factors.append((prime, count))
    return factors


# @lru_cache(maxsize=128)
def count_divisors(n):
    """
    Count the number of divisors of a number using its prime factorization.
    """
    pg = PrimeGenerator()
    pg.reset()
    factors = 1
    while n > 1:
        prime = pg.sieve()
        count = 0
        while n % prime == 0:
            count += 1
            n //= prime
        if count > 0:
            factors *= (count + 1)
    return factors


def divisors(n):
    """
    Count the number of divisors of a number n.
    
    :param n: The number to count divisors for.
    :return: The count of divisors of n.
    """
    limit = n // 2 if n % 2 == 0 else n // 3
    step = 1 if n % 2 == 0 else 2
    return [i for i in range(1, limit + 1, step) if n % i == 0] + [n]


def high_divisible_triangular(n):
    """
    Find the first triangular number that has more than n divisors.
    
    :param n: The minimum number of divisors.
    :return: The first triangular number with more than n divisors.
    """
    triangle_number = 0
    max_div = 0
    for d0 in itertools.count(3, 2):
        print(d0, end="\r")
        nd0 = count_divisors(d0)
        md0 = d0 // 2
        for d1 in (md0, md0 + 1):
            nd1 = count_divisors(d1)
            n_div = nd0 * nd1
            if n_div > n:
                triangle_number = d0 * d1
                return triangle_number
            if n_div > max_div:
                max_div = n_div
                triangle_number = d0 * d1
                print(f"current max div found: {n_div}, n = {triangle_number}")

if __name__ == "__main__":
    n = 500
    result = high_divisible_triangular(n)
    print(f"The first triangular number with more than {n} divisors is: {result}")
    # print(primesFactor(result))
    # print(divisors(result))
