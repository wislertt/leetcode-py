from typing import Any

import pytest

from leetcode_py import logged_test

from .helpers import assert_data_stream_as_disjoint_intervals, run_data_stream_as_disjoint_intervals
from .solution import SummaryRanges


class TestDataStreamAsDisjointIntervals:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                [
                    "SummaryRanges",
                    "addNum",
                    "getIntervals",
                    "addNum",
                    "getIntervals",
                    "addNum",
                    "getIntervals",
                    "addNum",
                    "getIntervals",
                    "addNum",
                    "getIntervals",
                ],
                [[], [1], [], [3], [], [7], [], [2], [], [6], []],
                [
                    None,
                    None,
                    [[1, 1]],
                    None,
                    [[1, 1], [3, 3]],
                    None,
                    [[1, 1], [3, 3], [7, 7]],
                    None,
                    [[1, 3], [7, 7]],
                    None,
                    [[1, 3], [6, 7]],
                ],
            ),
            (["SummaryRanges", "getIntervals"], [[], []], [None, []]),
            (["SummaryRanges", "addNum", "getIntervals"], [[], [0], []], [None, None, [[0, 0]]]),
            (
                ["SummaryRanges", "addNum", "addNum", "getIntervals"],
                [[], [5], [5], []],
                [None, None, None, [[5, 5]]],
            ),
            (
                ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals"],
                [[], [5], [], [4], []],
                [None, None, [[5, 5]], None, [[4, 5]]],
            ),
            (
                ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals"],
                [[], [5], [], [6], []],
                [None, None, [[5, 5]], None, [[5, 6]]],
            ),
            (
                ["SummaryRanges", "addNum", "addNum", "addNum", "getIntervals"],
                [[], [1], [2], [3], []],
                [None, None, None, None, [[1, 3]]],
            ),
            (
                ["SummaryRanges", "addNum", "addNum", "getIntervals", "addNum", "getIntervals"],
                [[], [1], [1], [], [1], []],
                [None, None, None, [[1, 1]], None, [[1, 1]]],
            ),
            (
                ["SummaryRanges", "addNum", "addNum", "addNum", "addNum", "getIntervals"],
                [[], [10], [8], [6], [7], []],
                [None, None, None, None, None, [[6, 8], [10, 10]]],
            ),
            (
                [
                    "SummaryRanges",
                    "addNum",
                    "addNum",
                    "addNum",
                    "getIntervals",
                    "addNum",
                    "getIntervals",
                ],
                [[], [100], [50], [75], [], [49], []],
                [
                    None,
                    None,
                    None,
                    None,
                    [[50, 50], [75, 75], [100, 100]],
                    None,
                    [[49, 50], [75, 75], [100, 100]],
                ],
            ),
            (
                [
                    "SummaryRanges",
                    "addNum",
                    "getIntervals",
                    "addNum",
                    "getIntervals",
                    "addNum",
                    "getIntervals",
                ],
                [[], [10000], [], [0], [], [9999], []],
                [
                    None,
                    None,
                    [[10000, 10000]],
                    None,
                    [[0, 0], [10000, 10000]],
                    None,
                    [[0, 0], [9999, 10000]],
                ],
            ),
            (
                ["SummaryRanges", "addNum", "addNum", "addNum", "addNum", "addNum", "getIntervals"],
                [[], [3], [1], [2], [5], [4], []],
                [None, None, None, None, None, None, [[1, 5]]],
            ),
        ],
    )
    def test_data_stream_as_disjoint_intervals(
        self, operations: list[str], inputs: list[list[Any]], expected: list[Any]
    ):
        result = run_data_stream_as_disjoint_intervals(SummaryRanges, operations, inputs)
        assert_data_stream_as_disjoint_intervals(result, expected)
