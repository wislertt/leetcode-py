class Solution:
    # Time: O(n)
    # Space: O(1)
    def min_changes(self, s: str) -> int:
        # Every substring has even length, so each pair (s[2i], s[2i+1]) must
        # be uniform; aligning each pair to its majority character is optimal.
        changes = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                changes += 1
        return changes
