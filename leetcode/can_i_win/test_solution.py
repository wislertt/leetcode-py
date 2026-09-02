import pytest

from leetcode_py import logged_test

from .helpers import assert_can_i_win, run_can_i_win
from .solution import Solution


class TestCanIWin:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "max_choosable_integer, desired_total, expected",
        [
            (10, 11, False),
            (10, 0, True),
            (10, 1, True),
            (1, 1, True),
            (1, 2, False),
            (2, 2, True),
            (2, 3, False),
            (2, 4, False),
            (3, 6, True),
            (3, 7, False),
            (4, 6, True),
            (4, 10, False),
            (5, 15, True),
            (5, 16, False),
            (5, 50, False),
            (6, 20, False),
            (7, 28, True),
            (7, 29, False),
            (8, 36, False),
            (10, 40, False),
            (10, 55, False),
            (10, 56, False),
        ],
    )
    def test_can_i_win(self, max_choosable_integer: int, desired_total: int, expected: bool):
        result = run_can_i_win(Solution, max_choosable_integer, desired_total)
        assert_can_i_win(result, expected)
