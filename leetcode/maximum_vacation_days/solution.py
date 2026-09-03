class Solution:
    # Time: O(k * n^2)
    # Space: O(n)
    def max_vacation_days(self, flights: list[list[int]], days: list[list[int]]) -> int:
        n = len(flights)
        k = len(days[0])
        # dp[j] = best vacation total ending week w in city j; -1 marks unreachable
        dp = [-1] * n
        dp[0] = 0
        for week in range(k):
            ndp = [-1] * n
            for j in range(n):
                best = -1
                for i in range(n):
                    if dp[i] < 0:
                        continue
                    if i == j or flights[i][j] == 1:
                        best = max(best, dp[i])
                if best >= 0:
                    ndp[j] = best + days[j][week]
            dp = ndp
        return max(dp)
