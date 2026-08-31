class Solution:
    # Time: O(n + k)
    # Space: O(n)
    def new21_game(self, n: int, k: int, max_pts: int) -> float:
        if k == 0:
            return 1.0
        # dp[i]: probability of ending with exactly i points; dp[i] is the
        # mean of dp[i - max_pts .. min(i - 1, k - 1)], kept as a running
        # window sum since only pre-stop states seed further draws
        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        window = 1.0
        for i in range(1, n + 1):
            dp[i] = window / max_pts
            if i < k:
                window += dp[i]
            if i - max_pts >= 0 and i - max_pts < k:
                window -= dp[i - max_pts]
        return sum(dp[k : n + 1])
