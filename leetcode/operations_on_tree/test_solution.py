import pytest

from leetcode_py import logged_test

from .helpers import assert_operations_on_tree, run_operations_on_tree
from .solution import LockingTree


class TestLockingTree:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"],
                [[-1, 0, 0, 1, 1, 2, 2], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]],
                [None, True, False, True, True, True, False],
            ),
            (["LockingTree"], [[-1, 0]], [None]),
            (
                ["LockingTree", "lock", "lock", "unlock", "unlock"],
                [[-1, 0], [1, 1], [1, 2], [1, 2], [1, 1]],
                [None, True, False, False, True],
            ),
            (
                ["LockingTree", "lock", "upgrade", "upgrade"],
                [[-1, 0, 1], [0, 1], [2, 3], [0, 3]],
                [None, True, False, False],
            ),
            (
                ["LockingTree", "lock", "lock", "upgrade"],
                [[-1, 0, 1], [2, 4], [0, 1], [0, 5]],
                [None, True, True, False],
            ),
            (
                ["LockingTree", "lock", "lock", "upgrade"],
                [[-1, 0, 1, 2], [0, 1], [3, 2], [2, 5]],
                [None, True, True, False],
            ),
            (
                ["LockingTree", "lock", "lock", "lock", "upgrade", "lock", "upgrade", "unlock"],
                [[-1, 0, 1, 2, 2, 1], [3, 7], [4, 8], [5, 9], [0, 1], [3, 2], [1, 6], [3, 2]],
                [None, True, True, True, True, True, False, True],
            ),
            (
                ["LockingTree", "lock", "lock", "upgrade", "unlock", "upgrade", "upgrade"],
                [[-1, 0, 0, 1, 1], [3, 2], [2, 1], [1, 5], [2, 1], [1, 5], [0, 5]],
                [None, True, True, True, True, False, True],
            ),
            (
                ["LockingTree", "lock", "lock", "unlock", "upgrade", "unlock", "upgrade"],
                [[-1, 0, 0, 2], [3, 4], [3, 4], [3, 5], [2, 4], [2, 4], [0, 4]],
                [None, True, False, False, True, True, False],
            ),
            (
                ["LockingTree", "lock", "lock", "lock", "upgrade", "upgrade", "upgrade"],
                [[-1, 0, 0, 1, 1, 4], [3, 1], [5, 2], [2, 3], [1, 9], [4, 9], [0, 9]],
                [None, True, True, True, True, False, True],
            ),
            (
                ["LockingTree", "lock", "lock", "unlock", "unlock", "lock", "upgrade", "upgrade"],
                [[-1, 0], [0, 3], [1, 3], [0, 3], [1, 3], [1, 1], [0, 2], [0, 1]],
                [None, True, True, True, True, True, True, False],
            ),
            (
                ["LockingTree", "unlock", "upgrade", "upgrade", "unlock", "lock"],
                [[-1, 0, 1, 0, 0], [2, 2], [4, 3], [2, 3], [3, 1], [4, 2]],
                [None, False, False, False, False, True],
            ),
            (
                [
                    "LockingTree",
                    "upgrade",
                    "lock",
                    "upgrade",
                    "lock",
                    "lock",
                    "unlock",
                    "upgrade",
                    "unlock",
                    "lock",
                    "upgrade",
                ],
                [
                    [-1, 0, 0, 0, 0, 2, 1, 6],
                    [4, 5],
                    [6, 2],
                    [7, 4],
                    [5, 3],
                    [0, 4],
                    [3, 6],
                    [0, 3],
                    [4, 4],
                    [1, 5],
                    [0, 5],
                ],
                [None, False, True, False, True, True, False, False, False, True, False],
            ),
            (
                ["LockingTree", "lock", "lock", "upgrade", "lock", "lock"],
                [[-1, 0, 0, 1, 3], [4, 3], [2, 4], [2, 2], [3, 5], [4, 3]],
                [None, True, True, False, True, False],
            ),
            (
                [
                    "LockingTree",
                    "upgrade",
                    "unlock",
                    "lock",
                    "lock",
                    "lock",
                    "upgrade",
                    "unlock",
                    "unlock",
                    "upgrade",
                    "upgrade",
                ],
                [
                    [-1, 0, 0, 1],
                    [3, 1],
                    [2, 4],
                    [0, 5],
                    [2, 6],
                    [0, 6],
                    [2, 1],
                    [3, 6],
                    [3, 4],
                    [3, 4],
                    [1, 2],
                ],
                [None, False, False, True, True, False, False, False, False, False, False],
            ),
            (
                [
                    "LockingTree",
                    "lock",
                    "lock",
                    "unlock",
                    "lock",
                    "upgrade",
                    "upgrade",
                    "upgrade",
                    "lock",
                    "upgrade",
                    "lock",
                ],
                [
                    [-1, 0, 1, 2, 3, 0],
                    [5, 3],
                    [2, 5],
                    [2, 2],
                    [1, 5],
                    [4, 4],
                    [2, 2],
                    [5, 2],
                    [3, 5],
                    [3, 2],
                    [4, 3],
                ],
                [None, True, True, False, True, False, False, False, True, False, True],
            ),
            (
                ["LockingTree", "lock", "upgrade", "upgrade", "upgrade", "unlock", "lock"],
                [[-1, 0, 0, 2, 3, 4, 2, 1], [2, 6], [7, 2], [7, 5], [2, 4], [0, 4], [0, 3]],
                [None, True, False, False, False, False, True],
            ),
            (
                ["LockingTree", "lock", "lock", "lock", "lock", "unlock", "upgrade"],
                [[-1, 0, 1], [1, 6], [1, 6], [0, 2], [0, 4], [1, 3], [1, 3]],
                [None, True, False, True, False, False, False],
            ),
        ],
    )
    def test_operations_on_tree(
        self, operations: list[str], inputs: list[list[int]], expected: list[bool | None]
    ):
        result, _ = run_operations_on_tree(LockingTree, operations, inputs)
        assert_operations_on_tree(result, expected)
