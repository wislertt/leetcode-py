class Solution:
    # Time: O(n * k)
    # Space: O(k)
    def rearrange_sticks(self, n: int, k: int) -> int:
        mod = 1_000_000_007
        prev = [0] * (k + 1)
        prev[0] = 1
        for i in range(1, n + 1):
            curr = [0] * (k + 1)
            hi = min(i, k)
            for j in range(1, hi + 1):
                curr[j] = ((i - 1) * prev[j] + prev[j - 1]) % mod
            prev = curr
        return prev[k]
