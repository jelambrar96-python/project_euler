from itertools import permutations, islice
from collections import deque


def permutations_cycle(iterable, r=None):
    leniter = len(iterable)
    r = len(iterable) if r is None else r
    iter_deque = deque(iterable=iterable)
    iter_deque.rotate(1)

    for i in range(leniter):
        iter_deque.rotate(-1)
        first = iter_deque[0]
        for perm in permutations(islice(iter_deque, 1, leniter), r=r-1):
            yield first, *perm

    # raise StopIteration()

for perm in permutations_cycle(range(3)):
    print(perm)