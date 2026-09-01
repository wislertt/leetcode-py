import pytest

from leetcode_py import logged_test

from .helpers import assert_maximum_subarray_sum, run_maximum_subarray_sum
from .solution import Solution


class TestMaximumSumOfDistinctSubarraysWithLengthK:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1, 5, 4, 2, 9, 9, 9], 3, 15),
            ([4, 4, 4], 3, 0),
            ([1, 2, 3], 3, 6),
            ([1, 1, 1], 2, 0),
            ([1], 1, 1),
            ([5], 1, 5),
            ([1, 2, 3, 4, 5], 5, 15),
            ([2, 2, 2, 2], 1, 2),
            ([1, 3, 2, 3, 1], 3, 6),
            ([9, 9, 9, 9], 2, 0),
            ([1, 2, 7, 8, 9, 3, 4], 3, 24),
            ([10, 20, 30, 1, 2], 2, 50),
            ([3, 2, 7, 7, 5], 2, 12),
            ([1, 2, 1, 3, 4], 3, 8),
            ([6], 1, 6),
            ([1, 2, 1], 3, 0),
            ([2, 2, 3], 3, 0),
            ([1, 1], 2, 0),
        ],
    )
    def test_maximum_subarray_sum(self, nums: list[int], k: int, expected: int):
        result = run_maximum_subarray_sum(Solution, nums, k)
        assert_maximum_subarray_sum(result, expected)
