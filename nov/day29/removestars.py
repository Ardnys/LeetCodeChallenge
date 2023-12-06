class Solution:
    def removeStars(self, s: str) -> str:
        stacc = []
        for c in s:
            if c == "*":
                stacc.pop()
            else:
                stacc.append(c)

        return "".join(stacc)


sol = Solution()
s = "leet**cod*e"
sol.removeStars(s)
