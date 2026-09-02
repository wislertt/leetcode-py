class Solution:
    # Time: O(n)
    # Space: O(n)
    def max_sum_min_product(self, nums: list[int]) -> int:
        mod = 1_000_000_007
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        stack: list[int] = []
        best = 0
        for i, num in enumerate([*nums, 0]):
            while stack and nums[stack[-1]] >= num:
                height = nums[stack.pop()]
                left = stack[-1] if stack else -1
                best = max(best, height * (prefix[i] - prefix[left + 1]))
            stack.append(i)
        return best % mod
