class Solution:
    # Time: O(n)
    # Space: O(n)
    def find_132pattern(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False

        stack: list[int] = []
        third = float("-inf")
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < third:
                return True
            while stack and stack[-1] < nums[i]:
                third = stack.pop()
            stack.append(nums[i])
        return False
