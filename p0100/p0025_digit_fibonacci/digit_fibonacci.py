def numDigits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count


def fibbo(nth):
    x, y = 0, 1
    index = 0
    while True:
        x, y = y, x + y
        digits = numDigits(x)
        index += 1
        if digits >= nth:
            return index
    return None



if __name__ == '__main__':
    Nth = 1000
    fnth = fibbo(1000)
    print(fnth)
