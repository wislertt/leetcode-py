class Solution:
    # Time: O(n)
    # Space: O(1)
    def does_valid_array_exist(self, derived: list[int]) -> bool:
        # Each original value appears exactly twice across the derived XORs,
        # so every pair cancels and the total XOR must be 0.
        total = 0
        for value in derived:
            total ^= value
        return total == 0
