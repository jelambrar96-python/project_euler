

def reverseNumber(num, base=10):
    revNum = 0
    while num > 0:
        revNum = revNum * base + num % base
        num //= base
    return revNum


def isPalindrome(num):
    return reverseNumber(num) == num


def main(limit, maxIterations):
    lychrels = []
    for i in range(10, limit, 1):
        valid = True
        currentNumber = i
        reversedCurrentNumber = reverseNumber(currentNumber)
        for __ in range(maxIterations + 1):
            candidate = reversedCurrentNumber + currentNumber
            reversedNumber = reverseNumber(candidate)
            if candidate == reversedNumber:
                valid = False
                break
            currentNumber, reversedCurrentNumber = candidate, reversedNumber
        if valid:
            lychrels.append(i)
    return lychrels


if __name__ == '__main__':
    lychrels = main(10_000, 50)
    # print(lychrels)
    print(len(lychrels))

