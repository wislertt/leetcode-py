from functools import cache


class Solution:
    # Time: O(n^2 * k)
    # Space: O(n^2 * k)
    def get_length_of_optimal_compression(self, s: str, k: int) -> int:
        n = len(s)

        @cache
        def dp(i: int, remaining: int) -> int:
            if remaining < 0:
                return n + 1
            if i >= n or n - i <= remaining:
                return 0
            best = dp(i + 1, remaining - 1)
            count = 0
            for j in range(i, n):
                if s[j] == s[i]:
                    count += 1
                    cost = 1 if count == 1 else 1 + len(str(count))
                    deleted = j - i + 1 - count
                    best = min(best, cost + dp(j + 1, remaining - deleted))
            return best

        return dp(0, k)
