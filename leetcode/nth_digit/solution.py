class Solution:
    # Time: O(log n)
    # Space: O(1)
    def find_nth_digit(self, n: int) -> int:
        digits = 1
        count = 9
        start = 1
        while n > digits * count:
            n -= digits * count
            digits += 1
            count *= 10
            start *= 10
        num = start + (n - 1) // digits
        return int(str(num)[(n - 1) % digits])
