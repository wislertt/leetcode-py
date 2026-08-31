class Solution:
    # Time: O(n)
    # Space: O(1)
    def find_missing_ranges(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        ranges: list[list[int]] = []
        prev = lower - 1
        for i in range(len(nums) + 1):
            curr = nums[i] if i < len(nums) else upper + 1
            if curr - prev >= 2:
                ranges.append([prev + 1, curr - 1])
            prev = curr
        return ranges
