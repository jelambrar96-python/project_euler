def power_digit_sum(n):
    if n == 0:
        return 1
    return sum(int(c) for c in str(2**n))


if __name__ == '__main__':
    N = 1000
    sumDigits = power_digit_sum(N)
    print(f"power digit sum 2^{N} is {sumDigits}")