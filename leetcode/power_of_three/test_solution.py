import pytest

from leetcode_py import logged_test

from .helpers import assert_is_power_of_three, run_is_power_of_three
from .solution import Solution


class TestPowerOfThree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (27, True),
            (0, False),
            (-1, False),
            (1, True),
            (3, True),
            (9, True),
            (2, False),
            (6, False),
            (45, False),
            (81, True),
            (243, True),
            (729, True),
            (1162261467, True),
            (2147483647, False),
            (-3, False),
            (-27, False),
            (2147483646, False),
            (59049, True),
            (1594323, True),
            (15, False),
        ],
    )
    def test_is_power_of_three(self, n: int, expected: bool):
        result = run_is_power_of_three(Solution, n)
        assert_is_power_of_three(result, expected)
