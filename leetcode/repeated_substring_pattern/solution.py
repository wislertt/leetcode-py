class Solution:
    # Time: O(n)
    # Space: O(n)
    def repeated_substring_pattern(self, s: str) -> bool:
        n = len(s)
        lps = [0] * n
        length = 0
        for i in range(1, n):
            while length > 0 and s[i] != s[length]:
                length = lps[length - 1]
            if s[i] == s[length]:
                length += 1
            lps[i] = length
        longest_proper_suffix = lps[n - 1] if n > 0 else 0
        return longest_proper_suffix > 0 and n % (n - longest_proper_suffix) == 0
