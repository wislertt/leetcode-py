class Solution:
    # Time: O(log n)
    # Space: O(log n)
    def new_integer(self, n: int) -> int:
        result = 0
        place = 1
        while n > 0:
            result += (n % 9) * place
            place *= 10
            n //= 9
        return result
