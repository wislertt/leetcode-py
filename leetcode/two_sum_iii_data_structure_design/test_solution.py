import pytest

from leetcode_py import logged_test

from .helpers import assert_two_sum, run_two_sum
from .solution import TwoSum


class TestTwoSumIIIDataStructureDesign:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (["TwoSum", "add", "find"], [[], [1], [2]], [None, None, False]),
            (["TwoSum", "add", "add", "find"], [[], [1], [3], [4]], [None, None, None, True]),
            (["TwoSum", "add", "add", "find"], [[], [1], [1], [2]], [None, None, None, True]),
            (["TwoSum", "add", "add", "find"], [[], [1], [1], [3]], [None, None, None, False]),
            (["TwoSum", "find"], [[], [5]], [None, False]),
            (["TwoSum", "add", "add", "find"], [[], [0], [0], [0]], [None, None, None, True]),
            (["TwoSum", "add", "find"], [[], [0], [0]], [None, None, False]),
            (["TwoSum", "add", "add", "find"], [[], [-1], [2], [1]], [None, None, None, True]),
            (["TwoSum", "add", "add", "find"], [[], [-1], [2], [0]], [None, None, None, False]),
            (
                ["TwoSum", "add", "add", "find"],
                [[], [100000], [100000], [200000]],
                [None, None, None, True],
            ),
            (
                ["TwoSum", "add", "add", "find"],
                [[], [-100000], [100000], [0]],
                [None, None, None, True],
            ),
            (["TwoSum", "add", "find", "add"], [[], [3], [6], [3]], [None, None, False, None]),
            (["TwoSum", "add", "find", "find"], [[], [3], [6], [7]], [None, None, False, False]),
            (
                ["TwoSum", "add", "add", "add", "find"],
                [[], [1], [2], [3], [5]],
                [None, None, None, None, True],
            ),
            (["TwoSum", "add", "add", "find"], [[], [1], [3], [7]], [None, None, None, False]),
            (["TwoSum", "add", "add", "find"], [[], [-5], [-5], [-10]], [None, None, None, True]),
            (["TwoSum", "add", "add", "find"], [[], [5], [5], [10]], [None, None, None, True]),
        ],
    )
    def test_two_sum(
        self, operations: list[str], inputs: list[list[int]], expected: list[bool | None]
    ):
        result, _ = run_two_sum(TwoSum, operations, inputs)
        assert_two_sum(result, expected)
