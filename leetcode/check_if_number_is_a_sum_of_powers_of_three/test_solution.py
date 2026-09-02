import pytest

from leetcode_py import logged_test

from .helpers import assert_check_powers_of_three, run_check_powers_of_three
from .solution import Solution


class TestCheckIfNumberIsASumOfPowersOfThree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (12, True),
            (91, True),
            (21, False),
            (1, True),
            (2, False),
            (3, True),
            (4, True),
            (5, False),
            (6, False),
            (7, False),
            (8, False),
            (9, True),
            (10, True),
            (11, False),
            (13, True),
            (14, False),
            (15, False),
            (27, True),
            (28, True),
            (30, True),
            (81, True),
            (82, True),
            (100, False),
            (121, True),
            (243, True),
            (729, True),
            (1000, True),
            (364, True),
            (1093, True),
            (9841, True),
            (999999, False),
            (1000000, False),
            (9999999, False),
            (10000000, False),
            (9999998, False),
            (59049, True),
            (59050, True),
            (1594323, True),
            (4782969, True),
            (4782970, True),
            (8887159, False),
            (9661959, False),
            (5593761, False),
            (5755009, False),
            (1564519, False),
            (3876056, False),
            (5074422, False),
            (7493246, False),
        ],
    )
    def test_check_powers_of_three(self, n: int, expected: bool):
        result = run_check_powers_of_three(Solution, n)
        assert_check_powers_of_three(result, expected)
