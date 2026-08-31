import pytest

from leetcode_py import logged_test

from .helpers import assert_zigzag_iterator, run_zigzag_iterator
from .solution import ZigzagIterator


class TestZigzagIteratorTest:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                [
                    "ZigzagIterator",
                    "next",
                    "has_next",
                    "next",
                    "next",
                    "next",
                    "has_next",
                    "next",
                    "has_next",
                ],
                [[[1, 2], [3, 4, 5, 6]], [], [], [], [], [], [], [], []],
                [None, 1, True, 3, 2, 4, True, 5, True],
            ),
            (["ZigzagIterator", "next", "has_next"], [[[1], []], [], []], [None, 1, False]),
            (["ZigzagIterator", "next", "has_next"], [[[], [1]], [], []], [None, 1, False]),
            (["ZigzagIterator", "has_next"], [[[], []], []], [None, False]),
            (
                ["ZigzagIterator", "next", "next", "next", "has_next"],
                [[[1, 2, 3], []], [], [], [], []],
                [None, 1, 2, 3, False],
            ),
            (
                ["ZigzagIterator", "next", "next", "next", "has_next"],
                [[[], [7, 8, 9]], [], [], []],
                [None, 7, 8, 9, False],
            ),
            (
                ["ZigzagIterator", "next", "next", "next", "next", "has_next"],
                [[[1, 2, 3], [4]], [], [], [], [], []],
                [None, 1, 4, 2, 3, False],
            ),
            (
                ["ZigzagIterator", "next", "next", "next", "next", "has_next"],
                [[[1], [2, 3, 4]], [], [], [], [], []],
                [None, 1, 2, 3, 4, False],
            ),
            (
                ["ZigzagIterator", "next", "next", "next", "has_next"],
                [[[1, 2], [3]], [], [], [], []],
                [None, 1, 3, 2, False],
            ),
            (
                ["ZigzagIterator", "next", "next", "next", "next", "next", "has_next"],
                [[[1, 1, 1], [2, 2]], [], [], [], [], [], []],
                [None, 1, 2, 1, 2, 1, False],
            ),
            (
                ["ZigzagIterator", "next", "next", "next", "next", "next", "next", "has_next"],
                [[[10, 20, 30, 40], [50, 60]], [], [], [], [], [], [], []],
                [None, 10, 50, 20, 60, 30, 40, False],
            ),
            (
                ["ZigzagIterator", "next", "next", "has_next"],
                [[[5], [6]], [], [], []],
                [None, 5, 6, False],
            ),
            (
                [
                    "ZigzagIterator",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "next",
                    "has_next",
                ],
                [[[1, 2, 3, 4], [5, 6, 7, 8]], [], [], [], [], [], [], [], [], []],
                [None, 1, 5, 2, 6, 3, 7, 4, 8, False],
            ),
        ],
    )
    def test_zigzag_iterator(
        self, operations: list[str], inputs: list[list], expected: list[int | bool | None]
    ):
        result, _ = run_zigzag_iterator(ZigzagIterator, operations, inputs)
        assert_zigzag_iterator(result, expected)
