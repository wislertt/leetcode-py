class Solution:
    # Time: O(n^2)
    # Space: O(n^2)
    def stone_game(self, piles: list[int]) -> bool:
        n = len(piles)
        # dp[i][j] = max net advantage current player can secure from piles[i..j]
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                pick_left = piles[i] - dp[i + 1][j]
                pick_right = piles[j] - dp[i][j - 1]
                dp[i][j] = max(pick_left, pick_right)
        return dp[0][n - 1] > 0
