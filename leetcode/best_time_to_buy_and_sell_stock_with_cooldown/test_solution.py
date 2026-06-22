import pytest

from leetcode_py import logged_test

from .helpers import assert_max_profit, run_max_profit
from .solution import Solution


class TestBestTimeToBuyAndSellStockWithCooldown:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "prices, expected",
        [
            ([1, 2, 3, 0, 2], 3),
            ([1], 0),
            ([1, 2], 1),
            ([3, 2, 1], 0),
            ([1, 2, 3], 2),
            ([1, 2, 4], 3),
            ([2, 4, 1], 2),
            ([1, 4, 2], 3),
            ([1, 2, 3, 0, 2, 5], 6),
            ([6, 1, 6, 4, 2, 0, 1], 6),
            ([5], 0),
            ([1, 2, 3, 4, 5], 4),
            ([1, 3, 1, 4], 3),
            ([2, 1], 0),
        ],
    )
    def test_max_profit(self, prices: list[int], expected: int):
        result = run_max_profit(Solution, prices)
        assert_max_profit(result, expected)
