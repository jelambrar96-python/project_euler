from itertools import combinations_with_replacement
from tqdm import tqdm


setCoins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200

# # brute force solution
# solutions = 0
# for ncoins in tqdm(range(1, 201)):
#     solutions += sum( 1 for combs in combinations_with_replacement(setCoins, ncoins) if sum(combs) == target )


def count_partitions(index, remains):
    if remains == 0:
        return 1
    if index >= len(setCoins):
        return 0
    solutions = 0
    for ind in range(index, len(setCoins)):
        coin = setCoins[ind]
        if coin > remains:
            continue
        result = count_partitions(ind, remains=remains - coin)
        solutions += result
    return solutions


solutions = count_partitions(0, target)
print(solutions)
