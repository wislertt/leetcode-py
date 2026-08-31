from typing import ClassVar


class Solution:
    # Dot passed through when moving directly between two keys, if any.
    # Keyed on unordered pairs; 0 means the segment crosses no other dot.
    CROSS: ClassVar[dict[tuple[int, int], int]] = {
        (1, 3): 2,
        (1, 7): 4,
        (1, 9): 5,
        (3, 7): 5,
        (3, 9): 6,
        (7, 9): 8,
        (2, 8): 5,
        (4, 6): 5,
    }

    # Time: O(n!) branch factor bounded by the 9-dot grid — exhaustive DFS
    # Space: O(9) — bitmask visited set and recursion depth
    def number_of_patterns(self, m: int, n: int) -> int:
        def dfs(current: int, used: int, length: int) -> int:
            if length > n:
                return 0
            count = 1 if length >= m else 0
            for nxt in range(1, 10):
                if used & (1 << nxt):
                    continue
                crossed = Solution.CROSS.get((current, nxt), Solution.CROSS.get((nxt, current), 0))
                if crossed and not used & (1 << crossed):
                    continue
                count += dfs(nxt, used | (1 << nxt), length + 1)
            return count

        return sum(dfs(start, 1 << start, 1) for start in range(1, 10))
