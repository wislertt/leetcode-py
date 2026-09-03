import pytest

from leetcode_py import logged_test

from .helpers import assert_count_corner_rectangles, run_count_corner_rectangles
from .solution import Solution


class TestNumberOfCornerRectangles:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[1, 0, 0, 1, 0], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [1, 0, 1, 0, 1]], 1),
            ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 9),
            ([[1, 1, 1, 1]], 0),
            ([[1]], 0),
            ([[1, 1], [1, 1]], 1),
            ([[1, 0], [0, 1]], 0),
            ([[1, 1], [1, 0]], 0),
            ([[1, 0, 1], [1, 0, 1]], 1),
            ([[1, 1], [1, 1], [1, 1]], 3),
            ([[1, 1, 0], [0, 1, 1], [1, 1, 0]], 1),
            ([[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]], 1),
            ([[1, 1, 1, 1], [1, 1, 1, 1]], 6),
            ([[1, 1, 1], [0, 0, 0]], 0),
            ([[0, 1, 0], [1, 0, 1], [0, 1, 0]], 0),
            ([[0, 0, 1, 1], [0, 1, 1, 1], [0, 0, 0, 0]], 1),
            ([[0], [1]], 0),
        ],
    )
    def test_count_corner_rectangles(self, grid: list[list[int]], expected: int):
        result = run_count_corner_rectangles(Solution, grid)
        assert_count_corner_rectangles(result, expected)
