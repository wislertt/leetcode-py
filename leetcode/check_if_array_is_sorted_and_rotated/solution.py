class Solution:
    # Time: O(n)
    # Space: O(1)
    def check(self, nums: list[int]) -> bool:
        breaks = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                breaks += 1
                if breaks > 1:
                    return False
        return True
