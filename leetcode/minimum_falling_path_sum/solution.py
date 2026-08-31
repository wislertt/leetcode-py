class Solution:
    # Time: O(n^2)
    # Space: O(n)
    def min_falling_path_sum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        dp = matrix[0][:]
        for row in range(1, n):
            new_dp = [0] * n
            for col in range(n):
                best = dp[col]
                if col > 0:
                    best = min(best, dp[col - 1])
                if col < n - 1:
                    best = min(best, dp[col + 1])
                new_dp[col] = matrix[row][col] + best
            dp = new_dp
        return min(dp)
