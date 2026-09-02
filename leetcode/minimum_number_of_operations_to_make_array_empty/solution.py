from collections import Counter


class Solution:
    # Time: O(n)
    # Space: O(n)
    def min_operations(self, nums: list[int]) -> int:
        operations = 0
        for count in Counter(nums).values():
            if count == 1:
                return -1
            groups, remainder = divmod(count, 3)
            operations += groups + (1 if remainder else 0)
        return operations
