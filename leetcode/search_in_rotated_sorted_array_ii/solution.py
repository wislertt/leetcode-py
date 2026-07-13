class Solution:
    # Time: O(n) worst case (duplicates collapse bounds), O(log n) average
    # Space: O(1)
    def search(self, nums: list[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # Ambiguous boundary: shrink from both ends when all three equal
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:  # left half sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # right half sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False
