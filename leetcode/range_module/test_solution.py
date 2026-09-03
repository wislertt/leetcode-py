import pytest

from leetcode_py import logged_test

from .helpers import assert_range_module, run_range_module
from .solution import RangeModule


class TestDesignRangeModule:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["RangeModule", "add_range", "remove_range", "query_range", "query_range"],
                [[], [10, 20], [14, 16], [10, 14], [13, 15]],
                [None, None, None, True, False],
            ),
            (
                ["RangeModule", "add_range", "remove_range", "query_range"],
                [[], [10, 20], [14, 16], [16, 17]],
                [None, None, None, True],
            ),
            (
                ["RangeModule", "add_range", "query_range"],
                [[], [5, 10], [5, 10]],
                [None, None, True],
            ),
            (
                ["RangeModule", "add_range", "query_range"],
                [[], [1, 5], [7, 9]],
                [None, None, False],
            ),
            (["RangeModule", "query_range"], [[], [1, 2]], [None, False]),
            (
                ["RangeModule", "add_range", "add_range", "query_range", "query_range"],
                [[], [1, 4], [6, 9], [3, 7], [2, 3]],
                [None, None, None, False, True],
            ),
            (
                ["RangeModule", "add_range", "add_range", "query_range"],
                [[], [1, 5], [5, 10], [1, 10]],
                [None, None, None, True],
            ),
            (
                ["RangeModule", "add_range", "add_range", "query_range", "query_range"],
                [[], [1, 5], [4, 8], [1, 8], [8, 9]],
                [None, None, None, True, False],
            ),
            (
                ["RangeModule", "add_range", "remove_range", "query_range", "query_range"],
                [[], [1, 10], [3, 5], [4, 5], [2, 3]],
                [None, None, None, False, True],
            ),
            (
                ["RangeModule", "add_range", "remove_range", "query_range"],
                [[], [2, 8], [2, 8], [2, 8]],
                [None, None, None, False],
            ),
            (
                ["RangeModule", "add_range", "remove_range", "query_range", "query_range"],
                [[], [1, 10], [4, 6], [6, 10], [3, 7]],
                [None, None, None, True, False],
            ),
            (
                ["RangeModule", "add_range", "remove_range", "query_range"],
                [[], [1, 3], [5, 7], [1, 3]],
                [None, None, None, True],
            ),
            (
                ["RangeModule", "add_range", "remove_range", "add_range", "query_range"],
                [[], [1, 10], [2, 4], [3, 6], [3, 6]],
                [None, None, None, None, True],
            ),
            (
                ["RangeModule", "add_range", "remove_range", "add_range", "query_range"],
                [[], [1, 10], [2, 4], [3, 6], [4, 7]],
                [None, None, None, None, True],
            ),
            (
                [
                    "RangeModule",
                    "add_range",
                    "add_range",
                    "add_range",
                    "query_range",
                    "query_range",
                ],
                [[], [1, 3], [7, 9], [13, 15], [1, 3], [8, 9]],
                [None, None, None, None, True, True],
            ),
            (
                [
                    "RangeModule",
                    "add_range",
                    "add_range",
                    "add_range",
                    "query_range",
                    "query_range",
                ],
                [[], [5, 7], [2, 7], [12, 18], [13, 17], [8, 13]],
                [None, None, None, None, True, False],
            ),
            (
                ["RangeModule", "query_range", "add_range", "query_range", "add_range"],
                [[], [11, 16], [2, 8], [10, 13], [16, 19]],
                [None, False, None, False, None],
            ),
            (
                ["RangeModule", "query_range", "add_range", "remove_range"],
                [[], [15, 18], [2, 7], [10, 14]],
                [None, False, None, None],
            ),
            (
                ["RangeModule", "query_range", "add_range", "add_range", "add_range"],
                [[], [17, 23], [13, 15], [3, 7], [13, 19]],
                [None, False, None, None, None],
            ),
            (
                ["RangeModule", "add_range", "add_range", "query_range"],
                [[], [6, 9], [12, 17], [3, 7]],
                [None, None, None, False],
            ),
            (
                ["RangeModule", "query_range", "add_range", "remove_range"],
                [[], [5, 11], [14, 18], [6, 8]],
                [None, False, None, None],
            ),
        ],
    )
    def test_range_module(
        self, operations: list[str], inputs: list[list[int]], expected: list[bool | None]
    ):
        result, _ = run_range_module(RangeModule, operations, inputs)
        assert_range_module(result, expected)
