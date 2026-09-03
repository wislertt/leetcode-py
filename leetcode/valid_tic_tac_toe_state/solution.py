class Solution:
    # Time: O(1) - the board is always 3 x 3
    # Space: O(1)

    def valid_tic_tac_toe(self, board: list[str]) -> bool:
        x_count = sum(row.count("X") for row in board)
        o_count = sum(row.count("O") for row in board)

        if o_count not in (x_count - 1, x_count):
            return False

        x_wins = self._wins(board, "X")
        o_wins = self._wins(board, "O")

        if x_wins and o_wins:
            return False
        if x_wins:
            return x_count == o_count + 1
        if o_wins:
            return x_count == o_count
        return True

    def _wins(self, board: list[str], player: str) -> bool:
        lines = [board[i] for i in range(3)]
        lines += ["".join(row[j] for row in board) for j in range(3)]
        lines.append("".join(board[i][i] for i in range(3)))
        lines.append("".join(board[i][2 - i] for i in range(3)))
        return any(line == player * 3 for line in lines)
