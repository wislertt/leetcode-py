import pytest

from leetcode_py import logged_test

from .helpers import assert_map_sum, run_map_sum
from .solution import MapSum


class TestMapSumPairs:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["MapSum", "insert", "sum", "insert", "sum"],
                [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]],
                [None, None, 3, None, 5],
            ),
            (["MapSum", "insert", "sum"], [[], ["a", 3], ["a"]], [None, None, 3]),
            (
                ["MapSum", "insert", "sum", "sum"],
                [[], ["app", 1], ["ap"], ["apple"]],
                [None, None, 1, 0],
            ),
            (
                ["MapSum", "insert", "insert", "sum", "sum"],
                [[], ["apple", 3], ["apple", 2], ["apple"], ["ap"]],
                [None, None, None, 2, 2],
            ),
            (["MapSum", "sum"], [[], ["a"]], [None, 0]),
            (
                ["MapSum", "insert", "insert", "insert", "sum", "sum", "sum"],
                [[], ["a", 1], ["ab", 2], ["abc", 3], ["a"], ["ab"], ["abc"]],
                [None, None, None, None, 6, 5, 3],
            ),
            (
                ["MapSum", "insert", "insert", "sum", "sum", "sum"],
                [[], ["ap", 4], ["apple", 5], ["ap"], ["appl"], ["applex"]],
                [None, None, None, 9, 5, 0],
            ),
            (
                ["MapSum", "insert", "insert", "sum", "sum", "sum"],
                [[], ["cat", 1], ["dog", 2], ["c"], ["d"], ["e"]],
                [None, None, None, 1, 2, 0],
            ),
            (
                ["MapSum", "insert", "insert", "sum", "sum", "sum"],
                [[], ["abc", 1], ["abd", 2], ["ab"], ["abc"], ["a"]],
                [None, None, None, 3, 1, 3],
            ),
            (
                ["MapSum", "insert", "insert", "sum", "insert", "sum"],
                [[], ["app", 1], ["apple", 10], ["ap"], ["apple", 1], ["ap"]],
                [None, None, None, 11, None, 2],
            ),
            (
                ["MapSum", "insert", "sum", "sum", "sum"],
                [[], ["aaaaaaaaaa", 1000], ["a"], ["aaaaaaaaab"], ["aaaaaaaaaaa"]],
                [None, None, 1000, 0, 0],
            ),
            (
                ["MapSum", "insert", "insert", "insert", "sum", "sum"],
                [[], ["te", 5], ["tea", 6], ["ten", 7], ["te"], ["ten"]],
                [None, None, None, None, 18, 7],
            ),
            (
                ["MapSum", "insert", "insert", "insert", "sum", "insert", "sum"],
                [[], ["ba", 2], ["bat", 3], ["bar", 4], ["ba"], ["bat", 9], ["ba"]],
                [None, None, None, None, 9, None, 15],
            ),
            (
                ["MapSum", "insert", "sum", "sum", "insert", "sum", "sum"],
                [[], ["k", 1000], ["k"], ["kk"], ["kk", 1000], ["k"], ["z"]],
                [None, None, 1000, 0, None, 2000, 0],
            ),
        ],
    )
    def test_map_sum(self, operations: list[str], inputs: list[list], expected: list[int | None]):
        result, _ = run_map_sum(MapSum, operations, inputs)
        assert_map_sum(result, expected)
