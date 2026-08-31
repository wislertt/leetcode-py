import pytest

from leetcode_py import logged_test

from .helpers import assert_linked_list_ops, run_linked_list_ops
from .solution import MyLinkedList


class TestDesignLinkedList:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                [
                    "MyLinkedList",
                    "add_at_head",
                    "add_at_tail",
                    "add_at_index",
                    "get",
                    "delete_at_index",
                    "get",
                ],
                [[], [1], [3], [1, 2], [1], [1], [1]],
                [None, None, None, None, 2, None, 3],
            ),
            (["MyLinkedList", "add_at_head", "get"], [[], [1], [0]], [None, None, 1]),
            (
                ["MyLinkedList", "add_at_tail", "get", "get"],
                [[], [1], [0], [1]],
                [None, None, 1, -1],
            ),
            (["MyLinkedList", "get"], [[], [0]], [None, -1]),
            (
                ["MyLinkedList", "add_at_head", "delete_at_index", "get"],
                [[], [1], [0], [0]],
                [None, None, None, -1],
            ),
            (["MyLinkedList", "add_at_index", "get"], [[], [0, 1], [0]], [None, None, 1]),
            (["MyLinkedList", "add_at_index", "get"], [[], [1, 1], [0]], [None, None, -1]),
            (
                ["MyLinkedList", "add_at_tail", "add_at_index", "delete_at_index", "get", "get"],
                [[], [1], [0, 2], [0], [0], [0]],
                [None, None, None, None, 1, 1],
            ),
            (
                ["MyLinkedList", "add_at_head", "add_at_head", "add_at_head", "get", "get", "get"],
                [[], [1], [2], [3], [0], [1], [2]],
                [None, None, None, None, 3, 2, 1],
            ),
            (
                [
                    "MyLinkedList",
                    "add_at_tail",
                    "add_at_tail",
                    "add_at_tail",
                    "delete_at_index",
                    "delete_at_index",
                    "get",
                    "get",
                    "get",
                ],
                [[], [1], [2], [3], [0], [0], [0], [0], [0]],
                [None, None, None, None, None, None, 3, 3, 3],
            ),
            (
                ["MyLinkedList", "add_at_index", "add_at_index", "add_at_index", "get"],
                [[], [3, 3], [0, 1], [1, 2], [0]],
                [None, None, None, None, 1],
            ),
            (
                [
                    "MyLinkedList",
                    "add_at_tail",
                    "add_at_index",
                    "add_at_index",
                    "add_at_index",
                    "get",
                    "get",
                    "get",
                    "get",
                ],
                [[], [5], [0, 1], [1, 2], [2, 3], [0], [1], [2], [3]],
                [None, None, None, None, None, 1, 2, 3, 5],
            ),
            (
                ["MyLinkedList", "add_at_head", "delete_at_index", "get", "add_at_tail", "get"],
                [[], [5], [0], [0], [7], [0]],
                [None, None, None, -1, None, 7],
            ),
            (
                [
                    "MyLinkedList",
                    "add_at_tail",
                    "add_at_tail",
                    "add_at_index",
                    "delete_at_index",
                    "delete_at_index",
                    "get",
                    "add_at_head",
                    "get",
                    "get",
                ],
                [[], [1], [2], [1, 3], [2], [0], [0], [9], [0], [1]],
                [None, None, None, None, None, None, 3, None, 9, 3],
            ),
        ],
    )
    def test_linked_list_ops(
        self, operations: list[str], inputs: list[list[int]], expected: list[int | None]
    ):
        result, _ = run_linked_list_ops(MyLinkedList, operations, inputs)
        assert_linked_list_ops(result, expected)
