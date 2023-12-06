def productExceptSelf(nums):
    length = len(nums)
    product = [1] * length

    for i in range(1, length):
        product[i] = product[i - 1] * nums[i - 1]

    right = nums[-1]
    # start from second to last, until but not including -1, decrement
    for i in range(length - 2, -1, -1):
        product[i] *= right
        right *= nums[i]
    return product


nums = [2, 3, 4, 5, 6]
print(productExceptSelf(nums))
