class Solution:
    # Time: O(m * n) — one pass over the matrix
    # Space: O(n) — single-row DP array
    def maximal_square(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        dp = [0] * (cols + 1)
        max_side = 0
        prev = 0  # holds dp[i-1][j-1] during the in-place update

        for row in matrix:
            for j in range(cols):
                temp = dp[j + 1]
                if row[j] == "1":
                    dp[j + 1] = min(dp[j + 1], dp[j], prev) + 1
                    max_side = max(max_side, dp[j + 1])
                else:
                    dp[j + 1] = 0
                prev = temp

        return max_side * max_side
