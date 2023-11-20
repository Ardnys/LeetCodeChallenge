from math import ceil


def searchInsert(nums, target: int) -> int:
    left = 0
    right = len(nums)

    if target > nums[right - 1]:
        return right

    while left <= right:
        mid = int((right + left) / 2)

        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return left


