class Solution:
    # Time: O(log n)
    # Space: O(log n)
    def integer_replacement(self, n: int) -> int:
        ops = 0
        while n != 1:
            if n % 2 == 0:
                n //= 2
            elif n == 3 or n % 4 == 1:
                n -= 1
            else:
                n += 1
            ops += 1
        return ops
