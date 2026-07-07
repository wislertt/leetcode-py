import pytest

from leetcode_py import logged_test

from .helpers import assert_roman_to_int, run_roman_to_int
from .solution import Solution


class TestRomanToInteger:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("III", 3),
            ("LVIII", 58),
            ("MCMXCIV", 1994),
            ("I", 1),
            ("V", 5),
            ("X", 10),
            ("IV", 4),
            ("IX", 9),
            ("XL", 40),
            ("XC", 90),
            ("CD", 400),
            ("CM", 900),
            ("MMMCMXCIX", 3999),
            ("MMMDCCCLXXXVIII", 3888),
            ("DCXXI", 621),
            ("MCMXC", 1990),
        ],
    )
    def test_roman_to_int(self, s: str, expected: int):
        result = run_roman_to_int(Solution, s)
        assert_roman_to_int(result, expected)
