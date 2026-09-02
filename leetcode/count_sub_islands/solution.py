class Solution:
    # Time: O(m * n)
    # Space: O(m * n)
    def count_sub_islands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] != 1:
                    continue
                is_sub = True
                stack = [(r, c)]
                grid2[r][c] = 0
                while stack:
                    cr, cc = stack.pop()
                    if grid1[cr][cc] != 1:
                        is_sub = False
                    for nr, nc in ((cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)):
                        if 0 <= nr < rows and 0 <= nc < cols and grid2[nr][nc] == 1:
                            grid2[nr][nc] = 0
                            stack.append((nr, nc))
                if is_sub:
                    count += 1
        return count
