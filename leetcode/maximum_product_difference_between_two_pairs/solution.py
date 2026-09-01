class Solution:
    # Time: O(n)
    # Space: O(1)
    def max_product_difference(self, nums: list[int]) -> int:
        max1 = max2 = 0
        min1 = min2 = 10_001
        for num in nums:
            if num > max1:
                max1, max2 = num, max1
            elif num > max2:
                max2 = num
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num
        return max1 * max2 - min1 * min2
