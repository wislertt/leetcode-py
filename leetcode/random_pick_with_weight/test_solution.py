import pytest

from leetcode_py import logged_test

from .helpers import assert_random_pick_operations, run_random_pick_operations
from .solution import Solution


class TestTestRandomPickWithWeight:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (["Solution", "pickIndex"], [[[1]], []], [None, 0]),
            (["Solution", "pickIndex"], [[[5]], []], [None, 0]),
            (["Solution", "pickIndex", "pickIndex"], [[[100]], [], []], [None, 0, 0]),
            (
                ["Solution", "pickIndex", "pickIndex", "pickIndex"],
                [[[1]], [], [], []],
                [None, 0, 0, 0],
            ),
            (["Solution", "pickIndex"], [[[100000]], []], [None, 0]),
            (["Solution", "pickIndex"], [[[7]], []], [None, 0]),
            (["Solution", "pickIndex", "pickIndex"], [[[2]], [], []], [None, 0, 0]),
            (["Solution", "pickIndex"], [[[42]], []], [None, 0]),
            (["Solution", "pickIndex"], [[[99999]], []], [None, 0]),
            (["Solution", "pickIndex"], [[[3]], []], [None, 0]),
            (
                ["Solution", "pickIndex", "pickIndex", "pickIndex", "pickIndex", "pickIndex"],
                [[[1]], [], [], [], [], []],
                [None, 0, 0, 0, 0, 0],
            ),
            (["Solution", "pickIndex"], [[[10]], []], [None, 0]),
            (["Solution", "pickIndex"], [[[256]], []], [None, 0]),
            (["Solution", "pickIndex", "pickIndex"], [[[1]], [], []], [None, 0, 0]),
            (["Solution", "pickIndex"], [[[13]], []], [None, 0]),
        ],
    )
    def test_random_pick(
        self, operations: list[str], inputs: list[list[int]], expected: list[int | None]
    ):
        result = run_random_pick_operations(Solution, operations, inputs)
        assert_random_pick_operations(result, expected)
