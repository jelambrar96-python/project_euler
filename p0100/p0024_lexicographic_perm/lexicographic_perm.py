from itertools import permutations


str = "0123456789"

def lexicographic_perm(nth):
    for i, perm in enumerate(permutations(str), start=1):
        if i == nth:
            return "".join(perm)
    return None


if __name__ == '__main__':
    NTH = 1_000_000
    print(lexicographic_perm(NTH))
