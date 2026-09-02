import pytest

from leetcode_py import logged_test

from .helpers import assert_compute_area, run_compute_area
from .solution import Solution


class TestRectangleArea:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "ax1, ay1, ax2, ay2, bx1, by1, bx2, by2, expected",
        [
            (-3, 0, 3, 4, 0, -1, 9, 2, 45),
            (-2, -2, 2, 2, -2, -2, 2, 2, 16),
            (0, 0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 1, 1, 2, 2, 3, 3, 2),
            (0, 0, 1, 1, -1, -1, 0, 0, 2),
            (0, 0, 2, 2, 2, 0, 4, 2, 8),
            (0, 0, 4, 4, 1, 1, 2, 2, 16),
            (0, 0, 4, 4, 4, 4, 8, 8, 32),
            (-5, -5, -1, -1, -3, -3, 1, 1, 28),
            (10000, -10000, 10000, 10000, -10000, -10000, 10000, 10000, 400000000),
            (-10000, -10000, 10000, 10000, -10000, -10000, 10000, 10000, 400000000),
            (-10000, -10000, 10000, 10000, 0, 0, 1, 1, 400000000),
            (0, 2, 1, 7, -4, 6, 4, 10, 36),
            (-7, 0, 7, 9, -10, -10, 9, -7, 183),
            (-8, 1, 1, 2, -2, -8, 1, -5, 18),
            (2, -2, 3, -2, -10, -8, 8, -4, 72),
            (-7, -9, 10, 5, 1, 1, 6, 8, 253),
            (-7, 2, 7, 7, 2, -6, 8, 0, 106),
        ],
    )
    def test_compute_area(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
        expected: int,
    ):
        result = run_compute_area(Solution, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
        assert_compute_area(result, expected)
