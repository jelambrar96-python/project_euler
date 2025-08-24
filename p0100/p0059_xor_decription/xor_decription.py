from itertools import product
from string import ascii_lowercase
from tqdm import tqdm


def computeScore(decriptedText, dictionary):
    return sum(decriptedText.count(item) for item in dictionary)


def decript(key, list_numbers):
    lenkey = len(key)
    ordkey = [ord(k) for k in key]
    return [ordkey[i % lenkey] ^ item for i, item in enumerate(list_numbers)]


def asciitoText(asciiList):
    return "".join(chr(item) for item in asciiList)


def decription(listNumbers, dictionary):
    maxScore = 0
    bestKey = None
    with tqdm(total=len(ascii_lowercase) ** 3) as pbar:
        for chars in product(ascii_lowercase, repeat=3):
            pbar.update(1)
            text = asciitoText(decript(chars, listNumbers))
            score = computeScore(text, dictionary)
            if score > maxScore:
                maxScore = score
                bestKey = chars
        return bestKey


if __name__ == '__main__':

    strdata = None
    with open('cipher.txt') as f:
        strdata = f.read()
    list_numbers = [int(item.strip()) for item in strdata.strip().split(',')]
    

    strdata = None
    with open('google-10000-english.txt') as f:
        strdata = f.read()
    dictionary = [item.strip() for item in strdata.strip().split('\n') if item]
    # print(dictionary)

    bestKey = decription(list_numbers, dictionary)
    print(bestKey)
    print(sum(decript(bestKey, list_numbers)))
