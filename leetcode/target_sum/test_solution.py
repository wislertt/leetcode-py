import pytest

from leetcode_py import logged_test

from .helpers import assert_find_target_sum_ways, run_find_target_sum_ways
from .solution import Solution


class TestTargetSum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, target, expected",
        [
            ([1, 1, 1, 1, 1], 3, 5),
            ([1], 1, 1),
            ([1], 2, 0),
            ([0, 0, 0, 0, 0, 0, 0, 0, 0], 0, 512),
            ([1000], -1000, 1),
            ([0, 0, 1], 1, 4),
            ([1, 2, 1], 0, 2),
            ([2, 3, 5], 5, 0),
            ([0], 0, 2),
            ([0, 1, 0], 1, 4),
            ([1000], 1000, 1),
            ([1, 2, 3, 4, 5], 3, 3),
            ([1, 1, 1], -1, 3),
            ([9, 7, 0, 3, 9, 8, 6, 5, 7, 5], 0, 0),
        ],
    )
    def test_find_target_sum_ways(self, nums: list[int], target: int, expected: int):
        result = run_find_target_sum_ways(Solution, nums, target)
        assert_find_target_sum_ways(result, expected)
