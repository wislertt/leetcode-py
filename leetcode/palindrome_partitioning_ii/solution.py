class Solution:
    # Time: O(n^2)
    # Space: O(n^2)
    def min_cut(self, s: str) -> int:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        cut = [0] * n
        for i in range(n):
            best = n
            for j in range(i + 1):
                if s[j] == s[i] and (i - j < 2 or is_pal[j + 1][i - 1]):
                    is_pal[j][i] = True
                    best = 0 if j == 0 else min(best, cut[j - 1] + 1)
            cut[i] = best
        return cut[n - 1]
