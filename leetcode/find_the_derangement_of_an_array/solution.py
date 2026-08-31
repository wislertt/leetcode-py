class Solution:
    # Time: O(n)
    # Space: O(1)
    def find_derangement(self, n: int) -> int:
        mod = 1_000_000_007
        if n == 1:
            return 0
        a, b = 1, 0  # D(1) = 0 carried via a = D(k-1)
        for k in range(2, n + 1):
            a, b = b, (k - 1) * (a + b) % mod
        return b % mod
