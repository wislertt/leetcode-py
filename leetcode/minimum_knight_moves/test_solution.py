import pytest

from leetcode_py import logged_test

from .helpers import assert_min_knight_moves, run_min_knight_moves
from .solution import Solution


class TestMinimumKnightMoves:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "x, y, expected",
        [
            (0, 0, 0),
            (2, 1, 1),
            (1, 2, 1),
            (-2, 1, 1),
            (1, 1, 2),
            (-1, -1, 2),
            (1, 0, 3),
            (0, 1, 3),
            (3, 0, 3),
            (2, 0, 2),
            (0, 2, 2),
            (3, 3, 2),
            (2, 2, 4),
            (2, 3, 3),
            (4, 4, 4),
            (6, 6, 4),
            (5, 5, 4),
            (7, 7, 6),
            (300, 300, 200),
        ],
    )
    def test_min_knight_moves(self, x: int, y: int, expected: int):
        result = run_min_knight_moves(Solution, x, y)
        assert_min_knight_moves(result, expected)
