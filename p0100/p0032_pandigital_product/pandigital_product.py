from itertools import permutations
from math import factorial

from tqdm import tqdm




digits = "123456789"
set_products = set()


with tqdm(total=factorial(len(digits))) as pbar:
    for perm in permutations(digits, 9):
        pbar.update(1)
        strperm = "".join(perm)

        for df0 in range(1, 5):
            f0 = int(strperm[0:df0])
            for df1 in range(1, 10 - 2 * df0):
                f1 = int(strperm[df0:df0 + df1])
                p = int(strperm[df0 + df1:])
                if f0 * f1 == p:
                    set_products.add(p)


print(sum(set_products))