class Solution:
    # Time: O(n)
    # Space: O(1)
    def dominant_index(self, nums: list[int]) -> int:
        largest = second = -1
        largest_idx = -1
        for i, num in enumerate(nums):
            if num > largest:
                largest_idx = i
                second = largest
                largest = num
            elif num > second:
                second = num
        if largest >= 2 * second:
            return largest_idx
        return -1
