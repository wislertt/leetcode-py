import pytest

from leetcode_py import logged_test

from .helpers import assert_projection_area, run_projection_area
from .solution import Solution


class TestProjectionAreaOf3DShapes:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[1, 2], [3, 4]], 17),
            ([[2]], 5),
            ([[1, 0], [0, 2]], 8),
            ([[0]], 0),
            ([[1]], 3),
            ([[50]], 101),
            ([[0, 0], [0, 0]], 0),
            ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 15),
            ([[2, 2, 2], [2, 1, 2], [2, 2, 2]], 21),
            ([[1, 4, 7], [2, 5, 8], [3, 6, 9]], 51),
            ([[0, 5, 3], [3, 0, 1], [0, 3, 2]], 28),
            ([[5]], 11),
            ([[5, 5], [1, 5]], 24),
            ([[50, 0], [5, 5]], 113),
            ([[5, 0], [50, 50]], 158),
            ([[1, 5, 2, 2], [2, 7, 1, 50], [3, 50, 50, 5], [5, 7, 1, 0]], 282),
        ],
    )
    def test_projection_area(self, grid: list[list[int]], expected: int):
        result = run_projection_area(Solution, grid)
        assert_projection_area(result, expected)
