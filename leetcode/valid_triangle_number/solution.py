class Solution:
    # Time: O(n^2)
    # Space: O(1) extra (sorting not counted)
    def triangle_number(self, nums: list[int]) -> int:
        nums = sorted(nums)
        count = 0
        for k in range(len(nums) - 1, 1, -1):
            left, right = 0, k - 1
            while left < right:
                if nums[left] + nums[right] > nums[k]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count
