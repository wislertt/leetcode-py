class Solution:
    # Time: O(n)
    # Space: O(1)
    def score_of_string(self, s: str) -> int:
        return sum(abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1))
