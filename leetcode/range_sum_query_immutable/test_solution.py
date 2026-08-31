from typing import Any

import pytest

from leetcode_py import logged_test

from .helpers import assert_range_sum_query_immutable, run_range_sum_query_immutable
from .solution import NumArray


class TestRangeSumQueryImmutable:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["NumArray", "sumRange", "sumRange", "sumRange"],
                [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]],
                [None, 1, -1, -3],
            ),
            (
                ["NumArray", "sumRange", "sumRange", "sumRange", "sumRange", "sumRange"],
                [[[1, 2, 3, 4, 5]], [0, 4], [1, 3], [2, 2], [0, 0], [4, 4]],
                [None, 15, 9, 3, 1, 5],
            ),
            (["NumArray", "sumRange"], [[[7]], [0, 0]], [None, 7]),
            (
                ["NumArray", "sumRange", "sumRange", "sumRange", "sumRange"],
                [[[-1, -2, -3, -4]], [0, 3], [1, 2], [0, 1], [3, 3]],
                [None, -10, -5, -3, -4],
            ),
            (["NumArray", "sumRange", "sumRange"], [[[0, 0, 0]], [0, 2], [1, 1]], [None, 0, 0]),
            (
                ["NumArray", "sumRange", "sumRange", "sumRange"],
                [[[100000, -100000, 100000]], [0, 2], [0, 1], [1, 2]],
                [None, 100000, 0, 0],
            ),
            (
                ["NumArray", "sumRange", "sumRange", "sumRange", "sumRange"],
                [[[5, 5, 5, 5]], [0, 3], [1, 3], [0, 1], [2, 3]],
                [None, 20, 15, 10, 10],
            ),
            (
                ["NumArray", "sumRange", "sumRange", "sumRange", "sumRange", "sumRange"],
                [[[1, -1, 1, -1, 1, -1]], [0, 5], [1, 4], [0, 3], [2, 5], [3, 3]],
                [None, 0, 0, 0, 0, -1],
            ),
            (
                ["NumArray", "sumRange", "sumRange", "sumRange", "sumRange"],
                [[[9, 8, 7, 6, 5, 4, 3, 2, 1]], [0, 8], [4, 8], [0, 4], [2, 6]],
                [None, 45, 15, 35, 25],
            ),
            (
                ["NumArray", "sumRange", "sumRange", "sumRange", "sumRange", "sumRange"],
                [[[-5, 10, -15, 20, -25]], [0, 4], [1, 3], [2, 2], [0, 2], [3, 4]],
                [None, -15, 15, -15, -10, -5],
            ),
            (
                ["NumArray", "sumRange", "sumRange", "sumRange", "sumRange"],
                [[[2, 4, 6, 8, 10]], [0, 0], [0, 2], [3, 4], [1, 4]],
                [None, 2, 12, 18, 28],
            ),
            (
                ["NumArray", "sumRange", "sumRange", "sumRange"],
                [[[3]], [0, 0], [0, 0], [0, 0]],
                [None, 3, 3, 3],
            ),
        ],
    )
    def test_range_sum_query_immutable(
        self, operations: list[str], inputs: list[list[Any]], expected: list[Any]
    ):
        result = run_range_sum_query_immutable(NumArray, operations, inputs)
        assert_range_sum_query_immutable(result, expected)
