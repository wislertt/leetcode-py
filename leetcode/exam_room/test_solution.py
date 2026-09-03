import pytest

from leetcode_py import logged_test

from .helpers import assert_exam_room, run_exam_room
from .solution import ExamRoom


class TestExamRoom:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"],
                [[10], [], [], [], [], [4], []],
                [None, 0, 9, 4, 2, None, 5],
            ),
            (["ExamRoom", "seat"], [[1], []], [None, 0]),
            (["ExamRoom", "seat", "leave", "seat"], [[1], [], [0], []], [None, 0, None, 0]),
            (
                ["ExamRoom", "seat", "seat", "leave", "seat"],
                [[2], [], [], [0], []],
                [None, 0, 1, None, 0],
            ),
            (
                ["ExamRoom", "seat", "seat", "leave", "seat"],
                [[2], [], [], [1], []],
                [None, 0, 1, None, 1],
            ),
            (["ExamRoom", "seat", "seat", "seat"], [[3], [], [], []], [None, 0, 2, 1]),
            (
                ["ExamRoom", "seat", "seat", "seat", "seat"],
                [[4], [], [], [], []],
                [None, 0, 3, 1, 2],
            ),
            (
                ["ExamRoom", "seat", "seat", "leave", "seat"],
                [[4], [], [], [0], []],
                [None, 0, 3, None, 0],
            ),
            (
                ["ExamRoom", "seat", "seat", "seat", "leave", "seat"],
                [[5], [], [], [], [0], []],
                [None, 0, 4, 2, None, 0],
            ),
            (
                ["ExamRoom", "seat", "seat", "seat", "leave", "seat"],
                [[5], [], [], [], [4], []],
                [None, 0, 4, 2, None, 4],
            ),
            (
                ["ExamRoom", "seat", "seat", "seat", "leave", "seat", "leave", "seat"],
                [[10], [], [], [], [4], [], [0], []],
                [None, 0, 9, 4, None, 4, None, 0],
            ),
            (
                ["ExamRoom", "seat", "seat", "seat", "leave", "seat", "seat"],
                [[10], [], [], [], [9], [], []],
                [None, 0, 9, 4, None, 9, 2],
            ),
            (
                ["ExamRoom", "seat", "seat", "seat", "leave", "leave", "seat", "seat"],
                [[6], [], [], [], [2], [5], [], []],
                [None, 0, 5, 2, None, None, 5, 2],
            ),
            (
                ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "leave", "seat", "seat"],
                [[8], [], [], [], [], [0], [7], [], []],
                [None, 0, 7, 3, 5, None, None, 0, 7],
            ),
            (
                ["ExamRoom", "seat", "seat", "seat", "leave", "seat"],
                [[1000000000], [], [], [], [499999999], []],
                [None, 0, 999999999, 499999999, None, 499999999],
            ),
            (
                ["ExamRoom", "seat", "seat", "leave", "seat", "seat", "seat"],
                [[4], [], [], [0], [], [], []],
                [None, 0, 3, None, 0, 1, 2],
            ),
            (
                ["ExamRoom", "seat", "leave", "seat", "seat", "seat"],
                [[8], [], [0], [], [], []],
                [None, 0, None, 0, 7, 3],
            ),
            (
                ["ExamRoom", "seat", "seat", "leave", "leave", "seat"],
                [[12], [], [], [0], [11], []],
                [None, 0, 11, None, None, 0],
            ),
            (
                ["ExamRoom", "seat", "leave", "seat", "leave", "seat", "leave"],
                [[1], [], [0], [], [0], [], [0]],
                [None, 0, None, 0, None, 0, None],
            ),
            (
                ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"],
                [[12], [], [], [], [], [11], []],
                [None, 0, 11, 5, 8, None, 11],
            ),
            (["ExamRoom", "seat", "seat", "seat"], [[8], [], [], []], [None, 0, 7, 3]),
            (
                ["ExamRoom", "seat", "leave", "seat", "seat", "seat", "seat", "leave"],
                [[7], [], [0], [], [], [], [], [1]],
                [None, 0, None, 0, 6, 3, 1, None],
            ),
        ],
    )
    def test_exam_room(
        self, operations: list[str], inputs: list[list[int]], expected: list[int | None]
    ):
        result, _ = run_exam_room(ExamRoom, operations, inputs)
        assert_exam_room(result, expected)
