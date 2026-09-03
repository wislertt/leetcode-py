import pytest

from leetcode_py import logged_test

from .helpers import assert_complete_binary_tree_inserter, run_complete_binary_tree_inserter
from .solution import CBTInserter


class TestCompleteBinaryTreeInserter:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["CBTInserter", "insert", "insert", "get_root"],
                [[1, 2], [3], [4], []],
                [None, 1, 2, [1, 2, 3, 4]],
            ),
            (["CBTInserter", "insert", "get_root"], [[1], [2], []], [None, 1, [1, 2]]),
            (["CBTInserter", "get_root"], [[1, 2, 3], []], [None, [1, 2, 3]]),
            (
                ["CBTInserter", "insert", "insert", "insert", "get_root"],
                [[1], [2], [3], [4], []],
                [None, 1, 1, 2, [1, 2, 3, 4]],
            ),
            (
                ["CBTInserter", "insert", "get_root"],
                [[4, 2, 6, 1, 3, 5, 7], [8], []],
                [None, 1, [4, 2, 6, 1, 3, 5, 7, 8]],
            ),
            (
                ["CBTInserter", "get_root", "insert", "get_root"],
                [[1, 2], [], [3], []],
                [None, [1, 2], 1, [1, 2, 3]],
            ),
            (
                ["CBTInserter", "insert", "insert", "get_root"],
                [[0], [0], [0], []],
                [None, 0, 0, [0, 0, 0]],
            ),
            (
                ["CBTInserter", "insert", "get_root"],
                [[1, 2, 3, 4, 5], [6], []],
                [None, 3, [1, 2, 3, 4, 5, 6]],
            ),
            (
                ["CBTInserter", "insert", "insert", "get_root"],
                [[1, 2, 3, 4, 5], [6], [7], []],
                [None, 3, 3, [1, 2, 3, 4, 5, 6, 7]],
            ),
            (
                ["CBTInserter", "get_root", "insert", "get_root"],
                [[5, 3, 8], [], [1], []],
                [None, [5, 3, 8], 3, [5, 3, 8, 1]],
            ),
            (
                ["CBTInserter", "insert", "insert", "get_root"],
                [[7, 4, 9, 2], [5000], [0], []],
                [None, 4, 9, [7, 4, 9, 2, 5000, 0]],
            ),
            (
                ["CBTInserter", "insert", "get_root"],
                [[1, 2, 3, 4, 5, 6, 7], [8], []],
                [None, 4, [1, 2, 3, 4, 5, 6, 7, 8]],
            ),
            (
                ["CBTInserter", "insert", "insert", "insert", "get_root"],
                [[2], [1], [3], [4], []],
                [None, 2, 2, 1, [2, 1, 3, 4]],
            ),
            (
                ["CBTInserter", "insert", "get_root"],
                [[9, 8, 7, 6, 5], [4], []],
                [None, 7, [9, 8, 7, 6, 5, 4]],
            ),
            (
                ["CBTInserter", "insert", "insert", "get_root"],
                [[100], [200], [300], []],
                [None, 100, 100, [100, 200, 300]],
            ),
            (
                ["CBTInserter", "get_root", "insert", "get_root"],
                [[1, 2, 3], [], [4], []],
                [None, [1, 2, 3], 2, [1, 2, 3, 4]],
            ),
            (
                ["CBTInserter", "insert", "get_root"],
                [[6, 4, 8, 2, 5, 7], [1], []],
                [None, 8, [6, 4, 8, 2, 5, 7, 1]],
            ),
            (["CBTInserter", "insert"], [[8, 4], [12]], [None, 8]),
        ],
    )
    def test_complete_binary_tree_inserter(
        self,
        operations: list[str],
        inputs: list[list[int | None]],
        expected: list[int | list[int | None] | None],
    ):
        result, _ = run_complete_binary_tree_inserter(CBTInserter, operations, inputs)
        assert_complete_binary_tree_inserter(result, expected)
