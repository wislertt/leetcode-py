import pytest

from leetcode_py import logged_test

from .helpers import assert_int_to_roman, run_int_to_roman
from .solution import Solution


class TestIntegerToRoman:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num, expected",
        [
            (3749, "MMMDCCXLIX"),
            (58, "LVIII"),
            (1994, "MCMXCIV"),
            (1, "I"),
            (3999, "MMMCMXCIX"),
            (3, "III"),
            (4, "IV"),
            (8, "VIII"),
            (9, "IX"),
            (14, "XIV"),
            (40, "XL"),
            (90, "XC"),
            (400, "CD"),
            (900, "CM"),
            (1000, "M"),
            (444, "CDXLIV"),
            (999, "CMXCIX"),
            (1776, "MDCCLXXVI"),
            (2024, "MMXXIV"),
            (3549, "MMMDXLIX"),
        ],
    )
    def test_int_to_roman(self, num: int, expected: str):
        result = run_int_to_roman(Solution, num)
        assert_int_to_roman(result, expected)
