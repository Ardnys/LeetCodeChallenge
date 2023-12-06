from typing import List
"""
it's the worst to try to solve it with a dict later
"""


def twoSum(nums: List[int], target: int) -> List[int]:
    for i, num in enumerate(nums):
        hold = num
        for j, uh in enumerate(nums):
            if i >= j:
                continue
            if hold + uh == target:
                return [i, j]


if __name__ == '__main__':
    res = twoSum([-1, -2, -3, -4, -5], -8)
    print(res)
