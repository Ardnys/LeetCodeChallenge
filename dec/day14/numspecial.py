from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        special = 0
        for row in mat:
            if sum(row) == 1:
                col = row.index(1)
                yes = sum(row[col] for row in mat)
                if yes == 1:
                    special += 1
        return special


sol = Solution()
mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
print(f"res = {sol.numSpecial(mat)}")
