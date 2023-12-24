class Solution:
    def minOperations(self, s: str) -> int:
        count = 0
        chars = list(s)
        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                chars[i] = "1" if chars[i] == "0" else "0"
                count += 1

        chars = list(s)

        chars[0] = "1" if chars[0] == "0" else "0"
        other_count = 1
        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                chars[i] = "1" if chars[i] == "0" else "0"
                other_count += 1

        return min(count, other_count)


sol = Solution()
string = "10010100"
print(f"str: {string}, count: {sol.minOperations(string)}")
