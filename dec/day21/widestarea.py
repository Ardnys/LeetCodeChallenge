from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        m = 0
        for i in range(1, len(points)):
            w = points[i][0] - points[i - 1][0]
            m = max(m, w)

        return m


sol = Solution()
mat = [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]
print(f"area: {sol.maxWidthOfVerticalArea(mat)}")
