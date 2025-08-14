import collections
import itertools


def digits(number):
    digits = []
    while number > 0:
        digits.append(number % 10)
        number //= 10
    return digits


def sameDigits(num1, num2):
    # print(num1, num2)
    # print(digits(num1), digits(num2))
    return sorted(digits(num1)) == sorted(digits(num2))


def findPermutedMultiple(N):
    for n in range(1, 1_000_000_000 // N, 1):
        flag = True
        for i in range(2, N + 1):
            if not sameDigits(n, n * i):
                flag = False
                break
        if flag:
            # print([i * n for i in range(1, N + 1)])
            return n
    return None


if __name__ == '__main__':
    print(findPermutedMultiple(6))
