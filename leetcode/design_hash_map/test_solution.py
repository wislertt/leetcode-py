import pytest

from leetcode_py import logged_test

from .helpers import assert_hash_map, run_hash_map
from .solution import MyHashMap


class TestDesignHashMap:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"],
                [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]],
                [None, None, None, 1, -1, None, 1, None, -1],
            ),
            (
                ["MyHashMap", "put", "put", "get", "put", "get"],
                [[], [1, 10], [1, 20], [1], [1, 30], [1]],
                [None, None, None, 20, None, 30],
            ),
            (["MyHashMap", "remove", "get"], [[], [5], [5]], [None, None, -1]),
            (
                ["MyHashMap", "put", "get", "remove", "get"],
                [[], [0, 100], [0], [0], [0]],
                [None, None, 100, None, -1],
            ),
            (
                ["MyHashMap", "put", "get", "remove", "get"],
                [[], [1000000, 7], [1000000], [1000000], [1000000]],
                [None, None, 7, None, -1],
            ),
            (["MyHashMap", "put", "get"], [[], [3, 0], [3]], [None, None, 0]),
            (
                ["MyHashMap", "put", "remove", "put", "get"],
                [[], [1, 5], [1], [1, 9], [1]],
                [None, None, None, None, 9],
            ),
            (
                ["MyHashMap", "put", "put", "put", "get", "get", "get"],
                [[], [1, 1], [2, 2], [3, 3], [1], [2], [3]],
                [None, None, None, None, 1, 2, 3],
            ),
            (["MyHashMap", "get"], [[], [1]], [None, -1]),
            (
                ["MyHashMap", "put", "put", "put", "put", "get", "get"],
                [[], [1, 1], [2, 2], [1, 100], [2, 200], [1], [2]],
                [None, None, None, None, None, 100, 200],
            ),
            (
                ["MyHashMap", "put", "put", "put", "remove", "get", "get", "get"],
                [[], [1, 1], [2, 2], [3, 3], [2], [1], [2], [3]],
                [None, None, None, None, None, 1, -1, 3],
            ),
            (
                ["MyHashMap", "put", "remove", "remove", "get"],
                [[], [7, 7], [7], [7], [7]],
                [None, None, None, None, -1],
            ),
            (
                ["MyHashMap", "put", "get", "put", "get", "remove", "get"],
                [[], [10, 1], [10], [10, 2], [10], [10], [10]],
                [None, None, 1, None, 2, None, -1],
            ),
        ],
    )
    def test_hash_map(
        self, operations: list[str], inputs: list[list[int]], expected: list[int | None]
    ):
        result, _ = run_hash_map(MyHashMap, operations, inputs)
        assert_hash_map(result, expected)
