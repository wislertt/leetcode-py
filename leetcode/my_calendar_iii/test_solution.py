import pytest

from leetcode_py import logged_test

from .helpers import assert_calendar_ops, run_calendar_ops
from .solution import MyCalendarThree


class TestMyCalendarIII:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["MyCalendarThree", "book", "book", "book", "book", "book", "book"],
                [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]],
                [None, 1, 1, 2, 3, 3, 3],
            ),
            (["MyCalendarThree", "book"], [[], [1, 2]], [None, 1]),
            (
                ["MyCalendarThree", "book", "book", "book"],
                [[], [1, 5], [5, 10], [10, 15]],
                [None, 1, 1, 1],
            ),
            (["MyCalendarThree", "book", "book"], [[], [3, 7], [3, 7]], [None, 1, 2]),
            (
                ["MyCalendarThree", "book", "book", "book"],
                [[], [3, 7], [3, 7], [3, 7]],
                [None, 1, 2, 3],
            ),
            (
                ["MyCalendarThree", "book", "book", "book"],
                [[], [10, 40], [5, 15], [5, 10]],
                [None, 1, 2, 2],
            ),
            (
                ["MyCalendarThree", "book", "book", "book"],
                [[], [0, 100], [10, 20], [12, 15]],
                [None, 1, 2, 3],
            ),
            (["MyCalendarThree", "book", "book"], [[], [5, 10], [10, 20]], [None, 1, 1]),
            (
                ["MyCalendarThree", "book", "book", "book"],
                [[], [0, 1000000000], [0, 1000000000], [999999999, 1000000000]],
                [None, 1, 2, 3],
            ),
            (
                ["MyCalendarThree", "book", "book", "book"],
                [[], [1, 10], [2, 3], [4, 5]],
                [None, 1, 2, 2],
            ),
            (
                ["MyCalendarThree", "book", "book", "book"],
                [[], [1, 5], [3, 8], [20, 30]],
                [None, 1, 2, 2],
            ),
            (
                ["MyCalendarThree", "book", "book", "book"],
                [[], [1, 4], [2, 5], [6, 9]],
                [None, 1, 2, 2],
            ),
            (
                ["MyCalendarThree", "book", "book", "book", "book"],
                [[], [1, 10], [1, 10], [1, 10], [1, 10]],
                [None, 1, 2, 3, 4],
            ),
            (
                ["MyCalendarThree", "book", "book", "book", "book"],
                [[], [1, 3], [2, 4], [3, 5], [4, 6]],
                [None, 1, 2, 2, 2],
            ),
            (
                ["MyCalendarThree", "book", "book", "book", "book"],
                [[], [0, 100], [10, 20], [10, 20], [30, 40]],
                [None, 1, 2, 3, 3],
            ),
            (
                ["MyCalendarThree", "book", "book", "book"],
                [[], [5, 15], [10, 20], [14, 25]],
                [None, 1, 2, 3],
            ),
            (
                ["MyCalendarThree", "book", "book", "book"],
                [[], [0, 50], [25, 30], [24, 26]],
                [None, 1, 2, 3],
            ),
            (
                ["MyCalendarThree", "book", "book", "book"],
                [[], [7, 9], [1, 8], [8, 12]],
                [None, 1, 2, 2],
            ),
        ],
    )
    def test_calendar_ops(
        self, operations: list[str], inputs: list[list[int]], expected: list[int | None]
    ):
        result, _ = run_calendar_ops(MyCalendarThree, operations, inputs)
        assert_calendar_ops(result, expected)
