class Solution:
    # Time: O(1) — bounded 8x8 scan in four directions
    # Space: O(1)
    def num_rook_captures(self, board: list[list[str]]) -> int:
        rook_i = rook_j = -1
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    rook_i, rook_j = i, j
        count = 0
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            i, j = rook_i + di, rook_j + dj
            while 0 <= i < 8 and 0 <= j < 8 and board[i][j] == ".":
                i, j = i + di, j + dj
            if 0 <= i < 8 and 0 <= j < 8 and board[i][j] == "p":
                count += 1
        return count
