def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(len(nums)):
        if nums[i] == 0:
            for j in range(i+1, len(nums)):
                # locate first non zero
                if nums[j] != 0:
                    # swap
                    nums[i] = nums[j]
                    nums[j] = 0
                    break


# [0, 1, 0, 3, 12]
# [1, 3, 0, 0, 12]
