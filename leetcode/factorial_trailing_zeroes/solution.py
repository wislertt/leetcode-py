class Solution:
    # Time: O(log n) (base 5)
    # Space: O(1)
    def trailing_zeroes(self, n: int) -> int:
        zero_count = 0
        while n > 0:
            n //= 5
            zero_count += n
        return zero_count
