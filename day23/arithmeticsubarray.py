def checkArithmeticSubarrays(nums, l, r):
    yes = []
    for i in range(len(l)):
        arr = nums[l[i] : r[i] + 1]
        arr.sort()
        print(f"is this arithmetic: {arr}")
        diff = arr[1] - arr[0]
        uh = True
        for j in range(1, len(arr) - 1):
            if arr[j + 1] - arr[j] != diff:
                uh = False
                break

        yes.append(uh)

    return yes


nums = [-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10]
l = [0, 1, 6, 4, 8, 7]
r = [4, 4, 9, 7, 9, 10]

yes = checkArithmeticSubarrays(nums, l, r)
print(f"yes: {yes}")
