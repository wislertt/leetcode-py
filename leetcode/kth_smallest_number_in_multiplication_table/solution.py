class Solution:
    # Time: O(m * log(m * n))
    # Space: O(1)
    def find_kth_number(self, m: int, n: int, k: int) -> int:
        # Ensure the per-row count loop iterates over the smaller dimension.
        if m > n:
            m, n = n, m

        def count_le(x: int) -> int:
            return sum(min(x // i, n) for i in range(1, m + 1))

        lo, hi = 1, m * n
        while lo < hi:
            mid = (lo + hi) // 2
            if count_le(mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo
