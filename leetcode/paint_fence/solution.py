class Solution:
    # Time: O(n)
    # Space: O(1)
    def num_ways(self, n: int, k: int) -> int:
        if n == 1:
            return k
        same, diff = k, k * (k - 1)
        for _ in range(n - 2):
            same, diff = diff, (same + diff) * (k - 1)
        return same + diff
