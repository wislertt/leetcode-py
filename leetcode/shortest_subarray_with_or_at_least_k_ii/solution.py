class Solution:
    # Time: O(n * 30)
    # Space: O(30)
    def minimum_subarray_length(self, nums: list[int], k: int) -> int:
        best = len(nums) + 1
        counts = [0] * 30
        left = 0
        for right, value in enumerate(nums):
            for bit in range(30):
                if (value >> bit) & 1:
                    counts[bit] += 1
            while left <= right and self._or_value(counts) >= k:
                best = min(best, right - left + 1)
                for bit in range(30):
                    if (nums[left] >> bit) & 1:
                        counts[bit] -= 1
                left += 1
        return -1 if best == len(nums) + 1 else best

    def _or_value(self, counts: list[int]) -> int:
        value = 0
        for bit, count in enumerate(counts):
            if count:
                value |= 1 << bit
        return value
