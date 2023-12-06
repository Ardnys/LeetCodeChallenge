def maxOperations(nums, k: int) -> int:
    map = {}
    op = 0

    for num in nums:
        comp = k - num
        if comp in map:
            op += 1
            if map[comp] == 1:
                del map[comp]
            else:
                map[comp] -= 1
        else:
            map[num] = map.get(num, 0) + 1
    return op


nums = [1, 2, 3, 4]
k = 5
print(maxOperations(nums, k))
