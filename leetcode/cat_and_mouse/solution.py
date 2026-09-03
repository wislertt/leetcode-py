from collections import deque


class Solution:
    # Time: O(n^3)
    # Space: O(n^2)
    def cat_mouse_game(self, graph: list[list[int]]) -> int:
        n = len(graph)
        draw, mouse_win, cat_win = 0, 1, 2
        # color[m][c][t]: result of the state with the mouse on m, the cat on c and
        # t picking the mover (0 mouse, 1 cat). Unresolved states stay draw.
        color = [[[draw] * 2 for _ in range(n)] for _ in range(n)]
        # degree[m][c][t]: how many of the mover's options are still undecided.
        degree = [[[0] * 2 for _ in range(n)] for _ in range(n)]
        for m in range(n):
            for c in range(n):
                degree[m][c][0] = len(graph[m])
                degree[m][c][1] = len(graph[c]) - (0 in graph[c])

        queue: deque[tuple[int, int, int]] = deque()
        for node in range(n):
            for turn in (0, 1):
                if node and color[node][node][turn] == draw:
                    color[node][node][turn] = cat_win
                    queue.append((node, node, turn))
                if color[0][node][turn] == draw:
                    color[0][node][turn] = mouse_win
                    queue.append((0, node, turn))

        while queue:
            m, c, turn = queue.popleft()
            outcome = color[m][c][turn]
            if turn == 0:
                # A resolved mouse-to-move state was reached by the cat moving.
                parents = [(m, prev_c, 1) for prev_c in graph[c] if prev_c != 0]
            else:
                # A resolved cat-to-move state was reached by the mouse moving.
                parents = [(prev_m, c, 0) for prev_m in graph[m]]
            for prev_m, prev_c, prev_turn in parents:
                if color[prev_m][prev_c][prev_turn] != draw:
                    continue
                if outcome == prev_turn + mouse_win:
                    # The mover can step into a state it already wins.
                    color[prev_m][prev_c][prev_turn] = outcome
                    queue.append((prev_m, prev_c, prev_turn))
                else:
                    degree[prev_m][prev_c][prev_turn] -= 1
                    if degree[prev_m][prev_c][prev_turn] == 0:
                        # Every option loses, so the state is lost for the mover.
                        color[prev_m][prev_c][prev_turn] = outcome
                        queue.append((prev_m, prev_c, prev_turn))
        return color[1][2][0]
