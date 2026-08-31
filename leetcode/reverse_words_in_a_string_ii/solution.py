class Solution:
    # Time: O(n)
    # Space: O(1)
    def reverse_words(self, s: list[str]) -> None:
        def reverse(left: int, right: int) -> None:
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        reverse(0, len(s) - 1)
        start = 0
        for i, ch in enumerate(s):
            if ch == " ":
                reverse(start, i - 1)
                start = i + 1
        reverse(start, len(s) - 1)
