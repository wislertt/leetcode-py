class Solution:
    # Time: O(n)
    # Space: O(n)
    def sorted_squares(self, nums: list[int]) -> list[int]:
        result: list[int] = [0] * len(nums)
        left, right = 0, len(nums) - 1
        index = len(nums) - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[index] = nums[left] * nums[left]
                left += 1
            else:
                result[index] = nums[right] * nums[right]
                right -= 1
            index -= 1
        return result
