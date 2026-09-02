class Solution:
    # Time: O(n)
    # Space: O(min(n, index_diff))
    def contains_nearby_almost_duplicate(
        self, nums: list[int], index_diff: int, value_diff: int
    ) -> bool:
        width = value_diff + 1
        buckets: dict[int, int] = {}
        for i, num in enumerate(nums):
            if i > index_diff:
                del buckets[nums[i - index_diff - 1] // width]
            bucket = num // width
            if bucket in buckets:
                return True
            if bucket - 1 in buckets and num - buckets[bucket - 1] <= value_diff:
                return True
            if bucket + 1 in buckets and buckets[bucket + 1] - num <= value_diff:
                return True
            buckets[bucket] = num
        return False
