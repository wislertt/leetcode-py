from typing import Any

import pytest

from leetcode_py import logged_test

from .helpers import assert_depth_sum, run_depth_sum
from .solution import Solution


class TestNestedListWeightSum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nested_list, expected",
        [
            ([[1, 1], 2, [1, 1]], 10),
            ([1, [4, [6]]], 27),
            ([0], 0),
            ([1], 1),
            ([[1]], 2),
            ([[[[1]]]], 4),
            ([[-1, [-2]], -3], -11),
            ([[2, 2], 2, [2, 2]], 18),
            ([1, [2, [3, [4, [5]]]]], 55),
            ([[10]], 20),
            ([5, [5, [5, [5]]]], 50),
            ([[1, 2], [3, [4]], [5]], 34),
            ([100], 100),
            ([[[-100]]], -300),
            ([[1, [2, [3]]], [4]], 28),
        ],
    )
    def test_depth_sum(self, nested_list: list[Any], expected: int):
        result = run_depth_sum(Solution, nested_list)
        assert_depth_sum(result, expected)
