class Solution:
    # Time: O(log n)
    # Space: O(1)
    def h_index(self, citations: list[int]) -> int:
        n = len(citations)
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if citations[mid] >= n - mid:
                hi = mid - 1
            else:
                lo = mid + 1
        return n - lo
