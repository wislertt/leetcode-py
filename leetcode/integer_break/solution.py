class Solution:
    # Time: O(n^2)
    # Space: O(n)
    def integer_break(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1

        for target in range(2, n + 1):
            for part in range(1, target):
                dp[target] = max(dp[target], part * (target - part), part * dp[target - part])

        return dp[n]
