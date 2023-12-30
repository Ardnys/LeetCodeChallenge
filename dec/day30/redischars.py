from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        if n == 1:
            return True
        char_freqs = [0] * 26

        for word in words:
            for char in word:
                char_freqs[ord(char) - ord("a")] += 1

        for freq in char_freqs:
            if freq % n != 0:
                return False
        return True


sol = Solution()
words = ["bc", "abc"]
print(sol.makeEqual(words))
