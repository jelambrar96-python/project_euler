import math
import itertools


from tqdm import tqdm


def champernownesBruteForce(n):
    counter = 0
    for i in itertools.count(1,1):
        strNum = str(i)
        lenStrNum = len(strNum)
        counter += lenStrNum
        if counter >= n:
            diff = counter - n
            return int(strNum[ -1 - diff])



def champernownes(n):
    if n < 10:
        return n

    ind = n - 1 # init with 0

    interval = 0
    intervalInitValue = 0
    intervalFinalValue = 9
    while ind >= intervalFinalValue:
        interval += 1
        intervalInitValue = intervalFinalValue
        intervalFinalValue += ((interval + 1) * 9 * 10 ** interval) 

    newind = ind - intervalInitValue
    modnum = interval - newind % (interval + 1)
    result = (newind // ((interval + 1) * 10 ** modnum)) % 10 
    result += (1 if modnum == interval else 0)
    return  result


if __name__ == '__main__':

    solution = math.prod(champernownes(10 ** n) for n in range(0, 7))
    print(solution)
