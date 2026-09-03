from collections import deque


class Solution:
    # Time: O((mn)^2) each BFS scan is O(mn) and runs once per tree
    # Space: O(mn) for the BFS queue and visited set
    def cut_off_tree(self, forest: list[list[int]]) -> int:
        rows, cols = len(forest), len(forest[0])
        trees = sorted(
            (forest[r][c], r, c) for r in range(rows) for c in range(cols) if forest[r][c] > 1
        )

        def bfs(sr: int, sc: int, tr: int, tc: int) -> int:
            if (sr, sc) == (tr, tc):
                return 0
            seen: set[tuple[int, int]] = {(sr, sc)}
            queue: deque[tuple[int, int, int]] = deque([(sr, sc, 0)])
            while queue:
                r, c, steps = queue.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and forest[nr][nc] > 0
                        and (nr, nc) not in seen
                    ):
                        if (nr, nc) == (tr, tc):
                            return steps + 1
                        seen.add((nr, nc))
                        queue.append((nr, nc, steps + 1))
            return -1

        total = 0
        cur_r, cur_c = 0, 0
        for _, tree_r, tree_c in trees:
            dist = bfs(cur_r, cur_c, tree_r, tree_c)
            if dist < 0:
                return -1
            total += dist
            cur_r, cur_c = tree_r, tree_c
        return total
