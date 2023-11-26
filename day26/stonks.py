from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        m = 0
        while j < len(prices):
            if prices[i] > prices[j]:
                i = j
                j += 1
            else:
                profit = prices[j] - prices[i]
                if profit > m:
                    m = profit
                j += 1

        return m


prices = [7, 1, 5, 3, 6, 4]
sol = Solution()
print(f"prices: {prices}, max profit: {sol.maxProfit(prices)}")
