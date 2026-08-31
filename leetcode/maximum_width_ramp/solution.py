class Solution:
    # Time: O(n)
    # Space: O(n)
    def max_width_ramp(self, nums: list[int]) -> int:
        stack: list[int] = []
        for i, num in enumerate(nums):
            if not stack or num < nums[stack[-1]]:
                stack.append(i)
        width = 0
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                width = max(width, j - stack.pop())
        return width
