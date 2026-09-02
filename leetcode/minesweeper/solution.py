from collections import deque


class Solution:
    DIRECTIONS: tuple[tuple[int, int], ...] = (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    )

    # Time: O(m * n)
    # Space: O(m * n)
    def update_board(self, board: list[list[str]], click: list[int]) -> list[list[str]]:
        rows, cols = len(board), len(board[0])
        row, col = click
        if board[row][col] == "M":
            board[row][col] = "X"
            return board

        queue: deque[tuple[int, int]] = deque([(row, col)])
        while queue:
            r, c = queue.popleft()
            mines = self._adjacent_mines(board, r, c)
            if mines:
                board[r][c] = str(mines)
                continue
            board[r][c] = "B"
            for dr, dc in self.DIRECTIONS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "E":
                    board[nr][nc] = "B"
                    queue.append((nr, nc))
        return board

    def _adjacent_mines(self, board: list[list[str]], r: int, c: int) -> int:
        rows, cols = len(board), len(board[0])
        return sum(
            1
            for dr, dc in self.DIRECTIONS
            if 0 <= r + dr < rows and 0 <= c + dc < cols and board[r + dr][c + dc] == "M"
        )
