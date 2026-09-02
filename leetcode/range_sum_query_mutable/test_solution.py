import pytest

from leetcode_py import logged_test

from .helpers import assert_num_array, run_num_array
from .solution import NumArray


class TestRangeSumQueryMutable:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["NumArray", "sum_range", "update", "sum_range"],
                [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]],
                [None, 9, None, 8],
            ),
            (
                ["NumArray", "sum_range", "update", "sum_range"],
                [[[1]], [0, 0], [0, -100], [0, 0]],
                [None, 1, None, -100],
            ),
            (
                ["NumArray", "update", "update", "sum_range"],
                [[[5, 5, 5]], [0, 5], [1, -5], [0, 2]],
                [None, None, None, 5],
            ),
            (
                ["NumArray", "sum_range", "update", "sum_range", "update", "sum_range"],
                [[[-2, 0, 3, -5, 2, -1]], [0, 2], [1, 2], [0, 5], [2, -3], [2, 4]],
                [None, 1, None, -1, None, -6],
            ),
            (["NumArray", "update", "sum_range"], [[[7, 8, 9]], [1, 8], [0, 2]], [None, None, 24]),
            (
                ["NumArray", "sum_range", "update", "sum_range", "sum_range"],
                [[[1, 2, 3, 4]], [1, 3], [2, 10], [0, 1], [2, 3]],
                [None, 9, None, 3, 14],
            ),
            (
                ["NumArray", "sum_range", "update", "sum_range"],
                [[[-100, 100]], [0, 1], [1, -100], [0, 1]],
                [None, 0, None, -200],
            ),
            (
                ["NumArray", "sum_range", "sum_range", "sum_range"],
                [[[3, 1, 4, 1, 5]], [0, 4], [1, 3], [2, 2]],
                [None, 14, 6, 4],
            ),
            (
                ["NumArray", "update", "update", "update", "sum_range"],
                [[[1, 2, 3]], [0, -1], [1, -2], [2, -3], [0, 2]],
                [None, None, None, None, -6],
            ),
            (
                ["NumArray", "update", "update", "sum_range", "sum_range"],
                [[[0, 0, 0, 0]], [3, 4], [0, -4], [0, 3], [1, 2]],
                [None, None, None, 0, 0],
            ),
            (
                ["NumArray", "sum_range", "sum_range", "sum_range"],
                [[[9, -9, 9]], [0, 0], [1, 1], [2, 2]],
                [None, 9, -9, 9],
            ),
            (
                ["NumArray", "sum_range", "update", "update", "sum_range", "update", "sum_range"],
                [[[2, 4, 6, 8, 10]], [0, 4], [0, -2], [4, -10], [0, 4], [2, 1], [1, 3]],
                [None, 30, None, None, 6, None, 13],
            ),
            (
                ["NumArray", "update", "sum_range", "update"],
                [[[-24, 95, 77, -25, 33, 23]], [5, -1], [1, 5], [1, 72]],
                [None, None, 179, None],
            ),
            (
                ["NumArray", "update", "update"],
                [[[90, -24, -4, 81, 73]], [1, 42], [3, -58]],
                [None, None, None],
            ),
            (
                ["NumArray", "sum_range", "update"],
                [[[-84, -60, -20, 14, -10, -74]], [2, 2], [2, 94]],
                [None, -20, None],
            ),
            (
                ["NumArray", "sum_range", "sum_range", "update", "sum_range"],
                [[[52, 12, -46]], [0, 0], [0, 0], [1, 53], [2, 2]],
                [None, 52, 52, None, -46],
            ),
        ],
    )
    def test_num_array(
        self, operations: list[str], inputs: list[list[int]], expected: list[int | None]
    ):
        result, _ = run_num_array(NumArray, operations, inputs)
        assert_num_array(result, expected)
