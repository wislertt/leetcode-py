class Solution:
    # Time: O(n)
    # Space: O(1)
    def minimum_length(self, s: str) -> int:
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            ch = s[left]
            while left <= right and s[left] == ch:
                left += 1
            while left <= right and s[right] == ch:
                right -= 1
        return right - left + 1
