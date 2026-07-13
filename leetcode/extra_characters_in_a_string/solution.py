class Solution:
    # Time: O(n^2 * m)
    # Space: O(n)
    def min_extra_char(self, s: str, dictionary: list[str]) -> int:
        n = len(s)
        word_set = set(dictionary)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(i):
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])

        return dp[n]
