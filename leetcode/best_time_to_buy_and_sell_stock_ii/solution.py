class Solution:
    # Time: O(n)
    # Space: O(1)
    def max_profit(self, prices: list[int]) -> int:
        profit = 0

        for day in range(1, len(prices)):
            # Capture every positive upswing; sum equals any multi-day strategy
            if prices[day] > prices[day - 1]:
                profit += prices[day] - prices[day - 1]

        return profit
