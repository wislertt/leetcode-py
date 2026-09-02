class Solution:
    # Time: O(m * n)
    # Space: O(1)
    def game_of_life(self, board: list[list[int]]) -> None:
        # Encode next state in the second bit: 0b10 = alive next gen,
        # 0b01 = alive this gen. Low bit stays readable while filling.
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                live = 0
                for x in range(max(i - 1, 0), min(i + 2, m)):
                    for y in range(max(j - 1, 0), min(j + 2, n)):
                        if (x, y) != (i, j) and board[x][y] & 1:
                            live += 1
                if board[i][j] & 1:
                    if live in (2, 3):
                        board[i][j] |= 2
                elif live == 3:
                    board[i][j] |= 2

        for row in board:
            for j in range(n):
                row[j] >>= 1
