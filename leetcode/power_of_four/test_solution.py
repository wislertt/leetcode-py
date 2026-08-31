import pytest

from leetcode_py import logged_test

from .helpers import assert_is_power_of_four, run_is_power_of_four
from .solution import Solution


class TestPowerOfFour:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (16, True),
            (5, False),
            (1, True),
            (4, True),
            (8, False),
            (64, True),
            (256, True),
            (1024, True),
            (2, False),
            (3, False),
            (0, False),
            (-4, False),
            (-1, False),
            (2147483647, False),
            (1073741824, True),
            (20, False),
            (12, False),
            (65536, True),
            (17, False),
            (268435456, True),
            (31, False),
        ],
    )
    def test_is_power_of_four(self, n: int, expected: bool):
        result = run_is_power_of_four(Solution, n)
        assert_is_power_of_four(result, expected)
