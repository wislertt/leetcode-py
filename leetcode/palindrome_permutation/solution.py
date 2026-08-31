from collections import Counter


class Solution:
    # Time: O(n)
    # Space: O(1) for the 26-letter alphabet
    def can_permute_palindrome(self, s: str) -> bool:
        counts = Counter(s)
        return sum(count % 2 for count in counts.values()) < 2
