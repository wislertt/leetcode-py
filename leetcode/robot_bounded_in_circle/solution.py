class Solution:
    # Time: O(n)
    # Space: O(1)
    def is_robot_bounded(self, instructions: str) -> bool:
        x = y = 0
        dx, dy = 0, 1
        for instruction in instructions:
            if instruction == "G":
                x, y = x + dx, y + dy
            elif instruction == "L":
                dx, dy = -dy, dx
            else:
                dx, dy = dy, -dx
        return (x == 0 and y == 0) or (dx, dy) != (0, 1)
