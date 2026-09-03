class Solution:
    # Time: O(n^3 / k * k) = O(n^3) over intervals with k-step splits
    # Space: O(n^2)
    def merge_stones(self, stones: list[int], k: int) -> int:
        n = len(stones)
        if n == 1:
            return 0
        if (n - 1) % (k - 1) != 0:
            return -1

        prefix = [0] * (n + 1)
        for i, stones_count in enumerate(stones):
            prefix[i + 1] = prefix[i] + stones_count

        # dp[i][j] = min cost to merge stones[i..j] down to the minimum possible pile count
        dp = [[0] * n for _ in range(n)]
        for length in range(k, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = min(dp[i][mid] + dp[mid + 1][j] for mid in range(i, j, k - 1))
                if (j - i) % (k - 1) == 0:
                    dp[i][j] += prefix[j + 1] - prefix[i]
        return dp[0][n - 1]
