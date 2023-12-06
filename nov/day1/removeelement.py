from typing import List


def removeElement(nums: List[int], val: int) -> int:
    size = len(nums)
    bruh = 0
    for i in range(size):
        if nums[i] != val:
            nums[bruh] = nums[i]
            bruh += 1
    return bruh


if __name__ == "__main__":
    malist = [2, 3, 3, 2]
    val = 2
    not_k = removeElement(malist, val)
    print(f"list: {malist} elems: {not_k}")
