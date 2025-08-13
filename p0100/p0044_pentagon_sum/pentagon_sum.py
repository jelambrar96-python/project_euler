import math
import itertools


def isPentagon(number):
    s = int(round(math.sqrt(1 + 24 * number)))
    return s**2 == (1 + 24 * number) and (1 + s) % 6 == 0


def pentagonNth(k):
    return (k * (3 * k - 1)) // 2


def findFirst():
    for k in itertools.count(2, 1):
        pk = pentagonNth(k)
        for j in range(k - 1, 0, -1):
            pj = pentagonNth(j)
            diffP, sumP = pk - pj, pk + pj
            if isPentagon(diffP) and isPentagon(sumP):
                return k, j


def pentagonNumbers():
    kmin, jmin = findFirst()
    pkmin, pjmin = pentagonNth(kmin), pentagonNth(jmin)
    currentMinDiff = pkmin - pjmin
    for k in itertools.count(kmin + 1, 1):
        pk = pentagonNth(k)
        deltaK = 3 * k + 2
        if deltaK > currentMinDiff:
            return kmin, jmin # code
        for j in range(k - 1, 0, -1):
            pj = pentagonNth(j)
            diffP, sumP = pk - pj, pk + pj
            if diffP > currentMinDiff:
                break
            if not isPentagon(diffP) or not isPentagon(sumP):
                continue
            if diffP < currentMinDiff:
                currentMinDiff = diffP
                kmin, jmin = k, j
                break


if __name__ == '__main__':
    kmin, jmin = pentagonNumbers()
    print(kmin, jmin)
    print(pentagonNth(kmin), pentagonNth(jmin))
    print(pentagonNth(kmin) - pentagonNth(jmin))
