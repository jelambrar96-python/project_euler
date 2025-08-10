import math

def factorial_digit_sum(n):
    return sum(int (c) for c in str(math.factorial(n)))

if __name__ == '__main__':
    N = 100
    print(factorial_digit_sum(N))