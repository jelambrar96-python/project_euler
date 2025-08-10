import itertools
# import bisect


def dictincPowers(rangeA, rangeB):
    setPowers = set()
    for a, b in itertools.product(rangeA,rangeB):
        setPowers.add(a ** b)
    return setPowers


if __name__ == '__main__':
    rangeA = range(2, 101)
    rangeB = range(2, 101)
    dpowers = dictincPowers(rangeA=rangeA, rangeB=rangeB)
    print(len(dpowers))
