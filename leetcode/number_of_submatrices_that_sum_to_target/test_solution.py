import pytest

from leetcode_py import logged_test

from .helpers import assert_num_submatrix_sum_target, run_num_submatrix_sum_target
from .solution import Solution


class TestNumberOfSubmatricesThatSumToTarget:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "matrix, target, expected",
        [
            ([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0, 4),
            ([[1, -1], [-1, 1]], 0, 5),
            ([[904]], 0, 0),
            ([[1]], 1, 1),
            ([[1, -1]], 0, 1),
            ([[1, 2], [3, 4]], 3, 2),
            ([[0, 0], [0, 0]], 0, 9),
            ([[1, 1, 1], [1, 1, 1]], 2, 7),
            ([[2, 2], [2, 2]], 4, 4),
            ([[1, -1, 1], [-1, 1, -1]], 0, 10),
            ([[5]], 5, 1),
            ([[0, 1], [1, 0]], 1, 6),
        ],
    )
    def test_num_submatrix_sum_target(self, matrix: list[list[int]], target: int, expected: int):
        result = run_num_submatrix_sum_target(Solution, matrix, target)
        assert_num_submatrix_sum_target(result, expected)
