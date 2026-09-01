import pytest

from leetcode_py import logged_test

from .helpers import assert_count_good_strings, run_count_good_strings
from .solution import Solution


class TestCountWaysToBuildGoodStrings:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "low, high, zero, one, expected",
        [
            (3, 3, 1, 1, 8),
            (2, 3, 1, 2, 5),
            (1, 1, 1, 1, 2),
            (1, 2, 1, 1, 6),
            (2, 2, 1, 1, 4),
            (4, 4, 1, 2, 5),
            (5, 5, 2, 2, 0),
            (7, 9, 3, 4, 4),
            (10, 12, 2, 3, 28),
            (15, 20, 5, 6, 9),
            (2, 10, 1, 2, 230),
            (100, 100, 50, 50, 4),
            (1000, 1000, 500, 500, 4),
            (50, 60, 7, 11, 93),
            (3, 30, 2, 3, 7736),
            (200, 250, 13, 17, 153968),
            (1, 100000, 1, 1, 215447031),
            (100000, 100000, 1, 1, 607723520),
            (99999, 100000, 3, 5, 393881602),
            (100000, 100000, 99999, 99999, 0),
        ],
    )
    def test_count_good_strings(self, low: int, high: int, zero: int, one: int, expected: int):
        result = run_count_good_strings(Solution, low, high, zero, one)
        assert_count_good_strings(result, expected)
