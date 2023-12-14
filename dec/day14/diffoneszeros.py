from typing import List

"""
You are given a 0-indexed m x n binary matrix grid.

A 0-indexed m x n difference matrix diff is created with the following procedure:

Let the number of ones in the ith row be onesRowi.
Let the number of ones in the jth column be onesColj.
Let the number of zeros in the ith row be zerosRowi.
Let the number of zeros in the jth column be zerosColj.
diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
Return the difference matrix diff.

diff = nrow + ncol - 2 * (zerosRowi + zerosColj)
"""


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        nrow, ncol = len(grid), len(grid[0])

        row_ones = [0] * nrow
        col_ones = [0] * ncol

        for i in range(nrow):
            for j in range(ncol):
                row_ones[i] += grid[i][j]
                col_ones[j] += grid[i][j]
        diff = [[0 for _ in range(ncol)] for _ in range(nrow)]

        for i in range(nrow):
            for j in range(ncol):
                diff[i][j] = nrow + ncol - 2 * (row_ones[i] + col_ones[j])

        return diff


sol = Solution()
grid = [[0, 1, 1], [1, 0, 1], [0, 0, 1]]
print(f"res: {sol.onesMinusZeros(grid)}")
