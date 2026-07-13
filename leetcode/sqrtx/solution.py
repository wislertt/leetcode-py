class Solution:
    # Time: O(log x)
    # Space: O(1)
    def my_sqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = 0
        right = x

        while left < right:
            mid = (left + right) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid > x:
                right = mid
            else:
                left = mid + 1

        return left
