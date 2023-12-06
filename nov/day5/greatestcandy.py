def kidsWithCandies(candies, extraCandies):
    # yes = []
    diff = max(candies) - extraCandies
    return [candy >= diff for candy in candies]
    # for candy in candies:
    #     if candy + extraCandies >= max(candies):
    #         yes.append(True)
    #     else:
    #         yes.append(False)
    # return yes


candies = [2, 3, 5, 1, 3]
kgn = kidsWithCandies(candies, 3)
print(kgn)
