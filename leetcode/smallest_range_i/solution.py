class Solution:
    # Time: O(n)
    # Space: O(1)
    def smallest_range_i(self, nums: list[int], k: int) -> int:
        return max(0, max(nums) - min(nums) - 2 * k)
