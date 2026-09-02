import pytest

from leetcode_py import logged_test

from .helpers import assert_max_profit, run_max_profit
from .solution import Solution


class TestTestBestTimeToBuyAndSellStockIV:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "solution_class, k, prices, expected",
        [
            (Solution, 2, [2, 4, 1], 2),
            (Solution, 2, [3, 2, 6, 5, 0, 3], 7),
            (Solution, 1, [1], 0),
            (Solution, 100, [1, 2, 3, 4, 5], 4),
            (Solution, 1, [7, 6, 4, 3, 1], 0),
            (Solution, 2, [1, 2, 3, 4, 5], 4),
            (Solution, 1, [3, 3, 5, 0, 0, 3, 1, 4], 4),
            (Solution, 2, [3, 3, 5, 0, 0, 3, 1, 4], 6),
            (Solution, 1, [1, 2], 1),
            (Solution, 2, [2, 1], 0),
            (Solution, 3, [1, 5, 2, 6, 0, 1, 7], 15),
            (Solution, 2, [0, 0, 0], 0),
            (Solution, 3, [8, 0, 7, 2], 7),
            (Solution, 4, [8, 11, 9, 8, 3, 3, 0], 3),
            (Solution, 4, [11, 3, 7, 8, 1, 10, 12, 6], 16),
            (Solution, 2, [6, 1], 0),
            (Solution, 1, [6, 10, 10, 18, 8, 9, 3, 18, 7], 15),
            (Solution, 1, [15, 8, 7, 12, 16, 20, 5, 7, 8], 13),
            (Solution, 1, [13, 5, 13, 19, 1, 15, 20, 10], 19),
            (Solution, 1, [8, 5, 0, 20, 17, 2, 3], 20),
            (Solution, 4, [13, 12], 0),
            (Solution, 2, [10, 17, 15, 2], 7),
            (Solution, 4, [17, 16, 19, 20, 16, 12], 4),
            (Solution, 1, [16, 2, 6, 11, 6, 14], 12),
        ],
    )
    def test_max_profit(self, solution_class, k: int, prices: list[int], expected: int):
        result = run_max_profit(solution_class, k, prices)
        assert_max_profit(result, expected)
