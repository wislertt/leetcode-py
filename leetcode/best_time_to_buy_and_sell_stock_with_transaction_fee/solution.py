class Solution:
    # Time: O(n)
    # Space: O(1)
    def max_profit(self, prices: list[int], fee: int) -> int:
        cash = 0
        hold = -prices[0]
        for price in prices[1:]:
            cash = max(cash, hold + price - fee)
            hold = max(hold, cash - price)
        return cash
