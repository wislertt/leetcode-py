class Solution:
    # Time: O(n!)
    # Space: O(n)
    def total_n_queens(self, n: int) -> int:
        cols: set[int] = set()
        diag1: set[int] = set()
        diag2: set[int] = set()

        def backtrack(row: int) -> int:
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                count += backtrack(row + 1)
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
            return count

        return backtrack(0)
