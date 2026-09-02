import pytest

from leetcode_py import logged_test

from .helpers import assert_peeking_iterator, run_peeking_iterator
from .solution import PeekingIterator


class TestPeekingIterator:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["PeekingIterator", "next", "peek", "next", "next", "has_next"],
                [[[1, 2, 3]], [], [], [], [], []],
                [None, 1, 2, 2, 3, False],
            ),
            (
                ["PeekingIterator", "peek", "next", "peek", "peek", "next", "has_next"],
                [[[1, 2, 3]], [], [], [], [], [], []],
                [None, 1, 1, 2, 2, 2, True],
            ),
            (
                ["PeekingIterator", "has_next", "peek", "next", "has_next"],
                [[[1]], [], [], [], []],
                [None, True, 1, 1, False],
            ),
            (["PeekingIterator", "next", "has_next"], [[[1]], [], []], [None, 1, False]),
            (["PeekingIterator", "peek", "peek", "peek"], [[[5]], [], [], []], [None, 5, 5, 5]),
            (
                ["PeekingIterator", "peek", "peek", "next", "next", "has_next"],
                [[[2, 2]], [], [], [], [], []],
                [None, 2, 2, 2, 2, False],
            ),
            (
                ["PeekingIterator", "peek", "next", "peek", "next", "peek", "next", "has_next"],
                [[[7, 7, 7, 7]], [], [], [], [], [], [], []],
                [None, 7, 7, 7, 7, 7, 7, True],
            ),
            (
                ["PeekingIterator", "has_next", "peek", "has_next", "next", "has_next"],
                [[[1, 2]], [], [], [], [], []],
                [None, True, 1, True, 1, True],
            ),
            (
                ["PeekingIterator", "peek", "next", "next", "peek", "next", "has_next"],
                [[[1000, 1, 999]], [], [], [], [], [], []],
                [None, 1000, 1000, 1, 999, 999, False],
            ),
            (
                ["PeekingIterator", "peek", "next", "peek", "next", "peek", "next", "peek"],
                [[[3, 1, 4, 1, 5]], [], [], [], [], [], [], []],
                [None, 3, 3, 1, 1, 4, 4, 1],
            ),
            (["PeekingIterator", "peek", "next"], [[[10]], [], []], [None, 10, 10]),
            (
                ["PeekingIterator", "has_next", "next", "has_next", "next", "has_next", "next"],
                [[[42, 42, 42]], [], [], [], [], [], []],
                [None, True, 42, True, 42, True, 42],
            ),
            (
                ["PeekingIterator", "peek", "peek", "next", "next", "peek", "next", "has_next"],
                [[[8, 6, 7]], [], [], [], [], [], [], []],
                [None, 8, 8, 8, 6, 7, 7, False],
            ),
            (
                ["PeekingIterator", "has_next", "has_next", "peek", "next", "has_next"],
                [[[9]], [], [], [], [], []],
                [None, True, True, 9, 9, False],
            ),
            (
                ["PeekingIterator", "next", "peek", "next", "has_next"],
                [[[500, 501]], [], [], [], []],
                [None, 500, 501, 501, False],
            ),
            (
                [
                    "PeekingIterator",
                    "peek",
                    "peek",
                    "next",
                    "peek",
                    "next",
                    "peek",
                    "next",
                    "has_next",
                ],
                [[[1, 2, 3, 4, 5]], [], [], [], [], [], [], [], []],
                [None, 1, 1, 1, 2, 2, 3, 3, True],
            ),
        ],
    )
    def test_peeking_iterator(
        self, operations: list[str], inputs: list[list], expected: list[int | bool | None]
    ):
        result, _ = run_peeking_iterator(PeekingIterator, operations, inputs)
        assert_peeking_iterator(result, expected)
