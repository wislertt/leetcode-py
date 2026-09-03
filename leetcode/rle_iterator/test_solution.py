import pytest

from leetcode_py import logged_test

from .helpers import assert_rle_iterator, run_rle_iterator
from .solution import RLEIterator


class TestRLEIterator:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["RLEIterator", "next", "next", "next", "next"],
                [[3, 8, 0, 9, 2, 5], [2], [1], [1], [2]],
                [None, 8, 8, 5, -1],
            ),
            (["RLEIterator", "next", "next"], [[0, 9, 2, 5], [1], [2]], [None, 5, -1]),
            (["RLEIterator", "next", "next"], [[5, 7], [5], [1]], [None, 7, -1]),
            (
                ["RLEIterator", "next", "next", "next", "next"],
                [[2, 4, 2, 6], [2], [2], [2], [1]],
                [None, 4, 6, -1, -1],
            ),
            (
                ["RLEIterator", "next", "next", "next", "next"],
                [[1, 1, 0, 2, 3, 3], [1], [3], [1], [1]],
                [None, 1, 3, -1, -1],
            ),
            (["RLEIterator", "next"], [[1000000000, 1000000000], [999999999]], [None, 1000000000]),
            (["RLEIterator", "next"], [[1, 1, 1, 2, 1, 3, 1, 4], [4]], [None, 4]),
            (
                ["RLEIterator", "next", "next", "next"],
                [[2, 8, 1, 8, 2, 5], [2], [1], [2]],
                [None, 8, 8, 5],
            ),
            (["RLEIterator", "next"], [[0, 1, 0, 2], [1]], [None, -1]),
            (["RLEIterator", "next", "next"], [[3, 5], [3], [1]], [None, 5, -1]),
            (["RLEIterator", "next"], [[1, 10, 1, 20, 1, 30, 1, 40, 1, 50], [5]], [None, 50]),
            (
                ["RLEIterator", "next", "next", "next", "next", "next"],
                [[4, 1, 4, 2, 4, 3], [3], [3], [3], [3], [3]],
                [None, 1, 2, 3, 3, -1],
            ),
            (["RLEIterator", "next"], [[2, 3, 2, 4], [100]], [None, -1]),
            (["RLEIterator", "next", "next", "next"], [[7, 9], [7], [1], [1]], [None, 9, -1, -1]),
            (
                ["RLEIterator", "next", "next", "next"],
                [[1, 0, 1, 1, 1, 2], [1], [1], [1]],
                [None, 0, 1, 2],
            ),
        ],
    )
    def test_next(self, operations: list[str], inputs: list[list[int]], expected: list[int | None]):
        result, _ = run_rle_iterator(RLEIterator, operations, inputs)
        assert_rle_iterator(result, expected)
