class Solution:
    # Time: O(n)
    # Space: O(1)
    def single_number(self, nums: list[int]) -> int:
        ones = 0
        twos = 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones
