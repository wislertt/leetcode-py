import pytest

from leetcode_py import logged_test

from .helpers import assert_divide, run_divide
from .solution import Solution


class TestDivideTwoIntegers:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "dividend, divisor, expected",
        [
            (10, 3, 3),
            (7, -3, -2),
            (0, 1, 0),
            (0, -5, 0),
            (1, 1, 1),
            (1, -1, -1),
            (-1, 1, -1),
            (-1, -1, 1),
            (100, -7, -14),
            (-100, -7, 14),
            (-100, 7, -14),
            (15, 4, 3),
            (-15, 4, -3),
            (5, -2, -2),
            (2147483647, 1, 2147483647),
            (2147483647, 2, 1073741823),
            (2147483647, -1, -2147483647),
            (-2147483648, -1, 2147483647),
            (-2147483648, 1, -2147483648),
            (-2147483648, 2, -1073741824),
            (-2147483648, -2, 1073741824),
            (3, 3, 1),
            (6, 2, 3),
        ],
    )
    def test_divide(self, dividend: int, divisor: int, expected: int):
        result = run_divide(Solution, dividend, divisor)
        assert_divide(result, expected)
