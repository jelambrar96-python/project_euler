from tqdm import tqdm


amicable_dict = {1:1}


def sumDivisors(n):
    limit = (n // 2 + 1) if n % 2 == 0 else (n // 3 + 1)
    step = 1 if n % 2 == 0 else 2
    sum = 1
    for i in range(2, limit, step):
        if i * i  == n:
            sum += i
            break
        elif i * i > n:
            break    
        if n % i == 0:
            sum += i
            sum += (n//i)
    return sum


def sumAmicable(n):
    sumAmi = 0
    for i in tqdm(range(2,n)):
        m = sumDivisors(i)
        if i == sumDivisors(m) and m != i:
            sumAmi += i
            print(i)
    return sumAmi


if __name__ == '__main__':
    N = 10000
    print(sumAmicable(N))
