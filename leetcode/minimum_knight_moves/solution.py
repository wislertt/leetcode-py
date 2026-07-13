from collections import deque


class Solution:
    # Time: O(x * y)
    # Space: O(x * y)
    def min_knight_moves(self, x: int, y: int) -> int:
        # Symmetry: target mirrored into first quadrant. BFS bounded to a small
        # region around origin + target; allow slight negatives to reach (1,1).
        x, y = abs(x), abs(y)
        seen: set[tuple[int, int]] = {(0, 0)}
        queue: deque[tuple[int, int, int]] = deque([(0, 0, 0)])
        directions = [
            (1, 2),
            (2, 1),
            (-1, 2),
            (-2, 1),
            (1, -2),
            (2, -1),
            (-1, -2),
            (-2, -1),
        ]
        while queue:
            cur_x, cur_y, dist = queue.popleft()
            if cur_x == x and cur_y == y:
                return dist
            for dx, dy in directions:
                nx, ny = cur_x + dx, cur_y + dy
                if (nx, ny) not in seen and -2 <= nx <= x + 4 and -2 <= ny <= y + 4:
                    seen.add((nx, ny))
                    queue.append((nx, ny, dist + 1))
        return -1
