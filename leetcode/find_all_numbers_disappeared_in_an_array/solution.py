class Solution:
    # Time: O(n)
    # Space: O(1) excluding the output list
    def find_disappeared_numbers(self, nums: list[int]) -> list[int]:
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        return [i + 1 for i, num in enumerate(nums) if num > 0]
