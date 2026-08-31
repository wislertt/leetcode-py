from collections import Counter


class Solution:
    # Time: O(n * m) where m is the max bricks per row
    # Space: O(n * m)
    def least_bricks(self, wall: list[list[int]]) -> int:
        edge_counts: Counter[int] = Counter()
        for row in wall:
            position = 0
            for width in row[:-1]:
                position += width
                edge_counts[position] += 1
        crossings = max(edge_counts.values(), default=0)
        return len(wall) - crossings
