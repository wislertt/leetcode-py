class Solution:
    # Time: O(log n)
    # Space: O(1)
    def search_range(self, nums: list[int], target: int) -> list[int]:
        def find_left(nums: list[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left if left < len(nums) and nums[left] == target else -1

        def find_right(nums: list[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right if right >= 0 and nums[right] == target else -1

        if not nums:
            return [-1, -1]

        left_pos = find_left(nums, target)
        if left_pos == -1:
            return [-1, -1]

        right_pos = find_right(nums, target)
        return [left_pos, right_pos]
