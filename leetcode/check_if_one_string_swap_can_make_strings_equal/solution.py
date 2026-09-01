class Solution:
    # Time: O(n)
    # Space: O(1)
    def are_almost_equal(self, s1: str, s2: str) -> bool:
        diffs = [i for i, (a, b) in enumerate(zip(s1, s2, strict=True)) if a != b]
        if not diffs:
            return True
        if len(diffs) != 2:
            return False
        i, j = diffs
        return s1[i] == s2[j] and s1[j] == s2[i]
