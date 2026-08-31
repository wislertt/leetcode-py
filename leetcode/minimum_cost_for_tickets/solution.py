class Solution:
    # Time: O(D) where D is the last travel day
    # Space: O(D)
    def min_cost_tickets(self, days: list[int], costs: list[int]) -> int:
        dayset = set(days)
        last = days[-1]
        dp = [0] * (last + 1)
        for day in range(1, last + 1):
            if day not in dayset:
                dp[day] = dp[day - 1]
            else:
                dp[day] = min(
                    dp[day - 1] + costs[0],
                    dp[max(day - 7, 0)] + costs[1],
                    dp[max(day - 30, 0)] + costs[2],
                )
        return dp[last]
