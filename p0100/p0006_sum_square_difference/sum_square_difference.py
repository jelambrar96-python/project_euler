
def sum_square_diffetrence(n):
    """
    Calculate the difference between the sum of the squares of the first n natural numbers
    and the square of the sum of the first n natural numbers.

    :param n: The upper limit of the natural numbers to consider.
    :return: The difference between the sum of squares and the square of the sum.
    """
    return n * (n + 1) * ( 3 * n * n - n - 2) // 12

if __name__ == "__main__":
    n = 100
    result = sum_square_diffetrence(n)
    print(f"The difference for the first {n} natural numbers is: {result}")
