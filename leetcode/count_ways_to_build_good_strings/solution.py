MOD = 1_000_000_007


class Solution:
    # Time: O(high)
    # Space: O(high)
    def count_good_strings(self, low: int, high: int, zero: int, one: int) -> int:
        # dp[i] = number of distinct strings of length i buildable from the empty string
        dp = [0] * (high + 1)
        dp[0] = 1
        for length in range(1, high + 1):
            total = dp[length - zero] if length >= zero else 0
            if length >= one:
                total += dp[length - one]
            dp[length] = total % MOD
        return sum(dp[low : high + 1]) % MOD
