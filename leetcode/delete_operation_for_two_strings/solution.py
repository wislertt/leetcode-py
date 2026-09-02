class Solution:
    # Time: O(n * m)
    # Space: O(m)
    def min_distance(self, word1: str, word2: str) -> int:
        m = len(word2)
        prev = list(range(m + 1))
        for i in range(1, len(word1) + 1):
            curr = [i] + [0] * m
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = 1 + min(prev[j], curr[j - 1])
            prev = curr
        return prev[m]
