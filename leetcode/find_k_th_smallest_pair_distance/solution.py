from bisect import bisect_right


class Solution:
    # Time: O(n log n + n log W) where W = max(nums) - min(nums)
    # Space: O(n)
    def smallest_distance_pair(self, nums: list[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)

        def count_pairs_within(dist: int) -> int:
            count = 0
            for i in range(n):
                count += bisect_right(nums, nums[i] + dist, lo=i + 1) - (i + 1)
            return count

        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if count_pairs_within(mid) >= k:
                high = mid
            else:
                low = mid + 1
        return low
