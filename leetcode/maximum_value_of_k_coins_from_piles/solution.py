class Solution:
    # Time: O(total_coins * k)
    # Space: O(k)
    def max_value_of_coins(self, piles: list[list[int]], k: int) -> int:
        dp = [0] * (k + 1)
        for pile in piles:
            prefix = [0]
            for value in pile:
                prefix.append(prefix[-1] + value)
            new_dp = dp[:]
            for taken in range(1, k + 1):
                best = new_dp[taken]
                for use in range(min(taken, len(prefix) - 1) + 1):
                    candidate = dp[taken - use] + prefix[use]
                    if candidate > best:
                        best = candidate
                new_dp[taken] = best
            dp = new_dp
        return dp[k]
