import itertools
from tqdm import tqdm

def isPalindrome(number, base = 10):
    result = 0
    k = number
    while k > 0:
        result *= base 
        result += k % base
        k //= base
    return result == number


def doublePalindromeBruteForce(limit):
    return [ i for i in tqdm(range(1, limit, 2)) if isPalindrome(i, 10) and isPalindrome(i, 2) ]


def doublePalindromes(limit):
    if limit < 3:
        return [1]
    if limit < 5:
        return [1, 3]

    doublePalindromesList = [1, 3]
    symbols = (0, 1)

    for i in itertools.count(1,1):
        for prd in itertools.product(symbols, repeat=i):

            for j in range(2):                
                symInternal = list(prd + prd[::-1]) if j == 1 else (list(prd) + list(reversed(prd[:-1])))
                binNumber = [1] + symInternal + [1]
                decNumber = sum(item * (2 ** idx) for idx, item in enumerate(binNumber))
                if decNumber >= limit:
                    continue

                if isPalindrome(decNumber, 10):
                    doublePalindromesList.append(decNumber)

        if 2 ** (2 * i + 3) > limit:
            break
    return doublePalindromesList


if __name__ == '__main__':
    
    N = 1_000_000
    doublePalindromesList = doublePalindromeBruteForce(N)
    print(sum(doublePalindromesList))
    doublePalindromesList = doublePalindromes(N)
    print(sum(doublePalindromesList))
