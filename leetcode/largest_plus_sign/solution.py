class Solution:
    # Time: O(n^2)
    # Space: O(n^2)
    def order_of_largest_plus_sign(self, n: int, mines: list[list[int]]) -> int:
        blocked = {(x, y) for x, y in mines}

        # dp[r][c] = length of the run of 1s ending at (r, c) in the current direction
        dp = [[n] * n for _ in range(n)]

        for r in range(n):
            # left to right
            run = 0
            for c in range(n):
                run = 0 if (r, c) in blocked else run + 1
                dp[r][c] = min(dp[r][c], run)
            # right to left
            run = 0
            for c in range(n - 1, -1, -1):
                run = 0 if (r, c) in blocked else run + 1
                dp[r][c] = min(dp[r][c], run)

        for c in range(n):
            # top to bottom
            run = 0
            for r in range(n):
                run = 0 if (r, c) in blocked else run + 1
                dp[r][c] = min(dp[r][c], run)
            # bottom to top
            run = 0
            for r in range(n - 1, -1, -1):
                run = 0 if (r, c) in blocked else run + 1
                dp[r][c] = min(dp[r][c], run)

        return max(max(row) for row in dp)
