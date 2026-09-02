class Solution:
    # Time: O(n)
    # Space: O(1)
    def array_sign(self, nums: list[int]) -> int:
        sign = 1
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                sign = -sign
        return sign
