import pytest

from leetcode_py import logged_test

from .helpers import assert_randomized_set_operations, run_randomized_set_operations
from .solution import RandomizedSet


class TestTestInsertDeleteGetRandomO1:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (["RandomizedSet", "insert", "getRandom"], [[], [5], []], [None, True, 5]),
            (
                ["RandomizedSet", "insert", "insert", "remove", "getRandom"],
                [[], [1], [2], [1], []],
                [None, True, True, True, 2],
            ),
            (
                ["RandomizedSet", "insert", "insert", "insert", "remove", "remove", "getRandom"],
                [[], [1], [2], [3], [1], [2], []],
                [None, True, True, True, True, True, 3],
            ),
            (
                ["RandomizedSet", "insert", "insert", "getRandom"],
                [[], [7], [7], []],
                [None, True, False, 7],
            ),
            (
                ["RandomizedSet", "remove", "insert", "getRandom"],
                [[], [9], [9], []],
                [None, False, True, 9],
            ),
            (
                ["RandomizedSet", "insert", "remove", "insert", "getRandom"],
                [[], [4], [4], [4], []],
                [None, True, True, True, 4],
            ),
            (
                [
                    "RandomizedSet",
                    "insert",
                    "insert",
                    "insert",
                    "insert",
                    "remove",
                    "remove",
                    "remove",
                    "getRandom",
                ],
                [[], [10], [20], [30], [40], [10], [20], [30], []],
                [None, True, True, True, True, True, True, True, 40],
            ),
            (
                ["RandomizedSet", "insert", "remove", "insert", "remove", "insert", "getRandom"],
                [[], [1], [1], [2], [2], [3], []],
                [None, True, True, True, True, True, 3],
            ),
            (["RandomizedSet", "insert", "getRandom"], [[], [-5], []], [None, True, -5]),
            (
                ["RandomizedSet", "insert", "insert", "remove", "remove", "insert", "getRandom"],
                [[], [1], [2], [1], [2], [8], []],
                [None, True, True, True, True, True, 8],
            ),
            (
                ["RandomizedSet", "insert", "getRandom"],
                [[], [2147483647], []],
                [None, True, 2147483647],
            ),
            (
                ["RandomizedSet", "insert", "insert", "insert", "remove", "remove", "getRandom"],
                [[], [100], [200], [300], [200], [300], []],
                [None, True, True, True, True, True, 100],
            ),
            (
                ["RandomizedSet", "insert", "insert", "remove", "insert", "remove", "getRandom"],
                [[], [3], [5], [3], [6], [5], []],
                [None, True, True, True, True, True, 6],
            ),
            (
                [
                    "RandomizedSet",
                    "insert",
                    "insert",
                    "insert",
                    "remove",
                    "remove",
                    "remove",
                    "insert",
                    "getRandom",
                ],
                [[], [1], [2], [3], [1], [2], [3], [9], []],
                [None, True, True, True, True, True, True, True, 9],
            ),
            (
                ["RandomizedSet", "insert", "remove", "remove", "insert", "getRandom"],
                [[], [2], [2], [5], [5], []],
                [None, True, True, False, True, 5],
            ),
        ],
    )
    def test_randomized_set(
        self, operations: list[str], inputs: list[list[int]], expected: list[int | None]
    ):
        result = run_randomized_set_operations(RandomizedSet, operations, inputs)
        assert_randomized_set_operations(result, expected)
