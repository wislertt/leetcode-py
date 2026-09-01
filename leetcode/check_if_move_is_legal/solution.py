class Solution:
    # Time: O(8 * 8) = O(1)
    # Space: O(1)
    def check_move(self, board: list[list[str]], r_move: int, c_move: int, color: str) -> bool:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))
        for dr, dc in directions:
            r, c = r_move + dr, c_move + dc
            seen = 0
            while 0 <= r < 8 and 0 <= c < 8 and board[r][c] != ".":
                if board[r][c] == color:
                    if seen >= 1:
                        return True
                    break
                seen += 1
                r += dr
                c += dc
        return False
