import pytest

from leetcode_py import logged_test

from .helpers import assert_hash_set, run_hash_set
from .solution import MyHashSet


class TestDesignHashSet:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                [
                    "MyHashSet",
                    "add",
                    "add",
                    "contains",
                    "contains",
                    "add",
                    "contains",
                    "remove",
                    "contains",
                ],
                [[], [1], [2], [1], [3], [2], [2], [2], [2]],
                [None, None, None, True, False, None, True, None, False],
            ),
            (
                [
                    "MyHashSet",
                    "add",
                    "add",
                    "add",
                    "remove",
                    "contains",
                    "add",
                    "add",
                    "add",
                    "remove",
                    "contains",
                    "add",
                    "add",
                    "add",
                    "remove",
                    "contains",
                    "add",
                    "add",
                    "add",
                    "remove",
                    "contains",
                ],
                [
                    [],
                    [1],
                    [10001],
                    [1],
                    [1],
                    [1],
                    [7],
                    [10007],
                    [7],
                    [7],
                    [7],
                    [123],
                    [10123],
                    [123],
                    [123],
                    [123],
                    [5000],
                    [15000],
                    [5000],
                    [5000],
                    [5000],
                ],
                [
                    None,
                    None,
                    None,
                    None,
                    None,
                    False,
                    None,
                    None,
                    None,
                    None,
                    False,
                    None,
                    None,
                    None,
                    None,
                    False,
                    None,
                    None,
                    None,
                    None,
                    False,
                ],
            ),
            (
                ["MyHashSet", "add", "contains", "remove", "contains"],
                [[], [5], [5], [5], [5]],
                [None, None, True, None, False],
            ),
            (["MyHashSet", "remove", "contains"], [[], [99], [99]], [None, None, False]),
            (
                ["MyHashSet", "add", "remove", "add", "contains"],
                [[], [1], [1], [1], [1]],
                [None, None, None, None, True],
            ),
            (
                ["MyHashSet", "add", "contains", "add", "contains"],
                [[], [0], [0], [0], [0]],
                [None, None, True, None, True],
            ),
            (
                ["MyHashSet", "add", "contains", "remove", "contains"],
                [[], [1000000], [1000000], [1000000], [1000000]],
                [None, None, True, None, False],
            ),
            (
                ["MyHashSet", "add", "add", "add", "contains", "remove", "contains", "contains"],
                [[], [10], [20], [30], [20], [20], [20], [30]],
                [None, None, None, None, True, None, False, True],
            ),
            (
                ["MyHashSet", "add", "add", "add", "remove", "contains"],
                [[], [7], [7], [7], [7], [7]],
                [None, None, None, None, None, False],
            ),
            (["MyHashSet", "contains", "contains"], [[], [1], [2]], [None, False, False]),
            (
                [
                    "MyHashSet",
                    "add",
                    "contains",
                    "add",
                    "contains",
                    "remove",
                    "contains",
                    "add",
                    "contains",
                ],
                [[], [3], [3], [4], [4], [3], [3], [3], [3]],
                [None, None, True, None, True, None, False, None, True],
            ),
            (
                ["MyHashSet", "add", "add", "add", "add", "add", "contains", "remove", "contains"],
                [[], [1], [2], [3], [4], [5], [3], [3], [3]],
                [None, None, None, None, None, None, True, None, False],
            ),
            (
                ["MyHashSet", "add", "add", "remove", "remove", "contains"],
                [[], [100], [200], [100], [200], [100]],
                [None, None, None, None, None, False],
            ),
        ],
    )
    def test_hash_set(
        self, operations: list[str], inputs: list[list[int]], expected: list[int | bool | None]
    ):
        result, _ = run_hash_set(MyHashSet, operations, inputs)
        assert_hash_set(result, expected)
