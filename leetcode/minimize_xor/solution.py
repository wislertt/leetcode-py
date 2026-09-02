class Solution:
    # Time: O(log(max(num1, num2)))
    # Space: O(1)
    def minimize_xor(self, num1: int, num2: int) -> int:
        target_bits = bin(num2).count("1")
        x = num1
        cur_bits = bin(x).count("1")

        # Drop the lowest set bits while we have too many.
        while cur_bits > target_bits:
            x &= x - 1
            cur_bits -= 1

        # Otherwise take the lowest clear bits.
        bit = 1
        while cur_bits < target_bits:
            if not x & bit:
                x |= bit
                cur_bits += 1
            bit <<= 1

        return x
