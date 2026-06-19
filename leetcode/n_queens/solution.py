class Solution:
    # Time: O(n!)
    # Space: O(n) excluding output
    def solve_n_queens(self, n: int) -> list[list[str]]:
        result: list[list[str]] = []
        cols: set[int] = set()
        diag1: set[int] = set()  # r - c
        diag2: set[int] = set()  # r + c
        queens: list[int] = []  # column index per row

        def can_place(row: int, col: int) -> bool:
            return col not in cols and row - col not in diag1 and row + col not in diag2

        def backtrack(row: int) -> None:
            if row == n:
                board: list[str] = []
                for q_col in queens:
                    board.append("." * q_col + "Q" + "." * (n - q_col - 1))
                result.append(board)
                return
            for col in range(n):
                if not can_place(row, col):
                    continue
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                queens.append(col)
                backtrack(row + 1)
                queens.pop()
                diag2.discard(row + col)
                diag1.discard(row - col)
                cols.discard(col)

        backtrack(0)
        return result
