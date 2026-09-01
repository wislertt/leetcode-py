import pytest

from leetcode_py import logged_test

from .helpers import assert_largest_submatrix, run_largest_submatrix
from .solution import Solution


class TestLargestSubmatrixWithRearrangements:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "matrix, expected",
        [
            [[[0, 0, 1], [1, 1, 1], [1, 0, 1]], 4],
            [[[1, 0, 1, 0, 1]], 3],
            [[[1, 1, 0], [1, 0, 1]], 2],
            [[[0]], 0],
            [[[1]], 1],
            [[[1, 1], [1, 1]], 4],
            [[[0, 0], [0, 0]], 0],
            [[[1, 0], [0, 1]], 1],
            [[[0, 1], [1, 0]], 1],
            [[[1, 1, 1, 1]], 4],
            [[[1], [1], [1], [1]], 4],
            [[[0, 1, 1], [1, 1, 1], [1, 0, 0]], 4],
            [[[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 1, 1, 0]], 6],
            [[[0, 1, 1, 1, 1]], 4],
            [[[0, 1, 1, 0], [1, 1, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0], [1, 1, 1, 1]], 8],
            [[[0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [0, 1, 0, 1], [1, 1, 0, 1]], 8],
            [[[1, 1, 1]], 3],
            [[[1], [0], [1], [1], [1]], 3],
        ],
    )
    def test_largest_submatrix(self, matrix: list[list[int]], expected: int):
        result = run_largest_submatrix(Solution, matrix)
        assert_largest_submatrix(result, expected)
