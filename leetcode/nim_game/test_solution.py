import pytest

from leetcode_py import logged_test

from .helpers import assert_can_win_nim, run_can_win_nim
from .solution import Solution


class TestNimGame:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (4, False),
            (1, True),
            (2, True),
            (3, True),
            (5, True),
            (6, True),
            (7, True),
            (8, False),
            (9, True),
            (10, True),
            (11, True),
            (12, False),
            (13, True),
            (16, False),
            (20, False),
            (100, False),
            (1000, False),
            (2147483647, True),
            (2147483646, True),
            (2147483644, False),
        ],
    )
    def test_can_win_nim(self, n: int, expected: bool):
        result = run_can_win_nim(Solution, n)
        assert_can_win_nim(result, expected)
