class Solution:
    # Time: O(m * log(max(quantities)))
    # Space: O(1)
    def minimized_maximum(self, n: int, quantities: list[int]) -> int:
        lo, hi = 1, max(quantities)
        while lo < hi:
            mid = (lo + hi) // 2
            if sum(-(-q // mid) for q in quantities) <= n:
                hi = mid
            else:
                lo = mid + 1
        return lo
