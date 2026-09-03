import pytest

from leetcode_py import logged_test

from .helpers import assert_surface_area, run_surface_area
from .solution import Solution


class TestSurfaceAreaOf3dShapes:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[1, 2], [3, 4]], 34),
            ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 32),
            ([[2, 2, 2], [2, 1, 2], [2, 2, 2]], 46),
            ([[1]], 6),
            ([[2]], 10),
            ([[0]], 0),
            ([[50]], 202),
            ([[0, 0], [0, 0]], 0),
            ([[1, 0], [0, 1]], 12),
            ([[1, 1], [1, 1]], 16),
            ([[2, 1], [1, 2]], 24),
            ([[1, 1], [0, 1]], 14),
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 102),
            ([[5, 3, 4], [1, 2, 1], [0, 2, 3]], 66),
            ([[3]], 14),
            ([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], 48),
            ([[2, 1], [3, 3]], 30),
            ([[1, 1], [1, 2]], 20),
            ([[4, 2], [4, 0]], 34),
            ([[4, 0, 4, 0], [0, 4, 1, 4], [4, 0, 4, 0], [1, 1, 0, 0]], 114),
            ([[4]], 18),
            ([[2, 1, 0, 1], [4, 0, 3, 3], [0, 1, 4, 0], [1, 1, 1, 0]], 80),
            ([[3, 1, 2], [3, 4, 0], [1, 0, 1]], 54),
        ],
    )
    def test_surface_area(self, grid: list[list[int]], expected: int):
        result = run_surface_area(Solution, grid)
        assert_surface_area(result, expected)
