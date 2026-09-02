class Solution:
    # Time: O(26 * n)
    # Space: O(1)
    def count_palindromic_subsequence(self, s: str) -> int:
        total = 0
        for outer in set(s):
            left = s.index(outer)
            right = s.rindex(outer)
            if left == right:
                continue
            total += len(set(s[left + 1 : right]))
        return total
