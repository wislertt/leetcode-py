class Solution:
    # Time: O(n)
    # Space: O(n)
    def divide_array_into_equal_pairs(self, nums: list[int]) -> bool:
        counts: dict[int, int] = {}
        for num in nums:
            if num in counts:
                del counts[num]
            else:
                counts[num] = 1
        return not counts
