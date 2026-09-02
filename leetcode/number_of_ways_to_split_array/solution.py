class Solution:
    # Time: O(n)
    # Space: O(1)
    def ways_to_split_array(self, nums: list[int]) -> int:
        total = sum(nums)
        left = 0
        valid = 0
        for i in range(len(nums) - 1):
            left += nums[i]
            if left >= total - left:
                valid += 1
        return valid
