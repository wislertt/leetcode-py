class Solution:
    # Time: O(n * k)
    # Space: O(k)
    def k_inverse_pairs(self, n: int, k: int) -> int:
        mod = 1_000_000_007
        # dp[j]: arrays using values 1..i with exactly j inverse pairs.
        dp = [0] * (k + 1)
        dp[0] = 1
        for i in range(2, n + 1):
            prefix = [0] * (k + 2)
            for j in range(k + 1):
                prefix[j + 1] = (prefix[j] + dp[j]) % mod
            # Inserting value i adds between 0 and i-1 new inverse pairs.
            new = [0] * (k + 1)
            for j in range(k + 1):
                low = max(0, j - (i - 1))
                new[j] = (prefix[j + 1] - prefix[low]) % mod
            dp = new
        return dp[k]
