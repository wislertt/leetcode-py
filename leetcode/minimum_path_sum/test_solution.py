import pytest

from leetcode_py import logged_test

from .helpers import assert_min_path_sum, run_min_path_sum
from .solution import Solution


class TestMinimumPathSum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),
            ([[1, 2, 3], [4, 5, 6]], 12),
            ([[1, 1], [1, 1]], 3),
            ([[1]], 1),
            ([[1, 2], [1, 1]], 3),
            ([[1, 2, 5], [3, 2, 1]], 6),
            ([[5, 1, 1], [1, 5, 1], [1, 1, 5]], 13),
            ([[0, 0], [0, 0]], 0),
            ([[1, 3, 5, 9], [8, 1, 3, 4], [5, 0, 6, 1], [8, 8, 4, 0]], 12),
            ([[1, 2], [5, 6], [1, 1]], 8),
            ([[2]], 2),
            ([[1, 4, 7], [2, 5, 8], [3, 6, 9]], 21),
            ([[10, 20], [30, 40]], 70),
            ([[1, 0], [0, 1]], 2),
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 21),
            ([[100]], 100),
            ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 5),
            ([[1, 2], [3, 4]], 7),
            ([[9, 1, 4, 8]], 22),
        ],
    )
    def test_min_path_sum(self, grid: list[list[int]], expected: int):
        result = run_min_path_sum(Solution, grid)
        assert_min_path_sum(result, expected)
