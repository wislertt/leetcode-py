import pytest

from leetcode_py import logged_test

from .helpers import assert_randomized_collection_operations, run_randomized_collection_operations
from .solution import RandomizedCollection


class TestInsertDeleteGetRandomO1DuplicatesAllowed:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["RandomizedCollection", "insert", "insert", "insert", "getRandom"],
                [[], [1], [1], [1], []],
                [None, True, False, False, 1],
            ),
            (
                ["RandomizedCollection", "insert", "insert", "remove", "getRandom"],
                [[], [1], [1], [1], []],
                [None, True, False, True, 1],
            ),
            (
                ["RandomizedCollection", "insert", "insert", "remove", "getRandom"],
                [[], [5], [5], [5], []],
                [None, True, False, True, 5],
            ),
            (
                ["RandomizedCollection", "insert", "insert", "insert", "remove", "getRandom"],
                [[], [1], [2], [1], [2], []],
                [None, True, True, False, True, 1],
            ),
            (
                [
                    "RandomizedCollection",
                    "insert",
                    "insert",
                    "insert",
                    "remove",
                    "remove",
                    "getRandom",
                ],
                [[], [3], [3], [3], [3], [3], []],
                [None, True, False, False, True, True, 3],
            ),
            (
                ["RandomizedCollection", "remove", "insert", "getRandom"],
                [[], [9], [9], []],
                [None, False, True, 9],
            ),
            (
                ["RandomizedCollection", "insert", "remove", "insert", "getRandom"],
                [[], [4], [4], [4], []],
                [None, True, True, True, 4],
            ),
            (
                [
                    "RandomizedCollection",
                    "insert",
                    "insert",
                    "insert",
                    "remove",
                    "remove",
                    "getRandom",
                ],
                [[], [1], [1], [1], [1], [1], []],
                [None, True, False, False, True, True, 1],
            ),
            (
                ["RandomizedCollection", "insert", "remove", "remove", "insert", "getRandom"],
                [[], [2], [2], [2], [2], []],
                [None, True, True, False, True, 2],
            ),
            (
                ["RandomizedCollection", "insert", "insert", "getRandom"],
                [[], [-5], [-5], []],
                [None, True, False, -5],
            ),
            (
                ["RandomizedCollection", "insert", "getRandom"],
                [[], [2147483647], []],
                [None, True, 2147483647],
            ),
            (
                ["RandomizedCollection", "insert", "insert", "getRandom"],
                [[], [-2147483648], [-2147483648], []],
                [None, True, False, -2147483648],
            ),
            (
                [
                    "RandomizedCollection",
                    "insert",
                    "insert",
                    "insert",
                    "remove",
                    "remove",
                    "getRandom",
                ],
                [[], [10], [20], [30], [20], [30], []],
                [None, True, True, True, True, True, 10],
            ),
            (
                ["RandomizedCollection", "insert", "getRandom", "insert", "getRandom"],
                [[], [7], [], [7], []],
                [None, True, 7, False, 7],
            ),
            (
                [
                    "RandomizedCollection",
                    "insert",
                    "insert",
                    "insert",
                    "remove",
                    "remove",
                    "getRandom",
                ],
                [[], [5], [6], [6], [6], [6], []],
                [None, True, True, False, True, True, 5],
            ),
            (
                [
                    "RandomizedCollection",
                    "insert",
                    "insert",
                    "insert",
                    "insert",
                    "remove",
                    "remove",
                    "getRandom",
                ],
                [[], [8], [8], [9], [8], [8], [9], []],
                [None, True, False, True, False, True, True, 8],
            ),
            (
                [
                    "RandomizedCollection",
                    "insert",
                    "insert",
                    "remove",
                    "insert",
                    "remove",
                    "getRandom",
                ],
                [[], [3], [3], [3], [3], [3], []],
                [None, True, False, True, False, True, 3],
            ),
            (
                ["RandomizedCollection", "insert", "insert", "remove", "getRandom"],
                [[], [2], [3], [3], []],
                [None, True, True, True, 2],
            ),
            (
                ["RandomizedCollection", "insert", "insert", "remove", "getRandom"],
                [[], [6], [6], [6], []],
                [None, True, False, True, 6],
            ),
            (
                ["RandomizedCollection", "insert", "insert", "insert", "remove", "getRandom"],
                [[], [-1], [-1], [7], [7], []],
                [None, True, False, True, True, -1],
            ),
        ],
    )
    def test_randomized_collection(
        self, operations: list[str], inputs: list[list[int]], expected: list[int | bool | None]
    ):
        result = run_randomized_collection_operations(RandomizedCollection, operations, inputs)
        assert_randomized_collection_operations(result, expected)
