class Solution:
    # Time: O(n)
    # Space: O(n)
    def magical_string(self, n: int) -> int:
        if n <= 0:
            return 0
        s = [1, 2, 2]
        i = 2
        while len(s) < n:
            nxt = s[-1] ^ 3
            s.extend([nxt] * s[i])
            i += 1
        return s[:n].count(1)
