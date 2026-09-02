class Solution:
    # Time: O(n)
    # Space: O(1)
    def min_number_operations(self, target: list[int]) -> int:
        operations = 0
        prev = 0
        for value in target:
            if value > prev:
                operations += value - prev
            prev = value
        return operations
