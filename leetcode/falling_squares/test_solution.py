import pytest

from leetcode_py import logged_test

from .helpers import assert_falling_squares, run_falling_squares
from .solution import Solution


class TestFallingSquares:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "positions, expected",
        [
            ([[1, 2], [2, 3], [6, 1]], [2, 5, 5]),
            ([[100, 100], [200, 100]], [100, 100]),
            ([[1, 5]], [5]),
            ([[1, 2], [1, 3]], [2, 5]),
            ([[1, 2], [3, 2]], [2, 2]),
            ([[1, 2], [2, 2], [4, 1]], [2, 4, 4]),
            ([[6, 1], [3, 3], [1, 5], [2, 4], [4, 2]], [1, 3, 8, 12, 14]),
            ([[9, 4], [5, 5], [1, 3], [4, 2], [7, 1]], [4, 9, 9, 11, 11]),
            ([[100000000, 1000000]], [1000000]),
            ([[1, 1000000], [500000, 1000000]], [1000000, 2000000]),
            ([[2, 2], [4, 2], [6, 2], [8, 2]], [2, 2, 2, 2]),
            ([[1, 3], [1, 3], [1, 3]], [3, 6, 9]),
            ([[4, 1], [9, 1], [3, 1], [1, 4]], [1, 1, 1, 5]),
            ([[3, 4], [3, 2]], [4, 6]),
            ([[10, 1], [2, 1], [10, 5], [10, 4], [8, 1], [6, 4]], [1, 1, 6, 10, 10, 10]),
            ([[11, 1], [9, 3], [5, 3], [11, 4]], [1, 4, 4, 8]),
            ([[7, 5], [5, 3], [12, 5], [3, 2], [1, 1]], [5, 8, 8, 8, 8]),
            ([[5, 1], [12, 4]], [1, 4]),
            ([[6, 2], [1, 3], [5, 3], [2, 4], [7, 1], [3, 2]], [2, 3, 5, 9, 9, 11]),
            ([[1, 5], [1, 5], [9, 1], [5, 5]], [5, 10, 10, 15]),
        ],
    )
    def test_falling_squares(self, positions: list[list[int]], expected: list[int]):
        result = run_falling_squares(Solution, positions)
        assert_falling_squares(result, expected)
