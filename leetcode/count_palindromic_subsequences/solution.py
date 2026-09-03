from bisect import bisect_left, bisect_right


class Solution:
    # Time: O(n^2 log n)
    # Space: O(n^2)
    def count_palindromic_subsequences(self, s: str) -> int:
        mod = 1_000_000_007
        n = len(s)
        pos: dict[str, list[int]] = {c: [] for c in "abcd"}
        for i, c in enumerate(s):
            pos[c].append(i)
        # dp[i][j]: number of distinct palindromic subsequences in s[i..j]
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                inner = dp[i + 1][j - 1] if i + 1 <= j - 1 else 0
                if s[i] != s[j]:
                    dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - inner) % mod
                    continue
                # s[i] == s[j] == c: every palindrome either has no c at the
                # ends (counted twice) or is wrapped in a new c layer.
                lst = pos[s[i]]
                k = lst[bisect_right(lst, i)]  # first c strictly inside (i, j)
                if k >= j:
                    dp[i][j] = (2 * inner + 2) % mod
                    continue
                h = lst[bisect_left(lst, j) - 1]  # last c strictly inside (i, j)
                if k == h:
                    dp[i][j] = (2 * inner + 1) % mod
                else:
                    mid = dp[k + 1][h - 1] if k + 1 <= h - 1 else 0
                    dp[i][j] = (2 * inner - mid) % mod
        return dp[0][n - 1]
