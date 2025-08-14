

def digits(num):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    return digits


def square_root_convergents(nth):
    terms = [None] * nth
    terms[0] = [1, 2]
    for i in range(1, nth):
        numBef, denBef = terms[i - 1]
        terms[i] = [denBef, (numBef + 2 * denBef)]
    for i in range(nth):
        terms[i][0] += terms[i][1]
    return terms


if __name__ == '__main__':
    list_fract = square_root_convergents(1_000)
    # print(list_fract)
    list_fract_filtered = [ [a, b] for a, b in list_fract if len(digits(a)) > len(digits(b)) ]
    # print(list_fract_filtered)
    print(len(list_fract_filtered))