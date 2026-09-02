from math import gcd


class Solution:
    # Time: O(2^m * m^2) where m = len(nums) = 2n <= 14
    # Space: O(2^m)
    def max_score(self, nums: list[int]) -> int:
        m = len(nums)
        gcd_table = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(i + 1, m):
                gcd_table[i][j] = gcd_table[j][i] = gcd(nums[i], nums[j])

        full = (1 << m) - 1
        dp = [0] * (1 << m)
        for mask in range(full):
            op = mask.bit_count() // 2 + 1
            for i in range(m):
                if mask >> i & 1:
                    continue
                for j in range(i + 1, m):
                    if mask >> j & 1:
                        continue
                    nxt = mask | 1 << i | 1 << j
                    dp[nxt] = max(dp[nxt], dp[mask] + op * gcd_table[i][j])
        return dp[full]
