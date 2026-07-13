class Solution:
    # Time: O(n)
    # Space: O(1)
    def valid_palindrome(self, s: str) -> bool:
        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # Mismatch: try skipping either the left or the right character.
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
            left += 1
            right -= 1
        return True
