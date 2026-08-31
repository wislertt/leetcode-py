class Solution:
    # Time: O(n^3) steps x O(n^2) row pairs
    # Space: O(n^2)
    def cherry_pickup(self, grid: list[list[int]]) -> int:
        n = len(grid)
        # -1 marks unreachable states (cherry counts are always >= 0)
        unreachable = -1
        # dp[r1][r2]: max cherries with both walkers on diagonal r + c = t
        dp = [[unreachable] * n for _ in range(n)]
        dp[0][0] = grid[0][0]

        for t in range(1, 2 * n - 1):
            ndp = [[unreachable] * n for _ in range(n)]
            for r1 in range(max(0, t - n + 1), min(n, t + 1)):
                for r2 in range(r1, min(n, t + 1)):
                    c1, c2 = t - r1, t - r2
                    if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                        continue
                    best = unreachable
                    for pr1 in (r1 - 1, r1):
                        for pr2 in (r2 - 1, r2):
                            if 0 <= pr1 < n and 0 <= pr2 < n and dp[pr1][pr2] > best:
                                best = dp[pr1][pr2]
                    if best < 0:
                        continue
                    cherries = grid[r1][c1]
                    if r1 != r2:
                        cherries += grid[r2][c2]
                    ndp[r1][r2] = best + cherries
            dp = ndp

        return max(dp[n - 1][n - 1], 0)
