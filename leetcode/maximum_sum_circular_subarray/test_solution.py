import pytest

from leetcode_py import logged_test

from .helpers import assert_max_subarray_sum_circular, run_max_subarray_sum_circular
from .solution import Solution


class TestMaximumSumCircularSubarray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, -2, 3, -2], 3),
            ([5, -3, 5], 10),
            ([-3, -2, -3], -2),
            ([1], 1),
            ([-1], -1),
            ([1, 2, 3], 6),
            ([-1, -2, -3], -1),
            ([8, -1, 3, 4], 15),
            ([2, -2, 2, -2, 2], 4),
            ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
            ([10, -5, 10], 20),
            ([3, -1, 2, -1], 4),
            ([-5, 3, -5], 3),
            ([5, -4, 5], 10),
            ([0, 0, 0], 0),
            ([-10, 5, -10, 5], 5),
            ([1, -1, 1, -1, 1, -1, 1], 2),
            ([-3, -1, -2], -1),
        ],
    )
    def test_max_subarray_sum_circular(self, nums: list[int], expected: int):
        result = run_max_subarray_sum_circular(Solution, nums)
        assert_max_subarray_sum_circular(result, expected)
