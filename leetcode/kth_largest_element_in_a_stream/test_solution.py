from typing import Any

import pytest

from leetcode_py import logged_test

from .helpers import assert_kth_largest, run_kth_largest
from .solution import KthLargest


class TestKthLargestElementInAStream:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["KthLargest", "add", "add", "add", "add", "add"],
                [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]],
                [None, 4, 5, 5, 8, 8],
            ),
            (
                ["KthLargest", "add", "add", "add", "add"],
                [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]],
                [None, 7, 7, 7, 8],
            ),
            (["KthLargest", "add", "add", "add"], [[1, [5]], [2], [3], [1]], [None, 5, 5, 5]),
            (["KthLargest", "add"], [[1, []], [3]], [None, 3]),
            (["KthLargest", "add"], [[3, [5, 6]], [7]], [None, 5]),
            (["KthLargest", "add", "add"], [[2, [-3, -1, -2]], [-4], [-5]], [None, -2, -2]),
            (["KthLargest", "add"], [[3, [9, 9, 9]], [9]], [None, 9]),
            (["KthLargest", "add", "add", "add"], [[2, [3, 4]], [5], [6], [7]], [None, 4, 5, 6]),
            (["KthLargest", "add", "add"], [[2, [0]], [1], [2]], [None, 0, 1]),
            (["KthLargest", "add"], [[3, [1, 2, 3, 4, 5]], [0]], [None, 3]),
            (["KthLargest", "add", "add"], [[3, [5, 1, 2, 4, 3]], [6], [7]], [None, 4, 5]),
            (["KthLargest", "add", "add", "add"], [[2, [1, 1]], [1], [1], [1]], [None, 1, 1, 1]),
            (
                ["KthLargest", "add", "add", "add", "add"],
                [[3, [10, 20]], [15], [25], [5], [30]],
                [None, 10, 15, 15, 20],
            ),
        ],
    )
    def test_kth_largest(self, operations: list[str], inputs: list[list[Any]], expected: list[Any]):
        result = run_kth_largest(KthLargest, operations, inputs)
        assert_kth_largest(result, expected)
