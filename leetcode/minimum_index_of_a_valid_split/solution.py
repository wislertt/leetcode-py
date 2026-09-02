class Solution:
    # Time: O(n)
    # Space: O(1)
    def minimum_index(self, nums: list[int]) -> int:
        dominant = 0
        count = 0
        for num in nums:
            if count == 0:
                dominant = num
                count = 1
            elif num == dominant:
                count += 1
            else:
                count -= 1

        total = 0
        for num in nums:
            if num == dominant:
                total += 1

        left = 0
        for i, num in enumerate(nums):
            if num == dominant:
                left += 1
            right = total - left
            if left * 2 > i + 1 and right * 2 > len(nums) - i - 1:
                return i
        return -1
