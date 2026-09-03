import pytest

from leetcode_py import logged_test

from .helpers import assert_knight_probability, run_knight_probability
from .solution import Solution


class TestKnightProbabilityInChessboard:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, k, row, column, expected",
        [
            (3, 2, 0, 0, 0.0625),
            (1, 0, 0, 0, 1.0),
            (3, 1, 0, 0, 0.25),
            (1, 1, 0, 0, 0.0),
            (2, 1, 0, 0, 0.0),
            (3, 0, 0, 0, 1.0),
            (3, 2, 1, 1, 0.0),
            (3, 3, 0, 0, 0.015625),
            (3, 4, 1, 1, 0.0),
            (4, 2, 0, 0, 0.125),
            (4, 3, 1, 2, 0.0703125),
            (5, 2, 2, 2, 0.375),
            (5, 4, 0, 0, 0.046875),
            (8, 3, 4, 4, 0.62109375),
            (8, 4, 0, 0, 0.0986328125),
            (25, 1, 12, 12, 1.0),
            (25, 0, 24, 24, 1.0),
            (6, 5, 2, 3, 0.13720703125),
            (2, 3, 0, 1, 0.0),
            (3, 6, 0, 0, 0.000244140625),
        ],
    )
    def test_knight_probability(self, n: int, k: int, row: int, column: int, expected: float):
        result = run_knight_probability(Solution, n, k, row, column)
        assert_knight_probability(result, expected)
