class Solution:
    # Time: O(n)
    # Space: O(1)
    def min_cost_climbing_stairs(self, cost: list[int]) -> int:
        # dp[i] = min cost to reach step i (top is index n).
        # Start at step 0 or 1 for free, so dp[0] = dp[1] = 0.
        prev_two, prev_one = 0, 0  # dp[i-2], dp[i-1]
        for step_cost in cost:
            current = step_cost + min(prev_one, prev_two)
            prev_two, prev_one = prev_one, current
        # Top reached from either of the last two steps (already paid)
        return min(prev_one, prev_two)
