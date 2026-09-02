class Solution:
    # Time: O(n * log(max(nums)))
    # Space: O(1)
    def minimum_size(self, nums: list[int], max_operations: int) -> int:
        def ops_needed(penalty: int) -> int:
            return sum((n - 1) // penalty for n in nums)

        lo, hi = 1, max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if ops_needed(mid) <= max_operations:
                hi = mid
            else:
                lo = mid + 1
        return lo
