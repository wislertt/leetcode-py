from typing import Any

import pytest

from leetcode_py import logged_test

from .helpers import assert_depth_sum_inverse, run_depth_sum_inverse
from .solution import Solution


class TestNestedListWeightSumII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nested_list, expected",
        [
            ([[1, 1], 2, [1, 1]], 8),
            ([1, [4, [6]]], 17),
            ([1, [2, [3]]], 10),
            ([[1], [2], [3]], 6),
            ([1, 2, 3], 6),
            ([[-1, -1], 2, [[-3]]], -1),
            ([0, [0, [0]]], 0),
            ([[[[5]]]], 5),
            ([100], 100),
            ([-100], -100),
            ([1, [1], 1, [1]], 6),
            ([[1, 2], [3, [4, [5]]]], 31),
            ([[1], [[2]], [[[3]]]], 10),
            ([6, [5, 4], [3, [2]]], 44),
            ([[-2], [1, [-1]], 0], -3),
        ],
    )
    def test_depth_sum_inverse(self, nested_list: list[Any], expected: int):
        result = run_depth_sum_inverse(Solution, nested_list)
        assert_depth_sum_inverse(result, expected)
