class Solution:
    # Time: O(n^2)
    # Space: O(n^2)
    def largest_island(self, grid: list[list[int]]) -> int:
        n = len(grid)
        sizes = [0, 0]  # island ids start at 2 so 0/1 stay sentinel-free
        label = [[0] * n for _ in range(n)]

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0 or label[r][c]:
                    continue
                island_id = len(sizes)
                stack = [(r, c)]
                size = 0
                while stack:
                    x, y = stack.pop()
                    if not (0 <= x < n and 0 <= y < n) or grid[x][y] != 1 or label[x][y]:
                        continue
                    label[x][y] = island_id
                    size += 1
                    stack.extend(((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)))
                sizes.append(size)

        best = max(sizes)
        for r in range(n):
            for c in range(n):
                if grid[r][c] != 0:
                    continue
                nbr_ids = set()
                for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                        nbr_ids.add(label[x][y])
                best = max(best, 1 + sum(sizes[i] for i in nbr_ids))
        return best
