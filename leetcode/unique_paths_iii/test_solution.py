import pytest

from leetcode_py import logged_test

from .helpers import assert_unique_paths_iii, run_unique_paths_iii
from .solution import Solution


class TestTestUniquePathsIII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]], 2),
            ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]], 4),
            ([[0, 1], [2, 0]], 0),
            ([[1, 2]], 1),
            ([[2, 1]], 1),
            ([[1, -1, 2]], 0),
            ([[1, 0, 2, 0]], 0),
            ([[1, 0, 0, 0, 2]], 1),
            ([[1, 0], [0, 2]], 0),
            ([[2, -1], [0, 1]], 1),
            ([[1, 0, 0], [0, 0, 2]], 1),
            ([[1, 0, 0, 0], [0, -1, -1, 0], [0, -1, -1, 0], [0, 0, 0, 2]], 0),
            ([[0, 2], [1, 0]], 0),
            ([[1, 0, 0], [-1, 0, 0], [0, 0, 2]], 0),
            ([[0, 1, 0], [0, 0, 2]], 0),
            ([[0, 2], [1, -1], [-1, 0]], 0),
            ([[0, 2, 1], [0, 0, 0]], 1),
            ([[-1], [1], [2]], 1),
            ([[1], [2]], 1),
            ([[-1, -1], [0, 2], [1, 0]], 0),
            ([[2, 0, 0, 0], [0, 0, 0, 1]], 0),
            ([[0, 0, 0, -1], [1, 2, 0, -1]], 1),
        ],
    )
    def test_unique_paths_iii(self, grid: list[list[int]], expected: int):
        result = run_unique_paths_iii(Solution, grid)
        assert_unique_paths_iii(result, expected)
