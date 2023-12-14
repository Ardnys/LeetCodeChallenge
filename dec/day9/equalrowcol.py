from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        """
        pass it one way, like pass the rows
        then add them in a set
        then pass other way, like cols
        check if the thing exists
        """
        nums = 0
        rows = [row for row in grid]
        for i, row in enumerate(grid):
            col = [row[i] for row in grid]
            nums += rows.count(col)

        return nums


sol = Solution()
grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
print(f"pairs {sol.equalPairs(grid)}")
