import math
import random


class Solution:
    # Time: O(1) per rand_point call, O(1) init
    # Space: O(1)

    def __init__(self, radius: float, x_center: float, y_center: float) -> None:
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def rand_point(self) -> list[float]:
        # Sampling radius as sqrt(u) * R makes the point density uniform per
        # unit area: a uniform angle sweeps equal area only at equal radii, so
        # the radial CDF r^2/R^2 must be inverted with sqrt(u).
        length = math.sqrt(random.random()) * self.radius
        angle = random.uniform(0, 2 * math.pi)
        return [
            self.x_center + length * math.cos(angle),
            self.y_center + length * math.sin(angle),
        ]
