class Solution:
    # Time: O(c + o)
    # Space: O(o)
    def robot_sim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        blocked = {(x, y) for x, y in obstacles}
        x, y, dx, dy = 0, 0, 0, 1
        best = 0
        for command in commands:
            if command == -2:
                dx, dy = -dy, dx
            elif command == -1:
                dx, dy = dy, -dx
            else:
                for _ in range(command):
                    next_x, next_y = x + dx, y + dy
                    if (next_x, next_y) in blocked:
                        break
                    x, y = next_x, next_y
                best = max(best, x * x + y * y)
        return best
