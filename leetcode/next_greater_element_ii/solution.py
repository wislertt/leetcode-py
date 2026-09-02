class Solution:
    # Time: O(n)
    # Space: O(n)
    def next_greater_elements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [-1] * n
        stack: list[int] = []
        for i in range(2 * n):
            idx = i % n
            while stack and nums[stack[-1]] < nums[idx]:
                result[stack.pop()] = nums[idx]
            if i < n:
                stack.append(idx)
        return result
