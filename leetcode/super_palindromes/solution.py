class Solution:
    # Time: O(R^0.5 * log R) where R = int(right), over ~2 * 10^(d/2) palindrome roots
    # Space: O(1)
    def super_palindromes_in_range(self, left: str, right: str) -> int:
        lo, hi = int(left), int(right)
        count = 0
        # Palindromic roots with up to 9 digits: their squares cover up to 10^18 - 1.
        # Roots are visited in increasing order, so we can stop once we pass hi.
        for length in range(1, 10):
            half_len = (length + 1) // 2
            for half in range(10 ** (half_len - 1), 10**half_len):
                digits = str(half)
                if length % 2 == 0:
                    root = int(digits + digits[::-1])
                else:
                    root = int(digits + digits[-2::-1])
                square = root * root
                if square > hi:
                    return count
                if square >= lo and str(square) == str(square)[::-1]:
                    count += 1
        return count
