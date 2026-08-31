import pytest

from leetcode_py import logged_test

from .helpers import assert_max_equal_rows_after_flips, run_max_equal_rows_after_flips
from .solution import Solution


class TestFlipColumnsForMaximumNumberOfEqualRows:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "matrix, expected",
        [
            ([[0, 1], [1, 1]], 1),
            ([[0, 1], [1, 0]], 2),
            ([[0, 0, 0], [0, 0, 1], [1, 1, 0]], 2),
            ([[0]], 1),
            ([[1]], 1),
            ([[0, 0], [0, 0]], 2),
            ([[0, 1], [1, 1], [1, 0], [0, 0]], 2),
            ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 1),
            ([[0, 1, 0], [1, 0, 1], [1, 0, 1]], 3),
            ([[1, 1, 1, 1], [0, 0, 0, 0], [1, 0, 1, 0]], 2),
            ([[0, 0, 0, 0], [0, 0, 1, 1], [1, 1, 0, 0], [1, 1, 1, 1]], 2),
            ([[0], [1], [0]], 3),
            ([[0, 1, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0]], 3),
        ],
    )
    def test_max_equal_rows_after_flips(self, matrix: list[list[int]], expected: int):
        result = run_max_equal_rows_after_flips(Solution, matrix)
        assert_max_equal_rows_after_flips(result, expected)
