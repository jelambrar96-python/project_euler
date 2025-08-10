import itertools

from tqdm import tqdm


primes = [3, 5, 7]


def isPrime(number):
    if number < 1:
        return False

    if number % 2 == 0:
        return False
    
    for i in range(3, number // 2, 2):
        if i * i  > number:
            break
        if number % i == 0:
            return False
    return True


def quadratic_primes(limitA, limitB):
    max_consecutive_primes = 0
    maxA = None
    maxB = None
    for a in tqdm(range(-1 * limitA + 1, limitA)):
        for b in range(-1 * limitB, limitB + 1):

            for n in itertools.count(0, 1):
                number = n * n + a * n + b
                if not isPrime(number):
                    if n > max_consecutive_primes:
                       maxA = a
                       maxB = b
                       max_consecutive_primes = n
                    break
    return maxA, maxB


if __name__ == '__main__':
    limit_a = 1000
    limit_b = 1000
    a, b = quadratic_primes(limitA=limit_a, limitB=limit_b)
    print(a * b)

    