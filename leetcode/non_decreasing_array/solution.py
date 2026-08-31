class Solution:
    # Time: O(n)
    # Space: O(1)
    def check_possibility(self, nums: list[int]) -> bool:
        changed = False
        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                continue
            if changed:
                return False
            changed = True
            if i == 0 or nums[i - 1] <= nums[i + 1]:
                nums[i] = nums[i + 1]
            else:
                nums[i + 1] = nums[i]
        return True
