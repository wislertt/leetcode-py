import pytest

from leetcode_py import logged_test

from .helpers import assert_num_squares, run_num_squares
from .solution import Solution


class TestPerfectSquares:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (12, 3),
            (13, 2),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 1),
            (5, 2),
            (9, 1),
            (16, 1),
            (18, 2),
            (25, 1),
            (50, 2),
            (7, 4),
            (100, 1),
            (43, 3),
            (8, 2),
            (11, 3),
        ],
    )
    def test_num_squares(self, n: int, expected: int):
        result = run_num_squares(Solution, n)
        assert_num_squares(result, expected)
