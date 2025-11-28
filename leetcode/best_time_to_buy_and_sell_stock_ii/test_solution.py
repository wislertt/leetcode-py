from typing import List

import pytest

from leetcode_py import logged_test

from .helpers import assert_max_profit, run_max_profit
from .solution import Solution


class TestBestTimeToBuyAndSellStockIi:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize("prices, expected", [])
    def test_max_profit(self, prices: List[int], expected: int):
        result = run_max_profit(Solution, prices)
        assert_max_profit(result, expected)
