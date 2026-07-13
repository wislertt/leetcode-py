class Solution:
    # Two pointers - slow tracks insertion position for next non-zero
    # Fast scans array; swap non-zero to front, preserving relative order
    # Time: O(n)
    # Space: O(1)
    def move_zeroes(self, nums: list[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
