import pytest

from leetcode_py import logged_test

from .helpers import assert_is_power_of_two, run_is_power_of_two
from .solution import Solution


class TestPowerOfTwo:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, True),
            (16, True),
            (3, False),
            (2, True),
            (4, True),
            (8, True),
            (32, True),
            (1024, True),
            (0, False),
            (-1, False),
            (-2, False),
            (-16, False),
            (5, False),
            (6, False),
            (2147483648, True),
            (2147483647, False),
            (1073741824, True),
            (536870912, True),
        ],
    )
    def test_is_power_of_two(self, n: int, expected: bool):
        result = run_is_power_of_two(Solution, n)
        assert_is_power_of_two(result, expected)
