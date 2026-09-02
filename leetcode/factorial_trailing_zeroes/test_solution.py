import pytest

from leetcode_py import logged_test

from .helpers import assert_trailing_zeroes, run_trailing_zeroes
from .solution import Solution


class TestFactorialTrailingZeroes:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
            (4, 0),
            (5, 1),
            (6, 1),
            (10, 2),
            (15, 3),
            (24, 4),
            (25, 6),
            (26, 6),
            (30, 7),
            (49, 10),
            (50, 12),
            (100, 24),
            (124, 28),
            (125, 31),
            (200, 49),
            (300, 74),
            (624, 152),
            (625, 156),
            (1000, 249),
            (2500, 624),
            (9999, 2495),
            (10000, 2499),
        ],
    )
    def test_trailing_zeroes(self, n: int, expected: int):
        result = run_trailing_zeroes(Solution, n)
        assert_trailing_zeroes(result, expected)
