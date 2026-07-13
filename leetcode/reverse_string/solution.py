class Solution:
    # Time: O(n)
    # Space: O(1)
    def reverse_string(self, s: list[str]) -> None:
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
