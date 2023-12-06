class Solution:
    def totalMoney(self, n: int) -> int:
        # there's a constant time solution but too much math that one
        sum = 0
        starting_moni = 0
        for i in range(1, n + 1):
            uh = (i % 7) + starting_moni
            if i % 7 == 0:
                uh = 7 + starting_moni
                starting_moni += 1
                # print(f"{uh}")
                sum += uh
                continue

            # print(f"{uh} + ", end="")

            # print(f"index: {i} -> {uh}")
            sum += uh

        return sum


sol = Solution()
sol.totalMoney(20)
