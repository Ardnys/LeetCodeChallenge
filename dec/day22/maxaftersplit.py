class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count("1")
        zeros = 0
        m = 0

        for i in range(len(s) - 1):
            if s[i] == "0":
                zeros += 1
            elif ones > 0:
                ones -= 1
            m = max(m, ones + zeros)

        return m


sol = Solution()
s = "1111"
print(f"str: {s}, max_score: {sol.maxScore(s)}")
