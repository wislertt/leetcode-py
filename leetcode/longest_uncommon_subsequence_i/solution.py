class Solution:
    # Time: O(min(len(a), len(b)))
    # Space: O(1)
    def find_luslength(self, a: str, b: str) -> int:
        # A whole string is always a subsequence of itself, so if a != b the
        # longer (or either, on a tie) string cannot be a subsequence of the
        # other: equal-length subsequences imply equality. If a == b every
        # subsequence is shared, so nothing is uncommon.
        return max(len(a), len(b)) if a != b else -1
