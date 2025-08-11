import itertools
from tqdm import tqdm 


maxpandigital = 0

for i in tqdm(range(1, 333_333)):
    digits = []
    valid  = True
    for n in itertools.count(1, 1):
        p = i * n
        digitsP = [int(item) for item in str(p)]
        setDigitsP = set(digitsP)
        if len(setDigitsP) < len(digitsP):
            valid = False
            break
        if setDigitsP & {0}:
            valid = False
            break
        if set(digits) & setDigitsP:
            valid = False
            break
        digits.extend(digitsP)
        if len(digits) > 9:
            valid = False
            break
        if len(digits) == 9:
            break
    if valid:
        num = sum(item * 10 ** i for i, item in enumerate(reversed(digits)))
        if num > maxpandigital:
            maxpandigital = num


print(maxpandigital)