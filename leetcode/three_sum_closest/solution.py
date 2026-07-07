class Solution:
    # Time: O(n^2)
    # Space: O(1) (ignoring sort space)
    def three_sum_closest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                # Update closest if this sum is nearer to target
                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum
                if current_sum == target:
                    return current_sum
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest
