class Solution:
    # Time: O(n)
    # Space: O(1)
    def max_length_between_equal_characters(self, s: str) -> int:
        best = -1
        first: dict[str, int] = {}
        for i, ch in enumerate(s):
            j = first.setdefault(ch, i)
            if j != i:
                best = max(best, i - j - 1)
        return best
