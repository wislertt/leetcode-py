import pytest

from leetcode_py import logged_test

from .helpers import assert_first_unique, run_first_unique
from .solution import FirstUnique


class TestFirstUniqueNumber:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                [
                    "FirstUnique",
                    "show_first_unique",
                    "add",
                    "show_first_unique",
                    "add",
                    "show_first_unique",
                    "add",
                    "show_first_unique",
                ],
                [[2, 3, 5], [], [5], [], [2], [], [3], []],
                [None, 2, None, 2, None, 3, None, -1],
            ),
            (
                [
                    "FirstUnique",
                    "show_first_unique",
                    "add",
                    "add",
                    "add",
                    "add",
                    "add",
                    "show_first_unique",
                ],
                [[7, 7, 7, 7, 7, 7], [], [7], [3], [3], [7], [17], []],
                [None, -1, None, None, None, None, None, 17],
            ),
            (
                ["FirstUnique", "show_first_unique", "add", "show_first_unique"],
                [[809], [], [809], []],
                [None, 809, None, -1],
            ),
            (
                ["FirstUnique", "add", "add", "add", "show_first_unique"],
                [[1, 2, 3], [1], [2], [3], []],
                [None, None, None, None, -1],
            ),
            (
                [
                    "FirstUnique",
                    "show_first_unique",
                    "show_first_unique",
                    "add",
                    "show_first_unique",
                ],
                [[5, 5], [], [], [5], []],
                [None, -1, -1, None, -1],
            ),
            (
                [
                    "FirstUnique",
                    "add",
                    "show_first_unique",
                    "add",
                    "show_first_unique",
                    "add",
                    "show_first_unique",
                ],
                [[4, 4, 6], [4], [], [6], [], [9], []],
                [None, None, 6, None, -1, None, 9],
            ),
            (
                [
                    "FirstUnique",
                    "show_first_unique",
                    "add",
                    "show_first_unique",
                    "add",
                    "show_first_unique",
                ],
                [[42], [], [42], [], [42], []],
                [None, 42, None, -1, None, -1],
            ),
            (
                [
                    "FirstUnique",
                    "show_first_unique",
                    "add",
                    "show_first_unique",
                    "add",
                    "show_first_unique",
                ],
                [[100000000], [], [100000000], [], [1], []],
                [None, 100000000, None, -1, None, 1],
            ),
            (
                [
                    "FirstUnique",
                    "show_first_unique",
                    "add",
                    "show_first_unique",
                    "add",
                    "show_first_unique",
                ],
                [[1, 1, 2], [], [2], [], [3], []],
                [None, 2, None, -1, None, 3],
            ),
            (
                [
                    "FirstUnique",
                    "add",
                    "show_first_unique",
                    "add",
                    "add",
                    "add",
                    "show_first_unique",
                    "show_first_unique",
                ],
                [[9, 9, 9, 9], [19], [], [9], [19], [9], [], []],
                [None, None, 19, None, None, None, -1, -1],
            ),
            (
                ["FirstUnique", "show_first_unique", "add", "add", "add", "show_first_unique"],
                [[9, 9, 9, 6, 9, 9, 6, 8], [], [8], [8], [9], []],
                [None, 8, None, None, None, -1],
            ),
            (
                [
                    "FirstUnique",
                    "add",
                    "show_first_unique",
                    "show_first_unique",
                    "add",
                    "add",
                    "add",
                    "add",
                    "show_first_unique",
                ],
                [[9, 9], [8], [], [], [12], [8], [11], [9], []],
                [None, None, 8, 8, None, None, None, None, 12],
            ),
            (
                [
                    "FirstUnique",
                    "add",
                    "show_first_unique",
                    "show_first_unique",
                    "add",
                    "show_first_unique",
                    "add",
                    "add",
                    "show_first_unique",
                ],
                [[11, 4, 8, 4, 8, 4, 7], [18], [], [], [8], [], [7], [19], []],
                [None, None, 11, 11, None, 11, None, None, 11],
            ),
            (
                [
                    "FirstUnique",
                    "show_first_unique",
                    "add",
                    "show_first_unique",
                    "add",
                    "show_first_unique",
                    "show_first_unique",
                    "add",
                    "show_first_unique",
                ],
                [[4, 7, 3], [], [11], [], [7], [], [], [13], []],
                [None, 4, None, 4, None, 4, 4, None, 4],
            ),
            (
                [
                    "FirstUnique",
                    "show_first_unique",
                    "show_first_unique",
                    "add",
                    "add",
                    "add",
                    "show_first_unique",
                ],
                [[7, 1, 5, 2], [], [], [7], [1], [7], []],
                [None, 7, 7, None, None, None, 5],
            ),
        ],
    )
    def test_first_unique(
        self, operations: list[str], inputs: list[list[int]], expected: list[int | None]
    ):
        result, _ = run_first_unique(FirstUnique, operations, inputs)
        assert_first_unique(result, expected)
