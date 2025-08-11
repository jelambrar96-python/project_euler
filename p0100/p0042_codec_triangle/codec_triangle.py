from math import isqrt, sqrt
from tqdm import tqdm 


def is_triangle_number(number: int) -> bool:
    s = int(round(sqrt(1 + 8 * number)))
    return s**2 == 1 + 8 * number and (-1 + s) % 2 == 0


def isTriangular(num):
    n = isqrt(2 * num)
    tn = n * (n + 1) // 2
    return num == tn


def triangle_words(list_names):
    words = []
    for item in tqdm(list_names):
        score = sum((ord(c) - 64) for c in item)
        if isTriangular(score):
            words.append(item)
    return words


if __name__ == '__main__':
    data = None
    with open('words.txt') as f:
        data = f.read()
    data = data.replace('"', '').strip().split(",")
    data.sort()
    print(len(triangle_words(data)))

