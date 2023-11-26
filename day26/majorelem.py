from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # map performs waaay better

        uh = {}
        for n in nums:
            if n not in uh:
                uh[n] = 1
            else:
                uh[n] += 1

        m = 0
        boi = 0
        for k, v in uh.items():
            if v > m:
                m = v
                boi = k

        return boi

    # constant memo sol
    # spoiler alert: it succ


"""
    nums.sort()
    n = len(nums)
    target = int(n / 2)
    count = 1
    m = 1
    idx = 0

    for i in range(1, n):
        if nums[i - 1] == nums[i]:
            count += 1
        else:
            if count >= target and count > m:
                m = count
                idx = i - 1

            count = 1
    if count > m:
        m = count
        idx = n - 1

    return nums[idx]



"""


nums = [2, 2, 1, 1, 1, 2, 2]
print(f"nums: {nums}, maj elem: {Solution().majorityElement(nums)}")
