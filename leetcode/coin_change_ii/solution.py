class Solution:
    # Time: O(n * amount)
    # Space: O(amount)
    def change(self, amount: int, coins: list[int]) -> int:
        # dp[a] = number of combinations summing to a
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]
        return dp[amount]
