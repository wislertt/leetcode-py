class Solution:
    # Time: O(S + n * m) where S = total chars in words, n = len(words[0]), m = len(target)
    # Space: O(26 * n + m)
    def num_ways(self, words: list[str], target: str) -> int:
        mod = 1_000_000_007
        n = len(words[0])
        m = len(target)

        counts: list[list[int]] = [[0] * 26 for _ in range(n)]
        for word in words:
            for k, char in enumerate(word):
                counts[k][ord(char) - 97] += 1

        dp = [0] * (m + 1)
        dp[0] = 1
        for k in range(n):
            column = counts[k]
            for i in range(m, 0, -1):
                freq = column[ord(target[i - 1]) - 97]
                if freq:
                    dp[i] = (dp[i] + dp[i - 1] * freq) % mod
        return dp[m]
