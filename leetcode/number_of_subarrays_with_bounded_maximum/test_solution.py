import pytest

from leetcode_py import logged_test

from .helpers import assert_num_subarray_bounded_max, run_num_subarray_bounded_max
from .solution import Solution


class TestNumberOfSubarraysWithBoundedMaximum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, left, right, expected",
        [
            ([2, 1, 4, 3], 2, 3, 3),
            ([2, 9, 2, 5, 6], 2, 8, 7),
            ([1], 1, 1, 1),
            ([0], 0, 0, 1),
            ([5], 1, 4, 0),
            ([1000000000], 1000000000, 1000000000, 1),
            ([1, 1, 1], 1, 1, 6),
            ([2, 2, 2], 1, 1, 0),
            ([0, 0, 0], 0, 0, 6),
            ([3, 1, 2, 3], 3, 3, 7),
            ([1, 4, 3, 2, 5], 2, 4, 9),
            ([7, 1, 7, 1, 7], 1, 7, 15),
            ([0, 1, 0, 1, 0], 0, 1, 15),
            ([5, 4, 3, 2, 1], 3, 5, 12),
            ([1, 2, 3, 4, 5, 6], 2, 5, 14),
            ([7, 7, 2, 4, 4, 3, 5, 3], 3, 7, 35),
            ([6, 2], 2, 8, 3),
            ([3, 8], 0, 7, 1),
            ([7, 6], 3, 6, 1),
            ([9, 0, 5, 9, 8, 0, 3, 6], 8, 8, 4),
            ([9, 5, 5, 0, 6, 2, 9, 1, 1], 5, 9, 40),
            ([3, 4, 0], 6, 9, 0),
            ([0, 0, 5, 3, 1, 8], 5, 7, 9),
        ],
    )
    def test_num_subarray_bounded_max(self, nums: list[int], left: int, right: int, expected: int):
        result = run_num_subarray_bounded_max(Solution, nums, left, right)
        assert_num_subarray_bounded_max(result, expected)
