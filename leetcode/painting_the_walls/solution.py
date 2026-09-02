class Solution:
    # Time: O(n^2)
    # Space: O(n)
    def paint_walls(self, cost: list[int], time: list[int]) -> int:
        n = len(cost)
        # dp[j] = min cost of paid walls so the free painter can cover j walls;
        # a paid wall with time t covers itself plus t free walls.
        inf = 10**18
        dp = [0] + [inf] * n
        for c, t in zip(cost, time, strict=True):
            for j in range(n, 0, -1):
                candidate = dp[max(0, j - t - 1)] + c
                if candidate < dp[j]:
                    dp[j] = candidate
        return dp[n]
