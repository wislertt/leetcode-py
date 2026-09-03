class Solution:
    # Time: O(1) (at most 31 iterations for the 32-bit constraint)
    # Space: O(1)
    def has_alternating_bits(self, n: int) -> bool:
        # x = n ^ (n >> 1) has every bit set iff adjacent bits all differ;
        # adding the carry back onto x must produce the next power of two.
        x = n ^ (n >> 1)
        return x & (x + 1) == 0
