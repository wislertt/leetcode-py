import pytest

from leetcode_py import logged_test

from .helpers import assert_longest_subarray, run_longest_subarray
from .solution import Solution


class TestLongestSubarrayWithMaximumBitwiseAnd:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3, 3, 2, 2], 2),
            ([1, 2, 3, 4], 1),
            ([1], 1),
            ([1000000], 1),
            ([5, 5, 5], 3),
            ([5, 5, 1, 5, 5], 2),
            ([1, 1, 2, 2, 1], 2),
            ([7, 7, 7, 7], 4),
            ([4, 5, 4, 5, 4], 1),
            ([1, 2, 1, 2, 1], 1),
            ([1000000, 1000000, 999999], 2),
            ([3, 3, 2, 2, 3, 3, 3], 3),
            ([6, 6, 7, 7, 7, 6], 3),
            ([1, 2, 3, 4, 5, 6, 7, 8], 1),
            ([9, 9, 9, 1, 9, 9], 3),
            ([2, 2, 2, 2, 2, 2], 6),
            ([10, 20, 20, 10, 10, 20], 2),
            ([1, 1, 1, 1, 1000000, 1], 1),
        ],
    )
    def test_longest_subarray(self, nums: list[int], expected: int):
        result = run_longest_subarray(Solution, nums)
        assert_longest_subarray(result, expected)
