import pytest

from leetcode_py import logged_test

from .helpers import assert_monotone_increasing_digits, run_monotone_increasing_digits
from .solution import Solution


class TestMonotoneIncreasingDigits:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (10, 9),
            (1234, 1234),
            (332, 299),
            (0, 0),
            (1, 1),
            (9, 9),
            (11, 11),
            (21, 19),
            (32, 29),
            (100, 99),
            (120, 119),
            (321, 299),
            (666, 666),
            (999, 999),
            (54321, 49999),
            (123321, 122999),
            (555555, 555555),
            (987654321, 899999999),
            (666666666, 666666666),
            (1000000000, 999999999),
        ],
    )
    def test_monotone_increasing_digits(self, n: int, expected: int):
        result = run_monotone_increasing_digits(Solution, n)
        assert_monotone_increasing_digits(result, expected)
