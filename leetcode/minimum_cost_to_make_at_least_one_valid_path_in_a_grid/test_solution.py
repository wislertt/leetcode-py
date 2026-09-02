import pytest

from leetcode_py import logged_test

from .helpers import assert_min_cost, run_min_cost
from .solution import Solution


class TestMinimumCostToMakeAtLeastOneValidPathInAGrid:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]], 3),
            ([[1, 1, 3], [3, 2, 2], [1, 1, 4]], 0),
            ([[1, 2], [4, 3]], 1),
            ([[1]], 0),
            ([[2]], 0),
            ([[3]], 0),
            ([[1, 1]], 0),
            ([[4]], 0),
            ([[2, 2], [2, 2]], 2),
            ([[1, 2], [3, 4]], 1),
            ([[4, 3], [2, 1]], 1),
            ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 2),
            ([[2, 2, 2], [2, 2, 2], [2, 2, 2]], 4),
            ([[3, 4, 3], [2, 2, 2], [1, 1, 1]], 1),
            ([[4, 2, 2, 4], [2, 1, 4, 3], [2, 1, 1, 4], [4, 2, 1, 1]], 4),
            ([[2]], 0),
            ([[4], [3]], 1),
            ([[2, 3], [4, 1], [1, 4], [3, 4]], 3),
            ([[3, 2, 3]], 2),
            ([[1]], 0),
            ([[3], [4], [1], [1]], 2),
            ([[2, 1]], 1),
            ([[4, 4, 1, 2], [3, 3, 1, 3], [3, 1, 4, 1], [2, 2, 1, 1]], 3),
            ([[4, 2, 2, 4]], 3),
        ],
    )
    def test_min_cost(self, grid: list[list[int]], expected: int):
        result = run_min_cost(Solution, grid)
        assert_min_cost(result, expected)
