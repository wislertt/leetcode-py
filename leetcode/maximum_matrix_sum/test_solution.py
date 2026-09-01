import pytest

from leetcode_py import logged_test

from .helpers import assert_max_matrix_sum, run_max_matrix_sum
from .solution import Solution


class TestMaximumMatrixSum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "matrix, expected",
        [
            ([[1, -1], [-1, 1]], 4),
            ([[1, 2, 3], [-1, -2, -3], [1, 2, 3]], 16),
            ([[1, 2], [3, 4]], 10),
            ([[-1, -2], [-3, -4]], 10),
            ([[-1, -1], [-1, -1]], 4),
            ([[1, -1], [1, -1]], 4),
            ([[0, 0], [0, 0]], 0),
            ([[-1, 0], [0, -1]], 2),
            ([[100000, -100000], [-100000, 100000]], 400000),
            ([[1, -1, 1], [-1, 1, -1], [1, -1, 1]], 9),
            ([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]], 7),
            ([[2, -2, 2], [2, 2, 2], [-2, 2, -2]], 14),
            ([[-5, 3], [2, -7]], 17),
            ([[9, -9, 9], [-9, 9, -9], [9, -9, 8]], 80),
            ([[-1, 2, -3, 4], [5, -6, 7, -8], [-9, 10, -11, 12], [13, -14, 15, -16]], 136),
            ([[-2, -3, 0, -3], [-2, 2, -3, -2], [-2, 2, 0, -1], [-1, -1, 1, 1]], 26),
            ([[-1, 0, 3, 0], [-1, 2, 3, 0], [0, -3, 2, -2], [1, -1, 1, -2]], 22),
            ([[3, -1, 0], [1, -3, 0], [-1, 2, -1]], 12),
            ([[-3, -2], [1, -1]], 5),
            ([[0, -2, 0], [0, -3, -1], [0, 3, -3]], 12),
        ],
    )
    def test_max_matrix_sum(self, matrix: list[list[int]], expected: int):
        result = run_max_matrix_sum(Solution, matrix)
        assert_max_matrix_sum(result, expected)
