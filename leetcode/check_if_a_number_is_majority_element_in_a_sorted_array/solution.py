class Solution:
    # Time: O(log n)
    # Space: O(1)
    def is_majority_element(self, nums: list[int], target: int) -> bool:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        candidate = left + len(nums) // 2
        return candidate < len(nums) and nums[candidate] == target
