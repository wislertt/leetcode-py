class Solution:
    # Time: O(n)
    # Space: O(n)
    def is_path_crossing(self, path: str) -> bool:
        x = y = 0
        seen = {(0, 0)}
        moves = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
        for step in path:
            dx, dy = moves[step]
            x, y = x + dx, y + dy
            if (x, y) in seen:
                return True
            seen.add((x, y))
        return False
