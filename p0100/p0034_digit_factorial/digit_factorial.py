

import math

from tqdm import tqdm




result = 0
numbers = []
for i in tqdm(range(3, 10_000_000)):
    digits_factorial = sum(math.factorial(int(c)) for c in str(i))
    if i == digits_factorial:
        numbers.append(i)


print(sum(numbers))