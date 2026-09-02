class Solution:
    # Time: O(m * n)
    # Space: O(1)
    def count_battleships(self, board: list[list[str]]) -> int:
        count = 0
        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell != "X":
                    continue
                if r > 0 and board[r - 1][c] == "X":
                    continue
                if c > 0 and row[c - 1] == "X":
                    continue
                count += 1
        return count
