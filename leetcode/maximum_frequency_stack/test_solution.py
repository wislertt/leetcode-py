import pytest

from leetcode_py import logged_test

from .helpers import assert_freq_stack_operations, run_freq_stack_operations
from .solution import FreqStack


class TestTestMaximumFrequencyStack:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                [
                    "FreqStack",
                    "push",
                    "push",
                    "push",
                    "push",
                    "push",
                    "push",
                    "pop",
                    "pop",
                    "pop",
                    "pop",
                ],
                [[], [5], [7], [5], [7], [4], [5], [], [], [], []],
                [None, None, None, None, None, None, None, 5, 7, 5, 4],
            ),
            (["FreqStack", "push", "pop"], [[], [5], []], [None, None, 5]),
            (
                ["FreqStack", "push", "push", "push", "push", "pop", "pop", "pop", "pop"],
                [[], [1], [2], [2], [1], [], [], [], []],
                [None, None, None, None, None, 1, 2, 2, 1],
            ),
            (
                ["FreqStack", "push", "push", "push", "pop", "pop", "pop"],
                [[], [5], [5], [5], [], [], []],
                [None, None, None, None, 5, 5, 5],
            ),
            (
                [
                    "FreqStack",
                    "push",
                    "push",
                    "push",
                    "push",
                    "push",
                    "pop",
                    "pop",
                    "pop",
                    "pop",
                    "pop",
                ],
                [[], [5], [4], [5], [4], [5], [], [], [], [], []],
                [None, None, None, None, None, None, 5, 4, 5, 4, 5],
            ),
            (
                ["FreqStack", "push", "push", "push", "pop", "pop", "pop"],
                [[], [1], [2], [3], [], [], []],
                [None, None, None, None, 3, 2, 1],
            ),
            (
                [
                    "FreqStack",
                    "push",
                    "push",
                    "push",
                    "push",
                    "push",
                    "push",
                    "pop",
                    "pop",
                    "pop",
                    "pop",
                    "pop",
                    "pop",
                ],
                [[], [1], [2], [2], [3], [3], [3], [], [], [], [], [], []],
                [None, None, None, None, None, None, None, 3, 3, 2, 3, 2, 1],
            ),
            (["FreqStack", "push", "pop"], [[], [1000000000], []], [None, None, 1000000000]),
            (["FreqStack", "push", "push", "pop"], [[], [0], [0], []], [None, None, None, 0]),
            (
                ["FreqStack", "push", "push", "push", "pop", "push", "pop"],
                [[], [1], [2], [1], [], [1], []],
                [None, None, None, None, 1, None, 1],
            ),
            (
                [
                    "FreqStack",
                    "push",
                    "push",
                    "push",
                    "push",
                    "push",
                    "push",
                    "push",
                    "pop",
                    "pop",
                    "pop",
                    "pop",
                    "pop",
                    "pop",
                    "pop",
                ],
                [[], [1], [2], [3], [1], [2], [3], [1], [], [], [], [], [], [], []],
                [None, None, None, None, None, None, None, None, 1, 3, 2, 1, 3, 2, 1],
            ),
            (
                [
                    "FreqStack",
                    "push",
                    "push",
                    "push",
                    "push",
                    "push",
                    "pop",
                    "pop",
                    "pop",
                    "pop",
                    "pop",
                ],
                [[], [7], [7], [7], [8], [8], [], [], [], [], []],
                [None, None, None, None, None, None, 7, 8, 7, 8, 7],
            ),
        ],
    )
    def test_freq_stack(
        self, operations: list[str], inputs: list[list[int]], expected: list[int | None]
    ):
        result = run_freq_stack_operations(FreqStack, operations, inputs)
        assert_freq_stack_operations(result, expected)
