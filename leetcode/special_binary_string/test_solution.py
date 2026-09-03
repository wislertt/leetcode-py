import pytest

from leetcode_py import logged_test

from .helpers import assert_make_largest_special, run_make_largest_special
from .solution import Solution


class TestSpecialBinaryString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("10", "10"),
            ("1100", "1100"),
            ("11011000", "11100100"),
            ("1010", "1010"),
            ("110100", "110100"),
            ("111000", "111000"),
            ("11001100", "11001100"),
            ("11110000", "11110000"),
            ("10101010", "10101010"),
            ("110010", "110010"),
            ("1101010010", "1101010010"),
            ("111000111000", "111000111000"),
            ("10110101100010", "11100101001010"),
            ("1011010100110010", "1101010011001010"),
            ("11011010001101110000", "11110001001110100100"),
            ("111111000001001011011000", "111111000001001110010010"),
            ("1100111011100111000101000100", "1111110001100101001001001100"),
            ("11011110111100010000110111000000", "11111111000100100011110001000100"),
            ("111011010100111110011001001000101000", "111111100110010010001101010010101000"),
        ],
    )
    def test_make_largest_special(self, s: str, expected: str):
        result = run_make_largest_special(Solution, s)
        assert_make_largest_special(result, expected)
