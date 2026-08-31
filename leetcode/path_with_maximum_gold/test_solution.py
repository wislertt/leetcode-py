import pytest

from leetcode_py import logged_test

from .helpers import assert_get_maximum_gold, run_get_maximum_gold
from .solution import Solution


class TestPathWithMaximumGoldTest:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[0, 6, 0], [5, 8, 7], [0, 9, 0]], 24),
            ([[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]], 28),
            ([[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [2, 0, 9]], 28),
            ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0),
            ([[5]], 5),
            ([[0]], 0),
            ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 9),
            ([[1, 0, 1], [0, 0, 0], [1, 0, 1]], 1),
            ([[10, 20], [30, 40]], 100),
            ([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], 55),
            ([[25, 25], [25, 25]], 100),
            ([[1, 0], [0, 1]], 1),
            ([[5, 5], [5, 0], [5, 5]], 25),
            ([[0, 5, 5], [5, 0, 5], [5, 5, 0]], 15),
            ([[100, 0, 0], [0, 0, 0], [0, 0, 100]], 100),
            ([[3, 4], [7, 0], [0, 8]], 14),
        ],
    )
    def test_get_maximum_gold(self, grid: list[list[int]], expected: int):
        result = run_get_maximum_gold(Solution, grid)
        assert_get_maximum_gold(result, expected)
