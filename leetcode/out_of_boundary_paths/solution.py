class Solution:
    # Time: O(max_move * m * n)
    # Space: O(m * n)
    def find_paths(
        self,
        m: int,
        n: int,
        max_move: int,
        start_row: int,
        start_column: int,
    ) -> int:
        mod = 1_000_000_007
        # dp[r][c]: number of paths currently at cell (r, c) inside the grid.
        dp = [[0] * n for _ in range(m)]
        dp[start_row][start_column] = 1
        paths = 0
        for _ in range(max_move):
            nxt = [[0] * n for _ in range(m)]
            for row in range(m):
                for col in range(n):
                    count = dp[row][col]
                    if not count:
                        continue
                    for n_row, n_col in (
                        (row + 1, col),
                        (row - 1, col),
                        (row, col + 1),
                        (row, col - 1),
                    ):
                        if 0 <= n_row < m and 0 <= n_col < n:
                            nxt[n_row][n_col] = (nxt[n_row][n_col] + count) % mod
                        else:
                            paths = (paths + count) % mod
            dp = nxt
        return paths
