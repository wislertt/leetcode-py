class Solution:
    # Time: O(n)
    # Space: O(1)
    def min_operations(self, s: str) -> int:
        start_zero = 0  # changes to reach pattern 0101...
        for i, char in enumerate(s):
            if int(char) != i % 2:
                start_zero += 1
        return min(start_zero, len(s) - start_zero)
