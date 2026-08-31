import pytest

from leetcode_py import logged_test

from .helpers import assert_check_subarray_sum, run_check_subarray_sum
from .solution import Solution


class TestContinuousSubarraySum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([23, 2, 4, 6, 7], 6, True),
            ([23, 2, 6, 4, 7], 6, True),
            ([23, 2, 6, 4, 7], 13, False),
            ([1, 2], 2, False),
            ([0, 0], 1, True),
            ([0], 1, False),
            ([5, 0, 0], 3, True),
            ([1, 1], 5, False),
            ([2, 4], 6, True),
            ([1, 2, 3], 5, True),
            ([1000000000], 3, False),
            ([6, 6], 6, True),
            ([1, 0], 2, False),
            ([5, 2, 4], 7, True),
            ([1, 2, 12], 6, False),
            ([7, 1, 5], 4, True),
        ],
    )
    def test_check_subarray_sum(self, nums: list[int], k: int, expected: bool):
        result = run_check_subarray_sum(Solution, nums, k)
        assert_check_subarray_sum(result, expected)
