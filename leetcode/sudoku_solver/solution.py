class Solution:
    # Time: O(9^(n)) where n = number of empty cells, pruned heavily by validity checks
    # Space: O(n) recursion stack + O(1) bookkeeping sets
    def solve_sudoku(self, board: list[list[str]]) -> None:
        rows = [set[str]() for _ in range(9)]
        cols = [set[str]() for _ in range(9)]
        boxes = [set[str]() for _ in range(9)]
        empties: list[tuple[int, int]] = []

        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == ".":
                    empties.append((r, c))
                else:
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[(r // 3) * 3 + c // 3].add(ch)

        def backtrack(idx: int) -> bool:
            if idx == len(empties):
                return True
            r, c = empties[idx]
            b = (r // 3) * 3 + c // 3
            for d in map(str, range(1, 10)):
                if d in rows[r] or d in cols[c] or d in boxes[b]:
                    continue
                board[r][c] = d
                rows[r].add(d)
                cols[c].add(d)
                boxes[b].add(d)
                if backtrack(idx + 1):
                    return True
                board[r][c] = "."
                rows[r].discard(d)
                cols[c].discard(d)
                boxes[b].discard(d)
            return False

        backtrack(0)
