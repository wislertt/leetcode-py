import math
from collections import defaultdict


class Solution:
    # Time: O(n^2) where n is the number of points
    # Space: O(n) for the hash map
    def max_points(self, points: list[list[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        max_count = 0

        for i in range(len(points)):
            slope_count: defaultdict[tuple[int, int], int] = defaultdict(int)
            duplicate = 0
            current_max = 0

            x1, y1 = points[i]

            for j in range(i + 1, len(points)):
                x2, y2 = points[j]

                # Handle duplicate points
                if x1 == x2 and y1 == y2:
                    duplicate += 1
                    continue

                # Calculate slope as a reduced fraction (dx, dy)
                dx = x2 - x1
                dy = y2 - y1

                # Reduce to lowest terms using GCD
                gcd_val = math.gcd(dx, dy)
                if gcd_val != 0:
                    dx //= gcd_val
                    dy //= gcd_val

                # Normalize the direction (ensure consistent representation)
                if dx < 0:
                    dx = -dx
                    dy = -dy
                elif dx == 0:
                    dy = abs(dy)

                slope = (dx, dy)
                slope_count[slope] += 1
                current_max = max(current_max, slope_count[slope])

            max_count = max(max_count, current_max + duplicate + 1)

        return max_count
