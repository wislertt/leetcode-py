import pytest

from leetcode_py import logged_test

from .helpers import assert_lfu_cache, run_lfu_cache
from .solution import LFUCache


class TestLFUCache:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"],
                [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]],
                [None, None, None, 1, None, -1, 3, None, -1, 3, 4],
            ),
            (
                ["LFUCache", "put", "put", "put", "get", "get", "get"],
                [[2], [1, 1], [2, 2], [1, 10], [1], [2], [1]],
                [None, None, None, None, 10, 2, 10],
            ),
            (
                ["LFUCache", "put", "put", "put", "get", "get", "get"],
                [[2], [1, 1], [2, 2], [3, 3], [1], [2], [3]],
                [None, None, None, None, -1, 2, 3],
            ),
            (
                ["LFUCache", "put", "put", "get", "put", "get", "get", "get"],
                [[2], [1, 1], [2, 2], [1], [3, 3], [2], [1], [3]],
                [None, None, None, 1, None, -1, 1, 3],
            ),
            (
                ["LFUCache", "put", "get", "put", "get", "get"],
                [[1], [1, 1], [1], [2, 2], [1], [2]],
                [None, None, 1, None, -1, 2],
            ),
            (
                [
                    "LFUCache",
                    "put",
                    "put",
                    "put",
                    "get",
                    "get",
                    "get",
                    "put",
                    "get",
                    "get",
                    "get",
                    "get",
                ],
                [[3], [1, 1], [2, 2], [3, 3], [1], [2], [3], [4, 4], [1], [2], [3], [4]],
                [None, None, None, None, 1, 2, 3, None, -1, 2, 3, 4],
            ),
            (
                ["LFUCache", "put", "put", "put", "get", "get"],
                [[2], [1, 1], [2, 2], [1, 100], [1], [2]],
                [None, None, None, None, 100, 2],
            ),
            (
                ["LFUCache", "put", "get", "put", "put", "get", "get", "get"],
                [[2], [1, 1], [1], [2, 2], [3, 3], [2], [1], [3]],
                [None, None, 1, None, None, -1, 1, 3],
            ),
            (
                ["LFUCache", "put", "put", "put", "put", "get", "get", "get"],
                [[2], [1, 1], [2, 2], [1, 5], [3, 3], [2], [1], [3]],
                [None, None, None, None, None, -1, 5, 3],
            ),
            (
                [
                    "LFUCache",
                    "put",
                    "put",
                    "put",
                    "get",
                    "get",
                    "get",
                    "put",
                    "get",
                    "get",
                    "get",
                    "get",
                ],
                [[3], [1, 1], [2, 2], [3, 3], [1], [1], [2], [4, 4], [3], [1], [2], [4]],
                [None, None, None, None, 1, 1, 2, None, -1, 1, 2, 4],
            ),
            (
                ["LFUCache", "put", "put", "get", "put", "get", "get", "get"],
                [[2], [1, 1], [2, 2], [3], [3, 3], [1], [2], [3]],
                [None, None, None, -1, None, -1, 2, 3],
            ),
            (
                ["LFUCache", "put", "put", "put", "put", "put", "get", "get", "get", "get", "get"],
                [[10], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1], [2], [3], [4], [5]],
                [None, None, None, None, None, None, 1, 2, 3, 4, 5],
            ),
            (
                ["LFUCache", "put", "put", "get", "put", "get", "get"],
                [[2], [1, 1], [2, 2], [2], [3, 3], [1], [2]],
                [None, None, None, 2, None, -1, 2],
            ),
            (
                [
                    "LFUCache",
                    "put",
                    "put",
                    "get",
                    "put",
                    "get",
                    "get",
                    "get",
                    "put",
                    "get",
                    "get",
                    "get",
                ],
                [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [1], [4, 4], [3], [1], [4]],
                [None, None, None, 1, None, -1, 3, 1, None, -1, 1, 4],
            ),
            (["LFUCache", "get"], [[2], [1]], [None, -1]),
        ],
    )
    def test_lfu_cache(
        self, operations: list[str], inputs: list[list[int]], expected: list[int | None]
    ):
        result, _ = run_lfu_cache(LFUCache, operations, inputs)
        assert_lfu_cache(result, expected)
