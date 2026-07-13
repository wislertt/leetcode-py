import pytest

from leetcode_py import logged_test

from .helpers import assert_max_profit, run_max_profit
from .solution import Solution


class TestTestBestTimeToBuyAndSellStockII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "solution_class, prices, expected",
        [
            (Solution, [7, 1, 5, 3, 6, 4], 7),
            (Solution, [1, 2, 3, 4, 5], 4),
            (Solution, [7, 6, 4, 3, 1], 0),
            (Solution, [5], 0),
            (Solution, [1, 2], 1),
            (Solution, [2, 1], 0),
            (Solution, [1, 2, 3], 2),
            (Solution, [3, 2, 1, 2, 3], 2),
            (Solution, [1, 4, 2], 3),
            (Solution, [2, 4, 1], 2),
            (Solution, [1, 2, 1, 2, 1, 2], 3),
            (Solution, [5, 4, 3, 2, 1, 2, 3, 4, 5], 4),
            (Solution, [3, 3, 3, 3], 0),
            (Solution, [0, 5], 5),
            (Solution, [1, 9, 1, 9, 1, 9], 24),
            (Solution, [9, 1, 9, 1, 9], 16),
            (Solution, [2, 1, 4], 3),
            (Solution, [1, 2, 4, 2, 5, 7, 2, 4, 9, 0], 15),
        ],
    )
    def test_max_profit(self, solution_class, prices: list[int], expected: int):
        result = run_max_profit(solution_class, prices)
        assert_max_profit(result, expected)
