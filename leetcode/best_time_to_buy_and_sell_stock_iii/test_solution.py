import pytest

from leetcode_py import logged_test

from .helpers import assert_max_profit, run_max_profit
from .solution import Solution


class TestTestBestTimeToBuyAndSellStockIII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "solution_class, prices, expected",
        [
            (Solution, [3, 3, 5, 0, 0, 3, 1, 4], 6),
            (Solution, [1, 2, 3, 4, 5], 4),
            (Solution, [7, 6, 4, 3, 1], 0),
            (Solution, [1], 0),
            (Solution, [5, 4, 3, 2, 1], 0),
            (Solution, [1, 2], 1),
            (Solution, [2, 1], 0),
            (Solution, [1, 2, 3, 4], 3),
            (Solution, [1, 5, 2, 6], 8),
            (Solution, [1, 2, 4, 2, 5, 7, 2, 4, 9, 0], 13),
            (Solution, [3, 3, 5, 0, 0, 3, 1, 4], 6),
            (Solution, [6, 1, 3, 2, 4, 7], 7),
            (Solution, [0, 0, 0], 0),
            (Solution, [2, 1, 2, 0, 1], 2),
            (Solution, [8, 6, 4, 3, 3, 2, 3, 5, 8, 3, 8, 2, 6], 11),
            (Solution, [14, 60, 88, 87, 34, 88, 72, 44, 10, 55], 128),
            (Solution, [70, 4, 83, 56, 90, 61, 23, 28, 3, 18], 113),
            (Solution, [7], 0),
            (Solution, [4, 1, 1, 3, 1, 5, 8, 4, 9], 12),
            (Solution, [8, 3, 3, 3], 0),
            (Solution, [1, 1, 3, 8, 3], 7),
            (Solution, [7, 6, 9, 1, 0, 9, 8, 3, 8], 14),
            (Solution, [2], 0),
        ],
    )
    def test_max_profit(self, solution_class, prices: list[int], expected: int):
        result = run_max_profit(solution_class, prices)
        assert_max_profit(result, expected)
