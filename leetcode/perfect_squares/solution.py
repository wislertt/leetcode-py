class Solution:
    # Time: O(n * sqrt(n))
    # Space: O(n)
    def num_squares(self, n: int) -> int:
        dp = [0] + [n + 1] * n
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]
