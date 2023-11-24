def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = m - 1
    j = n - 1
    insert = len(nums1) - 1

    while j >= 0:
        print(f"i: {i}, j: {j}, ins: {insert}")
        if i >= 0 and nums1[i] >= nums2[j]:
            nums1[insert] = nums1[i]
            nums1[i] = 0
            i -= 1
        else:
            nums1[insert] = nums2[j]
            nums2[j] = 0
            j -= 1
        insert -= 1
        print(f"nums: {nums1}")


nums1 = [2, 0]
nums2 = [1]
merge(nums1, 1, nums2, 1)
print(nums1)
