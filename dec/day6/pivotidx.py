from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0

        for i in range(len(nums)):
            total -= nums[i]
            if i != 0:
                left += nums[i - 1]
            if left == total:
                return i

        return -1


sol = Solution()
nums = [-1, -1, 0, 1, 1, 0]
print(f"idx: {sol.pivotIndex(nums)} for {nums}")
