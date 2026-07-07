class Solution:
    # Time: O(log10(n)) - process half the digits
    # Space: O(1)
    def is_palindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # Even length: x == reversed_half
        # Odd length: x == reversed_half // 10 (drop middle digit)
        return x == reversed_half or x == reversed_half // 10
