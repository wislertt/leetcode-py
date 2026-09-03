class Solution:
    # Time: O(n)
    # Space: O(1)
    def is_one_bit_character(self, bits: list[int]) -> bool:
        ones = 0
        for bit in reversed(bits[:-1]):
            if bit == 0:
                break
            ones += 1
        return ones % 2 == 0
