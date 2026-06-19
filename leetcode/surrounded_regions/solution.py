from collections import deque


class Solution:
    # Time: O(m * n)
    # Space: O(m * n) for the border-connected queue in the worst case
    def solve(self, board: list[list[str]]) -> None:
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        queue: deque[tuple[int, int]] = deque()

        def enqueue(i: int, j: int) -> None:
            if board[i][j] == "O":
                board[i][j] = "#"
                queue.append((i, j))

        # Seed from all border cells
        for i in range(m):
            enqueue(i, 0)
            enqueue(i, n - 1)
        for j in range(n):
            enqueue(0, j)
            enqueue(m - 1, j)

        # BFS: mark every 'O' reachable from a border (cannot be captured)
        while queue:
            i, j = queue.popleft()
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == "O":
                    board[ni][nj] = "#"
                    queue.append((ni, nj))

        # '#' = safe border-connected 'O'; everything else enclosed gets captured
        for i in range(m):
            for j in range(n):
                board[i][j] = "O" if board[i][j] == "#" else "X"
