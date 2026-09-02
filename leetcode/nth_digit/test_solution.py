import pytest

from leetcode_py import logged_test

from .helpers import assert_find_nth_digit, run_find_nth_digit
from .solution import Solution


class TestNthDigit:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (3, 3),
            (11, 0),
            (1, 1),
            (2, 2),
            (8, 8),
            (9, 9),
            (10, 1),
            (15, 2),
            (100, 5),
            (189, 9),
            (190, 1),
            (1000, 3),
            (2889, 9),
            (2890, 1),
            (10000, 7),
            (38889, 9),
            (38890, 1),
            (100000, 2),
            (488889, 9),
            (488890, 1),
            (1000000, 1),
            (12345, 3),
            (99999, 1),
            (999999, 4),
            (123456789, 2),
            (999999999, 9),
            (1000000000, 1),
            (2147483646, 2),
            (2147483647, 2),
        ],
    )
    def test_find_nth_digit(self, n: int, expected: int):
        result = run_find_nth_digit(Solution, n)
        assert_find_nth_digit(result, expected)
