import pytest

from leetcode_py import logged_test

from .helpers import assert_max_sum_submatrix, run_max_sum_submatrix
from .solution import Solution


class TestMaxSumOfRectangleNoLargerThanK:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "matrix, k, expected",
        [
            ([[1, 0, 1], [0, -2, 3]], 2, 2),
            ([[2, 2, -1]], 3, 3),
            ([[1]], 1, 1),
            ([[-5]], -5, -5),
            ([[1, 2], [3, 4]], 4, 4),
            ([[2, 2], [-1, 3]], 4, 4),
            ([[5, -3], [2, 1]], 3, 3),
            ([[-1, -2], [-3, -4]], -3, -3),
            ([[0, 0], [0, 0]], 0, 0),
            ([[1, -1, 2]], 1, 1),
            ([[10, -10, 10]], 5, 0),
            ([[3, 3], [3, 3]], 7, 6),
            ([[100, -100]], 0, 0),
            ([[4, -4, 4], [-4, 4, -4]], 4, 4),
            ([[3], [-3]], -1, -3),
            ([[3]], 3, 3),
            ([[-3, -2, 0, -2]], -7, -7),
            ([[3, 2]], 3, 3),
            ([[1, -3, 5], [0, 4, -5]], 0, 0),
            ([[2, 5, -3], [1, -3, -4]], -3, -3),
        ],
    )
    def test_max_sum_submatrix(self, matrix: list[list[int]], k: int, expected: int):
        result = run_max_sum_submatrix(Solution, matrix, k)
        assert_max_sum_submatrix(result, expected)
