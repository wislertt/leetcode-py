import pytest

from leetcode_py import logged_test

from .helpers import assert_my_stack, run_my_stack
from .solution import MyStack


class TestImplementStackUsingQueues:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["MyStack", "push", "push", "top", "pop", "empty"],
                [[], [1], [2], [], [], []],
                [None, None, None, 2, 2, False],
            ),
            (["MyStack", "empty"], [[], []], [None, True]),
            (
                ["MyStack", "push", "empty", "pop", "empty"],
                [[], [1], [], [], []],
                [None, None, False, 1, True],
            ),
            (
                ["MyStack", "push", "push", "push", "pop", "pop", "top", "pop", "empty"],
                [[], [1], [2], [3], [], [], [], [], []],
                [None, None, None, None, 3, 2, 1, 1, True],
            ),
            (["MyStack", "push", "top"], [[], [5], []], [None, None, 5]),
            (
                ["MyStack", "push", "push", "pop", "push", "top"],
                [[], [1], [2], [], [3], []],
                [None, None, None, 2, None, 3],
            ),
            (
                ["MyStack", "push", "push", "push", "push", "pop", "pop", "pop", "pop", "empty"],
                [[], [1], [2], [3], [4], [], [], [], [], []],
                [None, None, None, None, None, 4, 3, 2, 1, True],
            ),
            (
                ["MyStack", "push", "pop", "push", "pop", "empty"],
                [[], [7], [], [8], [], []],
                [None, None, 7, None, 8, True],
            ),
            (
                ["MyStack", "push", "push", "top", "top", "pop", "top"],
                [[], [9], [8], [], [], [], []],
                [None, None, None, 8, 8, 8, 9],
            ),
            (
                [
                    "MyStack",
                    "push",
                    "push",
                    "push",
                    "push",
                    "push",
                    "pop",
                    "pop",
                    "pop",
                    "push",
                    "top",
                ],
                [[], [1], [2], [3], [4], [5], [], [], [], [6], []],
                [None, None, None, None, None, None, 5, 4, 3, None, 6],
            ),
            (
                ["MyStack", "push", "empty", "top", "pop", "empty", "push", "empty"],
                [[], [1], [], [], [], [], [2], []],
                [None, None, False, 1, 1, True, None, False],
            ),
            (
                ["MyStack", "push", "push", "push", "pop", "push", "pop", "pop", "push", "pop"],
                [[], [1], [2], [3], [], [4], [], [], [5], []],
                [None, None, None, None, 3, None, 4, 2, None, 5],
            ),
        ],
    )
    def test_stack_operations(
        self, operations: list[str], inputs: list[list[int]], expected: list[int | None | bool]
    ):
        result, _ = run_my_stack(MyStack, operations, inputs)
        assert_my_stack(result, expected)
