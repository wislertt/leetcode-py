class Solution:
    # Time: O(k * n^2)
    # Space: O(n^2)
    def knight_probability(self, n: int, k: int, row: int, column: int) -> float:
        moves = ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2))
        prob = [[0.0] * n for _ in range(n)]
        prob[row][column] = 1.0
        for _ in range(k):
            nxt = [[0.0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    if prob[r][c] == 0.0:
                        continue
                    share = prob[r][c] / 8.0
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            nxt[nr][nc] += share
            prob = nxt
        return sum(map(sum, prob))
