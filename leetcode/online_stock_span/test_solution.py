import pytest

from leetcode_py import logged_test

from .helpers import assert_online_stock_span_operations, run_online_stock_span_operations
from .solution import StockSpanner


class TestTestOnlineStockSpan:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"],
                [[], [100], [80], [60], [70], [60], [75], [85]],
                [None, 1, 1, 1, 2, 1, 4, 6],
            ),
            (["StockSpanner", "next", "next", "next"], [[], [1], [2], [3]], [None, 1, 2, 3]),
            (["StockSpanner", "next", "next", "next"], [[], [3], [2], [1]], [None, 1, 1, 1]),
            (["StockSpanner", "next"], [[], [50]], [None, 1]),
            (
                ["StockSpanner", "next", "next", "next", "next", "next"],
                [[], [10], [10], [10], [10], [10]],
                [None, 1, 2, 3, 4, 5],
            ),
            (
                ["StockSpanner", "next", "next", "next", "next"],
                [[], [5], [3], [8], [2]],
                [None, 1, 1, 3, 1],
            ),
            (
                ["StockSpanner", "next", "next", "next", "next", "next"],
                [[], [31], [41], [48], [59], [79]],
                [None, 1, 2, 3, 4, 5],
            ),
            (
                ["StockSpanner", "next", "next", "next", "next", "next", "next"],
                [[], [100], [80], [60], [70], [60], [75]],
                [None, 1, 1, 1, 2, 1, 4],
            ),
            (
                ["StockSpanner", "next", "next", "next", "next"],
                [[], [29], [91], [62], [82]],
                [None, 1, 2, 1, 2],
            ),
            (
                ["StockSpanner", "next", "next", "next", "next", "next", "next", "next", "next"],
                [[], [1], [2], [3], [4], [5], [6], [7], [8]],
                [None, 1, 2, 3, 4, 5, 6, 7, 8],
            ),
            (
                ["StockSpanner", "next", "next", "next", "next", "next", "next"],
                [[], [8], [7], [6], [5], [4], [9]],
                [None, 1, 1, 1, 1, 1, 6],
            ),
            (
                [
                    "StockSpanner",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                ],
                [[], [5], [4], [3], [2], [1], [2], [3], [4], [5]],
                [None, 1, 1, 1, 1, 1, 3, 5, 7, 9],
            ),
            (
                ["StockSpanner", "next", "next", "next", "next", "next", "next"],
                [[], [120], [110], [100], [90], [80], [200]],
                [None, 1, 1, 1, 1, 1, 6],
            ),
            (
                ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"],
                [[], [7], [2], [1], [2], [8], [1], [2]],
                [None, 1, 1, 1, 3, 5, 1, 2],
            ),
            (
                ["StockSpanner", "next", "next", "next", "next"],
                [[], [25], [25], [25], [25]],
                [None, 1, 2, 3, 4],
            ),
            (
                ["StockSpanner", "next", "next", "next", "next", "next", "next"],
                [[], [9], [8], [7], [6], [5], [10]],
                [None, 1, 1, 1, 1, 1, 6],
            ),
            (
                ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"],
                [[], [3], [5], [2], [7], [1], [4], [6]],
                [None, 1, 2, 1, 4, 1, 2, 3],
            ),
            (
                ["StockSpanner", "next", "next", "next", "next", "next", "next", "next", "next"],
                [[], [15], [14], [13], [12], [16], [11], [10], [20]],
                [None, 1, 1, 1, 1, 5, 1, 1, 8],
            ),
        ],
    )
    def test_online_stock_span(
        self, operations: list[str], inputs: list[list[int]], expected: list[int | None]
    ):
        result = run_online_stock_span_operations(StockSpanner, operations, inputs)
        assert_online_stock_span_operations(result, expected)
