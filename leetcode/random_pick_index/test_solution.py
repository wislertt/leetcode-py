import pytest

from leetcode_py import logged_test

from .helpers import assert_random_pick_index, run_random_pick_index
from .solution import Solution


class TestRandomPickIndex:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (["Solution", "pick", "pick"], [[[1, 2, 3, 3, 3]], [3], [1]], [[None], [2, 3, 4], [0]]),
            (["Solution", "pick"], [[[1, 2, 3, 3, 3]], [3]], [[None], [2, 3, 4]]),
            (["Solution", "pick"], [[[1]], [1]], [[None], [0]]),
            (["Solution", "pick"], [[[7, 7, 7, 7]], [7]], [[None], [0, 1, 2, 3]]),
            (["Solution", "pick"], [[[5, 5]], [5]], [[None], [0, 1]]),
            (["Solution", "pick", "pick"], [[[3, 1, 3]], [3], [1]], [[None], [0, 2], [1]]),
            (["Solution", "pick", "pick"], [[[4, 9, 4, 9]], [9], [4]], [[None], [1, 3], [0, 2]]),
            (["Solution", "pick", "pick"], [[[-1, -1, 2]], [-1], [2]], [[None], [0, 1], [2]]),
            (["Solution", "pick"], [[[2147483647, 2147483647, 0]], [2147483647]], [[None], [0, 1]]),
            (["Solution", "pick"], [[[-2147483648, -2147483648]], [-2147483648]], [[None], [0, 1]]),
            (
                ["Solution", "pick", "pick"],
                [[[10, 20, 10, 20]], [10], [20]],
                [[None], [0, 2], [1, 3]],
            ),
            (
                ["Solution", "pick", "pick"],
                [[[1, 1, 2, 2, 3, 3]], [1], [3]],
                [[None], [0, 1], [4, 5]],
            ),
            (["Solution", "pick"], [[[6, 6, 6, 6, 6, 6]], [6]], [[None], [0, 1, 2, 3, 4, 5]]),
            (["Solution", "pick"], [[[1, 1, 2, 2, 3, 3, 3]], [3]], [[None], [4, 5, 6]]),
            (["Solution", "pick"], [[[42]], [42]], [[None], [0]]),
        ],
    )
    def test_pick(
        self, operations: list[str], inputs: list[list[int]], expected: list[list[int | None]]
    ):
        result = run_random_pick_index(Solution, operations, inputs)
        assert_random_pick_index(result, expected)
