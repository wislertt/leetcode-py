class Solution:
    # Time: O(n * k)
    # Space: O(n)
    def max_sum_after_partitioning(self, arr: list[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            best = 0
            mx = 0
            for length in range(1, min(k, i) + 1):
                mx = max(mx, arr[i - length])
                best = max(best, dp[i - length] + mx * length)
            dp[i] = best
        return dp[n]
