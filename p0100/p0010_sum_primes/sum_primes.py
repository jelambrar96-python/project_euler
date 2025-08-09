from tqdm import tqdm 



def sum_primes(limit):
    """
    Calculate the sum of all prime numbers below a given limit.
    
    :param limit: The upper limit (exclusive) for the prime numbers.
    :return: The sum of all prime numbers below the limit.
    """
    if limit < 2:
        return 0
    if limit < 3:
        return 2

    primes = []
    
    for num in tqdm(range(3, limit, 2)):
        is_prime = not any(num % p == 0 for p in primes if p * p <= num)
        if is_prime:
            primes.append(num)

    return 2 + sum(primes)


if __name__ == "__main__":
    limit = 2_000_000
    result = sum_primes(limit)
    print(f"The sum of all prime numbers below {limit} is: {result}")
