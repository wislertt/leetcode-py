import pytest

from leetcode_py import logged_test

from .helpers import assert_maximum_odd_binary_number, run_maximum_odd_binary_number
from .solution import Solution


class TestMaximumOddBinaryNumber:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("010", "001"),
            ("0101", "1001"),
            ("1", "1"),
            ("0011100", "1100001"),
            ("11100000", "11000001"),
            ("1000", "0001"),
            ("011111", "111101"),
            ("010101010101", "111110000001"),
            ("00001", "00001"),
            ("11111111111111111111", "11111111111111111111"),
            ("00000000000000000001", "00000000000000000001"),
            ("110000000", "100000001"),
            ("011000", "100001"),
            ("01", "01"),
        ],
    )
    def test_maximum_odd_binary_number(self, s: str, expected: str):
        result = run_maximum_odd_binary_number(Solution, s)
        assert_maximum_odd_binary_number(result, expected)
