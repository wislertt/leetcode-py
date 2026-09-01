import pytest

from leetcode_py import logged_test

from .helpers import assert_minimum_obstacles, run_minimum_obstacles
from .solution import Solution


class TestMinimumObstacleRemovalToReachCorner:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[0, 1, 1], [1, 1, 0], [1, 1, 0]], 2),
            ([[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]], 0),
            ([[0, 0]], 0),
            ([[0], [0]], 0),
            ([[0, 1], [1, 1], [0, 0]], 1),
            ([[0, 0], [1, 1], [1, 0]], 1),
            ([[0, 0], [1, 0]], 0),
            ([[0, 1], [1, 0]], 1),
            ([[0, 1, 1], [1, 1, 1], [1, 1, 0]], 3),
            ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0),
            ([[0, 1], [1, 1], [1, 0]], 2),
            ([[0, 1, 1], [0, 0, 1], [1, 0, 0]], 0),
            ([[0, 1, 0], [1, 1, 0], [0, 0, 0]], 1),
            ([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0]], 4),
            ([[0, 0, 1], [1, 0, 1], [1, 0, 0]], 0),
            ([[0, 1, 0, 1], [1, 1, 0, 1], [0, 0, 0, 0]], 1),
            ([[0, 0, 0, 1], [1, 1, 1, 1], [0, 1, 0, 1], [1, 0, 0, 0]], 1),
            ([[0, 0], [0, 0], [0, 0], [0, 0]], 0),
            ([[0, 1, 1, 1], [0, 0, 0, 0]], 0),
            ([[0, 1, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]], 0),
        ],
    )
    def test_minimum_obstacles(self, grid: list[list[int]], expected: int):
        result = run_minimum_obstacles(Solution, grid)
        assert_minimum_obstacles(result, expected)
