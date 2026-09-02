class Solution:
    # Time: O(log(n)^2)
    # Space: O(1)
    def divide(self, dividend: int, divisor: int) -> int:
        int_min, int_max = -(2**31), 2**31 - 1
        negative = (dividend < 0) != (divisor < 0)
        magnitude_a = abs(dividend)
        magnitude_b = abs(divisor)

        quotient = 0
        while magnitude_a >= magnitude_b:
            shift = 0
            while magnitude_a >= (magnitude_b << (shift + 1)):
                shift += 1
            quotient += 1 << shift
            magnitude_a -= magnitude_b << shift
        if negative:
            quotient = -quotient
        return max(int_min, min(int_max, quotient))
