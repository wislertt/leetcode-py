class Solution:
    # Time: O(n)
    # Space: O(1)
    def max_alternating_sum(self, nums: list[int]) -> int:
        even = 0
        odd = 0
        for num in nums:
            even, odd = max(even, odd + num), max(odd, even - num)
        return even
