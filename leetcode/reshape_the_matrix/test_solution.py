import pytest

from leetcode_py import logged_test

from .helpers import assert_matrix_reshape, run_matrix_reshape
from .solution import Solution


class TestReshapeTheMatrix:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "mat, r, c, expected",
        [
            ([[1, 2], [3, 4]], 1, 4, [[1, 2, 3, 4]]),
            ([[1, 2], [3, 4]], 2, 4, [[1, 2], [3, 4]]),
            ([[1, 2], [3, 4]], 2, 2, [[1, 2], [3, 4]]),
            ([[1, 2], [3, 4]], 4, 1, [[1], [2], [3], [4]]),
            ([[1, 2], [3, 4]], 1, 2, [[1, 2], [3, 4]]),
            ([[1, 2], [3, 4]], 3, 2, [[1, 2], [3, 4]]),
            ([[1]], 1, 1, [[1]]),
            ([[1, 2, 3]], 3, 1, [[1], [2], [3]]),
            ([[1], [2], [3]], 1, 3, [[1, 2, 3]]),
            ([[-1, 0], [5, -1000]], 1, 4, [[-1, 0, 5, -1000]]),
            ([[0, 0], [0, 0]], 4, 1, [[0], [0], [0], [0]]),
            ([[7, 8, 9, 10]], 2, 2, [[7, 8], [9, 10]]),
            ([[1000, -1000]], 2, 1, [[1000], [-1000]]),
            ([[1, 2, 3], [4, 5, 6]], 2, 3, [[1, 2, 3], [4, 5, 6]]),
            ([[1, 2, 3], [4, 5, 6]], 3, 2, [[1, 2], [3, 4], [5, 6]]),
            ([[1, 2, 3], [4, 5, 6]], 6, 1, [[1], [2], [3], [4], [5], [6]]),
            ([[1, 2, 3], [4, 5, 6]], 2, 6, [[1, 2, 3], [4, 5, 6]]),
            ([[5]], 2, 3, [[5]]),
            ([[-20, -67, 11], [-80, 2, -84]], 2, 3, [[-20, -67, 11], [-80, 2, -84]]),
            ([[-7]], 1, 1, [[-7]]),
        ],
    )
    def test_matrix_reshape(self, mat: list[list[int]], r: int, c: int, expected: list[list[int]]):
        result = run_matrix_reshape(Solution, mat, r, c)
        assert_matrix_reshape(result, expected)
