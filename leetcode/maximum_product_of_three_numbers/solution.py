class Solution:
    # Time: O(n)
    # Space: O(1)
    def maximum_product(self, nums: list[int]) -> int:
        max1 = max2 = max3 = -(10**18)
        min1 = min2 = 10**18
        for num in nums:
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num
        return max(max1 * max2 * max3, max1 * min1 * min2)
