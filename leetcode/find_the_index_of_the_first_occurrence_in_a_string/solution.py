class Solution:
    # Time: O(n + m)
    # Space: O(m)
    def str_str(self, haystack: str, needle: str) -> int:
        m = len(needle)
        if m == 0:
            return 0

        # Build KMP failure table: fail[i] = length of longest proper prefix
        # of needle[:i+1] that is also a suffix
        fail = [0] * m
        k = 0
        for i in range(1, m):
            while k > 0 and needle[i] != needle[k]:
                k = fail[k - 1]
            if needle[i] == needle[k]:
                k += 1
            fail[i] = k

        # Scan haystack using failure table to skip re-matched characters
        k = 0
        for i, ch in enumerate(haystack):
            while k > 0 and ch != needle[k]:
                k = fail[k - 1]
            if ch == needle[k]:
                k += 1
            if k == m:
                return i - m + 1
        return -1
