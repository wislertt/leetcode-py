import pytest

from leetcode_py import logged_test

from .helpers import assert_largest_triangle_area, run_largest_triangle_area
from .solution import Solution


class TestLargestTriangleArea:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "points, expected",
        [
            ([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]], 2.0),
            ([[1, 0], [0, 0], [0, 1]], 0.5),
            ([[0, 0], [1, 0], [0, 1]], 0.5),
            ([[0, 0], [4, 0], [0, 3]], 6.0),
            ([[1, 1], [2, 2], [3, 3]], 0.0),
            ([[0, 0], [5, 0], [0, 5], [5, 5]], 12.5),
            ([[2, 3], [7, 1], [4, 8]], 14.5),
            ([[-50, -50], [50, 50], [-50, 50]], 5000.0),
            ([[0, 0], [10, 0], [0, 10], [10, 10], [5, 5]], 50.0),
            ([[1, 0], [2, 0], [3, 0], [0, 4]], 4.0),
            ([[0, 0], [1, 1], [2, 0], [1, -2]], 2.0),
            ([[4, 1], [3, 1], [-2, -2]], 1.5),
            ([[5, -2], [-6, 4], [3, 8], [2, 3]], 49.0),
            ([[2, 8], [1, -5], [-2, -1]], 21.5),
            ([[-4, 0], [8, -3], [-1, 7], [4, -6], [-3, 1]], 46.5),
            ([[8, 3], [-3, -1], [-5, -7], [-5, 7], [6, 0]], 91.0),
            ([[-5, -3], [8, -7], [-6, 0], [-2, 8], [-6, 8], [-4, 3]], 77.5),
            ([[6, -4], [5, -1], [8, 3], [-7, -2], [-3, 8], [4, 4]], 69.0),
            ([[3, -5], [5, 2], [6, -8], [2, -4], [-3, -3], [6, -4]], 42.5),
        ],
    )
    def test_largest_triangle_area(self, points: list[list[int]], expected: float):
        result = run_largest_triangle_area(Solution, points)
        assert_largest_triangle_area(result, expected)
