import pytest

from leetcode_py import logged_test

from .helpers import assert_longest_subarray, run_longest_subarray
from .solution import Solution


class TestLongestContinuousSubarrayWithAbsoluteDiffLessThanOrEqualToLimit:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, limit, expected",
        [
            ([8, 2, 4, 7], 4, 2),
            ([10, 1, 2, 4, 7, 2], 5, 4),
            ([4, 2, 2, 2, 4, 4, 2, 2], 0, 3),
            ([5], 0, 1),
            ([5], 10, 1),
            ([1, 1, 1, 1], 0, 4),
            ([1, 2], 0, 1),
            ([1, 2], 1, 2),
            ([2, 1], 1, 2),
            ([3, 1, 4, 1, 5], 0, 1),
            ([1, 5, 6, 7, 8, 10, 6, 5, 6], 0, 1),
            ([1, 3, 6, 6, 6, 9], 2, 3),
            ([10, 9, 8, 7, 6, 5], 2, 3),
            ([1, 2, 3, 4, 5, 6, 7], 3, 4),
            ([4, 8, 5, 1, 7, 9], 3, 2),
            ([9, 9, 9, 1, 1, 1, 9, 9, 9], 0, 3),
            ([1000000000, 1, 999999999], 999999999, 3),
            ([7, 4, 8, 5, 8, 7], 3, 4),
        ],
    )
    def test_longest_subarray(self, nums: list[int], limit: int, expected: int):
        result = run_longest_subarray(Solution, nums, limit)
        assert_longest_subarray(result, expected)
