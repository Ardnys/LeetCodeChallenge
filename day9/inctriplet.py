from sys import maxsize


def increasingTriplet(nums) -> bool:
    mid = maxsize
    left = maxsize

    for i in nums:
        if i <= mid:
            mid = i
        elif i <= left:
            left = i
        else:
            return True

    return False
