from math import ceil


def searchMatrix(matrix, target: int) -> bool:
    nrows, ncols = len(matrix), len(matrix[0])

    r, c = 0, ncols - 1
    while (r < nrows and c > -1):
        i = matrix[r][c]
        if i == target:
            return True
        if target > i:
            r += 1
        else:
            c -= 1


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
yes = searchMatrix(matrix, 3)
print(f"yes: {yes}")
