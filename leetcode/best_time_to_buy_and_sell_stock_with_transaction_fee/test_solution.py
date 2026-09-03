import pytest

from leetcode_py import logged_test

from .helpers import assert_max_profit, run_max_profit
from .solution import Solution


class TestBestTimeToBuyAndSellStockWithTransactionFee:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "prices, fee, expected",
        [
            ([1, 3, 2, 8, 4, 9], 2, 8),
            ([1, 3, 7, 5, 10, 3], 3, 6),
            ([1], 2, 0),
            ([5], 0, 0),
            ([1, 2], 0, 1),
            ([2, 1], 1, 0),
            ([1, 2, 3, 4, 5], 1, 3),
            ([5, 4, 3, 2, 1], 2, 0),
            ([3, 3, 3, 3], 2, 0),
            ([1, 9, 1, 9], 2, 12),
            ([2, 7, 1, 8], 5, 2),
            ([1, 4, 2, 8], 3, 4),
            ([9, 1, 9, 1, 9], 2, 12),
            ([6, 1, 6, 4, 2, 3, 1], 2, 3),
            ([1, 3, 2, 8, 4, 9], 0, 13),
            ([1, 3, 7, 5, 10, 3], 100, 0),
            ([4, 3, 11, 4, 10, 14, 3], 5, 8),
            ([2, 8, 6, 5, 18, 14, 7], 5, 11),
            ([2, 4], 0, 2),
            ([4, 13, 4], 1, 8),
        ],
    )
    def test_max_profit(self, prices: list[int], fee: int, expected: int):
        result = run_max_profit(Solution, prices, fee)
        assert_max_profit(result, expected)
