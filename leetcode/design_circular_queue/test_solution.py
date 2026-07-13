import pytest

from leetcode_py import logged_test

from .helpers import assert_circular_queue, run_circular_queue
from .solution import MyCircularQueue


class TestDesignCircularQueue:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                [
                    "MyCircularQueue",
                    "en_queue",
                    "en_queue",
                    "en_queue",
                    "en_queue",
                    "rear",
                    "is_full",
                    "de_queue",
                    "en_queue",
                    "rear",
                ],
                [[3], [1], [2], [3], [4], [], [], [], [4], []],
                [None, True, True, True, False, 3, True, True, True, 4],
            ),
            (
                ["MyCircularQueue", "front", "rear", "is_empty", "de_queue"],
                [[3], [], [], [], []],
                [None, -1, -1, True, False],
            ),
            (
                ["MyCircularQueue", "en_queue", "front", "rear", "is_empty", "is_full"],
                [[1], [5], [], [], [], []],
                [None, True, 5, 5, False, True],
            ),
            (
                [
                    "MyCircularQueue",
                    "en_queue",
                    "en_queue",
                    "en_queue",
                    "is_full",
                    "de_queue",
                    "en_queue",
                    "front",
                    "rear",
                ],
                [[3], [1], [2], [3], [], [], [4], [], []],
                [None, True, True, True, True, True, True, 2, 4],
            ),
            (
                ["MyCircularQueue", "en_queue", "en_queue", "en_queue"],
                [[2], [1], [2], [3]],
                [None, True, True, False],
            ),
            (
                [
                    "MyCircularQueue",
                    "en_queue",
                    "en_queue",
                    "de_queue",
                    "de_queue",
                    "is_empty",
                    "front",
                ],
                [[2], [1], [2], [], [], [], []],
                [None, True, True, True, True, True, -1],
            ),
            (
                [
                    "MyCircularQueue",
                    "en_queue",
                    "en_queue",
                    "de_queue",
                    "en_queue",
                    "de_queue",
                    "en_queue",
                    "en_queue",
                    "front",
                    "rear",
                    "is_full",
                ],
                [[3], [1], [2], [], [3], [], [4], [5], [], [], []],
                [None, True, True, True, True, True, True, True, 3, 5, True],
            ),
            (
                ["MyCircularQueue", "en_queue", "rear", "en_queue", "rear", "en_queue", "rear"],
                [[3], [10], [], [20], [], [30], []],
                [None, True, 10, True, 20, True, 30],
            ),
            (
                [
                    "MyCircularQueue",
                    "en_queue",
                    "de_queue",
                    "is_empty",
                    "en_queue",
                    "front",
                    "rear",
                ],
                [[5], [1], [], [], [2], [], []],
                [None, True, True, True, True, 2, 2],
            ),
            (
                [
                    "MyCircularQueue",
                    "en_queue",
                    "en_queue",
                    "en_queue",
                    "de_queue",
                    "front",
                    "de_queue",
                    "front",
                ],
                [[3], [1], [2], [3], [], [], [], []],
                [None, True, True, True, True, 2, True, 3],
            ),
            (
                [
                    "MyCircularQueue",
                    "en_queue",
                    "is_full",
                    "en_queue",
                    "de_queue",
                    "is_empty",
                    "en_queue",
                    "front",
                ],
                [[1], [1], [], [2], [], [], [3], []],
                [None, True, True, False, True, True, True, 3],
            ),
            (
                ["MyCircularQueue", "en_queue", "front", "rear"],
                [[2], [0], [], []],
                [None, True, 0, 0],
            ),
            (
                ["MyCircularQueue", "en_queue", "en_queue", "is_empty", "is_full"],
                [[10], [1], [2], [], []],
                [None, True, True, False, False],
            ),
            (
                [
                    "MyCircularQueue",
                    "en_queue",
                    "en_queue",
                    "de_queue",
                    "de_queue",
                    "en_queue",
                    "en_queue",
                    "front",
                    "rear",
                    "is_full",
                ],
                [[2], [1], [2], [], [], [3], [4], [], [], []],
                [None, True, True, True, True, True, True, 3, 4, True],
            ),
            (
                [
                    "MyCircularQueue",
                    "en_queue",
                    "en_queue",
                    "en_queue",
                    "de_queue",
                    "de_queue",
                    "de_queue",
                    "en_queue",
                    "front",
                    "rear",
                    "is_empty",
                    "is_full",
                ],
                [[3], [1], [2], [3], [], [], [], [4], [], [], [], []],
                [None, True, True, True, True, True, True, True, 4, 4, False, False],
            ),
        ],
    )
    def test_circular_queue(
        self, operations: list[str], inputs: list[list[int]], expected: list[int | bool | None]
    ):
        result, _ = run_circular_queue(MyCircularQueue, operations, inputs)
        assert_circular_queue(result, expected)
