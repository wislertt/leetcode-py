class Solution:
    # Time: O(m * n)
    # Space: O(m * n) for the result (O(n) auxiliary)
    def rotate_the_box(self, box_grid: list[list[str]]) -> list[list[str]]:
        m, n = len(box_grid), len(box_grid[0])

        def settle(row: list[str]) -> list[str]:
            out = ["."] * n
            write = n - 1
            for i in range(n - 1, -1, -1):
                cell = row[i]
                if cell == "*":
                    out[i] = "*"
                    write = i - 1
                elif cell == "#":
                    out[write] = "#"
                    write -= 1
            return out

        settled = [settle(row) for row in box_grid]
        return [[settled[m - 1 - j][i] for j in range(m)] for i in range(n)]
