import pytest

from leetcode_py import logged_test

from .helpers import assert_range_sum_query_2d_mutable, run_range_sum_query_2d_mutable
from .solution import NumMatrix


class TestRangeSumQuery2DMutable:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["NumMatrix", "sum_region", "update", "sum_region"],
                [
                    [
                        [
                            [3, 0, 1, 4, 2],
                            [5, 6, 3, 2, 1],
                            [1, 2, 0, 1, 5],
                            [4, 1, 0, 1, 7],
                            [1, 0, 3, 0, 5],
                        ]
                    ],
                    [2, 1, 4, 3],
                    [3, 2, 2],
                    [2, 1, 4, 3],
                ],
                [None, 8, None, 10],
            ),
            (
                ["NumMatrix", "sum_region", "update", "sum_region"],
                [[[[5]]], [0, 0, 0, 0], [0, 0, 10], [0, 0, 0, 0]],
                [None, 5, None, 10],
            ),
            (
                ["NumMatrix", "sum_region", "sum_region"],
                [[[[1, 2, 3]]], [0, 0, 0, 1], [0, 1, 0, 2]],
                [None, 3, 5],
            ),
            (["NumMatrix", "sum_region"], [[[[1], [2], [3]]], [0, 0, 2, 0]], [None, 6]),
            (
                ["NumMatrix", "sum_region", "update", "sum_region"],
                [[[[1, 2], [3, 4]]], [0, 0, 1, 1], [0, 0, 5], [0, 0, 1, 1]],
                [None, 10, None, 14],
            ),
            (["NumMatrix", "sum_region"], [[[[1, 2], [3, 4]]], [1, 1, 1, 1]], [None, 4]),
            (
                ["NumMatrix", "update", "update", "sum_region"],
                [[[[0, 0], [0, 0]]], [0, 0, 7], [0, 0, 3], [0, 0, 0, 0]],
                [None, None, None, 3],
            ),
            (["NumMatrix", "sum_region"], [[[[-1, -2], [-3, -4]]], [0, 0, 1, 1]], [None, -10]),
            (
                ["NumMatrix", "update", "sum_region", "update", "sum_region"],
                [[[[9, 9, 9], [9, 9, 9]]], [0, 1, 1], [0, 0, 0, 2], [1, 2, -9], [0, 0, 1, 2]],
                [None, None, 19, None, 28],
            ),
            (["NumMatrix", "sum_region"], [[[[0, 0], [0, 0]]], [0, 0, 1, 1]], [None, 0]),
            (
                ["NumMatrix", "update", "sum_region"],
                [[[[1, 2], [3, 4]]], [1, 1, 100], [0, 0, 0, 0]],
                [None, None, 1],
            ),
            (
                ["NumMatrix", "sum_region", "sum_region", "sum_region"],
                [[[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], [0, 0, 2, 2], [1, 1, 2, 2], [0, 2, 0, 2]],
                [None, 45, 28, 3],
            ),
            (
                ["NumMatrix", "update", "sum_region"],
                [[[[5, 5], [5, 5]]], [0, 1, -5], [0, 0, 1, 1]],
                [None, None, 10],
            ),
            (
                ["NumMatrix", "sum_region", "update", "sum_region"],
                [[[[2, 4, 6], [8, 10, 12]]], [0, 1, 1, 1], [0, 1, 0], [0, 1, 1, 1]],
                [None, 14, None, 10],
            ),
            (
                ["NumMatrix", "sum_region", "update", "sum_region"],
                [[[[1]]], [0, 0, 0, 0], [0, 0, -1], [0, 0, 0, 0]],
                [None, 1, None, -1],
            ),
        ],
    )
    def test_range_sum_query_2d_mutable(
        self, operations: list[str], inputs: list[list[list[int]]], expected: list[int | None]
    ):
        result, _ = run_range_sum_query_2d_mutable(NumMatrix, operations, inputs)
        assert_range_sum_query_2d_mutable(result, expected)
