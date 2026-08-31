import pytest

from leetcode_py import logged_test

from .helpers import assert_calendar_ops, run_calendar_ops
from .solution import MyCalendarTwo


class TestMyCalendarII:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["MyCalendarTwo", "book", "book", "book", "book", "book", "book"],
                [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]],
                [None, True, True, True, False, True, True],
            ),
            (
                ["MyCalendarTwo", "book", "book", "book"],
                [[], [1, 2], [2, 3], [3, 4]],
                [None, True, True, True],
            ),
            (["MyCalendarTwo", "book", "book"], [[], [1, 2], [1, 2]], [None, True, True]),
            (
                ["MyCalendarTwo", "book", "book", "book"],
                [[], [1, 2], [1, 2], [1, 2]],
                [None, True, True, False],
            ),
            (
                ["MyCalendarTwo", "book", "book", "book", "book"],
                [[], [10, 20], [10, 20], [10, 20], [15, 25]],
                [None, True, True, False, False],
            ),
            (
                ["MyCalendarTwo", "book", "book", "book"],
                [[], [5, 15], [10, 20], [5, 10]],
                [None, True, True, True],
            ),
            (
                ["MyCalendarTwo", "book", "book", "book", "book"],
                [[], [1, 5], [4, 8], [2, 6], [10, 12]],
                [None, True, True, False, True],
            ),
            (
                ["MyCalendarTwo", "book", "book", "book", "book", "book"],
                [[], [1, 10], [2, 3], [3, 4], [2, 3], [1, 2]],
                [None, True, True, True, False, True],
            ),
            (
                ["MyCalendarTwo", "book", "book", "book"],
                [[], [0, 1000000000], [0, 1000000000], [0, 1000000000]],
                [None, True, True, False],
            ),
            (
                ["MyCalendarTwo", "book", "book", "book", "book"],
                [[], [26, 35], [26, 32], [20, 30], [20, 26]],
                [None, True, True, False, True],
            ),
            (
                ["MyCalendarTwo", "book", "book", "book", "book"],
                [[], [10, 20], [10, 13], [13, 16], [10, 16]],
                [None, True, True, True, False],
            ),
            (
                [
                    "MyCalendarTwo",
                    "book",
                    "book",
                    "book",
                    "book",
                    "book",
                    "book",
                    "book",
                    "book",
                    "book",
                    "book",
                ],
                [
                    [],
                    [24, 40],
                    [43, 50],
                    [27, 43],
                    [5, 21],
                    [30, 40],
                    [29, 38],
                    [44, 50],
                    [31, 38],
                    [30, 38],
                    [25, 32],
                ],
                [None, True, True, True, True, False, False, True, False, False, False],
            ),
        ],
    )
    def test_calendar_ops(
        self, operations: list[str], inputs: list[list[int]], expected: list[bool | None]
    ):
        result, _ = run_calendar_ops(MyCalendarTwo, operations, inputs)
        assert_calendar_ops(result, expected)
