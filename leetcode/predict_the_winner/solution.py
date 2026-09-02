class Solution:
    # Time: O(n^2)
    # Space: O(n^2)
    def predict_the_winner(self, nums: list[int]) -> bool:
        n = len(nums)
        # dp[l][r] is the best score difference (current player minus opponent)
        # achievable on the subarray nums[l:r + 1].
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                take_left = nums[left] - dp[left + 1][right]
                take_right = nums[right] - dp[left][right - 1]
                dp[left][right] = max(take_left, take_right)
        return dp[0][n - 1] >= 0
