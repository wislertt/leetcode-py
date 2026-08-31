from collections import deque


class Solution:
    # Time: O(n^2)
    # Space: O(n^2)
    def snakes_and_ladders(self, board: list[list[int]]) -> int:
        n = len(board)
        target = n * n

        def position(square: int) -> tuple[int, int]:
            row, col = divmod(square - 1, n)
            if row % 2 == 1:
                col = n - 1 - col
            return n - 1 - row, col

        moves = {1: 0}
        queue: deque[int] = deque([1])
        while queue:
            curr = queue.popleft()
            for nxt in range(curr + 1, min(curr + 6, target) + 1):
                row, col = position(nxt)
                dest = board[row][col] if board[row][col] != -1 else nxt
                if dest == target:
                    return moves[curr] + 1
                if dest not in moves:
                    moves[dest] = moves[curr] + 1
                    queue.append(dest)
        return -1
