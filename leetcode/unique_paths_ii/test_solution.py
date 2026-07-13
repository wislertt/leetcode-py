import pytest

from leetcode_py import logged_test

from .helpers import assert_unique_paths_with_obstacles, run_unique_paths_with_obstacles
from .solution import Solution


class TestTestUniquePathsII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2),
            ([[0, 1], [0, 0]], 1),
            ([[0, 0], [0, 0]], 2),
            ([[0]], 1),
            ([[1]], 0),
            ([[1, 0]], 0),
            ([[0, 0]], 1),
            ([[0], [0]], 1),
            ([[1], [0]], 0),
            ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 6),
            ([[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0]], 4),
            ([[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 0, 0]], 5),
        ],
    )
    def test_unique_paths_with_obstacles(self, grid: list[list[int]], expected: int):
        result = run_unique_paths_with_obstacles(Solution, grid)
        assert_unique_paths_with_obstacles(result, expected)
