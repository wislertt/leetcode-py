class Solution:
    # Time: O(m * n)
    # Space: O(n) using a single rolling row
    def is_interleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        if n > m:
            # Ensure s1 is the longer string so the rolling row stays minimal
            return self.is_interleave(s2, s1, s3)

        # dp[j] = True if s3[:i+j] is an interleaving of s1[:i] and s2[:j]
        dp = [False] * (n + 1)
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0:
                    dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
                elif j == 0:
                    dp[j] = dp[j] and s1[i - 1] == s3[i - 1]
                else:
                    dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (
                        dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                    )
        return dp[n]
