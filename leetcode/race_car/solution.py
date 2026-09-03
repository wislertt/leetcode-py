class Solution:
    # Time: O(target * log(target))
    # Space: O(target)
    def racecar(self, target: int) -> int:
        dp = [0] * (target + 1)
        for t in range(1, target + 1):
            k = t.bit_length()
            if t == 2**k - 1:
                dp[t] = k
                continue
            best = k + 1 + dp[2**k - 1 - t]
            for j in range(k - 1):
                nxt = t - 2 ** (k - 1) + 2**j
                best = min(best, k + j + 1 + dp[nxt])
            dp[t] = best
        return dp[target]
