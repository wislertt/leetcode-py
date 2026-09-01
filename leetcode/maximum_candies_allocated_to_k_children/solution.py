class Solution:
    # Time: O(n * log(max(candies)))
    # Space: O(1)
    def maximum_candies(self, candies: list[int], k: int) -> int:
        lo, hi = 1, max(candies)
        while lo <= hi:
            mid = (lo + hi) // 2
            if sum(pile // mid for pile in candies) >= k:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi
