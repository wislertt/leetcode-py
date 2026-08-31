from functools import cache


class Solution:
    # Time: O(n^4) over substring DP
    # Space: O(n^3) memoized substrings
    def encode(self, s: str) -> str:
        @cache
        def helper(sub: str) -> str:
            n = len(sub)
            if n <= 4:
                return sub
            best = sub
            for k in range(1, n // 2 + 1):
                if n % k == 0 and sub[:k] * (n // k) == sub:
                    cand = f"{n // k}[{helper(sub[:k])}]"
                    if len(cand) < len(best):
                        best = cand
            for split in range(1, n):
                cand = helper(sub[:split]) + helper(sub[split:])
                if len(cand) < len(best):
                    best = cand
            return best

        return helper(s)
