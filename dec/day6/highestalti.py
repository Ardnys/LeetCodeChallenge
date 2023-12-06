from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        uh = 0
        for i in gain:
            uh += i
            max_alt = max(uh, max_alt)

        return max_alt


sol = Solution()
gain = [-4, -3, -2, -1, 4, 3, 2]
print(f"alt: {sol.largestAltitude(gain)}")
