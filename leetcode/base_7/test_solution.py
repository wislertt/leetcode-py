import pytest

from leetcode_py import logged_test

from .helpers import assert_convert_to_base_7, run_convert_to_base_7
from .solution import Solution


class TestBase7:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num, expected",
        [
            (100, "202"),
            (-7, "-10"),
            (0, "0"),
            (1, "1"),
            (-1, "-1"),
            (7, "10"),
            (-100, "-202"),
            (6, "6"),
            (-6, "-6"),
            (49, "100"),
            (-49, "-100"),
            (343, "1000"),
            (-343, "-1000"),
            (2401, "10000"),
            (16807, "100000"),
            (823543, "10000000"),
            (5764801, "100000000"),
            (10000000, "150666343"),
            (-10000000, "-150666343"),
            (9999999, "150666342"),
            (-9999999, "-150666342"),
            (123456, "1022634"),
            (-654321, "-5363433"),
            (777, "2160"),
            (-777, "-2160"),
        ],
    )
    def test_convert_to_base_7(self, num: int, expected: str):
        result = run_convert_to_base_7(Solution, num)
        assert_convert_to_base_7(result, expected)
