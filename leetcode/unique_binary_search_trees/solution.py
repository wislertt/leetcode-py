class Solution:
    # Time: O(n^2)
    # Space: O(n)
    def num_trees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for nodes in range(1, n + 1):
            for left in range(nodes):
                dp[nodes] += dp[left] * dp[nodes - 1 - left]
        return dp[n]
