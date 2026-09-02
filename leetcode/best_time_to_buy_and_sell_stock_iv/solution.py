class Solution:
    # Time: O(n * min(k, n // 2))
    # Space: O(min(k, n // 2))
    def max_profit(self, k: int, prices: list[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        # Each transaction uses at least two days, so more trades than n // 2
        # degenerate into the unlimited-transaction case.
        limit = min(k, n // 2)
        buy = [-(10**9)] * (limit + 1)
        sell = [0] * (limit + 1)
        for price in prices:
            for j in range(1, limit + 1):
                buy[j] = max(buy[j], sell[j - 1] - price)
                sell[j] = max(sell[j], buy[j] + price)
        return sell[limit]
