class Solution:
    # Time: O(log n) where n is the value of right (number of bits)
    # Space: O(1)
    def range_bitwise_and(self, left: int, right: int) -> int:
        # The AND of the range equals the common most-significant bit prefix
        shift = 0

        while left < right:
            left >>= 1
            right >>= 1
            shift += 1

        return left << shift
