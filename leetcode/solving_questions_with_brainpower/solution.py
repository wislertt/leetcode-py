class Solution:
    # Time: O(n)
    # Space: O(n)
    def most_points(self, questions: list[list[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            points, power = questions[i]
            nxt = min(i + power + 1, n)
            dp[i] = max(dp[i + 1], points + dp[nxt])
        return dp[0]
