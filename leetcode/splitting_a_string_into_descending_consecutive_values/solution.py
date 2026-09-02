from functools import cache


class Solution:
    # Time: O(n^2) states explored via DFS over cut positions
    # Space: O(n) for recursion depth and memoization
    def split_string(self, s: str) -> bool:
        n = len(s)

        @cache
        def dfs(i: int, prev: int) -> bool:
            if i == n:
                return True
            for j in range(i + 1, n + 1):
                val = int(s[i:j])
                if prev - val == 1 and dfs(j, val):
                    return True
            return False

        # The first piece must leave at least one character for a second piece.
        return any(dfs(j, int(s[:j])) for j in range(1, n))
