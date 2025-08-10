from itertools import pairwise


def maximum_path(triangle):
    if len(triangle) == 0:
        return 0
    if len(triangle) == 1:
        return triangle[0][0]
    last_row = [max(i,j) for i,j in pairwise(triangle[-1])]
    triangle[-2] = [(i + j) for i,j in zip(last_row, triangle[-2])]
    triangle.pop(-1)
    return maximum_path(triangle)


if __name__ == '__main__':

    triangle = """
                75
                95 64
                17 47 82
                18 35 87 10
                20 04 82 47 65
                19 01 23 75 03 34
                88 02 77 73 07 63 67
                99 65 04 28 06 16 70 92
                41 41 26 56 83 40 80 70 33
                41 48 72 33 47 32 37 16 94 29
                53 71 44 65 25 43 91 52 97 51 14
                70 11 33 28 77 73 17 78 39 68 17 57
                91 71 52 38 17 14 91 43 58 50 27 29 48
                63 66 04 68 89 53 67 30 73 16 69 87 40 31
                04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    """

    triangle_num = [[int(n) for n in row.strip().split(" ")] for row in triangle.strip().split("\n") if triangle.strip()]
    # print(*triangle_num[::-1], sep="\n")
    maxSum = maximum_path(triangle_num)
    print(maxSum)