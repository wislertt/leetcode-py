class Solution:
    # Time: O(n^2)
    # Space: O(n)
    def num_perms_di_sequence(self, s: str) -> int:
        mod = 1_000_000_007
        n = len(s)
        # dp[j] = ways to place values so far where the last value is the
        # j-th smallest of the values still unused.
        dp = [1] * (n + 1)
        for i, ch in enumerate(s):
            m = n + 1 - i
            ndp = [0] * (m - 1)
            if ch == "I":
                # next value is larger: its rank is at least the last rank
                run = 0
                for j in range(m - 1):
                    run = (run + dp[j]) % mod
                    ndp[j] = run
            else:
                # next value is smaller: its rank is strictly below the last rank
                suf = 0
                for j in range(m - 2, -1, -1):
                    suf = (suf + dp[j + 1]) % mod
                    ndp[j] = suf
            dp = ndp
        return dp[0]
