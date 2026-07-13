import pytest

from leetcode_py import logged_test

from .helpers import assert_island_perimeter, run_island_perimeter
from .solution import Solution


class TestIslandPerimeter:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]], 16),
            ([[1]], 4),
            ([[1, 0]], 4),
            ([[0, 1]], 4),
            ([[1, 1]], 6),
            ([[1], [1]], 6),
            ([[1, 1], [1, 1]], 8),
            ([[1, 0], [0, 0]], 4),
            ([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 12),
            ([[1, 1, 1]], 8),
            ([[1], [1], [1]], 8),
            ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 12),
            ([[1, 1, 0], [0, 1, 1]], 10),
            ([[1, 1], [1, 0]], 8),
            ([[1, 1, 1], [0, 1, 0], [0, 1, 0]], 12),
        ],
    )
    def test_island_perimeter(self, grid: list[list[int]], expected: int):
        result = run_island_perimeter(Solution, grid)
        assert_island_perimeter(result, expected)
