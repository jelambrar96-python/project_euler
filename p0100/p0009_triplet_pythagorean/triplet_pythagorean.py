from tqdm import tqdm


def triplet_pythagorean(n):
    """
    Find the Pythagorean triplet (a, b, c) such that a + b + c = n.
    
    :param n: The sum of the triplet.
    :return: A tuple (a, b, c) if a Pythagorean triplet exists,
    otherwise return an empty list.
    """
    soltuions = []

    for a in tqdm(range(1, n // 3)):
        
        cnum = a * a + (n - a) * (n - a)
        cden = 2 * (n - a)

        if cden == 0:
            continue
        if cnum % cden != 0:
            continue

        c = cnum // cden
        b = n - a - c

        if b < a:
            continue

        if a * a + b * b == c * c:
            soltuions.append((a, b, c))

    return soltuions


if __name__ == "__main__":
    n = 1000
    triplet = triplet_pythagorean(n)
    if triplet:
        a, b, c = triplet[0]
        print(f"The Pythagorean triplet for n={n} is: a={a}, b={b}, c={c}")
        print(f"The product abc is: {a * b * c}")
    else:
        print(f"No Pythagorean triplet found for n={n}.")
