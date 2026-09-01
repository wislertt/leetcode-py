class Solution:
    # Time: O(n log M) where n = len(ribbons), M = max(ribbons)
    # Space: O(1)
    def max_length(self, ribbons: list[int], k: int) -> int:
        left, right = 1, max(ribbons)
        while left <= right:
            mid = (left + right) // 2
            if sum(r // mid for r in ribbons) >= k:
                left = mid + 1
            else:
                right = mid - 1
        return right
