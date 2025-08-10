from tqdm import tqdm


abundant_set = []


def sumDivisors(n):
    step = 1 if n % 2 == 0 else 2
    limit = (n // 2 + 1) if n % 2 == 0 else (n // 3 + 1)
    sum = 0
    for i in range(1, limit + step, step):
        if i * i  == n:
            sum += i
            break
        elif i * i > n:
            break    
        if n % i == 0:
            sum += i
            sum += (n//i)
    return sum - n


def non_abundand_sum(limit):
    sum_all = limit * (limit + 1) // 2
    for i in range(1, limit + 1):
        isAbundant = i < sumDivisors(i)
        if not isAbundant:
            continue
        # print(i)
        abundant_set.append(i)

    countAbun = len(abundant_set)
    noAbundSet = set()
    for i in range(countAbun):
        for j in range(i, countAbun):
            number = abundant_set[i] + abundant_set[j]
            if number > limit:
                break
            noAbundSet.add(number)

    return sum_all - sum(noAbundSet)


if __name__ == '__main__':

    print(non_abundand_sum(28123)) # 4179871
    # print(sumDivisors(28))