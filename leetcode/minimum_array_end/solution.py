class Solution:
    # Time: O(1)  # bounded by 64 iterations
    # Space: O(1)
    def min_end(self, n: int, x: int) -> int:
        result = x
        increment = n - 1
        inc_bit = 0
        for bit in range(64):
            if (x >> bit) & 1 == 0:
                if (increment >> inc_bit) & 1:
                    result |= 1 << bit
                inc_bit += 1
        return result
