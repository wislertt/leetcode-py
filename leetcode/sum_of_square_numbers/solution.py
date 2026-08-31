from math import isqrt


class Solution:
    # Time: O(sqrt(c))
    # Space: O(1)
    def judge_square_sum(self, c: int) -> bool:
        left, right = 0, isqrt(c)
        while left <= right:
            total = left * left + right * right
            if total == c:
                return True
            if total < c:
                left += 1
            else:
                right -= 1
        return False
