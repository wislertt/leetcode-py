import pytest

from leetcode_py import logged_test

from .helpers import assert_sliding_puzzle, run_sliding_puzzle
from .solution import Solution


class TestSlidingPuzzle:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "board, expected",
        [
            ([[1, 2, 3], [4, 0, 5]], 1),
            ([[1, 2, 3], [5, 4, 0]], -1),
            ([[4, 1, 2], [5, 0, 3]], 5),
            ([[1, 2, 3], [4, 5, 0]], 0),
            ([[3, 2, 4], [1, 5, 0]], 14),
            ([[0, 1, 2], [3, 4, 5]], 15),
            ([[1, 0, 2], [3, 4, 5]], 14),
            ([[1, 2, 0], [3, 4, 5]], 13),
            ([[2, 3, 4], [1, 5, 0]], -1),
            ([[1, 4, 2], [3, 5, 0]], 16),
            ([[3, 4, 5], [1, 2, 0]], 10),
            ([[0, 5, 4], [3, 2, 1]], 15),
        ],
    )
    def test_sliding_puzzle(self, board: list[list[int]], expected: int):
        result = run_sliding_puzzle(Solution, board)
        assert_sliding_puzzle(result, expected)
