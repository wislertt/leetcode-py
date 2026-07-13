import pytest

from leetcode_py import logged_test

from .helpers import assert_total_n_queens, run_total_n_queens
from .solution import Solution


class TestTestNQueensII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, 1),
            (2, 0),
            (3, 0),
            (4, 2),
            (5, 10),
            (6, 4),
            (7, 40),
            (8, 92),
            (9, 352),
            (8, 92),
            (9, 352),
        ],
    )
    def test_total_n_queens(self, n: int, expected: int):
        result = run_total_n_queens(Solution, n)
        assert_total_n_queens(result, expected)
