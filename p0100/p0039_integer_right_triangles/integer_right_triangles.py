from tqdm import tqdm


def triplet_pythagorean(n):
    """
    Find the Pythagorean triplet (a, b, c) such that a + b + c = n.
    
    :param n: The sum of the triplet.
    :return: A tuple (a, b, c) if a Pythagorean triplet exists,
    otherwise return an empty list.
    """
    soltuions = []

    for a in range(1, n // 3):
        
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


def integer_right_triangles(N):
    maximunSolutions = 0
    maxP = None
    for i in tqdm(range(12, N + 1, 1)):
        solutions = len(triplet_pythagorean(i))
        if solutions > maximunSolutions:
            maximunSolutions = solutions
            maxP = i
    return maxP


if __name__ == '__main__':
    N = 1000
    print(integer_right_triangles(N))
