import pytest

from leetcode_py import logged_test

from .helpers import assert_max_subarray_length, run_max_subarray_length
from .solution import Solution


class TestLengthOfLongestSubarrayWithAtMostKFrequency:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1, 2, 3, 1, 2, 3, 1, 2], 2, 6),
            ([1, 2, 1, 2, 1, 2, 1, 2], 1, 2),
            ([5, 5, 5, 5, 5, 5, 5], 4, 4),
            ([1], 1, 1),
            ([1, 2, 3], 1, 3),
            ([1, 1, 1, 1], 3, 3),
            ([2, 2, 2, 2, 2], 5, 5),
            ([1, 2, 1, 3, 4, 3, 3], 2, 6),
            ([1, 4, 4, 3], 1, 2),
            ([1000000000, 1000000000, 7], 1, 2),
            ([3, 1, 2, 1, 2, 3], 2, 6),
            ([4, 5, 4, 5, 4, 5, 6], 2, 5),
            ([1, 2, 3, 4, 5], 1, 5),
            ([9, 9, 1, 9, 9], 2, 3),
            ([7, 7, 7, 1, 1, 1, 7], 3, 6),
            ([1, 4, 2, 5, 4, 1], 3, 6),
            ([1, 5, 4, 4, 5], 3, 5),
            ([5], 1, 1),
            ([3], 1, 1),
            ([2, 2, 4, 3, 1, 4, 3, 5, 5], 5, 9),
            ([1], 1, 1),
            ([3, 2, 3, 4, 5, 5, 1, 2, 5, 2, 5], 5, 11),
            ([1, 3, 3, 4, 1], 2, 5),
            ([5, 2], 2, 2),
            ([2, 2, 2, 2, 3, 4, 3, 5], 7, 8),
        ],
    )
    def test_max_subarray_length(self, nums: list[int], k: int, expected: int):
        result = run_max_subarray_length(Solution, nums, k)
        assert_max_subarray_length(result, expected)
