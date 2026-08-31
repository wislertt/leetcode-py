import pytest

from leetcode_py import logged_test

from .helpers import assert_matrix_score, run_matrix_score
from .solution import Solution


class TestScoreAfterFlippingMatrix:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]], 39),
            ([[0]], 1),
            ([[1], [0]], 2),
            ([[1, 1], [1, 0], [0, 0]], 8),
            ([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 18),
            ([[0, 0], [0, 0]], 6),
            ([[1, 0], [0, 0], [1, 0]], 8),
            ([[0], [1]], 2),
            ([[0], [0], [1], [0]], 4),
            ([[0, 1]], 3),
            ([[0, 0]], 3),
            ([[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]], 42),
            ([[1, 1, 1], [1, 0, 0], [0, 0, 1], [1, 1, 1]], 24),
            ([[0], [1], [0]], 3),
        ],
    )
    def test_matrix_score(self, grid: list[list[int]], expected: int):
        result = run_matrix_score(Solution, grid)
        assert_matrix_score(result, expected)
