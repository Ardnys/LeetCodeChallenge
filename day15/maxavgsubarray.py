def findMaxAverage(nums, k: int) -> float:
    m = uh = sum(nums[:k])

    for i in range(k, len(nums)):
        uh += nums[i] - nums[i - k]
        m = max(m, uh)

    return m / k
