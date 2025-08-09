from tqdm import tqdm


def nth_prime(n):
    """
    Find the nth prime number.

    :param n: The position of the prime number to find (1-based index).
    :return: The nth prime number.
    """
    if n < 1:
        raise ValueError("n must be a positive integer.")

    if n == 1:
        return 2

    n -= 1 # Adjust for the first prime number being 2
    count = 0  # Count of primes found
    candidate = 1  # Current number to check for primality
    primes = []

    with tqdm(total=n) as pbar:

        while count < n:
            candidate += 2
            is_prime = not any(candidate % p == 0 for p in primes if p * p <= candidate)
            if is_prime:
                count += 1
                primes.append(candidate)
                pbar.update(1)

    return candidate

if __name__ == "__main__":
    n = 10001
    result = nth_prime(n)
    print(f"The {n}th prime number is: {result}")
