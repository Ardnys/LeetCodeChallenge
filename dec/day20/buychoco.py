from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        if len(prices) < 2:
            return money
        prices.sort()

        if prices[0] + prices[1] > money:
            return money
        return money - (prices[0] + prices[1])


sol = Solution()
prices = [3, 2, 2]
moni = 3
print(f"prices: {prices} moni: {moni} -> left: {sol.buyChoco(prices, moni)}")
