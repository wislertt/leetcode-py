class Solution:
    # Time: O(m * n)
    # Space: O(n) using a single rolling row
    def min_distance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # dp[j] = edit distance between word1 prefix (current row) and word2[:j]
        prev = list(range(n + 1))
        for i in range(1, m + 1):
            curr = [i] + [0] * n
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
            prev = curr
        return prev[n]
