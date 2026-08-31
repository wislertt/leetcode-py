class Solution:
    # Time: O(log10 n)
    # Space: O(1)
    def confusing_number(self, n: int) -> bool:
        rotated = [0, 1, -1, -1, -1, -1, 9, -1, 8, 6]
        x, y = n, 0
        while x:
            x, digit = divmod(x, 10)
            if rotated[digit] < 0:
                return False
            y = y * 10 + rotated[digit]
        return y != n
