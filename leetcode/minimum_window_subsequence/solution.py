class Solution:
    # Time: O(m * n)
    # Space: O(n)
    def min_window(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        start, best = 0, m + 1
        # dp[j] = smallest index i such that s1[:i] contains s2[:j] as a suffix subsequence
        prev = [0] * (n + 1)
        for i in range(1, m + 1):
            cur = [0] * (n + 1)
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    cur[j] = i if j == 1 else prev[j - 1]
                else:
                    cur[j] = prev[j]
            if cur[n] and i - cur[n] + 1 < best:
                best = i - cur[n] + 1
                start = cur[n] - 1
            prev = cur
        return "" if best > m else s1[start : start + best]
