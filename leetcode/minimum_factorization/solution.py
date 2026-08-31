class Solution:
    # Time: O(log(num) * 8)
    # Space: O(log(num))
    def smallest_factorization(self, num: int) -> int:
        if num < 10:
            return num
        digits: list[int] = []
        for d in range(9, 1, -1):
            while num % d == 0:
                num //= d
                digits.append(d)
        if num != 1:
            return 0
        result = 0
        for d in reversed(digits):
            result = result * 10 + d
        return result if result <= 2**31 - 1 else 0
