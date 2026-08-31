class Solution:
    # Time: O(n^2)
    # Space: O(n)
    def minimum_total(self, triangle: list[list[int]]) -> int:
        dp = triangle[-1][:]
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(row + 1):
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
        return dp[0]
