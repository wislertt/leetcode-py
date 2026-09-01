class Solution:
    # Time: O(log n)
    # Space: O(1)
    def minimum_one_bit_operations(self, n: int) -> int:
        # Valid states form a Gray code sequence ordered by operation count, so the
        # distance from n to 0 is the Gray-to-binary decode of n.
        result = 0
        while n:
            result ^= n
            n >>= 1
        return result
