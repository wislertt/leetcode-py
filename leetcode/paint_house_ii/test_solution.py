import pytest

from leetcode_py import logged_test

from .helpers import assert_min_cost_ii, run_min_cost_ii
from .solution import Solution


class TestPaintHouseII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "costs, expected",
        [
            ([[1, 5, 3], [2, 9, 4]], 5),
            ([[1, 3], [2, 4]], 5),
            ([[1, 5, 3], [2, 9, 4], [8, 1, 7]], 6),
            ([[7, 2], [3, 9], [1, 5]], 10),
            ([[1, 2, 3, 4]], 1),
            ([[4, 3, 2, 1], [1, 2, 3, 4]], 2),
            ([[1, 1, 1], [1, 1, 1]], 2),
            ([[10, 1, 10], [1, 10, 10], [10, 10, 1]], 3),
            ([[3, 5, 7, 9], [6, 4, 2, 8], [9, 3, 5, 7]], 8),
            ([[1, 4], [2, 3], [4, 1], [3, 2]], 10),
            ([[5, 1, 6, 2, 7], [8, 3, 4, 9, 1], [2, 7, 5, 1, 8]], 3),
            ([[2, 2, 2, 2], [2, 2, 2, 2]], 4),
        ],
    )
    def test_min_cost_ii(self, costs: list[list[int]], expected: int):
        result = run_min_cost_ii(Solution, costs)
        assert_min_cost_ii(result, expected)
