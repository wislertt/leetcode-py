class Solution:
    # Time: O(n)
    # Space: O(1)
    def number_of_arithmetic_slices(self, nums: list[int]) -> int:
        total = 0
        run = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                run += 1
                total += run
            else:
                run = 0
        return total
