from itertools import product


class Solution:
    # Time: O(k^(n-1)) states memoized by row; n <= 6 so bounded by 6^5 rows
    # Space: O(k^(n-1)) for the memo set of dead rows
    def pyramid_transition(self, bottom: str, allowed: list[str]) -> bool:
        tops: dict[str, list[str]] = {}
        for pattern in allowed:
            tops.setdefault(pattern[:2], []).append(pattern[2])

        dead: set[str] = set()

        def dfs(row: str) -> bool:
            if len(row) == 1:
                return True
            if row in dead:
                return False
            dead.add(row)
            options = [tops.get(row[i : i + 2], ()) for i in range(len(row) - 1)]
            return any(dfs("".join(level)) for level in product(*options))

        return dfs(bottom)
