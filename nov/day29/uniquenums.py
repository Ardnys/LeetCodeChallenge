from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        nums = {}
        for i in arr:
            if i in nums:
                nums[i] += 1
            else:
                nums[i] = 1

        return len(nums.values()) == len(set(nums.values()))


sol = Solution()
nums = [1, 2, 2, 1, 1, 3, 3]
print(sol.uniqueOccurrences(nums))
