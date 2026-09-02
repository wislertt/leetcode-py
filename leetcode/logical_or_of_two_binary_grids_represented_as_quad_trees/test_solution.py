import pytest

from leetcode_py import logged_test

from .helpers import assert_intersect, run_intersect
from .solution import Solution


class TestLogicalOrOfTwoBinaryGridsRepresentedAsQuadTrees:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid1, grid2, expected",
        [
            ([[0]], [[0]], [[0]]),
            ([[0]], [[1]], [[1]]),
            ([[1]], [[0]], [[1]]),
            ([[1]], [[1]], [[1]]),
            ([[1, 1], [1, 1]], [[0, 1], [1, 0]], [[1, 1], [1, 1]]),
            ([[0, 1], [1, 0]], [[1, 1], [1, 1]], [[1, 1], [1, 1]]),
            ([[0, 0], [0, 0]], [[0, 1], [1, 0]], [[0, 1], [1, 0]]),
            ([[1, 0], [0, 1]], [[0, 0], [0, 0]], [[1, 0], [0, 1]]),
            ([[0, 1], [1, 0]], [[1, 0], [0, 1]], [[1, 1], [1, 1]]),
            ([[0, 1], [0, 1]], [[1, 0], [1, 0]], [[1, 1], [1, 1]]),
            ([[0, 0], [1, 1]], [[1, 0], [1, 0]], [[1, 0], [1, 1]]),
            ([[0, 1], [1, 1]], [[1, 0], [1, 1]], [[1, 1], [1, 1]]),
            ([[1, 0], [0, 1]], [[0, 1], [1, 0]], [[1, 1], [1, 1]]),
            ([[1, 0], [1, 1]], [[0, 1], [1, 0]], [[1, 1], [1, 1]]),
            ([[0, 0], [0, 1]], [[0, 0], [1, 0]], [[0, 0], [1, 1]]),
            ([[1, 1], [0, 0]], [[0, 1], [0, 1]], [[1, 1], [0, 1]]),
            ([[1, 1], [1, 0]], [[1, 1], [1, 0]], [[1, 1], [1, 0]]),
            ([[0, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]),
        ],
    )
    def test_intersect(
        self, grid1: list[list[int]], grid2: list[list[int]], expected: list[list[int]]
    ):
        result = run_intersect(Solution, grid1, grid2)
        assert_intersect(result, expected)
