class Solution:
    # Time: O(n log m) where m = max(nums)
    # Space: O(1)
    def min_capability(self, nums: list[int], k: int) -> int:
        def can_steal(cap: int) -> bool:
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= cap:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= k

        lo, hi = min(nums), max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if can_steal(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
