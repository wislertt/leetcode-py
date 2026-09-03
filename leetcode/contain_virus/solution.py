class Solution:
    # Time: O((m * n)^2) across all days
    # Space: O(m * n)
    def contain_virus(self, is_infected: list[list[int]]) -> int:
        grid = is_infected
        rows, cols = len(grid), len(grid[0])
        walls_used = 0

        while True:
            seen = [[False] * cols for _ in range(rows)]
            regions: list[tuple[list[tuple[int, int]], set[tuple[int, int]], int]] = []
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1 and not seen[r][c]:
                        seen[r][c] = True
                        stack = [(r, c)]
                        cells: list[tuple[int, int]] = []
                        fronts: set[tuple[int, int]] = set()
                        walls = 0
                        while stack:
                            x, y = stack.pop()
                            cells.append((x, y))
                            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < rows and 0 <= ny < cols:
                                    if grid[nx][ny] == 0:
                                        walls += 1
                                        fronts.add((nx, ny))
                                    elif grid[nx][ny] == 1 and not seen[nx][ny]:
                                        seen[nx][ny] = True
                                        stack.append((nx, ny))
                        regions.append((cells, fronts, walls))

            if not regions:
                break
            max_threat = max(len(fronts) for _, fronts, _ in regions)
            if max_threat == 0:
                break
            target = next(region for region in regions if len(region[1]) == max_threat)
            walls_used += target[2]
            for x, y in target[0]:
                grid[x][y] = -1
            for cells, fronts, _ in regions:
                if cells is not target[0]:
                    for x, y in fronts:
                        grid[x][y] = 1

        return walls_used
