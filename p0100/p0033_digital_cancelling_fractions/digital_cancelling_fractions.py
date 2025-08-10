import math
from tqdm import tqdm


def simply(ab):
    g = math.gcd(*ab)
    return tuple(item//g for item in ab)


fractions_list = []


for d in tqdm(range(10, 100)):
    if d % 10 == 0:
        continue
    str_d = str(d)
    set_d = set(str_d)
    if len(set_d) == 1:
        continue
    
    for n in range(10, d):
        if n % 10 == 0:
            continue
        str_n = str(n)
        set_n = set(str_n)
        if len(set_n) == 1:
            continue

        digits = set_d | set_n

        for x in digits:
            new_d = int(str_d.replace(x, ''))
            new_n = int(str_n.replace(x, ''))
            if (new_d * n) == (new_n * d):
                fractions_list.append((n, d))


# print(*fractions_list, sep="\n")
prd = simply(tuple(math.prod(item) for item in zip(*fractions_list)))
print(prd)
