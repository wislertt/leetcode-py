import pytest

from leetcode_py import logged_test

from .helpers import assert_shuffle_operations, run_shuffle_operations
from .solution import Solution


class TestShuffleAnArray:
    @logged_test
    @pytest.mark.parametrize(
        "nums, operations, expected",
        [
            ([1, 2], ["Solution", "shuffle", "reset", "shuffle"], [None, [1, 2], None]),
            ([5], ["Solution", "shuffle", "reset", "shuffle"], [[5], [5], [5]]),
            ([7], ["Solution", "reset"], [[7]]),
            ([7], ["Solution", "shuffle"], [[7]]),
            ([1, 2, 3], ["Solution", "reset"], [[1, 2, 3]]),
            ([-1, 0, 1], ["Solution", "reset", "reset"], [[-1, 0, 1], [-1, 0, 1]]),
            ([4, 5, 6], ["Solution", "shuffle"], [None]),
            ([10, 20, 30], ["Solution", "shuffle", "shuffle"], [None, None]),
            ([2, 4, 6], ["Solution", "shuffle", "reset"], [None, [2, 4, 6]]),
            ([3, 1, 2], ["Solution", "shuffle", "reset"], [None, [3, 1, 2]]),
            ([-3, 0, 7], ["Solution", "reset", "shuffle"], [[-3, 0, 7], None]),
            ([1, 2, 3, 4], ["Solution", "shuffle", "reset"], [None, [1, 2, 3, 4]]),
            ([9, 8, 7], ["Solution", "shuffle", "reset"], [None, [9, 8, 7]]),
            ([-5, 5], ["Solution", "shuffle", "reset"], [None, [-5, 5]]),
            ([-99999, 99999], ["Solution", "shuffle", "reset"], [None, [-99999, 99999]]),
            ([0, -2, 8], ["Solution", "reset", "shuffle"], [[0, -2, 8], None]),
        ],
    )
    def test_shuffle_operations(
        self, nums: list[int], operations: list[str], expected: list[list[int] | None]
    ):
        result, _ = run_shuffle_operations(Solution, nums, operations)
        assert_shuffle_operations(result, expected, nums)
