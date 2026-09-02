import pytest

from leetcode_py import logged_test

from .helpers import assert_fraction_to_decimal, run_fraction_to_decimal
from .solution import Solution


class TestFractionToRecurringDecimal:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "numerator, denominator, expected",
        [
            (1, 2, "0.5"),
            (2, 1, "2"),
            (4, 333, "0.(012)"),
            (1, 3, "0.(3)"),
            (2, 3, "0.(6)"),
            (1, 6, "0.1(6)"),
            (22, 7, "3.(142857)"),
            (100, 3, "33.(3)"),
            (1, 90, "0.0(1)"),
            (-1, 2, "-0.5"),
            (-1, 3, "-0.(3)"),
            (-50, 8, "-6.25"),
            (7, -12, "-0.58(3)"),
            (0, 3, "0"),
            (0, -5, "0"),
            (-2147483648, -1, "2147483648"),
            (-2147483648, 1, "-2147483648"),
            (1, -2147483648, "-0.0000000004656612873077392578125"),
            (-7, 14, "-0.5"),
            (5, 4, "1.25"),
        ],
    )
    def test_fraction_to_decimal(self, numerator: int, denominator: int, expected: str):
        result = run_fraction_to_decimal(Solution, numerator, denominator)
        assert_fraction_to_decimal(result, expected)
