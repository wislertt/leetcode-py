class Solution:
    # Time: O(n)
    # Space: O(1)
    def wiggle_sort(self, nums: list[int]) -> None:
        for i in range(1, len(nums)):
            if (i % 2 == 1 and nums[i] < nums[i - 1]) or (i % 2 == 0 and nums[i] > nums[i - 1]):
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
