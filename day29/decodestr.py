class Solution:
    def decodeString(self, s: str) -> str:
        stacc = []
        times = 0
        curr_str = ""
        for c in s:
            if c == "[":
                stacc.append(curr_str)
                stacc.append(times)
                times = 0
                curr_str = ""
            elif c.isdigit():
                times = times * 10 + int(c)  # for multi digit numbers
            elif c == "]":
                num = stacc.pop()
                prev_str = stacc.pop()
                curr_str = prev_str + num * curr_str
            else:
                curr_str += c
        return curr_str


sol = Solution()
s = "3[a2[c]]"
print(f"encoded {s} -> decoded {sol.decodeString(s)}")
