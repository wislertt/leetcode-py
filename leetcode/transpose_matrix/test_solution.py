import pytest

from leetcode_py import logged_test

from .helpers import assert_transpose, run_transpose
from .solution import Solution


class TestTransposeMatrix:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "matrix, expected",
        [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 4, 7], [2, 5, 8], [3, 6, 9]]),
            ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]),
            ([[1]], [[1]]),
            ([[1, 2]], [[1], [2]]),
            ([[1], [2]], [[1, 2]]),
            ([[1, 2, 3, 4], [5, 6, 7, 8]], [[1, 5], [2, 6], [3, 7], [4, 8]]),
            ([[-1, 0], [3, 5]], [[-1, 3], [0, 5]]),
            ([[0]], [[0]]),
            ([[1, 2], [3, 4], [5, 6], [7, 8]], [[1, 3, 5, 7], [2, 4, 6, 8]]),
            ([[1000000000]], [[1000000000]]),
            ([[1, 2, 3]], [[1], [2], [3]]),
            ([[1], [2], [3]], [[1, 2, 3]]),
            ([[9, 8, 7], [6, 5, 4], [3, 2, 1]], [[9, 6, 3], [8, 5, 2], [7, 4, 1]]),
            ([[5, 5], [5, 5]], [[5, 5], [5, 5]]),
        ],
    )
    def test_transpose(self, matrix: list[list[int]], expected: list[list[int]]):
        result = run_transpose(Solution, matrix)
        assert_transpose(result, expected)
