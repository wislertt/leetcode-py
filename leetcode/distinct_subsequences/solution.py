class Solution:
    # Time: O(m * n)
    # Space: O(n) using a single rolling row
    def num_distinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        # dp[j] = number of ways to form t[:j] from the s prefix seen so far
        dp = [0] * (n + 1)
        dp[0] = 1  # empty t matches any s prefix exactly once
        for i in range(1, m + 1):
            # Iterate j backwards so dp[j-1] is still from the previous row
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
        return dp[n]
