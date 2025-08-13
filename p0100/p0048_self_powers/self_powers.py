


def selfPowers(n, digits):
    modop = 10 ** digits
    return sum((i ** i) % modop for i in range(1, n + 1)) % modop


if __name__ == '__main__':
    print(selfPowers(1000, 10))
