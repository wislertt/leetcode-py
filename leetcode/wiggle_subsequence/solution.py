class Solution:
    # Time: O(n)
    # Space: O(1)
    def wiggle_max_length(self, nums: list[int]) -> int:
        up = down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
        return max(up, down)
