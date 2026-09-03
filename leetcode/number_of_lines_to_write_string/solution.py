class Solution:
    # Time: O(len(s))
    # Space: O(1)
    def number_of_lines(self, widths: list[int], s: str) -> list[int]:
        lines = 1
        used = 0
        for ch in s:
            w = widths[ord(ch) - ord("a")]
            if used + w > 100:
                lines += 1
                used = w
            else:
                used += w
        return [lines, used]
