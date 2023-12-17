from typing import List

# this solution is 600 times slower than Java solution ?

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ferp = [0] * len(pref)
        ferp[0] = pref[0]
        for i in range(1, len(pref)):
            ferp[i] = pref[i] ^ pref[i - 1]

        return ferp


sol = Solution()
pref = [5, 2, 0, 3, 1]
print(f"{pref} => {sol.findArray(pref)}")
