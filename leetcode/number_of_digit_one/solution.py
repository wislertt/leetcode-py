class Solution:
    # Time: O(log10(n))
    # Space: O(1)
    def count_digit_one(self, n: int) -> int:
        total = 0
        place = 1
        while place <= n:
            high = n // (place * 10)
            cur = (n // place) % 10
            low = n % place
            if cur == 0:
                total += high * place
            elif cur == 1:
                total += high * place + low + 1
            else:
                total += (high + 1) * place
            place *= 10
        return total
