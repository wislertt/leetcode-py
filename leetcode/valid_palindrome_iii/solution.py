class Solution:
    # Time: O(n^2)
    # Space: O(n)
    def is_valid_palindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            prev = 0
            dp[i] = 1
            for j in range(i + 1, n):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = prev + 2
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = temp
        return n - dp[n - 1] <= k
