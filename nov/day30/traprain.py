from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lMax = [0 for _ in range(n)]
        lMax[0] = height[0]
        for i in range(1, n):
            lMax[i] = max(height[i], lMax[i - 1])

        rMax = [0 for _ in range(n)]
        rMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rMax[i] = max(height[i], rMax[i + 1])

        print(f"right maxes: {rMax}\nleft maxes:  {lMax}")

        total_woah = 0
        for i in range(n):
            woah = 0
            woah = min(lMax[i], rMax[i])
            total_woah += woah - height[i]

        return total_woah


sol = Solution()
l = [4, 2, 0, 3, 2, 5]
print(f"wo'ah {sol.trap(l)}")
