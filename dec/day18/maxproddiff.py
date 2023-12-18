from typing import List
from sys import maxsize


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1, max2, min1, min2 = 0, 0, maxsize, maxsize
        for num in nums:
            if num >= max2 and num >= max1:
                max2 = max1
                max1 = num
            elif num >= max2 and num < max1:
                max2 = num
            if num <= min2 and num <= min1:
                min2 = min1
                min1 = num
            elif num <= min2 and num > min1:
                min2 = num

        return (max2 * max1) - (min2 * min1)


sol = Solution()
nums = [5, 6, 2, 7, 4]
print(f"{nums} : max diff: {sol.maxProductDifference(nums)}")
