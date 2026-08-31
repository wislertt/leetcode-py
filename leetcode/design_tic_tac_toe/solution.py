class TicTacToe:
    # Time: O(n) setup — per-player row, column, and diagonal counters
    # Space: O(n) — 2n rows + 2n cols + 2 diagonals per player index
    def __init__(self, n: int) -> None:
        self.n = n
        self.rows = [[0] * n for _ in range(3)]
        self.cols = [[0] * n for _ in range(3)]
        self.diag = [0] * 3
        self.anti_diag = [0] * 3

    # Time: O(1) — increment four counters, compare against n
    # Space: O(1)
    def move(self, row: int, col: int, player: int) -> int:
        self.rows[player][row] += 1
        self.cols[player][col] += 1
        if row == col:
            self.diag[player] += 1
        if row + col == self.n - 1:
            self.anti_diag[player] += 1
        if (
            self.rows[player][row] == self.n
            or self.cols[player][col] == self.n
            or self.diag[player] == self.n
            or self.anti_diag[player] == self.n
        ):
            return player
        return 0
