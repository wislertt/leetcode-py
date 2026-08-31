import pytest

from leetcode_py import logged_test

from .helpers import assert_multiply, run_multiply
from .solution import Solution


class TestSparseMatrixMultiplication:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "mat1, mat2, expected",
        [
            ([[1, 0, 0], [-1, 0, 3]], [[7, 0, 0], [0, 0, 0], [0, 0, 1]], [[7, 0, 0], [-7, 0, 3]]),
            ([[0]], [[0]], [[0]]),
            ([[1, 0], [0, 1]], [[5, 6], [7, 8]], [[5, 6], [7, 8]]),
            ([[3]], [[4]], [[12]]),
            ([[1, 2, 3]], [[4], [5], [6]], [[32]]),
            ([[1], [2], [3]], [[4, 5, 6]], [[4, 5, 6], [8, 10, 12], [12, 15, 18]]),
            ([[-1, 0], [0, -1]], [[2, 3], [4, 5]], [[-2, -3], [-4, -5]]),
            ([[0, 0], [0, 0]], [[1, 2], [3, 4]], [[0, 0], [0, 0]]),
            (
                [[1, 0, 0], [0, 0, 0], [0, 0, 2]],
                [[0, 3, 0], [0, 0, 0], [5, 0, 0]],
                [[0, 3, 0], [0, 0, 0], [10, 0, 0]],
            ),
            ([[1, 2], [3, 4]], [[5, 6], [7, 8]], [[19, 22], [43, 50]]),
            ([[0, 1], [1, 0]], [[0, 1], [1, 0]], [[1, 0], [0, 1]]),
            ([[10]], [[-10]], [[-100]]),
            ([[1, 1], [1, 1]], [[1, 1], [1, 1]], [[2, 2], [2, 2]]),
            ([[2, 0, 1], [0, 3, 0]], [[1, 0], [0, 1], [1, 1]], [[3, 1], [0, 3]]),
            ([[1, 0, 0], [0, 0, 2]], [[0, 3], [0, 0], [5, 0]], [[0, 3], [10, 0]]),
        ],
    )
    def test_multiply(
        self, mat1: list[list[int]], mat2: list[list[int]], expected: list[list[int]]
    ):
        result = run_multiply(Solution, mat1, mat2)
        assert_multiply(result, expected)
