import pytest

from leetcode_py import logged_test

from .helpers import assert_reordered_power_of_2, run_reordered_power_of_2
from .solution import Solution


class TestReorderedPowerOf2:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, True),
            (10, False),
            (2, True),
            (4, True),
            (8, True),
            (16, True),
            (24, False),
            (32, True),
            (46, True),
            (64, True),
            (125, True),
            (128, True),
            (152, True),
            (218, True),
            (512, True),
            (1024, True),
            (4096, True),
            (6094, True),
            (8210, False),
            (1000, False),
            (9999, False),
            (65536, True),
            (131072, True),
            (102400, False),
            (1048576, True),
            (1234567, False),
            (536870912, True),
            (999999999, False),
            (123456789, False),
            (987654321, False),
            (444094478, False),
            (725927240, False),
            (427242187, False),
            (254604626, False),
            (661569692, False),
            (246871001, False),
        ],
    )
    def test_reordered_power_of_2(self, n: int, expected: bool):
        result = run_reordered_power_of_2(Solution, n)
        assert_reordered_power_of_2(result, expected)
