import pytest

from leetcode_py import logged_test

from .helpers import assert_min_cost, run_min_cost
from .solution import Solution


class TestPaintHouse:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "costs, expected",
        [
            ([[17, 2, 17], [16, 16, 5], [14, 3, 19]], 10),
            ([[7, 6, 2]], 2),
            ([[1, 2, 3]], 1),
            ([[1, 2, 2], [2, 1, 2]], 2),
            ([[1, 2, 2], [1, 2, 2], [2, 1, 3]], 4),
            ([[5, 5, 5]], 5),
            ([[10, 4, 2], [3, 9, 6], [7, 8, 1], [12, 3, 9]], 9),
            ([[1, 100, 100], [100, 1, 100], [100, 100, 1]], 3),
            ([[14, 3, 19], [16, 16, 5], [17, 2, 17], [12, 10, 11]], 21),
            ([[20, 18, 19], [1, 2, 3], [10, 20, 30], [5, 5, 5], [9, 1, 20]], 37),
            ([[2, 1, 3], [1, 2, 3], [3, 1, 2]], 3),
            ([[3, 5, 7], [8, 5, 2], [9, 1, 6], [4, 7, 3], [2, 8, 9]], 11),
        ],
    )
    def test_min_cost(self, costs: list[list[int]], expected: int):
        result = run_min_cost(Solution, costs)
        assert_min_cost(result, expected)
