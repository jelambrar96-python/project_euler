from math import factorial


def lattice_paths(n, m):
    fn = factorial(n)
    fm = factorial(m)
    return factorial(n + m) // (fn * fm)

if __name__ == '__main__':
    N = 20
    M = 20
    paths = lattice_paths(N, N)
    print(f"latice paths {N} x {M} is {paths}")
