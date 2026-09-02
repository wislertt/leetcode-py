import pytest

from leetcode_py import logged_test

from .helpers import assert_bulb_switch, run_bulb_switch
from .solution import Solution


class TestBulbSwitcher:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (0, 0),
            (1, 1),
            (2, 1),
            (3, 1),
            (4, 2),
            (5, 2),
            (6, 2),
            (7, 2),
            (8, 2),
            (9, 3),
            (10, 3),
            (11, 3),
            (12, 3),
            (15, 3),
            (16, 4),
            (17, 4),
            (24, 4),
            (25, 5),
            (26, 5),
            (35, 5),
            (36, 6),
            (37, 6),
            (49, 7),
            (50, 7),
            (99, 9),
            (100, 10),
            (101, 10),
            (999, 31),
            (1000, 31),
            (12345, 111),
            (999999, 999),
            (100000000, 10000),
            (1000000000, 31622),
        ],
    )
    def test_bulb_switch(self, n: int, expected: int):
        result = run_bulb_switch(Solution, n)
        assert_bulb_switch(result, expected)
