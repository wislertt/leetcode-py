class Solution:
    # Time: O(m * n)
    # Space: O(n)
    def max_points(self, points: list[list[int]]) -> int:
        n = len(points[0])
        dp = list(points[0])
        for row in points[1:]:
            left = [0] * n
            left[0] = dp[0]
            for c in range(1, n):
                left[c] = max(left[c - 1] - 1, dp[c])
            right = [0] * n
            right[n - 1] = dp[n - 1]
            for c in range(n - 2, -1, -1):
                right[c] = max(right[c + 1] - 1, dp[c])
            dp = [max(left[c], right[c]) + row[c] for c in range(n)]
        return max(dp)
